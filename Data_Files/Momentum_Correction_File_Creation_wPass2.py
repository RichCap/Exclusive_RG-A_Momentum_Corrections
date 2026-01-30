import ROOT
import array
from datetime import datetime
import traceback

from CommonPythonFunctions import *
from TextOfCorrectionCode  import *

import sys
from sys import argv
# Let there be 4 arguements in argv when running this code

# Arguement 1: Name of this code (Momentum_Correction_File_Creation_wPass2.py)


# Arguement 2: data-type (In/Out)
    # Options: 
    # 1) In -> Inbending
    # 2) Out -> Outbending
    
    
# Arguement 3: event-type (type of exclusive events)
    # Options: 
    # 1) SP    -> Single Pion (i.e., ep->eπ+N)
        # Should also run with EO to complete the full set of requirements for preforming the electron corrections
    # 2) DP    -> Double Pion (i.e., ep->epπ+π-)
    # 3) P0    -> Pi0 Channel (i.e., ep->epπ0)
    # 4) ES    -> Elastic Scattering (i.e., ep->e'p')
    # 4) EO    -> Electron Only (i.e., ep->e'X)
        # Should also run with SP to complete the full set of requirements for preforming the electron corrections
    # 5) MC    -> Simulated Single Pion (i.e., ep->eπ+N  - same option as SP but file names will be different)
    # 6) P0_MC -> Simulated Pi0 (i.e., ep->epπ0 - same option as P0 but using simulated files - has two additional options with P0_MC_P and P0_MC_M modifying the momentum of the proton by ±20 MeV)
    
    # NOTE: All options above default to the Fall 2018 Pass 1 versions of this code.
    # #     To use the Spring 2019 versions of the channels listed, add 'P1' (for Pass 1) or 'P2' (for Pass 2) to run either version of the Spring 2019 data.
    # #     For the Fall 2018 Pass 2 versions of the channels, add 'fp2' (for Fall data Pass 2) to this arguement.

    
# Arguement 4: file number (Full file name/path)
    # If the file number is given as 'All', then all files will be run instead of a select number of them
    # If the file number is given as 'test' or 'Test', then the code will run without saving any of the histograms
    # If the file number is given as 'time', then the code will run without saving any of the histograms (like with the option 'test') BUT will set CheckDataFrameQ = 'y' (See below for details on what this does)
    # Otherwise, input the path to the file to be processed
        # The lines of code which read as 'file_name = str(file_name.replace(' are meant to replace the full string of the file's path with the number to name this code's output (based on the input file)
        # Some of these lines are in place for backwards compatibility (may remove some if known to be unnecessary) - MUST ADD new lines when new directories are to be referrenced (do before running)
    

# EXAMPLES: 
    # python3 Momentum_Correction_File_Creation_wPass2.py In SP All
        # The line above would run ALL INBENDING (Fall 2018 Pass 1) files together for the ep->eπ+N channel
    # python3 Momentum_Correction_File_Creation_wPass2.py In P2EO All
        # The line above would run ALL INBENDING (Spring 2019 Pass 2) files together for the ep->e'X channel
    # python3 Momentum_Correction_File_Creation_wPass2.py Out fa2SP All
        # The line above would run ALL OUTBENDING (Fall 2018 Pass 2) files together for the ep->eπ+N channel
    # python3 Momentum_Correction_File_Creation_wPass2.py Out DP test
        # The line above would test-run the OUTBENDING files for the ep->epπ+π- channel (no results would be saved)
        
        
        
code_name, datatype, event_type, file_location = argv

datatype, file_location, event_type = ''.join([str(datatype), "bending"]), str(file_location), str(event_type)

file_name = str(file_location)


pass_version = "NA"
Beam_Energy = 10.6041 # Fall 2018 Beam Energy

if(("_MC" not in event_type) and (event_type not in ["MC"])):
    # Spring 2019 Data sets
    if("P1" in event_type):
        pass_version = "Spring 2019 - Pass 1"
        Beam_Energy = 10.1998
    if("P2" in event_type):
        pass_version = "Spring 2019 - Pass 2"
        Beam_Energy = 10.1998
    if("fa2" in event_type):
        pass_version =   "Fall 2018 - Pass 2"
        Beam_Energy = 10.6041 if("MC" not in event_type) else 10.6 # MC Beam Energy
    if(("C" in event_type) and ("MC" not in event_type)):
        pass_version = "".join([pass_version, " - Central Detector"])
    if("F" in event_type):
        pass_version = "".join([pass_version, " - Forward Detector"])
    
    if("MC" not in event_type):
        event_type = str(((((event_type.replace("P1", "")).replace("P2", "")).replace("C", "")).replace("F", "")).replace("fa2", ""))
    else:
        event_type =  str((((event_type.replace("P1", "")).replace("P2", "")).replace("F", "")).replace("fa2", ""))
    
    
# Normal values used (rounded)
Particle_Mass_Neutron = 0.9396
Particle_Mass_Proton  = 0.938
Particle_Mass_PiC     = 0.13957    # Mass of Charged Pions (same for pi+ and pi-)
Particle_Mass_Pi0     = 0.13498

# if("_MC" in event_type):
#     # # Exact values used by PDGParticle (see: https://github.com/JeffersonLab/clas12-offline-software/blob/516f47374b25c86d4e65cbeb1009c3422906949a/common-tools/clas-physics/src/main/java/org/jlab/clas/pdg/PDGDatabase.java#L31)
#     Particle_Mass_Neutron = 0.9396
#     Particle_Mass_Neutron = 0.939565379
#     Particle_Mass_Proton  = 0.938
#     # Particle_Mass_Proton  = 0.938272046
#     Particle_Mass_PiC     = 0.13957    # Mass of Charged Pions (same for pi+ and pi-)
#     Particle_Mass_PiC     = 0.13957018 # Mass of Charged Pions (same for pi+ and pi-)
#     Particle_Mass_Pi0     = 0.13498
#     Particle_Mass_Pi0     = 0.1349766
#     print("".join(["Setting Masses as:\nParticle_Mass_Neutron = ", str(Particle_Mass_Neutron), "\nParticle_Mass_Proton  = ", str(Particle_Mass_Proton), "\nParticle_Mass_PiC     = ", str(Particle_Mass_PiC), "\nParticle_Mass_Pi0     = ", str(Particle_Mass_Pi0)]))


####################################################################################################################################################################   
# Setting proper value for file_name

file_name = str(file_name.replace("/work/clas12/shrestha/clas12momcorr/utsav/dataFiles/inbending/ePipX/epip.skim4_00", ""))
file_name = str(file_name.replace("/work/clas12/shrestha/clas12momcorr/utsav/dataFiles/outbending/ePipX/skim4_00", ""))
    
file_name = str(file_name.replace("".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Double_Pion_Channel_eppippim/", str(datatype), "/"]), ""))
file_name = str(file_name.replace("".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Single_Pion_Channel_epipN/", str(datatype), "/"]), ""))
file_name = str(file_name.replace("".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/", str(datatype), "/"]), ""))
file_name = str(file_name.replace("".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/Valerii_Files/"]), ""))
    
file_name = str(file_name.replace("eP_Elastic.inb.nSidis_00", ""))
file_name = str(file_name.replace("eP_Elastic.outb.nSidis_00", ""))


file_name = str(file_name.replace("eP_Elastic_with_CDpro.inb.nSidis_00", ""))
file_name = str(file_name.replace("eP_Elastic_with_CDpro.outb.nSidis_00", ""))


file_name = str(file_name.replace("eP_Elastic_with_CDpro_New.inb.nSidis_00", ""))
file_name = str(file_name.replace("eP_Elastic_with_CDpro_New.outb.nSidis_00", ""))


file_name = str(file_name.replace("eP_Elastic_with_CDpro_New.inb.skim4_00", ""))
file_name = str(file_name.replace("eP_Elastic_with_CDpro_New.outb.skim4_00", ""))

    
file_name = str(file_name.replace("eP_Elastic_with_CDpro.inb.skim4_00", ""))
file_name = str(file_name.replace("eP_Elastic_with_CDpro.outb.skim4_00", ""))

file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/richcap/SIDIS_Analysis/Data_Files_Groovy/Matched_REC_MC/MC_Matching_sidis_epip_richcap.inb.45nA_job_", "")).replace(".hipo.root", "")

file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Only_Electron_Channel/electron_only.inb.skim4_00", ""))
file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Only_Electron_Channel/electron_only.inb.qa.skim4_00", ""))

file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Single_Pion_Channel_epipN/Inbending/ePip.inb.qa.nSidis_00", ""))

file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Single_Pion_Channel_epipN/Inbending_skim4/ePip.inb.qa.", ""))

file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Spring2019/Pass1/Inbending_nSidis/ePip.pass1.inb.qa.nSidis_00", ""))
file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Spring2019/Pass2/Inbending_nSidis/ePip.pass2.inb.qa.nSidis_00", ""))

file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Spring2019/Pass1/Inbending/ePip.pass1.inb.qa.MissingNeutron_00", ""))
file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Spring2019/Pass2/Inbending/ePip.pass2.inb.qa.MissingNeutron_00", ""))

file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Double_Pion_Channel_eppippim/Inbending_skim4/epPipPim.inb.qa.skim4_00", ""))


file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Central_Tracking/Pass1/Inbending/ePip.Central.pass1.inb.qa.nSidis_00", ""))
file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Central_Tracking/Pass2/Inbending/ePip.Central.pass2.inb.qa.nSidis_00", ""))


file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Inbending_skim4/ePip.inb.qa.skim4_00", ""))

file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Pi0_MC/lvl2_", ""))

file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/Inbending_nSidis/ePip.pass2.inb.qa.", ""))
file_name = str(file_name.replace("nSidis_00", "nSidis_"))

file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Outbending_skim4/ePip.outb.qa.rec_clas_005449.evio.0",        ""))
file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Only_Electron_Channel/Outbending/electron_only.outb.qa.rec_clas_005449.evio.0",         ""))
file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Elastic_Scattering_ep/Outbending/eP_Elastic_with_CDpro.outb.qa.rec_clas_005449.evio.0", ""))

file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Outbending_skim4/ePip.outb.qa.rec_clas_00",        ""))
file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Only_Electron_Channel/Outbending/electron_only.outb.qa.rec_clas_00",         ""))
file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Elastic_Scattering_ep/Outbending/eP_Elastic_with_CDpro.outb.qa.rec_clas_00", ""))


file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/Inbending_nSidis/Complete/ePip.pass2.inb.qa.nSidis_",                                ""))
file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/Inbending_nSidis/Complete/Only_Electron_Channel/electron_only.pass2.inb.qa.nSidis_", ""))

file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/Inbending_recon/Single_Pion_Channel_epipN/ePip.pass2.inb.qa.rec_clas_00",      ""))
file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/Inbending_recon/Only_Electron_Channel/electron_only.pass2.inb.qa.rec_clas_00", ""))

file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass1/Inbending_recon/Single_Pion_Channel_epipN/ePip.pass1.inb.qa.rec_clas_00",      ""))
file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass1/Inbending_recon/Only_Electron_Channel/electron_only.pass1.inb.qa.rec_clas_00", ""))


file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Outbending/Single_Pion_Channel_epipN/ePip.wCentral.pass2.outb.Fa18.rec_clas_00", ""))
file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Outbending/Only_Electron_Channel/electron_only.pass2.outb.Fa18.rec_clas_00",     ""))


file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Outbending/Single_Pion_Channel_epipN/ePip.wCentral.pass2.outb.qa.Fa18.rec_clas_00", ""))
file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Outbending/Only_Electron_Channel/electron_only.pass2.outb.qa.Fa18.rec_clas_00",     ""))

file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Inbending/Single_Pion_Channel_epipN/ePip.wCentral.pass2.inb.qa.Fa18.rec_clas_00", ""))
file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Inbending/Only_Electron_Channel/electron_only.pass2.inb.qa.Fa18.rec_clas_00",     ""))

file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/SIDIS/Matched_REC_MC/MC_Matching_sidis_epip_richcap.inb.qa.45nA_job_", ""))
file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/SIDIS/Matched_REC_MC/With_BeamCharge/Pass2/More_Cut_Info/MC_Matching_sidis_epip_richcap.inb.qa.new4.inb-clasdis_", ""))
file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/SIDIS/Matched_REC_MC/With_BeamCharge/Pass2/More_Cut_Info/MC_Matching_sidis_epip_richcap.inb.qa.new5.inb-clasdis",  ""))

file_name = str(file_name.replace("/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Outbending/Only_Electron_Channel/electron_only.pass2.outb.qa.Fa18.rec_clas_00", ""))

file_name = str(file_name.replace("-", "_")).replace(".hipo.root", "")
file_name = str(file_name).replace(".evio.root", "")
file_name = str(file_name).replace(".root", "")

####################################################################################################################################################################

    
ROOT.gStyle.SetTitleOffset(1.3, 'y')
ROOT.gStyle.SetGridColor(17)
ROOT.gStyle.SetPadGridX(1)
ROOT.gStyle.SetPadGridY(1)

    
####################################################################################################################################################################
# The following lines of code are used for determining which/how plots are made/named

event_Name = "error"

if(event_type == "E0"):
    print("".join([color.RED, "ERROR: E0 is not the correct input type...", color.END, "\n\tSetting to event_type = EO"]))
    event_type = "EO"


if(event_type in ["SP", "MC", "SIDIS"]):
    event_Name = "Single Pion Channel"
    MM_type = "epipX"
    print(MM_type)
else:
    print(f"event_type = {event_type}")
    
if(event_type == "DP"):
    event_Name = "Double Pion Channel"
    # # Missing Mass Choice:
    MM_type = "eppipX"
    # MM_type = "eppippim"
    # MM_type = "eppimX"
    # MM_type = "epippimX"
    
if("P0" in event_type):
    event_Name = "Pi0 Channel"
    if("MC" in event_type):
        event_Name  = "".join(["(MC) Pi0 Channel", " (+20 MeV)" if("MC_P" in event_type) else " (-20 MeV)" if("MC_M" in event_type) else " (GEN)" if("_Gen" in event_type) else ""])
        event_type  = "P0"
        Beam_Energy = 10.6 # MC Beam Energy

    MM_type = "eppi0X"
    MM_type = "epX"
    
if(event_type == "ES"):
    event_Name = "Elastic Scattering"
    MM_type = "epX"
    
if(event_type == "EO"):
    event_Name = "Electron Only"
    MM_type = "eX"

####################################################################################################################################################################    





####################################################################################################################################################################
# The following lines set the number of bins/axis ranges for the histograms made by this file (pre-set based on event channel for consistency)

if(MM_type == "epippimX"):
    Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max = 160, 0, 1
elif(MM_type == "epipX"):
    Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max = 200, 0.5, 1.2
elif(event_type != "ES"):
    # Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max = 160, -0.5, 0.5
    # Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max = 200, -0.5, 0.5
    Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max = 310, -0.3175, 0.3025
    Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max = 320, -0.3275, 0.3125
else:
    Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max = 120, -0.1, 0.1

# if("MC" in event_Name):
#     Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max = 200, 0.01, 0.03
    
#################################################################################################################################################################### 


if(event_Name != "error"):
    
    print("".join([color.BBLUE, "\n\n\nStarting ", str(event_Name), " ", str(datatype), "...\n", color.END]))
    
    if(pass_version != "NA" and pass_version != ""):
        print("".join(["\n", color.BBLUE, "RUNNING FILES FROM: ", str(pass_version), "\n", color.END]))
        
    print("".join(["Initial Beam Energy is given as: ", color.BOLD, str(Beam_Energy), " GeV", color.END, "\n"]))

    # These lines are left over from older versions of the code. Do not change or remove them without editing all other parts of code that reference them.
    CutChoice, CutChoice_2 = 'none', 'none'
    if(event_type == "ES"):
        CutChoice = "".join(["""
            // For ∆Phi Cuts:
            auto Beam_Energy = """, str(Beam_Energy), """;
            auto Proton_Mass = """, str(Particle_Mass_Proton), """;//0.938;
            auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
            auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
            auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);

            auto el_Phi = (180/3.1415926)*atan2(ey, ex);
            auto pro_Phi = (180/3.1415926)*atan2(proy, prox);
            if(el_Phi < 0){el_Phi += 360;}
            if(pro_Phi < 0){pro_Phi += 360;}
            double Cut_Upper = 183;
            double Cut_Lower = 177;
            auto Cut_Variable = abs(el_Phi - pro_Phi);

            if(esec == 1){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 181.23;
                    Cut_Lower = 178.75;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 181.16;
                    Cut_Lower = 178.8;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 181.14;
                    Cut_Lower = 178.84;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 181.17;
                    Cut_Lower = 178.79;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 181.38;
                    Cut_Lower = 178.66;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 181.61;
                    Cut_Lower = 178.35;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 182.37;
                    Cut_Lower = 177.77;
                }
            }
            if(esec == 2){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 181.47;
                    Cut_Lower = 179.06;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 181.45;
                    Cut_Lower = 179.03;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 181.53;
                    Cut_Lower = 179.05;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 181.5;
                    Cut_Lower = 179.2;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 181.69;
                    Cut_Lower = 179.26;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 181.93;
                    Cut_Lower = 179.03;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 182.43;
                    Cut_Lower = 177.64;
                }
            }
            if(esec == 3){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 181.56;
                    Cut_Lower = 179.2;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 181.68;
                    Cut_Lower = 179.09;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 181.62;
                    Cut_Lower = 179.15;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 181.63;
                    Cut_Lower = 179.26;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 181.76;
                    Cut_Lower = 179.25;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 181.81;
                    Cut_Lower = 179.15;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 181.96;
                    Cut_Lower = 178.08;
                }
            }
            if(esec == 4){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 181.35;
                    Cut_Lower = 178.63;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 181.74;
                    Cut_Lower = 178.14;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 181.59;
                    Cut_Lower = 178.24;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 181.69;
                    Cut_Lower = 178.22;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 181.93;
                    Cut_Lower = 177.93;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 182.05;
                    Cut_Lower = 178.05;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 182.13;
                    Cut_Lower = 177.77;
                }
            }
            if(esec == 5){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 181.06;
                    Cut_Lower = 178.6;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 180.92;
                    Cut_Lower = 178.52;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 180.94;
                    Cut_Lower = 178.52;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 180.89;
                    Cut_Lower = 178.43;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 180.88;
                    Cut_Lower = 178.47;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 181.1;
                    Cut_Lower = 178.32;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 182.47;
                    Cut_Lower = 178.04;
                }
            }
            if(esec == 6){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 181.26;
                    Cut_Lower = 178.78;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 181.33;
                    Cut_Lower = 178.71;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 181.14;
                    Cut_Lower = 178.68;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 181.07;
                    Cut_Lower = 178.53;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 180.93;
                    Cut_Lower = 178.51;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 181.32;
                    Cut_Lower = 178.16;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 182.42;
                    Cut_Lower = 177.81;
                }
            }
            return ((Cut_Variable < Cut_Upper) && (Cut_Variable > Cut_Lower));
        """])
        CutChoice_2 = "".join(["""
            // For ∆Theta Cuts:
            auto Beam_Energy = """, str(Beam_Energy),""";
            auto Proton_Mass = """, str(Particle_Mass_Proton), """;//0.938;
            auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
            auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
            auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
            auto proC = ROOT::Math::PxPyPzMVector(prox, proy, proz, Proton_Mass);
            auto Pro_Th_Calc = atan(Proton_Mass/((Beam_Energy + Proton_Mass)*tan(eleC.Theta()/2)))*(180/3.1415926);
            auto Cut_Variable = ((proC.Theta())*(180/3.1415926)) - Pro_Th_Calc;
            double Cut_Upper = 5;
            double Cut_Lower = -5;
            if(esec == 1){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 0.4;
                    Cut_Lower = -0.26;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 0.39;
                    Cut_Lower = -0.3;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 0.42;
                    Cut_Lower = -0.29;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 0.48;
                    Cut_Lower = -0.31;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 0.55;
                    Cut_Lower = -0.39;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 0.69;
                    Cut_Lower = -0.52;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 1.12;
                    Cut_Lower = -1.0;
                }
            }
            if(esec == 2){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 0.4;
                    Cut_Lower = -0.21;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 0.45;
                    Cut_Lower = -0.25;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 0.48;
                    Cut_Lower = -0.27;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 0.52;
                    Cut_Lower = -0.26;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 0.58;
                    Cut_Lower = -0.28;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 0.71;
                    Cut_Lower = -0.39;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 1.17;
                    Cut_Lower = -0.9;
                }
            }
            if(esec == 3){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 0.4;
                    Cut_Lower = -0.22;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 0.43;
                    Cut_Lower = -0.27;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 0.47;
                    Cut_Lower = -0.29;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 0.52;
                    Cut_Lower = -0.28;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 0.58;
                    Cut_Lower = -0.29;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 0.65;
                    Cut_Lower = -0.35;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 1.02;
                    Cut_Lower = -0.71;
                }
            }
            if(esec == 4){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 0.38;
                    Cut_Lower = -0.27;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 0.49;
                    Cut_Lower = -0.28;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 0.52;
                    Cut_Lower = -0.28;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 0.54;
                    Cut_Lower = -0.27;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 0.61;
                    Cut_Lower = -0.32;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 0.65;
                    Cut_Lower = -0.38;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 1.17;
                    Cut_Lower = -0.9;
                }
            }
            if(esec == 5){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 0.34;
                    Cut_Lower = -0.26;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 0.4;
                    Cut_Lower = -0.31;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 0.46;
                    Cut_Lower = -0.35;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 0.49;
                    Cut_Lower = -0.37;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 0.47;
                    Cut_Lower = -0.4;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 0.51;
                    Cut_Lower = -0.49;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 1.02;
                    Cut_Lower = -1.0;
                }
            }
            if(esec == 6){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 0.37;
                    Cut_Lower = -0.31;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 0.4;
                    Cut_Lower = -0.36;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 0.43;
                    Cut_Lower = -0.38;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 0.44;
                    Cut_Lower = -0.36;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 0.46;
                    Cut_Lower = -0.4;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 0.65;
                    Cut_Lower = -0.56;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 0.97;
                    Cut_Lower = -0.99;
                }
            }
            return ((Cut_Variable < Cut_Upper) && (Cut_Variable > Cut_Lower));
        """])


####################################################################################################################################################################
    # The following lines are used to manually select which types of histograms are run (and turn off those not related to the event type selected)
    ##################################################################################
    ##=====##=====##=====##     Choices for Initial Set-Up     ##=====##=====##=====##
    ##################################################################################

    # See_Num_of_Events_Q = 'y'
    See_Num_of_Events_Q = 'n'


    # Run (any) Delta P Histograms? (Use Delta_P_histo_Q to set answer)
    # Delta_P_histo_Q = 'n'
    Delta_P_histo_Q = 'y'

    Delta_Pel_histo_Q, Delta_Pip_histo_Q, Delta_Pim_histo_Q, Delta_Pro_histo_Q = 'n', 'n', 'n', 'n'

    if(Delta_P_histo_Q == 'y'):
        # Run ∆P (Electron) Histograms? (Use Delta_Pel_histo_Q to set answer)
        Delta_Pel_histo_Q = 'y'
        
        # Run ∆P (π+ Pion) Histograms? (Use Delta_Pip_histo_Q to set answer)
        Delta_Pip_histo_Q = 'y'
        
        # Run ∆P (π- Pion) Histograms? (Use Delta_Pim_histo_Q to set answer)
        # Delta_Pim_histo_Q = 'y'
        
        # Run ∆P (Proton) Histograms? (Use Delta_Pro_histo_Q to set answer)
        Delta_Pro_histo_Q = 'y'

    else:
        Delta_Pel_histo_Q, Delta_Pip_histo_Q, Delta_Pim_histo_Q, Delta_Pro_histo_Q = 'n', 'n', 'n', 'n'
        
        
    if(event_type in ["SP", "SP_P1", "SP_P2", "MC", "SIDIS"]):
        Delta_Pim_histo_Q, Delta_Pro_histo_Q = 'n', 'n'
    if(event_type == "DP"):
        Delta_Pel_histo_Q, Delta_Pip_histo_Q = 'n', 'n'
    if(event_type == "P0"):
        Delta_Pel_histo_Q, Delta_Pim_histo_Q, Delta_Pip_histo_Q = 'n', 'n', 'n'
    if(event_type == "ES"):
        Delta_Pim_histo_Q, Delta_Pip_histo_Q, Delta_Pro_histo_Q = 'n', 'n', 'n' # The proton corrections are turned off for now
    if(event_type == "EO"):
        Delta_Pim_histo_Q, Delta_Pip_histo_Q, Delta_Pro_histo_Q = 'n', 'n', 'n'

        
    # if(Delta_P_histo_Q != 'n'):
    #     if(Delta_Pel_histo_Q != 'n'):
    #         print("Running with ∆P(el) histograms.")
    #     if(Delta_Pip_histo_Q != 'n'):
    #         print("Running with ∆P(π+) histograms.")
    #     if(Delta_Pim_histo_Q != 'n'):
    #         print("Running with ∆P(π-) histograms.")
    #     if(Delta_Pro_histo_Q != 'n'):
    #         print("Running with ∆P(pro) histograms.")
    # else:
    #     print("\033[1mNOT running ∆P histograms.\033[0m")


    # Print rdf information? (Letting CheckDataFrameQ = 'y' will print out every variable name available for plotting within the dataframe)
    # Option does not affect the histograms that can/will be made. Purely provides user with more information while coding

    CheckDataFrameQ = 'n'
    if("time" == file_location):
        CheckDataFrameQ = 'y'
    else:
        CheckDataFrameQ = 'n'
    # CheckDataFrameQ = 'y'


    ########################################################################################
    ##=====##=====##=====##     Choices for Initial Set-Up (End)     ##=====##=====##=====##
    ########################################################################################
    
####################################################################################################################################################################





    ##########################################################################
    ##=====##=====##=====##     Choices for Saving     ##=====##=====##=====##
    ##########################################################################
    SaveResultsQ = 'yes'
    # SaveResultsQ = 'no'

    if(file_location in ["Test", "test", "time"]):
        SaveResultsQ = 'no'

    if(SaveResultsQ == 'no'):
        print(f"{color.BOLD}Not saving results...{color.END}")
    else:
        print(f"{color.BOLD}Results WILL be saved{color.END}")


    Extra_Part_of_Name = "_New_Python_Script"
    # First name for the new script (just a placeholder)
                
    if("Fall" in pass_version):
        Extra_Part_of_Name = "_Fall_Pass2_V1"
        # Initial tests of the Pass 2 Fall 2018 datasets
            
        Extra_Part_of_Name = "_Fall_Pass2_V2"
        # Ran on 1/24/2024
            # Fixed issue with the Central/Forward/Status cuts
            
        Extra_Part_of_Name = "_Fall_Pass2_V3"
        # Ran on 2/7/2024
            # Adjusted definition of the pipPhi variable
            # Redefined pipsec for the central detector - Now up to 12 sectors total (6 forward + 6 central)
            
        Extra_Part_of_Name = "_Fall_Pass2_V4"
        # Ran on 2/9/2024
            # Adjusted definition of the pipPhi variable (again)
            # Redefined pipsec for the central detector - Based on Ricardo's notes
            # Adjusted the phi shift function to be unique for the central detector particles
            # Added Stefan's Pi+ Energy Loss Corrections to the correction lists
                # Use the naming convension of '_ELPipMM' instead of just '_PipMM' to add the energy loss corrections to the Pi+ pions following this update
                # Only applies to Pass 2 files
            # Running this version with a new set of python files (updated structure - same basic code)
                # Removed a lot of unnecessary code that was no longer useful (cleaned this file up)
                # Some old corrections may no longer be available
            # Default option is to now run the same list of corrections for both the ∆P and MM plots (used to have to define the lists separately)
                # Use the 'automatic_MM_cor_select' variable to run the code to select options as it previously did
            # Updated the Fall 2018 Pass 2 Outbending files to be used by this code (includes QADB now)
            
            
        Extra_Part_of_Name = "_Shift_Test_V1"
        # Ran on 2/16/2024
            # Adjusted the phi shift function of the central detector (attempting to maximize my ability to create sector definitions)
            # Turned off all corrections and Missing Mass Plots (just interested in the phase space plots for this test)
            # Double the number of bins in the Phi vs P plots
            # Made the 'reg1' phi bin of the central detector pions the intergated phi bin (i.e., there are no phi bins yet for the central detector pions)
            
        Extra_Part_of_Name = "_Shift_Test_V2"
        # Ran on 2/16/2024
            # Adjusted Central Detector Sector definition
            
            
        Extra_Part_of_Name = "_Shift_Test_V3"
        # Ran on 2/16/2024
            # Adjusted Central Detector Sector definition (using the shifted phi angle)
            # Making all normal Missing Mass plots (did not run the corrections)
            
            
        Extra_Part_of_Name = "_Shift_Test_V4"
        # Ran on 2/16/2024
            # Fixed Central Detector Sector definition using the shifted phi angle
                # Needed to account for Phi > 360 (assigned to sector 7 and shifted down by 360)
            # Running with all corrections
            
            
        Extra_Part_of_Name = "_Shift_Test_V5"
        # Ran on 2/19/2024
            # Testing new shift to localize the phi bins better
            
            
        Extra_Part_of_Name = "_In_Forward_Test_V1"
        # Ran on 2/26/2024
            # Starting Corrections on Inbending Pass 2 Fall 2018 Data
            # Includes Stefan's Pi+ Energy Loss Correction
            
            
            
        Extra_Part_of_Name = "_Fall2018_P2_Test_V1"
        # Ran on 3/20/2024
            # Running Corrections on Inbending Pass 2 Fall 2018 Data (Single Pion and Electron Only)
                # Using updated versions of the files (nothing added yet - just fixed some minor issues related to incomplete files)
                # Updated the Exclusivity Cuts for SP and EO (Fall 2018 Pass 2 Inbending)
            # Includes Stefan's Pi+ Energy Loss Correction
            
            
        Extra_Part_of_Name = "_Fall2018_P2_Test_V2"
        # Ran on 3/21/2024
            # Created new Fall 2018 Pass 2 Electron Correction
                # Removed other Pass 1 corrections
                # Correction is named: "mmfaP2"
                
                
        Extra_Part_of_Name = "_Fall2018_P2_Test_V3"
        # Ran on 3/21/2024
            # Refined the new Fall 2018 Pass 2 Electron Correction
                # Correction is still named: "mmfaP2"
                
                
        Extra_Part_of_Name = "_Fall2018_P2_Test_V4"
        # Ran on 3/22/2024
            # Refined the new Fall 2018 Pass 2 Electron Correction
                # Correction is still named: "mmfaP2"
                # Changed some of the fit ranges for the SP ∆P fits for this refinement (momentum range is shifted back 0.05 GeV and the 1D fits have shorter ranges of ∆P to fit)
            # Will also be using the reworked EO files (should be much larger due the QADB not being updated yet for Pass 2)
        
        
        Extra_Part_of_Name = "_Fall2018_P2_Test_V5"
        # Ran on 3/22/2024
            # Creating initial Fall 20018 Pass 2 Pi+ Correction (called 'PipMMfaP2')
            
            
        Extra_Part_of_Name = "_Fall2018_P2_Test_V6"
        # Ran on 3/25/2024
            # Creating refinement of the Fall 20018 Pass 2 Pi+ Correction (still called 'PipMMfaP2')
            
        Extra_Part_of_Name = "_Fall2018_P2_Test_V7"
        # Ran on 3/25/2024
            # More refinements for the Fall 20018 Pass 2 Pi+ Correction (still called 'PipMMfaP2')
            # Also turned off the phase space plots to save time while running
                # i.e., Run_Phase_Space = 'no'
                
                
        Extra_Part_of_Name = "_Fall2018_P2_Test_V8"
        # Ran on 3/26/2024
            # More refinements for the Fall 20018 Pass 2 ELECTRON Correction (still called 'mmfaP2')
                # Refined the electron based on the latest version of the Pi+ correction (from Extra_Part_of_Name = "_Fall2018_P2_Test_V7")
            # Still turned off the phase space plots to save time while running
                # i.e., Run_Phase_Space = 'no'
                
                
        Extra_Part_of_Name = "_Fall2018_P2_Test_V9"
        # Ran on 3/26/2024
            # More refinements for the Fall 20018 Pass 2 Pi+ Correction (still called 'PipMMfaP2')
            # Removed Correction Options where the Pi+ Momentum Corrections are applied without the Energy Loss Corrections (always applying them together now - mainly done for faster run-time)
            # Still turned off the phase space plots to save time while running
                # i.e., Run_Phase_Space = 'no'
                
                
        Extra_Part_of_Name = "_Fall2018_P2_Theta_V1"
        # Ran on 4/15/2024
            # Corrections are identical to those used in Extra_Part_of_Name = "_Fall2018_P2_Test_V9" but new plots have been added to examine the theta dependence of the ∆P and MM plots
            # Still turned off the phase space plots to save time while running
                # i.e., Run_Phase_Space = 'no'
                
                
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V1"
        # Ran on 7/12/2024
            # Developing New Outbending Pass 2 Corrections for Fall 2018 data
                # Making Forward Detector Corrections Only
            # Using the default options that should be the same as used by Extra_Part_of_Name = "_Fa18_P2_MC_V1" (but not for MC files)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V2"
        # Ran on 7/17/2024
            # Turned off pion plots, old momentum corrections, and Delta p vs theta plots
                # Possible size/memory issue was occuring in the notebook code, so this reduction is aimed at (hopefully) reducing the likelihood of the notebook crashing and reseting
                # Only using Energy loss correction (no new corrections/cuts from '_Fall2018_P2_New_Out_V1')
            # Also running elastic scattering channel (will need new cuts for '_Fall2018_P2_New_Out_V3')
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V3"
        # Ran on 7/17/2024
            # Still having issues with loading the files: Missing Mass vs Theta plots have now also been removed
            # Updated the elastic scattering channel cuts
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V4"
        # Ran on 7/22/2024
            # Earlier issues with loading the files seems to have nothing to do with removed histograms
                # Issue seems to be related to the version of ROOT used by this code and the Jupyter Notebook
                    # Work-around found by moving the Notebook code into individual python scripts (see 'Run_With_Python' folder)
                # Still using the reduced histogram options to increase the speed at which this code runs while the new electron corrections are being developed (i.e., no pion plots are being made)
            # Updated the elastic scattering/Single Pion channel cuts (based on "_Fall2018_P2_New_Out_V2")
                # Made with new 'Run_With_Python' scripts (images and cuts saved in that folder)
                
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V5"
        # Ran on 7/22/2024
            # Added new (Outbending) Electron Momentum Correction (called "mmfaP2")
                # Includes 3 points from EO channel instead of just 1
            # Running with Pion plots again
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V6"
        # Ran on 7/23/2024
            # Refined the (Outbending) Electron Momentum Correction (still called "mmfaP2")
                # Includes 2 points from EO channel instead of just 3, and modified the error bars of the EO channel to be 1.5 times bigger than the SP channel to be more balanced between the two - SP is more important than EO)
            # Running with Pion plots still (may move to pion corrections if the refinement continues to perform well)
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V7"
        # Ran on 7/23/2024
            # Added new (Outbending) Pi+ Pion Momentum Correction (called "PipMMfaP2")
                # Fits for Electron Corrections may need to be checked again in case refinement is still needed (w/out pion correction) but the correction was applied in case the electrons were done
                    # The Missing Mass electron fits may need some improvements, but the Delta P plots generally looked like they would not improve much unless more of the EO channel was removed
            # Failed to add the Missing Mass vs pion plots to last version (issue fixed here)
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V8"
        # Ran on 7/24/2024
            # Refined the (Outbending) Pi+ Pion Momentum Correction (still called "PipMMfaP2")
                # Original Correction performed VERY poorly - hoping that the refinement fixes whatever issue caused the corrections to get worse
                    # Last correction had worse (more) momentum dependence, but better (less) phi dependence for the pion
                    
                    
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V9"
        # Ran on 7/24/2024
            # Refined the (Outbending) Pi+ Pion Momentum Correction again (still called "PipMMfaP2")
                # Last refinement worked a lot better but was not yet perfect - hoping that this refinement will help to start finishing the job
                
                
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V10"
        # Ran on 7/25/2024
            # Refined the (Outbending) Electron Momentum Correction again (after the pion corrections were applied)
                # Last pion refinement worked very well (to the point that refining the electron seemed to be the more potentially impactful choice over another pion refinement)
                # All corrections maintain the same names/fitting process as were used in the prior refinements
            # Reran with Run_Phase_Space = 'yes' (i.e., Running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V11"
        # Ran on 7/26/2024
            # Refined the (Outbending) Electron Momentum Correction again (did not apply the pion corrections)
                # The last electron correction did not perform well enough with the pion correction to justify how it now performed without it
                # The new refinement is designed without the pion correction included, but will hopefully be small enough to not force the pion correction to be completely reset (new refinement is very likely)
                # All corrections maintain the same names/fitting process as were used in the prior refinements
            # Updated the W-cuts for the EO channel
                # Cuts are now tighter to (hopefully) improve the elastic ∆P fits
            # Ran with Run_Phase_Space = 'no' (i.e., NOT running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V12"
        # Ran on 7/31/2024
            # Refined the (Outbending) Electron Momentum Correction again (did not apply any of the pion corrections)
                # Applying the pion energy loss correction before the electron correction makes the elastic scattering channel and the single pion channel incompatible with each other (electron corrections will be better if the electron is corrected by itself first)
                    # Will DEFINITELY need to rerun the pion corrections after this version
                # All corrections maintain the same names/fitting process as were used in the prior refinements
            # Ran with Run_Phase_Space = 'no' (i.e., NOT running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V13"
        # Ran on 8/6/2024
            # Modified the ∆P plots for the pions so that ∆P is plotted against the Energy Loss Corrected Momentum (and Theta) of the pion if the correction includes it
                # This issue was overlooked when the energy loss correction was first added
            # Refined the (Outbending) Electron Momentum Correction again (without the pion corrections still)
            # Ran with Run_Phase_Space = 'no' (i.e., NOT running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V14"
        # Ran on 8/7/2024
            # Refined the (Outbending) Electron Momentum Correction again (without the pion corrections still)
                # Refinement is split into 2 regions for higher and lower electron momentums
                    # For sectors 1, 2, and 4, the cutoff is at 6.5 GeV while for sectors 3, 5, and 6, the cutoff is at 4.75 GeV
                    # The split is meant to better correct for discrepancies in ∆P that remain at the edges due to high and low momentum electrons needing different types of corrections (i.e., the fits were being pulled in opposite ways so this prevents them from canceling each other out)
            # Ran with Run_Phase_Space = 'no' (i.e., NOT running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V15"
        # Ran on 8/7/2024
            # Refined the (Outbending) Electron Momentum Correction again (without the pion corrections still)
                # The new refinement is again split into 2 regions just like "Fall2018_P2_New_Out_V14" (same split for the same reasons)
            # Ran with Run_Phase_Space = 'no' (i.e., NOT running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V16"
        # Ran on 8/8/2024
            # Refined the (Outbending) Electron Momentum Correction again (without the pion corrections still)
                # The new refinement is NOT split like the last two refinements (hopefully will be the final electron refinement)
            # Ran with Run_Phase_Space = 'yes' (i.e., Running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V17"
        # Ran on 8/8/2024
            # Refined the (Outbending) Electron Momentum Correction again (without the pion corrections still)
                # The new refinement is NOT split
            # Ran with Run_Phase_Space = 'no' (i.e., Not running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V18"
        # Ran on 8/13/2024
            # Refined the (Outbending) Pion Momentum Correction (with all corrections)
            # Ran with Run_Phase_Space = 'no' (i.e., Not running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V19"
        # Ran on 8/14/2024
            # Refined the (Outbending) Pion Momentum Correction (with all corrections)
                # Using Split Mom Correction like what was done with the electron refinements
                # For sectors 1, 2, and 3, the cutoff is at 5 GeV while for sectors 4, 5, and 6, the cutoff is at 4.5 GeV
            # Additional refinements may still be necessary after this one (potentially to both particles)
            # Ran with Run_Phase_Space = 'no' (i.e., Not running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V20"
        # Ran on 8/14/2024
            # Refined the (Outbending) Pion Momentum Correction (with all corrections)
                # Used non-split (i.e., normal) correction for refinement
            # Ran with Run_Phase_Space = 'no' (i.e., Not running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_New_Out_V21"
        # Ran on 8/15/2024
            # Refined the (Outbending) Electron Momentum Correction (with all corrections)
                # Should (hopefully) be the final refinement (if it doesn't work well, may just revert to the corrections used in 'Fall2018_P2_New_Out_V20')
                # Correction was not enough of an improvement to use (refer to 'Fall2018_P2_New_Out_V20' for the final versions of the electron/pi+ pion corrections)
            # Ran with Run_Phase_Space = 'no' (i.e., Not running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_In_Refine_V1"
        # Ran on 8/21/2024
            # Making refinements to the Inbending Fall 2018 P2 Electron corrections (based on 'Forward_Fall2018_P2_Test_V9')
                # Refinements are made without any of the pion corrections and use a split momentum correction at p_el = 7 GeV (for all sectors)
            # Ran with Run_Phase_Space = 'no' (i.e., Not running Phase Space Plots)
            
        Extra_Part_of_Name = "_Fall2018_P2_In_Refine_V2"
        # Ran on 8/21/2024
            # Making refinements to the Inbending Fall 2018 P2 Electron corrections (based on 'Forward_Fall2018_P2_In_Refine_V1')
                # Correction was not split (were very small - likely the last electron refinement possible/necessary)
            # Ran with Run_Phase_Space = 'no' (i.e., Not running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_In_Refine_V3"
        # Ran on 8/22/2024
            # Making refinements to the Inbending Fall 2018 P2 Electron corrections (based on 'Forward_Fall2018_P2_In_Refine_V2')
                # Likely the last electron refinement possible/necessary (pion refinements to come next)
            # Ran with Run_Phase_Space = 'no' (i.e., Not running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_In_Refine_V4"
        # Ran on 8/22/2024
            # Making refinements to the Inbending Fall 2018 P2 Pion corrections (based on 'Forward_Fall2018_P2_In_Refine_V3')
                # Using Split Mom Correction at p_pip = 2.5 GeV (for all sectors)
            # Ran with Run_Phase_Space = 'no' (i.e., Not running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_In_Refine_V5"
        # Ran on 8/23/2024
            # Making refinements to the Inbending Fall 2018 P2 Pion corrections (based on 'Forward_Fall2018_P2_In_Refine_V4')
                # Correction was not split (were very small - likely the last pion refinement possible/necessary)
            # Ran with Run_Phase_Space = 'no' (i.e., Not running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Fall2018_P2_In_Refine_V6"
        # Ran on 9/3/2024
            # Final Version of refinements
                # No change to either correction, but now they are both applied with the same condensed format as is used in the publically distributed version
            # Ran with Run_Phase_Space = 'no' (i.e., Not running Phase Space Plots)
            
            
        if("Central"   in pass_version):
            Extra_Part_of_Name = f"_Central{Extra_Part_of_Name}"
        elif("Forward" in pass_version):
            Extra_Part_of_Name = f"_Forward{Extra_Part_of_Name}"
    
    else:
        Extra_Part_of_Name = "_Sp19_P2_Theta_V1"
        # Ran on 4/15/2024
            # Corrections are the same as the older (Pass 2) Spring 2019 corrections, but now the Pion Energy Loss corrections have also been added (will attempt to perform a new refinement if necessary)
            # All other options are the same as Extra_Part_of_Name = "_Fall2018_P2_Theta_V1", i.e.:
                # New ∆P and MM vs Theta Plots added (to study theta dependence)
                # Turned off the phase space plots to save time while running
                    # i.e., Run_Phase_Space = 'no'
                    
                    
        Extra_Part_of_Name = "_Sp19_P2_Refine_V1"
        # Ran on 8/27/2024
            # Refining the electron corrections (without the existing pion corrections)
                # Will revisit the pion corrections (with energy loss) in a later version of this code
            # Basically reviewing the Spring 2019 corrections with the newer version of this code (i.e., after all changes seen up to Extra_Part_of_Name = "_Fall2018_P2_In_Refine_V5" for the Fall 2018 dataset)
                # Removed some older corrections and am now just going to use 'mm0', 'mmRP2', 'ELPipMM0', 'ELPipMMP2' and all of their relevant combinations
            # Ran with Run_Phase_Space = 'no' (i.e., Not running Phase Space Plots)
            
            
        Extra_Part_of_Name = "_Sp19_P2_Refine_V2"
        # Ran on 8/27/2024
            # Refining the electron corrections (without the existing pion corrections) again
                # Last likely electron refinement
            # Ran with Run_Phase_Space = 'no' (i.e., Not running Phase Space Plots)
            
        Extra_Part_of_Name = "_Sp19_P2_Refine_V3"
        # Ran on 8/27/2024
            # Refining the pion corrections with a split momentum correction
                # The cutoff for this correction is at 3.5 GeV for all sectors
            # Ran with Run_Phase_Space = 'no' (i.e., Not running Phase Space Plots)
            
        Extra_Part_of_Name = "_Sp19_P2_Refine_V4"
        # Ran on 8/28/2024
            # Refining the pion corrections with a non-split momentum correction
                # Normal correction applied across the full range of fittable momentum distribution
            # Ran with Run_Phase_Space = 'no' (i.e., Not running Phase Space Plots)
                
                
        Extra_Part_of_Name = "_Sp19_P2_Refine_V5"
        # Ran on 8/29/2024
            # Removed refinement of the pion corrections that was added in Extra_Part_of_Name = "_Sp19_P2_Refine_V4"
                # Did not improve the MM plots
            # Also testing the Single-line version of the corrections to be used as the distributed version of the corrections
            # Ran with Run_Phase_Space = 'yes' (i.e., Running Phase Space Plots)
            
            
        if("Central"   in pass_version):
            Extra_Part_of_Name = f"_Central{Extra_Part_of_Name}"
        elif("Forward" in pass_version):
            Extra_Part_of_Name = f"_Forward{Extra_Part_of_Name}"
    
    if(event_type not in ["MC"]):
        if(event_type != "P0"):
            if(Delta_P_histo_Q != 'y'):
                OutputFileName = "".join([event_Name.replace(" ", "_"),     "_",       str(MM_type), "_", str(datatype), "_No_Dp",   str(Extra_Part_of_Name), "_File_", str(file_name), ".root"])
            else:
                OutputFileName = "".join([event_Name.replace(" ", "_"),     "_",       str(MM_type), "_", str(datatype), "_With_Dp", str(Extra_Part_of_Name), "_File_", str(file_name), ".root"])
        else:
            if("MC" not in event_Name):
                if(Delta_P_histo_Q != 'y'):
                    OutputFileName = "".join([event_Name.replace(" ", "_"), "_",       str(MM_type), "_", str(datatype), "_No_Dp",   str(Extra_Part_of_Name),                           ".root"])
                else:
                    OutputFileName = "".join([event_Name.replace(" ", "_"), "_",       str(MM_type), "_", str(datatype), "_With_Dp", str(Extra_Part_of_Name),                           ".root"])
            else:
                if(Delta_P_histo_Q != 'y'):
                    OutputFileName = "".join(["Pi0_Channel_",                          str(MM_type), "_", str(datatype), "_No_Dp",   str(Extra_Part_of_Name),                           ".root"])
                else:
                    OutputFileName = "".join(["Pi0_Channel_",                          str(MM_type), "_", str(datatype), "_With_Dp", str(Extra_Part_of_Name),                           ".root"])
    else:
        
        Extra_Part_of_Name = "_Fa18_P1_MC_V1"
        # Ran on 6/4/2024
            # Making Momentum Corrections for the Pass 1 versions of my SIDIS analysis Reconstructed Monte Carlo files
            # Running with default plots and (experimental data) corrections (should be treated as if it was just the normal Fall 2018 Pass 1 SP option)
        Extra_Part_of_Name = "_Fa18_P1_MC_V2"
        # Ran on 6/4/2024
            # Rerunning to fix errors in "_Fa18_P1_MC_V1"
            
            
        Extra_Part_of_Name = "_Fa18_P2_MC_V1"
        # Ran on 7/12/2024
            # Making Momentum Corrections for the Pass 2 versions of my SIDIS analysis Reconstructed Monte Carlo files
            # Running with default plots and (experimental data) corrections (should be treated as if it was just the normal Fall 2018 Pass 2 SP option)
            # Changed the MC beam energy to 10.604 GeV instead of 10.6041 GeV to more closely match the beam energy used by Stefan
            
        Extra_Part_of_Name = "_Fa18_P2_MC_V2"
        # Ran on 7/22/2024
            # Making Momentum Corrections for the Pass 2 versions of my SIDIS analysis Reconstructed Monte Carlo files
            # Running with default plots and (experimental data) corrections (should be treated as if it was just the normal Fall 2018 Pass 2 SP option)
                # Using same options as selected for "Fall2018_P2_New_Out_V5" (but with Inbending Corrections)
            # Changed the MC beam energy to 10.6 GeV instead of 10.604 GeV to more closely match the beam energy used by Stefan (beam energy from 'Fa18_P2_MC_V1' was still not correct)
            
            
        Extra_Part_of_Name = "_Fa18_P2_MC_V3"
        # Ran on 7/26/2024
            # Making Momentum Corrections for the Pass 2 versions of my SIDIS analysis Reconstructed Monte Carlo files
            # Running with default plots and (experimental data) corrections (should be treated as if it was just the normal Fall 2018 Pass 2 SP option)
                # Using same options as selected for "Fall2018_P2_New_Out_V10" (but with Inbending Corrections and turned off 'Run_Phase_Space')
            # Added new version of the Monte Carlo files with additional files that I added to the files already created by Stefan
        # ERROR NOTED ON 8/6/2024: Due to issues with the ifarm, this file version did not run to completion. Only 'final' version of this file is called: "Simulated_Single_Pion_Channel_epipX_Inbending_With_Dp_Fa18_P2_MC_V3_File_Incomplete.root"
            # Moved to "_Fa18_P2_MC_V4" instead of completing this version
            
        Extra_Part_of_Name = "_Fa18_P2_MC_V4"
        # Ran on 8/6/2024
            # Same as "_Fa18_P2_MC_V3" but with the bug fix to the ∆P (pion) plots (see "_Fall2018_P2_New_Out_V13")
                # "_Fa18_P2_MC_V3" may not have run to completion due to issues with the ifarm (see above)
        
        if(Delta_P_histo_Q != 'y'):
            OutputFileName = "".join(["Simulated_", event_Name.replace(" ", "_"), "_", str(MM_type), "_", str(datatype), "_No_Dp",   str(Extra_Part_of_Name), "_File_", str(file_name), ".root"])
        else:
            OutputFileName = "".join(["Simulated_", event_Name.replace(" ", "_"), "_", str(MM_type), "_", str(datatype), "_With_Dp", str(Extra_Part_of_Name), "_File_", str(file_name), ".root"])
            
            
    OutputFileName = OutputFileName.replace("__", "_")
    print(f"{color.BGREEN}Name of file that will be saved:{color.END}\n{str(OutputFileName)}\n")


    ################################################################################
    ##=====##=====##=====##     Choices for Saving (End)     ##=====##=====##=====##
    ################################################################################










    ###############################################################################
    ##=====##=====##=====##=====##   Initial Timer   ##=====##=====##=====##=====##
    ###############################################################################


    datetime_object_full = datetime.now()

    startMin_full, startHr_full = datetime_object_full.minute, datetime_object_full.hour

    if(datetime_object_full.minute < 10):
        timeMin_full = ''.join(['0', str(datetime_object_full.minute)])
    else:
        timeMin_full = str(datetime_object_full.minute)

    if(datetime_object_full.hour > 12 and datetime_object_full.hour < 24):
        print("".join(["The time that the code started is ", str((datetime_object_full.hour) - 12), ":", timeMin_full, " p.m."]))
    if(datetime_object_full.hour < 12 and datetime_object_full.hour > 0):
        print("".join(["The time that the code started is ", str(datetime_object_full.hour), ":", timeMin_full, " a.m."]))
    if(datetime_object_full.hour == 12):
        print("".join(["The time that the code started is ", str(datetime_object_full.hour), ":", timeMin_full, " p.m."]))
    if(datetime_object_full.hour == 0 or datetime_object_full.hour == 24):
        print("".join(["The time that the code started is 12:", timeMin_full, " a.m."]))


    ###############################################################################
    ##=====##=====##=====##=====##   Initial Timer   ##=====##=====##=====##=====##
    ###############################################################################





    #############################################################################
    ##=====##=====##=====##=====##   Loading RDF   ##=====##=====##=====##=====##
    #############################################################################

    # Default option is all outbending files
    # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/shrestha/clas12momcorr/data/outbending/ePipX/skim4_00*"
    running_code_with_these_files = "/work/clas12/shrestha/clas12momcorr/utsav/dataFiles/outbending/ePipX/skim4_005*"

    if(file_location in ["All", "Test", "test", "time"]):
        if(event_type in ["SP", "MC"]):
            if(pass_version in ["NA", ""]):
                if(datatype == "Inbending"):
                    running_code_with_these_files = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Single_Pion_Channel_epipN/Inbending_skim4/ePip.inb.qa.skim4_00*"
                else:
                    running_code_with_these_files = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Single_Pion_Channel_epipN/Outbending/ePip.outb.qa.nSidis_005*"
                    # Skim4 cuts
                    running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Outbending_skim4/ePip.outb.qa.rec_clas_*.root"
            if("Fall"     in pass_version):
                if(datatype == "Inbending"):
                    running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Inbending/Single_Pion_Channel_epipN/ePip.wCentral.pass2.inb.qa.Fa18.rec_clas_00*"
                else:
                    # running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Outbending/Single_Pion_Channel_epipN/ePip.wCentral.pass2.outb.Fa18.rec_clas_00*"
                    running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Outbending/Single_Pion_Channel_epipN/ePip.wCentral.pass2.outb.qa.Fa18.rec_clas_00*"
            elif("Pass 1" in pass_version):
                running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass1/Inbending_recon/Single_Pion_Channel_epipN/ePip.pass1.inb.qa.rec_clas_00*"
            else:
                running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/Inbending_recon/Single_Pion_Channel_epipN/ePip.pass2.inb.qa.rec_clas_00*"
        
        
        if(event_type == "DP"):
            if(datatype == "Inbending"):
                running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Double_Pion_Channel_eppippim/Inbending_skim4/epPipPim.inb.qa.skim4_00*"
            else:
                running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Double_Pion_Channel_eppippim/Outbending_skim4/epPipPim.outb.qa.skim4_00*"
                
        if("P0" in event_type):
            if(datatype == "Inbending"):
                running_code_with_these_files = "/lustre19/expphy/volatile/clas12/kenjo/lvl2_eppi0.inb.qa.eloss.exclusiveselection.root"
                running_code_with_these_files = "/u/home/richcap/lvl2_eppi0.inb.qa.eloss.exclusiveselection.root"
                running_code_with_these_files = "/u/home/richcap/lvl2_eppi0.inb.qa.exclusiveselection.root"
                if("MC" in event_Name):
                    running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Pi0_MC/lvl2_eppi0.inb.mc.eloss.root"
                    if("+20 MeV" in event_Name):
                        running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Pi0_MC/lvl2_eppi0.inb.mc.eloss.Ppos20.root"
                    if("-20 MeV" in event_Name):
                        running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Pi0_MC/lvl2_eppi0.inb.mc.eloss.Pneg20.root"
                    
            else:
                running_code_with_these_files = "/u/home/richcap/lvl2_eppi0.outb.qa.eloss.exclusiveselection.root"
                running_code_with_these_files = "/u/home/richcap/lvl2_eppi0.outb.qa.exclusiveselection.root"
                
        if(event_type == "ES"):
            if(datatype == "Inbending"):
                running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/", str(datatype), "/eP_Elastic_with_CDpro_New*.root"])
                running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/Valerii_Files/eP_Elastic_with_CDpro_New", ".inb" if("In" in str(datatype)) else ".outb", "*root"])
                running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/Valerii_Files/eP_Elastic_with_CDpro", ".inb" if("In" in str(datatype)) else ".outb", "*root"])
            else:
                # Skim4 cuts
                running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Elastic_Scattering_ep/Outbending/eP_Elastic_with_CDpro.outb.qa.rec_clas_005449.evio.0*.root"
                
        if(event_type == "EO"):
            if(datatype == "Inbending"):
                running_code_with_these_files     = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Only_Electron_Channel/electron_only", ".inb" if("In" in str(datatype)) else ".outb", "*root"])
                if("Fall"     in pass_version):
                    if(datatype == "Inbending"):
                        running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Inbending/Only_Electron_Channel/electron_only.pass2.inb.Fa18.rec_clas_00*"
                        running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Inbending/Only_Electron_Channel/electron_only.pass2.inb.qa.Fa18.rec_clas_00*"
                    else:
                        running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Outbending/Only_Electron_Channel/electron_only.pass2.outb.Fa18.rec_clas_00*"
                        running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Outbending/Only_Electron_Channel/electron_only.pass2.outb.qa.Fa18.rec_clas_00*"
                elif("Pass 2" in pass_version):
                    running_code_with_these_files = "".join(["/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/", "Inbending" if("In" in str(datatype)) else "Outbending", "_nSidis/Complete/Only_Electron_Channel/electron_only.pass2", ".inb" if("In" in str(datatype)) else ".outb", ".qa.nSidis_*root"])
                    running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/Inbending_recon/Only_Electron_Channel/electron_only.pass2.inb.qa.rec_clas_00*"
                else:
                    running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass1/Inbending_recon/Only_Electron_Channel/electron_only.pass1.inb.qa.rec_clas_00*"
            else:
                # Skim4 cuts
                running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Only_Electron_Channel/Outbending/electron_only.outb.qa.rec_clas_005*.root"
                if("Pass 2" in pass_version):
                    running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Outbending/Only_Electron_Channel/electron_only.pass2.outb.qa.Fa18.rec_clas_005*.root"
                
        if(event_type in ["MC"]):
            # running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/SIDIS_Analysis/Data_Files_Groovy/Matched_REC_MC/MC_Matching_sidis_epip_richcap.inb.qa.45nA_job_*.root"])
            # running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/SIDIS/Matched_REC_MC/MC_Matching_sidis_epip_richcap.inb.qa.45nA_job_*.root" if("Pass 2" not in pass_version) else "/w/hallb-scshelf2102/clas12/richcap/SIDIS/Matched_REC_MC/With_BeamCharge/Pass2/More_Cut_Info/MC_Matching_sidis_epip_richcap.inb.qa.new4.inb-clasdis_*"
            running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/SIDIS/Matched_REC_MC/MC_Matching_sidis_epip_richcap.inb.qa.45nA_job_*.root" if("Pass 2" not in pass_version) else "/w/hallb-scshelf2102/clas12/richcap/SIDIS/Matched_REC_MC/With_BeamCharge/Pass2/More_Cut_Info/MC_Matching_sidis_epip_richcap.inb.qa.new5.inb-clasdis*"
            event_type = "SP"

    else:
        running_code_with_these_files = file_location

    rdf = ROOT.RDataFrame("h22", str(running_code_with_these_files))
    
    if("E" in event_type):
        print(f"{color.BOLD}\nApplying Base Invariant Mass Cuts to Elastic Events...\n{color.END}")
        rdf = rdf.Filter("".join(["""
        auto Beam_Energy = """, str(Beam_Energy), """;
        auto Proton_Mass = """, str(Particle_Mass_Proton), """;//0.938;
        auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
        auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
        auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
        auto Cut_Variable = (beam + targ - eleC).M();
        double Cut_Upper = 1.3;
        double Cut_Lower = 0.6;
        return ((Cut_Variable < Cut_Upper) && (Cut_Variable > Cut_Lower));
        """]))
        
    if("SP" in event_type):
        print(color.BOLD + "\nApplying Base Missing Mass Cuts to Single Pion Events (MM < 1.8 GeV)...\n" + color.END)
        rdf = rdf.Filter("".join(["""
        auto beam = ROOT::Math::PxPyPzMVector(0, 0, """,    str(Beam_Energy),          """, 0);
        auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, """, str(Particle_Mass_Proton), """);
        auto ele  = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
        auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, """, str(Particle_Mass_PiC), """);
        auto MM_Vector = beam + targ - ele - pip0;
        auto cut_upper = 1.8;
        auto cut_lower = 0;
        return (MM_Vector.M() < cut_upper && MM_Vector.M() > cut_lower);
        """]))

    #############################################################################
    ##=====##=====##=====##=====##   Loading RDF   ##=====##=====##=====##=====##
    #############################################################################

    if(See_Num_of_Events_Q != 'n'):
        print("".join(["Number of events = ", str(rdf.Count().GetValue())]))
    print("".join([color.BBLUE, "Running code with files located here:\n", color.END, str(running_code_with_these_files), "\n"]))


    
    ######################################################################
    ##=====##=====##   For Central Detector Status Cuts   ##=====##=====##
    if(("status" in rdf.GetColumnNames()) or ("artsec" in rdf.GetColumnNames())):
        rdf = rdf.Filter("!((artsec == -1) && (status < 4000))") # Failed Forward Detector (Fiducial) Cuts but was not in the Central Detector
        if("Central"   in pass_version):
            print(f"{color.BOLD}\nMAKING CENTRAL DETECTOR CUTS\n{color.END}")
            rdf = rdf.Filter("(artsec == -1) && (status >= 4000 && status < 8000)")
        elif("Forward" in pass_version):
            print(f"{color.BOLD}\nMAKING FORWARD DETECTOR CUTS\n{color.END}")
            rdf = rdf.Filter("artsec == 1")
        else:
            print("\nMAKING STATUS CUTS\n")
    ##=====##=====##   Central Detector Status Cuts END   ##=====##=====##
    ######################################################################
            
            

    if(event_type not in ["SP", "MC", "EO"]):
        if("(GEN)" not in event_Name):
            if("prox"   not in rdf.GetColumnNames() and "px"   in rdf.GetColumnNames()):
                rdf = rdf.Define("prox", "px")
            if("proy"   not in rdf.GetColumnNames() and "py"   in rdf.GetColumnNames()):
                rdf = rdf.Define("proy", "py")
            if("proz"   not in rdf.GetColumnNames() and "pz"   in rdf.GetColumnNames()):
                rdf = rdf.Define("proz", "pz")
            if("prosec" not in rdf.GetColumnNames() and "psec" in rdf.GetColumnNames()):
                rdf = rdf.Define("prosec", "psec")
        else:
            print("".join([color.ERROR, "\n\nPro is generated", color.END]))
            if("prox"   not in rdf.GetColumnNames() and "px0"  in rdf.GetColumnNames()):
                rdf = rdf.Define("prox", "px0")
            if("proy"   not in rdf.GetColumnNames() and "py0"  in rdf.GetColumnNames()):
                rdf = rdf.Define("proy", "py0")
            if("proz"   not in rdf.GetColumnNames() and "pz0"  in rdf.GetColumnNames()):
                rdf = rdf.Define("proz", "pz0")
            if("prosec" not in rdf.GetColumnNames() and "psec" in rdf.GetColumnNames()):
                rdf = rdf.Define("prosec", "psec")
            
            
    
    






    ############################################################################################################################################################
    ##========================================================================================================================================================##
    ##==============##============##============##============##         Calculations for RDF         ##============##============##============##============##
    ##========================================================================================================================================================##
    ############################################################################################################################################################



    ## Proton Energy Loss Corrections ##
    if(event_type not in ["SP", "MC", "EO"]):
        Proton_Energy_Loss_Cor = Proton_Energy_Loss_Cor_Function(Bending_Type=datatype)

    ##########################################################################################################################
    ##==============##============##         Standard Kinematics - Angles and Momentums         ##============##============##
    ##########################################################################################################################


    #------------------------------------------#
    #---------------# Electron #---------------#
    #------------------------------------------#
    try:
        if("(GEN)" not in event_Name):
            ##=====##    Momentum Magnitude    ##=====##
            rdf = rdf.Define("el", "sqrt(ex*ex + ey*ey + ez*ez)")
            ##=====##       Polar Angles       ##=====##
            rdf = rdf.Define("elth", "atan2(sqrt(ex*ex + ey*ey), ez)*(180/3.1415926)")
            # if("Central" in str(pass_version)):
            #     print(color.BOLD, "\nMAKING CUT ON ELECTRON POLAR ANGLE TO SELECT THE EVENTS FROM THE 'Central' DETECTOR\n", color.END)
            #     rdf = rdf.Filter("elth > 35 && elth < 135")
            # if("Forward" in str(pass_version)):
            #     print(color.BOLD, "\nMAKING CUT ON ELECTRON POLAR ANGLE TO SELECT THE EVENTS FROM THE 'Forward' DETECTOR\n", color.END)
            #     rdf = rdf.Filter("elth >  5 && elth <  35")
            ##=====##     Azimuthal Angles     ##=====##
            rdf = rdf.Define("elPhi", """
                double elPhi = (180/3.1415926)*atan2(ey, ex);
                if(((esec == 4 || esec == 3) && elPhi < 0) || (esec > 4 && elPhi < 90)){
                    elPhi += 360;
                }
                return elPhi;
            """)
            rdf = rdf.Define("localelPhi", "elPhi - (esec - 1)*60")
            rdf = rdf.Define("localelPhiS", "localelPhi - (30/el)")
            rdf = rdf.Define("elPhiS", "elPhi - (30/el)")
            rdf = rdf.Define("elPhiNS", "(180/3.1415926)*atan2(ey, ex)") # 'NS' ==> No shifts (distribution will be from ±180˚)
        else:
            print("".join([color.Error, "El is generated\n\n", color.END]))
            ##=====##    Momentum Magnitude    ##=====##
            rdf = rdf.Define("el", "sqrt(ex0*ex0 + ey0*ey0 + ez0*ez0)")
            ##=====##       Polar Angles       ##=====##
            rdf = rdf.Define("elth", "atan2(sqrt(ex0*ex0 + ey0*ey0), ez0)*(180/3.1415926)")
            # if("Central" in str(pass_version)):
            #     print(color.BOLD, "\nMAKING CUT ON ELECTRON POLAR ANGLE TO SELECT THE EVENTS FROM THE 'Central' DETECTOR\n", color.END)
            #     rdf = rdf.Filter("elth > 35 && elth < 135")
            # if("Forward" in str(pass_version)):
            #     print(color.BOLD, "\nMAKING CUT ON ELECTRON POLAR ANGLE TO SELECT THE EVENTS FROM THE 'Forward' DETECTOR\n", color.END)
            #     rdf = rdf.Filter("elth >  5 && elth <  35")
            ##=====##     Azimuthal Angles     ##=====##
            rdf = rdf.Define("elPhi", """
                double elPhi = (180/3.1415926)*atan2(ey0, ex0);
                if(((esec == 4 || esec == 3) && elPhi < 0) || (esec > 4 && elPhi < 90)){
                    elPhi += 360;
                }
                return elPhi;
            """)
            rdf = rdf.Define("localelPhi", "elPhi - (esec - 1)*60")
            rdf = rdf.Define("localelPhiS", "localelPhi - (30/el)")
            rdf = rdf.Define("elPhiS", "elPhi - (30/el)")
            rdf = rdf.Define("elPhiNS", "(180/3.1415926)*atan2(ey0, ex0)") # 'NS' ==> No shifts (distribution will be from ±180˚)
    except Exception as e:
        print("Failure to process Electron Kinematics")
        print("".join(["ERROR: ", str(e)]))

    if(event_type != "EO"):
        #------------------------------------------#
        #---------------# Pi+ Pion #---------------#
        #------------------------------------------#
        if(event_type not in ["P0", "ES"]):
            try:
                ##=====##    Momentum Magnitude    ##=====##
                rdf = rdf.Define("pip", "sqrt(pipx*pipx+pipy*pipy+pipz*pipz)")
                ##=====##       Polar Angles       ##=====##
                rdf = rdf.Define("pipth", "atan2(sqrt(pipx*pipx+pipy*pipy), pipz)*(180/3.1415926)")
                rdf = rdf.Define("pipPhi", """
                    double pipPhi = (180/3.1415926)*atan2(pipy, pipx);
                    if(pipsec > 6){
                        if(pipPhi < -25){pipPhi += 360;}
                        pipPhi += 25;
                    }
                    else{
                        if(((pipsec == 4 || pipsec == 3) && pipPhi < 0) || (pipsec > 4 && pipPhi < 90)){
                            pipPhi += 360;
                        }
                    }
                    return pipPhi;
                """)
                if(("status" in rdf.GetColumnNames()) or ("artsec" in rdf.GetColumnNames())):
                    rdf = rdf.Redefine("pipsec", "".join([str(Central_Detector_Sector_Definition).replace("""
if(pipPhi < -25){pipPhi += 360;}
pipPhi += 25;""", ""), "return tempsec;"]))
                    rdf = rdf.Redefine("pipPhi", """
                    double tempPipPhi = pipPhi;
                    if(pipsec == 7 && tempPipPhi > 200){tempPipPhi += -360;}
                    return tempPipPhi;""")
                rdf = rdf.Define("localpipPhi", """
                    double localpipPhi;
                    if(pipsec < 7){localpipPhi = pipPhi - (pipsec - 1)*60;}
                    else{localpipPhi = pipPhi - (pipsec - 7)*60 - 30;} // The (pipsec - 7) resets the offset done to get the local phi above for the central detector sectors
                    return localpipPhi;
                """)
                # rdf = rdf.Define("localpipPhiS", "localpipPhi + (32/(pip-0.05))")
                rdf = rdf.Define("localpipPhiS", "".join(["""
                    double localpipPhiS = localpipPhi + (32/(pip-0.05));
                    if(pipsec < 7){localpipPhiS = localpipPhi + (32/(pip-0.05));}
                    // if(pipsec > 6){localpipPhiS = localpipPhi + (2/(pip-0.05));}
                    if(pipsec > 6){""", Central_Detector_PipPhi_Shift.replace("double pipPhi_Shift = ", "localpipPhiS = local"), """}
                    return localpipPhiS;
                """]))
                # rdf = rdf.Define("pipPhiS", "pipPhi + (32/(pip-0.05))")
                rdf = rdf.Define("pipPhiS",   "".join(["""
                    double pipPhiS;
                    if(pipsec < 7){pipPhiS = pipPhi + (32/(pip-0.05));}
                    // if(pipsec > 6){pipPhiS = pipPhi + (2/(pip-0.05));}
                    if(pipsec > 6){""", Central_Detector_PipPhi_Shift.replace("double pipPhi_Shift =", "pipPhiS ="), """}
                    return pipPhiS;
                """]))
                rdf = rdf.Define("pipPhiNS", "(180/3.1415926)*atan2(pipy, pipx)") # 'NS' ==> No shifts (distribution will be from ±180˚)
                #-----------------------------------------------------------#
                #---------------#  Pion (Energy Corrected)  #---------------#
                #-----------------------------------------------------------#
                if("Pass 2" in str(pass_version)):
                    try:
                        pion_EL_cor = f"""
                        {Pion_Energy_Loss_Cor_Function}
                        int pion_det;
                        if(pipsec < 7){{pion_det = 2;}} // Forward Detector
                        else{{pion_det = 3;          }} // Central Detector
                        auto p_pip_loss = eloss_pip(pip, pipth, pion_det, {"false" if("In" in datatype) else "true"});
                        auto f_pip_loss = ((pip+p_pip_loss)/pip);"""
                        ##=====##    (Energy Corrected) Momentum Coordinates    ##=====##
                        rdf = rdf.Define("pipx_cor", f"""
                        {pion_EL_cor}
                        double pipx_cor = f_pip_loss*pipx;
                        return pipx_cor;""")
                        rdf = rdf.Define("pipy_cor", f"""
                        {pion_EL_cor}
                        double pipy_cor = f_pip_loss*pipy;
                        return pipy_cor;""")
                        rdf = rdf.Define("pipz_cor", f"""
                        {pion_EL_cor}
                        double pipz_cor = f_pip_loss*pipz;
                        return pipz_cor;""")
                        del pion_EL_cor
                        ##=====##    (Energy Corrected) Momentum Magnitude    ##=====##
                        rdf = rdf.Define("pip_EL", "sqrt(pipx_cor*pipx_cor + pipy_cor*pipy_cor + pipz_cor*pipz_cor)")
                        ##=====##       (Energy Corrected) Polar Angles       ##=====##
                        rdf = rdf.Define("pipth_EL", "atan2(sqrt(pipx_cor*pipx_cor + pipy_cor*pipy_cor), pipz_cor)*(180/3.1415926)")
                        ##=====##     (Energy Corrected) Azimuthal Angles     ##=====##
                        rdf = rdf.Define("pipPhi_EL", """
                            double pipPhi_EL = (180/3.1415926)*atan2(pipy_cor, pipx_cor);
                            if(((pipsec == 4 || pipsec == 3) && pipPhi_EL < 0) || (pipsec > 4 && pipPhi_EL < 90)){
                                pipPhi_EL += 360;
                            }
                            return pipPhi_EL;
                        """)
                        rdf = rdf.Define("localpipPhi_EL",  "pipPhi_EL - (pipsec - 1)*60")
                        rdf = rdf.Define("localpipPhiS_EL", "localpipPhi_EL + (32/(pip_EL-0.05))")
                        rdf = rdf.Define("pipPhiS_EL",      "pipPhi_EL + (32/(pip_EL-0.05))")
                        rdf = rdf.Define("pipPhiNS_EL",     "(180/3.1415926)*atan2(pipy_cor, pipx_cor)") # 'NS' ==> No shifts (distribution will be from ±180˚)
                    except Exception as e:
                        print(f"{color.ERROR}\n\nFailure to process Pi+ Pion Kinematics (Corrected for Energy Loss)\n\n{color.END}")
                        print("".join(["ERROR: ", str(e)]))
                        print("".join([color.Error, "TRACEBACK: \n", color.END, str(traceback.format_exc()), "\n\n"]))
            except Exception as e:
                print(f"{color.ERROR}\n\nFailure to process Pi+ Pion Kinematics\n\n{color.END}")
                print("".join(["ERROR: ", str(e)]))
                print("".join([color.Error, "TRACEBACK: \n", color.END, str(traceback.format_exc()), "\n\n"]))

        #------------------------------------------#
        #---------------# Pi- Pion #---------------#
        #------------------------------------------#
        if(event_type == "DP"):
            try:
                ##=====##    Momentum Magnitude    ##=====##
                rdf = rdf.Define("pim", "sqrt(pimx*pimx+pimy*pimy+pimz*pimz)")
                ##=====##       Polar Angles       ##=====##
                rdf = rdf.Define("pimth", "atan2(sqrt(pimx*pimx+pimy*pimy), pimz)*(180/3.1415926)")
                ##=====##     Azimuthal Angles     ##=====##
                rdf = rdf.Define("pimPhi", """
                    double pimPhi = (180/3.1415926)*atan2(pimy, pimx);
                    if(((pimsec == 4 || pimsec == 3) && pimPhi < 0) || (pimsec > 4 && pimPhi < 90)){
                        pimPhi += 360;
                    }
                    return pimPhi;
                """)
                rdf = rdf.Define("localpimPhi", "pimPhi - (pimsec - 1)*60")
                rdf = rdf.Define("localpimPhiS", "localpimPhi - (32/(pim-0.05))")
                rdf = rdf.Define("pimPhiS", "pimPhi - (32/(pim-0.05))")
                rdf = rdf.Define("pimPhiNS", "(180/3.1415926)*atan2(pimy, pimx)") # 'NS' ==> No shifts (distribution will be from ±180˚)
            except Exception as e:
                print("Failure to process Pi- Pion Kinematics")
                print("".join(["ERROR: ", str(e)]))

        #----------------------------------------#
        #---------------# Proton #---------------#
        #----------------------------------------#
        if(event_type not in ["SP", "MC"]):
            try:
                ##=====##    Momentum Magnitude    ##=====##
                rdf = rdf.Define("pro", "sqrt(prox*prox + proy*proy + proz*proz)")
                ##=====##       Polar Angles       ##=====##
                rdf = rdf.Define("proth", "atan2(sqrt(prox*prox + proy*proy), proz)*(180/3.1415926)")
                ##=====##     Azimuthal Angles     ##=====##
                rdf = rdf.Define("proPhi", """
                    double proPhi = (180/3.1415926)*atan2(proy, prox);
                    if(((prosec == 4 || prosec == 3) && proPhi < 0) || (prosec > 4 && proPhi < 90)){
                        proPhi += 360;
                    }
                    return proPhi;
                """)
                rdf = rdf.Define("localproPhi", "proPhi - (prosec - 1)*60")
                rdf = rdf.Define("localproPhiS", "localproPhi + (32/(pro-0.05))")
                rdf = rdf.Define("proPhiS", "proPhi + (32/(pro-0.05))")
                rdf = rdf.Define("proPhiNS", "(180/3.1415926)*atan2(proy, prox)") # 'NS' ==> No shifts (distribution will be from ±180˚)
            except Exception as e:
                print("Failure to process Proton Kinematics")
                print("".join(["ERROR: ", str(e)]))

        #-----------------------------------------------------------#
        #---------------# Proton (Energy Corrected) #---------------#
        #-----------------------------------------------------------#
        if((event_type not in ["SP", "MC"]) and ("MC" not in event_Name)):
            try:
                ##=====##    (Energy Corrected) Momentum Coordinates    ##=====##
                rdf = rdf.Define("prox_cor", "".join(["""
                """, Proton_Energy_Loss_Cor, """
                double prox_cor = feloss*prox;
                return prox_cor;
                """]))
                rdf = rdf.Define("proy_cor", "".join(["""
                """, Proton_Energy_Loss_Cor, """
                double proy_cor = feloss*proy;
                return proy_cor;
                """]))
                rdf = rdf.Define("proz_cor", "".join(["""
                """, Proton_Energy_Loss_Cor, """
                double proz_cor = feloss*proz;
                return proz_cor;
                """]))
                ##=====##    (Energy Corrected) Momentum Magnitude    ##=====##
                rdf = rdf.Define("pro_cor", "sqrt(prox_cor*prox_cor + proy_cor*proy_cor + proz_cor*proz_cor)")
                ##=====##       (Energy Corrected) Polar Angles       ##=====##
                rdf = rdf.Define("proth_cor", "atan2(sqrt(prox_cor*prox_cor + proy_cor*proy_cor), proz_cor)*(180/3.1415926)")
                ##=====##     (Energy Corrected) Azimuthal Angles     ##=====##
                rdf = rdf.Define("proPhi_cor", """
                    double proPhi_cor = (180/3.1415926)*atan2(proy_cor, prox_cor);
                    if(((prosec == 4 || prosec == 3) && proPhi_cor < 0) || (prosec > 4 && proPhi_cor < 90)){
                        proPhi_cor += 360;
                    }
                    return proPhi_cor;
                """)
                rdf = rdf.Define("localproPhi_cor",  "proPhi_cor - (prosec - 1)*60")
                rdf = rdf.Define("localproPhiS_cor", "localproPhi_cor + (32/(pro_cor-0.05))")
                rdf = rdf.Define("proPhiS_cor",      "proPhi_cor + (32/(pro_cor-0.05))")
                rdf = rdf.Define("proPhiNS_cor",     "(180/3.1415926)*atan2(proy_cor, prox_cor)") # 'NS' ==> No shifts (distribution will be from ±180˚)
            except Exception as e:
                print("Failure to process Proton Kinematics")
                print("".join(["ERROR: ", str(e)]))


    ################################################################################################################################
    ##==============##============##         Standard Kinematics - Angles and Momentums (End)         ##============##============##
    ################################################################################################################################
    
    
    
    
    
    ###########################################################################################################
    ##=======================================================================================================##
    ##==============##============##         Correction Application Code         ##============##============##
    ##=======================================================================================================##
    ###########################################################################################################

    # // corEl ==> Gives the 'generation' of the electron correction
    #     // corEl == 0   --> No Correction
    #     // corEl == 1   --> Quad Momentum - Quad Phi (Final Version)
    #     // corEl == 2   --> Modified Electron Correction with extended range (Created using exsisting corrections (i.e., this is a refinement of those corrections) -- Quad Mom - Quad Phi -- Kinematic Coverage is from 0.95-9.95 GeV using both SP and EO channels)
    #     // corEl == 3   --> New Electron Correction with extended range (Created from Uncorrected Particles -- Quad Mom - Quad Phi -- Kinematic Coverage is from 0.95-9.95 GeV using both SP and EO channels)
    #     // corEl == 4   --> Old Electron Correction with (Spring 2019) pass2 data (Created from Uncorrected Particles -- Quad Mom -- does not use EO channels)
    #     // corEl == 5   --> New Electron Correction with (Spring 2019) pass2 data (Created from corEL = 4 Corrections -- Quad Mom -- does not use EO channels)
    #     // corEl == 6/4 --> New Electron Correction with (Fall   2018) pass2 data (6 is for Inbending, 4 is for Outbending)
    def NameElCor(corEl, datatype):
        coutN = 0
        if('mm0'    in corEl):
            coutN = 0
        if("mmF"    in corEl):
            coutN = 1
        if("mmExF"  in corEl):
            coutN = 2
        if("mmEF"   in corEl):
            coutN = 3
        if("mmP2"   in corEl):
            coutN = 4
        if("mmRP2"  in corEl):
            coutN = 5
        if("mmfaP2" in corEl):
            coutN = 6 if("Out" not in datatype) else 4
        if("mmRGK" in corEl):
            coutN = 7

        return coutN

    # // corPip ==> Gives the 'generation' of the π+ Pion correction
    #     // corPip == 0   --> No Correction
    #     // corPip == 1   --> Quad Momentum, Quad Phi (Old Version)
    #     // corPip == 2   --> Quad Momentum, Quad Phi (Extended - Test - Version)
    #     // corPip == 3   --> Quad Momentum, Quad Phi (Final Version)
    #     // corPip == 4   --> New π+ Pion Correction with (Spring 2019) pass2 data (Created from Uncorrected π+ Pion -- Quad Mom -- does not use EO channels)
    #     // corPip == 5   --> New π+ Pion Correction with (Spring 2019) pass2 data (Created from corPip == 4 -- Quad Mom -- Split at p = 4 GeV between two functions)
    #     // corPip == 6/4 --> New π+ Pion Correction with (Fall   2018) pass2 data (6 is for Inbending, 4 is for Outbending)
    def NamePipCor(corPip, datatype):
        coutN = 0
        if("Pip" not in corPip):
            coutN = 0
        else:
            if("PipMM0"      in corPip):
                coutN = 0
            if("PipMMExF"    in corPip):
                coutN = 2
            elif("PipMMEF"   in corPip):
                coutN = 3
            elif("PipMMP2"   in corPip):
                coutN = 4
            elif("PipMMsP2"  in corPip):
                coutN = 5
            elif("PipMMfaP2" in corPip):
                coutN = 6 if("Out" not in datatype) else 4
            else:
                coutN = 1
        return coutN


    # // corPim ==> Gives the 'generation' of the π- Pion correction
    #     // corPim == 0 --> No Correction
    #     // corPim == 1 --> Nick's Quad Momentum, Quad Phi
    #     // corPim == 2 --> Rounded version of corPim == 1 (Not developed yet)
    def NamePimCor(corPim, datatype):
        coutN = 0
        if("Pim" not in corPim):
            coutN = 0
        else:
            coutN = 1
        # if('PimMMpim_qPhi' in corPim):
        #     coutN = 1
        # if('PimMMpim_F' in corPim):
        #     coutN = 2
        return coutN


    # // corPro ==> Gives the 'generation' of the Proton correction
    #     // corPro == 0 --> No Correction
    #     // corPro == 1 --> Quad Momentum, No Phi
    def NameProCor(corPro, datatype):
        coutN = 0
        if("Pro" not in corPro):
            coutN = 0
        elif("MMpro_EF"    in corPro):
            coutN = 2
        elif("MMpro_QEF"   in corPro):
            coutN = 3
        elif("MMpro_LEF"   in corPro):
            coutN = 4
        # elif("MMpro_REF" in corPro):
        #     coutN = 5
        elif("MMpro_S_LEF" in corPro):
            coutN = 6
        elif("MMpro_SEF"   in corPro):
            coutN = 7
        elif("MMpro_SEC"   in corPro):
            coutN = 8
        elif("MMpro_SERC"  in corPro):
            coutN = 9
        elif("MMpro_SRE"   in corPro):
            coutN = 10
        elif("MMpro_SFRE"  in corPro):
            coutN = 11
        elif("MMpro_DRE"   in corPro):
            coutN = 12
        elif("MMpro_RE"    in corPro):
            coutN = 13
        elif("MMpro_FRE"   in corPro): # corPro == 14
            coutN = 14
        elif("MMpro_NRE"   in corPro): # corPro == 15
            coutN = 15
        elif("MMpro_NS"    in corPro): # corPro == 18
            coutN = 18
        else:
            coutN = 1
        if("Test_P" in corPro): # Not a real correction (adds +20 MeV to proton (+0.02))
            coutN = 16
        if("Test_M" in corPro): # Not a real correction (adds -20 MeV to proton (-0.02))
            coutN = 17
        return coutN


    def CorDpp(Data_Frame, Correction, Out_Type, Channel_Type, MM_Type, Data_Type, Extra_Cut):
        # Correction --> Name of Correction (string)
        # Out_Type --> Desired output of this function
            # Examples:
                # (*) 'MM' ---> Missing Mass Calculation (changes with MM_Type)
                # (*) 'D_p' --> ∆P Calculation 
                    # Options are:
                        # 'D_pel' (Default of SP Channel)
                        # 'D_pip' 
                        # 'D_pro' (Default of DP and P0 Channels)
                        # 'D_pim' (NOT AVAILABLE - must use Nick's Code)
                # (*) 'D_Angle' -> ∆Theta/∆Phi Calculation (only for the elastic proton calulation - as of 9/16/2022)
                # (*) 'Mom' --> Corrected Momentum (same options as ∆P regarding particle choice - will default to the electron)
                # (*) "WM" ---> Invariant Mass      
        # Channel_Type --> Name of channel (i.e., event_type)
        # Data_Type --> Whether the correction is for the 'Inbending' or 'Outbending' data

        Full_Correction_Output = ""

        # Correction Numbers (for code - translating the input string into integers for C++):
        corEl_Num  = str(NameElCor( Correction, Data_Type))
        corPip_Num = str(NamePipCor(Correction, Data_Type))
        corPim_Num = str(NamePimCor(Correction, Data_Type))
        corPro_Num = str(NameProCor(Correction, Data_Type))


        # Correction Choice (Inbending/Outbending):
        if("In" in Data_Type):
            Correction_Code = Correction_Code_Full_In
        else:
            Correction_Code = Correction_Code_Full_Out


        # Particles for Correction:
        Particles_for_Correction = "".join(["""
    auto fe = dppC(ex, ey, ez, esec, 0, """,    str(corEl_Num), """, """, str(corPip_Num), """, """, str(corPim_Num), """, """, str(corPro_Num), """) + 1;
    auto eleC = ROOT::Math::PxPyPzMVector(ex*fe, ey*fe, ez*fe, 0);
        """]) if("(GEN)" not in event_Name) else "".join(["""
    auto fe = dppC(ex0, ey0, ez0, esec, 0, """, str(corEl_Num), """, """, str(corPip_Num), """, """, str(corPim_Num), """, """, str(corPro_Num), """) + 1;
    auto eleC = ROOT::Math::PxPyPzMVector(ex0*fe, ey0*fe, ez0*fe, 0);
        """])

        if("P0" not in Channel_Type and "E" not in Channel_Type and ("Mom_el" not in Out_Type and "Mom_pim" not in Out_Type and "Mom_pro" not in Out_Type)):
            if(("_ELPipMM" not in Correction) or ("Pass 2" not in str(pass_version))):
                Particles_for_Correction = f"""{Particles_for_Correction}
        auto fpip = dppC(pipx, pipy, pipz, pipsec, 1, {corEl_Num}, {corPip_Num}, {corPim_Num}, {corPro_Num}) + 1;
        auto pipC = ROOT::Math::PxPyPzMVector(pipx*fpip, pipy*fpip, pipz*fpip, {Particle_Mass_PiC});
            """
            else:
                pion_det_def = """
                if(pipsec < 7){pion_det = 2;} // Forward Detector
                else{pion_det = 3;          } // Central Detector
                """
                Particles_for_Correction = f"""{Particles_for_Correction}
        {Pion_Energy_Loss_Cor_Function}
        int pion_det;
        {pion_det_def}
        auto p_pip_loss = eloss_pip(pip, pipth, pion_det, {"false" if("In" in Data_Type) else "true"});
        auto f_pip_loss = ((pip+p_pip_loss)/pip);
        auto fpip = dppC(pipx*f_pip_loss, pipy*f_pip_loss, pipz*f_pip_loss, pipsec, 1, {corEl_Num}, {corPip_Num}, {corPim_Num}, {corPro_Num}) + 1;
        auto pipC = ROOT::Math::PxPyPzMVector(pipx*f_pip_loss*fpip, pipy*f_pip_loss*fpip, pipz*f_pip_loss*fpip, {Particle_Mass_PiC});
            """

        if("DP" in Channel_Type and "E" not in Channel_Type and ("Mom_el" not in Out_Type and "Mom_pip" not in Out_Type and "Mom_pro" not in Out_Type)):
            Particles_for_Correction = "".join([Particles_for_Correction, """
    auto fpim = dppC(pimx, pimy, pimz, pimsec, 2, """, str(corEl_Num), """, """, str(corPip_Num), """, """, str(corPim_Num), """, """, str(corPro_Num), """) + 1;
    auto pimC = ROOT::Math::PxPyPzMVector(pimx*fpim, pimy*fpim, pimz*fpim, """, str(Particle_Mass_PiC), """);//0.13957);
        """])


        if("SP" not in Channel_Type and "MC" not in Channel_Type and "EO" not in Channel_Type and ("Mom_el" not in Out_Type and "Mom_pip" not in Out_Type and "Mom_pim" not in Out_Type)):
            if(("_NoELC" not in Correction) and ("MC" not in event_Name)):
                Particles_for_Correction = "".join(["""
            """, Particles_for_Correction, """
    auto fpro = dppC(prox_cor, proy_cor, proz_cor, prosec, 3, """, str(corEl_Num), """, """, str(corPip_Num), """, """, str(corPim_Num), """, """, str(corPro_Num), """) + 1;
    auto proC = ROOT::Math::PxPyPzMVector(prox_cor*fpro, proy_cor*fpro, proz_cor*fpro, """, str(Particle_Mass_Proton), """);//0.938);
            """])

            else: # If "_NoELC" is in 'Correction', then the proton energy loss correction is not applied

                Particles_for_Correction = "".join(["""

            """, Particles_for_Correction, """
    auto fpro = dppC(prox, proy, proz, prosec, 3, """, str(corEl_Num), """, """, str(corPip_Num), """, """, str(corPim_Num), """, """, str(corPro_Num), """) + 1;
    auto proC = ROOT::Math::PxPyPzMVector(prox*fpro, proy*fpro, proz*fpro, """, str(Particle_Mass_Proton), """);//0.938);
            """])

        if("Mom" in Out_Type and "Mom_el" not in Out_Type):
            Particles_for_Correction = Particles_for_Correction.replace("auto fe", "// auto fe")
            Particles_for_Correction = Particles_for_Correction.replace("auto eleC", "// auto eleC")



        # Calculation Choice
        Calculation_Code_Choice = ""


        ##========================================================##
        ##===============||----------------------||===============##
        ##===============||    Invariant Mass    ||===============##
        ##===============||----------------------||===============##
        ##========================================================##
        if("WM" in Out_Type):
            Calculation_Code_Choice = "".join(["""
    auto Output_Vectors = beam + targ - eleC;
    auto Final_Output = Output_Vectors.M""", "2" if(Out_Type == "WM2") else "","""();

            """])


        ##======================================================##
        ##===============||--------------------||===============##
        ##===============||    Missing Mass    ||===============##
        ##===============||--------------------||===============##
        ##======================================================##
        if("MM" in Out_Type):

            ##==============================================##
            ##=====##   Single Pion (eπ+N) Channel   ##=====##
            ##==============================================##
            if('epipX' == MM_Type and Channel_Type != "P0"):
                Calculation_Code_Choice = """
    auto Output_Vectors = beam + targ - eleC - pipC;
    auto Final_Output = Output_Vectors.M();
                """

            ##================================================##
            ##=====##   Double Pion (epπ+π-) Channel   ##=====##
            ##================================================##
            if('eppippimX' == MM_Type and Channel_Type == "DP"):
                Calculation_Code_Choice = """
    auto Output_Vectors = beam + targ - eleC - proC - pipC - pimC;
    auto Final_Output = Output_Vectors.M2();
                """

            if('eppipX'    == MM_Type and Channel_Type == "DP"):
                Calculation_Code_Choice = """
    auto Output_Vectors = beam + targ - eleC - pipC - proC;
    auto Final_Output = Output_Vectors.M2();
                """

            if('eppimX'    == MM_Type and Channel_Type == "DP"):
                Calculation_Code_Choice = """
    auto Output_Vectors = beam + targ - eleC - pimC - proC;
    auto Final_Output = Output_Vectors.M2();
                """

            if('epippimX'  == MM_Type and Channel_Type == "DP"):
                Calculation_Code_Choice = """
    auto Output_Vectors = beam + targ - eleC - pipC - pimC;
    auto Final_Output = Output_Vectors.M();
                """

            if('epX'       == MM_Type and Channel_Type == "DP"):
                Calculation_Code_Choice = """
    auto Output_Vectors = beam + targ - eleC - proC;
    auto Final_Output = Output_Vectors.M2();
                """

            ##==================================================##
            ##=====##   Pi0/Elastic Scattering Channel   ##=====##
            ##==================================================##
            if(MM_Type in ['eppi0X', 'epX'] or Channel_Type in ["P0", "ES"]):
                Calculation_Code_Choice = """
    auto Output_Vectors = beam + targ - eleC - proC;
    auto Final_Output = Output_Vectors.M2();
                """

            ##==================================================##
            ##=====##       Electron Only Channel        ##=====##
            ##==================================================##
            if(MM_Type in ['eX'] or Channel_Type in ["EO"]):
                Calculation_Code_Choice = "".join(["""
        auto Output_Vectors = beam + targ - eleC;
        auto Final_Output = Output_Vectors.M""", "2" if("2" in Out_Type) else "", """();
                """])

        ##========================================================##
        ##===============||----------------------||===============##
        ##===============||    ∆P Calculation    ||===============##
        ##===============||----------------------||===============##
        ##========================================================##
        if("D_p" in Out_Type):

            ##=============================================================##
            ##===============||---------------------------||===============##
            ##===============||    Single Pion Channel    ||===============##
            ##===============||---------------------------||===============##
            ##=============================================================##
            if(Channel_Type in ["SP", "MC"]):
                Calculation_Code_Choice = "".join(["""
    double neutronM2 = """, str(Particle_Mass_Neutron), "*", str(Particle_Mass_Neutron), """;//0.9396*0.9396;
                """])
                if("D_pip" in Out_Type):
                    ##================================================================================================##
                    ##=====================##         ∆P (Single Pion - π+) Calculations         ##===================##
                    ##================================================================================================##
                    Calculation_Code_Choice = "".join([Calculation_Code_Choice, """
    double Proton_M  = """, str(Particle_Mass_Proton), """;
    double Pion_C_M  = """, str(Particle_Mass_PiC), """;
    
    // Below are the kinematic calculations of the π+ momentum (from el+pro->el+Pip+N) based on the assumption that the π+ angle and electron reconstruction were measured by the detector correctly for exclusive events in the epipX channel
    // (The neutron is used as the "missing" particle)

    auto termA = (neutronM2 - (Proton_M*Proton_M) - (Pion_C_M*Pion_C_M))/2;
    auto termB = Proton_M*(Beam_Energy - eleC.P()) - Beam_Energy*eleC.P()*(1 - cos(eleC.Theta()));
    auto termC = ((eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, pipC))) - (Beam_Energy*cos(pipC.Theta())));

    auto sqrtTerm = ((termA - termB)*(termA - termB)) + (Pion_C_M*Pion_C_M)*((termC*termC) - ((Proton_M + Beam_Energy - eleC.P())*(Proton_M + Beam_Energy - eleC.P())));
    auto denominator = ((Proton_M + Beam_Energy - eleC.P()) + termC)*((Proton_M + Beam_Energy - eleC.P()) - termC);
    auto numeratorP = (termA - termB)*termC + (Proton_M + Beam_Energy - eleC.P())*sqrt(sqrtTerm);
    auto numeratorM = (termA - termB)*termC - (Proton_M + Beam_Energy - eleC.P())*sqrt(sqrtTerm);

    auto pip_CalculateP = numeratorP/denominator;
    auto pip_CalculateM = numeratorM/denominator;

    auto pip_Calculate = pip_CalculateP;

    if(abs(pipC.P() - pip_CalculateP) >= abs(pipC.P() - pip_CalculateM)){
        pip_Calculate = pip_CalculateM;
    }
    if(abs(pipC.P() - pip_CalculateP) <= abs(pipC.P() - pip_CalculateM)){
        pip_Calculate = pip_CalculateP;
    }

    auto Final_Output = pip_Calculate - pipC.P();

                    """])

                if("D_pel" in Out_Type):
                    ##======================================================================================================##
                    ##=====================##         ∆P (Single Pion - Electron) Calculations         ##===================##
                    ##======================================================================================================##
                    Calculation_Code_Choice = "".join([Calculation_Code_Choice, """
    double Proton_M  = """, str(Particle_Mass_Proton), """;
    double Pion_C_M  = """, str(Particle_Mass_PiC), """;
    
    // Below are the kinematic calculations of the electron momentum (from el+pro->el+Pip+N) based on the assumption that the electron angle and π+ reconstruction were measured by the detector correctly for exclusive events in the epipX channel
    // (The neutron is used as the "missing" particle)

    auto termA = ((neutronM2 - (Proton_M*Proton_M) - (Pion_C_M*Pion_C_M))/2) - Proton_M*Beam_Energy;
        // termA --> (("Neutron Mass Squared" - "Proton Mass Squared" - "π+ Mass Squared")/2) - "Proton Mass"*"Initial Electron Beam Energy"

    auto termB = pipC.E() - pipC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, pipC)) - Beam_Energy*(1 - cos(eleC.Theta())) - Proton_M;
        // termB --> "π+ Energy" - "π+ Momentum"*cos("Angle between Electron and π+") - "Initial Electron Beam Energy"*(1 - cos("Electron Theta")) - "Proton Mass"

    auto termC = Beam_Energy*(pipC.E() - pipC.P()*cos(pipC.Theta())) + Proton_M*pipC.E();
        // termC --> "Initial Electron Beam Energy"*("π+ Energy" - "π+ Momentum"*cos("π+ Theta")) + "Proton Mass"*"π+ Energy"

    auto pel_Calculated = (termA + termC)/termB;

    auto Final_Output = pel_Calculated - eleC.P();

                    """])



    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



            ##=============================================================##
            ##===============||---------------------------||===============##
            ##===============||    Double Pion Channel    ||===============##
            ##===============||---------------------------||===============##
            ##=============================================================## 
            if(Channel_Type == "DP"):
                if("D_pro" in Out_Type):
                    ##=================================================================================================##
                    ##=====================##         ∆P (Double Pion - Pro) Calculations         ##===================##
                    ##=================================================================================================##
                    Calculation_Code_Choice = "".join(["""
    double Proton_M  = """, str(Particle_Mass_Proton), """;

    // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pip+pim) based on the assumption that the proton angle and electron/π+ reconstruction were measured by the detector correctly for exclusive events in the ep->epπ+π- channel 
    // (π- is used as a "missing" particle)

    auto termA1 = pipC.E() + eleC.P() - Beam_Energy - Proton_M;
    // termA1 = "π+ Energy" + "Electron Momentum" - "Initial Beam Energy" - "Proton Mass"

    auto termB1 = Beam_Energy*cos(proC.Theta()) - eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC)) - pipC.P()*cos(ROOT::Math::VectorUtil::Angle(pipC, proC));
    // termB1 = "Initial Beam Energy"*cos("Proton Theta Angle") - "Electron Momentum" * cos("Angle between the Proton and Electron") - "π+ Momentum" * cos("Angle between the Proton and π+")

    auto termC1 = (Proton_M)*(Beam_Energy - eleC.P() - pipC.E() + (Proton_M)) - Beam_Energy*(eleC.P()*(1 - cos(eleC.Theta())) + (pipC.E() - pipC.P()*cos(pipC.Theta()))) + eleC.P()*(pipC.E() - pipC.P()*cos(ROOT::Math::VectorUtil::Angle(pipC, eleC)));
    // termC1 = "Proton Mass"*("Initial Beam Energy" - "Electron Momentum" - "π+ Energy" + "Proton Mass") - "Initial Beam Energy" * ("Electron Momentum" * (1 - cos("Electron Angle")) + ("π+ Energy" - "π+ Momentum" * cos("π+ Angle"))) + "Electron Momentum" * ("π+ Energy" - "π+ Momentum" * cos("Angle between the π+ and Electron"))

    auto termA2 = (termA1*termA1 - termB1*termB1);
    auto termB2 = -2*termB1*termC1;
    auto termC2 = termA1*termA1*(Proton_M)*(Proton_M) - termC1*termC1;

    auto pro_CalculateP = (-termB2 + sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);
    auto pro_CalculateM = (-termB2 - sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);

    auto pro_Calculate = pro_CalculateP;

    if(abs(proC.P() - pro_CalculateP) <= abs(proC.P() - pro_CalculateM)){
        pro_Calculate = pro_CalculateP;
    }
    else{
        pro_Calculate = pro_CalculateM;
    }
    
    if(pro_CalculateP < 0){
        pro_Calculate = pro_CalculateM;
    }
    if(pro_CalculateM < 0){
        pro_Calculate = pro_CalculateP;
    }


    auto Final_Output = pro_Calculate - proC.P();
    
                        """])
                    
                if("D_p_L_pro" in Out_Type):
                    # print("".join([color.BOLD, "TEST LARGER ∆P", color.END]))
                    ##========================================================================================================================##
                    ##=====================##         ∆P (Double Pion - Pro) Calculations - Larger ∆P Calc Value         ##===================##
                    ##========================================================================================================================##
                    Calculation_Code_Choice = "".join(["""
    double Proton_M  = """, str(Particle_Mass_Proton), """;
    
    // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pip+pim) based on the assumption that the proton angle and electron/π+ reconstruction were measured by the detector correctly for exclusive events in the ep->epπ+π- channel 
    // (π- is used as a "missing" particle)

    auto termA1 = pipC.E() + eleC.P() - Beam_Energy - Proton_M;
    // termA1 = "π+ Energy" + "Electron Momentum" - "Initial Beam Energy" - "Proton Mass"

    auto termB1 = Beam_Energy*cos(proC.Theta()) - eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC)) - pipC.P()*cos(ROOT::Math::VectorUtil::Angle(pipC, proC));
    // termB1 = "Initial Beam Energy"*cos("Proton Theta Angle") - "Electron Momentum" * cos("Angle between the Proton and Electron") - "π+ Momentum" * cos("Angle between the Proton and π+")

    auto termC1 = (Proton_M)*(Beam_Energy - eleC.P() - pipC.E() + (Proton_M)) - Beam_Energy*(eleC.P()*(1 - cos(eleC.Theta())) + (pipC.E() - pipC.P()*cos(pipC.Theta()))) + eleC.P()*(pipC.E() - pipC.P()*cos(ROOT::Math::VectorUtil::Angle(pipC, eleC)));
    // termC1 = "Proton Mass"*("Initial Beam Energy" - "Electron Momentum" - "π+ Energy" + "Proton Mass") - "Initial Beam Energy" * ("Electron Momentum" * (1 - cos("Electron Angle")) + ("π+ Energy" - "π+ Momentum" * cos("π+ Angle"))) + "Electron Momentum" * ("π+ Energy" - "π+ Momentum" * cos("Angle between the π+ and Electron"))

    auto termA2 = (termA1*termA1 - termB1*termB1);
    auto termB2 = -2*termB1*termC1;
    auto termC2 = termA1*termA1*(Proton_M)*(Proton_M) - termC1*termC1;

    auto pro_CalculateP = (-termB2 + sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);
    auto pro_CalculateM = (-termB2 - sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);

    auto pro_Calculate = pro_CalculateP;

    if(abs(proC.P() - pro_CalculateP) <= abs(proC.P() - pro_CalculateM)){
        pro_Calculate = pro_CalculateM;
    }
    else{
        pro_Calculate = pro_CalculateP;
    }
    
    if(pro_CalculateP < 0){
        pro_Calculate = pro_CalculateM;
    }
    if(pro_CalculateM < 0){
        pro_Calculate = pro_CalculateP;
    }

    auto Final_Output = pro_Calculate - proC.P();
    
    
                        """])
                    
                if("D_p_S_pro" in Out_Type):
                    # print("".join([color.BOLD, "TEST SET ∆P", color.END]))
                    ##=======================================================================================================================##
                    ##=====================##          ∆P (Double Pion - Pro) Calculations - Set ∆P Calc Value          ##===================##
                    ##=======================================================================================================================##
                    Calculation_Code_Choice = "".join(["""
    double Proton_M  = """, str(Particle_Mass_Proton), """;

    // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pip+pim) based on the assumption that the proton angle and electron/π+ reconstruction were measured by the detector correctly for exclusive events in the ep->epπ+π- channel 
    // (π- is used as a "missing" particle)
    // Uses condition which tries to use the Missing Mass value of each event to help select the ∆P value used

    auto termA1 = pipC.E() + eleC.P() - Beam_Energy - (Proton_M);
    // termA1 = "π+ Energy" + "Electron Momentum" - "Initial Beam Energy" - "Proton Mass"

    auto termB1 = Beam_Energy*cos(proC.Theta()) - eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC)) - pipC.P()*cos(ROOT::Math::VectorUtil::Angle(pipC, proC));
    // termB1 = "Initial Beam Energy"*cos("Proton Theta Angle") - "Electron Momentum" * cos("Angle between the Proton and Electron") - "π+ Momentum" * cos("Angle between the Proton and π+")

    auto termC1 = (Proton_M)*(Beam_Energy - eleC.P() - pipC.E() + (Proton_M)) - Beam_Energy*(eleC.P()*(1 - cos(eleC.Theta())) + (pipC.E() - pipC.P()*cos(pipC.Theta()))) + eleC.P()*(pipC.E() - pipC.P()*cos(ROOT::Math::VectorUtil::Angle(pipC, eleC)));
    // termC1 = "Proton Mass"*("Initial Beam Energy" - "Electron Momentum" - "π+ Energy" + "Proton Mass") - "Initial Beam Energy" * ("Electron Momentum" * (1 - cos("Electron Angle")) + ("π+ Energy" - "π+ Momentum" * cos("π+ Angle"))) + "Electron Momentum" * ("π+ Energy" - "π+ Momentum" * cos("Angle between the π+ and Electron"))

    auto termA2 = (termA1*termA1 - termB1*termB1);
    auto termB2 = -2*termB1*termC1;
    auto termC2 = termA1*termA1*(Proton_M)*(Proton_M) - termC1*termC1;

    auto pro_CalculateP = (-termB2 + sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);
    auto pro_CalculateM = (-termB2 - sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);

    auto pro_Calculate = pro_CalculateP;

    // Selecting based on closest match to the measured momentum
    if(abs(proC.P() - pro_CalculateP) <= abs(proC.P() - pro_CalculateM)){
        pro_Calculate = pro_CalculateP;
    }
    else{
        pro_Calculate = pro_CalculateM;
    }
    
    
    // Biasing selection based on Missing Mass
    if(((pro_CalculateP - proC.P())*(pro_CalculateM - proC.P())) < 0){
        // The above condition checks to see if the 2 possible values of ∆P will have the same sign (the signs would cancel to be positive if they are the same)
        // The following conditions would not matter if both values of ∆P would have the same sign
        auto beam_test = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
        auto targ_test = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_M);
        auto MM2_Vec = beam_test + targ_test - eleC - pipC - proC;
        auto MM2_Val = MM2_Vec.M2();
        auto Pion_C_M  = """, str(Particle_Mass_PiC), """;
        // auto MM2_Tru = (Pion_C_M*Pion_C_M);
        auto MM2_Dif = (Pion_C_M*Pion_C_M) - MM2_Val;
        if((MM2_Dif < 0)){ // If the Measured Missing Mass is GREATER than the Ideal Missing Mass...
            if((pro_CalculateP - proC.P()) > 0){ // ∆P should be negative if MM2_Dif is also negative
                pro_Calculate = pro_CalculateM;
            }
            if((pro_CalculateM - proC.P()) > 0){ // ∆P should be negative if MM2_Dif is also negative
                pro_Calculate = pro_CalculateP;
            }
        }
        if((MM2_Dif > 0)){ // If the Measured Missing Mass is LESS than the Ideal Missing Mass...
            if((pro_CalculateP - proC.P()) > 0){ // ∆P should NOT be negative if MM2_Dif is positive
                pro_Calculate = pro_CalculateP;
            }
            if((pro_CalculateM - proC.P()) > 0){ // ∆P should NOT be negative if MM2_Dif is positive
                pro_Calculate = pro_CalculateM;
            }
        }
        
        """, "".join(["""
        std::cout<<"====================================================================================================="<<std::endl;
        std::cout<<"(D_p_S_pro) Proton Correction = """, str(Correction), """"<<std::endl;
        std::cout<<"Sector = "<<prosec<<std::endl;
        std::cout<<"MM2 (Ideal)              = "<<(Pion_C_M*Pion_C_M)<<std::endl;
        std::cout<<"MM2 (Corrected)          = "<<MM2_Val<<std::endl;
        std::cout<<""<<std::endl;
        std::cout<<"proC.P()                 = "<<proC.P()<<std::endl;
        std::cout<<"pro_CalculateP           = "<<pro_CalculateP<<std::endl;
        std::cout<<"pro_CalculateM           = "<<pro_CalculateM<<std::endl;
        std::cout<<"pro_Calculate            = "<<pro_Calculate<<std::endl;
        std::cout<<""<<std::endl;
        std::cout<<"∆P (pro_P - proC.P())    = "<<pro_CalculateP - proC.P()<<std::endl;
        std::cout<<"∆P (pro_M - proC.P())    = "<<pro_CalculateM - proC.P()<<std::endl;
        std::cout<<"∆P (pro_C - proC.P())    = "<<pro_Calculate - proC.P()<<std::endl;
        std::cout<<std::endl<<std::endl;
        std::cout<<"====================================================================================================="<<std::endl;
        """]) if(False and (str(Correction) in ["mm0_NoELC", "mm0_Test_P_NoELC", "mm0_Test_M_NoELC", "mm0_Test_P", "mm0_Test_M", "mmEF_PipMMEF_ProMMpro_NRE"])) else "", """
    }
    
    
    // Requiring the calculated momentum be a postive value (impossible correction otherwise)
    if(pro_CalculateP < 0){
        pro_Calculate = pro_CalculateM;
    }
    if(pro_CalculateM < 0){
        pro_Calculate = pro_CalculateP;
    }

    
    
    auto Final_Output = pro_Calculate - proC.P();
    
    
                        """])
                    
                if("D_p_F_pro" in Out_Type):
                    # print("".join([color.BOLD, "TEST FLIP ∆P", color.END]))
                    ##========================================================================================================================##
                    ##=====================##          ∆P (Double Pion - Pro) Calculations - Flip ∆P Calc Value          ##===================##
                    ##========================================================================================================================##
                    Calculation_Code_Choice = "".join(["""
    double Proton_M  = """, str(Particle_Mass_Proton), """;
    double Pion_C_M  = """, str(Particle_Mass_PiC), """;
    
    // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pip+pim) based on the assumption that the proton angle and electron/π+ reconstruction were measured by the detector correctly for exclusive events in the ep->epπ+π- channel 
    // (π- is used as a "missing" particle)
    // Uses condition which tries to use the Missing Mass value of each event to help select the ∆P value used (Flips after a certian value of momentum)

    auto termA1 = pipC.E() + eleC.P() - Beam_Energy - (Proton_M);
    // termA1 = "π+ Energy" + "Electron Momentum" - "Initial Beam Energy" - "Proton Mass"

    auto termB1 = Beam_Energy*cos(proC.Theta()) - eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC)) - pipC.P()*cos(ROOT::Math::VectorUtil::Angle(pipC, proC));
    // termB1 = "Initial Beam Energy"*cos("Proton Theta Angle") - "Electron Momentum" * cos("Angle between the Proton and Electron") - "π+ Momentum" * cos("Angle between the Proton and π+")

    auto termC1 = (Proton_M)*(Beam_Energy - eleC.P() - pipC.E() + (Proton_M)) - Beam_Energy*(eleC.P()*(1 - cos(eleC.Theta())) + (pipC.E() - pipC.P()*cos(pipC.Theta()))) + eleC.P()*(pipC.E() - pipC.P()*cos(ROOT::Math::VectorUtil::Angle(pipC, eleC)));
    // termC1 = "Proton Mass"*("Initial Beam Energy" - "Electron Momentum" - "π+ Energy" + "Proton Mass") - "Initial Beam Energy" * ("Electron Momentum" * (1 - cos("Electron Angle")) + ("π+ Energy" - "π+ Momentum" * cos("π+ Angle"))) + "Electron Momentum" * ("π+ Energy" - "π+ Momentum" * cos("Angle between the π+ and Electron"))

    auto termA2 = (termA1*termA1 - termB1*termB1);
    auto termB2 = -2*termB1*termC1;
    auto termC2 = termA1*termA1*(Proton_M)*(Proton_M) - termC1*termC1;

    auto pro_CalculateP = (-termB2 + sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);
    auto pro_CalculateM = (-termB2 - sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);

    auto pro_Calculate = pro_CalculateP;

    // Selecting based on closest match to the measured momentum
    if(abs(proC.P() - pro_CalculateP) <= abs(proC.P() - pro_CalculateM)){
        pro_Calculate = pro_CalculateP;
    }
    else{
        pro_Calculate = pro_CalculateM;
    }
    
    
    // Biasing selection based on Missing Mass
    if(((pro_CalculateP - proC.P())*(pro_CalculateM - proC.P())) < 0){
        // The above condition checks to see if the 2 possible values of ∆P will have the same sign (the signs would cancel to be positive if they are the same)
        // The following conditions would not matter if both values of ∆P would have the same sign
        auto beam_test = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
        auto targ_test = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_M);
        auto MM2_Vec = beam_test + targ_test - eleC - pipC - proC;
        auto MM2_Val = MM2_Vec.M2();
        // auto MM2_Tru = (Pion_C_M*Pion_C_M);
        auto MM2_Dif = (Pion_C_M*Pion_C_M) - MM2_Val;
        
        if((MM2_Dif < 0)){ // If the Measured Missing Mass is GREATER than the Ideal Missing Mass...
            if(proC.P() < 1.5){ // Switch directions after p = 1.5 GeV...
                if((pro_CalculateP - proC.P()) < 0){ // ∆P should be negative if MM2_Dif is also negative
                    pro_Calculate = pro_CalculateP;
                }
                if((pro_CalculateM - proC.P()) < 0){ // ∆P should be negative if MM2_Dif is also negative
                    pro_Calculate = pro_CalculateM;
                }
            }
            else{ // For Momentum above 1.5 GeV
                if((pro_CalculateP - proC.P()) < 0){ // ∆P should NOT be negative if MM2_Dif is negative
                    pro_Calculate = pro_CalculateM;
                }
                if((pro_CalculateM - proC.P()) < 0){ // ∆P should NOT be negative if MM2_Dif is negative
                    pro_Calculate = pro_CalculateP;
                }
            }
        }
        if((MM2_Dif > 0)){ // If the Measured Missing Mass is LESS than the Ideal Missing Mass...
            if(proC.P() > 1.5){ // Switch directions after p = 1.5 GeV...
                if((pro_CalculateP - proC.P()) < 0){ // ∆P should be negative if MM2_Dif is positive
                    pro_Calculate = pro_CalculateP;
                }
                if((pro_CalculateM - proC.P()) < 0){ // ∆P should be negative if MM2_Dif is positive
                    pro_Calculate = pro_CalculateM;
                }
            }
            else{ // For Momentum below 1.5 GeV
                if((pro_CalculateP - proC.P()) < 0){ // ∆P should NOT be negative if MM2_Dif is also positive
                    pro_Calculate = pro_CalculateM;
                }
                if((pro_CalculateM - proC.P()) < 0){ // ∆P should NOT be negative if MM2_Dif is also positive
                    pro_Calculate = pro_CalculateP;
                }
            }
        }
        
        """, "".join(["""
        std::cout<<"====================================================================================================="<<std::endl;
        std::cout<<"(D_p_F_pro) Proton Correction = """, str(Correction), """"<<std::endl;
        std::cout<<"Sector = "<<prosec<<std::endl;
        std::cout<<"MM2 (Ideal)              = "<<(Pion_C_M*Pion_C_M)<<std::endl;
        std::cout<<"MM2 (Corrected)          = "<<MM2_Val<<std::endl;
        std::cout<<""<<std::endl;
        std::cout<<"proC.P()                 = "<<proC.P()<<std::endl;
        std::cout<<"pro_CalculateP           = "<<pro_CalculateP<<std::endl;
        std::cout<<"pro_CalculateM           = "<<pro_CalculateM<<std::endl;
        std::cout<<"pro_Calculate            = "<<pro_Calculate<<std::endl;
        std::cout<<""<<std::endl;
        std::cout<<"∆P (pro_P - proC.P())    = "<<pro_CalculateP - proC.P()<<std::endl;
        std::cout<<"∆P (pro_M - proC.P())    = "<<pro_CalculateM - proC.P()<<std::endl;
        std::cout<<"∆P (pro_C - proC.P())    = "<<pro_Calculate - proC.P()<<std::endl;
        std::cout<<std::endl<<std::endl;
        std::cout<<"====================================================================================================="<<std::endl;
        """]) if(False and (str(Correction) in ["mm0_NoELC", "mm0_Test_P_NoELC", "mm0_Test_M_NoELC", "mm0_Test_P", "mm0_Test_M", "mmEF_PipMMEF_ProMMpro_NRE"])) else "", """
    }
    
    
    // Requiring the calculated momentum be a postive value (impossible correction otherwise)
    if(pro_CalculateP < 0){
        pro_Calculate = pro_CalculateM;
    }
    if(pro_CalculateM < 0){
        pro_Calculate = pro_CalculateP;
    }

    auto Final_Output = pro_Calculate - proC.P();
    
    
                        """])
                    
                    
                    
                    
    
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



            ##=========================================================##
            ##===============||-----------------------||===============##
            ##===============||    π0 Pion Channel    ||===============##
            ##===============||-----------------------||===============##
            ##=========================================================## 
            if(Channel_Type == "P0"):
                if("D_pro" in Out_Type or "D_p_a_pro" in Out_Type or "D_p_b_pro" in Out_Type or "D_p_c_pro" in Out_Type or "D_p_sqrt_pro" in Out_Type):
                    ##=====================================================================================================##
                    ##=====================##         ∆P (π0 Pion Channel - Pro) Calculations         ##===================##
                    ##=====================================================================================================##
                    Calculation_Code_Choice = "".join(["""
    // double pi0M2term = (0.13498*0.13498)/2;
    double pi0M2term = (""", str(Particle_Mass_Pi0), """*""", str(Particle_Mass_Pi0), """)/2;
    double Proton_M  = """, str(Particle_Mass_Proton), """;
    
    // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pi0) based on the assumption that the proton angle and electron reconstruction were measured by the detector correctly for exclusive events in the ep->epπ0 channel
    // (π0 is used as the "missing" particle)


    auto termA1 = pi0M2term - (Proton_M)*((Beam_Energy) - eleC.P() + (Proton_M)) + (Beam_Energy)*eleC.P()*(1 - cos(eleC.Theta()));
        // termA1 = pi0M2term - "Proton Mass"*("Initial Beam Energy" - "Electron Momentum" + "Proton Mass") + "Initial Beam Energy"*"Electron Momentum"*(1 - cos("Electron Theta Angle"))

    auto termB1 = (Beam_Energy)*cos(proC.Theta()) - eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC));
        // termB1 = "Initial Beam Energy"*cos("Proton Theta Angle") - "Electron Momentum"*cos("Angle between the Proton and Electron")

    auto termC1 = eleC.P() - (Beam_Energy) - (Proton_M);
        // termC1 = "Electron Momentum" - "Initial Beam Energy" - "Proton Mass"

    auto termA2 = (termB1*termB1 - termC1*termC1);
    auto termB2 = -2*termB1*termA1;
    auto termC2 = termA1*termA1 - termC1*termC1*(Proton_M)*(Proton_M);
    
    auto sqrtTerm = termB2*termB2 - 4*termA2*termC2;
    
    auto pro_CalculateP = (-termB2 + sqrt(sqrtTerm)) / (2*termA2);
    auto pro_CalculateM = (-termB2 - sqrt(sqrtTerm)) / (2*termA2);

    auto pro_Calculate = pro_CalculateP;

    if(abs(proC.P() - pro_CalculateP) <= abs(proC.P() - pro_CalculateM)){
        pro_Calculate = pro_CalculateP;
    }
    else{
        pro_Calculate = pro_CalculateM;
    }

    if(pro_CalculateP < 0){
        pro_Calculate = pro_CalculateM;
    }
    if(pro_CalculateM < 0){
        pro_Calculate = pro_CalculateP;
    }
    auto Final_Output = pro_Calculate - proC.P();
    
    """, "".join(["""
    if(Final_Output > 0.007 || Final_Output < -0.007){
        auto MM_Vector = beam + targ - eleC - proC;
        auto MM2_Value = MM_Vector.M2();
        auto fpro_new  = (pro_Calculate/proC.P());
        auto proC_New  = ROOT::Math::PxPyPzMVector(prox*fpro_new, proy*fpro_new, proz*fpro_new, Proton_M);
        auto MM_Vector_New = beam + targ - eleC - proC_New;
        auto MM2_Value_New = MM_Vector_New.M2();
        std::cout<<"====================================================================================================="<<std::endl;
        std::cout<<"(""", str(Out_Type), """) Proton Correction = """, str(Correction), """"<<std::endl;
        std::cout<<"Sector = "<<prosec<<std::endl;
        std::cout<<"MM2 (Ideal)               = "<<(""", str(Particle_Mass_Pi0), """*""", str(Particle_Mass_Pi0), """)<<std::endl;
        std::cout<<"MM2 (Initial)             = "<<MM2_Value<<std::endl;
        std::cout<<"MM2 (Corrected)           = "<<MM2_Value_New<<std::endl;
        std::cout<<""<<std::endl;
        std::cout<<"term_A                    = "<<termA2<<std::endl;
        std::cout<<"term_B                    = "<<termB2<<std::endl;
        std::cout<<"term_C                    = "<<termC2<<std::endl;
        std::cout<<""<<std::endl;
        std::cout<<"Top Term (Plus)           = "<<(-termB2 + sqrt(sqrtTerm))<<std::endl;
        std::cout<<"Top Term (Minus)          = "<<(-termB2 - sqrt(sqrtTerm))<<std::endl;
        std::cout<<"Square Root Term          = "<<(sqrtTerm)<<std::endl;
        std::cout<<""<<std::endl;
        std::cout<<"proC.P()                  = "<<proC.P()<<std::endl;
        std::cout<<"pro_CalculateP            = "<<pro_CalculateP<<std::endl;
        std::cout<<"pro_CalculateM            = "<<pro_CalculateM<<std::endl;
        std::cout<<"Best Calculated Momentum  = "<<pro_Calculate<<std::endl;
        std::cout<<""<<std::endl;
        std::cout<<"proC_New.P() (Corrected)  = "<<proC_New.P()<<std::endl;
        std::cout<<""<<std::endl;
        std::cout<<"∆P (pro_P - proC.P())     = "<<pro_CalculateP - proC.P()<<std::endl;
        std::cout<<"∆P (pro_M - proC.P())     = "<<pro_CalculateM - proC.P()<<std::endl;
        std::cout<<"Best ∆P                   = "<<pro_Calculate - proC.P()<<std::endl;
        std::cout<<""<<std::endl;
        std::cout<<"fpro (New)                = "<<fpro_new<<std::endl;
        std::cout<<"pro_x (Corrected)         = "<<prox*fpro_new<<std::endl;
        std::cout<<"pro_y (Corrected)         = "<<proy*fpro_new<<std::endl;
        std::cout<<"pro_z (Corrected)         = "<<proz*fpro_new<<std::endl;
        std::cout<<""<<std::endl;
        std::cout<<"For Event Selection:"<<std::endl;
        std::cout<<"ex_0                      = "<<ex0<<std::endl;
        std::cout<<"ey_0                      = "<<ey0<<std::endl;
        std::cout<<"ez_0                      = "<<ez0<<std::endl;
        std::cout<<"e_sec                     = "<<esec<<std::endl;
        std::cout<<"eleC.P()                  = "<<eleC.P()<<std::endl;
        std::cout<<std::endl<<std::endl;
        std::cout<<"====================================================================================================="<<std::endl;
    }
    """]) if((True and "(GEN)" in str(event_Name)) and not ("D_p_a_pro" in Out_Type or "D_p_b_pro" in Out_Type or "D_p_c_pro" in Out_Type or "D_p_sqrt_pro" in Out_Type)) else "", """
    """, "Final_Output = termA2;" if("D_p_a_pro" in Out_Type) else "Final_Output = termB2;" if("D_p_b_pro" in Out_Type) else "Final_Output = termC2;" if("D_p_c_pro" in Out_Type) else "Final_Output = sqrtTerm;" if("D_p_sqrt_pro" in Out_Type) else ""])
                    
                    
                if("D_p_L_pro" in Out_Type):
                    ##=================================================================================================================##
                    ##=====================##         ∆P (π0 Pion Channel - Pro) Calculations - Larger ∆P         ##===================##
                    ##=================================================================================================================##
                    Calculation_Code_Choice = "".join(["""
    // double pi0M2term = (0.13498*0.13498)/2;
    double pi0M2term = (""", str(Particle_Mass_Pi0), """*""", str(Particle_Mass_Pi0), """)/2;
    double Proton_M  = """, str(Particle_Mass_Proton), """;
    
    // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pi0) based on the assumption that the proton angle and electron reconstruction were measured by the detector correctly for exclusive events in the ep->epπ0 channel
    // (π0 is used as the "missing" particle)

    auto termA1 = pi0M2term - (Proton_M)*((Beam_Energy) - eleC.P() + (Proton_M)) + (Beam_Energy)*eleC.P()*(1 - cos(eleC.Theta()));
        // termA1 = pi0M2term - "Proton Mass"*("Initial Beam Energy" - "Electron Momentum" + "Proton Mass") + "Initial Beam Energy"*"Electron Momentum"*(1 - cos("Electron Theta Angle"))

    auto termB1 = (Beam_Energy)*cos(proC.Theta()) - eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC));
        // termB1 = "Initial Beam Energy"*cos("Proton Theta Angle") - "Electron Momentum"*cos("Angle between the Proton and Electron")

    auto termC1 = eleC.P() - (Beam_Energy) - (Proton_M);
        // termC1 = "Electron Momentum" - "Initial Beam Energy" - "Proton Mass"

    auto termA2 = (termB1*termB1 - termC1*termC1);
    auto termB2 = -2*termB1*termA1;
    auto termC2 = termA1*termA1 - termC1*termC1*(Proton_M)*(Proton_M);

    auto pro_CalculateP = (-termB2 + sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);
    auto pro_CalculateM = (-termB2 - sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);

    auto pro_Calculate = pro_CalculateM;

    if(abs(proC.P() - pro_CalculateP) <= abs(proC.P() - pro_CalculateM)){
        pro_Calculate = pro_CalculateM;
    }
    else{
        pro_Calculate = pro_CalculateP;
    }

    if(pro_CalculateP < 0){
        pro_Calculate = pro_CalculateP;
    }
    if(pro_CalculateM < 0){
        pro_Calculate = pro_CalculateM;
    }
    
    auto Final_Output = pro_Calculate - proC.P();
    
    """])
                    
                if("D_p_G_pro" in Out_Type):
                    ##=================================================================================================================##
                    ##=====================##         ∆P (π0 Pion Channel - Pro) Calculations - Generated         ##===================##
                    ##=================================================================================================================##
                    Calculation_Code_Choice = "".join(["""
    double Proton_M  = """, str(Particle_Mass_Proton), """;
    // double pi0M2term = (0.13498*0.13498)/2;
    double pi0M2term = (""", str(Particle_Mass_Pi0), """*""", str(Particle_Mass_Pi0), """)/2;
    
    // Generated Proton Momentum:
    auto proG = ROOT::Math::PxPyPzMVector(px0, py0, pz0, Proton_M);

    // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pi0) based on the assumption that the proton angle and electron reconstruction were measured by the detector correctly for exclusive events in the ep->epπ0 channel
    // (π0 is used as the "missing" particle)
    // ∆P is calculated here using the generated momentums instead of reconstructed (for simulated data)

    auto termA1 = pi0M2term - (Proton_M)*((Beam_Energy) - eleC.P() + (Proton_M)) + (Beam_Energy)*eleC.P()*(1 - cos(eleC.Theta()));
        // termA1 = pi0M2term - "Proton Mass"*("Initial Beam Energy" - "Electron Momentum" + "Proton Mass") + "Initial Beam Energy"*"Electron Momentum"*(1 - cos("Electron Theta Angle"))

    auto termB1 = (Beam_Energy)*cos(proC.Theta()) - eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC));
        // termB1 = "Initial Beam Energy"*cos("Proton Theta Angle") - "Electron Momentum"*cos("Angle between the Proton and Electron")

    auto termC1 = eleC.P() - (Beam_Energy) - (Proton_M);
        // termC1 = "Electron Momentum" - "Initial Beam Energy" - "Proton Mass"

    auto termA2 = (termB1*termB1 - termC1*termC1);
    auto termB2 = -2*termB1*termA1;
    auto termC2 = termA1*termA1 - termC1*termC1*(Proton_M)*(Proton_M);

    auto pro_CalculateP = (-termB2 + sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);
    auto pro_CalculateM = (-termB2 - sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);

    auto pro_Calculate = pro_CalculateP;

    if(abs(proG.P() - pro_CalculateP) <= abs(proG.P() - pro_CalculateM)){
        pro_Calculate = pro_CalculateP;
    }
    else{
        pro_Calculate = pro_CalculateM;
    }

    if(pro_CalculateP < 0){
        pro_Calculate = pro_CalculateM;
    }
    if(pro_CalculateM < 0){
        pro_Calculate = pro_CalculateP;
    }

    auto Final_Output = pro_Calculate - proG.P();

                        """])
                    
                    
                if("D_p_gL_pro" in Out_Type):
                    ##=============================================================================================================================##
                    ##=====================##         ∆P (π0 Pion Channel - Pro) Calculations - Generated - Larger ∆P         ##===================##
                    ##=============================================================================================================================##
                    Calculation_Code_Choice = "".join(["""
    double Proton_M  = """, str(Particle_Mass_Proton), """;
    // double pi0M2term = (0.13498*0.13498)/2;
    double pi0M2term = (""", str(Particle_Mass_Pi0), """*""", str(Particle_Mass_Pi0), """)/2;
                    
    // Generated Proton Momentum:
    auto proG = ROOT::Math::PxPyPzMVector(px0, py0, pz0, Proton_M);

    // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pi0) based on the assumption that the proton angle and electron reconstruction were measured by the detector correctly for exclusive events in the ep->epπ0 channel
    // (π0 is used as the "missing" particle)

    auto termA1 = pi0M2term - (Proton_M)*((Beam_Energy) - eleC.P() + (Proton_M)) + (Beam_Energy)*eleC.P()*(1 - cos(eleC.Theta()));
        // termA1 = pi0M2term - "Proton Mass"*("Initial Beam Energy" - "Electron Momentum" + "Proton Mass") + "Initial Beam Energy"*"Electron Momentum"*(1 - cos("Electron Theta Angle"))

    auto termB1 = (Beam_Energy)*cos(proC.Theta()) - eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC));
        // termB1 = "Initial Beam Energy"*cos("Proton Theta Angle") - "Electron Momentum"*cos("Angle between the Proton and Electron")

    auto termC1 = eleC.P() - (Beam_Energy) - (Proton_M);
        // termC1 = "Electron Momentum" - "Initial Beam Energy" - "Proton Mass"

    auto termA2 = (termB1*termB1 - termC1*termC1);
    auto termB2 = -2*termB1*termA1;
    auto termC2 = termA1*termA1 - termC1*termC1*(Proton_M)*(Proton_M);

    auto pro_CalculateP = (-termB2 + sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);
    auto pro_CalculateM = (-termB2 - sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);

    auto pro_Calculate = pro_CalculateM;

    if(abs(proG.P() - pro_CalculateP) <= abs(proG.P() - pro_CalculateM)){
        pro_Calculate = pro_CalculateM;
    }
    else{
        pro_Calculate = pro_CalculateP;
    }

    if(pro_CalculateP < 0){
        pro_Calculate = pro_CalculateP;
    }
    if(pro_CalculateM < 0){
        pro_Calculate = pro_CalculateM;
    }
    
    auto Final_Output = pro_Calculate - proG.P();
    
    """])


                if("D_pel" in Out_Type):
                    ##==========================================================================================================##
                    ##=====================##         ∆P (π0 Pion Channel - Electron) Calculations         ##===================##
                    ##==========================================================================================================##
                    Calculation_Code_Choice = "".join(["""
                    
    double Proton_M  = """, str(Particle_Mass_Proton), """;

    // Below are the kinematic calculations of the electron momentum (from el+pro->el+pro+pi0) based on the assumption that the electron angle and proton reconstruction were measured by the detector correctly for exclusive events in the epπ0 channel
    // (π0 is used as the "missing" particle)

    // auto termA = (0.13498*0.13498)/2;
    auto termA = (""", str(Particle_Mass_Pi0), """*""", str(Particle_Mass_Pi0), """)/2;
        // termA --> "(Pi0 Mass Squared)/2"

    auto termB = termA - (Proton_M)*((Beam_Energy) - proC.E() + (Proton_M)) + (Beam_Energy)*(proC.E() - proC.P()*cos(proC.Theta()));
        // termB --> "0.5*Pi0 Mass^2" - "Proton Mass" * ("Initial Electron Beam Energy" - "Proton Energy" + "Proton Mass") + "Initial Electron Beam Energy" * ("Proton Energy" - "Proton Momentum"*cos("Proton Theta"))

    auto termC = proC.E() - Proton_M - proC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC)) - Beam_Energy*(1 - cos(eleC.Theta()));
        // termC --> "Proton Energy" - "Proton Mass" - "Proton Momentum"*cos("Angle between Electron and Proton") - "Initial Electron Beam Energy"*(1 - cos("Electron Theta"))

    auto pel_Calculated = termB/termC;

    auto Final_Output = pel_Calculated - eleC.P();

                    """])



    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



            ##============================================================##
            ##===============||--------------------------||===============##
            ##===============||    Elastic Scattering    ||===============##
            ##===============||--------------------------||===============##
            ##============================================================## 
            if("E" in Channel_Type):
                if("D_pro" in Out_Type and Channel_Type == "ES"):
                    ##========================================================================================================##
                    ##=====================##         ∆P (Elastic Scattering - Pro) Calculations         ##===================##
                    ##========================================================================================================##
                    Calculation_Code_Choice = "".join(["""
    double Proton_M  = """, str(Particle_Mass_Proton), """;

    // Below are the kinematic calculations of the proton momentum (from el+pro->el'+pro') based on the assumption that the proton angle and electron reconstruction were measured by the detector correctly for elastic events in the ep->e'p' channel

    auto termA1 = 2*eleC.P() - (Beam_Energy);
        // termA1 = 2*"Electron Momentum" - "Initial Beam Energy"

    auto termB1 = eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC)) - (Beam_Energy)*cos(proC.Theta());
        // termB1 = "Electron Momentum"*cos("Angle between the Proton and Electron") - "Initial Beam Energy"*cos("Proton Theta Angle")
        
    auto termC1 = 2*(Beam_Energy)*eleC.P()*(1 - cos(eleC.Theta()));
        // termC1 = 2*"Initial Beam Energy"*"Electron Momentum"*(1 - cos("Electron Theta Angle"))


    auto termA2 = (termB1*termB1 - termA1*termA1);
    auto termB2 = 2*termB1*termC1;
    auto termC2 = termC1*termC1 - termA1*termA1*(Proton_M)*(Proton_M);

    auto pro_CalculateP = (-termB2 + sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);
    auto pro_CalculateM = (-termB2 - sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);

    auto pro_Calculate = pro_CalculateP;

    if(abs(proC.P() - pro_CalculateP) <= abs(proC.P() - pro_CalculateM)){
        pro_Calculate = pro_CalculateP;
    }
    else{
        pro_Calculate = pro_CalculateM;
    }

    auto Final_Output = pro_Calculate - proC.P();

                        """])


                if("D_pel" in Out_Type):
                    ##=============================================================================================================##
                    ##=====================##         ∆P (Elastic Scattering - Electron) Calculations         ##===================##
                    ##=============================================================================================================##
                    Calculation_Code_Choice = "".join(["""
    double Proton_M  = """, str(Particle_Mass_Proton), """;
    
    // Below are the kinematic calculations of the electron momentum (from el+pro->el'+pro') based on the assumption that the electron angle was measured by the detector correctly
    
    auto termA = Beam_Energy*(1 - cos(eleC.Theta())) + Proton_M;
        // termA --> "Initial Electron Beam Energy"*(1 - cos("Electron Theta")) + "Proton Mass"
        
    auto termB = Beam_Energy*Proton_M;
        // termB --> "Initial Electron Beam Energy" * "Proton Mass"
        
    auto pel_Calculated = termB/termA;
    
    auto Final_Output = pel_Calculated - eleC.P();
                    """])


        ##########################################################################################################
        ##======================================================================================================##
        ##==============##============##         Delta P Calculations (End)         ##============##============##
        ##======================================================================================================##
        ##########################################################################################################
        
        
                
        ##=============================================================##
        ##===============||---------------------------||===============##
        ##===============||  ∆Theta/∆Phi Calculation  ||===============##
        ##===============||---------------------------||===============##
        ##=============================================================##
        if("D_Angle" in Out_Type):
            if("D_Angle_V1" in Out_Type):
                try:
                    Calculation_Code_Choice = "".join([Calculation_Code_Choice, """                    
    double Proton_M  = """, str(Particle_Mass_Proton), """;

    // Below are the kinematic calculations of the proton angle (theta) (from elastic scattering) 
    // To be used for exclusivity cuts

    auto Pro_Th_Calc = (proC.Theta())*(180/3.1415926); // Initialize the calculated proton angle as the same value as the measured/corrected proton angle (converted to degrees)

    Pro_Th_Calc = atan(Proton_M/((Beam_Energy + Proton_M)*tan(eleC.Theta()/2)))*(180/3.1415926);

    auto Delta_Theta = ((proC.Theta())*(180/3.1415926)) - Pro_Th_Calc;

    auto Final_Output = Delta_Theta;

                    """])
                except Exception as e:
                    print("\nFAILED ∆Theta CALCULATION (Version 1)\n")
                    print("".join(["ERROR: ", str(e)]))
            elif("D_Angle_V2" in Out_Type):
                try:
                    Calculation_Code_Choice = "".join([Calculation_Code_Choice, """
    double Proton_M  = """, str(Particle_Mass_Proton), """;

    // Below are the kinematic calculations of the proton angle (theta) (from elastic scattering) 
    // To be used for exclusivity cuts

    auto Pro_Th_Calc = (proC.Theta())*(180/3.1415926); // Initialize the calculated proton angle as the same value as the measured/corrected proton angle (converted to degrees)

    Pro_Th_Calc = acos(((Beam_Energy + Proton_M)*(proC.E() - + Proton_M))/(Beam_Energy*proC.P()))*(180/3.1415926);

    auto Delta_Theta = ((proC.Theta())*(180/3.1415926)) - Pro_Th_Calc;

    auto Final_Output = Delta_Theta;

                    """])
                except Exception as e:
                    print("\nFAILED ∆Theta CALCULATION (Version 2)\n")
                    print("".join(["ERROR: ", str(e)]))
            elif("D_Angle_V3" in Out_Type):
                try:
                    Calculation_Code_Choice = "".join([Calculation_Code_Choice, """

    // Below are the sums of the electron and proton azimuthal angles (used to give new kinematic cuts)

    double el_Phi = (180/3.1415926)*eleC.Phi();
    if(el_Phi < 0){
        el_Phi += 360;
    }
    double pro_Phi = (180/3.1415926)*proC.Phi();
    if(pro_Phi < 0){
        pro_Phi += 360;
    }
    double Absolute_Dif_in_Phi = abs(el_Phi - pro_Phi);

    auto Final_Output = Absolute_Dif_in_Phi;

                    """])
                except Exception as e:
                    print("\nFAILED ABSOLUTE ∆Phi CALCULATION\n")
                    print("".join(["ERROR: ", str(e)]))
            elif("D_Angle_V4" in Out_Type):
                try:
                    Calculation_Code_Choice = "".join([Calculation_Code_Choice, """
    double Proton_M  = """, str(Particle_Mass_Proton), """;
    
    // Below are the kinematic calculations of the proton angle (theta) (from elastic scattering) 
    // To be used for exclusivity cuts

    auto Pro_Th_Calc = (proC.Theta())*(180/3.1415926); // Initialize the calculated proton angle as the same value as the measured/corrected proton angle (converted to degrees)

    auto Calc_P_El = (Beam_Energy*Proton_M)/((Beam_Energy*(1 - cos(eleC.Theta()))) + Proton_M);
    auto Calc_Terms_1 = Beam_Energy*Calc_P_El*(1 - cos(eleC.Theta()));
    
    auto denomintator = Beam_Energy*sqrt(Calc_Terms_1*Calc_Terms_1 - 2*Calc_Terms_1*Proton_M*Proton_M);
    auto numerator = (Beam_Energy + Proton_M)*(Calc_Terms_1 - 2*Proton_M*Proton_M);

    auto Pro_Th_Calc_P = acos((numerator/denomintator))*(180/3.1415926);
    auto Pro_Th_Calc_M = acos(-(numerator/denomintator))*(180/3.1415926);
    
    if(abs(Pro_Th_Calc - Pro_Th_Calc_P) <= abs(Pro_Th_Calc - Pro_Th_Calc_M)){
        Pro_Th_Calc = Pro_Th_Calc_P;
    }
    else{
        Pro_Th_Calc = Pro_Th_Calc_M;
    }

    auto Delta_Theta = ((proC.Theta())*(180/3.1415926)) - Pro_Th_Calc;
    

    auto Final_Output = Delta_Theta;

                    """])
                except Exception as e:
                    print("\nFAILED ∆Theta CALCULATION (Version 4)\n")
                    print("".join(["ERROR: ", str(e)]))
            else:
                # print("Defaulting to Verion 1 of ∆Theta Calculation")
                try:
                    Calculation_Code_Choice = "".join([Calculation_Code_Choice, """
    double Proton_M  = """, str(Particle_Mass_Proton), """;
    
    // Below are the kinematic calculations of the proton angle (theta) (from elastic scattering) 
    // To be used for exclusivity cuts

    auto Pro_Th_Calc = (proC.Theta())*(180/3.1415926); // Initialize the calculated proton angle as the same value as the measured/corrected proton angle (converted to degrees)

    Pro_Th_Calc = atan(Proton_M/((Beam_Energy + Proton_M)*tan(eleC.Theta()/2)))*(180/3.1415926);

    auto Delta_Theta = ((proC.Theta())*(180/3.1415926)) - Pro_Th_Calc;

    auto Final_Output = Delta_Theta;

                    """])
                except Exception as e:
                    print("\nFAILED ∆Theta/∆Phi CALCULATION\n")
                    print("".join(["ERROR: ", str(e)]))




        ##=============================================================##
        ##===============||---------------------------||===============##
        ##===============||    Corrected Momentums    ||===============##
        ##===============||---------------------------||===============##
        ##=============================================================##
        if("Mom" in Out_Type):
            Calculation_Code_Choice = "".join(["""
    auto Final_Output = """, "ele" if("p" not in Out_Type) else str(Out_Type.replace("Mom_", "")), """C.P();
            """])

        Full_Correction_Output = "".join(["""
        """, Correction_Code, """
        
    auto Beam_Energy = """, str(Beam_Energy), """;
    // Defined by the run group/data set

    auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
    auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, """, str(Particle_Mass_Proton), """);""", Particles_for_Correction, """
        """, Calculation_Code_Choice, """
    return Final_Output;
        """])


        if("pim" not in Out_Type):
            Full_Correction_Output = Full_Correction_Output.replace("auto fpim =", "// auto fpim =")
            Full_Correction_Output = Full_Correction_Output.replace("auto pimC =", "// auto pimC =")


        Output_Title = str(Correction)
        if("MM" not in Out_Type):
            Output_Title = "".join([str(Out_Type.replace("Mom_", "")), "_", Output_Title])

        if("""cout<<"Sector = "<<prosec<<endl;""" in Calculation_Code_Choice):
            print(Calculation_Code_Choice)
            Output_test = Data_Frame.Define(str(Output_Title), str(Full_Correction_Output))
            Output_test.Count()
            
        try:
            Output = Data_Frame.Define(str(Output_Title), str(Full_Correction_Output))
            # print("".join([color.BOLD, "Correction Code: \n", color.END, str(Full_Correction_Output)]) if("D_Angle" in Out_Type) else "")
            if(Extra_Cut not in ["none", ""]):
                Output = Output.Filter(Extra_Cut)
        except Exception as e:
            print("".join([color.Error, """ERROR: Failed to create the DataFrame Column...\nCode is written as:
            """, color.END, "Output = Data_Frame.Define(", str(Output_Title), ", ", str(Full_Correction_Output).replace(str(Correction_Code_Full_In) if("In" in datatype) else str(Correction_Code_Full_Out), "Correction Code"), """)
            
            if(Extra_Cut not in ["none", ""]):
                Output = Output.Filter(""", str(Extra_Cut), ")"]))
            
            
            print("".join([color.BBLUE, "\nINPUTS: CorDpp('Data_Frame', '", str(Correction), "', '", str(Out_Type), "', '", str(Channel_Type), "', '", str(MM_Type), "', '", str(Data_Type), "', '", str(Extra_Cut), "')", color.END]))
            print("".join([color.Error, "ERROR GIVEN: \n", str(e), color.END, "\n\n"]))
            print("".join([color.Error, "TRACEBACK: \n", color.END_R, str(traceback.format_exc()), color.END, "\n\n"]))
            
            
        # # Below is for printing out the code for testing...
        # Output = "".join(["Data_Frame.Define(", str(Output_Title), ", ", str(Full_Correction_Output),")"])
        # print(Output)
        
        
        return Output

    # print("Done with Calculations.")
    ##################################################################################################################################################################
    ##==============================================================================================================================================================##
    ##==============##============##============##============##         Calculations for RDF (End)         ##============##============##============##============##
    ##==============================================================================================================================================================##
    ##################################################################################################################################################################





    
    
    
    
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    
    
    
    
    ##===================================================================================##
    ##==========##==========##     Printing RDF Information?     ##==========##==========##
    ##===================================================================================##

    if(CheckDataFrameQ == 'y'):
        print("Printing the full list of variables (and their object types) in the DataFrame...")
        # print("".join(["Number of events = ", str(rdf.Count().GetValue())]))
        for ii in range(0, len(rdf.GetColumnNames()), 1):
            print("".join([str((rdf.GetColumnNames())[ii]), " ( type -> ", rdf.GetColumnType(rdf.GetColumnNames()[ii]), " )"]))
        print("".join(["\tTotal length= ", str(len(rdf.GetColumnNames()))]))

    ##===================================================================================##
    ##=========##=========##    Printing RDF Information? (End)    ##=========##=========##
    ##===================================================================================##
    
    
    



    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    
    
    
    
    ###################################################################################################################################################
    ##===============================================================================================================================================##
    ##==============##============##============##         Helpful Functions for Making Histograms         ##============##============##============##
    ##===============================================================================================================================================##
    ###################################################################################################################################################
    
    #####################################################################################################
    ##=================================================================================================##
    ##=================================================================================================##
    ##=============================#########################################===========================##
    ##=============================##                                     ##===========================##
    ##=============================##         Dataframe Functions         ##===========================##
    ##=============================##                                     ##===========================##
    ##=============================#########################################===========================##
    ##=================================================================================================##
    ##=================================================================================================##
    #####################################################################################################
    
    
    ##==================================================================================================================##
    ##==========##==========##     Filter Function for Phi Binning and Other Kinematic Cuts     ##==========##==========##
    ##==================================================================================================================##

    # Other Kinematic Cuts can be made with the variable Extra_Cut. 
    # If Extra_Cut = "", then only the regular binning cuts will be made by this function.

    
    def regFilter(Bank, Binning, Sector, Region, Shift, Extra_Cut, Particle):
        if(Extra_Cut in ["", "none", "Both", "Both_2", "Both_3", "All"]):
            Bank1 = Bank
        else:
            Bank1 = Bank.Filter(str(Extra_Cut))

        # Shift On:
        Shift = "S"
        
        # # Shift Off:
        # Shift = "NS"
        
        # No Phi Bins
        if(Binning == '1'):
            PhiFilter = 'error'
            return Bank1

        binName = "".join(["local", str(Particle), "Phi", Shift])

        # Corrections for 3 phi bins
        if(Binning == '3'):
            PhiFilter = 'error'
            if(Region == 'reg1'):
                if(Particle == 'el'):
                    PhiFilter = "".join([binName, '>-5 && ',  binName, '<5'])
                else:
                    PhiFilter = "".join([binName, '>-10 && ', binName, '<10'])
            if(Region == 'reg2'):
                if(Particle == 'el'):
                    PhiFilter = "".join([binName, '<-5'])
                else:
                    PhiFilter = "".join([binName, '<-10'])
            if(Region == 'reg3'):
                if(Particle == 'el'):
                    PhiFilter = "".join([binName, '>5'])
                else:
                    PhiFilter = "".join([binName, '>10'])                    
            if((Particle != 'el') and (("status" in rdf.GetColumnNames()) or ("artsec" in rdf.GetColumnNames()))):
                if(Region == 'reg1'):
                    PhiFilter = "".join([PhiFilter, " || artsec == -1"])
                else:
                    PhiFilter = "".join([PhiFilter, " && artsec ==  1"])
            return Bank.Filter(PhiFilter)


         # Corrections for 5 phi bins
        if(Binning == '5'):
            PhiFilter = 'error'
            if(Region == 'reg1'):
                PhiFilter = "".join([binName, '>-5 && ', binName, '<5'])
            if(Region == 'reg2'):
                PhiFilter = "".join([binName, '<-5 && ', binName, '>-15'])
            if(Region == 'reg3'):
                PhiFilter = "".join([binName, '<-15'])
            if(Region == 'reg4'):
                PhiFilter = "".join([binName, '>5 && ',  binName, '<15'])
            if(Region == 'reg5'):
                PhiFilter = "".join([binName, '>15'])


            if(PhiFilter != 'error'):
                return Bank1.Filter(PhiFilter)
            else:
                return Bank1




    ##========================================================================================================================##
    ##==========##==========##     Filter Function for Phi Binning and Other Kinematic Cuts (End)     ##==========##==========##
    ##========================================================================================================================##






    ##==============================================================================================##
    ##==========##==========##     Function for Getting Phi Region List     ##==========##==========##
    ##==============================================================================================##

    def regList_Call(Bin, Particle, Version):
        # Meaning of inputs:
        # # Bin -> Number of Phi Bins
        # # Particle -> Denotes the difference in phi bins for version 2 of this function
        # # Version -> There are 2 versions of this function's output.
        # # # # The output will either be a single list of regions (version 1) OR it will be a list of lists for each region (version 2)
        # # # # Version 2 is used in some title name

        RegList_Out = ['regall']

        if(Version == 1):
            if(Bin == '1'):
                RegList_Out = ['regall']
            if(Bin == '3'):
                RegList_Out = ['reg1', 'reg2', 'reg3']
            if(Bin == '5'):
                RegList_Out = ['reg1', 'reg2', 'reg3', 'reg4', 'reg5']

        if(Version == 2):
            RegList_Out = [['No Phi Bins', 'regall']]

            if(Bin == '1'):
                RegList_Out = [['No Phi Bins', 'regall']]
            if(Bin == '3'):
                if(Particle == 'el'):
                    RegList_Out = [[' (-5 < localelPhiS < 5)', 'reg1'], [' (localelPhiS < -5)', 'reg2'], [' (localelPhiS > 5)', 'reg3']]
                else:
                    RegList_Out = [[''.join([' (-10 < local', str(Particle), 'PhiS < 10)']), 'reg1'], [''.join([' (local',       str(Particle), 'PhiS < -10)']), 'reg2'], [''.join([' (local', str(Particle), 'PhiS > 10)']),  'reg3']]
            if(Bin == '5'):
                RegList_Out     = [[''.join([' (-5 < local',  str(Particle), 'PhiS < 5)']),  'reg1'], [''.join([' (-15 < local', str(Particle), 'PhiS < -5)']),  'reg2'], [''.join([' (local', str(Particle), 'PhiS < -15)']), 'reg3'], [''.join([' (5 < local', str(Particle), 'PhiS < 15)']), 'reg4'], [''.join([' (local', str(Particle), 'PhiS > 15)']), 'reg5']]


        return RegList_Out


    ##====================================================================================================##
    ##==========##==========##     Function for Getting Phi Region List (End)     ##==========##==========##
    ##====================================================================================================##





    ############################################################################################################################
    ##------------------------------------------------------------------------------------------------------------------------##
    ##==========##==========##==========##     Main Functions for Creating Histograms     ##==========##==========##==========##
    ##------------------------------------------------------------------------------------------------------------------------##
    ############################################################################################################################




    ##==============================================================================================##
    ##==========##     For 2D Invariant Mass vs Momentum Histograms - HWC_Histo_All     ##==========##
    ##==============================================================================================##

    def histoMaker_HWC_Histo_All(Bank, Correction, Sector, Region, Binning, Particle_Plot, Particle, Extra_Cut):
        # Difference between Particle and Particle_Plot ==> Particle defines which particle is referenced for sectors and phi bins while Particle_Plot refers to which particle momentum will be plotted against
        regionName = ''

        Particle_Formatting = str(((((str(Particle).replace("el", "El")).replace("pro", "Pro")).replace("pip", "#pi^{+}")).replace("pim", "#pi^{-}")).replace("pi0", "#pi^{0}"))
        Particle_Plot_Formatting = str(((((str(Particle_Plot).replace("el", "El")).replace("pro", "Pro")).replace("pip", "#pi^{+}")).replace("pim", "#pi^{-}")).replace("pi0", "#pi^{0}"))
        # # No Phi Bin Region
        # if(Binning == '1'):
        #     regionName = ''

        # 3 Phi Bin Region
        if(Binning == '3'):
            if(Particle == 'el'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -5 < #phi_{'  if(Region == 'reg1') else ' Bin: #phi_{', str(Particle_Formatting), '} < 5'  if(Region == 'reg1') else '} < -5'  if(Region == 'reg2') else '} > 5'])
            else:
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -10 < #phi_{' if(Region == 'reg1') else ' Bin: #phi_{', str(Particle_Formatting), '} < 10' if(Region == 'reg1') else '} < -10' if(Region == 'reg2') else '} > 10'])

        # 5 Phi Bin Region
        if(Binning == '5'):
            if(Region == 'reg1'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -5 < #phi_{',  str(Particle_Formatting), '} < 5'])
            if(Region == 'reg2'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -15 < #phi_{', str(Particle_Formatting), '} < -5'])
            if(Region == 'reg3'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: #phi_{',       str(Particle_Formatting), '} < -15'])
            if(Region == 'reg4'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: 5 < #phi_{',   str(Particle_Formatting), '} < 15'])
            if(Region == 'reg5'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: #phi_{',       str(Particle_Formatting), '} > 15'])



        SecName = 'All Sectors' if(Sector == 0) else ''.join([str(Particle_Formatting), ' Sector ', str(Sector)])

        CorrrectionName = corNameTitles(Correction, Form="splitline", EVENT_TYPE=event_type, BENDING_TYPE=datatype)

        name = (Correction, Sector, Binning, Region, Particle_Plot, Particle, Extra_Cut)
               

        start_title     = "".join(["#splitline{", str(datatype), " Invariant Mass}"])
        if(pass_version not in ["NA", ""]):
            start_title = "".join(["#splitline{", str(start_title), "{", str(pass_version), "}}"])
        
        output_title     = "".join([str(start_title),            "{", str(CorrrectionName), " -- ", SecName,                                           "}; p_{",                    Particle_Plot_Formatting, "} (GeV); W (GeV)"])
        if(regionName   != "" and Extra_Cut != ""):
            output_title = "".join([str(start_title), "{#splitline{", str(CorrrectionName), " -- ", SecName,                                          "}{", regionName, "}}; p_{",  Particle_Plot_Formatting, "} (GeV); W (GeV)"])
        if(Extra_Cut    != "" and regionName == ""):
            output_title = "".join([str(start_title), "{#splitline{", str(CorrrectionName), " -- ", SecName,            "}{Cut Applied: ", Extra_Cut, "}}; p_{",                    Particle_Plot_Formatting, "} (GeV); W (GeV)"])
        if(Extra_Cut    != "" and regionName != ""):
            output_title = "".join([str(start_title), "{#splitline{", str(CorrrectionName), " -- ", SecName, "}{#splitline{Cut Applied: ", Extra_Cut, "}{", regionName, "}}}; p_{", Particle_Plot_Formatting, "} (GeV); W (GeV)"])
            
        WC_out = "".join(["WM_", Correction])

        output = Bank.Histo2D(("".join(["HWC_Histo_All_", str(name)]), str(output_title), 200, 2 if('el' in Particle_Plot) else 0, 12 if('el' in Particle_Plot) else 10, 200, 0, 5), Particle_Plot, WC_out)

        return output

    

    ##====================================================================================================##
    ##==========##     For 2D Invariant Mass vs Momentum Histograms - HWC_Histo_All (End)     ##==========##
    ##====================================================================================================##



    ##==========================================================================================##
    ##==========##     For 2D Missing Mass vs Momentum Histograms - hmmCPARTall     ##==========##
    ##==========================================================================================##

    def Missing_Mass_Histo_Maker(Bank, Correction, Sector, Region, Shift, Binning, Particle_Plot, Particle, Extra_Cut, Theta_Plot=False):

        # Difference between Particle and Particle_Plot ==> Particle defines which particle is referenced for sectors and phi bins while Particle_Plot refers to which particle momentum will be plotted against

        Particle_Formatting      = str(((((str(Particle).replace("el",      "El")).replace("pro", "Pro")).replace("pip", "#pi^{+}")).replace("pim", "#pi^{-}")).replace("pi0", "#pi^{0}"))
        Particle_Plot_Formatting = str(((((str(Particle_Plot).replace("el", "El")).replace("pro", "Pro")).replace("pip", "#pi^{+}")).replace("pim", "#pi^{-}")).replace("pi0", "#pi^{0}"))
        
        regionName = ''

        # # No Phi Bin Region
        # if(Binning == '1'):
        #     regionName = ''

        # 3 Phi Bin Region
        if(Binning == '3'):
            if(Particle == 'el'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -5 < #phi_{'  if(Region == 'reg1') else ' Bin: #phi_{', str(Particle_Formatting), '} < 5'  if(Region == 'reg1') else '} < -5'  if(Region == 'reg2') else '} > 5'])
            else:
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -10 < #phi_{' if(Region == 'reg1') else ' Bin: #phi_{', str(Particle_Formatting), '} < 10' if(Region == 'reg1') else '} < -10' if(Region == 'reg2') else '} > 10'])

        # 5 Phi Bin Region
        if(Binning == '5'):

            if(Region == 'reg1'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -5 < #phi_{',  str(Particle_Formatting), '} < 5'])
            if(Region == 'reg2'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -15 < #phi_{', str(Particle_Formatting), '} < -5'])
            if(Region == 'reg3'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: #phi_{',       str(Particle_Formatting), '} < -15'])
            if(Region == 'reg4'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: 5 < #phi_{',   str(Particle_Formatting), '} < 15'])
            if(Region == 'reg5'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: #phi_{',       str(Particle_Formatting), '} > 15'])

            
        SecName = 'All Sectors' if(Sector == 0) else ''.join([str(Particle_Formatting) , ' Sector ', str(Sector)])

        CorrrectionName = corNameTitles(Correction, Form="splitline", EVENT_TYPE=event_type, BENDING_TYPE=datatype)

        name = (Correction, Sector, '', Binning, Region, Particle_Plot, Particle, Extra_Cut)

                
        start_title     = "".join(["#splitline{(", str(datatype), ") MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "} ", str(SecName), "}"])
        if(pass_version not in ["NA", ""]):
            start_title = "".join(["#splitline{",  str(start_title), "{", str(pass_version), "}}"])
                
        output_title     = "".join([str(start_title),                           "{Correction:", str(CorrrectionName),                                                             "".join(["};p_{", str(Particle_Plot_Formatting), "} (GeV);"]) if(not Theta_Plot) else "".join(["};#theta_{", str(Particle_Plot_Formatting), "} (#circ);"]), "MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}", " (GeV^{2})" if(MM_type != "epipX") else " (GeV)"])
        if(regionName   != "" and Extra_Cut != ""):
            output_title = "".join(["#splitline{",            str(start_title), "{Correction:", str(CorrrectionName), "}}{",                                     str(regionName), "".join(["};p_{", str(Particle_Plot_Formatting), "} (GeV);"]) if(not Theta_Plot) else "".join(["};#theta_{", str(Particle_Plot_Formatting), "} (#circ);"]), "MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}", " (GeV^{2})" if(MM_type != "epipX") else " (GeV)"])
        if(Extra_Cut    != "" and regionName == ""):
            output_title = "".join(["#splitline{",            str(start_title), "{Correction:", str(CorrrectionName), "}}{Cut Applied: ", str(Extra_Cut),                         "".join(["};p_{", str(Particle_Plot_Formatting), "} (GeV);"]) if(not Theta_Plot) else "".join(["};#theta_{", str(Particle_Plot_Formatting), "} (#circ);"]), "MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}", " (GeV^{2})" if(MM_type != "epipX") else " (GeV)"])
        if(Extra_Cut    != "" and regionName != ""):
            output_title = "".join(["#splitline{#splitline{", str(start_title), "{Correction:", str(CorrrectionName), "}}{Cut Applied: ", str(Extra_Cut), "}}{", str(regionName), "".join(["};p_{", str(Particle_Plot_Formatting), "} (GeV);"]) if(not Theta_Plot) else "".join(["};#theta_{", str(Particle_Plot_Formatting), "} (#circ);"]), "MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}", " (GeV^{2})" if(MM_type != "epipX") else " (GeV)"])
        # if(regionName   != "" and Extra_Cut != ""):
        #     output_title = "".join(["#splitline{",            str(start_title), "{Correction:", str(CorrrectionName), "}}{",                                     str(regionName), "};p_{", str(Particle_Plot_Formatting), "} (GeV);", "".join(["#theta_{", str(Particle_Plot_Formatting), "} (#circ);"]) if(Theta_Plot) else "", "MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}", " (GeV^{2})" if(MM_type != "epipX") else " (GeV)"])
        # if(Extra_Cut    != "" and regionName == ""):
        #     output_title = "".join(["#splitline{",            str(start_title), "{Correction:", str(CorrrectionName), "}}{Cut Applied: ", str(Extra_Cut),                         "};p_{", str(Particle_Plot_Formatting), "} (GeV);", "".join(["#theta_{", str(Particle_Plot_Formatting), "} (#circ);"]) if(Theta_Plot) else "", "MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}", " (GeV^{2})" if(MM_type != "epipX") else " (GeV)"])
        # if(Extra_Cut    != "" and regionName != ""):
        #     output_title = "".join(["#splitline{#splitline{", str(start_title), "{Correction:", str(CorrrectionName), "}}{Cut Applied: ", str(Extra_Cut), "}}{", str(regionName), "};p_{", str(Particle_Plot_Formatting), "} (GeV);", "".join(["#theta_{", str(Particle_Plot_Formatting), "} (#circ);"]) if(Theta_Plot) else "", "MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}", " (GeV^{2})" if(MM_type != "epipX") else " (GeV)"])

        if(Theta_Plot):
            # output = Bank.Histo3D(("".join(["hmmCPARTall_Vs_Theta_", str(name)]), str(output_title), 240, 0, 12, 350, 0, 140, Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max), Particle_Plot, f"{Particle_Plot}th", Correction)
            output = Bank.Histo2D(("".join(["hmmCPARTall_Vs_Theta_", str(name)]), str(output_title), 350, 0, 140, Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max), f"{Particle_Plot}th", Correction)
        else:
            # output = Bank.Histo2D(("".join(["hmmCPARTall_",          str(name)]), str(output_title), 200, 2 if 'el' in Particle_Plot else 0, 12 if 'el' in Particle_Plot else 10, Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max), Particle_Plot, Correction)
            output = Bank.Histo2D(("".join(["hmmCPARTall_",          str(name)]), str(output_title), 240, 0, 12,  Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max), Particle_Plot,        Correction)

        return output

    

    ##================================================================================================##
    ##==========##     For 2D Missing Mass vs Momentum Histograms - hmmCPARTall (End)     ##==========##
    ##================================================================================================##




    ##################################################################################################################################
    ##------------------------------------------------------------------------------------------------------------------------------##
    ##==========##==========##==========##     Main Functions for Creating Histograms (End)     ##==========##==========##==========##
    ##------------------------------------------------------------------------------------------------------------------------------##
    ##################################################################################################################################

    
    
    
    

    ############################################################################################################################################
    ##=================================================######################################=================================================##
    ##=================================================##                                  ##=================================================##
    ##===============##===============##===============##         Exclusivity Cuts         ##===============##===============##===============##
    ##=================================================##                                  ##=================================================##
    ##=================================================######################################=================================================##
    # The following lines are used to set the additional exclusivity cuts used by this code to better select events related to the momentum corrections (based on channel selection)

    Calculated_Exclusive_Cuts = "esec != -2" # This statement is always true (avoids failure of calculated cuts if MM_type not defined properly)
    Calculated_Exclusive_Cuts_v2, Calculated_Exclusive_Cuts_v3, Calculated_Exclusive_Cuts_v4, Calculated_Exclusive_Cuts_v5, Calculated_Exclusive_Cuts_v6 = "esec != -2", "esec != -2", "esec != -2", "esec != -2", "esec != -2"
    Calculated_Dp_Cut, Calculated_Dp_Cut_V2 = "esec != -2", "esec != -2"


    ###########################################################################################################################
    ##=======================================================================================================================##
    ##===============##=============##         Exclusivity Cuts (Using MM from eπ+(N))         ##=============##=============##
    ##=======================================================================================================================##
    ###########################################################################################################################
    if(MM_type == "epipX"):
        
        if("In" in datatype):

            Calculated_Exclusive_Cuts = "".join(["""
                auto beam = ROOT::Math::PxPyPzMVector(0, 0, """,    str(Beam_Energy),          """, 0);
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, """, str(Particle_Mass_Proton), """);//0.938);
                auto ele  = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, """, str(Particle_Mass_PiC), """);//0.13957);
                auto MM_Vector = beam + targ - ele - pip0;
                
                auto cut_up = 1.1;
                auto cut_down = 0;
                
                if(esec == 1){
                    if(localelPhiS > -5 && localelPhiS < 5){
                        // Upper Cut
                        cut_up = (-0.002512)*el + (1.025113);
                        // Lower Cut
                        cut_down = (-0.006564)*el + (0.91629);
                    }
                    if(localelPhiS < -5){
                        // Upper Cut
                        cut_up = (-0.002166)*el + (1.047257);
                        // Lower Cut
                        cut_down = (-0.00436)*el + (0.919216);
                    }
                    if(localelPhiS > 5){
                        // Upper Cut
                        cut_up = (-0.006649)*el + (1.036503);
                        // Lower Cut
                        cut_down = (-0.008246)*el + (0.899835);
                    }
                }
                if(esec == 2){
                    if(localelPhiS > -5 && localelPhiS < 5){
                        // Upper Cut
                        cut_up = (-0.001108)*el + (1.012364);
                        // Lower Cut
                        cut_down = (-0.004842)*el + (0.894447);
                    }
                    if(localelPhiS < -5){
                        // Upper Cut
                        cut_up = (-0.000811)*el + (1.015682);
                        // Lower Cut
                        cut_down = (-0.004621)*el + (0.898917);
                    }

                    if(localelPhiS > 5){
                        // Upper Cut
                        cut_up = (-0.006132)*el + (1.03695);
                        // Lower Cut
                        cut_down = (-0.009834)*el + (0.915225);
                    }
                }
                if(esec == 3){
                    if(localelPhiS > -5 && localelPhiS < 5){
                        // Upper Cut
                        cut_up = (-0.00808)*el + (1.053207);
                        // Lower Cut
                        cut_down = (-0.014113)*el + (0.937174);
                    }
                    if(localelPhiS < -5){
                        // Upper Cut
                        cut_up = (-0.011922)*el + (1.066027);
                        // Lower Cut
                        cut_down = (-0.014898)*el + (0.925886);
                    }
                    if(localelPhiS > 5){
                        // Upper Cut
                        cut_up = (-0.008165)*el + (1.06216);
                        // Lower Cut
                        cut_down = (-0.009607)*el + (0.913684);
                    }
                }
                if(esec == 4){
                    if(localelPhiS > -5 && localelPhiS < 5){
                        // Upper Cut
                        cut_up = (-0.003636)*el + (1.040308);
                        // Lower Cut
                        cut_down = (-0.006253)*el + (0.919061);
                    }
                    if(localelPhiS < -5){
                        // Upper Cut
                        cut_up = (-0.004512)*el + (1.036327);
                        // Lower Cut
                        cut_down = (-0.003965)*el + (0.88969);
                    }
                    if(localelPhiS > 5){
                        // Upper Cut
                        cut_up = (-0.002362)*el + (1.045388);
                        // Lower Cut
                        cut_down = (5.5e-05)*el + (0.884049);
                    }
                }
                if(esec == 5){
                    if(localelPhiS > -5 && localelPhiS < 5){
                        // Upper Cut
                        cut_up = (-0.00373)*el + (1.027939);
                        // Lower Cut
                        cut_down = (-0.007682)*el + (0.920652);
                    }
                    if(localelPhiS < -5){
                        // Upper Cut
                        cut_up = (-0.000977)*el + (1.011744);
                        // Lower Cut
                        cut_down = (-0.003504)*el + (0.89456);
                    }
                    if(localelPhiS > 5){
                        // Upper Cut
                        cut_up = (-0.007179)*el + (1.056021);
                        // Lower Cut
                        cut_down = (-0.005851)*el + (0.908325);
                    }
                }
                if(esec == 6){
                    if(localelPhiS > -5 && localelPhiS < 5){
                        // Upper Cut
                        cut_up = (-0.004726)*el + (1.037422);
                        // Lower Cut
                        cut_down = (-0.007929)*el + (0.919135);
                    }
                    if(localelPhiS < -5){
                        // Upper Cut
                        cut_up = (-0.005149)*el + (1.047543);
                        // Lower Cut
                        cut_down = (-0.007816)*el + (0.926179);
                    }
                    if(localelPhiS > 5){
                        // Upper Cut
                        cut_up = (-0.004952)*el + (1.031514);
                        // Lower Cut
                        cut_down = (-0.009952)*el + (0.922387);
                    }
                }
                
                return (MM_Vector.M() < cut_up && MM_Vector.M() > cut_down);

            """])
            
            if("Pass 1" in pass_version and ("Fall" not in pass_version)):
                print(color.BBLUE, "\nUSING NEW EXCLUSIVITY CUTS FOR SPRING 2019 DATA (Pass 1)\n\n", color.END)
                Calculated_Exclusive_Cuts = "".join(["""
                    auto beam = ROOT::Math::PxPyPzMVector(0, 0, """,    str(Beam_Energy),          """, 0);
                    auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, """, str(Particle_Mass_Proton), """);
                    auto ele  = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                    auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, """, str(Particle_Mass_PiC), """);

                    auto MM_Vector = beam + targ - ele - pip0;

                    auto cut_upper = 1.1;
                    auto cut_lower = 0;

                    if(esec == 1){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0029394)*el + (1.0704569);
                            // Lower Cut
                            cut_lower = (-0.0080116)*el + (0.8771632);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0015837)*el + (1.0848313);
                            // Lower Cut
                            cut_lower = (-0.005)*el + (0.8758892);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.005183)*el + (1.0768906);
                            // Lower Cut
                            cut_lower = (-0.0106145)*el + (0.8589478);
                        }
                    }
                    if(esec == 2){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0002427)*el + (1.0492291);
                            // Lower Cut
                            cut_lower = (-0.0067184)*el + (0.853968);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.000816)*el + (1.0606348);
                            // Lower Cut
                            cut_lower = (-0.0048734)*el + (0.8483969);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0127831)*el + (1.125157);
                            // Lower Cut
                            cut_lower = (-0.009067)*el + (0.8550742);
                        }
                    }
                    if(esec == 3){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0131371)*el + (1.1300458);
                            // Lower Cut
                            cut_lower = (-0.0171171)*el + (0.897616);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0137094)*el + (1.1206948);
                            // Lower Cut
                            cut_lower = (-0.0194186)*el + (0.8945861);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0099831)*el + (1.1196493);
                            // Lower Cut
                            cut_lower = (-0.0106769)*el + (0.8644091);
                        }
                    }
                    if(esec == 4){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0036287)*el + (1.0805398);
                            // Lower Cut
                            cut_lower = (-0.0081657)*el + (0.8780205);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0036156)*el + (1.0741683);
                            // Lower Cut
                            cut_lower = (-0.0073527)*el + (0.8570785);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0036566)*el + (1.0950377);
                            // Lower Cut
                            cut_lower = (-0.0009844)*el + (0.840634);
                        }
                    }
                    if(esec == 5){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0041069)*el + (1.0766104);
                            // Lower Cut
                            cut_lower = (-0.006203)*el + (0.8679564);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0051101)*el + (1.0885182);
                            // Lower Cut
                            cut_lower = (-0.0011979)*el + (0.8345538);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0083046)*el + (1.1063391);
                            // Lower Cut
                            cut_lower = (-0.0045147)*el + (0.8587532);
                        }
                    }
                    if(esec == 6){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0087088)*el + (1.1095549);
                            // Lower Cut
                            cut_lower = (-0.0097436)*el + (0.8790762);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0048216)*el + (1.0863592);
                            // Lower Cut
                            cut_lower = (-0.0082379)*el + (0.8808634);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0065463)*el + (1.0862486);
                            // Lower Cut
                            cut_lower = (-0.0120596)*el + (0.8845782);
                        }
                    }  

                    return (MM_Vector.M() < cut_upper && MM_Vector.M() > cut_lower);

                """])
                
            if("Pass 2" in pass_version and ("Fall" not in pass_version)):
                print(color.BBLUE, "\nUSING NEW EXCLUSIVITY CUTS FOR SPRING 2019 DATA (Pass 2)\n\n", color.END)
                Calculated_Exclusive_Cuts = "".join(["""
                    auto beam = ROOT::Math::PxPyPzMVector(0, 0, """,    str(Beam_Energy),          """, 0);
                    auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, """, str(Particle_Mass_Proton), """);
                    auto ele  = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                    auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, """, str(Particle_Mass_PiC), """);

                    auto MM_Vector = beam + targ - ele - pip0;

                    auto cut_upper = 1.1;
                    auto cut_lower = 0;

                    if(esec == 1){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0019918)*el + (1.027293);
                            // Lower Cut
                            cut_lower = (-0.0027615)*el + (0.8940996);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (0.0019951)*el + (1.0062549);
                            // Lower Cut
                            cut_lower = (0.0008288)*el + (0.8713239);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0044249)*el + (1.0413328);
                            // Lower Cut
                            cut_lower = (-0.0044675)*el + (0.9004638);
                        }
                    }
                    if(esec == 2){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0036938)*el + (1.0308979);
                            // Lower Cut
                            cut_lower = (-0.0058183)*el + (0.8975511);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0029853)*el + (1.0269994);
                            // Lower Cut
                            cut_lower = (-0.0039011)*el + (0.8879641);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0069775)*el + (1.0507301);
                            // Lower Cut
                            cut_lower = (-0.0089656)*el + (0.911158);
                        }
                    }
                    if(esec == 3){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0050063)*el + (1.0377177);
                            // Lower Cut
                            cut_lower = (-0.0061733)*el + (0.8949918);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.00556)*el + (1.0394214);
                            // Lower Cut
                            cut_lower = (-0.0083744)*el + (0.9041797);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0034001)*el + (1.0307054);
                            // Lower Cut
                            cut_lower = (-0.0060003)*el + (0.894058);
                        }
                    }
                    if(esec == 4){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0017142)*el + (1.0288892);
                            // Lower Cut
                            cut_lower = (-0.0049154)*el + (0.902343);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0020321)*el + (1.0292366);
                            // Lower Cut
                            cut_lower = (-0.0066844)*el + (0.9077503);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (0.0025982)*el + (1.00456);
                            // Lower Cut
                            cut_lower = (0.0017599)*el + (0.855191);
                        }
                    }
                    if(esec == 5){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0027996)*el + (1.031067);
                            // Lower Cut
                            cut_lower = (-0.005691)*el + (0.9001498);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0007523)*el + (1.0230344);
                            // Lower Cut
                            cut_lower = (-0.0019585)*el + (0.8760821);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0051705)*el + (1.0432471);
                            // Lower Cut
                            cut_lower = (0.0010753)*el + (0.8466486);
                        }
                    }
                    if(esec == 6){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0030816)*el + (1.0257025);
                            // Lower Cut
                            cut_lower = (-0.0004971)*el + (0.8605466);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0033853)*el + (1.0271852);
                            // Lower Cut
                            cut_lower = (-0.0007073)*el + (0.8621061);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0039714)*el + (1.031813);
                            // Lower Cut
                            cut_lower = (-0.0028837)*el + (0.8792061);
                        }
                    }  

                    return (MM_Vector.M() < cut_upper && MM_Vector.M() > cut_lower);

                """])
                
            if("Pass 2" in pass_version and ("Fall" in pass_version)):
                print(color.BBLUE, "\nUSING NEW EXCLUSIVITY CUTS FOR FALL 2018 DATA (Pass 2)\n\n", color.END)
                Calculated_Exclusive_Cuts = "".join(["""
                    auto beam = ROOT::Math::PxPyPzMVector(0, 0, """,    str(Beam_Energy),          """, 0);
                    auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, """, str(Particle_Mass_Proton), """);
                    auto ele  = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                    auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, """, str(Particle_Mass_PiC), """);
                    auto MM_Vector = beam + targ - ele - pip0;
                    auto cut_upper = 1.1;
                    auto cut_lower = 0;
                    if(esec == 1){
                        if(localelPhiS > -5 && localelPhiS < 5){
                        // Upper Cut
                            cut_upper = (-0.0039554)*el + (1.0473555);
                            // Lower Cut
                            cut_lower = (-0.003947)*el + (0.9051718);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0010412)*el + (1.0352067);
                            // Lower Cut
                            cut_lower = (-0.0004544)*el + (0.884299);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0056314)*el + (1.055177);
                            // Lower Cut
                            cut_lower = (-0.0057279)*el + (0.9111849);
                        }
                    }
                    if(esec == 2){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0024812)*el + (1.0262642);
                            // Lower Cut
                            cut_lower = (-0.005965)*el + (0.8983191);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-2.77e-05)*el + (1.0140921);
                            // Lower Cut
                            cut_lower = (-0.0049283)*el + (0.8947587);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0080913)*el + (1.0594146);
                            // Lower Cut
                            cut_lower = (-0.0091806)*el + (0.9140446);
                        }
                    }
                    if(esec == 3){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0037445)*el + (1.0419128);
                            // Lower Cut
                            cut_lower = (-0.0066199)*el + (0.9083502);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0078946)*el + (1.0684359);
                            // Lower Cut
                            cut_lower = (-0.0076471)*el + (0.9135273);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0035279)*el + (1.0400137);
                            // Lower Cut
                            cut_lower = (-0.0060842)*el + (0.8998823);
                        }
                    }
                    if(esec == 4){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0019849)*el + (1.0421565);
                            // Lower Cut
                            cut_lower = (-0.0042306)*el + (0.9074003);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0018365)*el + (1.0449645);
                            // Lower Cut
                            cut_lower = (-0.0060099)*el + (0.9170312);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (0.000491)*el + (1.0262379);
                            // Lower Cut
                            cut_lower = (-0.000102)*el + (0.871096);
                        }
                    }
                    if(esec == 5){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.003869)*el + (1.0382558);
                            // Lower Cut
                            cut_lower = (-0.005851)*el + (0.9003115);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0024885)*el + (1.0340774);
                            // Lower Cut
                            cut_lower = (-0.0049768)*el + (0.8961298);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0063166)*el + (1.0490924);
                            // Lower Cut
                            cut_lower = (-0.0048805)*el + (0.8860154);
                        }
                    }
                    if(esec == 6){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0027279)*el + (1.0304784);
                            // Lower Cut
                            cut_lower = (-0.0042008)*el + (0.8943379);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.004937)*el + (1.0467457);
                            // Lower Cut
                            cut_lower = (-0.0040631)*el + (0.8924408);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0038176)*el + (1.0382673);
                            // Lower Cut
                            cut_lower = (-0.0045803)*el + (0.893171);
                        }
                    }
                    return (MM_Vector.M() < cut_upper && MM_Vector.M() > cut_lower);
                """])
            
        if("Out" in datatype):
            Calculated_Exclusive_Cuts = "".join(["""
                auto beam = ROOT::Math::PxPyPzMVector(0, 0, """, str(Beam_Energy), """, 0);
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, """, str(Particle_Mass_Proton), """);//0.938);
                auto ele  = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, """, str(Particle_Mass_PiC), """);//0.13957);
                auto MM_Vector = beam + targ - ele - pip0;

                auto cut_up = 1.1;
                auto cut_down = 0;
                if(esec == 1){
                    if(localelPhiS > -5 && localelPhiS < 5){
                        // Upper Cut
                        cut_up = (0.004043)*el + (0.989063);
                        // Lower Cut
                        cut_down = (-0.00269)*el + (0.899788);
                    }
                    if(localelPhiS < -5){
                        // Upper Cut
                        cut_up = (-9.4e-05)*el + (1.002402);
                        // Lower Cut
                        cut_down = (-0.005622)*el + (0.90179);
                    }
                    if(localelPhiS > 5){
                        // Upper Cut
                        cut_up = (0.008379)*el + (0.977598);
                        // Lower Cut
                        cut_down = (0.001488)*el + (0.891307);
                    }
                }
                if(esec == 2){
                    if(localelPhiS > -5 && localelPhiS < 5){
                        // Upper Cut
                        cut_up = (0.009323)*el + (0.953257);
                        // Lower Cut
                        cut_down = (-0.005005)*el + (0.907664);
                    }
                    if(localelPhiS < -5){
                        // Upper Cut
                        cut_up = (0.003401)*el + (0.980432);
                        // Lower Cut
                        cut_down = (-0.00735)*el + (0.910316);
                    }
                    if(localelPhiS > 5){
                        // Upper Cut
                        cut_up = (0.008858)*el + (0.969857);
                        // Lower Cut
                        cut_down = (-0.001044)*el + (0.895018);
                    }
                }
                if(esec == 3){
                    if(localelPhiS > -5 && localelPhiS < 5){
                        // Upper Cut
                        cut_up = (0.008251)*el + (0.971468);
                        // Lower Cut
                        cut_down = (-0.001976)*el + (0.896576);
                    }
                    if(localelPhiS < -5){
                        // Upper Cut
                        cut_up = (0.007759)*el + (0.981525);
                        // Lower Cut
                        cut_down = (-0.000646)*el + (0.893134);
                    }
                    if(localelPhiS > 5){
                        // Upper Cut
                        cut_up = (0.00521)*el + (0.98786);
                        // Lower Cut
                        cut_down = (-0.002292)*el + (0.897225);
                    }
                }
                if(esec == 4){
                    if(localelPhiS > -5 && localelPhiS < 5){
                        // Upper Cut
                        cut_up = (0.001179)*el + (1.013307);
                        // Lower Cut
                        cut_down = (-0.000126)*el + (0.878469);
                    }
                    if(localelPhiS < -5){
                        // Upper Cut
                        cut_up = (0.002951)*el + (1.008359);
                        // Lower Cut
                        cut_down = (-0.000494)*el + (0.889265);
                    }
                    if(localelPhiS > 5){
                        // Upper Cut
                        cut_up = (0.002793)*el + (1.00141);
                        // Lower Cut
                        cut_down = (-0.001988)*el + (0.891014);
                    }
                }
                if(esec == 5){
                    if(localelPhiS > -5 && localelPhiS < 5){
                        // Upper Cut
                        cut_up = (-0.000609)*el + (1.010997);
                        // Lower Cut
                        cut_down = (-0.006381)*el + (0.89851);
                    }
                    if(localelPhiS < -5){
                        // Upper Cut
                        cut_up = (-0.001719)*el + (1.02031);
                        // Lower Cut
                        cut_down = (-0.008516)*el + (0.917681);
                    }
                    if(localelPhiS > 5){
                        // Upper Cut
                        cut_up = (0.000408)*el + (1.013324);
                        // Lower Cut
                        cut_down = (-0.004329)*el + (0.892125);
                    }
                }
                if(esec == 6){
                    if(localelPhiS > -5 && localelPhiS < 5){
                        // Upper Cut
                        cut_up = (0.011072)*el + (0.955956);
                        // Lower Cut
                        cut_down = (-0.000468)*el + (0.889358);
                    }
                    if(localelPhiS < -5){
                        // Upper Cut
                        cut_up = (0.006269)*el + (0.996087);
                        // Lower Cut
                        cut_down = (0.001052)*el + (0.878127);
                    }
                    if(localelPhiS > 5){
                        // Upper Cut
                        cut_up = (0.009539)*el + (0.973095);
                        // Lower Cut
                        cut_down = (0.004656)*el + (0.866696);
                    }
                }


                return (MM_Vector.M() < cut_up && MM_Vector.M() > cut_down);

            """])
            
            
            if("Pass 2" in pass_version and ("Fall" in pass_version)):
                print(color.BBLUE, "\nUSING NEW (OUTBENDING) EXCLUSIVITY CUTS FOR FALL 2018 DATA (Pass 2)\n\n", color.END)
                Calculated_Exclusive_Cuts = "".join(["""
                    auto beam = ROOT::Math::PxPyPzMVector(0, 0, """,    str(Beam_Energy),          """, 0);
                    auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, """, str(Particle_Mass_Proton), """);
                    auto ele  = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                    auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, """, str(Particle_Mass_PiC), """);

                    auto MM_Vector = beam + targ - ele - pip0;

                    auto cut_upper = 1.1;
                    auto cut_lower = 0;
                    
                    if(esec == 1){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (0.00085)*el + (1.0155684);
                            // Lower Cut
                            cut_lower = (0.005)*el + (0.8454096);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0019918)*el + (1.046896);
                            // Lower Cut
                            cut_lower = (-0.0034129)*el + (0.9109);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (0.0032537)*el + (1.0025544);
                            // Lower Cut
                            cut_lower = (0.005685)*el + (0.8401328);
                        }
                    }
                    if(esec == 2){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (0.0025)*el + (1.0055498);
                            // Lower Cut
                            cut_lower = (0.005)*el + (0.835088);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (0.0014575)*el + (1.0154591);
                            // Lower Cut
                            cut_lower = (0.005)*el + (0.8392825);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (0.0056568)*el + (0.9868502);
                            // Lower Cut
                            cut_lower = (0.0053837)*el + (0.8357672);
                        }
                    }
                    if(esec == 3){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (0.0036459)*el + (0.9991959);
                            // Lower Cut
                            cut_lower = (0.0061)*el + (0.8284471);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (0.0034006)*el + (1.0023044);
                            // Lower Cut
                            cut_lower = (-0.004)*el + (0.9008054);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (0.0035806)*el + (0.9979392);
                            // Lower Cut
                            cut_lower = (-0.0022576)*el + (0.8911326);
                        }
                    }
                    if(esec == 4){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (0.0030531)*el + (1.0085585);
                            // Lower Cut
                            cut_lower = (0.0044807)*el + (0.853999);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (0.003645)*el + (1.0080695);
                            // Lower Cut
                            cut_lower = (0.0051523)*el + (0.8527973);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (0.0025041)*el + (1.0165799);
                            // Lower Cut
                            cut_lower = (-0.0011222)*el + (0.8952631);
                        }
                    }
                    if(esec == 5){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (0.0034878)*el + (0.9961862);
                            // Lower Cut
                            cut_lower = (0.0060497)*el + (0.8301999);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (0.0007298)*el + (1.0183639);
                            // Lower Cut
                            cut_lower = (0.0061)*el + (0.8341237);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (0.0039543)*el + (0.9949684);
                            // Lower Cut
                            cut_lower = (0.0061)*el + (0.8317604);
                        }
                    }
                    if(esec == 6){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (0.0033861)*el + (1.0031917);
                            // Lower Cut
                            cut_lower = (-0.0018161)*el + (0.8921721);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (0.003861)*el + (1.0051496);
                            // Lower Cut
                            cut_lower = (0.0060277)*el + (0.8343964);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (0.0040587)*el + (1.0039831);
                            // Lower Cut
                            cut_lower = (0.0051184)*el + (0.8465);
                        }
                    }  

                    return (MM_Vector.M() < cut_upper && MM_Vector.M() > cut_lower);

                """])

    ################################################################################################################################
    ##============================================================================================================================##
    ##===============##=============##        End of Exclusivity Cuts (Using MM from eπ+(N))        ##=============##=============##
    ##============================================================================================================================##
    ################################################################################################################################


    ###########################################################################################################################
    ##=======================================================================================================================##
    ##===============##=============##       Exclusivity Cuts (Using MM^2 from epπ+(π-))       ##=============##=============##
    ##=======================================================================================================================##
    ###########################################################################################################################
    # # Based on the (even) tighter cuts made from file: double_pion_eppipX_In_With_Dp_Exclusive_Tighter_Cut_New_File_All.root (uses ShowBackground())
    # # Cuts had an upper boundry of sigma = 1.75 and a lower boundry of sigma = 2
    if(MM_type == "eppipX"):

        if("In" in datatype):
            Calculated_Exclusive_Cuts_v4 = "".join(["""
                auto beam = ROOT::Math::PxPyPzMVector(0, 0, """, str(Beam_Energy), """, 0);
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, """, str(Particle_Mass_Proton), """);//0.938);
                auto ele  = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, """, str(Particle_Mass_PiC), """);//0.13957);
                auto pro0 = ROOT::Math::PxPyPzMVector(prox, proy, proz, """, str(Particle_Mass_Proton), """);//0.938);
                auto MM_Vector = beam + targ - ele - pip0 - pro0;
                auto cut_up = 0.2;
                auto cut_down = -0.2;
                return (MM_Vector.M2() < cut_up && MM_Vector.M2() > cut_down);
            
            """])
            Calculated_Exclusive_Cuts_v5 = "".join([str(Correction_Code_Full_In), """
                auto beam = ROOT::Math::PxPyPzMVector(0, 0, """, str(Beam_Energy), """, 0);
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, """, str(Particle_Mass_Proton), """);//0.938);
                
                auto fe = dppC(ex, ey, ez, esec, 0, 3, 2, 0, 0) + 1;
                auto eleC = ROOT::Math::PxPyPzMVector(ex*fe, ey*fe, ez*fe, 0);
                
                auto fpip = dppC(pipx, pipy, pipz, pipsec, 1, 3, 2, 0, 0) + 1;
                auto pipC = ROOT::Math::PxPyPzMVector(pipx*fpip, pipy*fpip, pipz*fpip, """, str(Particle_Mass_PiC), """);//0.13957);
                
                // auto ele = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                // auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, """, str(Particle_Mass_PiC), """);//0.13957);
                
                auto pro0 = ROOT::Math::PxPyPzMVector(prox, proy, proz, """, str(Particle_Mass_Proton), """);//0.938);
                auto MM_Vector = beam + targ - eleC - pipC - pro0;
                auto cut_up = 0.2;
                auto cut_down = -0.2;
                return (MM_Vector.M2() < cut_up && MM_Vector.M2() > cut_down);
            """])
            Calculated_Exclusive_Cuts_v6 = "".join(["""
                auto beam = ROOT::Math::PxPyPzMVector(0, 0, """, str(Beam_Energy), """, 0);
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, """, str(Particle_Mass_Proton), """);//0.938);
                auto ele = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, """, str(Particle_Mass_PiC), """);//0.13957);
                auto pro0 = ROOT::Math::PxPyPzMVector(prox_cor, proy_cor, proz_cor, """, str(Particle_Mass_Proton), """);//0.938);
                auto MM_Vector = beam + targ - ele - pip0 - pro0;
                auto cut_up = 0.2;
                auto cut_down = -0.2;
                return (MM_Vector.M2() < cut_up && MM_Vector.M2() > cut_down);
            
            """])
            Calculated_Exclusive_Cuts = "".join(["""
                auto beam = ROOT::Math::PxPyPzMVector(0, 0, """, str(Beam_Energy), """, 0);
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, """, str(Particle_Mass_Proton), """);//0.938);
                auto ele = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, """, str(Particle_Mass_PiC), """);//0.13957);
                auto pro0 = ROOT::Math::PxPyPzMVector(prox, proy, proz, """, str(Particle_Mass_Proton), """);//0.938);
                auto MM_Vector = beam + targ - ele - pip0 - pro0;
                auto cut_up = 0.2;
                auto cut_down = -0.2;
                if(esec == 1){
                    // Upper Cut
                    cut_up = (-0.007753)*el + (0.156477);
                    // Lower Cut
                    cut_down = (0.000549)*el + (-0.07865);
                }
                if(esec == 2){
                    // Upper Cut
                    cut_up = (-0.005691)*el + (0.128535);
                    // Lower Cut
                    cut_down = (-0.000459)*el + (-0.07017);
                }
                if(esec == 3){
                    // Upper Cut
                    cut_up = (-0.008299)*el + (0.141537);
                    // Lower Cut
                    cut_down = (-0.000401)*el + (-0.093103);
                }

                if(esec == 4){
                    // Upper Cut
                    cut_up = (-0.003421)*el + (0.127147);
                    // Lower Cut
                    cut_down = (0.001045)*el + (-0.073916);
                }
                if(esec == 5){
                    // Upper Cut
                    cut_up = (-0.010646)*el + (0.166571);
                    // Lower Cut
                    cut_down = (0.004321)*el + (-0.085768);
                }
                if(esec == 6){
                    // Upper Cut
                    cut_up = (-0.007125)*el + (0.143694);
                    // Lower Cut
                    cut_down = (-0.000127)*el + (-0.066184);
                }
                return (MM_Vector.M2() < cut_up && MM_Vector.M2() > cut_down);
            """])
            
        if("Out" in datatype):
            Calculated_Exclusive_Cuts = "".join(["""
                auto beam = ROOT::Math::PxPyPzMVector(0, 0, """, str(Beam_Energy), """, 0);
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, """, str(Particle_Mass_Proton), """);//0.938);
                auto ele  = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, """, str(Particle_Mass_PiC), """);//0.13957);
                auto pro0 = ROOT::Math::PxPyPzMVector(prox, proy, proz, """, str(Particle_Mass_Proton), """);//0.938);
                auto MM_Vector = beam + targ - ele - pip0 - pro0;
                auto cut_up = 0.2;
                auto cut_down = -0.2;
                if(esec == 1){
                    // Upper Cut
                    cut_up = (-0.00174)*el + (0.114841);
                    // Lower Cut
                    cut_down = (0.002693)*el + (-0.052275);
                }
                if(esec == 2){
                    // Upper Cut
                    cut_up = (0.000284)*el + (0.097696);
                    // Lower Cut
                    cut_down = (0.001777)*el + (-0.048444);
                }
                if(esec == 3){
                    // Upper Cut
                    cut_up = (-0.002927)*el + (0.123553);
                    // Lower Cut
                    cut_down = (0.003879)*el + (-0.060533);
                }
                if(esec == 4){
                    // Upper Cut
                    cut_up = (-0.001737)*el + (0.111652);
                    // Lower Cut
                    cut_down = (0.002936)*el + (-0.054787);
                }
                if(esec == 5){
                    // Upper Cut
                    cut_up = (-0.002577)*el + (0.118104);
                    // Lower Cut
                    cut_down = (0.003074)*el + (-0.057185);
                }
                if(esec == 6){
                    // Upper Cut
                    cut_up = (0.005977)*el + (0.072379);
                    // Lower Cut
                    cut_down = (0.004878)*el + (-0.056216);
                }

                return (MM_Vector.M2() < cut_up && MM_Vector.M2() > cut_down);

            """])
    ##################################################################################################################################
    ##==============================================================================================================================##
    ##===============##=============##       End of Exclusivity Cuts (Using MM^2 from epπ+(π-))       ##=============##=============##
    ##==============================================================================================================================##
    ##################################################################################################################################


    ###########################################################################################################################
    ##=======================================================================================================================##
    ##===============##=============##        Exclusivity Cuts (Using MM^2 from ep(π0))        ##=============##=============##
    ##=======================================================================================================================##
    ###########################################################################################################################
    if(MM_type == "eppi0X" or event_type == "P0"):

        if("In" in datatype):
            Calculated_Dp_Cut = "".join(["""
    double Proton_M  = """, str(Particle_Mass_Proton), """;
    auto Beam_Energy = """, str(Beam_Energy), """;
    auto eleC = ROOT::Math::PxPyPzMVector(""", "ex, ey, ez" if("(GEN)" not in str(event_Name)) else "ex0, ey0, ez0", """, 0);
    auto proC = ROOT::Math::PxPyPzMVector(prox, proy, proz, Proton_M);
            
    // double pi0M2term = (0.13498*0.13498)/2;
    double pi0M2term = (""", str(Particle_Mass_Pi0), """*""", str(Particle_Mass_Pi0), """)/2;
    // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pi0) based on the assumption that the proton angle and electron reconstruction were measured by the detector correctly for exclusive events in the ep->epπ0 channel
    // (π0 is used as the "missing" particle)

    auto termA1 = pi0M2term - (Proton_M)*((Beam_Energy) - eleC.P() + (Proton_M)) + (Beam_Energy)*eleC.P()*(1 - cos(eleC.Theta()));
        // termA1 = pi0M2term - "Proton Mass"*("Initial Beam Energy" - "Electron Momentum" + "Proton Mass") + "Initial Beam Energy"*"Electron Momentum"*(1 - cos("Electron Theta Angle"))

    auto termB1 = (Beam_Energy)*cos(proC.Theta()) - eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC));
        // termB1 = "Initial Beam Energy"*cos("Proton Theta Angle") - "Electron Momentum"*cos("Angle between the Proton and Electron")

    auto termC1 = eleC.P() - (Beam_Energy) - (Proton_M);
        // termC1 = "Electron Momentum" - "Initial Beam Energy" - "Proton Mass"

    auto termA2 = (termB1*termB1 - termC1*termC1);
    auto termB2 = -2*termB1*termA1;
    auto termC2 = termA1*termA1 - termC1*termC1*(Proton_M)*(Proton_M);

    auto pro_CalculateP = (-termB2 + sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);
    auto pro_CalculateM = (-termB2 - sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);

    auto pro_Calculate = pro_CalculateP;

    if(abs(proC.P() - pro_CalculateP) <= abs(proC.P() - pro_CalculateM)){
        pro_Calculate = pro_CalculateP;
    }
    else{
        pro_Calculate = pro_CalculateM;
    }

    if(pro_CalculateP < 0){
        pro_Calculate = pro_CalculateM;
    }
    if(pro_CalculateM < 0){
        pro_Calculate = pro_CalculateP;
    }

    auto Delta_P_Cut = pro_Calculate - proC.P();
    return (Delta_P_Cut > 0.05 || Delta_P_Cut < -0.05);
    """])
            Calculated_Dp_Cut_V2 = "".join(["""
    double Proton_M  = """, str(Particle_Mass_Proton), """;
    auto Beam_Energy = """, str(Beam_Energy), """;
    auto eleC = ROOT::Math::PxPyPzMVector(""", "ex, ey, ez" if("(GEN)" not in str(event_Name)) else "ex0, ey0, ez0", """, 0);
    auto proC = ROOT::Math::PxPyPzMVector(prox, proy, proz, Proton_M);
            
    double pi0M2term = (""", str(Particle_Mass_Pi0), """*""", str(Particle_Mass_Pi0), """)/2;
    // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pi0) based on the assumption that the proton angle and electron reconstruction were measured by the detector correctly for exclusive events in the ep->epπ0 channel
    // (π0 is used as the "missing" particle)

    auto termA1 = pi0M2term - (Proton_M)*((Beam_Energy) - eleC.P() + (Proton_M)) + (Beam_Energy)*eleC.P()*(1 - cos(eleC.Theta()));
        // termA1 = pi0M2term - "Proton Mass"*("Initial Beam Energy" - "Electron Momentum" + "Proton Mass") + "Initial Beam Energy"*"Electron Momentum"*(1 - cos("Electron Theta Angle"))

    auto termB1 = (Beam_Energy)*cos(proC.Theta()) - eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC));
        // termB1 = "Initial Beam Energy"*cos("Proton Theta Angle") - "Electron Momentum"*cos("Angle between the Proton and Electron")

    auto termC1 = eleC.P() - (Beam_Energy) - (Proton_M);
        // termC1 = "Electron Momentum" - "Initial Beam Energy" - "Proton Mass"

    auto termA2 = (termB1*termB1 - termC1*termC1);
    auto termB2 = -2*termB1*termA1;
    auto termC2 = termA1*termA1 - termC1*termC1*(Proton_M)*(Proton_M);
    
    auto sqrt_Term = termB2*termB2 - 4*termA2*termC2;

    return (sqrt_Term > 0.05);
    """])
            
            Calculated_Exclusive_Cuts = "".join(["""
                double Proton_M  = """, str(Particle_Mass_Proton), """;
                auto beam = ROOT::Math::PxPyPzMVector(0, 0, """, str(Beam_Energy), """, 0);
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_M);
                auto ele  = ROOT::Math::PxPyPzMVector(""", "ex, ey, ez" if("(GEN)" not in str(event_Name)) else "ex0, ey0, ez0", """, 0);
                auto pro0 = ROOT::Math::PxPyPzMVector(prox, proy, proz, Proton_M);
                auto MM_Vector = beam + targ - ele - pro0;

                auto cut_up = 0.2;
                auto cut_down = -0.2;
                if(esec == 1){
                    // Upper Cut
                    cut_up = (-0.010158)*el + (0.201356);
                    // Lower Cut
                    cut_down = (-0.004594)*el + (-0.111018);
                }
                if(esec == 2){
                    // Upper Cut
                    cut_up = (-0.006247)*el + (0.162532);
                    // Lower Cut
                    cut_down = (-0.000149)*el + (-0.152814);
                }
                if(esec == 3){
                    // Upper Cut
                    cut_up = (-0.003488)*el + (0.109428);
                    // Lower Cut
                    cut_down = (-0.00153)*el + (-0.182898);
                }
                if(esec == 4){
                    // Upper Cut
                    cut_up = (0.004176)*el + (0.097037);
                    // Lower Cut
                    cut_down = (0.016216)*el + (-0.250681);
                }
                if(esec == 5){
                    // Upper Cut
                    cut_up = (-0.00779)*el + (0.198103);
                    // Lower Cut
                    cut_down = (-0.001479)*el + (-0.117437);
                }
                if(esec == 6){
                    // Upper Cut
                    cut_up = (-0.007872)*el + (0.183541);
                    // Lower Cut
                    cut_down = (-0.002117)*el + (-0.126953);
                }
                
                return (MM_Vector.M2() < cut_up && MM_Vector.M2() > cut_down);
                
            """])
            
        if("Out" in datatype):
            Calculated_Exclusive_Cuts = "".join(["""
                double Proton_M  = """, str(Particle_Mass_Proton), """;
                auto beam = ROOT::Math::PxPyPzMVector(0, 0, """, str(Beam_Energy), """, 0);
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_M);
                auto ele  = ROOT::Math::PxPyPzMVector(""", "ex, ey, ez" if("(GEN)" not in str(event_Name)) else "ex0, ey0, ez0", """, 0);
                auto pro0 = ROOT::Math::PxPyPzMVector(prox, proy, proz, Proton_M);
                auto MM_Vector = beam + targ - ele - pro0;

                auto cut_up = 0.2;
                auto cut_down = -0.2;
                if(esec == 1){
                    // Upper Cut
                    cut_up = (-0.001608)*el + (0.198384);
                    // Lower Cut
                    cut_down = (-0.001539)*el + (-0.083213);
                }
                if(esec == 2){
                    // Upper Cut
                    cut_up = (-0.005089)*el + (0.208978);
                    // Lower Cut
                    cut_down = (-0.005069)*el + (-0.072368);
                }
                if(esec == 3){
                    // Upper Cut
                    cut_up = (-0.004209)*el + (0.208964);
                    // Lower Cut
                    cut_down = (-0.003013)*el + (-0.079125);
                }
                if(esec == 4){
                    // Upper Cut
                    cut_up = (-0.002011)*el + (0.193354);
                    // Lower Cut
                    cut_down = (-0.001948)*el + (-0.087898);
                }
                if(esec == 5){
                    // Upper Cut
                    cut_up = (-0.005285)*el + (0.222998);
                    // Lower Cut
                    cut_down = (-0.003286)*el + (-0.068903);
                }
                if(esec == 6){
                    // Upper Cut
                    cut_up = (0.006808)*el + (0.195471);
                    // Lower Cut
                    cut_down = (0.007351)*el + (-0.08916);
                }
                
                return (MM_Vector.M2() < cut_up && MM_Vector.M2() > cut_down);
                
            """])
    ##################################################################################################################################
    ##==============================================================================================================================##
    ##===============##=============##         End of Exclusivity Cuts (Using MM^2 from epπ0)         ##=============##=============##
    ##==============================================================================================================================##
    ##################################################################################################################################    
    
    
    
    
    #######################################################################################################################################
    ##===================================================================================================================================##
    ##===============##=============##         Exclusivity Cuts (Using WM from Elastic Scattering)         ##=============##=============##
    ##===================================================================================================================================##
    #######################################################################################################################################
    if("E" in event_type):
        
        if("Fall" in pass_version):
            if(("Pass 2" in str(pass_version)) and ("Out" not in str(datatype))):
                print(color.BBLUE, "\nUSING NEW EXCLUSIVITY CUTS FOR INBENDING FALL 2018 DATA (Pass 2)\n\n", color.END)
            if(("Pass 2" in str(pass_version)) and ("Out"     in str(datatype))):
                print(color.BBLUE, "\nUSING NEW EXCLUSIVITY CUTS FOR OUTBENDING FALL 2018 DATA (Pass 2)\n\n", color.END)
            Calculated_Exclusive_Cuts = "".join(["""        
            // For Invariant Mass Cut (Fall 2018 (Pass 2) - Based on a 1.75*sigma and 3*sigma cuts on the Invarient Mass - Upper Cut is 1.75*sigma - Lower Cut is 3*sigma - Linear Functions of Momentum - No Phi dependence):
            auto Beam_Energy = """, str(Beam_Energy), """;
            auto Proton_Mass = """, str(Particle_Mass_Proton), """;
            auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
            auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
            auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
            auto Cut_Variable = (beam + targ - eleC).M();
            auto Upper_Cut = 1.3;
            auto Lower_Cut = 0.7;
            if(esec == 1){
                Upper_Cut = (-0.0650775)*el + (1.6573556);
                Lower_Cut =  (0.0572346)*el + (0.2535145);
            }
            if(esec == 2){
                Upper_Cut = (-0.0295488)*el + (1.3342413);
                Lower_Cut =  (0.08144)*el + (0.0);
            }
            if(esec == 3){
                Upper_Cut = (-0.0772681)*el + (1.755999);
                Lower_Cut =  (0.0809523)*el + (0.0);
            }
            if(esec == 4){
                Upper_Cut = (-0.0590381)*el + (1.6139791);
                Lower_Cut =  (0.0805354)*el + (0.0576905);
            }
            if(esec == 5){
                Upper_Cut = (-0.0634982)*el + (1.6263832);
                Lower_Cut =  (0.0657277)*el + (0.1605387);
            }
            if(esec == 6){
                Upper_Cut = (-0.0472526)*el + (1.4835857);
                Lower_Cut =  (0.0832248)*el + (0.0);
            } 
            return ((Cut_Variable < Upper_Cut) && (Cut_Variable > Lower_Cut));
            """]) if(("Pass 2" in str(pass_version)) and ("Out" not in str(datatype))) else "".join(["""        
        // For Invariant Mass Cut (Outbending Fall 2018 (Pass 2) - Based on a 1.45*sigma and 2*sigma cuts on the Invarient Mass - Upper Cut is 1.45*sigma - Lower Cut is 2*sigma - Linear Functions of Momentum - No Phi dependence):
        auto Beam_Energy = """, str(Beam_Energy), """;
        auto Proton_Mass = """, str(Particle_Mass_Proton), """;
        auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
        auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
        auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
        auto Cut_Variable = (beam + targ - eleC).M();
        auto Upper_Cut = 1.3;
        auto Lower_Cut = 0.7;
        if(esec == 1){
            Upper_Cut = (-0.0445949)*el + (1.4938545);
            Lower_Cut =  (-0.0405884)*el + (1.1311165);
        }
        if(esec == 2){
            Upper_Cut = (-0.0315795)*el + (1.368575);
            Lower_Cut =  (-0.0781353)*el + (1.4513767);
        }
        if(esec == 3){
            Upper_Cut = (0.012916)*el + (0.9385967);
            Lower_Cut =  (-0.0631136)*el + (1.3075803);
        }
        if(esec == 4){
            Upper_Cut = (-0.0303366)*el + (1.357522);
            Lower_Cut =  (-0.0529724)*el + (1.2341513);
        }
        if(esec == 5){
            Upper_Cut = (-0.0490147)*el + (1.5081901);
            Lower_Cut =  (0.0180793)*el + (0.5865123);
        }
        if(esec == 6){
            Upper_Cut = (-0.0485971)*el + (1.5373772);
            Lower_Cut =  (-0.0676014)*el + (1.3853758);
        } 
        return ((Cut_Variable < Upper_Cut) && (Cut_Variable > Lower_Cut));
        """]) if("Pass 2" in str(pass_version)) else "esec != -2"
        
        else:
            if(("Pass 2" in str(pass_version)) and ("Out" not in str(datatype))):
                print(color.BBLUE, "\nUSING NEW EXCLUSIVITY CUTS FOR SPRING 2019 DATA (Pass 2)\n\n", color.END)
            if(("Pass 1" in str(pass_version)) and ("Out" not in str(datatype))):
                print(color.BBLUE, "\nUSING NEW EXCLUSIVITY CUTS FOR SPRING 2019 DATA (Pass 1)\n\n", color.END)
                

            Calculated_Exclusive_Cuts = "".join(["""        
            // For Invariant Mass Cut (Spring 2019 (Pass 2) - Based on a 1.75*sigma and 2*sigma cuts on the Invarient Mass - Upper Cut is 1.75*sigma - Lower Cut is 2*sigma - Linear Functions of Momentum - No Phi dependence):
            auto Beam_Energy = """, str(Beam_Energy), """;
            auto Proton_Mass = """, str(Particle_Mass_Proton), """;
            auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
            auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
            auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
            auto Cut_Variable = (beam + targ - eleC).M();
            auto Upper_Cut = 1.3;
            auto Lower_Cut = 0.7;
            if(esec == 1){
                Upper_Cut = (-0.0699295)*el + (1.6677124);
                Lower_Cut =  (0.0408107)*el + (0.4751967);
            }
            if(esec == 2){
                Upper_Cut = (-0.0570852)*el + (1.5409955);
                Lower_Cut =  (0.0580087)*el + (0.291677);
            }
            if(esec == 3){
                Upper_Cut = (-0.0654184)*el + (1.615408);
                Lower_Cut =  (0.0756399)*el + (0.1295325);
            }
            if(esec == 4){
                Upper_Cut = (-0.0715222)*el + (1.681577);
                Lower_Cut =  (0.0449407)*el + (0.4354458);
            }
            if(esec == 5){
                Upper_Cut = (-0.0696714)*el + (1.6621209);
                Lower_Cut =  (0.0446726)*el + (0.4418454);
            }
            if(esec == 6){
                Upper_Cut = (-0.0639287)*el + (1.6097967);
                Lower_Cut =  (0.0230642)*el + (0.6176546);
            } 
            return ((Cut_Variable < Upper_Cut) && (Cut_Variable > Lower_Cut));
            """]) if(("Pass 2" in str(pass_version)) and ("Out" not in str(datatype))) else "".join(["""        
            // For Invariant Mass Cut (Spring 2019 (Pass 1) - Based on a 2-sigma cut (upper bounds) on the Invarient Mass - Upper Cut is a function of the electron momentum - Lower cut is a constant and based on a 3-sigma cut - No Phi dependence):
            auto Beam_Energy = """, str(Beam_Energy), """;
            auto Proton_Mass = """, str(Particle_Mass_Proton), """;
            auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
            auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
            auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
            auto Cut_Variable = (beam + targ - eleC).M();
            auto Upper_Cut = 1.3;
            auto Lower_Cut = 0.7;
            if(esec == 1){
                Upper_Cut = (-0.0504201)*el + (1.5);
                Lower_Cut = (0.7361207);
            }
            if(esec == 2){
                Upper_Cut = (-0.0505571)*el + (1.5);
                Lower_Cut = (0.7398295);
            }
            if(esec == 3){
                Upper_Cut = (-0.0562397)*el + (1.5);
                Lower_Cut = (0.6487454);
            }
            if(esec == 4){
                Upper_Cut = (-0.0515732)*el + (1.5);
                Lower_Cut = (0.7500403);
            }
            if(esec == 5){
                Upper_Cut = (-0.0522959)*el + (1.5);
                Lower_Cut = (0.7597503);
            }
            if(esec == 6){
                Upper_Cut = (-0.0526918)*el + (1.5);
                Lower_Cut = (0.7333811);
            } 
            return ((Cut_Variable < Upper_Cut) && (Cut_Variable > Lower_Cut));
            """]) if(("Pass 1" in str(pass_version)) and ("Out" not in str(datatype))) else "".join(["""        
            // For Invariant Mass Cut (Determined with the help of Azimuthal Kinematic Cut applied on the invariant mass histogram):
            auto Beam_Energy = """, str(Beam_Energy), """;
            auto Proton_Mass = """, str(Particle_Mass_Proton), """;
            auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
            auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
            auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
            auto Cut_Variable = (beam + targ - eleC).M();
            double Cut_Upper = 1.3;
            double Cut_Lower = 0.7;
            if(esec == 1){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 1.35;
                    Cut_Lower = 0.8;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 1.23;
                    Cut_Lower = 0.83;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 1.27;
                    Cut_Lower = 0.81;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 1.4;
                    Cut_Lower = 0.75;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 1.31;
                    Cut_Lower = 0.73;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 1.31;
                    Cut_Lower = 0.78;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 1.18;
                    Cut_Lower = 0.79;
                }
                if(eleC.P() > 8.95 && eleC.P() < 9.45){
                    Cut_Upper = 1.11;
                    Cut_Lower = 0.8;
                }
                if(eleC.P() > 9.45 && eleC.P() < 9.95){
                    Cut_Upper = 1.2;
                    Cut_Lower = 0.78;
                }
            }
            if(esec == 2){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 1.31;
                    Cut_Lower = 0.74;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 1.28;
                    Cut_Lower = 0.75;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 1.25;
                    Cut_Lower = 0.77;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 1.21;
                    Cut_Lower = 0.77;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 1.19;
                    Cut_Lower = 0.78;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 1.2;
                    Cut_Lower = 0.77;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 1.12;
                    Cut_Lower = 0.78;
                }
                if(eleC.P() > 8.95 && eleC.P() < 9.45){
                    Cut_Upper = 1.1;
                    Cut_Lower = 0.79;
                }
                if(eleC.P() > 9.45 && eleC.P() < 9.95){
                    Cut_Upper = 1.2;
                    Cut_Lower = 0.82;
                }
            }
            if(esec == 3){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 1.45;
                    Cut_Lower = 0.57;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 1.19;
                    Cut_Lower = 0.69;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 1.16;
                    Cut_Lower = 0.65;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 1.23;
                    Cut_Lower = 0.61;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 1.14;
                    Cut_Lower = 0.66;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 1.09;
                    Cut_Lower = 0.69;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 1.05;
                    Cut_Lower = 0.68;
                }
                if(eleC.P() > 8.95 && eleC.P() < 9.45){
                    Cut_Upper = 1.03;
                    Cut_Lower = 0.64;
                }
                if(eleC.P() > 9.45 && eleC.P() < 9.95){
                    Cut_Upper = 1.2;
                    Cut_Lower = 0.66;
                }
            }
            if(esec == 4){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 1.19;
                    Cut_Lower = 0.77;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 1.27;
                    Cut_Lower = 0.7;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 1.25;
                    Cut_Lower = 0.69;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 1.27;
                    Cut_Lower = 0.69;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 1.23;
                    Cut_Lower = 0.74;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 1.14;
                    Cut_Lower = 0.76;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 1.12;
                    Cut_Lower = 0.79;
                }
                if(eleC.P() > 8.95 && eleC.P() < 9.45){
                    Cut_Upper = 1.1;
                    Cut_Lower = 0.8;
                }
                if(eleC.P() > 9.45 && eleC.P() < 9.95){
                    Cut_Upper = 1.2;
                    Cut_Lower = 0.81;
                }
            }
            if(esec == 5){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 1.26;
                    Cut_Lower = 0.81;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 1.2;
                    Cut_Lower = 0.8;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 1.2;
                    Cut_Lower = 0.77;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 1.2;
                    Cut_Lower = 0.76;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 1.17;
                    Cut_Lower = 0.78;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 1.13;
                    Cut_Lower = 0.78;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 1.1;
                    Cut_Lower = 0.82;
                }
                if(eleC.P() > 8.95 && eleC.P() < 9.45){
                    Cut_Upper = 1.06;
                    Cut_Lower = 0.83;
                }
                if(eleC.P() > 9.45 && eleC.P() < 9.95){
                    Cut_Upper = 1.2;
                    Cut_Lower = 0.81;
                }
            }
            if(esec == 6){
                if(eleC.P() > 5.45 && eleC.P() < 5.95){
                    Cut_Upper = 1.19;
                    Cut_Lower = 0.86;
                }
                if(eleC.P() > 5.95 && eleC.P() < 6.45){
                    Cut_Upper = 1.12;
                    Cut_Lower = 0.85;
                }
                if(eleC.P() > 6.45 && eleC.P() < 6.95){
                    Cut_Upper = 1.21;
                    Cut_Lower = 0.79;
                }
                if(eleC.P() > 6.95 && eleC.P() < 7.45){
                    Cut_Upper = 1.24;
                    Cut_Lower = 0.75;
                }
                if(eleC.P() > 7.45 && eleC.P() < 7.95){
                    Cut_Upper = 1.14;
                    Cut_Lower = 0.76;
                }
                if(eleC.P() > 7.95 && eleC.P() < 8.45){
                    Cut_Upper = 1.17;
                    Cut_Lower = 0.76;
                }
                if(eleC.P() > 8.45 && eleC.P() < 8.95){
                    Cut_Upper = 1.14;
                    Cut_Lower = 0.77;
                }
                if(eleC.P() > 8.95 && eleC.P() < 9.45){
                    Cut_Upper = 1.06;
                    Cut_Lower = 0.8;
                }
                if(eleC.P() > 9.45 && eleC.P() < 9.95){
                    Cut_Upper = 1.2;
                    Cut_Lower = 0.8;
                }
            }
            return ((Cut_Variable < Cut_Upper) && (Cut_Variable > Cut_Lower));
            """]) if("Out" not in datatype) else "".join(["""
            auto Beam_Energy = """, str(Beam_Energy), """;
            auto Proton_Mass = """, str(Particle_Mass_Proton), """;
            auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
            auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
            auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
            auto Cut_Variable = (beam + targ - eleC).M();

            double Phi = (180/3.1415926)*atan2(ey, ex);
            if(((esec == 4 || esec == 3) && Phi < 0) || (esec > 4 && Phi < 90)){
                Phi += 360;
            }
            double phi = (Phi - (esec - 1)*60) - (30/eleC.P());

            double Cut_Upper = 1.2;
            double Cut_Lower = 0.7;
            // double Cut_Upper = -0.0346*(eleC.P()) + 1.4574;
            // double Cut_Lower = -0.0047*(eleC.P()) + 0.8646;
            if(esec == 1){
                Cut_Upper = ((-0.0024)*phi + (-0.0131))*eleC.P() + ((0.0264)*phi + (1.1944));
                Cut_Lower = ((-0.0013)*phi + (-0.0191))*eleC.P() + ((0.0169)*phi + (0.9950));
            }
            if(esec == 2){
                Cut_Upper = ((-0.0011)*phi + (-0.0063))*eleC.P() + ((0.0137)*phi + (1.1209));
                Cut_Lower = ((-0.0012)*phi + (-0.0217))*eleC.P() + ((0.0151)*phi + (1.0104));
            }
            if(esec == 3){
                Cut_Upper =  ((0.0011)*phi + (-0.0087))*eleC.P() + ((-0.0111)*phi + (1.1678));
                Cut_Lower =  ((0.0020)*phi + (-0.0231))*eleC.P() + ((-0.0204)*phi + (1.0516));
            }
            if(esec == 4){
                Cut_Upper = ((-0.0014)*phi + (-0.0139))*eleC.P() +  ((0.0128)*phi + (1.1997));
                Cut_Lower =  ((0.0013)*phi + (-0.0320))*eleC.P() + ((-0.0137)*phi + (1.1266));
            }
            if(esec == 5){
                Cut_Upper = ((-0.0007)*phi + (-0.0357))*eleC.P() + ((0.0072)*phi + (1.3869));
                Cut_Lower = ((-0.0006)*phi + (-0.0619))*eleC.P() + ((0.0062)*phi + (1.3819));
            }
            if(esec == 6){
                Cut_Upper = ((0.0001)*phi + (-0.0417))*eleC.P() + ((-0.0001)*phi + (1.5031));
                Cut_Lower = ((0.0008)*phi + (-0.0462))*eleC.P() + ((-0.0071)*phi + (1.3042));
            }
            return ((Cut_Variable < Cut_Upper) && (Cut_Variable > Cut_Lower));
            """])
            Calculated_Exclusive_Cuts_v2 = "".join(["""
            auto Beam_Energy = """, str(Beam_Energy), """;
            auto Proton_Mass = """, str(Particle_Mass_Proton), """;
            auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
            auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
            auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
            auto Cut_Variable = (beam + targ - eleC).M();
            double Cut_Upper = 1.2;
            double Cut_Lower = 0.7;
            return ((Cut_Variable < Cut_Upper) && (Cut_Variable > Cut_Lower));
            """])
        
    ############################################################################################################################################
    ##========================================================================================================================================##
    ##===============##=============##        End of Exclusivity Cuts (Using WM from Elastic Scattering)        ##=============##=============##
    ##========================================================================================================================================##
    ############################################################################################################################################


    
    
    

    ############################################################################################################################################
    ##=================================================######################################=================================================##
    ##=================================================##                                  ##=================================================##
    ##===============##===============##===============##      Exclusivity Cuts (End)      ##===============##===============##===============##
    ##=================================================##                                  ##=================================================##
    ##=================================================######################################=================================================##
    ############################################################################################################################################
    
    # # # # esec != -2 This line is just to help search through code (does nothing)
    
    
    Invariant_Mass_Cuts_Q = "Cut_On"
    # Invariant_Mass_Cuts_Q = "Cut_Off"
    
    if(Invariant_Mass_Cuts_Q == "Cut_Off" or event_type != "ES"):
        # print("\nCutting on Invariant Mass (Only W < 3 GeV)\n" if(event_type == "ES") else "\nUsing Elastic Cuts\n")
        # print("Not using any additional cuts...")
        CutChoice, CutChoice_2 = "none", "none"
    
    
    if(CutChoice in ['', 'none']):
        kinematicCuts = ["", Calculated_Exclusive_Cuts]
    elif(CutChoice_2 not in ["", "none"]):
        kinematicCuts = ["", Calculated_Exclusive_Cuts, CutChoice, CutChoice_2, "Both", "Both_2", "Both_3", "All"]
    else:
        kinematicCuts = ["", Calculated_Exclusive_Cuts, CutChoice, "Both"]
        
    if("ES" == event_type):
        kinematicCuts = ["", Calculated_Exclusive_Cuts, CutChoice, CutChoice_2, "Both_3", "All"]
    
    if(Calculated_Exclusive_Cuts_v2 != "esec != -2"):
        kinematicCuts.append(Calculated_Exclusive_Cuts_v2)
    if(Calculated_Exclusive_Cuts_v3 != "esec != -2"):
        kinematicCuts.append(Calculated_Exclusive_Cuts_v3)
    if(Calculated_Exclusive_Cuts_v4 != "esec != -2"):
        kinematicCuts.append(Calculated_Exclusive_Cuts_v4)
    if(Calculated_Exclusive_Cuts_v5 != "esec != -2"):
        kinematicCuts.append(Calculated_Exclusive_Cuts_v5)
    # if(Calculated_Exclusive_Cuts_v6 != "esec != -2"):
    #     kinematicCuts.append(Calculated_Exclusive_Cuts_v6)
    # if(Calculated_Dp_Cut != "esec != -2"):
    #     # kinematicCuts = [Calculated_Dp_Cut, Calculated_Dp_Cut_V2]
    #     kinematicCuts = [Calculated_Dp_Cut]

    if("(GEN)" in event_Name):
        kinematicCuts = ["", Calculated_Dp_Cut_V2]
    elif("MC" in event_Name):
        kinematicCuts.append(Calculated_Dp_Cut_V2)
        
    def Cut_Function(Data_Frame, Input_Cut, Output_Type="Default"):
        
        Cut_Title = ""
        if(str(Input_Cut) == str(Calculated_Exclusive_Cuts)):
            Cut_Title = "Calculated Exclusivity Cuts"
        if(str(Input_Cut) == str(Calculated_Exclusive_Cuts_v2)):
            Cut_Title = "Calculated Exclusivity Cuts (Basic)"
        if(str(Input_Cut) == str(Calculated_Exclusive_Cuts_v3)):
            Cut_Title = "Calculated Exclusivity Cuts (Based on Both Angles)"
        if(str(Input_Cut) == str(Calculated_Exclusive_Cuts_v4)):
            Cut_Title = "Missing Mass Squared Cut"
        if(str(Input_Cut) == str(Calculated_Exclusive_Cuts_v5)):
            Cut_Title = "Corrected (Full) Missing Mass Squared Cut"
        if(str(Input_Cut) == str(Calculated_Exclusive_Cuts_v6)):
            Cut_Title = "Corrected (EL) Missing Mass Squared Cut"
        if(str(Input_Cut) == str(CutChoice)):
            Cut_Title = "Azimuthal Kinematic Cut"
        if(CutChoice_2 not in ["", "none"] and str(Input_Cut) == str(CutChoice_2)):
            Cut_Title = "Calculated Polar Kinematic Cut"
        if(str(Input_Cut) == "Both"):
            Cut_Title = "Invariant Mass and Azimuthal Angle Cuts"
        if(str(Input_Cut) == "Both_2"):
            Cut_Title = "Invariant Mass and Polar Angle Cuts"
        if(str(Input_Cut) == "Both_3"):
            Cut_Title = "Azimuthal and Polar Angle Cuts"
        if(str(Input_Cut) == "All"):
            Cut_Title = "All Additional Cuts"
        if(str(Input_Cut) == str(Calculated_Dp_Cut)):
            Cut_Title = "Large Dp Cut"
        if(str(Input_Cut) == str(Calculated_Dp_Cut_V2)):
            Cut_Title = "|Dp| < 0.005 GeV Cut"
            Cut_Title = "Square Root Term Cut"
        if(str(Input_Cut) == "esec != -2"):
            Cut_Title = "Error: Undefined Cut"
            print(f"{color.Error}{Cut_Title}!{color.END}")
            

            
        if(Output_Type == "Title"):
            return Cut_Title

        Cut_Data_Frame = Data_Frame
        if(Input_Cut not in ["", "none"]):
            try:
                if(  "Both"   == Input_Cut and CutChoice   != "none"):
                    Cut_Data_Frame = Cut_Data_Frame.Filter(Calculated_Exclusive_Cuts)
                    Cut_Data_Frame = Cut_Data_Frame.Filter(CutChoice)
                elif("Both_2" == Input_Cut and CutChoice_2 != ""     and CutChoice_2 != "none"):
                    Cut_Data_Frame = Cut_Data_Frame.Filter(Calculated_Exclusive_Cuts)
                    Cut_Data_Frame = Cut_Data_Frame.Filter(CutChoice_2)
                elif("Both_3" == Input_Cut and CutChoice   != "none" and CutChoice_2 not in ["", "none"]):
                    Cut_Data_Frame = Cut_Data_Frame.Filter(CutChoice)
                    Cut_Data_Frame = Cut_Data_Frame.Filter(CutChoice_2)
                elif("All"    == Input_Cut and CutChoice   != "none" and CutChoice_2 not in ["", "none"]):
                    Cut_Data_Frame = Cut_Data_Frame.Filter(Calculated_Exclusive_Cuts)
                    Cut_Data_Frame = Cut_Data_Frame.Filter(CutChoice)
                    Cut_Data_Frame = Cut_Data_Frame.Filter(CutChoice_2)
                else:
                    Cut_Data_Frame = Data_Frame.Filter(Input_Cut)
            except Exception as e:
                print("".join([color.Error, "ERROR: Failed to make the cut: ", color.END, str(Input_Cut), "\n\n", color.Error, "Error Reads as: ", str(e), color.END]))
            
        if(Output_Type == "Default"):
            return [Cut_Data_Frame, Cut_Title]
        elif(Output_Type == "Title"):
            return Cut_Title
        elif("Data" in Output_Type):
            return Cut_Data_Frame
        else:
            print("Error in arguements of 'Cut_Function'. Default output being used...")
            return [Cut_Data_Frame, Cut_Title]
    

    print(color.BOLD + "Running the code with the following cuts:" + color.END)
    for Cuts in kinematicCuts:
        print("\t" + str(Cut_Function("Data_Frame", Cuts, "Title") if(Cut_Function("Data_Frame", Cuts, "Title") != "") else "No (Additonal) Cuts"))
    
    #########################################################################################################################################################
    ##=====================================================================================================================================================##
    ##==============##============##============##         Helpful Functions for Making Histograms (End)         ##============##============##============##
    ##=====================================================================================================================================================##
    #########################################################################################################################################################

    # All code above this point is dedicated to subroutines and calculations
    
    
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #
    # All code beyond this point is dedicated to looping through the options selected for histogram creation (options to be selected below)
    #


    #=======================================================================================================================================================================================================================================================#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #=======================================================================================================================================================================================================================================================#










    #######################################################################################################################################################
    ##===================================================================================================================================================##
    ##==============##===================##============##         Choices for Making Histograms         ##============##===================##============##
    ##===================================================================================================================================================##
    #######################################################################################################################################################



    ######################################################################################
    ##=====##=====##=====##     Choices for Delta P Histograms     ##=====##=====##=====##
    ######################################################################################


    # Input the sector numbers you wish to run in the list below ('all' or 0 corresponds to running all the sectors at once without filtering)
    Delta_Pip_histo_SecList = ['all', 1, 2, 3, 4, 5, 6]
    # This value corresponds to the π+ pion AND the proton (depedending on the event type)



    # # Extra Sector Filter that filters based on Electron Sectors (instead of just π+ Sectors). ExtraElectronSecListFilterOn = 'no' turns this option off
    # ExtraElectronSecListFilterOn = 'no'
    ExtraElectronSecListFilterOn = 'yes'
    
    
    if(event_type not in ["SP", "MC"] and "E" not in event_type):
        Delta_Pip_histo_SecList = ['all', 1, 2, 3, 4, 5, 6] # Only the proton correction is available for the double pion channel (Turned off π0 channel as well)
        ExtraElectronSecListFilterOn = 'no'
    

    if(ExtraElectronSecListFilterOn == 'yes'):
        ExtraElectronSecListFilter = ['all', 1, 2, 3, 4, 5, 6]
    else:
        ExtraElectronSecListFilter = ['all']


    # # Combine Electron and π+ Filters? 
    # Combine_el_pip_filters_Q = "yes"
    Combine_el_pip_filters_Q = "no"
    
    
    if("E" in event_type and Combine_el_pip_filters_Q == "no"):
        Delta_Pip_histo_SecList = ["all"]
        
#     if("MC" in event_Name):
#         Delta_Pip_histo_SecList = ["all"]
        
        
    if((1 in Delta_Pip_histo_SecList) and (("status" in rdf.GetColumnNames()) or ("artsec" in rdf.GetColumnNames()))):
        if("Central"   in pass_version):
            Delta_Pip_histo_SecList = ['all', 7, 8, 9, 10, 11, 12]
        elif("Forward" in pass_version):
            Delta_Pip_histo_SecList = ['all', 1, 2, 3, 4, 5, 6]
        else:
            Delta_Pip_histo_SecList.append(7)
            Delta_Pip_histo_SecList.append(8)
            Delta_Pip_histo_SecList.append(9)
            Delta_Pip_histo_SecList.append(10)
            Delta_Pip_histo_SecList.append(11)
            Delta_Pip_histo_SecList.append(12)


    Delta_P_histo_CorList = ['mm0']
    Delta_P_histo_CorList.append("mmRGK")
    
    if(event_type in ["SP", "MC"]):
        if(datatype == "Inbending"):
            # Delta_P_histo_CorList = ['mm0', 'mmEF', 'mmEF_PipMMEF']            
            Delta_P_histo_CorList = ['mm0']
            if("Spring 2019 - Pass 2" in str(pass_version)):
                Delta_P_histo_CorList.append("mmRP2")
                Delta_P_histo_CorList.append("mmRP2_PipMMP2")
            elif("Pass 2" in str(pass_version)):
                Delta_P_histo_CorList.append("mmfaP2")
                Delta_P_histo_CorList.append("mmfaP2_PipMMfaP2")
            else:
                Delta_P_histo_CorList.append("mmEF")
                Delta_P_histo_CorList.append("mmEF_PipMMEF")
        if(datatype == "Outbending"):
            # Delta_P_histo_CorList = ['mm0', 'mmEF', 'mmExF', 'mmEF_PipMMEF', 'mmExF_PipMMExF']
            Delta_P_histo_CorList = ['mm0', 'mmEF',   'mmEF_PipMMEF']
            Delta_P_histo_CorList = ['mm0', 'mmfaP2', 'mmfaP2_PipMMfaP2']
            
        if("Pass 2" in str(pass_version)):
            Delta_P_histo_CorList_TEMP = Delta_P_histo_CorList
            for EL_cor_ii in Delta_P_histo_CorList_TEMP:
                if("ELPipMM" not in EL_cor_ii):
                    if("PipMM"   in EL_cor_ii):
                        Delta_P_histo_CorList.append(EL_cor_ii.replace("_PipMM", "_ELPipMM"))
                        Delta_P_histo_CorList.remove(EL_cor_ii)
                    else:
                        Delta_P_histo_CorList.append(f"{EL_cor_ii}_ELPipMM0")
                    # if("mm0" not in str(EL_cor_ii)):
                    #     Delta_P_histo_CorList.remove(EL_cor_ii)
            del Delta_P_histo_CorList_TEMP



        # # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        Delta_P_histo_CompareList = ['pi+', 'el']   # Show both corrections
        # Delta_P_histo_CompareList = ['el']          # Electron Corrections only
        # Delta_P_histo_CompareList = ['pi+']         # Pi+ Corrections only
            
            
    if(event_type == "DP"):
        if(datatype == "Inbending"):
            Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmEF_NoELC', 'mmEF', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF']
        if(datatype == "Outbending"):
            Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmEF_NoELC', 'mmEF', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF']
            
            
        # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        Delta_P_histo_CompareList = ['pro']
            
            
    if(event_type == "P0"):
        if(datatype == "Inbending"):
            Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_EF']
            
        if(datatype == "Outbending"):
            Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_EF']
            
        # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        # Delta_P_histo_CompareList = ['pro', 'el']
        Delta_P_histo_CompareList = ['pro']
        
        
    if(event_type == "ES"):
        if(datatype == "Inbending"):
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF']
            
        if(datatype == "Outbending"):
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF']
            
        # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        # Delta_P_histo_CompareList = ['pro', 'el']
        Delta_P_histo_CompareList = ['el']
        
    if(event_type == "EO"):
        if(datatype == "Inbending"):
            Delta_P_histo_CorList = ['mm0']
            if("Spring 2019 - Pass " in str(pass_version)):
                # Delta_P_histo_CorList.append("mmP2")
                Delta_P_histo_CorList.append("mmRP2")
            elif("Pass 2" in str(pass_version)):
                Delta_P_histo_CorList.append("mmfaP2")
            else:
                Delta_P_histo_CorList.append("mmEF")
                
                
        if(datatype == "Outbending"):
            Delta_P_histo_CorList = ['mm0', 'mmEF'] if("Pass 2" not in str(pass_version)) else ['mm0', 'mmfaP2']

        Delta_P_histo_CompareList = ['el']


    if("pi+" not in Delta_P_histo_CompareList and 'pro' not in Delta_P_histo_CompareList):
        Delta_Pip_histo_SecList = ["all"]

        
    Delta_P_histo_CorList.append("mmRGK")
    # Delta_P_histo_CorList = ['mm0']

    
    # Set the y-axis range od the ∆P histograms:
        # Note: original default binning was set to 200 bins for a range of -1 to 1 (halved for the elastic colisions)
    if("E" not in event_type):
        extendx_min, extendx_max = -3, 3
        extendx_min, extendx_max = -1, 1
        size_of_Dp_Bins = 0.005
    else:
        extendx_min, extendx_max = -1, 1
        size_of_Dp_Bins = 0.005
#     if("MC" in event_Name):
#         extendx_min, extendx_max = -0.05, 0.05
#         extendx_min, extendx_max = -0.02, 0.02
#         size_of_Dp_Bins = 0.0001
    
    extendx_min += -0.5*size_of_Dp_Bins
    extendx_max +=  0.5*size_of_Dp_Bins
        
    NumOfExtendedBins = round((extendx_max - extendx_min)/size_of_Dp_Bins)


    # For using ShowBackground() with the slices of the extra 2D histograms
    # SBehQ = 'yes'
    SBehQ = 'no'
    
    
    if(('pro' in Delta_P_histo_CompareList) and (event_type in ["DP"])):
        extra_Dp_calc = ["D_p", "D_p_L"]
        # extra_Dp_calc = ["D_p", "D_p_No_C"]
        # extra_Dp_calc = ["D_p", "D_p_S", "D_p_F"]
    elif(('pro' in Delta_P_histo_CompareList) and (event_type in ["P0"]) and ("MC" in event_Name)):
        extra_Dp_calc = ["D_p", "D_p_L", "D_p_G", "D_p_gL"]
        extra_Dp_calc = ["D_p", "D_p_L"]
        extra_Dp_calc = ["D_p", "D_p_L", "D_p_a", "D_p_b", "D_p_c", "D_p_sqrt"]
    else:
        extra_Dp_calc = ["D_p"]


    # Number of (π+/pro) phi bins
    NumPhiBins = ['1', '3']
    # NumPhiBins = ['1']
    
    if("E" in event_type or ("pi+" not in Delta_P_histo_CompareList and 'pro' not in Delta_P_histo_CompareList)):
        NumPhiBins = ['1']


    # # Number of (electron) phi bins
    # To run code normally (without electron phi bins in ∆P histograms), let NumPhiBinsEL = ['1'] (anything else will cut histograms based on electron phi angles)
    NumPhiBinsEL = ['1', '3']
    # NumPhiBinsEL = ['1']
    
    if(ExtraElectronSecListFilterOn == 'no'):
        NumPhiBinsEL = ['1']
        

    ##-----------------------------------------------------------------##
    ##-----##-----## Printing Choices for Delta P Histos ##-----##-----##
    ##-----------------------------------------------------------------##
    if(Delta_P_histo_Q == 'y'):
        print(color.BBLUE + "\nFor the ∆P histograms..." + color.END)
        print("".join(["The momentums being calculated are: ", str(Delta_P_histo_CompareList)]))

        print("".join(["The corrections that will run are: ", str(Delta_P_histo_CorList)]))
        print("These Corrections correspond to the following:")
        cor_num = 1
        for cor_names in Delta_P_histo_CorList:
            print("".join(["\t", str(cor_num), ") ", str(cor_names), " -> '", corNameTitles(cor_names, EVENT_TYPE=event_type, BENDING_TYPE=datatype), "'"]))
            cor_num += 1
        if(event_type != "EO"):
            print("".join(["The ", "Pi+" if(event_type in ["SP", "MC"]) else "proton", " sectors being run are: ", str(Delta_Pip_histo_SecList)]))
        print("".join(["The electron sectors being run are: ", str(ExtraElectronSecListFilter)]))
        if(event_type != "EO"):
            print("".join(["The list of (", "Pi+" if(event_type in ["SP", "MC"]) else "Proton", ") phi bins that will be run is: ", str(NumPhiBins)]))
        print("".join(["The list of (Electron) phi bins that will be run is: ", str(NumPhiBinsEL)]))

        if(str(SBehQ) != 'no'):
            print("".join(["Running fits with ShowBackground()?: ", str(SBehQ)]))
            
        print("extra_Dp_calc options selected:")
        for extra_option in extra_Dp_calc:
            print("".join(["\t(*) ", str(extra_option)]))

        # print("".join(["\nThe 2D histograms will be have a range of ", str(extendx_min), " < \u0394p < ", str(extendx_max)]))

    else:
        print(f"{color.BOLD}Not running ∆P histograms...{color.END}")
    ##----------------------------------------------------------------##
    ##-----##-----## Printed Choices for Delta P Histos ##-----##-----##
    ##----------------------------------------------------------------##

    # The value below will just help count the number of histograms made using these calculations (do not change or remove)
    Delta_P_histo_Count = 0



    ############################################################################################
    ##=====##=====##=====##     Choices for Delta P Histograms (End)     ##=====##=====##=====##
    ############################################################################################



    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



    ##############################################################################################
    ##=====##=====##=====##     Counting Delta P Histograms to be Made     ##=====##=====##=====##
    ##############################################################################################

    if(Delta_P_histo_Q == 'y'):

        for Cuts in kinematicCuts:
            for calc_option in extra_Dp_calc:
                for correction in Delta_P_histo_CorList:
                    for sec in Delta_Pip_histo_SecList:
                        for secEL in ExtraElectronSecListFilter:
                            for binning in NumPhiBins:
                                reglist = regList_Call(binning, 'pip' if(event_type in ["SP", "MC"]) else "pro", 1)
                                for binningEL in NumPhiBinsEL:

                                    if(Combine_el_pip_filters_Q != "yes"):
                                        if(binning == '3' and binningEL != "1"):
                                            continue
                                        if(binningEL == '3' and binning != "1"):
                                            continue
                                        if(sec != 'all' and secEL != 'all'):
                                            continue

                                    reglistEL = regList_Call(binningEL, 'el', 1)

                                    # Pi+/Proton Regions
                                    for region in reglist:
                                        # El Regions
                                        for regionEL in reglistEL:

                                            if('pi+' in Delta_P_histo_CompareList and Delta_Pip_histo_Q == 'y'):
                                                Delta_P_histo_Count += 1
                                                Delta_P_histo_Count += 1
                                                
                                            if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                                                Delta_P_histo_Count += 1
                                                Delta_P_histo_Count += 1
                                                if(str(calc_option) in ["D_p", "D_p_L"]):
                                                    Delta_P_histo_Count += 1

                                            if('el' in Delta_P_histo_CompareList and Delta_Pel_histo_Q == 'y'):
                                                Delta_P_histo_Count += 1
#                                                 Delta_P_histo_Count += 1

                                            
    if(event_type == "ES"):
        for Cuts in kinematicCuts:
            if(Cuts in ["Both_3", "All"]):
                continue
            # for Calc_Version in ["D_Angle_V1", "D_Angle_V2", "D_Angle_V3", "D_Angle_V4"]:
            for Calc_Version in ["D_Angle_V1", "D_Angle_V3"]:
                if((Cuts in [CutChoice, "Both"] and "V3" in Calc_Version) or (Cuts in [CutChoice_2, "Both_2"] and "V3" not in Calc_Version)):
                    continue
                for correction in Delta_P_histo_CorList:
                    for sec in ExtraElectronSecListFilter:
                        Delta_P_histo_Count += 1


    print(f"{color.BOLD}\nNumber of ∆P histograms to be made: {color.END}{str(Delta_P_histo_Count)}")

    Total_Extra = Delta_P_histo_Count
    Delta_P_histo_Count = 0


    #############################################################################################
    ##=====##=====##=====##     Counted Delta P Histograms to be Made     ##=====##=====##=====##
    #############################################################################################





    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#





    ###########################################################################################
    ##=====##=====##=====##     Choices for Missing Mass Histograms     ##=====##=====##=====##
    ###########################################################################################


    particleList, particle_plot_List = [], []
    
    if(event_type in ["SP", "MC"]):
        particleList       = ['el', 'pip']
        particle_plot_List = ['el', 'pip']
        # particleList = ['el']
        # particle_plot_List = ['el']
        
        
    if(event_type == "DP"):
        # particleList = ['el', 'pip', 'pro', 'pim']
        particleList = ['el', 'pip', 'pro']
        # particleList = ['pro']
        
        # particle_plot_List = ['el', 'pip', 'pro', 'pim']
        particle_plot_List = ['el', 'pip', 'pro']
        # particle_plot_List = ['pro']
        
        
    if(event_type == "P0"):
        particleList       = ['el', 'pro']
        particle_plot_List = ['el', 'pro']
        
        particleList       = ['pro']
        particle_plot_List = ['pro']

        
    if(event_type == "ES"):
        particleList       = ['el', 'pro']
        particle_plot_List = ['el', 'pro']
        # particleList = ['el']
        # particle_plot_List = ['el']
        
    if(event_type == "EO"):
        particleList       = ['el']
        particle_plot_List = ['el']

    correctionList = ['mm0']
    
    
    # Set automatic_MM_cor_select = True to use the same list of corrections for both the ∆P plots and the Missing Mass plots below
        # Set it to False if you want to run a different number of corrections for the Missing Mass Plots as compared to the ∆P Plots
    automatic_MM_cor_select = True
    if(automatic_MM_cor_select):
        print(f"{color.BOLD}\nUsing the same correction list for the Missing Mass Plots and was used for the ∆P Plots...\n{color.END}")
        correctionList = Delta_P_histo_CorList
    else:
        if(event_type in ["SP", "MC"]):
            if(datatype == "Inbending"):
                correctionList = ['mm0', 'mmEF', 'mmEF_PipMMEF']
                correctionList = ['mm0']
                if("Spring 2019 - Pass 2" in str(pass_version)):
                    # correctionList.append("mmP2")
                    correctionList.append("mmRP2")
                    # correctionList.append("mmP2_PipMMP2")
                    correctionList.append("mmRP2_PipMMP2")
                    # correctionList.append("mmRP2_PipMMsP2")
                else:
                    correctionList.append("mmEF")
                    correctionList.append("mmEF_PipMMEF")
            if(datatype == "Outbending"):
                correctionList = ['mm0', 'mmEF', 'mmEF_PipMMEF']

            if(event_type == "DP"):
                if(datatype == "Inbending"):
                    correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_NRE_NoELC', 'mmEF_PipMMEF_ProMMpro_NS_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_NRE', 'mmEF_PipMMEF_ProMMpro_NS']
                if(datatype == "Outbending"):
                    correctionList = ['mm0_NoELC', 'mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_F', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF']

            if(event_type == "P0"):
                if(datatype == "Inbending"):
                    correctionList = ['mm0']
                if(datatype == "Outbending"):
                    correctionList = ['mm0_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F', 'mmEF', 'mmEF_ProMMpro_EF']

            if(event_type == "ES"):
                if(datatype == "Inbending"):
                    correctionList = ['mm0', 'mmF']
                if(datatype == "Outbending"):
                    correctionList = ['mm0', 'mmF', 'mmEF']

            if(event_type == "EO"):
                if(datatype == "Inbending"):
                    correctionList = ['mm0', 'mmEF']
                    if("Spring 2019 - Pass " in str(pass_version)):
                        # correctionList.append("mmP2")
                        correctionList.append("mmRP2")
                if(datatype == "Outbending"):
                    correctionList = ['mm0', 'mmEF']



    binningList = ['1']
    # binningList = ['1','3','5']
    binningList = ['1', '3']
    # binningList = ['3']
    
    # if("E" in event_type):
    #     binningList = ['1']

    # Sector = 0 refers to all sectors so the code will start by making histograms that do not filter by sector
    # Any number 1-6 will correspond to the (DC) sector of that same number (above 6 is used for the Central Detector)

    
    SecRangeAll = [0, 1, 2, 3, 4, 5, 6]
    # SecRangeAll = [0]
    
    if((("status"     in rdf.GetColumnNames()) or ("artsec" in rdf.GetColumnNames())) and ("Forward" not in pass_version)):
        SecRangeAll = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        # Includes the Central Detector Sectors (7, 8, 9)





    ##-------------------------------------------------------##
    ##=====##=====##     Histogram Options     ##=====##=====##
    ##-------------------------------------------------------##
    # Run with the Missing Mass histograms?
        # Letting Run_Missing_Mass_Histos = 'no' will prevent the code from creating the Missing Mass histograms if the are not needed
    Run_Missing_Mass_Histos = 'yes'
    # Run_Missing_Mass_Histos = 'no'
    
    # Run with the Invariant Mass histograms?
        # Letting Run_Invariant_Mass_Histos = 'yes' causes the code to also create histograms for Invariant Mass vs the particle momentum
    # Run_Invariant_Mass_Histos = 'yes'
    Run_Invariant_Mass_Histos = 'no'
    
    if("E" in event_type):
        Run_Invariant_Mass_Histos = 'yes'
        Run_Missing_Mass_Histos   = 'no'
        # Elastic/Electron Only Channels use the Invariant Mass histograms instead of the Missing Mass ones
    

    # Letting Run_Phase_Space = 'yes' allows for the histograms without the missing mass values to be run
    Run_Phase_Space = 'yes'
    # Run_Phase_Space = 'no'
    
    Skip_Sector_Phase_Space = "yes"
    Skip_Sector_Phase_Space = "no"


    # This list is for the extra phase space histograms which can be run with or without shifts      
    # shiftList = ['', 'S', 'NS']
    shiftList = ['', 'S']
    
    
    # same_particle_P_and_Sec_MM = False  # Will allow for different particle momentum/sector to be plotted in the same histogram (mixes particles)
    same_particle_P_and_Sec_MM = True   # The particle momentum and sector will always be the same with this option

    ##-------------------------------------------------------------##
    ##=====##=====##     Histogram Options (End)     ##=====##=====##
    ##-------------------------------------------------------------##



    # Use the function ShowBackground? ('yes' or 'no')
    ShowBGq = 'no'
    # ShowBGq = 'yes'



    #################################################################################################
    ##=====##=====##=====##     Choices for Missing Mass Histograms (End)     ##=====##=====##=====##
    #################################################################################################



    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



    ###################################################################################################
    ##=====##=====##=====##     Counting Missing Mass Histograms to be Made     ##=====##=====##=====##
    ###################################################################################################

    # Print_Names_Of_Histos_To_Be_Made_Q = 'yes'
    Print_Names_Of_Histos_To_Be_Made_Q = 'no'



    if(particleList != []):
        print(color.BBLUE, "\nFor the Kinematic histograms...", color.END)
        print("".join(["Particles to be plotted include: ", str(particle_plot_List)]))
        print("".join(["Particles to be used for sector/phi binning include: ", str(particleList)]))

        print("".join(["Corrections included: ", str(correctionList)]))

        print("These Corrections correspond to the following:")
        cor_num = 1
        for cor_names in correctionList:
            print("".join(["   ", str(cor_num), ") ", str(cor_names), " -> '", corNameTitles(cor_names, EVENT_TYPE=event_type, BENDING_TYPE=datatype), "'"]))
            cor_num += 1

        print("".join(["The number of phi bins will include: ", str(binningList)]))
        
        print("".join(["The sectors to be included are: ", str(SecRangeAll), "\n"]))
        
        if(Run_Missing_Mass_Histos != "yes"):
            print(color.BOLD, "Will NOT be running the Missing Mass histograms.", color.END)
        if(Run_Phase_Space != 'yes'):
            print(color.BOLD, "Will NOT be running the phase space histograms.", color.END)
        elif('y' in Skip_Sector_Phase_Space and (len(SecRangeAll) > 1 and 0 in SecRangeAll)):
            print(color.BOLD, "Running the phase space histograms but NOT with separate sectors (only plots showing all sectors will be included).", color.END)
        if(Run_Invariant_Mass_Histos != 'yes'):
            print(color.BOLD, "Will NOT be running histograms with Invariant Mass.", color.END)

        if(str(ShowBGq) != 'no'):
            print("".join(["Using ShowBackground()?: ", ShowBGq]))

    else:
        print(f"{color.BOLD}\nNot running Kinematic Histograms...{color.END}")

    countHisto = 0


    if(Run_Missing_Mass_Histos == "yes"):
        for Cuts in kinematicCuts:
            # if(Cuts in [Calculated_Exclusive_Cuts if("E" not in event_type) else "esec != -2", Calculated_Exclusive_Cuts_v2, Calculated_Exclusive_Cuts_v3, Calculated_Exclusive_Cuts_v4, Calculated_Exclusive_Cuts_v5, Calculated_Exclusive_Cuts_v6, "Both", "Both_2", "All"]):
            #     continue
            for particle in particle_plot_List:
                for sector in SecRangeAll:
                    if(("el" in str(particle)) and (sector > 6)):
                        continue
                    for correction in correctionList:
                        for binning in binningList:
                            for particle_filter in particleList:
                                if(same_particle_P_and_Sec_MM and particle != particle_filter):
                                    continue
                                regionList = regList_Call(binning, particle_filter, 1)
                                for region in regionList:
                                    if(Print_Names_Of_Histos_To_Be_Made_Q == 'yes'):
                                        print("Histo: " + str((correction, sector, "", binning, region, particle, particle_filter, "Cut" if(Cuts != "") else "")))
                                        # print("Histo: " + str((correction, sector, "", binning, region, particle, particle_filter, "Cut" if(Cuts != "") else "")) + "_Vs_Theta")
                                    countHisto += 1
                                    # countHisto += 1
                                    if(ShowBGq == 'yes' and particle == 'el'):
                                        countHisto += 1


    if(Run_Phase_Space == 'yes'):
        for Cuts in kinematicCuts:
            for correction in correctionList:
                for particle in particleList:
                    for shift in shiftList:
                        for local_Q in ["", "local "]:
                            if(shift == "NS" and "local" in local_Q):
                                continue
                            for sector in SecRangeAll:
                                if(("el" in str(particle)) and (sector > 6)):
                                    continue
                                if('y' in Skip_Sector_Phase_Space and sector != 0):
                                    continue
                                else:
                                    countHisto += 1
                                    if("" == shift and "" == local_Q):
                                        countHisto += 1
                                    if('mm0' in correction):
                                        countHisto += 1
                                
    if(Run_Invariant_Mass_Histos == 'yes'): 
        for Cuts in kinematicCuts:
            # if(Cuts in [Calculated_Exclusive_Cuts if("E" in event_type) else "esec != -2", Calculated_Exclusive_Cuts_v2, Calculated_Exclusive_Cuts_v3, Calculated_Exclusive_Cuts_v4, Calculated_Exclusive_Cuts_v5, Calculated_Exclusive_Cuts_v6, "Both", "Both_2", "All"]):
            #     continue
            for particle in particle_plot_List:
                for particle_filter in particleList:
                    if(same_particle_P_and_Sec_MM and particle != particle_filter):
                        continue
                    for correction in correctionList:
                        for sector in SecRangeAll:
                            if(("el" in str(particle)) and (sector > 6)):
                                continue
                            for binning in binningList:
                                regionList = regList_Call(binning, particle_filter, 1)
                                for region in regionList:
                                    countHisto += 1


    print(f"{color.BOLD}\nTotal Kinematic Histograms that will be made:       {color.END}{str(countHisto)}")

    print(f"{color.BOLD}With the first half of the code, the total will be: {color.END}{str(Total_Extra + countHisto)}")

    count_Total = Total_Extra + countHisto


    if(datatype == "Inbending"):
        # This number should be set to the number of histograms expected to be made per minute while running this code (VERY rough estimate - often changes between runs)
        TimeToProcess = 720 if("DP" in event_type and file_location != "All") else 747 if("P0" in event_type) else (121.8 if("Pass" not in str(pass_version)) else 36.75) if("E" in event_type) else 1081 if("Pass" not in str(pass_version)) else 105
        if("MC" in event_Name):
            TimeToProcess = 30
    if(datatype == "Outbending"):
        # This is a VERY rough estimate of the runtime/histogram for when each file is loaded individually (times will vary bases on number of histograms/corrections and the file used)
        TimeToProcess = 1080 if("DP" in event_type and file_location != "All") else 747 if("P0" in event_type) else 110.7 if("E" in event_type) else 98 





    if((count_Total/TimeToProcess) > 1):
        if((count_Total/TimeToProcess) > 60):
            print("".join(["\nEstimated time to run: ", str((round((count_Total/TimeToProcess)/60)) - (round((count_Total/TimeToProcess)/60))%1), " hour(s) and ", str(round(count_Total/TimeToProcess)%60), " mins at a rate of ", str(TimeToProcess), " histograms per minute"]))
        else:
            print("".join(["\nEstimated time to run: ", str(round(count_Total/TimeToProcess)), " mins at a rate of ", str(TimeToProcess), " histograms per minute"]))
    else:
        print("".join(["\nEstimated time to run: ", str(round((count_Total/TimeToProcess)*60)), " seconds at a rate of ", str(TimeToProcess), " histograms per minute"]))


    print("Note: Estimates are based on observations made over time while running this code. Exact times will vary greatly based on choices and file size.\n(Estimates may also need to be updated after significant changes occur)")



    ##################################################################################################
    ##=====##=====##=====##     Counted Missing Mass Histograms to be Made     ##=====##=====##=====##
    ##################################################################################################



    #####################################################################################################################################################
    ##=================================================================================================================================================##
    ##==============##===================##============##         Made Choices for Histograms         ##============##===================##============##
    ##=================================================================================================================================================##
    #####################################################################################################################################################









    sys.stdout.flush()
    #=======================================================================================================================================================================================================================================================#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #=======================================================================================================================================================================================================================================================#










    ################################################################################################################################################################
    ##============================================================================================================================================================##
    ##==========##==========##==========##==========##==========##         Making  Histograms         ##==========##==========##==========##==========##==========##
    ##============================================================================================================================================================##
    ################################################################################################################################################################

    print("".join([color.BBLUE, "\nMaking Histograms now...", color.END]))


    #############################################################################################################
    ##=====##=====##=====##=====##=====##     Making Delta P Histograms     ##=====##=====##=====##=====##=====##
    #############################################################################################################

    if(Delta_P_histo_Q == 'y'):

        Dmom_pip_Histo, Dmom_pel_Histo, Dmom_pro_Histo = {}, {}, {}

        # print("Making the ∆P Histograms...")
        for Cuts in kinematicCuts:

            Cut_rdf, Cut_Title = Cut_Function(rdf, Cuts)
            
            for calc_option in extra_Dp_calc:

                for correction in Delta_P_histo_CorList:

                    correctionNAME = corNameTitles(correction, Form="splitline", EVENT_TYPE=event_type, BENDING_TYPE=datatype)
                    Erdf = Cut_rdf
                    if('pi+' in Delta_P_histo_CompareList and Delta_Pip_histo_Q == 'y'):
                        Erdf    = CorDpp(Erdf, correction, "D_pip", event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                        Erdf_MM = CorDpp(Erdf, correction, "MM",    event_type, MM_type, datatype, "")
                    if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                        # if("L" not in calc_option):
                        if(calc_option in ["D_p", "D_p_No_C"]):
                            Erdf    = CorDpp(Erdf,    correction, "D_pro", event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                            Erdf_MM = CorDpp(Erdf,    correction, "MM", event_type, MM_type, datatype, "")
                            Erdf_MM = CorDpp(Erdf_MM, correction, "D_p_L_pro", event_type, MM_type, datatype, "")
                        elif(calc_option in ["D_p_G", "D_p_gL"]):
                            Erdf    = CorDpp(Erdf,    correction, "".join([calc_option, "_pro"]), event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                            Erdf_MM = CorDpp(Erdf,    correction, "D_p_gL_pro" if(calc_option == "D_p_G") else "D_p_G_pro", event_type, MM_type, datatype, "")
                            Erdf_MM = CorDpp(Erdf_MM, correction, "MM", event_type, MM_type, datatype, "")
                            # Erdf_MM = CorDpp(Erdf_MM, correction, "D_pro", event_type, MM_type, datatype, "")
                            # Erdf_MM = CorDpp(Erdf_MM, correction, "D_p_L_pro", event_type, MM_type, datatype, "")
                        elif("D_p_L" not in calc_option):
                            Erdf    = CorDpp(Erdf,    correction, "".join([calc_option, "_pro"]), event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                            Erdf_MM = CorDpp(Erdf,    correction, "MM", event_type, MM_type, datatype, "")
                            Erdf_MM = CorDpp(Erdf_MM, correction, "D_p_L_pro", event_type, MM_type, datatype, "")
                            Erdf_MM = CorDpp(Erdf_MM, correction, "D_pro", event_type, MM_type, datatype, "")
                        else:
                            Erdf    = CorDpp(Erdf,    correction, "".join([calc_option, "_pro"]), event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                            Erdf_MM = CorDpp(Erdf,    correction, "MM", event_type, MM_type, datatype, "")
                            Erdf_MM = CorDpp(Erdf_MM, correction, "D_pro", event_type, MM_type, datatype, "")
                            # print("Printing the full list of variables (and their object types) in the DataFrame (Erdf)...")
                            # for ii in range(0, len(Erdf.GetColumnNames()), 1):
                            #     print("".join([str((Erdf.GetColumnNames())[ii]), " ( type -> ", Erdf.GetColumnType(Erdf.GetColumnNames()[ii]), " )"]))
                            # print("".join(["\tTotal length= ", str(len(Erdf.GetColumnNames()))]))
                            
                    if('el' in Delta_P_histo_CompareList and Delta_Pel_histo_Q == 'y'):
                        Erdf    = CorDpp(Erdf, correction, "D_pel", event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                        Erdf_MM = CorDpp(Erdf, correction, "MM",    event_type, MM_type, datatype, "")

                    for sec in Delta_Pip_histo_SecList:

                        SecName = "".join(["Pi+" if(event_type in ["SP", "MC"]) else "Pro", " Sector ", str(sec)]) if(sec not in ["all", 0]) else ""

                        for secEL in ExtraElectronSecListFilter:

                            if(secEL not in ["all", 0]):
                                if(sec not in ["all", 0]):
                                    SecName = ''.join(["Pi+" if(event_type in ["SP", "MC"]) else "Pro", " Sector ", str(sec), " and El Sector ", str(secEL)])
                                else:
                                    SecName = ''.join(['El Sector ', str(secEL)])

                            if(SecName == ""):
                                SecName = "All Sectors"

                            for binning in NumPhiBins:

                                reglist = regList_Call(binning, 'pip' if(event_type in ["SP", "MC"]) else 'pro', 2)

                                # Pi+/Pro Regions
                                for regionListName in reglist:
                                    if(len(regionListName) != 1):
                                        region, regionName = regionListName[1], regionListName[0]
                                    else:
                                        region = regionListName
                                        
                                    for binningEL in NumPhiBinsEL:
                                        
                                        if(Combine_el_pip_filters_Q != "yes"):
                                            if(binning == '3' and binningEL != "1"):
                                                continue
                                            if(binningEL == '3' and binning != "1"):
                                                continue
                                            if(sec != 'all' and secEL != 'all'):
                                                continue

                                        reglistEL = regList_Call(binningEL, 'el', 2)

                                        # EL Regions
                                        for regionListNameEL in reglistEL:
                                            if(len(regionListNameEL) != 1):
                                                regionEL, regionNameEL = regionListNameEL[1], regionListNameEL[0]
                                            else:
                                                regionEL = regionListNameEL

                                            if(sec not in ["all", 0]):
                                                sdf    = regFilter(Erdf.Filter(   "".join(["pip" if(event_type in ["SP", "MC"]) else "pro", "sec == ", str(sec)])), binning, sec, region, 'S', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", 'pip' if(event_type in ["SP", "MC"]) else 'pro')
                                                sdf_MM = regFilter(Erdf_MM.Filter("".join(["pip" if(event_type in ["SP", "MC"]) else "pro", "sec == ", str(sec)])), binning, sec, region, 'S', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", 'pip' if(event_type in ["SP", "MC"]) else 'pro')
                                            else:
                                                sdf    = regFilter(Erdf,    binning, sec, region, 'S', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", 'pip' if(event_type in ["SP", "MC"]) else 'pro')
                                                sdf_MM = regFilter(Erdf_MM, binning, sec, region, 'S', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", 'pip' if(event_type in ["SP", "MC"]) else 'pro')

                                            if(secEL not in ["all", 0]):
                                                sdf    = sdf.Filter(   "".join(["esec == ", str(secEL)]))
                                                sdf_MM = sdf_MM.Filter("".join(["esec == ", str(secEL)]))


                                            if(binningEL != '1'):
                                                sdf = regFilter(sdf, binningEL, secEL, regionEL, 'S', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", 'el')
                                                histoName                   = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title)
                                                histoName_3D_Theta_Dp       = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title, "Dp_Theta")
                                                if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                                                    histoName_3D            = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title, "MM_3D")
                                                    histoName_3D_Dp         = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title, "Dp_3D")
                                                    histoName_3D_Theta      = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title, "MM_Theta")
                                                    histoName_3D_Theta_Dp   = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title, "Dp_Theta")
                                                    histoName_3D_Theta_Dp_2 = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title, "Dp_3D_Theta")
                                                    histoName_3D_Electron   = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title, "Dp_Electron")
                                                    histoName_3D_El_Theta   = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title, "Dp_El_Theta")
                                            elif("D_p_L" in calc_option):
                                                histoName                   = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp")
                                                if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                                                    histoName_3D            = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp", "MM_3D")
                                                    histoName_3D_Dp         = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp", "Dp_MM_3D")
                                                    histoName_3D_Theta      = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp", "MM_Theta")
                                                    histoName_3D_Theta_Dp   = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp", "Dp_MM_Theta")
                                                    histoName_3D_Theta_Dp_2 = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp", "Dp_3D_Theta")
                                                    histoName_3D_Electron   = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp", "Dp_Electron")
                                                    histoName_3D_El_Theta   = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp", "Dp_El_Theta")
                                            elif("No_C" in calc_option):
                                                histoName                   = (correction, '', SecName, binning, region, Cut_Title, "No_C")
                                                if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                                                    histoName_3D            = (correction, '', SecName, binning, region, Cut_Title, "No_C", "MM_3D")
                                                    histoName_3D_Dp         = (correction, '', SecName, binning, region, Cut_Title, "No_C", "Dp_3D")
                                                    histoName_3D_Theta      = (correction, '', SecName, binning, region, Cut_Title, "No_C", "MM_Theta")
                                                    histoName_3D_Theta_Dp   = (correction, '', SecName, binning, region, Cut_Title, "No_C", "Dp_Theta")
                                                    histoName_3D_Theta_Dp_2 = (correction, '', SecName, binning, region, Cut_Title, "No_C", "Dp_3D_Theta")
                                                    histoName_3D_Electron   = (correction, '', SecName, binning, region, Cut_Title, "No_C", "Dp_Electron")
                                                    histoName_3D_El_Theta   = (correction, '', SecName, binning, region, Cut_Title, "No_C", "Dp_El_Theta")
                                            elif("S" in calc_option):
                                                histoName                   = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp")
                                                if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                                                    histoName_3D            = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp", "MM_3D")
                                                    histoName_3D_Dp         = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp", "Dp_3D")
                                                    histoName_3D_Theta      = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp", "MM_Theta")
                                                    histoName_3D_Theta_Dp   = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp", "Dp_Theta")
                                                    histoName_3D_Theta_Dp_2 = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp", "Dp_3D_Theta")
                                                    histoName_3D_Electron   = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp", "Dp_Electron")
                                                    histoName_3D_El_Theta   = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp", "Dp_El_Theta")
                                            elif("F" in calc_option):
                                                histoName                   = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp")
                                                if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                                                    histoName_3D            = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp", "MM_3D")
                                                    histoName_3D_Dp         = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp", "Dp_3D")
                                                    histoName_3D_Theta      = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp", "MM_Theta")
                                                    histoName_3D_Theta_Dp   = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp", "Dp_Theta")
                                                    histoName_3D_Theta_Dp_2 = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp", "Dp_3D_Theta")
                                                    histoName_3D_Electron   = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp", "Dp_Electron")
                                                    histoName_3D_El_Theta   = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp", "Dp_El_Theta")
                                            elif(calc_option in ["D_p_G", "D_p_gL"]):
                                                histoName                   = (correction, '', SecName, binning, region, Cut_Title, str(calc_option))
                                                if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                                                    histoName_3D            = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "MM_3D")
                                                    histoName_3D_Dp         = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_3D" if(calc_option in ["D_p_G"]) else "Dp_MM_3D")
                                                    histoName_3D_Theta      = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "MM_Theta")
                                                    histoName_3D_Theta_Dp   = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "".join(["Dp_" if(calc_option in ["D_p_G"]) else "Dp_MM_", "Theta"]))
                                                    histoName_3D_Theta_Dp_2 = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_3D_Theta")
                                                    histoName_3D_Electron   = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_Electron")
                                                    histoName_3D_El_Theta   = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_El_Theta")
                                            elif(str(calc_option) in ["D_p_a", "D_p_b", "D_p_c", "D_p_sqrt"]):
                                                histoName                   = (correction, '', SecName, binning, region, Cut_Title, str(calc_option))
                                                if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                                                    histoName_3D            = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "MM_3D")
                                                    histoName_3D_Dp         = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_3D")
                                                    histoName_3D_Pars       = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_Pars")
                                                    histoName_3D_Theta      = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_Theta")
                                                    histoName_3D_Theta_Dp_2 = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_3D_Theta")
                                                    histoName_3D_Electron   = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_Electron")
                                                    histoName_3D_El_Theta   = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_El_Theta")
                                            else:
                                                histoName                   = (correction, '', SecName, binning, region, Cut_Title)
                                                histoName_3D_Theta_Dp       = (correction, '', SecName, binning, region, Cut_Title, "Dp_Theta")
                                                if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                                                    histoName_3D            = (correction, '', SecName, binning, region, Cut_Title, "MM_3D")
                                                    histoName_3D_Dp         = (correction, '', SecName, binning, region, Cut_Title, "Dp_3D")
                                                    histoName_3D_Theta      = (correction, '', SecName, binning, region, Cut_Title, "MM_Theta")
                                                    histoName_3D_Theta_Dp   = (correction, '', SecName, binning, region, Cut_Title, "Dp_Theta")
                                                    histoName_3D_Theta_Dp_2 = (correction, '', SecName, binning, region, Cut_Title, "Dp_3D_Theta")
                                                    histoName_3D_Electron   = (correction, '', SecName, binning, region, Cut_Title, "Dp_Electron")
                                                    histoName_3D_El_Theta   = (correction, '', SecName, binning, region, Cut_Title, "Dp_El_Theta")


                                            Title_Line_1 = "".join(["(", str(datatype), ") #Delta p_{Particle} vs p_{Particle}"])
                                            if("D_p_L" in calc_option):
                                                Title_Line_1 = "".join(["(", str(datatype), ") Larger #Delta p_{Particle} vs p_{Particle}"])
                                            if("No_C" in calc_option):
                                                Title_Line_1 = "".join(["(", str(datatype), ") #Delta p_{Particle} vs (Uncorrected) p_{Particle}"])
                                            if("S" in calc_option):
                                                Title_Line_1 = "".join(["(", str(datatype), ") #Delta p_{Particle} (Modified Selection) vs p_{Particle}"])
                                            if("F" in calc_option):
                                                Title_Line_1 = "".join(["(", str(datatype), ") #Delta p_{Particle} (Modified Flipped Selection) vs p_{Particle}"])
                                            if(calc_option == "D_p_G"):
                                                Title_Line_1 = "".join(["(", str(datatype), ") Generated #Delta p_{Particle} vs p_{Particle}"])
                                            if(calc_option == "D_p_gL"):
                                                Title_Line_1 = "".join(["(", str(datatype), ") Larger Generated #Delta p_{Particle} vs p_{Particle}"])
                                                
                                            if(pass_version not in ["NA", ""]):
                                                Title_Line_1 = "".join(["#splitline{", str(pass_version), "}{", str(Title_Line_1), "}"])
                                            Title_Line_2     = ((("".join(["Correction: ", str(root_color.Bold), "{", str(correctionNAME), "}"]).replace("Pi+", "#pi^{+}")).replace("Pi-", "#pi^{-}")).replace("Phi", "#phi"))
                                            Title_Line_3     = "".join([str(SecName), "".join([" -- #phi_{", "#pi^{+} " if(event_type in ["SP", "MC"]) else "Pro", "} Bin: ", str(regionName)]) if(str(regionName) != "" and "No Phi Bins" not in regionName) else "", "".join([" -- #phi_{El} Bin: ", str(regionNameEL)]) if(str(regionNameEL) != "" and "No Phi Bins" not in regionNameEL) else ""])
                                            Title_Line_4     = "".join(["Cut Applied: ", str(Cut_Title) if(str(Cut_Title) != "") else "No Additional Cuts"])
                                            Title_Axis       = "".join(["; p_{Particle} (GeV); #Delta p_{Particle} (GeV)"])

                                            Title = "".join(["#splitline{#splitline{", str(Title_Line_1), "}{", str(Title_Line_2), "}}{#splitline{", str(Title_Line_3), "}{", str(Title_Line_4), "}}", Title_Axis])


                                            if('pi+' in Delta_P_histo_CompareList and Delta_Pip_histo_Q == 'y'):
                                                # Need to plot versus energy loss corrected pion
                                                Dmom_pip_Histo[histoName]             = sdf.Histo2D(("".join(["Dmom_pip_Histo",          str(histoName)]),             Title.replace("Particle",       "#pi^{+}"), 200, 0, 10,  NumOfExtendedBins, extendx_min, extendx_max), 'pip'   if("_ELPip" not in str(correction)) else 'pip_EL',   ''.join(['D_pip_', str(correction)]))
                                                Delta_P_histo_Count += 1
                                                Title_Theta          = Title.replace(Title_Line_1, Title_Line_1.replace("vs p_{Particle}", "vs #theta_{Particle}"))
                                                Title_Theta          = Title_Theta.replace(Title_Axis, "; #theta_{Particle} (#circ); #Delta p_{Particle} (GeV)")
                                                Dmom_pip_Histo[histoName_3D_Theta_Dp] = sdf.Histo2D(("".join(["Dmom_pip_vs_Theta_Histo", str(histoName_3D_Theta_Dp)]), Title_Theta.replace("Particle", "#pi^{+}"), 350, 0, 140, NumOfExtendedBins, extendx_min, extendx_max), 'pipth' if("_ELPip" not in str(correction)) else 'pipth_EL', ''.join(['D_pip_', str(correction)]))
                                                Delta_P_histo_Count += 1
                                                # Title_Theta          = Title.replace(Title_Line_1, Title_Line_1.replace("vs p_{Particle}", "vs p_{Particle} vs #theta_{Particle}"))
                                                # Title_Theta          = Title_Theta.replace(Title_Axis, "; p_{Particle} (GeV); #theta_{Particle} (#circ); #Delta p_{Particle} (GeV)")
                                                # Dmom_pip_Histo[histoName_3D_Theta_Dp] = sdf.Histo3D(("".join(["Dmom_pip_vs_Theta_Histo", str(histoName_3D_Theta_Dp)]), Title_Theta.replace("Particle", "#pi^{+}"), 200, 0, 10, 350, 0, 140, NumOfExtendedBins, extendx_min, extendx_max), 'pip', 'pipth', ''.join(['D_pip_', str(correction)]))
                                                # Delta_P_histo_Count += 1


                                            if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                                                Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), Title.replace("Particle", "Pro"), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pro' if(("_NoELC" in correction) or ("No_C" in calc_option) or ("MC" in event_Name)) else "pro_cor", ''.join(['D_pro_' if(str(calc_option) in ["D_p", "D_p_No_C"]) else ''.join([str(calc_option), '_pro_']), str(correction)]))
                                                Delta_P_histo_Count += 1
                                                
                                                
                                                Title_3D_Pro = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "#Delta p_{Particle} vs Missing Mass^{2} vs p_{Particle}")).replace(Title_Axis, "; p_{Particle} (GeV); #Delta p_{Particle} (GeV); MM^{2} (GeV^{2})")).replace("Particle", "Pro")
                                                if(str(calc_option) in ["D_p_a", "D_p_b", "D_p_c", "D_p_sqrt"]):
                                                    Title_3D_Pro = Title_3D_Pro.replace("#Delta p_{Pro}", str(calc_option))
                                                x_variable = 'pro' if(('_NoELC' in str(correction)) or ('No_C' in str(calc_option)) or ("MC" in event_Name)) else 'pro_cor'
                                                y_variable = ''.join(['D_pro_' if(str(calc_option) in ["D_p", "D_p_No_C"]) else ''.join([str(calc_option), '_pro_']), str(correction)])
                                                z_variable = str(correction)
                                                dp_min     = -0.5 if("MC" not in event_Name) else -0.05
                                                dp_max     =  0.5 if("MC" not in event_Name) else  0.05
                                                if(str(calc_option) in ["D_p_a", "D_p_b", "D_p_c", "D_p_sqrt"]):
                                                    dp_min = -15 if(str(calc_option) in ["D_p_a", "D_p_sqrt"]) else 0 if("D_p_b" in str(calc_option)) else -70
                                                    dp_max =  70 if("D_p_b" in str(calc_option)) else 35 if(str(calc_option) in "D_p_sqrt") else 0
                                                dp_bin     = 200 if(str(calc_option) not in "D_p_sqrt") else 400
                                                dp_min    += -0.5*((dp_max - dp_max)/dp_bin)
                                                dp_max    +=  0.5*((dp_max - dp_max)/dp_bin)
                                                dp_bin    += 1
                                                
                                                MM_min, MM_max = -0.1, 0.3
                                                if("(GEN)" in event_Name):
                                                    MM_min, MM_max = -0.05, 0.05
                                                # z_variable = "proth"
                                                Dmom_pro_Histo[histoName_3D] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D)]), Title_3D_Pro, 100, 0, 10, dp_bin, dp_min, dp_max, 200, MM_min, MM_max), x_variable, y_variable, z_variable)
                                                Delta_P_histo_Count += 1
                                                
                                                Title_3D_Pro_EL       = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "#Delta p_{Pro} vs #theta_{Pro} vs #theta_{El}")).replace(str(Title_Axis), "; #theta_{Pro} (#circ); #Delta p_{Pro} (GeV); #theta_{El} (#circ)"))
                                                Title_3D_Pro_EL_Theta = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "#Delta p_{Pro} vs #theta_{Pro} vs #theta_{El}")).replace(str(Title_Axis), "; #theta_{Pro} (#circ); #Delta p_{Pro} (GeV); #theta_{El} (#circ)"))
                                                Dmom_pro_Histo[histoName_3D_Electron] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_Electron)]), Title_3D_Pro_EL,       100, 0, 10,  dp_bin, dp_bin, dp_min, 100, 0, 10),  "pro",   str(y_variable), "el")
                                                Dmom_pro_Histo[histoName_3D_El_Theta] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_El_Theta)]), Title_3D_Pro_EL_Theta, 100, 0, 100, dp_bin, dp_bin, dp_min, 100, 0, 100), "proth", str(y_variable), "elth")
                                                Delta_P_histo_Count += 2
                                                
                                                if(str(calc_option) in ["D_p", "D_p_L", "D_p_G", "D_p_gL"]):
                                                    # print("".join([color.BBLUE, "\n\ncalc_option = ", str(calc_option), "\n\n", color.END]))
                                                    Title_3D_Pro_Dp = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "(Both) #Delta p_{Particle} vs p_{Particle}")).replace(Title_Axis, "; p_{Particle} (GeV); (Best) #Delta p_{Particle} (GeV); (Secondary) #Delta p_{Particle} (GeV)")).replace("Particle", "Pro")
                                                    if(calc_option in ["D_p_G", "D_p_gL"]):
                                                        Title_3D_Pro_Dp = str(Title_3D_Pro_Dp).replace("(Both)", "(Both - Generated)")
                                                    x_variable = 'pro' if(('_NoELC' in str(correction)) or ('No_C' in str(calc_option)) or ("MC" in event_Name)) else 'pro_cor'
                                                    x_bins, x_min, x_max = 100, 0, 10
                                                    
                                                    if(str(calc_option) in ["D_p_L", "D_p_gL"]):
                                                        x_variable = str(correction)
                                                        Title_3D_Pro_Dp = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "(Both) #Delta p_{Particle} vs MM^{2}")).replace(Title_Axis, "; MM^{2} (GeV^{2}); (Best) #Delta p_{Particle} (GeV); (Secondary) #Delta p_{Particle} (GeV)")).replace("Particle", "Pro")
                                                        x_bins, x_min, x_max = 200, MM_min, MM_max
                                                    y_variable = ''.join(['D_pro_', str(correction)])     if(calc_option not in ["D_p_G", "D_p_gL"]) else ''.join(['D_p_G_pro_',  str(correction)])
                                                    z_variable = ''.join(['D_p_L_pro_', str(correction)]) if(calc_option not in ["D_p_G", "D_p_gL"]) else ''.join(['D_p_gL_pro_', str(correction)])
                                                    
                                                    Dmom_pro_Histo[histoName_3D_Dp]         = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_Dp)]),             str(Title_3D_Pro_Dp), int(x_bins), x_min, x_max, dp_bin, dp_min, dp_max, 201, -0.15025, 0.15025), x_variable, y_variable, z_variable)
                                                    Dmom_pro_Histo[histoName_3D_Theta_Dp_2] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_Theta_Dp_2)]), str(str((Title_3D_Pro_Dp.replace("MM^{2} (GeV^{2})", "#theta_{Pro} (#circ)")).replace("p_{Pro} (GeV); (Best)", "#theta_{Pro} (#circ); (Best)")).replace("vs p_{Pro}", "vs #theta_{Pro}")).replace("MM^{2}", "#theta_{Pro}"), 100, 0, 100, dp_bin, dp_min, dp_max, 201, -0.15025, 0.15025), "proth", y_variable, z_variable)
                                                    Delta_P_histo_Count += 2

                                                if(str(calc_option) not in ["D_p_a", "D_p_b", "D_p_c", "D_p_sqrt"]):
                                                    Title_3D_Pro_Theta    = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "#Delta p_{Particle} vs #theta_{Particle} vs p_{Particle}")).replace(Title_Axis, "; p_{Particle} (GeV); #Delta p_{Particle} (GeV); #theta_{Particle} (#circ)")).replace("Particle", "Pro")
                                                    Title_3D_Pro_Theta_MM = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "Missing Mass^{2} vs #theta_{Particle} vs p_{Particle}")).replace(Title_Axis,    "; p_{Particle} (GeV); MM^{2} (GeV^{2}); #theta_{Particle} (#circ)")).replace("Particle", "Pro")
                                                    if(str(calc_option) in ["D_p_a", "D_p_b", "D_p_c", "D_p_sqrt"]):
                                                        Title_3D_Pro_Theta    = Title_3D_Pro_Theta.replace("#Delta p_{Pro}",    str(calc_option))
                                                        Title_3D_Pro_Theta_MM = Title_3D_Pro_Theta_MM.replace("#Delta p_{Pro}", str(calc_option))
                                                    y_variable = ''.join(['D_pro_' if(str(calc_option) in ["D_p", "D_p_No_C"]) else ''.join([str(calc_option), '_pro_']), str(correction)])
                                                    Dmom_pro_Histo[histoName_3D_Theta_Dp] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_Theta_Dp)]), Title_3D_Pro_Theta, 100, 0, 10, dp_bin, dp_min, dp_max, 100, 0, 100), "pro", str(y_variable), "proth")
                                                    Dmom_pro_Histo[histoName_3D_Theta]    = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_Theta)]), Title_3D_Pro_Theta_MM, 100, 0, 10, dp_bin, MM_min, MM_max, 100, 0, 100), "pro", str(correction), "proth")
                                                    Delta_P_histo_Count += 2
                                                else:
                                                    Title_3D_Pro_Dp       = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "".join([str(calc_option), " vs #Delta p_{Particle} vs p_{Particle}"]))).replace(Title_Axis, "".join(["; p_{Particle} (GeV); ", str(calc_option), "; #Delta p_{Particle} (GeV)"]))).replace("Particle",  "Pro")
                                                    Title_3D_Pro_Theta    = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "".join([str(calc_option), " vs #theta_{Particle} vs p_{Particle}"])).replace(Title_Axis,    "".join(["; p_{Particle} (GeV); ", str(calc_option), "; #theta_{Particle} (#circ)"])))).replace("Particle", "Pro")
                                                    # pars_variable = ''.join(['D_pro_' if(str(calc_option) in ["D_p", "D_p_No_C"]) else ''.join([str(calc_option), '_pro_']), str(correction)])
                                                    pars_variable = ''.join([str(calc_option), '_pro_', str(correction)])
                                                    dp_variable   = ''.join(['D_pro_', str(correction)])
                                                    
                                                    Dmom_pro_Histo[histoName_3D_Dp]    = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_Dp)]),    Title_3D_Pro_Dp,    100, 0, 10, dp_bin, dp_min, dp_max, 201, -0.05025, 0.05025), "pro", str(pars_variable), str(dp_variable))
                                                    Dmom_pro_Histo[histoName_3D_Theta] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_Theta)]), Title_3D_Pro_Theta, 100, 0, 10, dp_bin, dp_min, dp_max, 100,  0,       100),     "pro", str(pars_variable), "proth")
                                                    Delta_P_histo_Count += 2


                                            if('el' in Delta_P_histo_CompareList and Delta_Pel_histo_Q == 'y'):
                                                Dmom_pel_Histo[histoName]             = sdf.Histo2D(("".join(["Dmom_pel_Histo", str(histoName)]),             Title.replace("Particle",       "El"), 400, 0.5, 10.5, NumOfExtendedBins, extendx_min, extendx_max), 'el',   ''.join(['D_pel_', str(correction)]))
                                                Delta_P_histo_Count += 1
#                                                 Title_Theta          = Title.replace(Title_Line_1, Title_Line_1.replace("vs p_{Particle}", "vs #theta_{Particle}"))
#                                                 Title_Theta          = Title_Theta.replace(Title_Axis, "; #theta_{Particle} (#circ); #Delta p_{Particle} (GeV)")
#                                                 Dmom_pel_Histo[histoName_3D_Theta_Dp] = sdf.Histo2D(("".join(["Dmom_pel_Histo", str(histoName_3D_Theta_Dp)]), Title_Theta.replace("Particle", "El"), 350, 0, 140,    NumOfExtendedBins, extendx_min, extendx_max), 'elth', ''.join(['D_pel_', str(correction)]))
#                                                 Delta_P_histo_Count += 1
                                                # Title_Theta          = Title.replace(Title_Line_1, Title_Line_1.replace("vs p_{Particle}", "vs p_{Particle} vs #theta_{Particle}"))
                                                # Title_Theta          = Title_Theta.replace(Title_Axis, "; p_{Particle} (GeV); #theta_{Particle} (#circ); #Delta p_{Particle} (GeV)")
                                                # Dmom_pel_Histo[histoName_3D_Theta_Dp] = sdf.Histo3D(("".join(["Dmom_pel_Histo", str(histoName_3D_Theta_Dp)]), Title_Theta.replace("Particle", "El"), 400, 0.5, 10.5, 350, 0, 140, NumOfExtendedBins, extendx_min, extendx_max), 'el', 'elth', ''.join(['D_pel_', str(correction)]))
                                                # Delta_P_histo_Count += 1


        print("".join(["Number of ∆P Histograms made: ", str(Delta_P_histo_Count)]))


    ###########################################################################################################
    ##=====##=====##=====##=====##=====##     Made Delta P Histograms     ##=====##=====##=====##=====##=====##
    ###########################################################################################################





    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




    ############################################################################################################################################
    ##=====##=====##=====##=====##=====##     Making Delta Theta Histograms (Elastic Corrections Only)     ##=====##=====##=====##=====##=====##
    ############################################################################################################################################

    if(event_type == "ES"):

        Dmom_Angle_Histo = {}

        print("Making the ∆Theta/∆Phi Histograms...")
        
        for Cuts in kinematicCuts:
            if(Cuts in ["Both_3", "All"]):
                continue
                # Do not plot variables with cuts applied to them that are based on themselves
            
            Cut_rdf, Cut_Title = Cut_Function(rdf, Cuts)
        
            # for Calc_Version in ["D_Angle_V1", "D_Angle_V2", "D_Angle_V3", "D_Angle_V4"]:
            for Calc_Version in ["D_Angle_V1", "D_Angle_V3"]:
                if((Cuts in [CutChoice, "Both"] and "V3" in Calc_Version) or (Cuts in [CutChoice_2, "Both_2"] and "V3" not in Calc_Version)):
                    continue
                    # Do not plot variables with cuts applied to them that are based on themselves
                for correction in Delta_P_histo_CorList:

                    correctionNAME = corNameTitles(correction, Form="splitline", EVENT_TYPE=event_type, BENDING_TYPE=datatype)
                    
                    Erdf = Cut_rdf
                    Erdf = CorDpp(Erdf, correction, Calc_Version, event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                    
                    for sec in ExtraElectronSecListFilter:
                        if(sec in ["all", "All"]):
                            sec = 0
                        SecName = "".join(["El Sector ", str(sec)]) if(sec not in [0, "all", "All"]) else "All Sectors"

                        if(sec != 0):
                            sdf = regFilter(Erdf.Filter("".join(["esec == ", str(sec)])), '1', sec, 'regall', 'S', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", 'el')
                        else:
                            sdf = regFilter(Erdf, '1', sec, 'regall', 'S', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", 'el')
                            
                        histoName = (correction, '', SecName, binning, region, Cut_Title, str(Calc_Version))

                        Min_Delta_Angle = -50 if("V3" not in Calc_Version) else 155
                        Max_Delta_Angle =  50 if("V3" not in Calc_Version) else 205

                        Title_Line_1 = "".join(["(", str(datatype), ") #Delta ", "".join(["#theta_{Pro} (Version ", "1" if("V1" in Calc_Version) else "2" if("V2" in Calc_Version) else "3", ")"]) if("V3" not in Calc_Version) else "#phi_{|El-Pro|}", " vs p_{El} "])
                        Title_Line_2 = ((("".join(["Correction: ", str(root_color.Bold), "{", correctionNAME, "}"]).replace("Pi+", "#pi^{+}")).replace("Pi-", "#pi^{-}")).replace("Phi", "#phi"))
                        Title_Line_3 = "".join([SecName, "".join([" --- ", regionName]) if(regionName != "" and "No Phi Bins" not in regionName) else ""])
                        Title_Line_4 = "".join(["Cut Applied: ", Cut_Title if(Cut_Title != "") else "No Additional Cuts"])
                        Title_Axis = "".join(["; p_{El} (GeV); #Delta", "#theta_{Pro}" if("V3" not in Calc_Version) else "#phi_{|El-Pro|}"])

                        Dmom_Angle_Histo_Title = "".join(["#splitline{#splitline{", str(root_color.Bold), "{", str(Title_Line_1), "}}{", str(Title_Line_2), "}}{#splitline{", str(Title_Line_3), "}{", str(Title_Line_4), "}}", Title_Axis])
                        
                        Dmom_Angle_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_Angle_Histo", str(histoName)]), str(Dmom_Angle_Histo_Title), 200, 0, 10, 500, Min_Delta_Angle, Max_Delta_Angle), 'el', ''.join([str(Calc_Version), "_", str(correction)]))
                        
                        Delta_P_histo_Count += 1


        print("".join(["Number of ∆P Histograms made (with ∆Theta/∆Phi): ", str(Delta_P_histo_Count)]))


    ###########################################################################################################
    ##=====##=====##=====##=====##=====##     Made Delta P Histograms     ##=====##=====##=====##=====##=====##
    ###########################################################################################################





    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#





    
    ##################################################################################################################
    ##=====##=====##=====##=====##=====##     Making Missing Mass Histograms     ##=====##=====##=====##=====##=====##
    ##################################################################################################################


    hmmCPARTall = {}
    count = 0
    
    if(Run_Missing_Mass_Histos == "yes"):
        for Cuts in kinematicCuts:
            # if(Cuts in [Calculated_Exclusive_Cuts if("E" not in event_type) else "esec != -2", Calculated_Exclusive_Cuts_v2, Calculated_Exclusive_Cuts_v3, Calculated_Exclusive_Cuts_v4, Calculated_Exclusive_Cuts_v5, Calculated_Exclusive_Cuts_v6, "Both", "Both_2", "All"]):
            #     continue
            #     # Do not plot variables with cuts applied to them that are based on themselves
            Cut_rdf, Cut_Title = Cut_Function(rdf, Cuts)
            for particle in particle_plot_List:
                for sector in SecRangeAll:
                    if(("el" in str(particle)) and (sector > 6)):
                        continue
                    for correction in correctionList:
                        sdf1 = CorDpp(Cut_rdf, correction, "MM", event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")

                        for binning in binningList:
                            for particle_filter in particleList:
                                secfilter = 'esec' if(particle_filter == 'el') else 'pipsec' if(particle_filter == 'pip') else 'pimsec' if(particle_filter == 'pim') else 'prosec' if(particle_filter == 'pro') else 'error'
                                
                                if(same_particle_P_and_Sec_MM and particle != particle_filter):
                                    continue

                                if(secfilter == "error"):
                                    print("\nERROR IN SECTOR DEFINITION (Missing Mass)\n")

                                if(sector != 0):
                                    sdf = sdf1.Filter("".join([secfilter, ' == ', str(sector)]))
                                else:
                                    sdf = sdf1

                                regionList = regList_Call(binning, particle_filter, 1)

                                for region in regionList:

                                    name = (correction, sector, '', binning, region, particle, particle_filter, Cut_Title)

                                    hmmCPARTall[name]               = Missing_Mass_Histo_Maker(regFilter(sdf, binning, sector, region, '', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", particle_filter), correction, sector, region, '', binning, particle, particle_filter, Cut_Title)
                                    count += 1
                                    # hmmCPARTall[f"{name}_Vs_Theta"] = Missing_Mass_Histo_Maker(regFilter(sdf, binning, sector, region, '', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", particle_filter), correction, sector, region, '', binning, particle, particle_filter, Cut_Title, Theta_Plot=True)
                                    # count += 1


    print("".join(["Total Missing Mass Histograms made: ", str(count)]))

    ################################################################################################################
    ##=====##=====##=====##=====##=====##     Made Missing Mass Histograms     ##=====##=====##=====##=====##=====##
    ################################################################################################################





    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#





    ####################################################################################################################
    ##=====##=====##=====##=====##=====##     Making Invariant Mass Histograms     ##=====##=====##=====##=====##=====##
    ####################################################################################################################


    HWC_Histo_All = {}
    count_WM = 0
    
    if(Run_Invariant_Mass_Histos == 'yes'):
        for Cuts in kinematicCuts:
#             if(Cuts in [Calculated_Exclusive_Cuts if("E" in event_type) else "esec != -2", Calculated_Exclusive_Cuts_v2, Calculated_Exclusive_Cuts_v3, Calculated_Exclusive_Cuts_v4, Calculated_Exclusive_Cuts_v5, Calculated_Exclusive_Cuts_v6, "Both", "Both_2", "All"]):
#                 continue
#                 # Do not plot variables with cuts applied to them that are based on themselves
            Cut_rdf, Cut_Title = Cut_Function(rdf, Cuts)
            for correction in correctionList:
                sdf1 = CorDpp(Cut_rdf, correction, "WM", event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                for sector in SecRangeAll:
                    for particle in particle_plot_List:
                        if(("el" in str(particle)) and (sector > 6)):
                            continue
                        for particle_filter in particleList:

                            if(same_particle_P_and_Sec_MM and particle != particle_filter):
                                continue
                                
                            secfilter = 'esec' if(particle_filter == 'el') else "pipsec" if(particle_filter == 'pip') else 'pimsec' if(particle_filter == 'pim') else "prosec" if(particle_filter == 'pro') else 'error'
                            if(secfilter == "error"):
                                print("\nERROR IN SECTOR DEFINITION (Invariant Mass)\n")
                            if(sector != 0):
                                sdf = sdf1.Filter("".join([secfilter, ' == ', str(sector)]))
                            else:
                                sdf = sdf1
                            for binning in binningList:
                                regionList = regList_Call(binning, particle_filter, 1)
                                for region in regionList:
                                    name = (correction, sector, binning, region, particle, particle_filter, Cut_Title)
                                    HWC_Histo_All[name] = histoMaker_HWC_Histo_All(regFilter(sdf, binning, sector, region, "", Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", particle_filter), correction, sector, region, binning, particle, particle_filter, Cut_Title)

                                    count += 1
                                    count_WM += 1



        print("".join(["Total Invariant Mass Histograms made: ", str(count_WM)]))

    ##################################################################################################################
    ##=====##=====##=====##=====##=====##     Made Invariant Mass Histograms     ##=====##=====##=====##=====##=====##
    ##################################################################################################################





    ###############################################################################################################
    ##=====##=====##=====##=====##     Making Histograms for showing Phase Space     ##=====##=====##=====##=====##
    ###############################################################################################################


    def shiftTitle(SHIFT):
        output = ''
        if(SHIFT == ''):
            output = ' - No Shift'
        if(SHIFT == 'Se1'):
            output = ' - Electron Shift'
        if(SHIFT == 'Se2'):
            output = ' - Electron Shift 2'
        if(SHIFT == 'Spip1'):
            output = ' - #pi+ Shift'
        if(SHIFT == 'Se1Spip1'):
            output = ' - Electron Shift and #pi+ Shift'
        if(SHIFT == 'Se2Spip1'):
            output = ' - Electron Shift 2 and #pi+ Shift'
        if(SHIFT == 'S'):
            output = ' - Shifted'
        if(SHIFT == 'NS'):
            output = ' - No Shift (Not Local #phi)'

        return output


    if(Run_Phase_Space == 'yes'):
        count = 0

        Histo_P_v_Th, Histo_P_v_Phi, Histo_Th_v_Phi = {}, {}, {}
        
        for Cuts in kinematicCuts:
            Cut_rdf, Cut_Title = Cut_Function(rdf, Cuts)
            for correction in correctionList:
                correctionNAME = corNameTitles(correction, Form="splitline", EVENT_TYPE=event_type, BENDING_TYPE=datatype)
                for particle in particleList:
                    for shift in shiftList:
                        for local_Q in ["", "local "]:
                            if(shift == "NS" and "local" in local_Q):
                                continue
                            for sector in SecRangeAll:
                                if(("el" in str(particle)) and (sector > 6)):
                                    continue
                                if('y' in Skip_Sector_Phase_Space and sector != 0):
                                    continue
                                    
                                ref = (correction, sector, particle, Cut_Title, str(local_Q).replace(" ", ""), shift)

                                particle_title = (((particle.replace("el", "El")).replace("pip", "#pi+")).replace("pim", "#pi-")).replace("pro", "Pro")
                                sector_title = "(All Sectors)" if (sector == 0) else "".join(["(", particle_title, " Sector ", str(sector),")"])
                                
                                
                                Title_Mom_The_Line_1 = "".join(["(", str(datatype), ") #theta_{", str(particle_title), "} vs p_{",                      str(particle_title), "}"])
                                Title_Mom_Phi_Line_1 = "".join(["(", str(datatype), ") p_{",      str(particle_title), "} vs #phi_{",                   str(particle_title), "}", str(shiftTitle(shift))])
                                Title_The_Phi_Line_1 = "".join(["(", str(datatype), ") #theta_{", str(particle_title), "} vs ", str(local_Q), "#phi_{", str(particle_title), "}", str(shiftTitle(shift))])
                
                                if(pass_version not in ["NA", ""]):
                                    Title_Mom_The_Line_1 = "".join(["#splitline{", str(pass_version), "}{", str(Title_Mom_The_Line_1), "}"])
                                    Title_Mom_Phi_Line_1 = "".join(["#splitline{", str(pass_version), "}{", str(Title_Mom_Phi_Line_1), "}"])
                                    Title_The_Phi_Line_1 = "".join(["#splitline{", str(pass_version), "}{", str(Title_The_Phi_Line_1), "}"])
                                
                                Title_Line_2 = ((("".join(["Correction: ", str(root_color.Bold), "{", str(correctionNAME), "}"]).replace("Pi+", "#pi^{+}")).replace("Pi-", "#pi^{-}")).replace("Phi", "#phi"))
                                Title_Line_3 = "".join(["Cut Applied: ",   str(Cut_Title) if(str(Cut_Title) != "") else "No Additional Cuts"])
                                
                                Title_Mom_The_Axis = "".join(["; p_{",    str(particle_title), "} (GeV); #theta_{",   str(particle_title), "} (#circ)"])
                                Title_Mom_Phi_Axis = "".join(["; p_{",    str(particle_title), "} (GeV); #phi_{",     str(particle_title), "} (#circ)"])
                                Title_The_Phi_Axis = "".join(["; #phi_{", str(particle_title), "} (#circ); #theta_{", str(particle_title), "} (#circ)"])

                                Title_Mom_The = "".join(["#splitline{#splitline{", str(Title_Mom_The_Line_1), " ", str(sector_title), "}{", str(Title_Line_2), "}}{", str(Title_Line_3), "}", str(Title_Mom_The_Axis)])
                                Title_Mom_Phi = "".join(["#splitline{#splitline{", str(Title_Mom_Phi_Line_1), " ", str(sector_title), "}{", str(Title_Line_2), "}}{", str(Title_Line_3), "}", str(Title_Mom_Phi_Axis)])
                                Title_The_Phi = "".join(["#splitline{#splitline{", str(Title_The_Phi_Line_1), " ", str(sector_title), "}{", str(Title_Line_2), "}}{", str(Title_Line_3), "}", str(Title_The_Phi_Axis)])

                                Histo_Mom_The_ref_title = "".join(["Histo_P_v_Th_",   str(ref)])
                                Histo_Mom_Phi_ref_title = "".join(["Histo_P_v_Phi_",  str(ref)])
                                Histo_The_Phi_ref_title = "".join(["Histo_Th_v_Phi_", str(ref)])

                                if(sector == 0):
                                    sdf = CorDpp(rdf, correction, "".join(["Mom_", particle]), event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                                else:
                                    sdf = CorDpp(rdf.Filter("".join([particle.replace("l", ""), "sec", " == ", str(sector)])), correction, "".join(["Mom_", particle]), event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")

                                # Histo_P_v_Phi[ref]      = sdf.Histo2D((Histo_Mom_Phi_ref_title, Title_Mom_Phi, 110,  0,   11,  720, -260, 460), "".join([particle, "_", correction]),                        "".join([local_Q.replace(" ", ""), particle, "Phi", shift]))
                                Histo_P_v_Phi[ref]      = sdf.Histo2D((Histo_Mom_Phi_ref_title, Title_Mom_Phi, 110,  0,   11, 1440, -260, 460), "".join([particle, "_", correction]),                        "".join([local_Q.replace(" ", ""), particle, "Phi", shift]))
                                count += 1
                                
                                if("" == shift and "" == local_Q):
                                    Histo_P_v_Th[ref]   = sdf.Histo2D((Histo_Mom_The_ref_title, Title_Mom_The, 110,  0,   11,  560,  0,   140), "".join([particle, "_", correction]),                        "".join([particle, "th"]))
                                    count += 1
                                if('mm0' in correction):
                                    Histo_Th_v_Phi[ref] = sdf.Histo2D((Histo_The_Phi_ref_title, Title_The_Phi, 720, -260, 460, 560,  0,   140), "".join([local_Q.replace(" ", ""), particle, "Phi", shift]), "".join([particle, "th"]))
                                    count += 1


        print("".join(["Total Phase Space histograms made (without Missing Mass) = ", str(count)]))


    ###########################################################################################################
    ##=====##=====##=====##=====##          Made Phase Space Histograms          ##=====##=====##=====##=====##
    ###########################################################################################################



    ##############################################################################################################################################################
    ##==========================================================================================================================================================##
    ##==========##==========##==========##==========##==========##         Made  Histograms         ##==========##==========##==========##==========##==========##
    ##==========================================================================================================================================================##
    ##############################################################################################################################################################










    #=======================================================================================================================================================================================================================================================#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #=======================================================================================================================================================================================================================================================#








    ################################################################################################################################################################
    ##============================================================================================================================================================##
    ##==========##==========##==========##==========##==========##         Saving  Histograms         ##==========##==========##==========##==========##==========##
    ##============================================================================================================================================================##
    ################################################################################################################################################################        
    # if(SaveResultsQ == 'yes' or CheckDataFrameQ == "y"):


    def safe_write(histogram, name):
        try:
            if(histogram):
                histogram.Write()
            else:
                print(f"Warning: Histogram {name} is None and was not written.")
        except Exception as e:
            print(f"Error writing histogram {name}: {e}")
            print(f"{color.Error}TRACEBACK: \n{color.END_B}{str(traceback.format_exc())}{color.END}\n")
    
    Full_Crash_Check = "n"
    # Full_Crash_Check = "y"
    

    if(SaveResultsQ == 'yes'):
        print(f"\n{color.BOLD}Saving Results Now...{color.END}")
        RoutputFile = ROOT.TFile(str(OutputFileName), 'recreate')
    elif(CheckDataFrameQ == "y"):
        print(f"\n{color.BOLD}Printing the Results to be Saved Now...{color.END}")
    else:
        print(f"\n{color.BOLD}Printing the Final Count...{color.END}")

    countSaved = 0


    # # # # # # # # # # # # # # # # # # # #    For the ∆P Histograms    # # # # # # # # # # # # # # # # # # # # 

    if(Delta_P_histo_Q == 'y'):

        if('pi+' in Delta_P_histo_CompareList and Delta_Pip_histo_Q == 'y'):
            for saving_Dp_pip_name in Dmom_pip_Histo:
                if(SaveResultsQ == 'yes'):
                    # Dmom_pip_Histo[saving_Dp_pip_name].Write()
                    safe_write(Dmom_pip_Histo[saving_Dp_pip_name], f"Dmom_pip_Histo[{saving_Dp_pip_name}]")
                elif(CheckDataFrameQ == "y"):
                    print("".join(["Dmom_pip_Histo[", str(saving_Dp_pip_name), "]"]))
                elif(Full_Crash_Check == "y"):
                    print("".join(["type = ", str(type(Dmom_pip_Histo[saving_Dp_pip_name]))]))
                countSaved += 1
                # print("".join([str(countSaved), ") Dmom_pip_Histo[", str(saving_Dp_pip_name), "]"]))

        if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
            for saving_Dp_pro_name in Dmom_pro_Histo:
                if(SaveResultsQ == 'yes'):
                    # Dmom_pro_Histo[saving_Dp_pro_name].Write()
                    safe_write(Dmom_pro_Histo[saving_Dp_pro_name], f"Dmom_pro_Histo[{saving_Dp_pro_name}]")
                elif(CheckDataFrameQ == "y"):
                    print("".join(["Dmom_pro_Histo[", str(saving_Dp_pro_name), "]"]))
                elif(Full_Crash_Check == "y"):
                    print("".join(["type = ", str(type(Dmom_pro_Histo[saving_Dp_pro_name]))]))
                countSaved += 1

        if('el' in Delta_P_histo_CompareList and Delta_Pel_histo_Q == 'y'):
            for saving_Dp_pel_name in Dmom_pel_Histo:
                if(SaveResultsQ == 'yes'):
                    # Dmom_pel_Histo[saving_Dp_pel_name].Write()
                    safe_write(Dmom_pel_Histo[saving_Dp_pel_name], f"Dmom_pel_Histo[{saving_Dp_pel_name}]")
                elif(CheckDataFrameQ == "y"):
                    print("".join(["Dmom_pel_Histo[", str(saving_Dp_pel_name), "]"]))
                elif(Full_Crash_Check == "y"):
                    print("".join(["type = ", str(type(Dmom_pel_Histo[saving_Dp_pel_name]))]))
                countSaved += 1
                # print("".join([str(countSaved), ") Dmom_pel_Histo[", str(saving_Dp_pel_name), "]"]))

                
                
                
    # # # # # # # # # # # # # # # # # # # #    For the ∆Angle Histograms    # # # # # # # # # # # # # # # # # # # # 
                
        
        
    if(event_type == "ES"):
        for saving_DAngle_name in Dmom_Angle_Histo:
            if(SaveResultsQ == 'yes'):
                # Dmom_Angle_Histo[saving_DAngle_name].Write()
                safe_write(Dmom_Angle_Histo[saving_DAngle_name], f"Dmom_Angle_Histo[{saving_DAngle_name}]")
            elif(CheckDataFrameQ == "y"):
                print("".join(["Dmom_Angle_Histo[", str(saving_DAngle_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print("".join(["type = ", str(type(Dmom_Angle_Histo[saving_DAngle_name]))]))
            countSaved += 1
            
            
            

    # # # # # # # # # # # # # # # # # # Second half of code (Missing Mass Histograms) # # # # # # # # # # # # # # # # # #

    if(Run_Missing_Mass_Histos == "yes"):
        for saving_MM_name in hmmCPARTall:
            if(SaveResultsQ == 'yes'):
                # hmmCPARTall[saving_MM_name].Write()
                safe_write(hmmCPARTall[saving_MM_name], f"hmmCPARTall[{saving_MM_name}]")
            elif(CheckDataFrameQ == "y"):
                print("".join(["hmmCPARTall[", str(saving_MM_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print("".join(["type = ", str(type(hmmCPARTall[saving_MM_name]))]))
            countSaved += 1
            # print("".join([str(countSaved), ") hmmCPARTall[", str(saving_MM_name), "]"]))


    # # # # # # # # # # # # # # #   Other Phase Space Histograms (without Missing Mass)   # # # # # # # # # # # # # # #

    if(Run_Phase_Space == 'yes'):
        for saving_th_name in Histo_P_v_Th:
            if(SaveResultsQ == 'yes'):
                # Histo_P_v_Th[saving_th_name].Write()
                safe_write(Histo_P_v_Th[saving_th_name], f"Histo_P_v_Th[{saving_th_name}]")
            elif(CheckDataFrameQ == "y"):
                print("".join(["Histo_P_v_Th[", str(saving_th_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print("".join(["type = ", str(type(Histo_P_v_Th[saving_th_name]))]))
            countSaved += 1

        for saving_Phi_name in Histo_P_v_Phi:
            if(SaveResultsQ == 'yes'):
                # Histo_P_v_Phi[saving_Phi_name].Write()
                safe_write(Histo_P_v_Phi[saving_Phi_name], f"Histo_P_v_Phi[{saving_Phi_name}]")
            elif(CheckDataFrameQ == "y"):
                print("".join(["Histo_P_v_Phi[", str(saving_Phi_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print("".join(["type = ", str(type(Histo_P_v_Phi[saving_Phi_name]))]))
            countSaved += 1

        for saving_thPhi_name in Histo_Th_v_Phi:
            if(SaveResultsQ == 'yes'):
                # Histo_Th_v_Phi[saving_thPhi_name].Write()
                safe_write(Histo_Th_v_Phi[saving_thPhi_name], f"Histo_Th_v_Phi[{saving_thPhi_name}]")
            elif(CheckDataFrameQ == "y"):
                print("".join(["Histo_Th_v_Phi[", str(saving_thPhi_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print("".join(["type = ", str(type(Histo_Th_v_Phi[saving_thPhi_name]))]))
            countSaved += 1

    # # # # # # # # # # # # # # # # # # # # #     Invariant Mass Histograms     # # # # # # # # # # # # # # # # # # # # #

    if(Run_Invariant_Mass_Histos == 'yes'):
        for saving_WM_name in HWC_Histo_All:
            if(SaveResultsQ == 'yes'):
                # HWC_Histo_All[saving_WM_name].Write()
                safe_write(HWC_Histo_All[saving_WM_name], f"HWC_Histo_All[{saving_WM_name}]")
            elif(CheckDataFrameQ == "y"):
                print("".join(["HWC_Histo_All[", str(saving_WM_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print("".join(["type = ", str(type(HWC_Histo_All[saving_WM_name]))]))
            countSaved += 1


    # # # # # # # # # # # # # # # # # # # # #               Done               # # # # # # # # # # # # # # # # # # # # #


    if(SaveResultsQ == 'yes'):
        RoutputFile.Close()
        print("".join([color.BOLD, "Total Histograms Saved = ", color.END, str(countSaved)]))
    else:
        print("".join([color.BOLD, "Total Histograms that would be saved = ", color.END, str(countSaved)]))


    ###############################################################################################################################################################
    ##===========================================================================================================================================================##
    ##==========##==========##==========##==========##==========##         Saved  Histograms         ##==========##==========##==========##==========##==========##
    ##===========================================================================================================================================================##
    ###############################################################################################################################################################
#     else:
#         print("\n\n\033[1mCode not set to make the histograms at this time.\033[0m")




    print(f"\n{color.BOLD}The code has finished running.{color.END}")

    datetime_object_full = datetime.now()

    endMin_full, endHr_full = datetime_object_full.minute, datetime_object_full.hour

    if(datetime_object_full.minute < 10):
        timeMin_full = ''.join(['0', str(datetime_object_full.minute)])
    else:
        timeMin_full = str(datetime_object_full.minute)


    if(datetime_object_full.hour > 12 and datetime_object_full.hour < 24):
        print("".join(["The time that the code finished is ", str((datetime_object_full.hour) - 12), ":", timeMin_full, " p.m."]))
    if(datetime_object_full.hour < 12 and datetime_object_full.hour > 0):
        print("".join(["The time that the code finished is ", str(datetime_object_full.hour), ":", timeMin_full, " a.m."]))
    if(datetime_object_full.hour == 12):
        print("".join(["The time that the code finished is ", str(datetime_object_full.hour), ":", timeMin_full, " p.m."]))
    if(datetime_object_full.hour == 0 or datetime_object_full.hour == 24):
        print("".join(["The time that the code finished is 12:", timeMin_full, " a.m."]))

    DtHr_full = abs(endHr_full - startHr_full)*60
    NewDayQ = 'error'


    if(endHr_full >= startHr_full):
        DtHr_full = abs(endHr_full - startHr_full)*60
        NewDayQ = 'ok'
    elif(endHr_full < startHr_full):
        DtHr_full = abs((endHr_full+24) - startHr_full)*60
        NewDayQ = 'ok'

    DtMin_full = (endMin_full - startMin_full) + DtHr_full

    if(DtMin_full <= 0):
        print("Error")
    else:
        print("".join(["Total time elapsed: ", str(DtMin_full), " minutes"]))
        if(count_Total != 0):
            print("".join(["Rate of histograms made: ", str(count_Total/DtMin_full), " histo/min"]))
        else:
            print("Error: Total Number of Histograms = 0.")

    if(NewDayQ == 'error'):
        print("\nThere may have been an error with the timer.")


else:
    print("Error in getting event type.")
    print("".join(["Current Input: ", str(event_type), """
    
Accepted Inputs are:
    1) SP    -> Single Pion (i.e., ep->eπ+N)
    2) DP    -> Double Pion (i.e., ep->epπ+π-)
    3) P0    -> Pi0 Channel (i.e., ep->epπ0)
    4) ES    -> Elastic Scattering (i.e., ep->e'p')
    4) EO    -> Electron Only (i.e., ep->e'X)
    5) MC    -> Simulated Single Pion (i.e., ep->eπ+N  - same option as SP but file names will be different)
    6) P0_MC -> Simulated Pi0 (i.e., ep->epπ0 - same option as P0 but using simulated files - has two additional options with P0_MC_P and P0_MC_M modifying the momentum of the proton by ±20 MeV)
    
Ending Code...
    """]))

