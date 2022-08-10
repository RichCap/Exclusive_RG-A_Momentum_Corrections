#!/usr/bin/env run-groovy

import org.jlab.jnp.hipo4.io.HipoReader
import org.jlab.jnp.hipo4.data.Bank
import org.jlab.jnp.hipo4.data.Event
import org.jlab.jnp.hipo4.data.SchemaFactory
import groovyx.gpars.GParsPool
import org.jlab.clas.physics.LorentzVector
import org.jlab.jroot.ROOTFile
import uconn.utils.pid.Candidate.Level
import uconn.utils.pid.stefan.ElectronCandidate
import uconn.utils.pid.stefan.PionCandidate
import uconn.utils.pid.stefan.ProtonCandidate
import my.Sugar
import clasqa.QADB

long StartTime = System.nanoTime()

Sugar.enable()

def beam = LorentzVector.withPID(11, 0, 0, 10.6041)
def target = LorentzVector.withPID(2212, 0, 0, 0)

def isinb = ! ( args[0].contains('outb') || args[0].contains('torus+1') )
def ismc = args[0].contains("gemc")

def suff = isinb ? 'inb' : 'outb'
if(ismc) suff += '.mc'
else suff += '.qa'

def outname = args[0].split("/")[-1]
def ff = new ROOTFile("epPipPim.${suff}.${outname}.root")
def tt = ff.makeTree('h22','title','run/I:evn/I:ex:ey:ez:pipx:pipy:pipz:prox:proy:proz:pimx:pimy:pimz:esec:pipsec:prosec:pimsec')


GParsPool.withPool 2,{
    args.eachParallel{fname->
        println(fname)
        QADB qa = new QADB()

        def reader = new HipoReader()
        reader.open(fname)
        def event = new Event()
        def factory = reader.getSchemaFactory()
        def banks = ['RUN::config', 'REC::Event', 'REC::Particle', 'REC::Calorimeter', 'REC::Cherenkov', 'REC::Traj', 'REC::Scintillator'].collect{new Bank(factory.getSchema(it))}

        while(reader.hasNext()) {
            reader.nextEvent(event)
            banks.each{event.read(it)}

            if(banks.every()) {
                def (runb,evb,partb,ecb,ccb,trajb,scb) = banks

                def run = runb.getInt("run", 0)
                def evn = runb.getInt("event", 0)

                if(ismc || qa.OkForAsymmetry(run, evn))
                if(true) {
                    def canele = ElectronCandidate.getElectronCandidate(0, partb, ecb, ccb, trajb, isinb)
                    def ele = canele.getLorentzVector()
                    // def ww = (beam+target-ele).mass()
                    // def Q2 = -(beam-ele).mass2()
                    if(canele.iselectron()) {
                        def pipcans = (0..<partb.getRows()).collect{PionCandidate.getPionCandidate(it, partb, trajb, isinb)}.findAll{it.ispip()}
                        def protcans = (0..<partb.getRows()).collect{ProtonCandidate.getProtonCandidate(it, partb, trajb, isinb)}.findAll{it.isproton()}
                        def pimcans = (0..<partb.getRows()).collect{PionCandidate.getPionCandidate(it, partb, trajb, isinb)}.findAll{it.ispim()}

                        if(pipcans.size() == 1 && protcans.size() == 1 && pimcans.size() == 1) {
                            def canpip = pipcans[0], canprot = protcans[0], canpim = pimcans[0] 
                            def esec = canele.getPCALsector(), pipsec = canpip.getDCsector(), protsec = canprot.getDCsector(), pimsec = canpim.getDCsector()

                                def pip = canpip.getLorentzVector()
                                def prot = canprot.getLorentzVector()
                                def pim = canpim.getLorentzVector()
                                tt.fill(run, evn, ele.px(), ele.py(), ele.pz(),
                                    pip.px(), pip.py(), pip.pz(), prot.px(), prot.py(), prot.pz(), pim.px(), pim.py(), pim.pz(),
                                    esec, pipsec, protsec, pimsec)

                        }
                    }
                }
            }
        }

        reader.close()
    }
}


System.out.println("");



long RunTime = (System.nanoTime() - StartTime)/1000000000;

if(RunTime > 60){
    RunTime = RunTime/60;
    System.out.println("This code's runtime (in min) is: ");
}
else{
    System.out.println("This code's runtime (in sec) is: ");
}

System.out.println(RunTime);


tt.write()
ff.close()

