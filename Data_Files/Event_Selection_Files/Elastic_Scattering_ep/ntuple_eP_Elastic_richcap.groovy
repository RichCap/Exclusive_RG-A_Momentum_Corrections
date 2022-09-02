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
import uconn.utils.pid.stefan.ProtonCandidate.Cut
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


// Files with the name "eP_Elastic_with_CDpro_New" removed the condition for "OkForAsymmetry"
def outname = args[0].split("/")[-1]
def ff = new ROOTFile("eP_Elastic_with_CDpro.${suff}.${outname}.root")
def tt = ff.makeTree('h22','title','run/I:evn/I:ex:ey:ez:prox:proy:proz:esec:prosec')


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
                def (runb, evb, partb, ecb, ccb, trajb, scb) = banks

                def run = runb.getInt("run", 0)
                def evn = runb.getInt("event", 0)

                if(ismc || qa.OkForAsymmetry(run, evn))
                if(true) {
                    def canele = ElectronCandidate.getElectronCandidate(0, partb, ecb, ccb, trajb, isinb)
                    def ele = canele.getLorentzVector()
                    if(canele.iselectron()) {
                        def protcans = (0..<partb.getRows()).collect{ProtonCandidate.getProtonCandidate(it, partb, trajb, isinb)}.findAll{it.isproton(Cut.PID, Cut.CHI2PID, Cut.DC_FIDUCIAL_REG1, Cut.DC_FIDUCIAL_REG2, Cut.DC_FIDUCIAL_REG3, Cut.DELTA_VZ)} // Applying all PID cuts EXCEPT for the requirement to be in the forward detector (i.e., can come from the central detector too)

                        if(protcans.size() == 1) {
                            def canprot = protcans[0]
                            def esec = canele.getPCALsector(), prosec = canprot.getDCsector()

                                def pro = canprot.getLorentzVector()

                                tt.fill(run, evn, ele.px(), ele.py(), ele.pz(),
                                    pro.px(), pro.py(), pro.pz(),
                                    esec, prosec)

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

