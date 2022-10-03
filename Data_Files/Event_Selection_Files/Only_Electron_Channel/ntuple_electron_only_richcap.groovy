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


def outname = args[0].split("/")[-1]
def ff = new ROOTFile("electron_only.${suff}.${outname}.root")
def tt = ff.makeTree('h22','title','run/I:evn/I:ex:ey:ez:esec')


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
                    if(canele.iselectron()){
                        def esec = canele.getPCALsector()
                        tt.fill(run, evn, ele.px(), ele.py(), ele.pz(), esec)
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

