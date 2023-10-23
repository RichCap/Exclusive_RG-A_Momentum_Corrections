import ROOT
import array
from datetime import datetime
import traceback

from sys import argv
# Let there be 4 arguements in argv when running this code

# Arguement 1: Name of this code (File_Creation_Final_Momentum_Corrections_Github.py)

# Arguement 2: data-type (In/Out)
    # Options: 
    # 1) In -> Inbending
    # 2) Out -> Outbending

# Arguement 3: event-type (type of exclusive events)
    # Options: 
    # 1) SP    -> Single Pion (i.e., ep->eπ+N)
    # 2) DP    -> Double Pion (i.e., ep->epπ+π-)
    # 3) P0    -> Pi0 Channel (i.e., ep->epπ0)
    # 4) ES    -> Elastic Scattering (i.e., ep->e'p')
    # 4) EO    -> Electron Only (i.e., ep->e'X)
    # 5) MC    -> Simulated Single Pion (i.e., ep->eπ+N  - same option as SP but file names will be different)
    # 6) P0_MC -> Simulated Pi0 (i.e., ep->epπ0 - same option as P0 but using simulated files - has two additional options with P0_MC_P and P0_MC_M modifying the momentum of the proton by ±20 MeV)



# Arguement 4: file number (Full file name)
    # If the file number is given as 'All', then all files will be run instead of a select number of them
    # If the file number is given as 'test', then the code will run without saving any of the histograms

# EXAMPLES: 
    # python3 File_Creation_Final_Momentum_Corrections_Github.py In SP All
        # The line above would run ALL INBENDING files together for the ep->eπ+N channel
    # python3 File_Creation_Final_Momentum_Corrections_Github.py Out DP test
        # The line above would test-run the OUTBENDING files for the ep->epπ+π- channel (no results would be saved)
        
        
        

code_name, datatype, event_type, file_location = argv

datatype, file_location, event_type = ''.join([str(datatype), "bending"]), str(file_location), str(event_type)

file_name = str(file_location)


pass_version = "NA"
Beam_Energy = 10.6041 # Fall 2018 Beam Energy

if("_MC" not in event_type):
    # Spring 2019 Data sets
    if("P1" in event_type):
        pass_version = "Spring 2019 - Pass 1"
        Beam_Energy = 10.1998
    if("P2" in event_type):
        pass_version = "Spring 2019 - Pass 2"
        Beam_Energy = 10.1998
    if("C" in event_type):
        pass_version = "".join([pass_version, " - Central Detector"])
    if("F" in event_type):
        pass_version = "".join([pass_version, " - Forward Detector"])

    event_type = str((((event_type.replace("P1", "")).replace("P2", "")).replace("C", "")).replace("F", ""))
    
    
# Normal values used (rounded)
Particle_Mass_Neutron = 0.9396
Particle_Mass_Proton  = 0.938
Particle_Mass_PiC     = 0.13957    # Mass of Charged Pions (same for pi+ and pi-)
Particle_Mass_Pi0     = 0.13498

if("_MC" in event_type):
    # # Exact values used by PDGParticle (see: https://github.com/JeffersonLab/clas12-offline-software/blob/516f47374b25c86d4e65cbeb1009c3422906949a/common-tools/clas-physics/src/main/java/org/jlab/clas/pdg/PDGDatabase.java#L31)
    Particle_Mass_Neutron = 0.9396
    Particle_Mass_Neutron = 0.939565379

    Particle_Mass_Proton  = 0.938
    # Particle_Mass_Proton  = 0.938272046

    Particle_Mass_PiC     = 0.13957    # Mass of Charged Pions (same for pi+ and pi-)
    Particle_Mass_PiC     = 0.13957018 # Mass of Charged Pions (same for pi+ and pi-)

    Particle_Mass_Pi0     = 0.13498
    Particle_Mass_Pi0     = 0.1349766
    print("".join(["Setting Masses as:\nParticle_Mass_Neutron = ", str(Particle_Mass_Neutron), "\nParticle_Mass_Proton  = ", str(Particle_Mass_Proton), "\nParticle_Mass_PiC     = ", str(Particle_Mass_PiC), "\nParticle_Mass_Pi0     = ", str(Particle_Mass_Pi0)]))


    
    
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

file_name = str(file_name.replace("-", "_")).replace(".hipo.root", "")
file_name = str(file_name).replace(".evio.root", "")
file_name = str(file_name).replace(".root", "")

    
ROOT.gStyle.SetTitleOffset(1.3, 'y')
ROOT.gStyle.SetGridColor(17)
ROOT.gStyle.SetPadGridX(1)
ROOT.gStyle.SetPadGridY(1)


class color:
    PURPLE    = '\033[95m'
    CYAN      = '\033[96m'
    DARKCYAN  = '\033[36m'
    BLUE      = '\033[94m'
    GREEN     = '\033[92m'
    YELLOW    = '\033[93m'
    RED       = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    DELTA     = '\u0394' # symbol
    END       = '\033[0m'

    
class root_color:
    # Colors
    Black  = 0
    Red    = 2
    Green  = 3
    Blue   = 4
    Yellow = 5
    Pink   = 6
    Cyan   = 7
    DGreen = 8 # Dark Green
    Purple = 9
    Grey   = 13
    Brown  = 28
    Gold   = 41
    Rust   = 46
    
    # Fonts
    Bold   = '#font[22]'
    Italic = '#font[12]'
    
    # Symbols
    Delta   = '#Delta'
    Phi     = '#phi'
    # π     = '#pi'
    Degrees = '#circ'
    
    Line = '#splitline'


event_Name = "error"

if(event_type == "E0"):
    print("".join([color.RED, "ERROR: E0 is not the correct input type...", color.END, "\n\tSetting to event_type = EO"]))
    event_type = "EO"


if(event_type in ["SP", "MC", "SIDIS"]):
    event_Name = "Single Pion Channel"
    MM_type = "epipX"
    
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

if("MC" in event_Name):
    Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max = 200, 0.01, 0.03
    
if(event_Name != "error"):
    
    print("".join([color.BOLD, color.BLUE, "\n\n\nStarting ", str(event_Name), " ", str(datatype), "...\n", color.END]))
    
    if(pass_version != "NA" and pass_version != ""):
        print("".join(["\n", color.BOLD, color.BLUE, "RUNNING FILES FROM: ", str(pass_version), "\n", color.END]))
        
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








    ##########################################################################
    ##=====##=====##=====##     Choices for Saving     ##=====##=====##=====##
    ##########################################################################
    SaveResultsQ = 'yes'
    # SaveResultsQ = 'no'

    if(file_location in ["Test", "test", "time"]):
        SaveResultsQ = 'no'

    if(SaveResultsQ == 'no'):
        print("\033[1mNot saving results...\033[0m")
    else:
        print("\033[1mResults WILL be saved\033[0m")


    Extra_Part_of_Name = "_New_Proton_Refinement_V3"
    # Plotting the larger ∆P instead of the flipped choices
    # Modified the ENERGY LOSS CORRECTIONS (removed the constant terms)
    
    if(event_type in ["SP", "P0"]):
        Extra_Part_of_Name = "_GitHub_3D_Dp_Test_V2"
        # Testing improved ∆P calculation (p_calc can't be negative)
        if("MC" in event_Name):
            Version_MC = "_V14"
            # Using reconstructed kinematics (not using full sig figs for proton)
            # Changed binning for the square root term histograms
            # Added cut on the square root term (instead of ∆P - cut is for less than 0.05)
            
            Extra_Part_of_Name = "".join(["_MC_Testing_Normal", str(Version_MC)])
            
            if("+20 MeV" in event_Name):
                Extra_Part_of_Name = "_MC_Testing_Plus_V3"
                # Removed all non-testing corrections
                # ∆P histograms now do not plot sector-by-sector
                # Testing ∆P = P_calculated - P_generated (instead of measured)
                # Plotting the larger ∆P instead of the flipped choices
                
                Extra_Part_of_Name = "".join(["_MC_Testing_Plus", str(Version_MC)])
                
            if("-20 MeV" in event_Name):
                Extra_Part_of_Name = "_MC_Testing_Minus_V3"
                # Removed all non-testing corrections
                # ∆P histograms now do not plot sector-by-sector
                # Testing ∆P = P_calculated - P_generated (instead of measured)
                # Plotting the larger ∆P instead of the flipped choices
                
                Extra_Part_of_Name = "".join(["_MC_Testing_Minus", str(Version_MC)])
                
            if("(GEN)" in event_Name):
                Version_MC = "_V2"
                # Added cut on the square root term (instead of ∆P - cut is for less than 0.05)
                # Ran with "_V14" for REC
                
                Extra_Part_of_Name = "".join(["_MC_GEN_Test", str(Version_MC)])
                
    
    if(event_type == "MC"):
        Extra_Part_of_Name = "_GitHub_MC_Test_V1"
        # Testing the momentum corrections using Monte Carlo files (for use in SIDIS analysis)
        # Runs the same as event_type == "SP"
        
    if(pass_version not in ["NA", ""]):
        Extra_Part_of_Name = "".join(["_GitHub_Spring_2019_Pass_", "1" if("Pass 1" in pass_version) else "2", "_NEW_V1"])
        # Now has the more complete set of pass 2 files
        
    if("Central" in pass_version):
        Extra_Part_of_Name = "".join(["_GitHub_Spring_2019_Pass_", "1" if("Pass 1" in pass_version) else "2", "_V3" if("Central" not in pass_version) else "_Central_V1"])
        # No changes to regular Spring 2019 files (as of V3 above), but added the option to plot using only central detector pions
        # Added option to include "C" in the 3rd arguement of this code's input in order to switch from the Forward dectector to the central detector
        
    
    if("Out" in datatype):        
        Extra_Part_of_Name = "_Final_Outbending"
        # Complete set of corrections/histograms with the final versions of the corrections
            # Added a 'PipMMExF' option to see the old (extended) versions of the pion correction
            # The 'ExF' options of both particles are now used for the 'EF' versions of the prior 'Extra_Part_of_Name' iterations with the 'EF' version of the correction used as of '_Final_Outbending' is the one-line equivalent for those corrections
    
    
    
    # New Names as of 9-19-2023 (After Fall 2018 - Pass 1 corrections were finished)
    if("Pass" in str(pass_version)):
        Pass_File_Name     = str(pass_version).replace(" Detector", "")
        Pass_File_Name     = str(Pass_File_Name.replace("-", "_")).replace(" ", "_")
        Pass_File_Name     = str(Pass_File_Name.replace("___", "_"))
        Pass_File_Name     = str(Pass_File_Name.replace("__",  "_"))
        
        Extra_Version_Name = "_V1"
        # Ran on 9/19/2023-9/20/2023 with Spring 2019 data (Pass 2)
            # Ran 3 versions of files for SP and EO events (6 files total)
                # Included normal code (no changes since the last time it was run) and 2 versions where cuts to check the central/forward detector separately (via theta cuts) were added
                # Note: Later change was made to the Central detector cuts to remove the condition that the electron be detected there (no events were suriving the cut)
                    # This change was updated for only the SP events (Central EO would be the same as the other files if the cut was removed)
                    # Didn't matter since the central detector was cut in the groovy script already (did not remove the cut beforehand)
                    
                    
        Extra_Version_Name = "_V2"
        # Ran on 9/21/2023 with Spring 2019 data (Pass 2)
        # Added Refinements to the earlier Pass 2 Corrections (added phi-dependence)
            # Correction name is 'mmRP2' for 'Refined'-'Pass 2'
        # Extended the plot range of the theta particle in relavent plots (will help see the central detector particles later)
        
        
        Extra_Version_Name = "_V3"
        # Ran on 9/22/2023 with Spring 2019 data (Pass 2)
        # Refined the phi-dependent Pass 2 Correction again
            # Correction is still called 'mmRP2'
            
            
        Extra_Version_Name = "_V4"
        # Ran on 9/29/2023 with Spring 2019 data (Pass 2)
        # Added a pi+ phi-dependent Correction based on 'mmRP2'
        # Needed to test a potential issue in the Inbending pi+ corrections
            # Testing to see what the differences are between 'PipMMF', 'PipMMExF', and 'PipMMEF' in case the Inbending corrections for 'PipMMF' and 'PipMMEF' are the same (possible naming error in Inbending Pass 1)
                # RESULT OF TEST: The issue did NOT exist when finalizing the Pass 1 Corrections. It does, however, exist now such that the 'PipMMEF' correction no longer works the same as it did when finalizing the results
                    # The issue must have been created while working on the Outbending corrections with the Inbending code never having been readdressed and fixed before this point
                    # The issue has been resolved (for the next file version) and since the pion correction has not been used to develop new corrections yet, this presents no concerns for the status of the Pass 2 corrections
                    
                    
        Extra_Version_Name = "_V5"
        # Ran on 10/5/2023 with Spring 2019 data (Pass 2 AND Pass 1)
        # Refined the pi+ phi-dependent Correction based on 'mmRP2_PipMMP2'
            # Name has not been changed
        # Fixed the issue noted in the 'RESULT OF TEST' section of the 'Extra_Version_Name = "_V4"' notes
            # No longer using the extra corrections ('ExF') now that the test is complete
        # Finished creating the Pass 1 version of the required files
            # Ran with Pass 2 versions
            # Included the Pass 2 versions of the corrections to test how compatile they are (no existing Pass 1 corrections to compare otherwise)
            
            
        Extra_Version_Name = "_V6"
        # Ran on 10/16/2023 with Spring 2019 data (Pass 2 and Pass 1)
        # Made a new refinement correction for the pi+ pion based on 'mmRP2_PipMMP2'
            # Called 'mmRP2_PipMMsP2'
            # This correction splits the data to create separate corrections based on whether the pion momentum is above or below 4 GeV
            # As of this file, the refinement only is applied if pip >= 4
        # No new Pass 1 corrections were made
            # Now not running Pass 2 corrections for any pass 1 data set
        # Now running sector-by-sector phase space plots to try to find the issue with the pipPhi angle favoring larger values
        
        
        Extra_Version_Name = "_V7"
        # Running on 10/23/2023 with Spring 2019 data (Pass 2 and Pass 1)
        # Did not update the new refinement correction for the pi+ pion from the last version
            # Correction 'mmRP2_PipMMsP2' is still the same as it was in Extra_Version_Name = "_V6"
        # No new corrections/refinements were made (for either Pass version)
            # Still using all the same corrections and histograms as was used in Extra_Version_Name = "_V6"
        # Modified the Missing/Invariant Mass Exclusivity Cuts for the Spring 2019 data
            # Was still using the same cuts as the Pass 1 Fall 2018 data
            # Cuts are now unique between datasets and pass versions
                # Will still have the same name (must keep track of file version to track difference in the exclusivity cuts)
            # Single Pion Channels have cuts which are functions of electron sector, local phi angle, and momentum
                # phi-dependence is not continuous
                # Linear dependence on momentum
                # Cuts are from fits of the widths of the peak distributions (boundaries are taken from 3-sigma widths in both directions)
            # Electron Only/Elastic Scattering Channels have cuts which are functions of electron sector and momentum
                # No phi-dependence
                # Linear dependence on momentum for the upper cut, cut is constant in momentum for the lower cut
                # Cuts are from fits of the widths of the peak distributions (boundaries are taken from a 2-sigma width for the upper cut and a 3-sigma width for the lower cut)
        # Updated the time-estimates for running the code
            # Does not impact how the code runs
            # Just helps predict the amount of time that will be required to run when running the code as a test
        
        
        Extra_Part_of_Name = "".join(["_", str(Pass_File_Name), "_rec_clas", str(Extra_Version_Name)])
        # 'rec_clas' refers to the DST files used to create the root files in this code
            # The DST files are what was used instead of the skim4 or nSidis files since there was not any current versions of the skim files without the cuts I wanted removed
        # Refer to Extra_Version_Name above for version notes
    else:
        Extra_Part_of_Name = "_Pass1_Final_Tests_V1"
        # Ran with Extra_Version_Name = "_V4" above (with Pass 1 Fall 2018 data)
            # RESULT OF TEST: The issue did NOT exist when finalizing the Pass 1 Corrections. It does, however, exist now such that the 'PipMMEF' correction no longer works the same as it did when finalizing the results
                # The issue must have been created while working on the Outbending corrections with the Inbending code never having been readdressed and fixed before this point
                # The issue has been resolved (for the next file version) and since the pion correction has not been used to develop new corrections yet, this presents no concerns for the status of the Pass 2 corrections
    
    
    if(event_type != "MC"):
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
        if(Delta_P_histo_Q != 'y'):
            OutputFileName = "".join(["Simulated_", event_Name.replace(" ", "_"), "_", str(MM_type), "_", str(datatype), "_No_Dp",   str(Extra_Part_of_Name), "_File_", str(file_name), ".root"])
        else:
            OutputFileName = "".join(["Simulated_", event_Name.replace(" ", "_"), "_", str(MM_type), "_", str(datatype), "_With_Dp", str(Extra_Part_of_Name), "_File_", str(file_name), ".root"])
            
            

    print("".join(["\n\033[1mName of file that will be saved:\033[0m\n", str(OutputFileName), "\n"]))


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
                    # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/shrestha/clas12momcorr/data/inbending/ePipX/epip.skim4_00*"
                    # running_code_with_these_files = "/work/clas12/shrestha/clas12momcorr/utsav/dataFiles/inbending/ePipX/epip.skim4_005*"
                    running_code_with_these_files = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Single_Pion_Channel_epipN/Inbending/ePip.inb.qa.nSidis_005*"
                    running_code_with_these_files = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Single_Pion_Channel_epipN/Inbending_skim4/ePip.inb.qa.skim4_00*"
                else:
                    # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/shrestha/clas12momcorr/outbending/ePipX/skim4_00*"
                    # running_code_with_these_files = "/work/clas12/shrestha/clas12momcorr/utsav/dataFiles/outbending/ePipX/skim4_005*"
                    running_code_with_these_files = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Single_Pion_Channel_epipN/Outbending/ePip.outb.qa.nSidis_005*"
                    
                    # Skim4 cuts
                    # running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Outbending_skim4/ePip.outb.qa.rec_clas_005449.evio.0*.root"
                    running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Outbending_skim4/ePip.outb.qa.rec_clas_*.root"
            # elif("Central" in pass_version):
            #     if("Pass 1" in pass_version):
            #         running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Central_Tracking/Pass1/Inbending/ePip.Central.pass1.inb.qa.nSidis_00*"
            #     else:
            #         running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Central_Tracking/Pass2/Inbending/ePip.Central.pass2.inb.qa.nSidis_00*"
            # else:
            if("Pass 1" in pass_version):
                running_code_with_these_files = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Spring2019/Pass1/Inbending_nSidis/ePip.pass1.inb.qa.nSidis_00*"
                # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Spring2019/Pass1/Inbending/ePip.pass1.inb.qa.MissingNeutron_00*"
                running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass1/Inbending_recon/Single_Pion_Channel_epipN/ePip.pass1.inb.qa.rec_clas_00*"
            else:
                # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Spring2019/Pass2/Inbending_nSidis/ePip.pass2.inb.qa.nSidis_00*"
                # # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Spring2019/Pass2/Inbending/ePip.pass2.inb.qa.MissingNeutron_00*"
                # running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/Inbending_nSidis/Complete/ePip.pass2.inb.qa.nSidis_00*"
                # # running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/Inbending_nSidis/ePip.pass2.inb.qa.nSidis_00*"
                running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/Inbending_recon/Single_Pion_Channel_epipN/ePip.pass2.inb.qa.rec_clas_00*"
        
        
        if(event_type == "DP"):
            if(datatype == "Inbending"):
                # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/inb/epPipPim.inb.qa.nSidis_005*"
                running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Double_Pion_Channel_eppippim/Inbending_skim4/epPipPim.inb.qa.skim4_00*"
            else:
                # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/outb/epPipPim.outb.qa.nSidis_005*"
                running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Double_Pion_Channel_eppippim/Outbending_skim4/epPipPim.outb.qa.skim4_00*"
                
            # running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Double_Pion_Channel_eppippim/", str(datatype), "/epPipPim.", "out" if("Out" in str(datatype)) else "in", "b.qa.nSidis_005*"])
                
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
                # running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/", str(datatype), "/*.root"])
                # running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/", str(datatype), "/eP_Elastic_with_CDpro*.root"])
                running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/", str(datatype), "/eP_Elastic_with_CDpro_New*.root"])
                running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/Valerii_Files/eP_Elastic_with_CDpro_New", ".inb" if("In" in str(datatype)) else ".outb", "*root"])
                running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/Valerii_Files/eP_Elastic_with_CDpro", ".inb" if("In" in str(datatype)) else ".outb", "*root"])
            else:
                # Skim4 cuts
                running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Elastic_Scattering_ep/Outbending/eP_Elastic_with_CDpro.outb.qa.rec_clas_005449.evio.0*.root"
                
        if(event_type == "EO"):
            if(datatype == "Inbending"):
                running_code_with_these_files     = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Only_Electron_Channel/electron_only", ".inb" if("In" in str(datatype)) else ".outb", "*root"])
                if("Pass 2" in pass_version):
                    running_code_with_these_files = "".join(["/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/", "Inbending" if("In" in str(datatype)) else "Outbending", "_nSidis/Complete/Only_Electron_Channel/electron_only.pass2", ".inb" if("In" in str(datatype)) else ".outb", ".qa.nSidis_*root"])
                    running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/Inbending_recon/Only_Electron_Channel/electron_only.pass2.inb.qa.rec_clas_00*"
                else:
                    running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass1/Inbending_recon/Only_Electron_Channel/electron_only.pass1.inb.qa.rec_clas_00*"
            else:
                # Skim4 cuts
                running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Only_Electron_Channel/Outbending/electron_only.outb.qa.rec_clas_005449.evio.0*.root"
                running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Only_Electron_Channel/Outbending/electron_only.outb.qa.rec_clas_005*.root"
                
        if(event_type == "MC"):
            running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/SIDIS_Analysis/Data_Files_Groovy/Matched_REC_MC/MC_Matching_sidis_epip_richcap.inb.qa.45nA_job_*.root"])
            event_type = "SP"

    else:
        running_code_with_these_files = file_location

    rdf = ROOT.RDataFrame("h22", str(running_code_with_these_files))
    
    if("E" in event_type):
        print(color.BOLD + "\nApplying Base Invariant Mass Cuts to Elastic Events...\n" + color.END)
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

    #############################################################################
    ##=====##=====##=====##=====##   Loading RDF   ##=====##=====##=====##=====##
    #############################################################################

    if(See_Num_of_Events_Q != 'n'):
        print("".join(["Number of events = ", str(rdf.Count().GetValue())]))
    print("".join([color.BOLD, color.BLUE, "Running code with files located here:\n", color.END, str(running_code_with_these_files), "\n"]))




    if(event_type not in ["SP", "MC", "EO"]):
#         if("MC" not in event_Name):
#             if("prox" not in rdf.GetColumnNames() and "px" in rdf.GetColumnNames()):
#                 rdf = rdf.Define("prox", "px")
#             if("proy" not in rdf.GetColumnNames() and "py" in rdf.GetColumnNames()):
#                 rdf = rdf.Define("proy", "py")
#             if("proz" not in rdf.GetColumnNames() and "pz" in rdf.GetColumnNames()):
#                 rdf = rdf.Define("proz", "pz")
#             if("prosec" not in rdf.GetColumnNames() and "psec" in rdf.GetColumnNames()):
#                 rdf = rdf.Define("prosec", "psec")
        if("(GEN)" not in event_Name):
            if("prox" not in rdf.GetColumnNames() and "px" in rdf.GetColumnNames()):
                rdf = rdf.Define("prox", "px")
            if("proy" not in rdf.GetColumnNames() and "py" in rdf.GetColumnNames()):
                rdf = rdf.Define("proy", "py")
            if("proz" not in rdf.GetColumnNames() and "pz" in rdf.GetColumnNames()):
                rdf = rdf.Define("proz", "pz")
            if("prosec" not in rdf.GetColumnNames() and "psec" in rdf.GetColumnNames()):
                rdf = rdf.Define("prosec", "psec")
        else:
            print("".join([color.BOLD, color.RED, "\n\nPro is generated", color.END]))
            if("prox" not in rdf.GetColumnNames() and "px0" in rdf.GetColumnNames()):
                rdf = rdf.Define("prox", "px0")
            if("proy" not in rdf.GetColumnNames() and "py0" in rdf.GetColumnNames()):
                rdf = rdf.Define("proy", "py0")
            if("proz" not in rdf.GetColumnNames() and "pz0" in rdf.GetColumnNames()):
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
        
        Proton_Energy_Loss_Cor = ''.join(["""
        
        
        double dE_loss = 0;
        
        //=====// My Version of Andrey's Proton Energy Loss Correction (Corrections should be identical) //=====//
        
        """, """
        
        // Inbending Energy Loss Correction //
        if(proth < 27){
            dE_loss = exp(-2.739 - 3.932*pro); // + 0.002907;
        }
        if(proth > 27){
            dE_loss = exp(-1.2 - 4.228*pro); // + 0.007502;
        }
        
        
        """ if("In" in datatype) else """
        
        // Outbending Energy Loss Correction //
        if(proth > 27){
            dE_loss = exp(-1.871 - 3.063*pro); // + 0.007517;
        }
        
        """, """
        
        
        double feloss = (pro + dE_loss)/pro;

    
    """])
    


    ##########################################################################################################################
    ##==============##============##         Standard Kinematics - Angles and Momentums         ##============##============##
    ##########################################################################################################################


    #------------------------------------------#
    #---------------# Electron #---------------#
    #------------------------------------------#
    try:
#         if("MC" not in event_Name):
        if("(GEN)" not in event_Name):
            ##=====##    Momentum Magnitude    ##=====##
            rdf = rdf.Define("el", "sqrt(ex*ex + ey*ey + ez*ez)")
            ##=====##       Polar Angles       ##=====##
            rdf = rdf.Define("elth", "atan2(sqrt(ex*ex + ey*ey), ez)*(180/3.1415926)")
            # if("Central" in str(pass_version)):
            #     print(color.BOLD, "\nMAKING CUT ON ELECTRON POLAR ANGLE TO SELECT THE EVENTS FROM THE 'Central' DETECTOR\n", color.END)
            #     rdf = rdf.Filter("elth > 35 && elth < 135")
            if("Forward" in str(pass_version)):
                print(color.BOLD, "\nMAKING CUT ON ELECTRON POLAR ANGLE TO SELECT THE EVENTS FROM THE 'Forward' DETECTOR\n", color.END)
                rdf = rdf.Filter("elth >  5 && elth <  35")
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
            print("".join([color.BOLD, color.RED, "El is generated\n\n", color.END]))
            ##=====##    Momentum Magnitude    ##=====##
            rdf = rdf.Define("el", "sqrt(ex0*ex0 + ey0*ey0 + ez0*ez0)")
            ##=====##       Polar Angles       ##=====##
            rdf = rdf.Define("elth", "atan2(sqrt(ex0*ex0 + ey0*ey0), ez0)*(180/3.1415926)")
            # if("Central" in str(pass_version)):
            #     print(color.BOLD, "\nMAKING CUT ON ELECTRON POLAR ANGLE TO SELECT THE EVENTS FROM THE 'Central' DETECTOR\n", color.END)
            #     rdf = rdf.Filter("elth > 35 && elth < 135")
            if("Forward" in str(pass_version)):
                print(color.BOLD, "\nMAKING CUT ON ELECTRON POLAR ANGLE TO SELECT THE EVENTS FROM THE 'Forward' DETECTOR\n", color.END)
                rdf = rdf.Filter("elth >  5 && elth <  35")
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
                if("Central" in str(pass_version)):
                    print("".join([color.BOLD, "\nMAKING CUT ON PI+ PION POLAR ANGLE TO SELECT THE EVENTS FROM THE 'Central' DETECTOR\n\n", color.END]))
                    rdf = rdf.Filter("pipth > 35 && pipth < 135")
                if("Forward" in str(pass_version)):
                    print("".join([color.BOLD,   "MAKING CUT ON PI+ PION POLAR ANGLE TO SELECT THE EVENTS FROM THE 'Forward' DETECTOR\n\n", color.END]))
                    rdf = rdf.Filter("pipth >  5 && pipth <  35")
                ##=====##     Azimuthal Angles     ##=====##
                rdf = rdf.Define("pipPhi", """
                    double pipPhi = (180/3.1415926)*atan2(pipy, pipx);
                    if(((pipsec == 4 || pipsec == 3) && pipPhi < 0) || (pipsec > 4 && pipPhi < 90)){
                        pipPhi += 360;
                    }
                    return pipPhi;
                """)
                rdf = rdf.Define("localpipPhi", "pipPhi - (pipsec - 1)*60")
                rdf = rdf.Define("localpipPhiS", "localpipPhi + (32/(pip-0.05))")
                rdf = rdf.Define("pipPhiS", "pipPhi + (32/(pip-0.05))")
                rdf = rdf.Define("pipPhiNS", "(180/3.1415926)*atan2(pipy, pipx)") # 'NS' ==> No shifts (distribution will be from ±180˚)
            except Exception as e:
                print("Failure to process Pi+ Pion Kinematics")
                print("".join(["ERROR: ", str(e)]))

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
                rdf = rdf.Define("localproPhi_cor", "proPhi_cor - (prosec - 1)*60")
                rdf = rdf.Define("localproPhiS_cor", "localproPhi_cor + (32/(pro_cor-0.05))")
                rdf = rdf.Define("proPhiS_cor", "proPhi_cor + (32/(pro_cor-0.05))")
                rdf = rdf.Define("proPhiNS_cor", "(180/3.1415926)*atan2(proy_cor, prox_cor)") # 'NS' ==> No shifts (distribution will be from ±180˚)
            except Exception as e:
                print("Failure to process Proton Kinematics")
                print("".join(["ERROR: ", str(e)]))


    ################################################################################################################################
    ##==============##============##         Standard Kinematics - Angles and Momentums (End)         ##============##============##
    ################################################################################################################################





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




    #####################################################################################################
    ##=================================================================================================##
    ##==============##============##         Inbending Corrections         ##============##============##
    ##=================================================================================================##
    #####################################################################################################

    ##############################################################
    #----------#      Last updated on: 10-5-2023      #----------#
    ##############################################################
    Correction_Code_Full_In, Correction_Code_Full_Out = "", ""
    if(datatype == "Inbending"):
        
        Correction_Code_Full_In = """
        
        auto dppC = [&](float Px, float Py, float Pz, int sec, int ivec, int corEl, int corPip, int corPim, int corPro){

            // ivec = 0 --> Electron Corrections
            // ivec = 1 --> Pi+ Corrections
            // ivec = 2 --> Pi- Corrections
            // ivec = 3 --> Proton Corrections

            // corEl ==> Gives the 'generation' of the electron correction
                // corEl == 0 --> No Correction
                // corEl == 1 --> Final Version of Corrections
                // corEl == 2 --> Modified/Extended Correction (using the Elastic Events - based of existing corrections)
                // corEl == 3 --> New Extended Correction (using the Elastic Events - created from uncorrected ∆P Plots)
                // corEl == 4 --> Old Pass2 Corrections (Incomplete)
                // corEl == 5 --> New Pass2 Corrections (Refinement)
                
            // corPip ==> Gives the 'generation' of the π+ Pion correction
                // corPip == 0 --> No Correction
                // corPip == 1 --> Old Version of Corrections
                // corPip == 2 --> Final Version of Corrections (uses the wrong name   - is mmExF - same correction as corPip == 3)
                // corPip == 3 --> Final Version of Corrections (uses the correct name - is mmEF  - same correction as corPip == 2)
                // corPip == 4 --> New Pass2 Corrections (Incomplete)
                // corPip == 5 --> New Pass2 Corrections (refinement of corPip == 4  --- is split between two functions at p = 4 GeV)

            // corPim ==> Gives the 'generation' of the π- Pion correction
                // corPim == 0 --> No Correction
                // corPim == 1 --> Nick's Quadratic Momentum, Quadratic Phi

            // corPro ==> Gives the 'generation' of the Proton correction
                // corPro == 0 --> No Correction
                // corPro == 1 --> Quad Momentum, Quad Phi
                // corPro == 2 --> Quad Momentum, NO Phi
                // corPro == 3 --> Linear Momentum, NO Phi


            // Momentum Magnitude
            double pp = sqrt(Px*Px + Py*Py + Pz*Pz);

            // Initializing the correction factor
            double dp = 0;

            // Defining Phi Angle
            double Phi = (180/3.1415926)*atan2(Py, Px);

            // (Initial) Shift of the Phi Angle (done to realign sectors whose data is separated when plotted from ±180˚)
            if(((sec == 4 || sec == 3) && Phi < 0) || (sec > 4 && Phi < 90)){
                Phi += 360;
            }

            // Getting Local Phi Angle
            double PhiLocal = Phi - (sec - 1)*60;

            // Applying Shift Functions to Phi Angles (local shifted phi = phi)
            double phi = PhiLocal;

            // For Electron Shift
            if(ivec == 0){
                phi = PhiLocal - 30/pp;
            }

            // For π+ Pion/Proton Shift
            if(ivec == 1 || ivec == 3){
                phi = PhiLocal + (32/(pp-0.05));
            }

            // For π- Pion Shift
            if(ivec == 2){
                phi = PhiLocal - (32/(pp-0.05));
            }
            
            
            ////////////////////////////////////////////////////////////////////////////////////////////////
            //===============//===============//     No Corrections     //===============//===============//
            ////////////////////////////////////////////////////////////////////////////////////////////////

            if(corEl == 0 && ivec == 0){ // No Electron Correction
                dp = 0;
            }
            if(corPip == 0 && ivec == 1){ // No π+ Pion Correction
                dp = 0;
            }
            if(corPim == 0 && ivec == 2){ // No π- Pion Correction
                dp = 0;
            }
            if(corPro == 0 && ivec == 3){ // No Proton Correction
                dp = 0;
            }

            //////////////////////////////////////////////////////////////////////////////////////////////////
            //==============//==============//     No Corrections (End)     //==============//==============//
            //////////////////////////////////////////////////////////////////////////////////////////////////




            //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //==================================================================================================================================//
            //=======================//=======================//     Electron Corrections     //=======================//=======================//
            //==================================================================================================================================//
            //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


            if(corEl != 0 && ivec == 0){
                if(sec == 1){
                    dp = ((1.57e-06)*phi*phi + (5.021e-05)*phi + (-1.74089e-03))*pp*pp + ((-2.192e-05)*phi*phi + (-1.12528e-03)*phi + (0.0146476))*pp + ((8.504e-05)*phi*phi + (2.08012e-03)*phi + (-0.0122501));
                }
                if(sec == 2){
                    dp = ((-3.98e-06)*phi*phi + (1.66e-05)*phi + (-1.55918e-03))*pp*pp + ((2.136e-05)*phi*phi + (-5.7373e-04)*phi + (0.0143591))*pp + ((2.4e-06)*phi*phi + (1.6656e-03)*phi + (-0.0218711));
                }
                if(sec == 3){
                    dp = ((5.57e-06)*phi*phi + (2.3e-07)*phi + (-2.26999e-03))*pp*pp + ((-7.761e-05)*phi*phi + (4.1437e-04)*phi + (0.0152985))*pp + ((2.2542e-04)*phi*phi + (-9.442e-04)*phi + (-0.0231432));
                }
                if(sec == 4){
                    dp = ((3.48e-06)*phi*phi + (2.166e-05)*phi + (-2.29e-04))*pp*pp + ((-2.758e-05)*phi*phi + (7.226e-05)*phi + (-3.38e-03))*pp + ((3.166e-05)*phi*phi + (6.93e-05)*phi + (0.04767));
                }
                if(sec == 5){
                    dp = ((1.19e-06)*phi*phi + (-2.286e-05)*phi + (-1.6332e-04))*pp*pp + ((-1.05e-06)*phi*phi + (7.04e-05)*phi + (-5.0754e-03))*pp + ((-7.22e-06)*phi*phi + (4.1748e-04)*phi + (0.04441));
                }
                if(sec == 6){
                    dp = ((-5.97e-06)*phi*phi + (-3.689e-05)*phi + (5.782e-05))*pp*pp + ((6.573e-05)*phi*phi + (2.1376e-04)*phi + (-9.54576e-03))*pp + ((-1.7732e-04)*phi*phi + (-8.62e-04)*phi + (0.0618975));
                }
                
                // Extended Refinement of corEl == 1
                if(corEl == 2){
                    if(sec == 1){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected][Sector 1] is:
                        dp = dp + ((-1.5543e-05)*phi*phi + (-6.1257e-05)*phi + (9.0385e-04))*pp*pp + ((1.8051e-04)*phi*phi + (9.0971e-04)*phi + (-0.010544))*pp + ((-4.7617e-04)*phi*phi + (-0.0029024)*phi + (0.02882));
                    }
                    if(sec == 2){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected][Sector 2] is:
                        dp = dp + ((-1.0753e-07)*phi*phi + (-4.3441e-05)*phi + (-2.4143e-04))*pp*pp + ((-9.1649e-06)*phi*phi + (5.5094e-04)*phi + (0.0046169))*pp + ((5.7005e-05)*phi*phi + (-0.0014851)*phi + (-0.017753));
                    }
                    if(sec == 3){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected][Sector 3] is:
                        dp = dp + ((-1.3656e-05)*phi*phi + (-6.3819e-06)*phi + (9.4242e-04))*pp*pp + ((1.5109e-04)*phi*phi + (-1.6847e-04)*phi + (-0.010423))*pp + ((-3.8962e-04)*phi*phi + (0.001198)*phi + (0.029035));
                    }
                    if(sec == 4){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected][Sector 4] is:
                        dp = dp + ((-7.7030e-06)*phi*phi + (-2.2183e-05)*phi + (-3.2310e-04))*pp*pp + ((9.1683e-05)*phi*phi + (1.8863e-04)*phi + (0.0025154))*pp + ((-2.3756e-04)*phi*phi + (-2.8317e-04)*phi + (-0.0046244));
                    }
                    if(sec == 5){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected][Sector 5] is:
                        dp = dp + ((-8.7306e-07)*phi*phi + (2.1699e-05)*phi + (-5.7166e-04))*pp*pp + ((7.4275e-06)*phi*phi + (-2.5637e-04)*phi + (0.0054676))*pp + ((-1.2134e-05)*phi*phi + (8.1743e-04)*phi + (-0.010263));
                    }
                    if(sec == 6){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected][Sector 6] is:
                        dp = dp + ((4.3560e-06)*phi*phi + (3.3573e-05)*phi + (-6.6964e-04))*pp*pp + ((-6.6393e-05)*phi*phi + (-3.0575e-04)*phi + (0.0084299))*pp + ((2.4042e-04)*phi*phi + (5.1189e-04)*phi + (-0.024095));
                    }
                    if(sec == 1){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected (Extended)][Sector 1] is:
                        dp = dp + ((7.9660e-06)*phi*phi + (5.1523e-05)*phi + (-2.1894e-04))*pp*pp + ((-1.2252e-04)*phi*phi + (-6.2769e-04)*phi + (0.0029742))*pp + ((4.1380e-04)*phi*phi + (0.0017672)*phi + (-0.0092031));
                    }
                    if(sec == 2){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected (Extended)][Sector 2] is:
                        dp = dp + ((-2.1372e-06)*phi*phi + (2.0673e-05)*phi + (-1.7416e-04))*pp*pp + ((2.0227e-05)*phi*phi + (-2.6449e-04)*phi + (0.0026238))*pp + ((-4.7051e-05)*phi*phi + (7.5652e-04)*phi + (-0.0086124));
                    }
                    if(sec == 3){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected (Extended)][Sector 3] is:
                        dp = dp + ((3.3352e-09)*phi*phi + (-2.7138e-05)*phi + (1.8147e-04))*pp*pp + ((-2.2826e-05)*phi*phi + (2.6561e-04)*phi + (-0.0021432))*pp + ((1.3156e-04)*phi*phi + (-6.2599e-04)*phi + (0.0056483));
                    }
                    if(sec == 4){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected (Extended)][Sector 4] is:
                        dp = dp + ((8.0009e-06)*phi*phi + (1.1847e-05)*phi + (-4.0825e-04))*pp*pp + ((-1.0793e-04)*phi*phi + (-1.8450e-04)*phi + (0.005087))*pp + ((3.2556e-04)*phi*phi + (5.9843e-04)*phi + (-0.014079));
                    }
                    if(sec == 5){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected (Extended)][Sector 5] is:
                        dp = dp + ((3.5908e-07)*phi*phi + (-1.2954e-06)*phi + (-4.4109e-05))*pp*pp + ((-9.7218e-07)*phi*phi + (1.4249e-05)*phi + (2.9679e-04))*pp + ((-9.7975e-06)*phi*phi + (-5.2075e-05)*phi + (8.0729e-05));
                    }
                    if(sec == 6){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Corrected (Extended)][Sector 6] is:
                        dp = dp + ((-5.9006e-06)*phi*phi + (8.0310e-06)*phi + (2.0305e-04))*pp*pp + ((8.3625e-05)*phi*phi + (-4.1055e-05)*phi + (-0.0020693))*pp + ((-2.8471e-04)*phi*phi + (-6.3169e-05)*phi + (0.0046844));
                    }
                }
                
                // New Corrections created from corEl == 0 (wider kinematic range than what was used to create corEl == 1)
                if(corEl == 3){
                    if(sec == 1){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Uncorrected][Sector 1] is:
                        dp = ((-4.3303e-06)*phi*phi + (1.1006e-04)*phi + (-5.7235e-04))*pp*pp + ((3.2555e-05)*phi*phi + (-0.0014559)*phi + (0.0014878))*pp + ((-1.9577e-05)*phi*phi + (0.0017996)*phi + (0.025963));
                    }
                    if(sec == 2){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Uncorrected][Sector 2] is:
                        dp = ((-9.8045e-07)*phi*phi + (6.7395e-05)*phi + (-4.6757e-05))*pp*pp + ((-1.4958e-05)*phi*phi + (-0.0011191)*phi + (-0.0025143))*pp + ((1.2699e-04)*phi*phi + (0.0033121)*phi + (0.020819));
                    }
                    if(sec == 3){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Uncorrected][Sector 3] is:
                        dp = ((-5.9459e-07)*phi*phi + (-2.8289e-05)*phi + (-4.3541e-04))*pp*pp + ((-1.5025e-05)*phi*phi + (5.7730e-04)*phi + (-0.0077582))*pp + ((7.3348e-05)*phi*phi + (-0.001102)*phi + (0.057052));
                    }
                    if(sec == 4){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Uncorrected][Sector 4] is:
                        dp = ((-2.2714e-06)*phi*phi + (-3.0360e-05)*phi + (-8.9322e-04))*pp*pp + ((2.9737e-05)*phi*phi + (5.1142e-04)*phi + (0.0045641))*pp + ((-1.0582e-04)*phi*phi + (-5.6852e-04)*phi + (0.027506));
                    }
                    if(sec == 5){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Uncorrected][Sector 5] is:
                        dp = ((-1.1490e-06)*phi*phi + (-6.2147e-06)*phi + (-4.7235e-04))*pp*pp + ((3.7039e-06)*phi*phi + (-1.5943e-04)*phi + (-8.5238e-04))*pp + ((4.4069e-05)*phi*phi + (0.0014152)*phi + (0.031933));
                    }
                    if(sec == 6){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = Uncorrected][Sector 6] is:
                        dp = ((1.1076e-06)*phi*phi + (4.0156e-05)*phi + (-1.6341e-04))*pp*pp + ((-2.8613e-05)*phi*phi + (-5.1861e-04)*phi + (-0.0056437))*pp + ((1.2419e-04)*phi*phi + (4.9084e-04)*phi + (0.049976));
                    }
                }
                
                if(corEl == 4 || corEl == 5){ // Pass 2 Corrections (i.e., 'mmP2' and 'mmRP2')
                    if(sec == 1){
                        dp = (-4.3927e-04)*pp*pp + (5.8658e-04)*pp + (0.02801);
                    }
                    if(sec == 2){
                        dp = (4.8839e-04)*pp*pp + (-0.01132)*pp + (0.05124);
                    }
                    if(sec == 3){
                        dp = (3.3571e-04)*pp*pp + (-0.01172)*pp + (0.05763);
                    }
                    if(sec == 4){
                        dp = (1.0268e-04)*pp*pp + (-4.8374e-03)*pp + (0.0412);
                    }
                    if(sec == 5){
                        dp = (2.8250e-04)*pp*pp + (-7.9847e-03)*pp + (0.04232);
                    }
                    if(sec == 6){
                        dp = (1.3589e-04)*pp*pp + (-6.7704e-03)*pp + (0.03464);
                    }
                    
                    if(corEl == 5){ // Phi-dependent Refinement of Pass 2 Corrections
                        if(sec == 1){
                            // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmP2          (Pass 2 Correction)][Sector 1] is:
                            dp = dp +  ((1.0461e-07)*phi*phi +  (2.0228e-05)*phi +  (1.7357e-04))*pp*pp + ((-8.7646e-06)*phi*phi + (-3.9387e-04)*phi + (-5.4988e-04))*pp +  ((6.0164e-05)*phi*phi +   (0.0010708)*phi + (-0.0030032));
                            // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 1] is:
                            dp = dp + ((-6.4421e-07)*phi*phi + (-1.3073e-05)*phi + (-1.4102e-05))*pp*pp +  ((6.7547e-06)*phi*phi +  (1.0047e-04)*phi +  (3.1341e-04))*pp + ((-1.6767e-05)*phi*phi + (-2.0917e-04)*phi + (-0.0013211));
                        }
                        if(sec == 2){
                            // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmP2          (Pass 2 Correction)][Sector 2] is:
                            dp = dp + ((-7.3200e-07)*phi*phi +  (2.5209e-05)*phi + (-3.7645e-04))*pp*pp + ((-6.7578e-07)*phi*phi + (-5.1042e-04)*phi +   (0.0049163))*pp +  ((3.4087e-05)*phi*phi +   (0.0018198)*phi +  (-0.014044));
                            // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 2] is:
                            dp = dp + ((-7.4037e-07)*phi*phi + (-1.4694e-05)*phi + (-5.5340e-05))*pp*pp +  ((7.4548e-06)*phi*phi +  (1.2889e-04)*phi +  (6.2012e-04))*pp + ((-1.7841e-05)*phi*phi + (-2.6237e-04)*phi + (-0.0017847));
                        }
                        if(sec == 3){
                            // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmP2          (Pass 2 Correction)][Sector 3] is:
                            dp = dp + ((-4.3080e-08)*phi*phi +  (1.9303e-05)*phi + (-2.7301e-04))*pp*pp + ((-5.8015e-06)*phi*phi + (-1.8028e-04)*phi +   (0.0036556))*pp +  ((3.7849e-05)*phi*phi +  (4.8794e-04)*phi +  (-0.010733));
                            // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 3] is:
                            dp = dp + ((-7.7040e-07)*phi*phi +  (9.8938e-06)*phi + (-7.6219e-05))*pp*pp +  ((6.0610e-06)*phi*phi + (-8.0530e-05)*phi +   (0.0010106))*pp + ((-8.5135e-06)*phi*phi +  (1.5472e-04)*phi + (-0.0031448));
                        }
                        if(sec == 4){
                            // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmP2          (Pass 2 Correction)][Sector 4] is:
                            dp = dp + ((-4.1853e-07)*phi*phi +  (1.0473e-05)*phi + (-6.5274e-05))*pp*pp +  ((3.6816e-06)*phi*phi + (-1.5587e-05)*phi +  (7.6000e-04))*pp + ((-7.1764e-06)*phi*phi + (-1.5987e-04)*phi + (-0.0020378));
                            // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 4] is:
                            dp = dp + ((-3.2135e-07)*phi*phi +  (2.7994e-06)*phi +  (4.7069e-05))*pp*pp + ((-3.3353e-07)*phi*phi + (-1.2275e-05)*phi + (-4.2176e-04))*pp +  ((1.0466e-05)*phi*phi +  (2.0954e-05)*phi + (8.1115e-04));
                        }
                        if(sec == 5){
                            // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmP2          (Pass 2 Correction)][Sector 5] is:
                            dp = dp +  ((1.1760e-06)*phi*phi +  (2.9355e-05)*phi + (-2.1403e-04))*pp*pp + ((-1.8923e-05)*phi*phi + (-4.2933e-04)*phi +     (0.00421))*pp +  ((7.2838e-05)*phi*phi +   (0.0012461)*phi +  (-0.014348));
                            // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 5] is:
                            dp = dp + ((-1.5632e-06)*phi*phi + (-7.1527e-06)*phi +  (9.9895e-05))*pp*pp +  ((1.8332e-05)*phi*phi +  (5.5202e-05)*phi + (-0.0012584))*pp +  ((-5.1594e-05)*phi*phi + (-1.0622e-04)*phi +  (0.0036533));
                        }
                        if(sec == 6){
                            // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmP2          (Pass 2 Correction)][Sector 6] is:
                            dp = dp + ((-7.4655e-07)*phi*phi + (-3.2506e-05)*phi +  (3.0801e-04))*pp*pp +  ((3.7179e-07)*phi*phi +  (3.3195e-04)*phi +  (-0.0015145))*pp +  ((4.6216e-05)*phi*phi + (-7.6947e-04)*phi +  (-0.001801));
                            // The CONTINUOUS QUADRATIC function predicted for ∆p_{El} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 6] is:
                            dp = dp + ((-9.7434e-07)*phi*phi + (-6.4726e-06)*phi + (-6.1383e-05))*pp*pp +  ((1.1760e-05)*phi*phi +  (5.5914e-05)*phi +  (8.6014e-04))*pp + ((-3.4082e-05)*phi*phi + (-1.0690e-04)*phi + (-0.0027697));
                        }
                        
                    }
                    
                }
            }


            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //====================================================================================================================================//
            //======================//======================//     Electron Corrections (End)     //======================//======================//
            //====================================================================================================================================//
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //========================================================================================================================================================//
            //==============================//==============================//     π+ Corrections     //==============================//==============================//
            //========================================================================================================================================================//
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


            if(corPip != 0 && ivec == 1){
                if(sec == 1){
                    dp = ((-5.2e-07)*phi*phi + (-1.383e-05)*phi + (4.7179e-04))*pp*pp + ((8.33e-06)*phi*phi + (3.8849e-04)*phi + (-6.81319e-03))*pp + ((-1.645e-05)*phi*phi + (-5.0057e-04)*phi + (1.9902e-02));
                }
                if(sec == 2){
                    dp = ((-1.88e-06)*phi*phi + (3.303e-05)*phi + (1.1331e-03))*pp*pp + ((1.569e-05)*phi*phi + (-3.974e-05)*phi + (-1.25869e-02))*pp + ((-2.903e-05)*phi*phi + (-1.0638e-04)*phi + (2.61529e-02));
                }
                if(sec == 3){
                    dp = ((2.4e-07)*phi*phi + (-1.04e-05)*phi + (7.0864e-04))*pp*pp + ((8.0e-06)*phi*phi + (-5.156e-05)*phi + (-8.12169e-03))*pp  + ((-2.42e-05)*phi*phi + (8.928e-05)*phi + (2.13223e-02));
                }
                if(sec == 4){
                    dp = ((-4.0e-08)*phi*phi + (-3.59e-05)*phi + (1.32146e-03))*pp*pp + ((1.023e-05)*phi*phi + (2.2199e-04)*phi + (-1.33043e-02))*pp + ((-2.801e-05)*phi*phi + (-1.576e-04)*phi + (3.27995e-02));
                }
                if(sec == 5){
                    dp = ((2.7e-06)*phi*phi + (5.03e-06)*phi + (1.59668e-03))*pp*pp + ((-1.28e-05)*phi*phi + (-1.99e-06)*phi + (-1.71578e-02))*pp + ((2.091e-05)*phi*phi + (-4.14e-05)*phi + (3.25434e-02));
                }
                if(sec == 6){
                    dp = ((2.13e-06)*phi*phi + (-7.49e-05)*phi + (1.75565e-03))*pp*pp + ((-7.37e-06)*phi*phi + (5.8222e-04)*phi + (-1.27969e-02))*pp + ((4.9e-07)*phi*phi + (-7.2253e-04)*phi + (3.11499e-02));
                }
                
                
                if(corPip == 2 || corPip == 3){
                    if(sec == 1){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (Uncorrected Pion - With Elastic)][Sector 1] is:
                        dp = ((-5.4904e-07)*phi*phi + (-1.4436e-05)*phi + (3.1534e-04))*pp*pp + ((3.8231e-06)*phi*phi + (3.6582e-04)*phi + (-0.0046759))*pp + ((-5.4913e-06)*phi*phi + (-4.0157e-04)*phi + (0.010767));
                        
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (With (New) Pion - With Elastic)][Sector 1] is:
                        dp = dp + ((6.1103e-07)*phi*phi + (5.5291e-06)*phi + (-1.9120e-04))*pp*pp + ((-3.2300e-06)*phi*phi + (1.5377e-05)*phi + (7.5279e-04))*pp + ((2.1434e-06)*phi*phi + (-6.9572e-06)*phi + (-7.9333e-05));
                        dp = dp + ((-1.3049e-06)*phi*phi + (1.1295e-05)*phi + (4.5797e-04))*pp*pp + ((9.3122e-06)*phi*phi + (-5.1074e-05)*phi + (-0.0030757))*pp + ((-1.3102e-05)*phi*phi + (2.2153e-05)*phi + (0.0040938));
                    }
                    if(sec == 2){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (Uncorrected Pion - With Elastic)][Sector 2] is:
                        dp = ((-1.0087e-06)*phi*phi + (2.1319e-05)*phi + (7.8641e-04))*pp*pp + ((6.7485e-06)*phi*phi + (7.3716e-05)*phi + (-0.0094591))*pp + ((-1.1820e-05)*phi*phi + (-3.8103e-04)*phi + (0.018936));
                        
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (With (New) Pion - With Elastic)][Sector 2] is:
                        dp = dp + ((8.8155e-07)*phi*phi + (-2.8257e-06)*phi + (-2.6729e-04))*pp*pp + ((-5.4499e-06)*phi*phi + (3.8397e-05)*phi + (0.0015914))*pp + ((6.8926e-06)*phi*phi + (-5.9386e-05)*phi + (-0.0021749));
                        dp = dp + ((-2.0147e-07)*phi*phi + (1.1061e-05)*phi + (3.8827e-04))*pp*pp + ((4.9294e-07)*phi*phi + (-6.0257e-05)*phi + (-0.0022087))*pp + ((9.8548e-07)*phi*phi + (5.9047e-05)*phi + (0.0022905));
                    }
                    if(sec == 3){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (Uncorrected Pion - With Elastic)][Sector 3] is:
                        dp = ((8.6722e-08)*phi*phi + (-1.7975e-05)*phi + (4.8118e-05))*pp*pp + ((2.6273e-06)*phi*phi + (3.1453e-05)*phi + (-0.0015943))*pp + ((-6.4463e-06)*phi*phi + (-5.8990e-05)*phi + (0.0041703));
                        
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (With (New) Pion - With Elastic)][Sector 3] is:
                        dp = dp + ((9.6317e-07)*phi*phi + (-1.7659e-06)*phi + (-8.8318e-05))*pp*pp + ((-5.1346e-06)*phi*phi + (8.3318e-06)*phi + (3.7723e-04))*pp + ((3.9548e-06)*phi*phi + (-6.9614e-05)*phi + (2.1393e-04));
                        dp = dp + ((5.6438e-07)*phi*phi + (8.1678e-06)*phi + (-9.4406e-05))*pp*pp + ((-3.9074e-06)*phi*phi + (-6.5174e-05)*phi + (5.4218e-04))*pp + ((6.3198e-06)*phi*phi + (1.0611e-04)*phi + (-4.5749e-04));
                    }
                    if(sec == 4){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (Uncorrected Pion - With Elastic)][Sector 4] is:
                        dp = ((4.3406e-07)*phi*phi + (-4.9036e-06)*phi + (2.3064e-04))*pp*pp + ((1.3624e-06)*phi*phi + (3.2907e-05)*phi + (-0.0034872))*pp + ((-5.1017e-06)*phi*phi + (2.4593e-05)*phi + (0.0092479));
                        
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (With (New) Pion - With Elastic)][Sector 4] is:
                        dp = dp + ((6.0218e-07)*phi*phi + (-1.4383e-05)*phi + (-3.1999e-05))*pp*pp + ((-1.1243e-06)*phi*phi + (9.3884e-05)*phi + (-4.1985e-04))*pp + ((-1.8808e-06)*phi*phi + (-1.2222e-04)*phi + (0.0014037));
                        dp = dp + ((-2.5490e-07)*phi*phi + (-8.5120e-07)*phi + (7.9109e-05))*pp*pp + ((2.5879e-06)*phi*phi + (8.6108e-06)*phi + (-5.1533e-04))*pp + ((-4.4521e-06)*phi*phi + (-1.7012e-05)*phi + (7.4848e-04));
                    }
                    if(sec == 5){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (Uncorrected Pion - With Elastic)][Sector 5] is:
                        dp = ((2.4292e-07)*phi*phi + (8.8741e-06)*phi + (2.9482e-04))*pp*pp + ((3.7229e-06)*phi*phi + (7.3215e-06)*phi + (-0.0050685))*pp + ((-1.1974e-05)*phi*phi + (-1.3043e-04)*phi + (0.0078836));
                        
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (With (New) Pion - With Elastic)][Sector 5] is:
                        dp = dp + ((1.0867e-06)*phi*phi + (-7.7630e-07)*phi + (-4.4930e-05))*pp*pp + ((-5.6564e-06)*phi*phi + (-1.3417e-05)*phi + (2.5224e-04))*pp + ((6.8460e-06)*phi*phi + (9.0495e-05)*phi + (-4.6587e-04));
                        dp = dp + ((8.5720e-07)*phi*phi + (-6.7464e-06)*phi + (-4.0944e-05))*pp*pp + ((-4.7370e-06)*phi*phi + (5.8808e-05)*phi + (1.9047e-04))*pp + ((5.7404e-06)*phi*phi + (-1.1105e-04)*phi + (-1.9392e-04));
                    }
                    if(sec == 6){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (Uncorrected Pion - With Elastic)][Sector 6] is:
                        dp = ((2.1191e-06)*phi*phi + (-3.3710e-05)*phi + (2.5741e-04))*pp*pp + ((-1.2915e-05)*phi*phi + (2.3753e-04)*phi + (-2.6882e-04))*pp + ((2.2676e-05)*phi*phi + (-2.3115e-04)*phi + (-0.001283));
                        
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = Corrected (With (New) Pion - With Elastic)][Sector 6] is:
                        dp = dp + ((6.0270e-07)*phi*phi + (-6.8200e-06)*phi + (1.3103e-04))*pp*pp + ((-1.8745e-06)*phi*phi + (3.8646e-05)*phi + (-8.8056e-04))*pp + ((2.0885e-06)*phi*phi + (-3.4932e-05)*phi + (4.5895e-04));
                        dp = dp + ((4.7349e-08)*phi*phi + (-5.7528e-06)*phi + (-3.4097e-06))*pp*pp + ((1.7731e-06)*phi*phi + (3.5865e-05)*phi + (-5.7881e-04))*pp + ((-9.7008e-06)*phi*phi + (-4.1836e-05)*phi + (0.0035403));
                    }
                }
                
                
                if(corPip == 4 || corPip == 5){ // Corresponds to Correction = mmRP2_PipMMP2 or Correction = mmRP2_PipMMsP2
                    if(sec == 1){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 1] is:
                        dp =       ((2.3162e-07)*phi*phi +  (1.0037e-04)*phi + (6.3605e-04))*pp*pp +  ((2.5189e-06)*phi*phi + (-6.8325e-04)*phi + (-0.0073536))*pp + ((-4.8953e-06)*phi*phi +  (3.7776e-04)*phi + (0.017481));
                    }
                    if(sec == 2){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 2] is:
                        dp =       ((2.6856e-06)*phi*phi +  (7.3145e-05)*phi +  (0.0011107))*pp*pp + ((-1.7339e-05)*phi*phi + (-4.6609e-04)*phi +   (-0.01069))*pp +  ((1.9965e-05)*phi*phi +  (2.0460e-06)*phi + (0.017721));
                    }
                    if(sec == 3){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 3] is:
                        dp =       ((1.4348e-07)*phi*phi + (-6.0459e-05)*phi +  (0.0010993))*pp*pp + ((-2.9584e-07)*phi*phi +  (4.3780e-04)*phi +  (-0.010494))*pp +  ((4.7522e-06)*phi*phi + (-3.0397e-04)*phi + (0.011763));
                    }
                    if(sec == 4){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 4] is:
                        dp =       ((7.6182e-07)*phi*phi + (-2.4537e-05)*phi + (7.4374e-04))*pp*pp + ((-3.5117e-06)*phi*phi +  (1.6932e-04)*phi + (-0.0072707))*pp +  ((6.3642e-06)*phi*phi + (-1.1886e-04)*phi + (0.014928));
                    }
                    if(sec == 5){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 5] is:
                        dp =       ((3.4726e-07)*phi*phi + (-2.5325e-06)*phi +  (0.0012672))*pp*pp + ((-2.2847e-08)*phi*phi +  (2.9380e-05)*phi +  (-0.010917))*pp +  ((3.3013e-06)*phi*phi + (-1.0943e-04)*phi + (0.014334));
                    }
                    if(sec == 6){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2 (Refined Pass 2 Correction)][Sector 6] is:
                        dp =       ((2.7008e-08)*phi*phi +  (7.9373e-06)*phi +  (0.0011934))*pp*pp + ((-6.2218e-08)*phi*phi + (-8.2899e-05)*phi + (-0.0097092))*pp +  ((1.1058e-05)*phi*phi + (-1.1152e-05)*phi + (0.0097068));
                    }
                    
                    // Refinements made to this correction (kept the same name)
                    // Refinements were made with the file: Single_Pion_Channel_epipX_Inbending_With_Dp_Spring_2019_Pass_2_rec_clas_V4_File_All.root
                        // The refinements were created on 10/5/2023 (for V5)
                    if(sec == 1){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 1] is:
                        dp = dp +  ((8.4176e-07)*phi*phi +  (1.2005e-05)*phi + (-1.6620e-04))*pp*pp + ((-5.4513e-06)*phi*phi + (-9.3949e-05)*phi +   (0.0012257))*pp +  ((8.6315e-06)*phi*phi +  (1.1832e-04)*phi + (-0.0018008));
                    }
                    if(sec == 2){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 2] is:
                        dp = dp +  ((2.8775e-07)*phi*phi +  (3.6807e-06)*phi +  (2.1783e-05))*pp*pp + ((-1.3163e-06)*phi*phi + (-4.5873e-05)*phi + (-4.1510e-04))*pp +  ((1.6431e-06)*phi*phi +  (9.8938e-05)*phi +  (0.0012463));
                    }
                    if(sec == 3){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 3] is:
                        dp = dp +  ((5.3417e-08)*phi*phi + (-6.9131e-06)*phi +  (4.6364e-05))*pp*pp +  ((1.6226e-07)*phi*phi +  (5.9662e-05)*phi + (-3.8155e-04))*pp +  ((4.8169e-07)*phi*phi + (-8.2344e-05)*phi +  (2.5891e-04));
                    }
                    if(sec == 4){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 4] is:
                        dp = dp + ((-2.1283e-07)*phi*phi +  (6.3134e-06)*phi +  (4.8988e-06))*pp*pp +  ((2.4374e-06)*phi*phi + (-4.4217e-05)*phi + (-1.6725e-04))*pp + ((-4.4455e-06)*phi*phi +  (6.8315e-05)*phi +  (3.5471e-04));
                    }
                    if(sec == 5){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 5] is:
                        dp = dp +  ((6.0902e-07)*phi*phi +  (1.1325e-06)*phi + (-1.0441e-04))*pp*pp + ((-3.7002e-06)*phi*phi + (-8.4353e-06)*phi +  (7.3170e-04))*pp +  ((6.0250e-06)*phi*phi + (-1.6914e-06)*phi + (-0.0013206));
                    }
                    if(sec == 6){
                        // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 6] is:
                        dp = dp +  ((5.5947e-07)*phi*phi + (-4.3539e-06)*phi + (-1.0766e-04))*pp*pp + ((-4.3709e-06)*phi*phi +  (2.9333e-05)*phi +  (9.7093e-04))*pp +  ((9.2126e-06)*phi*phi + (-5.9750e-05)*phi + (-0.0019547));
                    }
                    
                    
                    if(corPip == 5){ // Corresponds to Correction = mmRP2_PipMMsP2
                        // Correction is split based on whether the momentum is greater than 4 GeV or less than 4 GeV
                        if(pp >= 4){
                            if(sec == 1){
                                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 1] is:
                                dp = dp + ((-7.2027e-06)*phi*phi + (-9.6557e-05)*phi + (-6.8172e-04))*pp*pp + ((8.6596e-05)*phi*phi + (9.5750e-04)*phi + (0.0034343))*pp + ((-2.5537e-04)*phi*phi + (-0.0022122)*phi + (0.0048584));
                            }
                            if(sec == 2){
                                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 2] is:
                                dp = dp + ((-1.1001e-05)*phi*phi + (-1.2434e-04)*phi + (-0.0023145))*pp*pp + ((1.2473e-04)*phi*phi + (0.0012392)*phi + (0.0224))*pp + ((-3.5197e-04)*phi*phi + (-0.0028099)*phi + (-0.048264));
                            }
                            if(sec == 3){
                                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 3] is:
                                dp = dp + ((-2.1964e-06)*phi*phi + (9.1340e-07)*phi + (-0.002515))*pp*pp + ((2.8086e-05)*phi*phi + (6.5217e-05)*phi + (0.023951))*pp + ((-8.9256e-05)*phi*phi + (-4.2422e-04)*phi + (-0.050746));
                            }
                            if(sec == 4){
                                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 4] is:
                                dp = dp + ((-3.7147e-06)*phi*phi + (7.7026e-05)*phi + (-0.0018494))*pp*pp + ((4.7613e-05)*phi*phi + (-8.8878e-04)*phi + (0.01796))*pp + ((-1.4740e-04)*phi*phi + (0.0024937)*phi + (-0.039466));
                            }
                            if(sec == 5){
                                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 5] is:
                                dp = dp + ((5.4313e-06)*phi*phi + (-3.1710e-05)*phi + (-0.0036724))*pp*pp + ((-5.9298e-05)*phi*phi + (4.1536e-04)*phi + (0.037361))*pp + ((1.5828e-04)*phi*phi + (-0.0013508)*phi + (-0.089146));
                            }
                            if(sec == 6){
                                // The CONTINUOUS QUADRATIC function predicted for ∆p_{#pi^{+}} for [Cor = mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)][Sector 6] is:
                                dp = dp + ((2.4524e-07)*phi*phi + (-1.1842e-04)*phi + (-0.0039563))*pp*pp + ((-1.0923e-06)*phi*phi + (0.001264)*phi + (0.040802))*pp + ((-1.3884e-06)*phi*phi + (-0.0032696)*phi + (-0.09893));
                            }
                        }
                    }
                    
                }

            }


            //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //==============================================================================================================================================================//
            //==============================//==============================//     π+ Corrections (End)     //==============================//==============================//
            //==============================================================================================================================================================//
            //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //========================================================================================================================================================//
            //==============================//==============================//     π- Corrections     //==============================//==============================//
            //========================================================================================================================================================//
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


            if(corPim != 0 && ivec == 2){

                if(sec == 1){
                    dp = ((-4.0192658422317425e-06)*phi*phi - (2.660222128967742e-05)*phi + 0.004774434682983547)*pp*pp;
                    dp = dp + ((1.9549520962477972e-05)*phi*phi - 0.0002456062756770577*phi - 0.03787692408323466)*pp; 
                    dp = dp + (-2.128953094937459e-05)*phi*phi + 0.0002461708852239913*phi + 0.08060704449822174 - 0.01;
                }

                if(sec == 2){
                    dp = ((1.193010521758372e-05)*phi*phi - (5.996221756031922e-05)*phi + 0.0009093437955814359)*pp*pp;
                    dp = dp + ((-4.89113824430594e-05)*phi*phi + 0.00021676479488147118*phi - 0.01861892053916726)*pp;  
                    dp = dp + (4.446394152208071e-05)*phi*phi - (3.6592784167335244e-05)*phi + 0.05498710249944096 - 0.01;
                }

                if(sec == 3){
                    dp = ((-1.6596664895992133e-07)*phi*phi + (6.317189710683516e-05)*phi + 0.0016364212312654086)*pp*pp;
                    dp = dp + ((-2.898409777520318e-07)*phi*phi - 0.00014531513577533802*phi - 0.025456145839203827)*pp;  
                    dp = dp + (2.6432552410603506e-06)*phi*phi + 0.00018447151306275443*phi + 0.06442602664627255 - 0.01;
                }

                if(sec == 4){
                    dp = ((2.4035259647558634e-07)*phi*phi - (8.649647351491232e-06)*phi + 0.004558993439848128)*pp*pp;
                    dp = dp + ((-5.981498144060984e-06)*phi*phi + 0.00010582131454222416*phi - 0.033572004651981686)*pp;  
                    dp = dp + (8.70140266889548e-06)*phi*phi - 0.00020137414379966883*phi + 0.07258774523336173 - 0.01;   
                }

                if(sec == 5){
                    dp = ((2.5817024702834863e-06)*phi*phi + 0.00010132810066914441*phi + 0.003397314538804711)*pp*pp;
                    dp = dp + ((-1.5116941263931812e-05)*phi*phi - 0.00040679799541839254*phi - 0.028144285760769876)*pp;  
                    dp = dp + (1.4701931057951464e-05)*phi*phi + 0.0002426350390593454*phi + 0.06781682510174941 - 0.01;
                }

                if(sec == 6){
                    dp = ((-8.196823669099362e-07)*phi*phi - (5.280412421933636e-05)*phi + 0.0018457238328451137)*pp*pp;
                    dp = dp + ((5.2675062282094536e-06)*phi*phi + 0.0001515803461044587*phi - 0.02294371578470564)*pp;  
                    dp = dp + (-9.459454671739747e-06)*phi*phi - 0.0002389523716779765*phi + 0.06428970810739926 - 0.01;
                }

            }


            //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //==============================================================================================================================================================//
            //==============================//==============================//     π- Corrections (End)     //==============================//==============================//
            //==============================================================================================================================================================//
            //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            
            
            
            

            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //================================================================================================================================================================//
            //==============================//==============================//     All Proton Corrections     //==============================//==============================//
            //================================================================================================================================================================//
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

            if(corPro != 0 && ivec == 3){
            
                if(corPro == 1){ // Quadratic Momentum - No Phi Dependence

                    if(sec == 1){
                        dp = (5.415e-04)*pp*pp + (-1.0262e-02)*pp + (7.78075e-03);
                        // From GitHub_F_Pro for GitHub_F2_Pro:
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
                        dp = dp + ((1.2129e-04)*pp*pp + (1.5373e-04)*pp + (-2.7084e-04));
                    }

                    if(sec == 2){
                        dp = (-9.5439e-04)*pp*pp + (-2.86273e-03)*pp + (3.38149e-03);
                        // From GitHub_F_Pro for GitHub_F2_Pro:
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
                        dp = dp + ((-1.6890e-03)*pp*pp + (4.3744e-03)*pp + (-2.1218e-03));
                    }

                    if(sec == 3){
                        dp = (-5.5541e-04)*pp*pp + (-7.69739e-03)*pp + (5.7692e-03);
                        // From GitHub_F_Pro for GitHub_F2_Pro:
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
                        dp = dp + ((7.6422e-04)*pp*pp + (-1.5425e-03)*pp + (5.4255e-04));
                    }

                    if(sec == 4){
                        dp = (-1.944e-04)*pp*pp + (-5.77104e-03)*pp + (3.42399e-03);
                        // From GitHub_F_Pro for GitHub_F2_Pro:
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
                        dp = dp + ((1.1174e-03)*pp*pp + (-3.2747e-03)*pp + (2.3687e-03));
                    }

                    if(sec == 5){
                        dp = (1.54009e-03)*pp*pp + (-1.69437e-02)*pp + (1.04656e-02);
                        // From GitHub_F_Pro for GitHub_F2_Pro:
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
                        dp = dp + ((-2.1067e-04)*pp*pp + (1.2266e-03)*pp + (-1.0553e-03));
                    }

                    if(sec == 6){
                        dp = (2.38182e-03)*pp*pp + (-2.07301e-02)*pp + (1.72325e-02);
                        // From GitHub_F_Pro for GitHub_F2_Pro:
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
                        dp = dp + ((-3.6002e-04)*pp*pp + (8.9582e-04)*pp + (-1.0093e-03));
                    }
                }
                
                
                if(corPro == 2){ // Quadratic Momentum - No Phi Dependence - With Elastic
                    if(sec == 1){
                        // // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 1][regall] is:
                        // dp = ((2.4366e-03)*pp*pp + (-0.01419)*pp + (0.01118));
                        
                        // Using consistent momentum bins of 0.25 GeV per slice:
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 1][regall] is:
                        dp = ((7.0897e-03)*pp*pp + (-0.03199)*pp + (0.02237));
                        
                        
                        // Refined with a limited π0 Channel Contributions (up to Pro = 0.95 GeV - The double pion channel's range is from 0.45 to 3.1 GeV)
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_EF][Sector 1][regall] is:
                        dp = dp + ((-0.0111)*pp*pp + (0.04398)*pp + (-0.0309));
                        
                        
                    }
                    if(sec == 2){
                        // // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 2][regall] is:
                        // dp = ((4.4524e-03)*pp*pp + (-0.01943)*pp + (0.01409));
                        
                        // Using consistent momentum bins of 0.25 GeV per slice:
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 2][regall] is:
                        dp = ((5.3849e-03)*pp*pp + (-0.02474)*pp + (0.01933));
                        
                        
                        // Refined with a limited π0 Channel Contributions (up to Pro = 0.95 GeV - The double pion channel's range is from 0.45 to 3.1 GeV)
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_EF][Sector 2][regall] is:
                        dp = dp + ((-8.3180e-03)*pp*pp + (0.03359)*pp + (-0.0251));
                        
                        
                    }
                    if(sec == 3){
                        // // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 3][regall] is:
                        // dp = ((6.2503e-03)*pp*pp + (-0.02598)*pp + (0.0168));
                        
                        // Using consistent momentum bins of 0.25 GeV per slice:
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 3][regall] is:
                        dp = ((0.01095)*pp*pp + (-0.04196)*pp + (0.02795));
                        
                        
                        // Refined with a limited π0 Channel Contributions (up to Pro = 0.95 GeV - The double pion channel's range is from 0.45 to 3.1 GeV)
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_EF][Sector 3][regall] is:
                        dp = dp + ((-0.01892)*pp*pp + (0.06574)*pp + (-0.04358));
                        
                        
                    }
                    if(sec == 4){
                        // // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 4][regall] is:
                        // dp = ((2.4303e-03)*pp*pp + (-0.01241)*pp + (8.5029e-03));
                        
                        // Using consistent momentum bins of 0.25 GeV per slice:
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 4][regall] is:
                        dp = ((0.01038)*pp*pp + (-0.04012)*pp + (0.02781));
                        
                        
                        // Refined with a limited π0 Channel Contributions (up to Pro = 0.95 GeV - The double pion channel's range is from 0.45 to 3.1 GeV)
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_EF][Sector 4][regall] is:
                        dp = dp + ((-0.0147)*pp*pp + (0.05475)*pp + (-0.03912));
                        
                        
                    }
                    if(sec == 5){
                        // // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 5][regall] is:
                        // dp = ((4.4340e-03)*pp*pp + (-0.02506)*pp + (0.01697));
                        
                        // Using consistent momentum bins of 0.25 GeV per slice:
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 5][regall] is:
                        dp = ((9.0227e-03)*pp*pp + (-0.04131)*pp + (0.02748));
                        
                        
                        // Refined with a limited π0 Channel Contributions (up to Pro = 0.95 GeV - The double pion channel's range is from 0.45 to 3.1 GeV)
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_EF][Sector 5][regall] is:
                        dp = dp + ((-0.01526)*pp*pp + (0.05599)*pp + (-0.03795));
                        
                        
                    }
                    if(sec == 6){
                        // // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 6][regall] is:
                        // dp = ((5.5915e-03)*pp*pp + (-0.02814)*pp + (0.02144));
                        
                        // Using consistent momentum bins of 0.25 GeV per slice:
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = Corrected - New][Sector 6][regall] is:
                        dp = ((8.8531e-03)*pp*pp + (-0.03881)*pp + (0.0284));
                        
                        
                        // Refined with a limited π0 Channel Contributions (up to Pro = 0.95 GeV - The double pion channel's range is from 0.45 to 3.1 GeV)
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_EF][Sector 6][regall] is:
                        dp = dp + ((-0.01037)*pp*pp + (0.0386)*pp + (-0.0256));
                        
                        
                    }
                }
                

                if(corPro == 3){ // (Double) Quadratic Momentum - No Phi Dependence - With Elastic
                    if(sec == 1){
                        dp = ((1 + TMath::Sign(1, -(pp - 1.4)))/2)*((-0.0959)*pp*pp + (0.18948)*pp + (-0.08328)) + ((1 + TMath::Sign(1, (pp - 1.4)))/2)*((0.01991)*(pp - 1.4)*(pp - 1.4) + (-0.01963)*(pp - 1.4) + ((-0.0959)*1.4*1.4 + (0.18948)*1.4 + (-0.0959)));
                    }
                    if(sec == 2){
                        dp = ((1 + TMath::Sign(1, -(pp - 1.5)))/2)*((-0.06642)*pp*pp + (0.14583)*pp + (-0.06885)) + ((1 + TMath::Sign(1, (pp - 1.5)))/2)*((0.07575)*(pp - 1.5)*(pp - 1.5) + (-0.07001)*(pp - 1.5) + ((-0.06642)*1.5*1.5 + (0.14583)*1.5 + (-0.06642)));
                    }
                    if(sec == 3){
                        dp = ((1 + TMath::Sign(1, -(pp - 1.05)))/2)*((-0.14588)*pp*pp + (0.26771)*pp + (-0.11513)) + ((1 + TMath::Sign(1, (pp - 1.05)))/2)*((0.03042)*(pp - 1.05)*(pp - 1.05) + (-0.04788)*(pp - 1.05) + ((-0.14588)*1.05*1.05 + (0.26771)*1.05 + (-0.14588)));
                    }
                    if(sec == 4){
                        dp = ((1 + TMath::Sign(1, -(pp - 1.4)))/2)*((-0.09563)*pp*pp + (0.19039)*pp + (-0.08607)) + ((1 + TMath::Sign(1, (pp - 1.4)))/2)*((-7.7622e-03)*(pp - 1.4)*(pp - 1.4) + (7.6980e-03)*(pp - 1.4) + ((-0.09563)*1.4*1.4 + (0.19039)*1.4 + (-0.09563)));
                    }
                    if(sec == 5){
                        dp = ((1 + TMath::Sign(1, -(pp - 1.5)))/2)*((-0.09331)*pp*pp + (0.19028)*pp + (-0.08766)) + ((1 + TMath::Sign(1, (pp - 1.5)))/2)*((5.7742e-03)*(pp - 1.5)*(pp - 1.5) + (1.2433e-03)*(pp - 1.5) + ((-0.09331)*1.5*1.5 + (0.19028)*1.5 + (-0.09331)));
                    }
                    if(sec == 6){
                        dp = ((1 + TMath::Sign(1, -(pp - 1.15)))/2)*((-0.12326)*pp*pp + (0.22076)*pp + (-0.09082)) + ((1 + TMath::Sign(1, (pp - 1.15)))/2)*((2.7284e-03)*(pp - 1.15)*(pp - 1.15) + (-0.01129)*(pp - 1.15) + ((-0.12326)*1.15*1.15 + (0.22076)*1.15 + (-0.12326)));
                    }
                }
                
                
                if(corPro == 4 || corPro == 6){ // Linear + Quadratic Momentum - No Phi Dependence - With Elastic (Used modified slices - i.e., each momentum bin was not identically sized to increase precision where statistics allowed)
                    if(sec == 1){
                        // // Created for V12 (Not a refinement but came from V10 as of 12-17-2022)
                        // dp = ((1 + TMath::Sign(1, (pp - 1.4)))/2)*((7.1549e-03)*pp + (-0.01676)) + ((1 + TMath::Sign(1, -(pp - 1.4)))/2)*((-0.13101)*(pp - 1.4)*(pp - 1.4) + (-0.10988)*(pp - 1.4) + ((7.1549e-03)*1.4 + (-0.01676)));
                        
                        // Created for V14 (As of 12-20-2022)
                        dp = ((1 + TMath::Sign(1, (pp - 1.4)))/2)*((4.4034e-03)*pp + (-0.01703)) + ((1 + TMath::Sign(1, -(pp - 1.4)))/2)*((-0.10898)*(pp - 1.4)*(pp - 1.4) + (-0.09574)*(pp - 1.4) + ((4.4034e-03)*1.4 + (-0.01703)));
                        
                    }
                    if(sec == 2){
                        // // Created for V12 (Not a refinement but came from V10 as of 12-17-2022)
                        // dp = ((1 + TMath::Sign(1, (pp - 1.5)))/2)*((-1.8045e-03)*pp + (-6.1883e-04)) + ((1 + TMath::Sign(1, -(pp - 1.5)))/2)*((-0.06692)*(pp - 1.5)*(pp - 1.5) + (-0.06165)*(pp - 1.5) + ((-1.8045e-03)*1.5 + (-6.1883e-04)));
                        
                        // Created for V14 (As of 12-20-2022)
                        dp = ((1 + TMath::Sign(1, (pp - 1.5)))/2)*((0.01318)*pp + (-0.03403)) + ((1 + TMath::Sign(1, -(pp - 1.5)))/2)*((-0.09829)*(pp - 1.5)*(pp - 1.5) + (-0.0986)*(pp - 1.5) + ((0.01318)*1.5 + (-0.03403)));

                    }
                    if(sec == 3){
                        // // Created for V12 (Not a refinement but came from V10 as of 12-17-2022)
                        // dp = ((1 + TMath::Sign(1, (pp - 1.05)))/2)*((-9.1530e-03)*pp + (0.01321)) + ((1 + TMath::Sign(1, -(pp - 1.05)))/2)*((-0.14416)*(pp - 1.05)*(pp - 1.05) + (-0.04263)*(pp - 1.05) + ((-9.1530e-03)*1.05 + (0.01321)));
                        
                        // Created for V14 (As of 12-20-2022)
                        dp = ((1 + TMath::Sign(1, (pp - 1.05)))/2)*((-4.7052e-03)*pp + (1.2410e-03)) + ((1 + TMath::Sign(1, -(pp - 1.05)))/2)*((-0.22721)*(pp - 1.05)*(pp - 1.05) + (-0.09702)*(pp - 1.05) + ((-4.7052e-03)*1.05 + (1.2410e-03)));

                    }
                    if(sec == 4){
                        // // Created for V12 (Not a refinement but came from V10 as of 12-17-2022)
                        // dp = ((1 + TMath::Sign(1, (pp - 1.4)))/2)*((-1.4632e-03)*pp + (5.9780e-04)) + ((1 + TMath::Sign(1, -(pp - 1.4)))/2)*((-0.08698)*(pp - 1.4)*(pp - 1.4) + (-0.06322)*(pp - 1.4) + ((-1.4632e-03)*1.4 + (5.9780e-04)));
                        
                        // Created for V14 (As of 12-20-2022)
                        dp = ((1 + TMath::Sign(1, (pp - 1.4)))/2)*((-1.0900e-03)*pp + (-4.0573e-03)) + ((1 + TMath::Sign(1, -(pp - 1.4)))/2)*((-0.09236)*(pp - 1.4)*(pp - 1.4) + (-0.073)*(pp - 1.4) + ((-1.0900e-03)*1.4 + (-4.0573e-03)));

                    }
                    if(sec == 5){
                        // // Created for V12 (Not a refinement but came from V10 as of 12-17-2022)
                        // dp = ((1 + TMath::Sign(1, (pp - 1.5)))/2)*((5.2396e-03)*pp + (-0.02372)) + ((1 + TMath::Sign(1, -(pp - 1.5)))/2)*((-0.10822)*(pp - 1.5)*(pp - 1.5) + (-0.10736)*(pp - 1.5) + ((5.2396e-03)*1.5 + (-0.02372)));
                        
                        // Created for V14 (As of 12-20-2022)
                        dp = ((1 + TMath::Sign(1, (pp - 1.5)))/2)*((7.3965e-03)*pp + (-0.02428)) + ((1 + TMath::Sign(1, -(pp - 1.5)))/2)*((-0.09539)*(pp - 1.5)*(pp - 1.5) + (-0.09263)*(pp - 1.5) + ((7.3965e-03)*1.5 + (-0.02428)));

                    }
                    if(sec == 6){
                        // // Created for V12 (Not a refinement but came from V10 as of 12-17-2022)
                        // dp = ((1 + TMath::Sign(1, (pp - 1.15)))/2)*((-7.5813e-03)*pp + (7.1798e-03)) + ((1 + TMath::Sign(1, -(pp - 1.15)))/2)*((-0.11408)*(pp - 1.15)*(pp - 1.15) + (-0.06441)*(pp - 1.15) + ((-7.5813e-03)*1.15 + (7.1798e-03)));
                        
                        // Created for V14 (As of 12-20-2022)
                        dp = ((1 + TMath::Sign(1, (pp - 1.15)))/2)*((-7.6214e-03)*pp + (8.1014e-03)) + ((1 + TMath::Sign(1, -(pp - 1.15)))/2)*((-0.12718)*(pp - 1.15)*(pp - 1.15) + (-0.06626)*(pp - 1.15) + ((-7.6214e-03)*1.15 + (8.1014e-03)));

                    }
                    
                    if(corPro == 6){
                        if(sec == 1){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.01209);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.0011625);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.0020235);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (1.3822e-10);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (6.1986e-12);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (0.001171);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (0.0029328);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-6.9294e-11);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-9.5240e-04);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-0.0098873);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-0.0038452);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (0.01);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (0.0032361);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (4.7611e-04);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.005);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (0.0032169);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (0.01);
                            }
                        }
                        if(sec == 2){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.0073511);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.0020223);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.0021045);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (1.0004e-10);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (1.6017e-11);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (1.6347e-04);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.0020222);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-0.0087368);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.0010099);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-1.9094e-09);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-2.0578e-09);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-0.01);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (0.01);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.0045736);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.005);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (-0.0034818);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (0.006159);
                            }
                        }
                        if(sec == 3){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.0026713);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.0025998);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.0035644);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.0055165);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.0062494);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.0045474);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.0010856);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (9.7786e-04);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (0.0073733);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (0.01);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (0.019838);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-0.0019305);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (3.0760e-12);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.0099999);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.005);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (0.01);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (0.0099999);
                            }
                        }
                        if(sec == 4){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-5.9369e-11);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.0026745);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.0025888);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (5.6656e-13);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.0034908);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.0016047);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.0015552);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-0.0010852);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-1.1536e-10);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (0.0043639);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-2.0560e-10);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-2.4232e-11);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (-0.0028999);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (-0.01);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.011888);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (0.01);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (1.3244e-10);
                            }
                        }
                        if(sec == 5){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.0014647);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-8.9216e-04);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (9.5401e-12);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (1.7695e-13);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.0018382);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.0019182);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.0045879);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-2.4413e-13);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (0.0072663);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-4.5738e-09);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-0.0097207);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-4.8651e-12);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (0.0013099);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (-0.0042066);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.005);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (-9.6964e-11);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (-0.0053576);
                            }
                        }
                        if(sec == 6){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.0067183);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (0.0010457);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.0019828);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (0.0015115);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (3.2544e-04);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (2.6222e-10);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (3.4673e-05);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-0.0064244);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.0060716);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (1.9671e-08);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (8.6804e-04);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-0.0039438);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (3.1952e-10);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.0074829);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.012681);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (-0.01);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (8.9608e-12);
                            }
                        }
                    }
                    
                }
                
                
                if(corPro == 5){ // Quadratic Momentum - Limited π0 Channel Contributions (up to Pro = 0.95 GeV - The double pion channel's range is from 0.45 to 3.1 GeV)
                    if(sec == 1){                        
                        // No Pi0 Channel
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF][Sector 1][regall] is:
                        dp = ((-0.016)*pp*pp + (0.04367)*pp + (-0.02515));
                        
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_REF][Sector 1][regall] is:
                        dp = dp + ((5.1479e-03)*pp*pp + (-0.01511)*pp + (7.8694e-03));
                        
                        // // Refined for V11 (on 12-16-2022)
                        // dp = dp + ((1 + TMath::Sign(1, -(pp - 1.275)))/2)*((-0.0672)*pp*pp + (0.12527)*pp + (-0.05132)) + ((1 + TMath::Sign(1, (pp - 1.275)))/2)*((0.02389)*(pp - 1.275)*(pp - 1.275) + (-0.02468)*(pp - 1.275) + ((-0.0672)*1.275*1.275 + (0.12527)*1.275 + (-0.0672)));
                        
                        // Refined for V12 (on 12-17-2022 from V10)
                        dp = dp + ((1 + TMath::Sign(1, (pp - 1.275)))/2)*((8.5400e-03)*pp + (-0.01927)) + ((1 + TMath::Sign(1, -(pp - 1.275)))/2)*((-0.09972)*(pp - 1.275)*(pp - 1.275) + (-0.07965)*(pp - 1.275) + ((8.5400e-03)*1.275 + (-0.01927)));
                        
                    }
                    if(sec == 2){
                        // No Pi0 Channel
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF][Sector 2][regall] is:
                        dp = ((-5.4403e-03)*pp*pp + (0.0159)*pp + (-0.01021));
                        
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_REF][Sector 2][regall] is:
                        dp = dp + ((-2.2364e-03)*pp*pp + (7.1578e-03)*pp + (-5.6010e-03));
                        
                        // // Refined for V11 (on 12-16-2022)
                        // dp = dp + ((1 + TMath::Sign(1, -(pp - 1.5)))/2)*((-0.04061)*pp*pp + (0.08923)*pp + (-0.04188)) + ((1 + TMath::Sign(1, (pp - 1.5)))/2)*((0.03201)*(pp - 1.5)*(pp - 1.5) + (-0.0294)*(pp - 1.5) + ((-0.04061)*1.5*1.5 + (0.08923)*1.5 + (-0.04061)));
                        
                        // Refined for V12 (on 12-17-2022 from V10)
                        dp = dp + ((1 + TMath::Sign(1, (pp - 1.5)))/2)*((6.9186e-03)*pp + (-0.01614)) + ((1 + TMath::Sign(1, -(pp - 1.5)))/2)*((-0.05739)*(pp - 1.5)*(pp - 1.5) + (-0.05469)*(pp - 1.5) + ((6.9186e-03)*1.5 + (-0.01614)));
                        
                    }
                    if(sec == 3){
                        // No Pi0 Channel
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF][Sector 3][regall] is:
                        dp = ((-0.0145)*pp*pp + (0.04082)*pp + (-0.02562));
                        
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_REF][Sector 3][regall] is:
                        dp = dp + ((4.1488e-03)*pp*pp + (-0.01091)*pp + (5.3172e-03));
                        
                        // // Refined for V11 (on 12-16-2022)
                        // dp = dp + ((1 + TMath::Sign(1, -(pp - 1.05)))/2)*((-0.13676)*pp*pp + (0.23057)*pp + (-0.09126)) + ((1 + TMath::Sign(1, (pp - 1.05)))/2)*((0.01506)*(pp - 1.05)*(pp - 1.05) + (-0.01978)*(pp - 1.05) + ((-0.13676)*1.05*1.05 + (0.23057)*1.05 + (-0.13676)));
                        
                        // Refined for V12 (on 12-17-2022 from V10)
                        dp = dp + ((1 + TMath::Sign(1, (pp - 1.05)))/2)*((3.3854e-03)*pp + (-8.8397e-03)) + ((1 + TMath::Sign(1, -(pp - 1.05)))/2)*((-0.19272)*(pp - 1.05)*(pp - 1.05) + (-0.09488)*(pp - 1.05) + ((3.3854e-03)*1.05 + (-8.8397e-03)));
                        
                    }
                    if(sec == 4){
                        // No Pi0 Channel
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF][Sector 4][regall] is:
                        dp = ((-0.01124)*pp*pp + (0.03298)*pp + (-0.02235));
                        
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_REF][Sector 4][regall] is:
                        dp = dp + ((-2.9293e-04)*pp*pp + (3.6047e-03)*pp + (-3.3081e-03));
                        
                        // // Refined for V11 (on 12-16-2022)
                        // dp = dp + ((1 + TMath::Sign(1, -(pp - 1.6)))/2)*((-0.02931)*pp*pp + (0.06137)*pp + (-0.0254)) + ((1 + TMath::Sign(1, (pp - 1.6)))/2)*((0.03319)*(pp - 1.6)*(pp - 1.6) + (-0.02383)*(pp - 1.6) + ((-0.02931)*1.6*1.6 + (0.06137)*1.6 + (-0.02931)));
                        
                        // Refined for V12 (on 12-17-2022 from V10)
                        dp = dp + ((1 + TMath::Sign(1, (pp - 1.6)))/2)*((9.4470e-03)*pp + (-0.02198)) + ((1 + TMath::Sign(1, -(pp - 1.6)))/2)*((-0.03889)*(pp - 1.6)*(pp - 1.6) + (-0.04655)*(pp - 1.6) + ((9.4470e-03)*1.6 + (-0.02198)));
                        
                    }
                    if(sec == 5){
                        // No Pi0 Channel
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF][Sector 5][regall] is:
                        dp = ((-0.01092)*pp*pp + (0.02808)*pp + (-0.0197));
                        
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_REF][Sector 5][regall] is:
                        dp = dp + ((1.4513e-03)*pp*pp + (-6.5134e-03)*pp + (4.6868e-03));
                        
                        // // Refined for V11 (on 12-16-2022)
                        // dp = dp + ((1 + TMath::Sign(1, -(pp - 1.3)))/2)*((-0.04212)*pp*pp + (0.09356)*pp + (-0.04422)) + ((1 + TMath::Sign(1, (pp - 1.3)))/2)*((0.02924)*(pp - 1.3)*(pp - 1.3) + (-0.03753)*(pp - 1.3) + ((-0.04212)*1.3*1.3 + (0.09356)*1.3 + (-0.04212)));
                        
                        // Refined for V12 (on 12-17-2022 from V10)
                        dp = dp + ((1 + TMath::Sign(1, (pp - 1.3)))/2)*((8.3686e-04)*pp + (-2.4123e-03)) + ((1 + TMath::Sign(1, -(pp - 1.3)))/2)*((-0.07312)*(pp - 1.3)*(pp - 1.3) + (-0.04876)*(pp - 1.3) + ((8.3686e-04)*1.3 + (-2.4123e-03)));
                        
                    }
                    if(sec == 6){
                        // No Pi0 Channel
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF][Sector 6][regall] is:
                        dp = ((-8.2723e-03)*pp*pp + (0.02055)*pp + (-0.01167));
                        
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = mmEF_PipMMEF_ProMMpro_REF][Sector 6][regall] is:
                        dp = dp + ((-1.6250e-03)*pp*pp + (5.6738e-03)*pp + (-3.8019e-03));
                        
                        // // Refined for V11 (on 12-16-2022)
                        // dp = dp + ((1 + TMath::Sign(1, -(pp - 1.15)))/2)*((-0.10524)*pp*pp + (0.17545)*pp + (-0.06634)) + ((1 + TMath::Sign(1, (pp - 1.15)))/2)*((0.01179)*(pp - 1.15)*(pp - 1.15) + (-0.01127)*(pp - 1.15) + ((-0.10524)*1.15*1.15 + (0.17545)*1.15 + (-0.10524)));
                        
                        // Refined for V12 (on 12-17-2022 from V10)
                        dp = dp + ((1 + TMath::Sign(1, (pp - 1.15)))/2)*((5.3711e-03)*pp + (-0.01317)) + ((1 + TMath::Sign(1, -(pp - 1.15)))/2)*((-0.12512)*(pp - 1.15)*(pp - 1.15) + (-0.08387)*(pp - 1.15) + ((5.3711e-03)*1.15 + (-0.01317)));
                        
                    }
                }
                
                
                if(corPro == 7 || corPro == 9){ // Correction based on each momentum slice (and the refinement based on different Missing Mass cuts)
                    if(sec == 1){
                        if(0.45 < pp && pp < 0.5){
                            dp = (-0.021819);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (-0.0093479);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (-0.0021986);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (-6.9048e-10);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.0020348);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.0053929);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.01);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.01);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.0095658);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (1.8395e-07);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.0074868);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.01);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (1.4167e-10);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (-0.0090363);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (-0.014638);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-0.0038945);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (0.0093729);
                        }
                    }
                    if(sec == 2){
                        if(0.45 < pp && pp < 0.5){
                            dp = (-0.019298);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (-0.01);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (-0.0037632);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (7.2271e-12);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (1.8242e-12);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.003169);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.0040409);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (4.5497e-05);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.0098463);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.01);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.01);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.0085684);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (0.0095119);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (-0.0091352);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (-0.015);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-0.013501);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (6.0009e-04);
                        }
                    }
                    if(sec == 3){
                        if(0.45 < pp && pp < 0.5){
                            dp = (-0.019429);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (-0.012631);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (-0.0089295);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (-0.0074301);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (-0.0040745);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (2.8793e-11);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.0024547);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.0069585);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.01);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.013924);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.010148);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (-0.0064441);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (-0.01);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (-0.01);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (-0.015);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (1.3172e-10);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (-0.0054761);
                        }
                    }
                    if(sec == 4){
                        if(0.45 < pp && pp < 0.5){
                            dp = (-0.014202);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (-0.012726);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (-0.0085499);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (-0.004222);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (-0.0027015);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (2.6980e-08);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.0012598);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.0035453);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.0089578);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.01);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.01);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.01);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (-0.01);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (-0.0026096);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (-0.0074676);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (2.3952e-09);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (-0.0047979);
                        }
                    }
                    if(sec == 5){
                        if(0.45 < pp && pp < 0.5){
                            dp = (-0.017364);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (-0.012949);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (-0.0092785);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (-0.0065438);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (-0.0028204);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (-6.4951e-05);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.0026037);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.0099247);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.01);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.0099625);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.0025209);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.01);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (7.9251e-10);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (-0.011977);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (-0.015);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-0.01);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (-0.013272);
                        }
                    }
                    if(sec == 6){
                        if(0.45 < pp && pp < 0.5){
                            dp = (-0.02);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (-0.0046567);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (-9.2643e-04);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.001573);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.0016599);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.0027488);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.0077023);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.003881);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.0030017);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.01);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.01);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (-5.4120e-10);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (-0.0036718);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (-1.0769e-09);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (-0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-0.02);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (-0.01);
                        }
                    }
                    // =======================================     Refinements     ======================================= //
                    if(sec == 1){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-0.011303);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (-0.0044224);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (-4.5442e-04);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (-0.0010117);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (1.0040e-11);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (3.6941e-11);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (-1.5646e-10);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-2.4947e-12);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (0.0017482);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (0.0046418);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (-2.3315e-08);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (0.01);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (1.1194e-08);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (7.9079e-11);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (0.0050276);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (-0.0072997);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (-0.0026774);
                        }
                    }
                    if(sec == 2){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-0.0057038);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (-0.0040769);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (6.2003e-14);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (7.2271e-12);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (1.7567e-11);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (3.1891e-04);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (0.0020065);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-0.0036864);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-5.6157e-08);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (-3.1879e-11);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (-0.01);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (-0.0081166);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (-8.1586e-05);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (9.6112e-10);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (0.0054416);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (-0.0026217);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (9.3476e-08);
                        }
                    }
                    if(sec == 3){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-0.004816);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (-0.0026276);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (1.3363e-12);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (2.2468e-11);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (2.1101e-12);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (4.1322e-12);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (-1.8556e-04);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-2.2785e-12);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-7.5973e-09);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (7.9404e-11);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (0.009469);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (-3.9013e-10);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (5.5080e-09);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (5.3885e-11);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (-0.01);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (2.8086e-10);
                        }
                    }
                    if(sec == 4){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-3.7370e-10);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (-0.0015416);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (-0.0022765);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (2.3736e-12);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (9.1573e-12);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (4.7601e-09);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (-2.1201e-11);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-0.003609);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-5.6674e-04);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (-6.0882e-12);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (-4.2169e-11);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (-3.4033e-09);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (5.2086e-09);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (-0.01);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (0.014995);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (1.5830e-09);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (9.3421e-09);
                        }
                    }
                    if(sec == 5){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-0.0021403);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (-0.0012417);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (8.4554e-14);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (2.6724e-12);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (-0.0012886);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (-1.3706e-04);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (-0.0035262);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-4.9661e-04);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-7.8030e-11);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (0.0047555);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (-0.0064624);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (-3.3666e-14);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (6.9266e-11);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (-0.0021577);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (2.8252e-09);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (0.0022419);
                        }
                    }
                    if(sec == 6){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-0.01);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (-0.0019688);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (-0.001408);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (-0.0024985);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (6.6324e-04);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (4.5377e-10);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (0.0016273);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-1.5775e-09);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-1.7147e-09);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (7.7408e-10);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (0.0028554);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (4.8094e-04);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (6.1673e-09);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (-2.4257e-10);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (0.014998);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (3.3257e-11);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (9.8751e-10);
                        }
                    }
                    // =======================================     Refinements V2     ======================================= //
                    if(sec == 1){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-0.00674);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (-0.0021521);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (-1.0711e-12);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (-3.2767e-04);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (1.0040e-11);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (3.6941e-11);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (-1.5646e-10);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-2.0569e-11);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-1.1507e-11);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (-4.5915e-04);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (-0.01);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (-6.4942e-11);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (1.1194e-08);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (1.1223e-04);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (1.1763e-09);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (-0.0027527);
                        }
                    }
                    if(sec == 2){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-9.2425e-04);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (-0.0017666);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (6.2003e-14);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (7.2271e-12);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (2.3803e-15);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (3.4029e-11);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (0.0023854);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (5.8243e-12);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-5.6157e-08);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (-3.9773e-11);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (-1.1691e-09);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (-0.0062381);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (-2.5359e-10);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (9.4728e-10);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (0.011524);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (0.0049111);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (9.3476e-08);
                        }
                    }
                    if(sec == 3){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-0.0020058);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (1.2070e-12);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (1.3363e-12);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (2.2468e-11);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (2.1101e-12);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (3.3193e-14);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (-3.3475e-04);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-2.2785e-12);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-7.5973e-09);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (-6.5245e-12);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (-1.4439e-10);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (-3.9013e-10);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (5.5080e-09);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (1.6712e-09);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (0.01);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (2.8086e-10);
                        }
                    }
                    if(sec == 4){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (0.0011084);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (3.3935e-12);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (2.4527e-11);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (2.3736e-12);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (9.1573e-12);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (4.7601e-09);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (9.3275e-04);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-1.5001e-10);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-1.5133e-10);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (-6.0882e-12);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (-4.2169e-11);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (-3.4033e-09);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (4.5969e-09);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (8.7796e-11);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (-0.0079479);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (1.5830e-09);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (9.3421e-09);
                        }
                    }
                    if(sec == 5){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-2.5100e-04);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (3.8222e-13);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (8.4554e-14);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (1.5883e-10);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (-8.6649e-11);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (-0.0010283);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (-0.0040928);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-0.0011459);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-6.6704e-12);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (-8.2846e-10);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (3.6619e-10);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (-3.3666e-14);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (4.9719e-08);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (8.0961e-11);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (1.0333e-09);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (-4.9458e-10);
                        }
                    }
                    if(sec == 6){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-0.0082436);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (-5.9226e-04);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (0.0011147);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (0.0014713);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (4.6906e-04);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (2.6198e-10);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (2.2429e-10);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-1.5775e-09);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-1.7147e-09);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (4.4781e-10);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (1.3319e-10);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (-1.1409e-10);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (6.1673e-09);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (-4.3664e-09);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (-0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (3.3257e-11);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (9.8751e-10);
                        }
                    }
//==================//=======================================     Refinements Based on New Exclusivity Cuts     =======================================//
                    if(corPro == 9){
                        if(sec == 1){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (0.02);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (0.016883);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.016182);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (0.01);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (0.01);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (0.01);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (0.01);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-1.7619e-11);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-2.9013e-11);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-5.9897e-10);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-0.01);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-1.7249e-11);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (1.0511e-10);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.01);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.005);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (6.7706e-11);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (0.01);
                            }
                        }
                        if(sec == 2){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (0.027684);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (0.02);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.015868);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (0.01);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (0.01);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (0.01);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (0.01);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (8.6624e-11);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-2.8453e-12);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-1.8781e-12);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-2.3874e-10);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (0.01);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (-1.6146e-10);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (6.3840e-11);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.005);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (-0.0014661);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (3.1120e-09);
                            }
                        }
                        if(sec == 3){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (0.025976);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (0.02);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.014662);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (0.01);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (0.01);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (0.0055924);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (0.0038916);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-5.3770e-11);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-7.4755e-12);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-3.2957e-10);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-4.3949e-11);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-2.1512e-10);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (0.01);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (7.5114e-11);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.005);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (8.0087e-11);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (3.9947e-10);
                            }
                        }
                        if(sec == 4){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (0.019243);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (0.018771);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.01);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (0.01);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (0.0057702);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (0.0059918);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (0.0092294);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-1.2730e-12);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-3.1387e-10);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-3.9105e-10);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-2.0599e-11);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-3.1564e-10);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (3.0837e-12);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (8.5209e-10);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.0092159);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (4.1911e-11);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (5.4589e-11);
                            }
                        }
                        if(sec == 5){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (0.02);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (0.016807);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.013753);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (0.014285);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (0.01);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (0.01);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-3.4999e-11);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-3.7870e-11);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-3.4511e-11);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-4.1769e-12);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-2.9406e-10);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-3.3963e-12);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (1.3165e-10);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (6.1992e-10);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.005);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (3.3053e-11);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (0.0013973);
                            }
                        }
                        if(sec == 6){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (0.02);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (0.017859);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.01);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (0.01);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (0.01);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (0.018843);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (0.0096899);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-2.9812e-12);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-2.2143e-10);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (4.1613e-11);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (4.7149e-04);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-1.0888e-10);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (1.6797e-09);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (-5.3988e-12);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.005);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (3.2226e-11);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (9.8497e-11);
                            }
                        }
                        // =======================================     Refinements with New Cuts V2     ======================================= //
                        if(sec == 1){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.0075);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.0025);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.0025);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.0025);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.0025);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.0025);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (0.0075);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (0.0075);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (0.0125);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (0.0125);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (0.0075673);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-0.0025);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (0.0125);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.0125);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.0075);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (0.0075);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (0.0075);
                            }
                        }
                        if(sec == 2){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (0.0075);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (0.0034762);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.0032147);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.0025);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (0.0025);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (0.0025);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (0.0025);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-0.0025);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.0075);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-0.0075);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-0.0075);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (0.0125);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (-0.0025);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.0025);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.005);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (0.005);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (0.0075);
                            }
                        }
                        if(sec == 3){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (0.0075);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (0.0025);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.0025);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.0025);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (0.0025);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (0.0025);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (0.0028321);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (0.0035503);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.0075);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (0.009763);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-0.0075);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-0.0025);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (-0.0075);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.0025);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.005);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (0.005);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (0.0073797);
                            }
                        }
                        if(sec == 4){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.0075);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.0075);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.0125);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.0025);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.0025);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (0.0025);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.0125);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-0.0075);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (0.0075);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-0.0075);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-0.0075);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-0.0125);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (-0.0025);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (-0.0075);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.0090977);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (0.0075);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (0.0075);
                            }
                        }
                        if(sec == 5){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.0075);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.0025);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.0025);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.0025);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.0025);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-1.9599e-08);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (0.0075);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-0.0025);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.0075);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-0.0075);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-0.005);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-0.0125);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (0.0021607);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.0025);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.005);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (-0.0075);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (-0.012064);
                            }
                        }
                        if(sec == 6){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.0075);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (0.0075);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.0025);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.0025);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.0025);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (0.0025);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (0.0075);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (0.0059837);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.0075);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (0.0075);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (0.0075);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (0.0070873);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (4.3578e-09);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (-0.0025);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.0075);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (0.0075);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (0.0075);
                            }
                        }
                        // =======================================     Refinements with Old Cuts     ======================================= //
                        if(sec == 1){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.01279);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.018525);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.016369);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.01);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.01);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.01);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.02);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-0.018655);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.015);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-0.0092379);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-0.0058995);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-0.01);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (-0.015953);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (-0.014454);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.012616);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (-0.0072444);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (-0.025);
                            }
                        }
                        if(sec == 2){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.026494);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.025555);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.018981);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.01);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.019474);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.02);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.0096482);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (1.8500e-10);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.005);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (0.0055748);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (0.005);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-0.013046);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (-0.0024152);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.00349);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.0084552);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (-0.005);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (-0.0075361);
                            }
                        }
                        if(sec == 3){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.027385);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.02);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.015027);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.01);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.014524);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.01);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.01);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (2.8544e-12);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.010999);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-0.015);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (0.005);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (0.0084148);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (0.01);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.0055991);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.010668);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (-0.010227);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (-0.0064019);
                            }
                        }
                        if(sec == 4){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.012915);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.015);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.015);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.0084149);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.0091235);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.0070069);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (0.0011843);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-0.005);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.0088171);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-0.0052478);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (0.005);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (0.0040997);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (0.01);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.015);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.0057669);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (-0.0098353);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (-0.0069987);
                            }
                        }
                        if(sec == 5){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.015);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.017453);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.015598);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.01);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.01);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.009637);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.0061192);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-0.0042108);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.005);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (0.005);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (0.005);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (0.0048165);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (2.7391e-10);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (-3.3162e-12);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.0077807);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (0.0056473);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (0.0094693);
                            }
                        }
                        if(sec == 6){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.025);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.015);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.01);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.01);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.018783);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.02);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.01);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-0.0017191);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.006928);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-0.015);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-0.011629);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-0.0061836);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (0.0028732);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (1.1382e-11);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.005);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (0.0066681);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (-0.005);
                            }
                        }
                        // =======================================     Refinements with Old Cuts V2     ======================================= //
                        if(sec == 1){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.01279);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.018525);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.016369);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.01);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.01);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.01);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.02);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-0.018655);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.015);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-0.0092379);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-0.0058995);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-0.01);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (-0.015953);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (-0.014454);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.012616);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (-0.0072444);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (-0.025);
                            }
                        }
                        if(sec == 2){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.026494);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.025555);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.018981);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.01);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.019474);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.02);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.0096482);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (1.8500e-10);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.005);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (0.0055748);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (0.005);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-0.013046);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (-0.0024152);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.00349);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.0084552);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (-0.005);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (-0.0075361);
                            }
                        }
                        if(sec == 3){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.027385);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.02);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.015027);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.01);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.014524);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.01);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.01);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (2.8544e-12);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.010999);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-0.015);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (0.005);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (0.0084148);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (0.01);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.0055991);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.010668);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (-0.010227);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (-0.0064019);
                            }
                        }
                        if(sec == 4){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.012915);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.015);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.015);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.0084149);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.0091235);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.0070069);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (0.0011843);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-0.005);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.0088171);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-0.0052478);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (0.005);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (0.0040997);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (0.01);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.015);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.0057669);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (-0.0098353);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (-0.0069987);
                            }
                        }
                        if(sec == 5){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.015);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.017453);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.015598);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.01);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.01);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.009637);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.0061192);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-0.0042108);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.005);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (0.005);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (0.005);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (0.0048165);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (2.7391e-10);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (-3.3162e-12);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.0077807);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (0.0056473);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (0.0094693);
                            }
                        }
                        if(sec == 6){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (-0.025);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-0.015);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.01);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.01);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.018783);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-0.02);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.01);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-0.0017191);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (-0.006928);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-0.015);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-0.011629);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-0.0061836);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (0.0028732);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (1.1382e-11);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.005);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (0.0066681);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (-0.005);
                            }
                        }
                    }
                }
                
                if(corPro == 8){ // Correction based on each momentum slice (with new exclusive cut (|MM2| < 0.2))
                    if(sec == 1){
                        if(0.45 < pp && pp < 0.5){
                            dp = (-7.4312e-11);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.01);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.01);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.01);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.016996);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.018437);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.01);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.01);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.01);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.0052936);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.01);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.02);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (1.9562e-10);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (4.6509e-11);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (-0.010629);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-2.3723e-10);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (0.01);
                        }
                    }
                    if(sec == 2){
                        if(0.45 < pp && pp < 0.5){
                            dp = (0.01);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.012049);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.014356);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.01);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.012726);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.01);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.01);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.0036561);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.01);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (-2.8366e-14);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (-1.0070e-10);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.01);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (0.01);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (-0.01);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-0.01);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (3.3980e-10);
                        }
                    }
                    if(sec == 3){
                        if(0.45 < pp && pp < 0.5){
                            dp = (0.0085381);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.0090808);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.0060518);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.0059923);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.0084798);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.0076231);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.01);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.01);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.01);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.02);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (-0.01);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (-0.01);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (6.8759e-08);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (-0.01);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (8.7633e-11);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (5.1931e-12);
                        }
                    }
                    if(sec == 4){
                        if(0.45 < pp && pp < 0.5){
                            dp = (0.0056357);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.0058428);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.0081993);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.0089556);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.0046634);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.0055047);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.0093798);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.01);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.01);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.01);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.01);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.01);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (-0.01);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (-0.02);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (0.012419);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (2.9119e-12);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (-0.01);
                        }
                    }
                    if(sec == 5){
                        if(0.45 < pp && pp < 0.5){
                            dp = (-2.6028e-10);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.0049117);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.0073274);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.0083419);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.01);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (-6.3270e-13);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.01);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.01);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.02);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.01);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (-3.0080e-11);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.01);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (9.6874e-10);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (-0.019089);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (-0.015);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-0.01);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (-0.018318);
                        }
                    }
                    if(sec == 6){
                        if(0.45 < pp && pp < 0.5){
                            dp = (-1.2613e-11);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.014062);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.01511);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.01);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.01);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.019064);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.02);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.01);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.01);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.018395);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.010096);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (-5.3104e-12);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (1.6519e-09);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (7.3725e-04);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-0.02);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (-0.01);
                        }
                    }
                    // =======================================     Refinements with Old Cuts     ======================================= //
                    if(sec == 1){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-0.027942);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (-0.02);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (-0.017727);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (-0.018227);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (-0.019137);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (-0.01);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (-0.0085849);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-0.0083214);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-0.0076428);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (-0.0083065);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (-0.013988);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (-0.01);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (6.4422e-12);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (-8.1260e-05);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (-0.0096005);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (-0.01316);
                        }
                    }
                    if(sec == 2){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-0.029984);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (-0.026625);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (-0.019963);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (-0.017848);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (-0.01);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (-0.01);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (-0.0086173);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-0.0091684);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-0.0058583);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (0.005);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (-0.005);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (-0.0060876);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (-0.0051109);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (0.00735);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (-0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (0.0066393);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (0.005);
                        }
                    }
                    if(sec == 3){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-0.029155);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (-0.02);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (-0.016941);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (-0.016379);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (-0.01);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (-0.01);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (-0.01);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-0.01);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-0.014068);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (-0.005);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (0.0089903);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (0.0085133);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (-2.3560e-11);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (0.0075731);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (-0.0094564);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (-0.0058177);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (-0.0052369);
                        }
                    }
                    if(sec == 4){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-0.015);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (-0.025);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (-0.015);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (-0.01);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (-0.0097275);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (-0.01);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (-0.012622);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-0.01081);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-0.0091726);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (-0.011661);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (-0.014094);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (-0.0082875);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (0.01);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (0.015);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (-0.013673);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (0.005);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (0.005);
                        }
                    }
                    if(sec == 5){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-0.025);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (-0.02);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (-0.017404);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (-0.016382);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (-0.01);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (-0.0092589);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (-0.01);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-0.01);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-0.012515);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (-0.005);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (-0.006036);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (-0.0056029);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (0.0029782);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (0.01);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (0.0076877);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (-0.005);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (0.0055403);
                        }
                    }
                    if(sec == 6){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (-0.029184);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (-0.025);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (-0.016657);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (-0.01);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (-0.016229);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (-0.018756);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (-0.01);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (-0.0082998);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (-0.01382);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (-0.014116);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (-0.005);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (-8.2321e-10);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (-1.2420e-11);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (-0.0047283);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (-0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = dp + (0.012833);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = dp + (0.005);
                        }
                    }
                }
                if(corPro == 10 || corPro == 11){ // Correction based on each momentum slice (Version 2)
                    if(sec == 1){
                        if(0.45 < pp && pp < 0.5){
                            dp = (-7.4312e-11);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.01);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.01);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.01);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.016996);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.0028929);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.0075);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (-0.001155);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.008814);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.0074449);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (-0.010845);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (-0.0025);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (-0.019406);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (-0.015332);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (-0.017342);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-0.018183);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (-0.028557);
                        }
                    }
                    if(sec == 2){
                        if(0.45 < pp && pp < 0.5){
                            dp = (0.01);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (-0.017922);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (-0.0036615);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (-0.0025);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (-0.006974);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (-0.0040121);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.011285);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (-0.0061409);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (-0.0026538);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.0080748);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (-0.0025);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (-0.0093783);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (0.0020999);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (3.4480e-04);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (-0.0049448);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-0.012678);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (-0.0069719);
                        }
                    }
                    if(sec == 3){
                        if(0.45 < pp && pp < 0.5){
                            dp = (0.0085381);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.0090808);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.0060518);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.0059923);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.0084798);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.0076231);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.01);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.01);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.01);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (-0.006313);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.022117);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.0078855);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (0.0125);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (0.0036982);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (-0.016336);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (8.7633e-11);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (-0.0109);
                        }
                    }
                    if(sec == 4){
                        if(0.45 < pp && pp < 0.5){
                            dp = (0.0056357);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.0058428);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.0081993);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.0089556);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.0046634);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.0055047);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.0093798);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.01);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.01);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.01);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.01);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.0056994);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (0.0075);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (0.0098904);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (-0.0060692);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (0.005);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (-0.011295);
                        }
                    }
                    if(sec == 5){
                        if(0.45 < pp && pp < 0.5){
                            dp = (-2.6028e-10);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.0049117);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.0073274);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.0083419);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.01);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (-6.3270e-13);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.01);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.01);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.02);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.01);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (-3.0080e-11);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.01);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (9.6874e-10);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (-0.019089);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (-0.015);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-0.01);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (-0.018318);
                        }
                    }
                    if(sec == 6){
                        if(0.45 < pp && pp < 0.5){
                            dp = (-1.2613e-11);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.014062);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.01511);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.01);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.01);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.019064);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.02);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.01);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.01);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.018395);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.010096);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (-8.4664e-12);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (0.0064037);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (0.0056894);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (0.0096238);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-0.02);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (-0.0125);
                        }
                    }
                    
                    // =======================================     Refinements without cuts     ======================================= //
                    
                    if(sec == 1){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (0.0084315);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (0.0050019);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (0.0057869);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (0.0046812);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (0.0071708);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (0.011709);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (0.012436);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (0.014368);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (0.007452);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (0.012436);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (0.012436);
                        }
                    }
                    if(sec == 2){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (0.030631);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (0.025994);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (0.017748);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (0.014691);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (0.017752);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (0.0082397);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (0.0046455);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (0.0046455);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (0.0046455);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (0.0046455);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (0.0046455);
                        }
                    }
                    if(sec == 3){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (0.0051397);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (0.0035474);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (0.0034197);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (0.0029979);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (0.0028054);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (0.0029933);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (0.0013555);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (0.0014152);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (0.007457);
                        }
                    }
                    if(sec == 4){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (0.0078426);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (0.0052728);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (8.4034e-04);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (0.0017963);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (0.0019293);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (0.0020944);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (0.001689);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (0.0014401);
                        }
                    }
                    if(sec == 5){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (0.0075001);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (0.0050126);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (0.0036773);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (0.0016987);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (0.0036964);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (0.0030682);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (0.0030682);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (0.0030682);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (0.0018697);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (0.0018697);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (0.0018697);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (0.0036964);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (0.0036964);
                        }
                    }
                    if(sec == 6){
                        if(0.45 < pp && pp < 0.5){
                            dp = dp + (0.01116);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = dp + (0.01116);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = dp + (0.01116);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = dp + (0.0062951);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = dp + (0.0051388);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = dp + (0.0051388);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = dp + (0.0051388);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = dp + (0.0051388);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = dp + (0.0051388);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = dp + (0.0051388);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = dp + (0.0062951);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = dp + (0.0062951);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = dp + (0.0062951);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = dp + (0.0062951);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = dp + (0.0062951);
                        }
                    }
                    
//==================//=======================================     Refinements For Final Correction     =======================================//
                    if(corPro == 11){
                        if(sec == 1){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (0.0032238);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (-2.0784e-04);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.0010965);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (-0.0012269);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-0.0015037);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (0.0015141);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (0.0015309);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (0.0043368);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (0.0022633);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (0.0046164);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (0.015204);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (0.0083456);
                            }
                        }
                        if(sec == 2){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (0.0059567);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (0.006196);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.0017573);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (0.0011075);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (0.0053651);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (0.0029749);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (0.0037233);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (0.010133);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (0.0083556);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (0.0039278);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (0.010051);
                            }
                        }
                        if(sec == 3){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (6.9670e-04);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (5.4424e-04);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (4.3451e-04);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (2.8968e-04);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (-6.6300e-04);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (-7.3205e-05);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (2.8984e-04);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (6.3692e-04);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (0.0058949);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (0.0053996);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (-5.8068e-04);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-0.0015021);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (-0.0054621);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.001449);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (0.0070565);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (-0.0035413);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (0.0055068);
                            }
                        }
                        if(sec == 4){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (0.0033399);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (0.0022257);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-2.6303e-04);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (2.2120e-04);
                            }
                            if(0.65 < pp && pp < 0.7){
                                dp = dp + (4.0717e-04);
                            }
                            if(0.7 < pp && pp < 0.75){
                                dp = dp + (1.8582e-04);
                            }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-9.0982e-04);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (0.0011315);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (0.0036228);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (0.0023682);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (0.0060595);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (0.005713);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (0.0024642);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (0.001497);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.001317);
                            }
                            if(2.0 < pp && pp < 2.25){
                                dp = dp + (-0.0015231);
                            }
                            if(2.25 < pp && pp < 2.75){
                                dp = dp + (0.0047541);
                            }
                        }
                        if(sec == 5){
                            if(0.45 < pp && pp < 0.5){
                                dp = dp + (0.0016535);
                            }
                            if(0.5 < pp && pp < 0.55){
                                dp = dp + (4.6649e-04);
                            }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (0.0012979);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (2.7825e-05);
                            }
                            // if(0.65 < pp && pp < 0.7){
                            //     dp = dp + (0.0012245);
                            // }
                            // if(0.7 < pp && pp < 0.75){
                            //     dp = dp + (2.9172e-05);
                            // }
                            if(0.75 < pp && pp < 0.8){
                                dp = dp + (-0.0032516);
                            }
                            if(0.8 < pp && pp < 0.85){
                                dp = dp + (-8.4837e-04);
                            }
                            if(0.85 < pp && pp < 0.9){
                                dp = dp + (0.0022281);
                            }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (0.0038184);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (7.9725e-04);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-4.1466e-04);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (0.0033156);
                            }
                            // if(1.5 < pp && pp < 1.75){
                            //     dp = dp + (0.0037279);
                            // }
                            // if(1.75 < pp && pp < 2.0){
                            //     dp = dp + (4.4757e-04);
                            // }
                            // if(2.0 < pp && pp < 2.25){
                            //     dp = dp + (0.0023994);
                            // }
                            // if(2.25 < pp && pp < 2.75){
                            //     dp = dp + (0.0023994);
                            // }
                        }
                        if(sec == 6){
                            // if(0.45 < pp && pp < 0.5){
                            //     dp = dp + (0.0036862);
                            // }
                            // if(0.5 < pp && pp < 0.55){
                            //     dp = dp + (-0.0045317);
                            // }
                            if(0.55 < pp && pp < 0.6){
                                dp = dp + (-0.001431);
                            }
                            if(0.6 < pp && pp < 0.65){
                                dp = dp + (0.0023042);
                            }
                            // if(0.65 < pp && pp < 0.7){
                            //     dp = dp + (8.4403e-04);
                            // }
                            // if(0.7 < pp && pp < 0.75){
                            //     dp = dp + (-0.0045579);
                            // }
                            // if(0.75 < pp && pp < 0.8){
                            //     dp = dp + (-0.0016706);
                            // }
                            // if(0.8 < pp && pp < 0.85){
                            //     dp = dp + (-0.0017198);
                            // }
                            // if(0.85 < pp && pp < 0.9){
                            //     dp = dp + (-0.0086078);
                            // }
                            if(0.9 < pp && pp < 0.95){
                                dp = dp + (-7.8749e-04);
                            }
                            if(0.95 < pp && pp < 1.0){
                                dp = dp + (0.0057313);
                            }
                            if(1.0 < pp && pp < 1.25){
                                dp = dp + (-0.001211);
                            }
                            if(1.25 < pp && pp < 1.5){
                                dp = dp + (-0.004281);
                            }
                            if(1.5 < pp && pp < 1.75){
                                dp = dp + (-0.0090585);
                            }
                            if(1.75 < pp && pp < 2.0){
                                dp = dp + (-0.0083043);
                            }
                            // if(2.0 < pp && pp < 2.25){
                            //     dp = dp + (0.015975);
                            // }
                            // if(2.25 < pp && pp < 2.75){
                            //     dp = dp + (0.0096651);
                            // }
                        }
                    }
                }
                
                if(corPro == 12){
                    if(sec == 1){
                        dp = ((1 + TMath::Sign(1, -(pp - (1.37961))))/2)*((-0.10988)*pp*pp + (0.17061)*pp + (-0.04566)) + ((1 + TMath::Sign(1, (pp - (1.37961))))/2)*((-0.02395)*(pp - (1.37961))*(pp - (1.37961)) + (0.0188)*(pp - (1.37961)) + ((-0.10988)*(1.37961)*(1.37961) + (0.17061)*(1.37961) + (-0.04566)));
                    }
                    if(sec == 2){
                        dp = ((1 + TMath::Sign(1, -(pp - (0.90061))))/2)*((0.2957)*pp*pp + (-0.45727)*pp + (0.18551)) + ((1 + TMath::Sign(1, (pp - (0.90061))))/2)*((0.0142)*(pp - (0.90061))*(pp - (0.90061)) + (-0.03563)*(pp - (0.90061)) + ((0.2957)*(0.90061)*(0.90061) + (-0.45727)*(0.90061) + (0.18551)));
                    }
                    if(sec == 3){
                        dp = ((1 + TMath::Sign(1, -(pp - (0.97528))))/2)*((0.07708)*pp*pp + (-0.10793)*pp + (0.0479)) + ((1 + TMath::Sign(1, (pp - (0.97528))))/2)*((0.01151)*(pp - (0.97528))*(pp - (0.97528)) + (-0.03167)*(pp - (0.97528)) + ((0.07708)*(0.97528)*(0.97528) + (-0.10793)*(0.97528) + (0.0479)));
                    }
                    if(sec == 4){
                        dp = ((1 + TMath::Sign(1, -(pp - (0.94952))))/2)*((0.12712)*pp*pp + (-0.18059)*pp + (0.07288)) + ((1 + TMath::Sign(1, (pp - (0.94952))))/2)*((1.4963e-03)*(pp - (0.94952))*(pp - (0.94952)) + (-0.01659)*(pp - (0.94952)) + ((0.12712)*(0.94952)*(0.94952) + (-0.18059)*(0.94952) + (0.07288)));
                    }
                    if(sec == 5){
                        dp = ((1 + TMath::Sign(1, -(pp - (1.16982))))/2)*((-9.4111e-03)*pp*pp + (0.01929)*pp + (2.4572e-03)) + ((1 + TMath::Sign(1, (pp - (1.16982))))/2)*((0.02872)*(pp - (1.16982))*(pp - (1.16982)) + (-0.05903)*(pp - (1.16982)) + ((-9.4111e-03)*(1.16982)*(1.16982) + (0.01929)*(1.16982) + (2.4572e-03)));
                    }
                    if(sec == 6){
                        dp = ((1 + TMath::Sign(1, -(pp - (0.92377))))/2)*((-5.6309e-03)*pp*pp + (7.1724e-03)*pp + (0.01738)) + ((1 + TMath::Sign(1, (pp - (0.92377))))/2)*((2.0807e-03)*(pp - (0.92377))*(pp - (0.92377)) + (-0.02525)*(pp - (0.92377)) + ((-5.6309e-03)*(0.92377)*(0.92377) + (7.1724e-03)*(0.92377) + (0.01738)));
                    }
                }
                
                if(corPro == 13){
                    if(sec == 1){
                        dp = ((1 + TMath::Sign(1, -(pp - (1.4681))))/2)*((-0.07881)*pp*pp + (0.12097)*pp + (-0.02689)) + ((1 + TMath::Sign(1, (pp - (1.4681))))/2)*((-0.05413)*(pp - (1.4681))*(pp - (1.4681)) + (0.06397)*(pp - (1.4681)) + ((-0.07881)*(1.4681)*(1.4681) + (0.12097)*(1.4681) + (-0.02689)));
                    }
                    if(sec == 2){
                        dp = ((1 + TMath::Sign(1, -(pp - (0.83137))))/2)*((-0.0252)*pp*pp + (1.9204e-03)*pp + (0.02614)) + ((1 + TMath::Sign(1, (pp - (0.83137))))/2)*((3.0648e-03)*(pp - (0.83137))*(pp - (0.83137)) + (-0.01249)*(pp - (0.83137)) + ((-0.0252)*(0.83137)*(0.83137) + (1.9204e-03)*(0.83137) + (0.02614)));
                    }
                    if(sec == 3){
                        dp = ((1 + TMath::Sign(1, -(pp - (1.81971))))/2)*((-0.01604)*pp*pp + (0.02618)*pp + (1.3139e-03)) + ((1 + TMath::Sign(1, (pp - (1.81971))))/2)*((-0.0198)*(pp - (1.81971))*(pp - (1.81971)) + (0.01804)*(pp - (1.81971)) + ((-0.01604)*(1.81971)*(1.81971) + (0.02618)*(1.81971) + (1.3139e-03)));
                    }
                    if(sec == 4){
                        dp = ((1 + TMath::Sign(1, -(pp - (1.1))))/2)*((0.10967)*pp*pp + (-0.17521)*pp + (0.07558)) + ((1 + TMath::Sign(1, (pp - (1.1))))/2)*((7.3136e-03)*(pp - (1.1))*(pp - (1.1)) + (-0.02294)*(pp - (1.1)) + ((0.10967)*(1.1)*(1.1) + (-0.17521)*(1.1) + (0.07558)));
                    }
                    if(sec == 5){
                        dp = ((1 + TMath::Sign(1, -(pp - (1.3247))))/2)*((-4.8153e-03)*pp*pp + (8.2971e-04)*pp + (0.01374)) + ((1 + TMath::Sign(1, (pp - (1.3247))))/2)*((-2.7883e-03)*(pp - (1.3247))*(pp - (1.3247)) + (-0.01603)*(pp - (1.3247)) + ((-4.8153e-03)*(1.3247)*(1.3247) + (8.2971e-04)*(1.3247) + (0.01374)));
                    }
                    if(sec == 6){
                        dp = ((1 + TMath::Sign(1, -(pp - (1.075))))/2)*((-0.01358)*pp*pp + (9.8430e-04)*pp + (0.02437)) + ((1 + TMath::Sign(1, (pp - (1.075))))/2)*((8.9354e-03)*(pp - (1.075))*(pp - (1.075)) + (-0.01746)*(pp - (1.075)) + ((-0.01358)*(1.075)*(1.075) + (9.8430e-04)*(1.075) + (0.02437)));
                    }
                }
                
                if(corPro == 14){
                    if(sec == 1){
                        dp = ((1 + TMath::Sign(1, -(pp - (1.42692))))/2)*((-0.10673)*pp*pp + (0.17056)*pp + (-0.04586)) + ((1 + TMath::Sign(1, (pp - (1.42692))))/2)*((-0.03061)*(pp - (1.42692))*(pp - (1.42692)) + (0.02836)*(pp - (1.42692)) + ((-0.10673)*(1.42692)*(1.42692) + (0.17056)*(1.42692) + (-0.04586)));
                    }
                    if(sec == 2){
                        dp = ((1 + TMath::Sign(1, -(pp - (0.82618))))/2)*((0.18658)*pp*pp + (-0.29765)*pp + (0.13182)) + ((1 + TMath::Sign(1, (pp - (0.82618))))/2)*((0.01199)*(pp - (0.82618))*(pp - (0.82618)) + (-0.03199)*(pp - (0.82618)) + ((0.18658)*(0.82618)*(0.82618) + (-0.29765)*(0.82618) + (0.13182)));
                    }
                    if(sec == 3){
                        dp = ((1 + TMath::Sign(1, -(pp - (0.97431))))/2)*((0.05887)*pp*pp + (-0.0819)*pp + (0.03947)) + ((1 + TMath::Sign(1, (pp - (0.97431))))/2)*((0.0115)*(pp - (0.97431))*(pp - (0.97431)) + (-0.03073)*(pp - (0.97431)) + ((0.05887)*(0.97431)*(0.97431) + (-0.0819)*(0.97431) + (0.03947)));
                    }
                    if(sec == 4){
                        dp = ((1 + TMath::Sign(1, -(pp - (1.12335))))/2)*((0.04921)*pp*pp + (-0.0722)*pp + (0.03733)) + ((1 + TMath::Sign(1, (pp - (1.12335))))/2)*((6.2541e-03)*(pp - (1.12335))*(pp - (1.12335)) + (-0.02645)*(pp - (1.12335)) + ((0.04921)*(1.12335)*(1.12335) + (-0.0722)*(1.12335) + (0.03733)));
                    }
                    if(sec == 5){
                        dp = ((1 + TMath::Sign(1, -(pp - (1.174))))/2)*((0.02769)*pp*pp + (-0.0443)*pp + (0.02957)) + ((1 + TMath::Sign(1, (pp - (1.174))))/2)*((0.01511)*(pp - (1.174))*(pp - (1.174)) + (-0.04819)*(pp - (1.174)) + ((0.02769)*(1.174)*(1.174) + (-0.0443)*(1.174) + (0.02957)));
                    }
                    if(sec == 6){
                        dp = ((1 + TMath::Sign(1, -(pp - (1.05172))))/2)*((-5.2223e-03)*pp*pp + (5.0774e-03)*pp + (0.01891)) + ((1 + TMath::Sign(1, (pp - (1.05172))))/2)*((2.1664e-04)*(pp - (1.05172))*(pp - (1.05172)) + (-0.02573)*(pp - (1.05172)) + ((-5.2223e-03)*(1.05172)*(1.05172) + (5.0774e-03)*(1.05172) + (0.01891)));
                    }
                }
                
                if(corPro == 15){
                    if(sec == 1){
                        dp = ((1 + TMath::Sign(1, -(pp - (1.42692))))/2)*((-0.10673)*pp*pp + (0.17056)*pp + (-0.04586)) + ((1 + TMath::Sign(1, (pp - (1.42692))))/2)*((-0.03061)*(pp - (1.42692))*(pp - (1.42692)) + (0.02836)*(pp - (1.42692)) + ((-0.10673)*(1.42692)*(1.42692) + (0.17056)*(1.42692) + (-0.04586)));
                    }
                    if(sec == 2){
                        dp = ((1 + TMath::Sign(1, -(pp - (0.82618))))/2)*((0.18658)*pp*pp + (-0.29765)*pp + (0.13182)) + ((1 + TMath::Sign(1, (pp - (0.82618))))/2)*((0.01199)*(pp - (0.82618))*(pp - (0.82618)) + (-0.03199)*(pp - (0.82618)) + ((0.18658)*(0.82618)*(0.82618) + (-0.29765)*(0.82618) + (0.13182)));
                    }
                    if(sec == 3){
                        dp = ((1 + TMath::Sign(1, -(pp - (0.97431))))/2)*((0.05887)*pp*pp + (-0.0819)*pp + (0.03947)) + ((1 + TMath::Sign(1, (pp - (0.97431))))/2)*((0.0115)*(pp - (0.97431))*(pp - (0.97431)) + (-0.03073)*(pp - (0.97431)) + ((0.05887)*(0.97431)*(0.97431) + (-0.0819)*(0.97431) + (0.03947)));
                    }
                    if(sec == 4){
                        dp = ((1 + TMath::Sign(1, -(pp - (1.12335))))/2)*((0.04921)*pp*pp + (-0.0722)*pp + (0.03733)) + ((1 + TMath::Sign(1, (pp - (1.12335))))/2)*((6.2541e-03)*(pp - (1.12335))*(pp - (1.12335)) + (-0.02645)*(pp - (1.12335)) + ((0.04921)*(1.12335)*(1.12335) + (-0.0722)*(1.12335) + (0.03733)));
                    }
                    // if(sec == 5){
                    //     dp = ((1 + TMath::Sign(1, -(pp - (1.2764))))/2)*((-0.05446)*pp*pp + (0.06807)*pp + (-6.6949e-03)) + ((1 + TMath::Sign(1, (pp - (1.2764))))/2)*((9.3495e-03)*(pp - (1.2764))*(pp - (1.2764)) + (-0.02295)*(pp - (1.2764)) + ((-0.05446)*(1.2764)*(1.2764) + (0.06807)*(1.2764) + (-6.6949e-03)));
                    // }
                    // if(sec == 5){
                    //     dp = ((1 + TMath::Sign(1, -(pp - (1.14774))))/2)*((-0.02308)*pp*pp + (-5.8975e-04)*pp + (0.02605)) + ((1 + TMath::Sign(1, (pp - (1.14774))))/2)*((0.01083)*(pp - (1.14774))*(pp - (1.14774)) + (-0.02783)*(pp - (1.14774)) + ((-0.02308)*(1.14774)*(1.14774) + (-5.8975e-04)*(1.14774) + (0.02605)));
                    // }
                    if(sec == 5){
                        dp = ((1 + TMath::Sign(1, -(pp - (1.26673))))/2)*((-0.07969)*pp*pp + (0.09716)*pp + (-0.01131)) + ((1 + TMath::Sign(1, (pp - (1.26673))))/2)*((2.5671e-03)*(pp - (1.26673))*(pp - (1.26673)) + (-8.4397e-03)*(pp - (1.26673)) + ((-0.07969)*(1.26673)*(1.26673) + (0.09716)*(1.26673) + (-0.01131)));
                    }
                    if(sec == 6){
                        dp = ((1 + TMath::Sign(1, -(pp - (0.97449))))/2)*((-0.02624)*pp*pp + (-9.6652e-04)*pp + (0.03259)) + ((1 + TMath::Sign(1, (pp - (0.97449))))/2)*((7.1481e-03)*(pp - (0.97449))*(pp - (0.97449)) + (-0.0298)*(pp - (0.97449)) + ((-0.02624)*(0.97449)*(0.97449) + (-9.6652e-04)*(0.97449) + (0.03259)));
                    }
                }
                
                if(corPro == 16){
                    dp = 0.02;
                }
                if(corPro == 17){
                    dp = -0.02;
                }
                if(corPro == 18){
                    if(sec == 1){
                        // Peak #1:
                        if(0.45 < pp && pp < 0.6){
                            dp = (0.014267);
                        }
                        // Peak #2:
                        if(0.6 < pp && pp < 0.75){
                            dp = (0.020639);
                        }
                        // Peak #3:
                        if(0.75 < pp && pp < 0.9){
                            dp = (0.022209);
                        }
                        // Peak #4:
                        if(0.9 < pp && pp < 1.05){
                            dp = (0.018976);
                        }
                        // Peak #5:
                        if(1.05 < pp && pp < 1.2){
                            dp = (0.01094);
                        }
                        // Peak #6:
                        if(1.2 < pp && pp < 1.35){
                            dp = (-0.001899);
                        }
                        // Peak #7:
                        if(1.35 < pp && pp < 1.5){
                            dp = (-0.019541);
                        }
                        // Peak #8:
                        if(1.5 < pp && pp < 1.65){
                            dp = (-0.016269);
                        }
                        // Peak #9:
                        if(1.65 < pp && pp < 1.8){
                            dp = (-0.014064);
                        }
                        // Peak #10:
                        if(1.8 < pp && pp < 1.95){
                            dp = (-0.013236);
                        }
                        // Peak #11:
                        if(1.95 < pp && pp < 2.1){
                            dp = (-0.013785);
                        }
                        // Peak #12:
                        if(2.1 < pp && pp < 2.25){
                            dp = (-0.015712);
                        }
                        // Peak #13:
                        if(2.25 < pp && pp < 2.4){
                            dp = (-0.019016);
                        }
                        // Peak #14:
                        if(2.4 < pp && pp < 2.55){
                            dp = (-0.023698);
                        }
                        // Peak #15:
                        if(2.55 < pp && pp < 2.7){
                            dp = (-0.029757);
                        }
                        // Peak #16:
                        if(2.7 < pp && pp < 2.85){
                            dp = (-0.037194);
                        }
                        // Peak #17:
                        if(2.85 < pp && pp < 3.0){
                            dp = (-0.021008);
                        }
                    }

                    if(sec == 2){
                        // Peak #1:
                        if(0.45 < pp && pp < 0.6){
                            dp = (0.02698);
                        }
                        // Peak #2:
                        if(0.6 < pp && pp < 0.75){
                            dp = (0.015917);
                        }
                        // Peak #3:
                        if(0.75 < pp && pp < 0.9){
                            dp = (0.016054);
                        }
                        // Peak #4:
                        if(0.9 < pp && pp < 1.05){
                            dp = (0.01725);
                        }
                        // Peak #5:
                        if(1.05 < pp && pp < 1.2){
                            dp = (0.0047734);
                        }
                        // Peak #6:
                        if(1.2 < pp && pp < 1.35){
                            dp = (0.0013196);
                        }
                        // Peak #7:
                        if(1.35 < pp && pp < 1.5){
                            dp = (-0.0015947);
                        }
                        // Peak #8:
                        if(1.5 < pp && pp < 1.65){
                            dp = (-0.0039695);
                        }
                        // Peak #9:
                        if(1.65 < pp && pp < 1.8){
                            dp = (-0.0058047);
                        }
                        // Peak #10:
                        if(1.8 < pp && pp < 1.95){
                            dp = (-0.0071004);
                        }
                        // Peak #11:
                        if(1.95 < pp && pp < 2.1){
                            dp = (-0.0033565);
                        }
                        // Peak #12:
                        if(2.1 < pp && pp < 2.25){
                            dp = (-0.0080731);
                        }
                        // Peak #13:
                        if(2.25 < pp && pp < 2.4){
                            dp = (-0.0077501);
                        }
                        // Peak #14:
                        if(2.4 < pp && pp < 2.55){
                            dp = (-0.0068876);
                        }
                        // Peak #15:
                        if(2.55 < pp && pp < 2.7){
                            dp = (-0.0054855);
                        }
                        // Peak #16:
                        if(2.7 < pp && pp < 2.85){
                            dp = (-0.0035439);
                        }
                        // Peak #17:
                        if(2.85 < pp && pp < 3.0){
                            dp = (-0.0053436);
                        }
                    }

                    if(sec == 3){
                        // Peak #1:
                        if(0.45 < pp && pp < 0.6){
                            dp = (0.012699);
                        }
                        // Peak #2:
                        if(0.6 < pp && pp < 0.75){
                            dp = (0.01101);
                        }
                        // Peak #3:
                        if(0.75 < pp && pp < 0.9){
                            dp = (0.011971);
                        }
                        // Peak #4:
                        if(0.9 < pp && pp < 1.05){
                            dp = (0.015537);
                        }
                        // Peak #5:
                        if(1.05 < pp && pp < 1.2){
                            dp = (0.011189);
                        }
                        // Peak #6:
                        if(1.2 < pp && pp < 1.35){
                            dp = (0.0073577);
                        }
                        // Peak #7:
                        if(1.35 < pp && pp < 1.5){
                            dp = (0.0040443);
                        }
                        // Peak #8:
                        if(1.5 < pp && pp < 1.65){
                            dp = (0.0012484);
                        }
                        // Peak #9:
                        if(1.65 < pp && pp < 1.8){
                            dp = (-0.0010299);
                        }
                        // Peak #10:
                        if(1.8 < pp && pp < 1.95){
                            dp = (-0.0027908);
                        }
                        // Peak #11:
                        if(1.95 < pp && pp < 2.1){
                            dp = (-0.0040342);
                        }
                        // Peak #12:
                        if(2.1 < pp && pp < 2.25){
                            dp = (-0.00476);
                        }
                        // Peak #13:
                        if(2.25 < pp && pp < 2.4){
                            dp = (-0.0049684);
                        }
                        // Peak #14:
                        if(2.4 < pp && pp < 2.55){
                            dp = (-0.0046593);
                        }
                        // Peak #15:
                        if(2.55 < pp && pp < 2.7){
                            dp = (-0.0093326);
                        }
                        // Peak #16:
                        if(2.7 < pp && pp < 2.85){
                            dp = (0.011011);
                        }
                        // Peak #17:
                        if(2.85 < pp && pp < 3.0){
                            dp = (-6.2688e-04);
                        }
                    }

                    if(sec == 4){
                        // Peak #1:
                        if(0.45 < pp && pp < 0.6){
                            dp = (0.012989);
                        }
                        // Peak #2:
                        if(0.6 < pp && pp < 0.75){
                            dp = (0.011151);
                        }
                        // Peak #3:
                        if(0.75 < pp && pp < 0.9){
                            dp = (0.012188);
                        }
                        // Peak #4:
                        if(0.9 < pp && pp < 1.05){
                            dp = (0.013715);
                        }
                        // Peak #5:
                        if(1.05 < pp && pp < 1.2){
                            dp = (0.018279);
                        }
                        // Peak #6:
                        if(1.2 < pp && pp < 1.35){
                            dp = (0.005456);
                        }
                        // Peak #7:
                        if(1.35 < pp && pp < 1.5){
                            dp = (0.001913);
                        }
                        // Peak #8:
                        if(1.5 < pp && pp < 1.65){
                            dp = (0.0076526);
                        }
                        // Peak #9:
                        if(1.65 < pp && pp < 1.8){
                            dp = (-0.003086);
                        }
                        // Peak #10:
                        if(1.8 < pp && pp < 1.95){
                            dp = (-0.0070247);
                        }
                        // Peak #11:
                        if(1.95 < pp && pp < 2.1){
                            dp = (-4.4125e-04);
                        }
                        // Peak #12:
                        if(2.1 < pp && pp < 2.25){
                            dp = (-0.0025763);
                        }
                        // Peak #13:
                        if(2.25 < pp && pp < 2.4){
                            dp = (-0.00443);
                        }
                        // Peak #14:
                        if(2.4 < pp && pp < 2.55){
                            dp = (-0.0060022);
                        }
                        // Peak #15:
                        if(2.55 < pp && pp < 2.7){
                            dp = (-0.007293);
                        }
                        // Peak #16:
                        if(2.7 < pp && pp < 2.85){
                            dp = (-0.0083023);
                        }
                        // Peak #17:
                        if(2.85 < pp && pp < 3.0){
                            dp = (-0.0090302);
                        }
                    }

                    if(sec == 5){
                        // Peak #1:
                        if(0.45 < pp && pp < 0.6){
                            dp = (0.017734);
                        }
                        // Peak #2:
                        if(0.6 < pp && pp < 0.75){
                            dp = (0.017964);
                        }
                        // Peak #3:
                        if(0.75 < pp && pp < 0.9){
                            dp = (0.022542);
                        }
                        // Peak #4:
                        if(0.9 < pp && pp < 1.05){
                            dp = (0.0076657);
                        }
                        // Peak #5:
                        if(1.05 < pp && pp < 1.2){
                            dp = (-0.0028627);
                        }
                        // Peak #6:
                        if(1.2 < pp && pp < 1.35){
                            dp = (-0.016175);
                        }
                        // Peak #7:
                        if(1.35 < pp && pp < 1.5){
                            dp = (-0.017377);
                        }
                        // Peak #8:
                        if(1.5 < pp && pp < 1.65){
                            dp = (-0.018463);
                        }
                        // Peak #9:
                        if(1.65 < pp && pp < 1.8){
                            dp = (-0.019434);
                        }
                        // Peak #10:
                        if(1.8 < pp && pp < 1.95){
                            dp = (-0.020289);
                        }
                        // Peak #11:
                        if(1.95 < pp && pp < 2.1){
                            dp = (-0.021029);
                        }
                        // Peak #12:
                        if(2.1 < pp && pp < 2.25){
                            dp = (-0.012653);
                        }
                        // Peak #13:
                        if(2.25 < pp && pp < 2.4){
                            dp = (-0.022162);
                        }
                        // Peak #14:
                        if(2.4 < pp && pp < 2.55){
                            dp = (-0.022555);
                        }
                        // Peak #15:
                        if(2.55 < pp && pp < 2.7){
                            dp = (-0.022833);
                        }
                        // Peak #16:
                        if(2.7 < pp && pp < 2.85){
                            dp = (-0.022995);
                        }
                        // Peak #17:
                        if(2.85 < pp && pp < 3.0){
                            dp = (-0.018542);
                        }
                    }

                    if(sec == 6){
                        // Peak #1:
                        if(0.45 < pp && pp < 0.6){
                            dp = (0.02485);
                        }
                        // Peak #2:
                        if(0.6 < pp && pp < 0.75){
                            dp = (0.019982);
                        }
                        // Peak #3:
                        if(0.75 < pp && pp < 0.9){
                            dp = (0.013933);
                        }
                        // Peak #4:
                        if(0.9 < pp && pp < 1.05){
                            dp = (0.017751);
                        }
                        // Peak #5:
                        if(1.05 < pp && pp < 1.2){
                            dp = (0.018378);
                        }
                        // Peak #6:
                        if(1.2 < pp && pp < 1.35){
                            dp = (-0.0015799);
                        }
                        // Peak #7:
                        if(1.35 < pp && pp < 1.5){
                            dp = (-0.0052446);
                        }
                        // Peak #8:
                        if(1.5 < pp && pp < 1.65){
                            dp = (-0.0085877);
                        }
                        // Peak #9:
                        if(1.65 < pp && pp < 1.8){
                            dp = (-0.011609);
                        }
                        // Peak #10:
                        if(1.8 < pp && pp < 1.95){
                            dp = (-0.014309);
                        }
                        // Peak #11:
                        if(1.95 < pp && pp < 2.1){
                            dp = (-0.016687);
                        }
                        // Peak #12:
                        if(2.1 < pp && pp < 2.25){
                            dp = (-0.018743);
                        }
                        // Peak #13:
                        if(2.25 < pp && pp < 2.4){
                            dp = (-0.020478);
                        }
                        // Peak #14:
                        if(2.4 < pp && pp < 2.55){
                            dp = (-0.021891);
                        }
                        // Peak #15:
                        if(2.55 < pp && pp < 2.7){
                            dp = (-0.022983);
                        }
                        // Peak #16:
                        if(2.7 < pp && pp < 2.85){
                            dp = (-0.025752);
                        }
                        // Peak #17:
                        if(2.85 < pp && pp < 3.0){
                            dp = (-0.026201);
                        }
                    }
                }
                
            }


            ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //===================================================================================================================================================================//
            //==============================//==============================//     End of Proton Corrections     //==============================//==============================//
            //===================================================================================================================================================================//
            ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



            return dp/pp;
        };



        """



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



    ######################################################################################################
    ##==================================================================================================##
    ##==============##============##         Outbending Corrections         ##============##============##
    ##==================================================================================================##
    ######################################################################################################


    ############################################################
    #----------#     Last updated on: 5-23-2023     #----------#
    ############################################################


    if(datatype == "Outbending"):

        Correction_Code_Full_Out = """
        
        auto dppC = [&](float Px, float Py, float Pz, int sec, int ivec, int corEl, int corPip, int corPim, int corPro)
        {
            // ivec = 0 --> Electron Corrections
            // ivec = 1 --> Pi+ Corrections
            // ivec = 2 --> Pi- Corrections
            // ivec = 3 --> Proton Corrections

            // corEl ==> Gives the 'generation' of the electron correction
                // corEl == 0 --> No Correction
                // corEl == 1 --> Old Version of Corrections
                // corEl == 2 --> Extended Version of Corrections (Initial/test versions)
                // corEl == 3 --> Final Extended Version of Corrections (Final Refinement)

            // corPip ==> Gives the 'generation' of the π+ Pion correction
                // corPip == 0 --> No Correction
                // corPip == 1 --> Old Version of Corrections
                // corPip == 2 --> Extended Version of Corrections (Initial/test versions) - Uses corEl = 2 (or 3)
                // corPip == 3 --> Final (Extended) Version of Corrections - Uses corEl = 2 (or 3)

            // corPim ==> Gives the 'generation' of the π- Pion correction
                // corPim == 0 --> No Correction
                // corPim == 1 --> Nick's Quadratic Momentum, Quadratic Phi

            // corPro ==> Gives the 'generation' of the Proton correction
                // corPro == 0 --> No Correction
                // corPro == 1 --> Quad Momentum, NO Phi


            // Momentum Magnitude
            double pp = sqrt(Px*Px + Py*Py + Pz*Pz);

            // Initializing the correction factor
            double dp = 0;


            // Defining Phi Angle
            double Phi = (180/3.1415926)*atan2(Py, Px);


            // (Initial) Shift of the Phi Angle (done to realign sectors whose data is separated when plotted from ±180˚)
            if(((sec == 4 || sec == 3) && Phi < 0) || (sec > 4 && Phi < 90)){
                Phi += 360;
            }

            // Getting Local Phi Angle
            double PhiLocal = Phi - (sec - 1)*60;

            // Applying Shift Functions to Phi Angles (local shifted phi = phi)
            double phi = PhiLocal;

            // For Electron Shift
            if(ivec == 0){
                phi = PhiLocal - 30/pp;
            }

            // For π+ Pion/Proton Shift
            if(ivec == 1 || ivec == 3){
                phi = PhiLocal + (32/(pp-0.05));
            }

            // For π- Pion Shift
            if(ivec == 2){
                phi = PhiLocal - (32/(pp-0.05));
            }


            ////////////////////////////////////////////////////////////////////////////////////////////////
            //===============//===============//     No Corrections     //===============//===============//
            ////////////////////////////////////////////////////////////////////////////////////////////////

            if(corEl == 0  && ivec == 0){ // No Electron Correction
                dp = 0;
            }
            if(corPip == 0 && ivec == 1){ // No π+ Correction
                dp = 0;
            }
            if(corPim == 0 && ivec == 2){ // No π- Correction
                dp = 0;
            }
            if(corPro == 0 && ivec == 3){ // No Proton Correction
                dp = 0;
            }

            //////////////////////////////////////////////////////////////////////////////////////////////////
            //==============//==============//     No Corrections (End)     //==============//==============//
            //////////////////////////////////////////////////////////////////////////////////////////////////
            


            //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //==================================================================================================================================//
            //=======================//=======================//     Electron Corrections     //=======================//=======================//
            //==================================================================================================================================//
            //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

            if(ivec == 0 && corEl != 0){
                // Old Corrections (mmF)
                if(sec == 1){
                    dp = ((-7.68e-06)*phi*phi + (4.636e-05)*phi + (4.7165e-04))*pp*pp + ((1.2086e-04)*phi*phi + (2.09591e-05)*phi + (-0.01582))*pp + ((-4.1002e-04)*phi*phi + (1.7298e-04)*phi + (0.10544));
                    dp = dp + ((7.51e-06)*phi*phi + (6.45e-06)*phi + (-0.00152778))*pp*pp + ((-0.00011089)*phi*phi + (-0.00017683)*phi + (0.02131197))*pp + ((0.00037962)*phi*phi + (0.00060197)*phi + (-0.06886547));                    
                }
                if(sec == 2){
                    dp = ((-2.69e-06)*phi*phi + (9.252e-05)*phi + (5.1693e-04))*pp*pp + ((3.016e-05)*phi*phi + (-6.0141e-04)*phi + (-0.0146))*pp + ((-6.09e-05)*phi*phi + (1.604e-03)*phi + (0.09208));
                    dp = dp + ((1.24e-06)*phi*phi + (-4.735e-05)*phi + (-0.00150312))*pp*pp + ((-2.097e-05)*phi*phi + (0.00049518)*phi + (0.01920915))*pp + ((7.474e-05)*phi*phi + (-0.00132086)*phi + (-0.05686766));                    
                }
                if(sec == 3){
                    dp = ((-1.045e-05)*phi*phi + (-6.491e-05)*phi + (1.1362e-03))*pp*pp + ((1.2512e-04)*phi*phi + (5.3421e-04)*phi + (-0.0174))*pp + ((-3.0891e-04)*phi*phi + (-1.5332e-03)*phi + (0.09389));
                    dp = dp + ((6.94e-06)*phi*phi + (4.271e-05)*phi + (-0.00182765))*pp*pp + ((-8.322e-05)*phi*phi + (-0.00042238)*phi + (0.01994986))*pp + ((0.00021956)*phi*phi + (0.00103844)*phi + (-0.04956505));                    
                }
                if(sec == 4){
                    dp = ((-7.37e-06)*phi*phi + (-8.13e-06)*phi + (9.2425e-04))*pp*pp + ((1.1312e-04)*phi*phi + (-5.24444e-05)*phi + (-0.022944))*pp + ((-3.518e-04)*phi*phi + (3.1893e-04)*phi + (0.1323));
                    dp = dp + ((8.74e-06)*phi*phi + (-1.617e-05)*phi + (-0.00173764))*pp*pp + ((-0.00011774)*phi*phi + (0.00024329)*phi + (0.02310896))*pp + ((0.00036368)*phi*phi + (-0.00076238)*phi + (-0.07050779));
                }
                if(sec == 5){
                    dp = ((-8.17e-06)*phi*phi + (-1.681e-05)*phi + (7.8066e-04))*pp*pp + ((1.4176e-04)*phi*phi + (4.1096e-04)*phi + (-0.026944))*pp + ((-4.4153e-04)*phi*phi + (-1.3535e-03)*phi + (0.1486));
                    dp = dp + ((7.69e-06)*phi*phi + (1.774e-05)*phi + (-1.57552e-03))*pp*pp + ((-1.0778e-04)*phi*phi + (-2.6133e-04)*phi + (0.02076174))*pp + ((3.196e-04)*phi*phi + (8.8134e-04)*phi + (-0.06204126));
                }
                if(sec == 6){
                    dp = ((1.63e-06)*phi*phi + (6.251e-05)*phi + (-2.2457e-04))*pp*pp + ((8.18e-06)*phi*phi + (-6.688e-04)*phi + (4.2875e-04))*pp + ((-2.172e-05)*phi*phi + (1.5467e-03)*phi + (0.05676));
                    dp = dp + ((1.34e-06)*phi*phi + (-1.574e-05)*phi + (-0.00133653))*pp*pp + ((-1.991e-05)*phi*phi + (0.00024404)*phi + (0.01428837))*pp + ((5.149e-05)*phi*phi + (-0.0007992)*phi + (-0.03467815));
                }
                
                // Extended Corrections Test (mmExF)
                if(corEl == 2){
                    if(sec == 1){
                        dp =       ((2.6957e-06)*phi*phi + (1.41185e-05)*phi + (-8.54848e-04))*pp*pp + ((-4.3470e-05)*phi*phi + (3.66281e-04)*phi +  (0.01007791))*pp +  ((1.9932e-04)*phi*phi + (-8.11713e-04)*phi + (-0.008384375));
                        dp = dp + ((-7.6847e-06)*phi*phi +  (4.1267e-05)*phi +  (-7.4240e-04))*pp*pp +  ((1.2218e-04)*phi*phi + (-4.9847e-04)*phi +   (0.0088033))*pp + ((-4.9434e-04)*phi*phi +     (0.001114)*phi + (-0.021955));
                        dp = dp +  ((1.3641e-05)*phi*phi + (-1.5731e-05)*phi +  (-8.7395e-04))*pp*pp + ((-1.8416e-04)*phi*phi +  (9.9110e-05)*phi +    (0.010497))*pp +  ((6.2267e-04)*phi*phi +   (2.5877e-04)*phi + (-0.028027));
                        dp = dp + ((-7.3331e-06)*phi*phi +  (2.9512e-06)*phi +   (1.4857e-04))*pp*pp +  ((9.4041e-05)*phi*phi +  (5.5267e-05)*phi + (-5.8894e-04))*pp + ((-3.0270e-04)*phi*phi +  (-5.5944e-04)*phi + (-0.0034499));
                    }
                    if(sec == 1){
                        dp =      ((1.31890e-06)*phi*phi + (4.26057e-05)*phi + (-0.002322628))*pp*pp + ((-1.140900000e-05)*phi*phi + (2.218800000e-05)*phi + (0.02878927))*pp + ((2.495000000e-05)*phi*phi + (1.617000000e-06)*phi + (-0.061816275));
                    }
                    if(sec == 2){
                        dp =      ((-5.7393e-06)*phi*phi + (-1.217322e-05)*phi + (-3.59798e-04))*pp*pp +  ((6.3547e-05)*phi*phi + (6.47806e-04)*phi + (0.00561929))*pp + ((-1.51718e-04)*phi*phi +  (-0.00195272)*phi + (-0.0100398));
                        dp = dp +  ((7.0884e-06)*phi*phi +    (8.7982e-06)*phi +   (-0.0010783))*pp*pp + ((-1.0109e-04)*phi*phi + (-1.1700e-04)*phi +   (0.012013))*pp +   ((3.3792e-04)*phi*phi +   (2.8723e-04)*phi + (-0.025106));
                        dp = dp + ((-1.6415e-06)*phi*phi +    (3.6995e-06)*phi +  (-4.1021e-04))*pp*pp +  ((3.7988e-05)*phi*phi + (-5.4482e-05)*phi +  (0.0045624))*pp +  ((-1.7928e-04)*phi*phi +   (1.3032e-04)*phi + (-0.01276));
                    }
                    if(sec == 3){
                        dp =     ((-4.84189e-06)*phi*phi + (-2.772552e-05)*phi + (-5.87211e-04))*pp*pp + ((5.40286e-05)*phi*phi + (1.739683e-04)*phi + (0.01062548))*pp + ((-9.6672e-05)*phi*phi + (-3.63641e-04)*phi + (-0.01983092));
                        dp = dp +  ((7.5610e-06)*phi*phi +    (4.4297e-05)*phi +    (-0.001235))*pp*pp + ((-1.0371e-04)*phi*phi +  (-5.5008e-04)*phi +   (0.015016))*pp +  ((2.9442e-04)*phi*phi +    (0.0013219)*phi + (-0.038352));
                    }
                    if(sec == 4){
                        dp =      ((9.2070e-07)*phi*phi + (-3.1801e-05)*phi + (-9.9342e-04))*pp*pp + ((-5.6000e-06)*phi*phi + (3.37922e-04)*phi + (0.0127541))*pp + ((1.9148e-05)*phi*phi + (-0.001328248)*phi + (-0.01868997));
                        dp = dp + ((9.8896e-07)*phi*phi +  (7.0400e-06)*phi +  (-0.0013222))*pp*pp + ((-1.8327e-05)*phi*phi + (-1.1266e-04)*phi +  (0.016429))*pp + ((6.1367e-05)*phi*phi +   (6.8615e-04)*phi + (-0.042902));
                    }
                    if(sec == 5){
                        dp =    ((9.3229677e-06)*phi*phi + (3.51099e-05)*phi + (-0.0021918953))*pp*pp + ((-1.220143e-04)*phi*phi + (-3.22997e-04)*phi + (0.02648059))*pp + ((3.96753e-04)*phi*phi + (7.7590e-04)*phi + (-0.0807585));
                        dp = dp + ((-1.2999e-05)*phi*phi +  (5.3299e-06)*phi +   (-4.8562e-06))*pp*pp +    ((1.7110e-04)*phi*phi +  (-1.1444e-04)*phi + (-0.0015372))*pp + ((-5.0501e-04)*phi*phi + (6.8521e-04)*phi + (0.01591));
                    }
                    if(sec == 6){
                        dp =     ((2.503612e-06)*phi*phi + (2.68581e-05)*phi + (-0.00139564))*pp*pp + ((-2.2352e-05)*phi*phi + (-2.05667e-04)*phi + (0.0233939))*pp + ((1.02934e-04)*phi*phi +  (6.1117e-04)*phi + (-0.059224)); 
                        dp = dp + ((-2.5661e-06)*phi*phi + (-4.5408e-06)*phi + (-8.7958e-04))*pp*pp +  ((4.0724e-05)*phi*phi +   (1.3044e-04)*phi + (0.0092421))*pp + ((-1.6950e-04)*phi*phi + (-8.5567e-04)*phi + (-0.013069));
                    }
                }
                
                // Final (Refined) Extended Corrections (mmEF)
                if(corEl == 3){
                    if(sec == 1){
                        dp =     ((1.3189e-06)*phi*phi +  (4.26057e-05)*phi +  (-0.002322628))*pp*pp +  ((-1.1409e-05)*phi*phi +    (2.2188e-05)*phi + (0.02878927))*pp +   ((2.4950e-05)*phi*phi +   (1.6170e-06)*phi + (-0.061816275));
                    }
                    if(sec == 2){
                        dp =    ((-2.9240e-07)*phi*phi +   (3.2448e-07)*phi +  (-0.001848308))*pp*pp +   ((4.4500e-07)*phi*phi +   (4.76324e-04)*phi + (0.02219469))*pp +   ((6.9220e-06)*phi*phi +  (-0.00153517)*phi + (-0.0479058));
                    }
                    if(sec == 3){
                        dp =    ((2.71911e-06)*phi*phi + (1.657148e-05)*phi +  (-0.001822211))*pp*pp + ((-4.96814e-05)*phi*phi + (-3.761117e-04)*phi + (0.02564148))*pp +  ((1.97748e-04)*phi*phi +  (9.58259e-04)*phi + (-0.05818292));
                    }
                    if(sec == 4){
                        dp =    ((1.90966e-06)*phi*phi +  (-2.4761e-05)*phi +   (-0.00231562))*pp*pp +  ((-2.3927e-05)*phi*phi +   (2.25262e-04)*phi +  (0.0291831))*pp +   ((8.0515e-05)*phi*phi + (-6.42098e-04)*phi + (-0.06159197));
                    }
                    if(sec == 5){
                        dp = ((-3.6760323e-06)*phi*phi +  (4.04398e-05)*phi + (-0.0021967515))*pp*pp +  ((4.90857e-05)*phi*phi +  (-4.37437e-04)*phi + (0.02494339))*pp + ((-1.08257e-04)*phi*phi +   (0.00146111)*phi + (-0.0648485));
                    }
                    if(sec == 6){
                        dp =    ((-6.2488e-08)*phi*phi +  (2.23173e-05)*phi +   (-0.00227522))*pp*pp +   ((1.8372e-05)*phi*phi +   (-7.5227e-05)*phi +   (0.032636))*pp +  ((-6.6566e-05)*phi*phi +  (-2.4450e-04)*phi + (-0.072293));
                    }
                }

            }

            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //====================================================================================================================================//
            //======================//======================//     Electron Corrections (End)     //======================//======================//
            //====================================================================================================================================//
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //====================================================================================================================================//
            //=========================//=========================//     π+ Corrections     //=========================//=========================//
            //====================================================================================================================================//
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

            if(ivec == 1 && corPip != 0){
            
                // Old Corrections (PipMMF)
                if(sec == 1){
                    dp = ((5.7e-07)*phi*phi + (-2.531e-05)*phi + (3.2253e-04))*pp*pp + ((2.12e-06)*phi*phi + (-3.6741e-04)*phi + (-0.01378))*pp + ((-1.215e-05)*phi*phi + (4.275e-04)*phi + (0.04561));
                    dp = dp + ((-2.12e-06)*phi*phi + (3.185e-05)*phi + (0.00178389))*pp*pp + ((1.262e-05)*phi*phi + (-0.00012324)*phi + (-0.01494883))*pp + ((-1.422e-05)*phi*phi + (0.00021045)*phi + (0.02590949));
                }
                if(sec == 2){
                    dp = ((-4e-08)*phi*phi + (-9.836e-05)*phi + (3.142e-04))*pp*pp + ((8.6e-07)*phi*phi + (4.6073e-04)*phi + (-0.0136))*pp + ((8.09e-06)*phi*phi + (-6.0253e-04)*phi + (0.03594));
                    dp = dp + ((-9.8e-07)*phi*phi + (3.974e-05)*phi + (0.00159441))*pp*pp + ((6.61e-06)*phi*phi + (-0.00023934)*phi + (-0.01295355))*pp + ((-1.087e-05)*phi*phi + (0.00027704)*phi + (0.02013232));
                }
                if(sec == 3){
                    dp = ((-1.37e-06)*phi*phi + (3.759e-05)*phi + (7.4895e-04))*pp*pp + ((8.45e-06)*phi*phi + (1.464e-04)*phi + (-0.01952))*pp + ((-1.41e-06)*phi*phi + (-3.5781e-04)*phi + (0.0353));
                    dp = dp + ((-3.2e-07)*phi*phi + (-2.98e-06)*phi + (0.00144252))*pp*pp + ((2.9e-06)*phi*phi + (-5.719e-05)*phi + (-0.01197579))*pp + ((-5.74e-06)*phi*phi + (0.00024614)*phi + (0.02228774));
                }
                if(sec == 4){
                    dp = ((2.7e-06)*phi*phi + (5.028e-05)*phi + (9.007e-04))*pp*pp + ((-1.548e-05)*phi*phi + (-6.141e-05)*phi + (-0.0151))*pp + ((2.063e-05)*phi*phi + (1.7882e-04)*phi + (0.03522));
                    dp = dp + ((-8.2e-07)*phi*phi + (-2.606e-05)*phi + (0.00102121))*pp*pp + ((6.32e-06)*phi*phi + (0.00013252)*phi + (-0.00898872))*pp + ((-9.79e-06)*phi*phi + (-0.00017861)*phi + (0.01654247));
                }
                if(sec == 5){
                    dp = ((2.2e-06)*phi*phi + (-1.554e-05)*phi + (5.465e-04))*pp*pp + ((-1.06e-05)*phi*phi + (1.226e-04)*phi + (-0.01651))*pp + ((1.039e-05)*phi*phi + (-2.062e-04)*phi + (0.0436));
                    dp = dp + ((-5.8e-07)*phi*phi + (-1.4e-07)*phi + (0.00129068))*pp*pp + ((5.43e-06)*phi*phi + (-2.262e-05)*phi + (-0.01076443))*pp + ((-7.78e-06)*phi*phi + (0.00010021)*phi + (0.01975448));
                }
                if(sec == 6){
                    dp = ((1.11e-06)*phi*phi + (-1e-08)*phi + (6.88e-05))*pp*pp + ((-8.86e-06)*phi*phi + (-5.94e-05)*phi + (-0.01133))*pp + ((1.919e-05)*phi*phi + (-2.444e-04)*phi + (0.03491));
                    dp = dp + ((-1.15e-06)*phi*phi + (6.34e-06)*phi + (0.00196799))*pp*pp + ((1.196e-05)*phi*phi + (-0.00010685)*phi + (-0.01774286))*pp + ((-2.573e-05)*phi*phi + (0.00042626)*phi + (0.03688378));
                }
                
                // Extended Corrections Test (PipMMExF)
                if(corPip == 2){
                    if(sec == 1){
                        dp =      ((-5.5619e-07)*phi*phi +  (1.2176e-05)*phi +   (0.0019766))*pp*pp +  ((2.2974e-06)*phi*phi + (-3.2344e-04)*phi +  (-0.018279))*pp + ((-3.3287e-06)*phi*phi +  (1.2371e-04)*phi + (0.037557));
                        dp = dp + ((-1.1071e-07)*phi*phi +  (1.1611e-05)*phi + (-6.8815e-04))*pp*pp + ((-2.2037e-06)*phi*phi + (-1.8548e-04)*phi +  (0.0055018))*pp +  ((2.3393e-07)*phi*phi +  (1.2655e-04)*phi + (-0.0055127));
                        dp = dp + ((-1.0665e-06)*phi*phi + (-9.2758e-06)*phi +  (2.1876e-04))*pp*pp +  ((6.5297e-06)*phi*phi +  (2.7729e-05)*phi + (-0.0010923))*pp + ((-1.4148e-07)*phi*phi +  (2.9491e-05)*phi + (-0.0043183));
                    }
                    if(sec == 2){
                        dp =      ((-3.0769e-06)*phi*phi +  (5.2387e-06)*phi +   (0.0025674))*pp*pp +  ((1.8124e-05)*phi*phi + (-1.7621e-04)*phi +  (-0.020154))*pp + ((-1.2558e-05)*phi*phi +  (1.2769e-04)*phi + (0.033566));
                        dp = dp + ((-1.2998e-06)*phi*phi + (-2.7296e-05)*phi + (-1.2792e-04))*pp*pp +  ((6.8931e-06)*phi*phi +  (1.6941e-04)*phi +  (0.0013802))*pp + ((-8.9689e-06)*phi*phi + (-2.5644e-04)*phi + (-0.0032964));
                        dp = dp + ((-9.8764e-08)*phi*phi + (-1.9100e-05)*phi + (-3.9391e-04))*pp*pp + ((-3.3432e-07)*phi*phi +  (1.0039e-04)*phi +  (0.0033748))*pp +  ((5.3722e-06)*phi*phi + (-1.1331e-04)*phi + (-0.0070953));
                    }
                    if(sec == 3){
                        dp =       ((1.3125e-06)*phi*phi + (-5.9180e-05)*phi +   (0.0014564))*pp*pp + ((-7.2451e-06)*phi*phi +  (6.3174e-04)*phi +  (-0.017146))*pp +  ((1.0599e-05)*phi*phi + (-8.1889e-04)*phi + (0.029497));
                        dp = dp + ((-1.7131e-06)*phi*phi +  (5.7922e-05)*phi +  (5.9580e-04))*pp*pp +  ((1.1049e-05)*phi*phi + (-2.7280e-04)*phi + (-0.0039213))*pp + ((-8.5944e-06)*phi*phi +  (2.8071e-04)*phi + (-1.3545e-04));
                        dp = dp + ((-4.0314e-07)*phi*phi +  (4.1308e-06)*phi + (-5.3057e-04))*pp*pp +  ((1.3308e-06)*phi*phi +  (1.2769e-05)*phi +  (0.0044938))*pp +  ((2.0059e-06)*phi*phi +  (9.1931e-06)*phi + (-0.0076076));
                    }
                    if(sec == 4){
                        dp =      ((-3.3265e-07)*phi*phi + (-3.0209e-05)*phi +    (0.001713))*pp*pp +  ((7.3058e-06)*phi*phi +  (3.1596e-04)*phi +  (-0.017057))*pp + ((-1.3587e-05)*phi*phi + (-2.3543e-04)*phi + (0.034361));
                        dp = dp +  ((9.2471e-07)*phi*phi +  (7.2685e-06)*phi + (-1.4055e-05))*pp*pp + ((-8.2856e-06)*phi*phi +  (1.0956e-05)*phi +  (0.0013298))*pp +  ((1.1312e-05)*phi*phi + (-3.6642e-05)*phi + (-0.004602));
                        dp = dp + ((-1.2205e-06)*phi*phi +  (1.4853e-05)*phi +  (2.6654e-04))*pp*pp +  ((8.0883e-06)*phi*phi + (-8.1258e-05)*phi + (-0.0017054))*pp + ((-6.7779e-06)*phi*phi + (-4.1304e-05)*phi + (0.0013179));
                        dp = dp +  ((2.4054e-07)*phi*phi + (-3.9757e-05)*phi +  (3.5924e-04))*pp*pp + ((-3.0307e-07)*phi*phi +  (3.2370e-04)*phi + (-0.0024836))*pp + ((-3.9735e-06)*phi*phi + (-2.7823e-04)*phi + (9.4398e-04));
                    }
                    if(sec == 5){
                        dp =       ((4.9522e-08)*phi*phi +  (1.6615e-06)*phi +   (0.0013238))*pp*pp + ((-7.7824e-07)*phi*phi + (-1.8424e-05)*phi +  (-0.013754))*pp +  ((6.2245e-06)*phi*phi +  (5.4907e-05)*phi + (0.027401));
                        dp = dp +  ((8.9196e-08)*phi*phi + (-3.7341e-05)*phi +  (1.5161e-05))*pp*pp +  ((3.2196e-06)*phi*phi +  (3.1272e-04)*phi + (-0.0012442))*pp + ((-9.1313e-06)*phi*phi + (-5.1308e-04)*phi + (0.0042737));
                        dp = dp +  ((2.0598e-06)*phi*phi +  (2.0426e-05)*phi + (-1.5120e-04))*pp*pp + ((-1.2444e-05)*phi*phi + (-1.3032e-04)*phi + (7.0147e-04))*pp +  ((1.2403e-05)*phi*phi +  (7.1482e-05)*phi + (-0.0013052));
                    }
                    if(sec == 6){
                        dp =      ((-1.1641e-06)*phi*phi +  (3.6397e-05)*phi +   (0.0017669))*pp*pp +  ((1.2615e-05)*phi*phi + (-3.1012e-04)*phi +  (-0.018168))*pp + ((-1.9665e-05)*phi*phi +  (6.8981e-05)*phi + (0.038744));
                        dp = dp + ((-4.7604e-08)*phi*phi + (-8.9182e-06)*phi + (-9.4440e-05))*pp*pp + ((-1.9801e-06)*phi*phi +  (2.6388e-05)*phi +  (0.0014914))*pp +  ((5.5219e-06)*phi*phi + (-9.8614e-05)*phi + (-0.0038784));
                        dp = dp +  ((8.1876e-07)*phi*phi + (-1.2894e-05)*phi + (-4.6578e-04))*pp*pp + ((-6.8450e-06)*phi*phi +  (8.5513e-05)*phi +  (0.0035454))*pp +  ((1.0147e-05)*phi*phi + (-1.0325e-04)*phi + (-0.0054159));
                    }
                }
                
                // Final (Refined) Extended Corrections (PipMMEF)
                if(corPip == 3){
                    if(sec == 1){
                        dp =   ((-1.7334e-06)*phi*phi +  (1.45112e-05)*phi +  (0.00150721))*pp*pp +    ((6.6234e-06)*phi*phi + (-4.81191e-04)*phi +  (-0.0138695))*pp + ((-3.23625e-06)*phi*phi +   (2.79751e-04)*phi + (0.027726));
                    }
                    if(sec == 2){
                        dp = ((-4.475464e-06)*phi*phi + (-4.11573e-05)*phi +  (0.00204557))*pp*pp +  ((2.468278e-05)*phi*phi +   (9.3590e-05)*phi +   (-0.015399))*pp + ((-1.61547e-05)*phi*phi +   (-2.4206e-04)*phi + (0.0231743));
                    }
                    if(sec == 3){
                        dp =   ((-8.0374e-07)*phi*phi +   (2.8728e-06)*phi +  (0.00152163))*pp*pp +    ((5.1347e-06)*phi*phi +  (3.71709e-04)*phi +  (-0.0165735))*pp +   ((4.0105e-06)*phi*phi + (-5.289869e-04)*phi + (0.02175395));
                    }
                    if(sec == 4){
                        dp =   ((-3.8790e-07)*phi*phi + (-4.78445e-05)*phi + (0.002324725))*pp*pp +   ((6.80543e-06)*phi*phi +  (5.69358e-04)*phi +  (-0.0199162))*pp + ((-1.30264e-05)*phi*phi +  (-5.91606e-04)*phi + (0.03202088));
                    }
                    if(sec == 5){
                        dp =  ((2.198518e-06)*phi*phi + (-1.52535e-05)*phi + (0.001187761))*pp*pp + ((-1.000264e-05)*phi*phi +  (1.63976e-04)*phi + (-0.01429673))*pp +   ((9.4962e-06)*phi*phi +  (-3.86691e-04)*phi + (0.0303695));
                    }
                    if(sec == 6){
                        dp =  ((-3.92944e-07)*phi*phi +  (1.45848e-05)*phi +  (0.00120668))*pp*pp +    ((3.7899e-06)*phi*phi + (-1.98219e-04)*phi +  (-0.0131312))*pp +  ((-3.9961e-06)*phi*phi +  (-1.32883e-04)*phi + (0.0294497));
                    }
                }

            }

            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //====================================================================================================================================//
            //=======================//=======================//      π+ Corrections (End)      //=======================//=======================//
            //====================================================================================================================================//
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            
            
            
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //====================================================================================================================================//
            //=========================//=========================//     π- Corrections     //=========================//=========================//
            //====================================================================================================================================//
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

            if(ivec == 2 && corPim != 0){
                if(sec == 1){
                    dp = ((2.7123584594392597e-06)*phi*phi + (-5.468601175954242e-05)*phi + (0.002313330256974031))*pp*pp + ((-8.039703360516874e-06)*phi*phi + (0.00044464879674067275)*phi + (-0.02546911446157775))*pp + ((3.5973669277966655e-06)*phi*phi + (-0.0003856844699023182)*phi + (0.05496480659602064) - 0.015);
                }
                if(sec == 2){
                    dp = ((1.9081500905303347e-06)*phi*phi + (3.310647986349362e-05)*phi + (-0.0003264357817968204))*pp*pp + ((-1.2306311457915714e-05)*phi*phi + (-6.404982516446639e-05)*phi + (-0.01287404671840319))*pp + ((9.746651642120768e-06)*phi*phi + (6.1503461629194e-05)*phi + (0.04249861359511857) - 0.015);
                }
                if(sec == 3){
                    dp = ((3.467960715633796e-06)*phi*phi + (-0.00011427345789836184)*phi + (0.004780571116355615))*pp*pp + ((-1.2639455891842017e-05)*phi*phi + (0.00044737258600913664)*phi + (-0.03827009444373719))*pp + ((5.8243648992776484e-06)*phi*phi + (-0.0004240381542174731)*phi + (0.06589846610477122) - 0.015);
                }
                if(sec == 4){
                    dp = ((-7.97757466039691e-06)*phi*phi + (-0.00011075801628158914)*phi + (0.006505144041475733))*pp*pp + ((3.570788801587046e-05)*phi*phi + (0.0005835525352273808)*phi + (-0.045031773715754606))*pp + ((-3.223327114068019e-05)*phi*phi + (-0.0006144362450858762)*phi + (0.07280937684254037) - 0.015);
                }
                if(sec == 5){
                    dp = ((1.990802625607816e-06)*phi*phi + (7.057771450607931e-05)*phi + (0.005399025205722829))*pp*pp + ((-7.670376562908147e-06)*phi*phi + (-0.00032508260930191955)*phi + (-0.044439500813069875))*pp + ((7.599354976329091e-06)*phi*phi + (0.0002562152836894338)*phi + (0.07195292224032898) - 0.015);
                }
                if(sec == 6){
                    dp = ((1.9247834787602347e-06)*phi*phi + (7.638857332736951e-05)*phi + (0.005271258583881754))*pp*pp + ((-2.7349724034956845e-06)*phi*phi + (-0.00016130256163798413)*phi + (-0.03668300882287307))*pp + ((7.40942843287096e-07)*phi*phi + (-5.785254680184232e-05)*phi + (0.06282320712979896) - 0.015);
                }
            }

            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //====================================================================================================================================//
            //=======================//=======================//      π- Corrections (End)      //=======================//=======================//
            //====================================================================================================================================//
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //====================================================================================================================================//
            //========================//========================//     Proton Corrections     //========================//========================//
            //====================================================================================================================================//
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

            if(ivec == 3 && corPro != 0){ // Quadratic Momentum - No Phi Dependence

                if(sec == 1){
                    dp = (-4.30864e-03)*pp*pp + (1.53688e-02)*pp + (-1.66676e-02);                    
                    // From GitHub_F_Pro for GitHub_F2_Pro:
                    // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
                    dp = dp + ((-4.3301e-04)*pp*pp + (1.4483e-03)*pp + (-1.1343e-03));
                }

                if(sec == 2){
                    dp = (-1.29444e-02)*pp*pp + (4.11823e-02)*pp + (-3.4069e-02);                    
                    // From GitHub_F_Pro for GitHub_F2_Pro:
                    // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
                    dp = dp + ((5.2462e-04)*pp*pp + (-1.4881e-03)*pp + (8.0050e-04));
                }

                if(sec == 3){
                    dp = (-9.36605e-03)*pp*pp + (3.25537e-02)*pp + (-3.41826e-02);                    
                    // From GitHub_F_Pro for GitHub_F2_Pro:
                    // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
                    dp = dp + ((-1.9155e-03)*pp*pp + (6.1540e-03)*pp + (-4.0436e-03));
                }

                if(sec == 4){
                    dp = (-1.45314e-02)*pp*pp + (4.97218e-02)*pp + (-4.43198e-02);                    
                    // From GitHub_F_Pro for GitHub_F2_Pro:
                    // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
                    dp = dp + ((5.9258e-04)*pp*pp + (-3.7177e-04)*pp + (-2.3707e-04));
                }

                if(sec == 5){
                    dp = (-1.08441e-02)*pp*pp + (3.89079e-02)*pp + (-3.68669e-02);                    
                    // From GitHub_F_Pro for GitHub_F2_Pro:
                    // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
                    dp = dp + ((-5.5398e-04)*pp*pp + (2.3721e-03)*pp + (-2.3279e-03));
                }

                if(sec == 6){
                    dp = (-4.55633e-03)*pp*pp + (1.75565e-02)*pp + (-1.74574e-02);                    
                    // From GitHub_F_Pro for GitHub_F2_Pro:
                    // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
                    dp = dp + ((-1.1516e-03)*pp*pp + (3.0094e-03)*pp + (-8.2480e-04));
                }
                
            }

            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //====================================================================================================================================//
            //======================//=======================//     Proton Corrections (End)     //=======================//======================//
            //====================================================================================================================================//
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


            return dp/pp;
        };
        
        
        
        """



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
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



    ###########################################################################################################
    ##=======================================================================================================##
    ##==============##============##         Correction Application Code         ##============##============##
    ##=======================================================================================================##
    ###########################################################################################################

    # // corEl ==> Gives the 'generation' of the electron correction
    #     // corEl == 0 --> No Correction
    #     // corEl == 1 --> Quad Momentum - Quad Phi (Final Version)
    #     // corEl == 2 --> Modified Electron Correction with extended range (Created using exsisting corrections (i.e., this is a refinement of those corrections) -- Quad Mom - Quad Phi -- Kinematic Coverage is from 0.95-9.95 GeV using both SP and EO channels)
    #     // corEl == 3 --> New Electron Correction with extended range (Created from Uncorrected Particles -- Quad Mom - Quad Phi -- Kinematic Coverage is from 0.95-9.95 GeV using both SP and EO channels)
    #     // corEl == 4 --> Old Electron Correction with pass2 data (Created from Uncorrected Particles -- Quad Mom -- does not use EO channels)
    #     // corEl == 5 --> New Electron Correction with pass2 data (Created from corEL = 4 Corrections -- Quad Mom -- does not use EO channels)
    def NameElCor(corEl, datatype):
        coutN = 0
        if('mm0' in corEl):
            coutN = 0
        if("mmF" in corEl):
            coutN = 1
        if("mmExF" in corEl):
            coutN = 2
        if("mmEF" in corEl):
            coutN = 3
        if("mmP2" in corEl):
            coutN = 4
        if("mmRP2" in corEl):
            coutN = 5

        return coutN

    # // corPip ==> Gives the 'generation' of the π+ Pion correction
    #     // corPip == 0 --> No Correction
    #     // corPip == 1 --> Quad Momentum, Quad Phi (Old Version)
    #     // corPip == 2 --> Quad Momentum, Quad Phi (Extended - Test - Version)
    #     // corPip == 3 --> Quad Momentum, Quad Phi (Final Version)
    #     // corPip == 4 --> New π+ Pion Correction with pass2 data (Created from Uncorrected π+ Pion -- Quad Mom -- does not use EO channels)
    #     // corPip == 5 --> New π+ Pion Correction with pass2 data (Created from corPip == 4 -- Quad Mom -- Split at p = 4 GeV between two functions)
    def NamePipCor(corPip, datatype):
        coutN = 0
        if("Pip" not in corPip):
            coutN = 0
        else:
            if("PipMMExF" in corPip):
                coutN = 2
            elif("PipMMEF" in corPip):
                coutN = 3
            elif("PipMMP2" in corPip):
                coutN = 4
            elif("PipMMsP2" in corPip):
                coutN = 5
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
        elif("MMpro_EF" in corPro):
            coutN = 2
        elif("MMpro_QEF" in corPro):
            coutN = 3
        elif("MMpro_LEF" in corPro):
            coutN = 4
        # elif("MMpro_REF" in corPro):
        #     coutN = 5
        elif("MMpro_S_LEF" in corPro):
            coutN = 6
        elif("MMpro_SEF" in corPro):
            coutN = 7
        elif("MMpro_SEC" in corPro):
            coutN = 8
        elif("MMpro_SERC" in corPro):
            coutN = 9
        elif("MMpro_SRE" in corPro):
            coutN = 10
        elif("MMpro_SFRE" in corPro):
            coutN = 11
        elif("MMpro_DRE" in corPro):
            coutN = 12
        elif("MMpro_RE" in corPro):
            coutN = 13
        elif("MMpro_FRE" in corPro): # corPro == 14
            coutN = 14
        elif("MMpro_NRE" in corPro): # corPro == 15
            coutN = 15
        elif("MMpro_NS" in corPro): # corPro == 18
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
        
#         if("MC" not in event_Name) else "".join(["""
#     auto fe = dppC(ex0, ey0, ez0, esec, 0, """, str(corEl_Num), """, """, str(corPip_Num), """, """, str(corPim_Num), """, """, str(corPro_Num), """) + 1;
#     auto eleC = ROOT::Math::PxPyPzMVector(ex0*fe, ey0*fe, ez0*fe, 0);
#         """])

        if("P0" not in Channel_Type and "E" not in Channel_Type and ("Mom_el" not in Out_Type and "Mom_pim" not in Out_Type and "Mom_pro" not in Out_Type)):
            Particles_for_Correction = "".join([Particles_for_Correction, """
    auto fpip = dppC(pipx, pipy, pipz, pipsec, 1, """, str(corEl_Num), """, """, str(corPip_Num), """, """, str(corPim_Num), """, """, str(corPro_Num), """) + 1;
    auto pipC = ROOT::Math::PxPyPzMVector(pipx*fpip, pipy*fpip, pipz*fpip, """, str(Particle_Mass_PiC), """);//0.13957);
        """])

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
    
    // auto beam_test      = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
    // auto targ_test      = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_M);
    // 
    // auto cor_Factor     = ((Final_Output)/proC.P()) + 1;
    // auto cor_FactorM    = ((pro_CalculateM - proC.P())/proC.P()) + 1;
    // auto cor_FactorP    = ((pro_CalculateP - proC.P())/proC.P()) + 1;
    // 
    // // auto cor_Factor     = ((pro_Calculate  - pro_cor)/pro_cor);
    // // auto cor_FactorM    = ((pro_CalculateM - pro_cor)/pro_cor);
    // // auto cor_FactorP    = ((pro_CalculateP - pro_cor)/pro_cor);
    // 
    // auto pro_OG         = ROOT::Math::PxPyPzMVector(prox_cor, proy_cor, proz_cor, Proton_M);
    // 
    // auto proC_Calc      = ROOT::Math::PxPyPzMVector(proC.Px()*cor_Factor,  proC.Py()*cor_Factor,  proC.Pz()*cor_Factor,  Proton_M);
    // auto proC_Calc_M    = ROOT::Math::PxPyPzMVector(proC.Px()*cor_FactorM, proC.Py()*cor_FactorM, proC.Pz()*cor_FactorM, Proton_M);
    // auto proC_Calc_P    = ROOT::Math::PxPyPzMVector(proC.Px()*cor_FactorP, proC.Py()*cor_FactorP, proC.Pz()*cor_FactorP, Proton_M);
    // 
    // auto MM2_Vec_OG     = beam_test + targ_test - eleC - pipC - pro_OG;
    // auto MM2_Vector     = beam_test + targ_test - eleC - pipC - proC;
    // auto MM2_Vec_Calc   = beam_test + targ_test - eleC - pipC - proC_Calc;
    // auto MM2_Vec_Cal_M  = beam_test + targ_test - eleC - pipC - proC_Calc_M;
    // auto MM2_Vec_Cal_P  = beam_test + targ_test - eleC - pipC - proC_Calc_P;
    // 
    // auto MM2_Test_OG    = MM2_Vec_OG.M2();
    // auto MM2_Test       = MM2_Vector.M2();
    // auto MM2_Test_Calc  = MM2_Vec_Calc.M2();
    // auto MM2_Test_Cal_M = MM2_Vec_Cal_M.M2();
    // auto MM2_Test_Cal_P = MM2_Vec_Cal_P.M2();
    // 
    // if(MM2_Test < 0.02 && MM2_Test > -0.1){
    //     
    //     // auto Cor_Name = "None";
    //     // if(2 == corPro_Num){
    //     //     Cor_Name = "MMpro_EF";
    //     // }
    //     // if(3 == corPro_Num){
    //     //     Cor_Name = "MMpro_QEF";
    //     // }
    //     // if(4 == corPro_Num){
    //     //     Cor_Name = "MMpro_LEF";
    //     // }
    //     // if(5 == corPro_Num){
    //     //     Cor_Name = "MMpro_REF";
    //     // }
    //     // if(6 == corPro_Num){
    //     //     Cor_Name = "MMpro_S_LEF";
    //     // }
    //     // if(7 == corPro_Num){
    //     //     Cor_Name = "MMpro_SEF";
    //     // }
    //     // std::cout<<"Proton Correction = "<<Cor_Name<<std::endl;
    //     
    //     double Pion_C_M  = """, str(Particle_Mass_PiC), """;
    //     std::cout<<"Proton Correction = """, str(Correction), """"<<std::endl;
    //     std::cout<<"Sector = "<<prosec<<std::endl;
    //     std::cout<<"Missing Mass Ideal                   = "<<(Pion_C_M*Pion_C_M)<<std::endl;
    //     std::cout<<"MM2_Test_OG (Measured)               = "<<MM2_Test_OG<<std::endl;
    //     std::cout<<"MM2_Test    (Measured - Corrected)   = "<<MM2_Test<<std::endl;
    //     std::cout<<"MM2_Test_Calc  (Corrected - New)     = "<<MM2_Test_Calc<<std::endl;
    //     std::cout<<"MM2_Test_Cal_M (Corrected - New - M) = "<<MM2_Test_Cal_M<<std::endl;
    //     std::cout<<"MM2_Test_Cal_P (Corrected - New - P) = "<<MM2_Test_Cal_P<<std::endl;
    //     std::cout<<std::endl;
    //     
    //     std::cout<<"Delta P = "<<Final_Output<<std::endl;
    //     std::cout<<"Momentum (Measured) = "<<proC.P()<<std::endl;
    //     std::cout<<"Momentum (Calculated) = "<<pro_Calculate<<std::endl<<std::endl;
    //     
    //     std::cout<<"==========================================================================================================================================================================================="<<std::endl<<std::endl;
    // }
    
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
    if((termB2*termB2 - 4*termA2*termC2) < 0){
        std::cout<<"MAJOR ERROR IN ∆P CALCULATION"<<std::endl;
        std::cout<<"SQUARE ROOT TERM = "<<(termB2*termB2 - 4*termA2*termC2)<<std::endl;
        Final_Output = 0.03;
        auto MM_Vector = beam + targ - eleC - proC;
        auto MM2_Value = MM_Vector.M2();
        auto fpro_new  = (pro_Calculate/proC.P());
        auto proC_New  = ROOT::Math::PxPyPzMVector(prox*fpro_new, proy*fpro_new, proz*fpro_new, Proton_M);
        auto MM_Vector_New = beam + targ - eleC - proC_New;
        auto MM2_Value_New = MM_Vector_New.M2();
        std::cout<<"Sector = "<<prosec<<std::endl;
        std::cout<<"MM2 (Ideal)              = "<<(""", str(Particle_Mass_Pi0), """*""", str(Particle_Mass_Pi0), """)<<std::endl;
        std::cout<<"MM2 (Initial)            = "<<MM2_Value<<std::endl;
        std::cout<<"MM2 (Corrected)          = "<<MM2_Value_New<<std::endl;
        std::cout<<""<<std::endl;
        std::cout<<"proC.P()                 = "<<proC.P()<<std::endl;
        std::cout<<"pro_CalculateP           = "<<pro_CalculateP<<std::endl;
        std::cout<<"pro_CalculateM           = "<<pro_CalculateM<<std::endl;
        std::cout<<"Best Calculated Momentum = "<<pro_Calculate<<std::endl;
        std::cout<<""<<std::endl;
        std::cout<<"proC_New.P() (Corrected) = "<<proC_New.P()<<std::endl;
        std::cout<<""<<std::endl;
        std::cout<<"∆P (pro_P - proC.P())    = "<<pro_CalculateP - proC.P()<<std::endl;
        std::cout<<"∆P (pro_M - proC.P())    = "<<pro_CalculateM - proC.P()<<std::endl;
        std::cout<<"Best ∆P                  = "<<pro_Calculate - proC.P()<<std::endl;
        std::cout<<"pro_x                    = "<<px0<<std::endl;
        std::cout<<"pro_y                    = "<<py0<<std::endl;
        std::cout<<"pro_z                    = "<<pz0<<std::endl;
        std::cout<<""<<std::endl;
    }
                        """]) if(False) else "", "".join(["""
    if(Final_Output > 0.007 || Final_Output < -0.007){
    
    // if(Final_Output > 0.005 || Final_Output < -0.005){
    // if(Final_Output < 0.086 && Final_Output > 0.084){
    // if((ex0 == 0.609115) && (ey0 == -1.74351) && (ez0 == 3.79649) && (esec == 6) && (px0 == -0.251199) && (py0 == 0.0714427) && (pz0 == 2.57867) && (psec == 4) && (g1x == -0.250953) && (g1y == 1.21755) && (g1z == 3.1962) && (g2x == -0.108286) && (g2y == 0.410871) && (g2z == 0.906975) && (g1sec == 3) && (g2sec == 3) && (run == 11) && (status == 127) && (dcx1 == -25.0513) && (dcy1 == 1.70499) && (dcz1 == 247.699)){
    // if((ex0 < 0.60912 && ex0 > 0.60910) && (ey0 < -1.74350 && ey0 > -1.74352) && (ez0 < 3.7965 && ez0 > 3.79640) && (esec == 6) && (px0 < -0.25118 && px0 > -0.2512) && (py0 == 0.0714427) && (pz0 == 2.57867) && (psec == 4) && (g1x == -0.250953) && (g1y == 1.21755) && (g1z == 3.1962) && (g2x == -0.108286) && (g2y == 0.410871) && (g2z == 0.906975) && (g1sec == 3) && (g2sec == 3) && (run == 11) && (status == 127) && (dcx1 == -25.0513) && (dcy1 == 1.70499) && (dcz1 == 247.699)){
    // if((ex0 < 0.60912 && ex0 > 0.60910) && (ey0 < -1.74350 && ey0 > -1.74352) && (ez0 < 3.7965 && ez0 > 3.79640) && (esec == 6) && (px0 < -0.25118 && px0 > -0.2512) && ((py0 < (0.0714427+0.0001) && py0 > (0.0714427-0.0001))) && ((pz0 < (2.57867+0.0001) && pz0 > (2.57867-0.0001))) && (psec == 4) && ((g1x < (-0.250953+0.0001) && g1x > (-0.250953-0.0001))) && ((g1y < (1.21755+0.0001) && g1y > (1.21755-0.0001))) && ((g1z < (3.1962+0.0001) && g1z > (3.1962-0.0001))) && ((g2x < (-0.108286+0.0001) && g2x > (-0.108286-0.0001))) && ((g2y < (0.410871+0.0001) && g2y > (0.410871-0.0001))) && ((g2z < (0.906975+0.0001) && g2z > (0.906975-0.0001))) && (g1sec == 3) && (g2sec == 3) && (run == 11) && (status == 127) && ((dcx1 < (-25.0513+0.0001) && dcx1 > (-25.0513-0.0001))) && ((dcy1 < (1.70499+0.0001) && dcy1 > (1.70499-0.0001))) && ((dcz1 < (247.699+0.001) && dcz1 > (247.699-0.001)))){
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
        // std::cout<<"eleC.E()                  = "<<eleC.E()<<std::endl;
        // std::cout<<"pro_x                     = "<<px0<<std::endl;
        // std::cout<<"pro_y                     = "<<py0<<std::endl;
        // std::cout<<"pro_z                     = "<<pz0<<std::endl;
        // std::cout<<"pro_sec                   = "<<psec<<std::endl;
        // std::cout<<"g1_x                      = "<<g1x<<std::endl;
        // std::cout<<"g1_y                      = "<<g1y<<std::endl;
        // std::cout<<"g1_z                      = "<<g1z<<std::endl;
        // std::cout<<"g2_x                      = "<<g2x<<std::endl;
        // std::cout<<"g2_y                      = "<<g2y<<std::endl;
        // std::cout<<"g2_z                      = "<<g2z<<std::endl;
        // std::cout<<"g1_sec                    = "<<g1sec<<std::endl;
        // std::cout<<"g2_sec                    = "<<g2sec<<std::endl;
        // std::cout<<"run_num                   = "<<run<<std::endl;
        // std::cout<<"status_num                = "<<status<<std::endl;
        // std::cout<<"dc_x1                     = "<<dcx1<<std::endl;
        // std::cout<<"dc_y1                     = "<<dcy1<<std::endl;
        // std::cout<<"dc_z1                     = "<<dcz1<<std::endl;
        // std::cout<<""<<std::endl;
        // std::cout<<"ex0_0_60912_ex0_0_60910   = "<<(ex0 < 0.60912 && ex0 > 0.60910)<<std::endl;
        // std::cout<<"ey0_1_74350_ey0_1_74352   = "<<(ey0 < -1.74350 && ey0 > -1.74352)<<std::endl;
        // std::cout<<"ez0_3_7965_ez0_3_79640    = "<<(ez0 < 3.7965 && ez0 > 3.79640)<<std::endl;
        // std::cout<<"esec_6                    = "<<(esec == 6)<<std::endl;
        // std::cout<<"px0_0_25118_px0_0_2512    = "<<(px0 < -0.25118 && px0 > -0.2512)<<std::endl;
        // std::cout<<"py0_0_0714427             = "<<((py0 < (0.0714427+0.0001) && py0 > (0.0714427-0.0001)))<<std::endl;
        // std::cout<<"pz0_2_57867               = "<<((pz0 < (2.57867+0.0001) && pz0 > (2.57867-0.0001)))<<std::endl;
        // std::cout<<"psec_4                    = "<<(psec == 4)<<std::endl;
        // std::cout<<"g1x_0_250953              = "<<((g1x < (-0.250953+0.0001) && g1x > (-0.250953-0.0001)))<<std::endl;
        // std::cout<<"g1y_1_21755               = "<<((g1y < (1.21755+0.0001) && g1y > (1.21755-0.0001)))<<std::endl;
        // std::cout<<"g1z_3_1962                = "<<((g1z < (3.1962+0.0001) && g1z > (3.1962-0.0001)))<<std::endl;
        // std::cout<<"g2x_0_108286              = "<<((g2x < (-0.108286+0.0001) && g2x > (-0.108286-0.0001)))<<std::endl;
        // std::cout<<"g2y_0_410871              = "<<((g2y < (0.410871+0.0001) && g2y > (0.410871-0.0001)))<<std::endl;
        // std::cout<<"g2z_0_906975              = "<<((g2z < (0.906975+0.0001) && g2z > (0.906975-0.0001)))<<std::endl;
        // std::cout<<"g1sec_3                   = "<<(g1sec == 3)<<std::endl;
        // std::cout<<"g2sec_3                   = "<<(g2sec == 3)<<std::endl;
        // std::cout<<"run_11                    = "<<(run == 11)<<std::endl;
        // std::cout<<"status_127                = "<<(status == 127)<<std::endl;
        // std::cout<<"dcx1_25_0513              = "<<((dcx1 < (-25.0513+0.0001) && dcx1 > (-25.0513-0.0001)))<<std::endl;
        // std::cout<<"dcy1_1_70499              = "<<((dcy1 < (1.70499+0.0001) && dcy1 > (1.70499-0.0001)))<<std::endl;
        // std::cout<<"dcz1_247_699              = "<<((dcz1 < (247.699+0.001) && dcz1 > (247.699-0.001)))<<std::endl;
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
#                     Calculation_Code_Choice = "".join([Calculation_Code_Choice, """
#     // Below are the kinematic calculations of the proton angle (theta) (from elastic scattering) 
#     // To be used for exclusivity cuts
#     auto Pro_Th_Calc = (proC.Theta())*(180/3.1415926); // Initialize the calculated proton angle as the same value as the measured/corrected proton angle (converted to degrees)
#     auto denomintator = Beam_Energy*Beam_Energy*(cos(eleC.Theta()) - 1);
#     auto square_root_term = (cos(eleC.Theta()) - 1)*(2*(0.938*0.938) - (Beam_Energy*Beam_Energy) + 2*(Beam_Energy*0.938) + Beam_Energy*(Beam_Energy - 2*(0.938))*cos(eleC.Theta()));
#     auto Pro_Th_Calc_P = acos(((Beam_Energy + (0.938))*sqrt(square_root_term))/(denomintator))*(180/3.1415926);
#     auto Pro_Th_Calc_M = acos((-(Beam_Energy + (0.938))*sqrt(square_root_term))/(denomintator))*(180/3.1415926);
#     cout<<endl;
#     cout<<"El_Th = "<<eleC.Theta()*(180/3.1415926)<<endl;
#     cout<<"Pro_Th Initial = "<<Pro_Th_Calc<<endl;
#     cout<<"Pro_Th Calc P = "<<Pro_Th_Calc_P<<endl;
#     cout<<"Pro_Th Calc M = "<<Pro_Th_Calc_M<<endl;
#     if(abs(Pro_Th_Calc - Pro_Th_Calc_P) <= abs(Pro_Th_Calc - Pro_Th_Calc_M)){
#         Pro_Th_Calc = Pro_Th_Calc_P;
#     }
#     else{
#         Pro_Th_Calc = Pro_Th_Calc_M;
#     }
#     auto Delta_Theta = ((proC.Theta())*(180/3.1415926)) - Pro_Th_Calc;
#     cout<<"Delta Theta = "<<Delta_Theta<<endl;
#     auto Final_Output = Delta_Theta;
#                     """])
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
    
    // if(abs(eleC.P() - Calc_P_El) < 0.1){
    //     cout<<endl;
    //     cout<<"El_P = "<<eleC.P()<<endl;
    //     cout<<"El_Th = "<<eleC.Theta()*(180/3.1415926)<<endl;
    //     cout<<"El_P_Calc = "<<Calc_P_El<<endl;
    //     cout<<"Pro_Th Initial = "<<(proC.Theta())*(180/3.1415926)<<endl;
    //     cout<<"Calc_Terms_1 = "<<Calc_Terms_1<<endl;
    //     cout<<"denomintator = "<<denomintator<<endl;
    //     cout<<"numerator = "<<numerator<<endl;
    //     cout<<"Pro_Th Calc P = "<<Pro_Th_Calc_P<<endl;
    //     cout<<"Pro_Th Calc M = "<<Pro_Th_Calc_M<<endl;
    //     cout<<"Delta Theta = "<<Delta_Theta<<endl;
    // }

    


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



#         Full_Correction_Output = "".join([Correction_Code, """
#     auto Beam_Energy = """, str(Beam_Energy), """;
#     // Defined by the run group/data set
#     """, "// " if("MM" not in Out_Type and "WM" not in Out_Type) else "", """auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
#     """, "// " if("MM" not in Out_Type and "WM" not in Out_Type) else "", """auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, 0.938);
#         """, Particles_for_Correction, """
#         """, Calculation_Code_Choice, """
#     return Final_Output;
#         """])
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
            # fail
            Output = Data_Frame.Define(str(Output_Title), str(Full_Correction_Output))
#             if("D_pro" in Out_Type and "MC" in event_Name):
#                 Output.Display(str(Output_Title)).Print()
            # print("".join([color.BOLD, "Correction Code: \n", color.END, str(Full_Correction_Output)]) if("D_Angle" in Out_Type) else "")
            if(Extra_Cut not in ["none", ""]):
                Output = Output.Filter(Extra_Cut)
                # if("D_Angle" in Out_Type):
                #     print("".join([color.BOLD, "\n\n\nCut Code: \n", color.END, str(Extra_Cut)]))
                # # print("".join([color.BOLD, "\n\n\nCut Code: \n", color.END, str(Extra_Cut)]) if("D_Angle" in Out_Type) else "")
            # if("D_Angle_V4" in Out_Type and Correction == "mm0" and Extra_Cut != ""):
            #     Output.Display(str(Output_Title), 10).Print()
        except Exception as e:
            print("".join([color.RED, color.BOLD, """ERROR: Failed to create the DataFrame Column...\nCode is written as:
            """, color.END, "Output = Data_Frame.Define(", str(Output_Title), ", ", str(Full_Correction_Output).replace(str(Correction_Code_Full_In) if("In" in datatype) else str(Correction_Code_Full_Out), "Correction Code"), """)
            
            if(Extra_Cut not in ["none", ""]):
                Output = Output.Filter(""", str(Extra_Cut), ")"]))
            
            
            print("".join([color.BLUE, color.BOLD, "\nINPUTS: CorDpp('Data_Frame', '", str(Correction), "', '", str(Out_Type), "', '", str(Channel_Type), "', '", str(MM_Type), "', '", str(Data_Type), "', '", str(Extra_Cut), "')", color.END]))
            print("".join([color.RED, color.BOLD, "ERROR GIVEN: \n", str(e), color.END, "\n\n"]))
            print("".join([color.RED, color.BOLD, "TRACEBACK: \n", color.END, color.RED, str(traceback.format_exc()), color.END, "\n\n"]))
            

        
        # ######################################################################################################################
        # ##==================================##############################################==================================##
        # ##==========##==========##==========##       Back-to-Back (Exclusive) Cut       ##==========##==========##==========##
        # ##==================================##############################################==================================##
        # ######################################################################################################################
        # if(Channel_Type == "ES"):
        #     # Output = Output.Filter("(abs(elPhi) + abs(proPhi)) > 175 && (abs(elPhi) + abs(proPhi)) < 185")
        #     Output = Output.Filter("""
        #         bool Back_to_Back_Cut = (1 == 1);
        #         if(esec == 1){
        #             Back_to_Back_Cut = (prosec == 4);
        #         }
        #         if(esec == 2){
        #             Back_to_Back_Cut = (prosec == 5);
        #         }
        #         if(esec == 3){
        #             Back_to_Back_Cut = (prosec == 6);
        #         }
        #         if(esec == 4){
        #             Back_to_Back_Cut = (prosec == 1);
        #         }
        #         if(esec == 5){
        #             Back_to_Back_Cut = (prosec == 2);
        #         }
        #         if(esec == 6){
        #             Back_to_Back_Cut = (prosec == 3);
        #         }
        #         return Back_to_Back_Cut;
        #     """)
        # ######################################################################################################################
        # ##==================================##############################################==================================##
        # ##==========##==========##==========##    Back-to-Back (Exclusive) Cut (End)    ##==========##==========##==========##
        # ##==================================##############################################==================================##
        # ######################################################################################################################
            
            

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






    ##==============================================================================================##
    ##==========##==========##     Function for Correction Title Names      ##==========##==========##
    ##==============================================================================================##

    def corNameTitles(CorrectionNameIn, Form="Default"):
        CorrectionName1, CorrectionName2, CorrectionName3, CorrectionName4 = 'Error', 'Error', 'Error', 'Error'

        if(CorrectionNameIn == "No correction"):
            CorrectionNameIn = "mm0"

        if('mm0'      in CorrectionNameIn):
            CorrectionName1 = 'No El Cor'
        if('mm1'      in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Linear - No Phi)'
        if('mmPhi'    in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Linear - Linear Phi)'
        if('mmPhi_R1' in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Quad - Linear Phi - Refined 1)'.replace('Linear', 'Linear' if("In" in datatype) else 'Quad')
        if('mmPhi_R2' in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Quad - Quad Phi - Refined 2)'
        if('mmPhi_R3' in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Quad - Quad Phi - Refined 3)'
        if('mmPhi_R4' in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Quad - Quad Phi - Refined 4)'
        if('mmPhi_R5' in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Quad - Quad Phi - Refined 5)'
        if('mmF'      in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Quad - Quad Phi)'
        if('mmEF'     in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Quad - Quad Phi - With Elastic Cors)'
        if('mmExF'    in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Quad - Quad Phi - Extended)'
        if('mmP2'     in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Quad - Pass 2)'
        if('mmRP2'    in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Quad - Quad Phi - Pass 2)'
            
        if(event_type in ["EO"]):
            if(CorrectionNameIn == "mm0"):
                CorrectionName = "No Momentum Corrections"
            else:
                CorrectionName = CorrectionName1
            return CorrectionName

        if('Pip' not in CorrectionNameIn):
            CorrectionName2 = 'No Pi+ Cor' if(event_type not in ["P0"]) else ""
        if('Pip' in CorrectionNameIn):
            if('MMQ'       in CorrectionNameIn):
                CorrectionName2 = 'Pi+ Cor (Quad - No Phi)'
            if('MMPhi'     in CorrectionNameIn):
                CorrectionName2 = 'Pi+ Cor (Quad - Linear Phi)'
            if('MMqPhi_R1' in CorrectionNameIn):
                CorrectionName2 = 'Pi+ Cor (Quad - Quad Phi - Refined 1)'
            if('MMqPhi_R2' in CorrectionNameIn):
                CorrectionName2 = 'Pi+ Cor (Quad - Quad Phi - Refined 2)'
            if('MMqPhi_R3' in CorrectionNameIn):
                CorrectionName2 = 'Pi+ Cor (Quad - Quad Phi - Refined 3)'
            if('MMqPhi_R4' in CorrectionNameIn):
                CorrectionName2 = 'Pi+ Cor (Quad - Quad Phi - Refined 4)'
            if('MMqPhi_R5' in CorrectionNameIn):
                CorrectionName2 = 'Pi+ Cor (Quad - Quad Phi - Refined 5)'
            if('MMF'       in CorrectionNameIn):
                CorrectionName2 = 'Pi+ Cor (Quad - Quad Phi)'
            if('MMExF'     in CorrectionNameIn):
                CorrectionName2 = 'Pi+ Cor (Quad - Quad Phi - Extended)'
            if('MMEF'      in CorrectionNameIn):
                CorrectionName2 = 'Pi+ Cor (Quad - Quad Phi - With Elastic Cors)'
            if('MMP2'      in CorrectionNameIn):
                CorrectionName2 = 'Pi+ Cor (Quad - Pass 2)'
            if('MMsP2'      in CorrectionNameIn):
                CorrectionName2 = 'Pi+ Cor (Quad - Pass 2 - Split)'

        if('Pim' not in CorrectionNameIn):
            CorrectionName3 = 'No Pi- Cor' if(event_type in ["DP"]) else ""
        if('Pim' in CorrectionNameIn):
            if('MMpimPhi'   in CorrectionNameIn):
                CorrectionName3 = 'Pi- Cor (Linear - Linear Phi)'
            if('MMpim_qPhi' in CorrectionNameIn):
                CorrectionName3 = 'Pi- Cor (Quad - Quad Phi)'
            if('MMpim_F'    in CorrectionNameIn):
                CorrectionName3 = 'Pi- Cor (Quad - Quad Phi - Rounded)'

        if('Pro' not in CorrectionNameIn):
            CorrectionName4 = 'No Pro Cor' if(event_type not in ["SP", "MC"]) else ""
            # if(('_NoELC' not in CorrectionNameIn and event_type == "DP") or (event_type == "P0")):
            if((('_NoELC' not in CorrectionNameIn)) and CorrectionName4 != ""):
                CorrectionName4 = ''.join([CorrectionName4, " (Energy Loss Cor)"])
        if('Pro' in CorrectionNameIn):
            if('MMproPhi'       in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Linear - Linear Phi)'
            if("MMpro_qPhi"     in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad - Quad Phi)'
            if('MMpro_pi0Phi'   in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad - Quad Phi - From Pi0)'
            if('MMpro_pi2Phi'   in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad - Quad Phi - From Double Pion)'
            if('MMpro_NoPhi'    in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Linear - No Phi)'
            if('MMpro_qNoPhi'   in CorrectionNameIn or 'MMpro_F' in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad - No Phi)'
            if('MMpro_EF'       in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad - No Phi - With Elastic Cors)'
            if('MMpro_REF'      in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad - Refined - With Elastic Cors)'
            if('MMpro_QEF'      in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Double Quad - With Elastic Cors)'
            if('MMpro_LEF'      in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad+Linear - With Elastic Cors)'
            if('MMpro_S_LEF'    in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad+Linear+Slices - With Elastic Cors)'
            if('MMpro_SEF'      in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Sliced - With Elastic Cors)'
            if('MMpro_SE_NoELC' in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Sliced - With Elastic Cors - Before Energy Loss)' # Removed
            if('MMpro_SEC'      in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Sliced - With Elastic Cors - New Cut)'
            if('MMpro_SERC'     in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Sliced - With Elastic Cors and New Refined Cut)'
            if('MMpro_SRE'      in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Sliced - With Elastic Cors - Refined)'
            if('MMpro_SFRE'     in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Sliced - Elastic Cors - Refined - Final)'
            if('MMpro_DRE'      in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Double Quad - Elastic Cors)'
            if('MMpro_RE'       in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Double Quad - Elastic Cors - Refined - Old)'
            if('MMpro_FRE'      in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Double Quad - Elastic Cors - Refined)'
            if('MMpro_NRE'      in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Double Quad - Elastic Cors - New)'
            if('MMpro_NS'       in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Sliced - Manual Refined New)'
                

            if(('_NoELC' not in CorrectionNameIn)):
                CorrectionName4 = CorrectionName4.replace(")", " - Energy Loss Cor)")

        if(CorrectionName1 == 'Error'):
            print("".join(["Error with the Electron Correction in CorrectionNameInput = ", str(CorrectionNameIn)]))
            CorrectionName1 = "El Cor (ERROR)"

        if(CorrectionName2 == 'Error' and event_type not in ["P0", "ES"]):
            print("".join(["Error with the Pi+ Pion Correction in CorrectionNameInput = ", str(CorrectionNameIn)]))
            CorrectionName2 = "Pi+ Cor (ERROR)"

        if(CorrectionName3 == 'Error' and event_type not in ["SP", "MC", "P0", "ES"]):
            print("".join(["Error with the Pi- Pion Correction in CorrectionNameInput = ", str(CorrectionNameIn)]))
            CorrectionName3 = "Pi- Cor (ERROR)"

        if(CorrectionName4 == 'Error' and event_type not in ["SP", "MC"]):
            print("".join(["Error with the Proton Correction in CorrectionNameInput = ", str(CorrectionNameIn)]))
            CorrectionName4 = "Pro Cor (ERROR)"

        CorrectionName = "".join([CorrectionName1, " - " if(CorrectionName2 != "") else "", CorrectionName2, " - " if(CorrectionName3 != "") else "", CorrectionName3, " - " if(CorrectionName4 != "") else "", CorrectionName4])
        
        if(event_type in ["SP", "MC"]):
            CorrectionName = "".join([CorrectionName1, " - " if(CorrectionName2 != "") else "", CorrectionName2])
        elif(event_type != "ES"):
            CorrectionName = "".join([CorrectionName1, " - " if(CorrectionName2 != "") else "", CorrectionName2, " - " if(CorrectionName3 != "") else "", CorrectionName3, " - " if(CorrectionName4 != "") else "", CorrectionName4])
        else:
            CorrectionName = "".join([CorrectionName1, " - " if(CorrectionName4 != "") else "", CorrectionName4])


        if(CorrectionName1 == 'El Cor (Quad - Quad Phi)' and CorrectionName2 == 'Pi+ Cor (Quad - Quad Phi)'):
            if(event_type in ["SP", "MC"]):
                CorrectionName = 'El/Pi+ Cor (Quad - Quad Phi)'
            else:
                if(CorrectionName3 == 'Pi- Cor (Quad - Quad Phi)'):
                    if('Pro Cor (Quad - Quad Phi' in CorrectionName4):
                        CorrectionName = "".join(["El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)"])
                    else:
                        CorrectionName = "".join(["El/Pi+/Pi- Cor (Quad - Quad Phi) - ", CorrectionName4])
                else:
                    if('Pro Cor (Quad - Quad Phi' in CorrectionName4):
                        CorrectionName = "".join(["El/Pi+/Pro Cor (Quad - Quad Phi) - ", CorrectionName3])
                    else:
                        CorrectionName = "".join(["El/Pi+ Cor (Quad - Quad Phi) - ", CorrectionName3, " - ", CorrectionName4])

        if(event_type not in ["SP", "MC"]):
            if("Energy Loss Cor" not in CorrectionName and '_NoELC' not in CorrectionNameIn):
                CorrectionName = CorrectionName.replace('Pro Cor (Quad - Quad Phi)', 'Pro Cor (Quad - Quad Phi - Energy Loss Cor)')
                
        CorrectionName = CorrectionName.replace('- No Pi- Cor ', "")
                
        if(CorrectionNameIn in ["mm0", "mm0_NoELC"]):
            CorrectionName = "".join(["No Momentum Corrections", " (Energy Loss Cor)" if(event_type not in ["SP", "MC"] and (("NoELC" not in CorrectionNameIn) or ("MC" in event_Name))) else ""])

        if(Form != "Default"):
            if("No Momentum Corrections" not in CorrectionName and CorrectionName != 'El/Pi+ Cor (Quad - Quad Phi)'):
                if(event_type in ["SP", "MC"]):
                    CorrectionName = "".join(["#splitline{", str(CorrectionName1), "}{", str(CorrectionName2), "}"])
                if("E" in event_type or event_type == "P0"):
                    CorrectionName = "".join(["#splitline{", str(CorrectionName1), "}{", str(CorrectionName4), "}"])
                if(event_type == "DP"):
                    CorrectionName = "".join(["#splitline{#splitline{", str(CorrectionName1), "}{", str(CorrectionName2), "}}{", "".join(["#splitline{", str(CorrectionName3), "}{", str(CorrectionName4), "}"]) if(str(CorrectionName3) not in ["No Pi- Cor", "", "Error"]) else str(CorrectionName4), "}"])
                    if(CorrectionName1 == 'El Cor (Quad - Quad Phi)' and CorrectionName2 == 'Pi+ Cor (Quad - Quad Phi)'):
                        CorrectionName = "".join(["#splitline{El/Pi+ Cor (Quad - Quad Phi)}{", "".join(["#splitline{", str(CorrectionName3), "}{", str(CorrectionName4), "}"]) if(str(CorrectionName3) not in ["No Pi- Cor", "", "Error"]) else str(CorrectionName4), "}"])
                    if(CorrectionName1 == 'El Cor (Quad - Quad Phi - Energy Loss Cor)' and CorrectionName2 == 'Pi+ Cor (Quad - Quad Phi - Energy Loss Cor)'):
                        CorrectionName = "".join(["#splitline{El/Pi+ Cor (Quad - Quad Phi - Energy Loss Cor)}{", "".join(["#splitline{", str(CorrectionName3), "}{", str(CorrectionName4), "}"]) if(str(CorrectionName3) not in ["No Pi- Cor", "", "Error"]) else str(CorrectionName4), "}"])
                    
        if("Test" in CorrectionNameIn):
            CorrectionName = "".join(["" if("mm0" in CorrectionNameIn) else "".join(["(", str(str(CorrectionNameIn).replace("_Test_M", "")).replace("_Test_P", ""), ") "]), "Test Proton Correction (", "Adding 20 MeV" if("Test_P" in CorrectionNameIn) else "Subtracting 20 MeV" if("Test_M" in CorrectionNameIn) else "Error", " - Energy Loss Cor)" if(event_type not in ["SP", "MC"] and "NoELC" not in CorrectionNameIn) else ")"])

        return CorrectionName



        ##===================================================================================================##
        ##==========##==========##     Function for Correction Title Names (End)     ##==========##==========##
        ##===================================================================================================##
        
        
        
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

        CorrrectionName = corNameTitles(Correction, Form="splitline")

        name = (Correction, Sector, Binning, Region, Particle_Plot, Particle, Extra_Cut)
               

        start_title = "".join(["#splitline{", str(datatype), " Invariant Mass}"])
        if(pass_version not in ["NA", ""]):
            start_title = "".join(["#splitline{", str(start_title), "{", str(pass_version), "}}"])
        
        output_title = "".join([str(start_title), "{", str(CorrrectionName), " -- ", SecName, "}; p_{", Particle_Plot_Formatting, "} [GeV]; W [GeV]"])
        if(regionName != "" and Extra_Cut != ""):
            output_title = "".join([str(start_title), "{#splitline{", str(CorrrectionName), " -- ", SecName, "}{", regionName, "}}; p_{", Particle_Plot_Formatting, "} [GeV]; W [GeV]"])
        if(Extra_Cut != "" and regionName == ""):
            output_title = "".join([str(start_title), "{#splitline{", str(CorrrectionName), " -- ", SecName, "}{Cut Applied: ", Extra_Cut, "}}; p_{", Particle_Plot_Formatting, "} [GeV]; W [GeV]"])
        if(Extra_Cut != "" and regionName != ""):
            output_title = "".join([str(start_title), "{#splitline{", str(CorrrectionName), " -- ", SecName, "}{#splitline{Cut Applied: ", Extra_Cut, "}{", regionName, "}}}; p_{", Particle_Plot_Formatting, "} [GeV]; W [GeV]"])
            
        WC_out = "".join(["WM_", Correction])

        output = Bank.Histo2D(("".join(["HWC_Histo_All_", str(name)]), str(output_title), 200, 2 if('el' in Particle_Plot) else 0, 12 if('el' in Particle_Plot) else 10, 200, 0, 5), Particle_Plot, WC_out)

        return output

    

    ##====================================================================================================##
    ##==========##     For 2D Invariant Mass vs Momentum Histograms - HWC_Histo_All (End)     ##==========##
    ##====================================================================================================##



    ##==========================================================================================##
    ##==========##     For 2D Missing Mass vs Momentum Histograms - hmmCPARTall     ##==========##
    ##==========================================================================================##

    def Missing_Mass_Histo_Maker(Bank, Correction, Sector, Region, Shift, Binning, Particle_Plot, Particle, Extra_Cut):

        # Difference between Particle and Particle_Plot ==> Particle defines which particle is referenced for sectors and phi bins while Particle_Plot refers to which particle momentum will be plotted against

        Particle_Formatting = str(((((str(Particle).replace("el", "El")).replace("pro", "Pro")).replace("pip", "#pi^{+}")).replace("pim", "#pi^{-}")).replace("pi0", "#pi^{0}"))
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

        CorrrectionName = corNameTitles(Correction, Form="splitline")

        name = (Correction, Sector, '', Binning, Region, Particle_Plot, Particle, Extra_Cut)

                
        start_title = "".join(["#splitline{(", str(datatype), ") MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "} ", str(SecName), "}"])
        if(pass_version not in ["NA", ""]):
            start_title = "".join(["#splitline{", str(start_title), "{", str(pass_version), "}}"])
                
        output_title = "".join([str(start_title),                               "{Correction:", str(CorrrectionName), "};p_{", str(Particle_Plot_Formatting), "} [GeV];MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}"])
        if(regionName != "" and Extra_Cut != ""):
            output_title = "".join(["#splitline{",            str(start_title), "{Correction:", str(CorrrectionName), "}}{", str(regionName), "};p_{", str(Particle_Plot_Formatting), "} [GeV];MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}"])
        if(Extra_Cut != "" and regionName == ""):
            output_title = "".join(["#splitline{",            str(start_title), "{Correction:", str(CorrrectionName), "}}{Cut Applied: ", str(Extra_Cut), "};p_{", str(Particle_Plot_Formatting), "} [GeV];MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}"])
        if(Extra_Cut != "" and regionName != ""):
            output_title = "".join(["#splitline{#splitline{", str(start_title), "{Correction:", str(CorrrectionName), "}}{Cut Applied: ", str(Extra_Cut), "}}{", str(regionName), "};p_{", str(Particle_Plot_Formatting), "} [GeV];MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}"])

        # output = Bank.Histo2D(("".join(["hmmCPARTall_", str(name)]), str(output_title), 200, 2 if 'el' in Particle_Plot else 0, 12 if 'el' in Particle_Plot else 10, Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max), Particle_Plot, Correction)
        output = Bank.Histo2D(("".join(["hmmCPARTall_", str(name)]), str(output_title), 240, 0, 12, Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max), Particle_Plot, Correction)

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
    ############################################################################################################################################

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
            
            if("Pass 1" in pass_version):
                print(color.BOLD, color.BLUE, "\nUSING NEW EXCLUSIVITY CUTS FOR SPRING 2019 DATA (Pass 1)\n\n", color.END)
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
                
            if("Pass 2" in pass_version):
                print(color.BOLD, color.BLUE, "\nUSING NEW EXCLUSIVITY CUTS FOR SPRING 2019 DATA (Pass 2)\n\n", color.END)
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
                            cut_upper = (-0.0009746)*el + (1.0662726);
                            // Lower Cut
                            cut_lower = (-0.003077)*el + (0.8593037);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (0.0022395)*el + (1.0521977);
                            // Lower Cut
                            cut_lower = (0.0002064)*el + (0.8374306);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0043019)*el + (1.0873004);
                            // Lower Cut
                            cut_lower = (-0.0045241)*el + (0.8632384);
                        }
                    }
                    if(esec == 2){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0017436)*el + (1.0671729);
                            // Lower Cut
                            cut_lower = (-0.006537)*el + (0.8630303);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0009251)*el + (1.0620756);
                            // Lower Cut
                            cut_lower = (-0.0042113)*el + (0.8512631);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0062341)*el + (1.0963343);
                            // Lower Cut
                            cut_lower = (-0.0096668)*el + (0.8751263);
                        }
                    }
                    if(esec == 3){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0044655)*el + (1.0838766);
                            // Lower Cut
                            cut_lower = (-0.0068203)*el + (0.8592193);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0043441)*el + (1.0826992);
                            // Lower Cut
                            cut_lower = (-0.0092879)*el + (0.8691799);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0024024)*el + (1.0751932);
                            // Lower Cut
                            cut_lower = (-0.0067032)*el + (0.8576486);
                        }
                    }
                    if(esec == 4){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (0.0009057)*el + (1.0597884);
                            // Lower Cut
                            cut_lower = (-0.0058479)*el + (0.8690836);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0005842)*el + (1.0702956);
                            // Lower Cut
                            cut_lower = (-0.007878)*el + (0.8748704);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (0.0027736)*el + (1.0548513);
                            // Lower Cut
                            cut_lower = (0.0011848)*el + (0.8174472);
                        }
                    }
                    if(esec == 5){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (0.0006062)*el + (1.0575388);
                            // Lower Cut
                            cut_lower = (-0.0057308)*el + (0.8602961);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.0006488)*el + (1.0737746);
                            // Lower Cut
                            cut_lower = (-0.0016143)*el + (0.8323827);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.0055699)*el + (1.0974838);
                            // Lower Cut
                            cut_lower = (0.0019992)*el + (0.7994388);
                        }
                    }
                    if(esec == 6){
                        if(localelPhiS > -5 && localelPhiS < 5){
                            // Upper Cut
                            cut_upper = (-0.0026965)*el + (1.0722083);
                            // Lower Cut
                            cut_lower = (-0.0002484)*el + (0.8195911);
                        }
                        if(localelPhiS < -5){
                            // Upper Cut
                            cut_upper = (-0.00398)*el + (1.0802161);
                            // Lower Cut
                            cut_lower = (-0.0001438)*el + (0.8190835);
                        }
                        if(localelPhiS > 5){
                            // Upper Cut
                            cut_upper = (-0.004144)*el + (1.0814831);
                            // Lower Cut
                            cut_lower = (-0.0026884)*el + (0.8391593);
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
#             Calculated_Dp_Cut_V2 = "".join(["""
#     double Proton_M  = """, str(Particle_Mass_Proton), """;
#     auto Beam_Energy = """, str(Beam_Energy), """;
#     auto eleC = ROOT::Math::PxPyPzMVector(""", "ex, ey, ez" if("(GEN)" not in str(event_Name)) else "ex0, ey0, ez0", """, 0);
#     auto proC = ROOT::Math::PxPyPzMVector(prox, proy, proz, Proton_M);  
#     double pi0M2term = (""", str(Particle_Mass_Pi0), """*""", str(Particle_Mass_Pi0), """)/2;
#     // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pi0) based on the assumption that the proton angle and electron reconstruction were measured by the detector correctly for exclusive events in the ep->epπ0 channel
#     // (π0 is used as the "missing" particle)
#     auto termA1 = pi0M2term - (Proton_M)*((Beam_Energy) - eleC.P() + (Proton_M)) + (Beam_Energy)*eleC.P()*(1 - cos(eleC.Theta()));
#         // termA1 = pi0M2term - "Proton Mass"*("Initial Beam Energy" - "Electron Momentum" + "Proton Mass") + "Initial Beam Energy"*"Electron Momentum"*(1 - cos("Electron Theta Angle"))
#     auto termB1 = (Beam_Energy)*cos(proC.Theta()) - eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC));
#         // termB1 = "Initial Beam Energy"*cos("Proton Theta Angle") - "Electron Momentum"*cos("Angle between the Proton and Electron")
#     auto termC1 = eleC.P() - (Beam_Energy) - (Proton_M);
#         // termC1 = "Electron Momentum" - "Initial Beam Energy" - "Proton Mass"
#     auto termA2 = (termB1*termB1 - termC1*termC1);
#     auto termB2 = -2*termB1*termA1;
#     auto termC2 = termA1*termA1 - termC1*termC1*(Proton_M)*(Proton_M);
#     auto pro_CalculateP = (-termB2 + sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);
#     auto pro_CalculateM = (-termB2 - sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);
#     auto pro_Calculate = pro_CalculateP;
#     if(abs(proC.P() - pro_CalculateP) <= abs(proC.P() - pro_CalculateM)){
#         pro_Calculate = pro_CalculateP;
#     }
#     else{
#         pro_Calculate = pro_CalculateM;
#     }
#     if(pro_CalculateP < 0){
#         pro_Calculate = pro_CalculateM;
#     }
#     if(pro_CalculateM < 0){
#         pro_Calculate = pro_CalculateP;
#     }
#     auto Delta_P_Cut = pro_Calculate - proC.P();
#     return (Delta_P_Cut > 0.005 || Delta_P_Cut < -0.005);
#     """])
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
        if(("Pass 2" in str(pass_version)) and ("Out" not in str(datatype))):
            print(color.BOLD, color.BLUE, "\nUSING NEW EXCLUSIVITY CUTS FOR SPRING 2019 DATA (Pass 2)\n\n", color.END)
        if(("Pass 1" in str(pass_version)) and ("Out" not in str(datatype))):
            print(color.BOLD, color.BLUE, "\nUSING NEW EXCLUSIVITY CUTS FOR SPRING 2019 DATA (Pass 1)\n\n", color.END)
        
        Calculated_Exclusive_Cuts = "".join(["""        
        // For Invariant Mass Cut (Spring 2019 (Pass 2) - Based on a 2-sigma cut (upper bounds) on the Invarient Mass - Upper Cut is a function of the electron momentum - Lower cut is a constant and based on a 3-sigma cut - No Phi dependence):
        auto Beam_Energy = """, str(Beam_Energy), """;
        auto Proton_Mass = """, str(Particle_Mass_Proton), """;
        auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
        auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
        auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
        auto Cut_Variable = (beam + targ - eleC).M();
        auto Upper_Cut = 1.3;
        auto Lower_Cut = 0.7;
        if(esec == 1){
            Upper_Cut = (-0.0491542)*el + (1.5);
            Lower_Cut = (0.7878436);
        }
        if(esec == 2){
            Upper_Cut = (-0.0505903)*el + (1.5);
            Lower_Cut = (0.745676);
        }
        if(esec == 3){
            Upper_Cut = (-0.0503804)*el + (1.5);
            Lower_Cut = (0.735096);
        }
        if(esec == 4){
            Upper_Cut = (-0.0491416)*el + (1.5);
            Lower_Cut = (0.7817657);
        }
        if(esec == 5){
            Upper_Cut = (-0.0495588)*el + (1.5);
            Lower_Cut = (0.7855759);
        }
        if(esec == 6){
            Upper_Cut = (-0.0496809)*el + (1.5);
            Lower_Cut = (0.7655371);
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
#     if(Calculated_Exclusive_Cuts_v6 != "esec != -2"):
#         kinematicCuts.append(Calculated_Exclusive_Cuts_v6)
#     if(Calculated_Dp_Cut != "esec != -2"):
#         # kinematicCuts = [Calculated_Dp_Cut, Calculated_Dp_Cut_V2]
#         kinematicCuts = [Calculated_Dp_Cut]

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
                print("".join([color.BOLD, color.RED, "ERROR: Failed to make the cut: ", color.END, str(Input_Cut), "\n\n", color.BOLD, color.RED, "Error Reads as: ", str(e), color.END]))
            
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
    
    
    if(event_type != "SP" and "E" not in event_type):
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
        
    if("MC" in event_Name):
        Delta_Pip_histo_SecList = ["all"]


    Delta_P_histo_CorList = ['mm0']

    
    
    if(event_type in ["SP", "MC"]):
        if(datatype == "Inbending"):
            # Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_PipMMF']
            # Delta_P_histo_CorList = ['mm0', 'mmF_PipMMF', 'mmExF_PipMMF', 'mmEF_PipMMF']
            # Delta_P_histo_CorList = ['mm0', 'mmF', 'mmEF', 'mmExF', 'mmF_PipMMF', 'mmExF_PipMMF', 'mmEF_PipMMF']
            # Delta_P_histo_CorList = ['mm0', 'mmF', 'mmEF', 'mmF_PipMMF', 'mmEF_PipMMF']
            # Delta_P_histo_CorList = ['mm0', 'mmF', 'mmEF', 'mmF_PipMMF', 'mmEF_PipMMF', 'mmEF_PipMMEF']
            Delta_P_histo_CorList = ['mm0', 'mmEF', 'mmEF_PipMMEF']
            # Delta_P_histo_CorList = ['mm0', 'mmEF', 'mmEF_PipMMF', 'mmEF_PipMMExF', 'mmEF_PipMMEF']
            
            if("Spring 2019 - Pass 2" in str(pass_version)):
                Delta_P_histo_CorList.append("mmP2")
                Delta_P_histo_CorList.append("mmRP2")
                Delta_P_histo_CorList.append("mmP2_PipMMP2")
                Delta_P_histo_CorList.append("mmRP2_PipMMP2")
                Delta_P_histo_CorList.append("mmRP2_PipMMsP2")

        if(datatype == "Outbending"):
            # Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_PipMMF']
            # Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_PipMMF', 'mmEF']
#             Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_PipMMF', 'mmExF', 'mmEF', 'mmEF_PipMMEF', 'mmExF_PipMMEF']
            # Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_PipMMF', 'mmEF', 'mmEF_PipMMEF']
            # Delta_P_histo_CorList = ['mm0', 'mmEF', 'mmEF_PipMMEF']
            Delta_P_histo_CorList = ['mm0', 'mmEF', 'mmExF', 'mmEF_PipMMEF', 'mmExF_PipMMExF']
            # Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_PipMMF', 'mmEF', 'mmEF_PipMMEF', "mmExF_PipMMEF", "mmExF"]

        # # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        Delta_P_histo_CompareList = ['pi+', 'el']   # Show both corrections
        # Delta_P_histo_CompareList = ['el']          # Electron Corrections only
        # Delta_P_histo_CompareList = ['pi+']         # Pi+ Corrections only
            
            
    if(event_type == "DP"):
        if(datatype == "Inbending"):
            # # Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F_NoELC', 'mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F']
            # # Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_F', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_F']
            # # Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_F', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF']
            # # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_QEF']
            # # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_QEF']
            # # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF']
            # # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF']
            # # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_QEF', 'mmEF_PipMMEF_ProMMpro_LEF']
            # # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_REF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_REF']
            # # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_REF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_REF', 'mmEF_PipMMEF_ProMMpro_LEF', 'mmEF_PipMMEF_ProMMpro_QEF']
            # # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_S_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF', 'mmEF_PipMMEF_ProMMpro_S_LEF', 'mmEF_PipMMEF_ProMMpro_SEF']
            # # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_S_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF', 'mmEF_PipMMEF_ProMMpro_S_LEF', 'mmEF_PipMMEF_ProMMpro_SEF']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_S_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEC_NoELC', 'mmEF_PipMMEF_ProMMpro_SERC_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF', 'mmEF_PipMMEF_ProMMpro_S_LEF', 'mmEF_PipMMEF_ProMMpro_SEF', 'mmEF_PipMMEF_ProMMpro_SEC', 'mmEF_PipMMEF_ProMMpro_SERC']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEC_NoELC', 'mmEF_PipMMEF_ProMMpro_SERC_NoELC', 'mmEF_PipMMEF_ProMMpro_SRE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_SEF', 'mmEF_PipMMEF_ProMMpro_SEC', 'mmEF_PipMMEF_ProMMpro_SERC', 'mmEF_PipMMEF_ProMMpro_SRE']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEC_NoELC', 'mmEF_PipMMEF_ProMMpro_SERC_NoELC', 'mmEF_PipMMEF_ProMMpro_SRE_NoELC', 'mmEF_PipMMEF_ProMMpro_SFRE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_SEF', 'mmEF_PipMMEF_ProMMpro_SEC', 'mmEF_PipMMEF_ProMMpro_SERC', 'mmEF_PipMMEF_ProMMpro_SRE', 'mmEF_PipMMEF_ProMMpro_SFRE']
            # # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_FRE_NoELC', 'mmEF_PipMMEF_ProMMpro_SEC_NoELC', 'mmEF_PipMMEF_ProMMpro_SERC_NoELC', 'mmEF_PipMMEF_ProMMpro_SRE_NoELC', 'mmEF_PipMMEF_ProMMpro_SFRE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_FRE', 'mmEF_PipMMEF_ProMMpro_SEC', 'mmEF_PipMMEF_ProMMpro_SERC', 'mmEF_PipMMEF_ProMMpro_SRE', 'mmEF_PipMMEF_ProMMpro_SFRE']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_FRE_NoELC', 'mmEF_PipMMEF_ProMMpro_RE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_FRE', 'mmEF_PipMMEF_ProMMpro_RE']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_DRE_NoELC', 'mmEF_PipMMEF_ProMMpro_FRE_NoELC', 'mmEF_PipMMEF_ProMMpro_RE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_DRE', 'mmEF_PipMMEF_ProMMpro_FRE', 'mmEF_PipMMEF_ProMMpro_RE']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_NRE_NoELC', 'mmEF_PipMMEF_ProMMpro_FRE_NoELC', 'mmEF_PipMMEF_ProMMpro_RE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_NRE', 'mmEF_PipMMEF_ProMMpro_FRE', 'mmEF_PipMMEF_ProMMpro_RE']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_NRE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_NRE']
            Delta_P_histo_CorList = ['mm0_NoELC', 'mm0_Test_P_NoELC', 'mm0_Test_M_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_NRE_NoELC', 'mm0', 'mm0_Test_P', 'mm0_Test_M', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_NRE']
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_NRE_NoELC', 'mmEF_PipMMEF_ProMMpro_NS_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_NRE', 'mmEF_PipMMEF_ProMMpro_NS']
            
        
            # Delta_P_histo_CorList = ['mmEF_PipMMEF_ProMMpro_SEF']
            # Delta_P_histo_CorList = ['mm0']
        if(datatype == "Outbending"):
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F_NoELC', 'mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_F', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_F']
            Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_F', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF']
            
            
        # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        Delta_P_histo_CompareList = ['pro']
            
            
    if(event_type == "P0"):
        if(datatype == "Inbending"):
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F', 'mmEF', 'mmEF_ProMMpro_F']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F', 'mmEF', 'mmEF_ProMMpro_EF']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_ProMMpro_EF_NoELC', 'mmEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_EF', 'mmEF_ProMMpro_QEF']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_ProMMpro_EF_NoELC', 'mmEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_EF', 'mmEF_ProMMpro_QEF']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_ProMMpro_LEF_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_LEF']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_ProMMpro_LEF_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_LEF']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_ProMMpro_EF_NoELC', 'mmEF_ProMMpro_QEF_NoELC', 'mmEF_ProMMpro_LEF_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_EF', 'mmEF_ProMMpro_QEF', 'mmEF_ProMMpro_LEF']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_ProMMpro_EF_NoELC', 'mmEF_ProMMpro_REF_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_EF', 'mmEF_ProMMpro_REF']
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_ProMMpro_EF_NoELC', 'mmEF_ProMMpro_REF_NoELC', 'mmEF_ProMMpro_LEF_NoELC', 'mmEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_EF', 'mmEF_ProMMpro_REF', 'mmEF_ProMMpro_LEF', 'mmEF_ProMMpro_QEF']

            Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_ProMMpro_RE_NoELC', 'mmEF_ProMMpro_NRE_NoELC', 'mmEF_ProMMpro_FRE_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_RE', 'mmEF_ProMMpro_NRE', 'mmEF_ProMMpro_FRE']
            Delta_P_histo_CorList = ['mm0', 'mm0_Test_P', 'mm0_Test_M', 'mmEF', 'mmEF_Test_M', 'mmEF_Test_P', 'mmEF_ProMMpro_NRE']
            Delta_P_histo_CorList = ['mm0', 'mm0_Test_P', 'mm0_Test_M', 'mmEF', 'mmEF_ProMMpro_NRE', 'mmEF_ProMMpro_NS']
            Delta_P_histo_CorList = ['mm0', 'mm0_Test_P', 'mm0_Test_M']
            Delta_P_histo_CorList = ['mm0']
            
                        
        if(datatype == "Outbending"):
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F', 'mmEF', 'mmEF_ProMMpro_F']
            Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F', 'mmEF', 'mmEF_ProMMpro_EF']
            
        # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        # Delta_P_histo_CompareList = ['pro', 'el']
        Delta_P_histo_CompareList = ['pro']
        
        
    if(event_type == "ES"):
        if(datatype == "Inbending"):
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F', 'mmEF_NoELC', 'mmEF_ProMMpro_F_NoELC', 'mmEF', 'mmEF_ProMMpro_F']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF_ProMMpro_F', 'mmEF_ProMMpro_F_NoELC', 'mmEF', 'mmEF_ProMMpro_F']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmF_ProMMpro_F']
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmF']
            
        if(datatype == "Outbending"):
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F', 'mmEF_NoELC', 'mmEF_ProMMpro_F_NoELC', 'mmEF', 'mmEF_ProMMpro_F']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF_ProMMpro_F', 'mmEF_ProMMpro_F_NoELC', 'mmEF', 'mmEF_ProMMpro_F']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmF_ProMMpro_F']
#             Delta_P_histo_CorList = ['mm0_NoELC', 'mmF']
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmF', 'mmEF']

            
            
        # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        # Delta_P_histo_CompareList = ['pro', 'el']
        Delta_P_histo_CompareList = ['el']
        
        
        
    if(event_type == "EO"):
        if(datatype == "Inbending"):
            # Delta_P_histo_CorList = ['mm0', 'mmF', 'mmEF', 'mmExF']
            # Delta_P_histo_CorList = ['mm0', 'mmF', 'mmEF']
            Delta_P_histo_CorList = ['mm0', 'mmEF']
            if("Spring 2019 - Pass " in str(pass_version)):
                Delta_P_histo_CorList.append("mmP2")
                Delta_P_histo_CorList.append("mmRP2")
                
        if(datatype == "Outbending"):
#             Delta_P_histo_CorList = ['mm0', 'mmF']
#             Delta_P_histo_CorList = ['mm0', 'mmF', 'mmEF']
#             Delta_P_histo_CorList = ['mm0', 'mmF', 'mmExF', 'mmEF']
            Delta_P_histo_CorList = ['mm0', 'mmExF', 'mmEF']

        Delta_P_histo_CompareList = ['el']






    if("pi+" not in Delta_P_histo_CompareList and 'pro' not in Delta_P_histo_CompareList):
        Delta_Pip_histo_SecList = ["all"]



    
    # Set the y-axis range od the ∆P histograms:
        # Note: original default binning was set to 200 bins for a range of -1 to 1 (halved for the elastic colisions)
    if("E" not in event_type):
        extendx_min, extendx_max = -3, 3
        extendx_min, extendx_max = -1, 1
        size_of_Dp_Bins = 0.005
        # size_of_Dp_Bins = 0.01
    else:
        # extendx_min, extendx_max = -0.3, 0.3
        extendx_min, extendx_max = -1, 1
        size_of_Dp_Bins = 0.005
        # size_of_Dp_Bins = 0.01
    if("MC" in event_Name):
        extendx_min, extendx_max = -0.05, 0.05
        extendx_min, extendx_max = -0.02, 0.02
        size_of_Dp_Bins = 0.0001
        # print(size_of_Dp_Bins)
    
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


    # NOT ADDED YET... (Add later)
    # # If Same_Binning_Dp_Q = "no", then the ∆P plots will include phi binning based on particles not being corrected (i.e., will plot ∆P of the electron in terms of the pion phi bins (etc.))
    # # Same_Binning_Dp_Q = "no"
    # Same_Binning_Dp_Q = "yes"

    ##-----------------------------------------------------------------##
    ##-----##-----## Printing Choices for Delta P Histos ##-----##-----##
    ##-----------------------------------------------------------------##
    if(Delta_P_histo_Q == 'y'):
        print(color.BOLD + color.BLUE + "\nFor the ∆P histograms..." + color.END)
        print("".join(["The momentums being calculated are: ", str(Delta_P_histo_CompareList)]))

        print("".join(["The corrections that will run are: ", str(Delta_P_histo_CorList)]))
        print("These Corrections correspond to the following:")
        cor_num = 1
        for cor_names in Delta_P_histo_CorList:
            print("".join(["\t", str(cor_num), ") ", str(cor_names), " -> '", corNameTitles(cor_names), "'"]))
            cor_num += 1
        # if(event_type != "EO" and ("pi+" in Delta_P_histo_CompareList or 'pro' in Delta_P_histo_CompareList)):
        if(event_type != "EO"):
            print("".join(["The ", "Pi+" if(event_type in ["SP", "MC"]) else "proton", " sectors being run are: ", str(Delta_Pip_histo_SecList)]))
        print("".join(["The electron sectors being run are: ", str(ExtraElectronSecListFilter)]))
        # if(event_type != "EO" and ("pi+" in Delta_P_histo_CompareList or 'pro' in Delta_P_histo_CompareList)):
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
        print("\033[1mNot running ∆P histograms...\033[0m")
    ##----------------------------------------------------------------##
    ##-----##-----## Printed Choices for Delta P Histos ##-----##-----##
    ##----------------------------------------------------------------##

    # The value below will just help count the number of histograms made using these calculations (do not change or remove)
    Delta_P_histo_Count, Total_Extra = 0, 0



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

                                            
    if(event_type == "ES"):
        for Cuts in kinematicCuts:
            if(Cuts in ["Both_3", "All"]):
                continue
            # for Calc_Version in ["D_Angle_V1", "D_Angle_V2", "D_Angle_V3", "D_Angle_V4"]:
            for Calc_Version in ["D_Angle_V1", "D_Angle_V3"]:
                if((Cuts in [CutChoice, "Both"] and "V3" in Calc_Version) or (Cuts in [CutChoice_2, "Both_2"] and "V3" not in Calc_Version)):
                    continue
                for correction in Delta_P_histo_CorList:
                    for sec in [0, 1, 2, 3, 4, 5, 6]:
                        Delta_P_histo_Count += 1


        print("".join(["\033[1mNumber of ∆P histograms to be made: \033[0m", str(Delta_P_histo_Count)]))

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
        particleList = ['el', 'pip']
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
        particleList = ['el', 'pro']
        particle_plot_List = ['el', 'pro']
        
        particleList = ['pro']
        particle_plot_List = ['pro']

        
    if(event_type == "ES"):
        particleList = ['el', 'pro']
        particle_plot_List = ['el', 'pro']
#         particleList = ['el']
#         particle_plot_List = ['el']
        
    if(event_type == "EO"):
        particleList = ['el']
        particle_plot_List = ['el']

    correctionList = ['mm0']
    
    
    if(event_type in ["SP", "MC"]):
        if(datatype == "Inbending"):
            # correctionList = ['mm0', 'mmF', 'mmF_PipMMF']
            # correctionList = ['mm0', 'mmF_PipMMF', 'mmExF_PipMMF', 'mmEF_PipMMF']
            # correctionList = ['mm0', 'mmF', 'mmEF', 'mmExF', 'mmF_PipMMF', 'mmExF_PipMMF', 'mmEF_PipMMF']
            # correctionList = ['mm0', 'mmF', 'mmEF', 'mmF_PipMMF', 'mmEF_PipMMF']
            correctionList = ['mm0', 'mmF', 'mmEF', 'mmF_PipMMF', 'mmEF_PipMMF', 'mmEF_PipMMEF']
            correctionList = ['mm0', 'mmEF', 'mmEF_PipMMEF']
            # correctionList = ['mm0', 'mmEF', 'mmEF_PipMMF', 'mmEF_PipMMExF', 'mmEF_PipMMEF']
            
            if("Spring 2019 - Pass 2" in str(pass_version)):
                correctionList.append("mmP2")
                correctionList.append("mmRP2")
                correctionList.append("mmP2_PipMMP2")
                correctionList.append("mmRP2_PipMMP2")
                correctionList.append("mmRP2_PipMMsP2")
                
        if(datatype == "Outbending"):
#             correctionList = ['mm0', 'mmF', 'mmF_PipMMF']
#             correctionList = ['mm0', 'mmF', 'mmF_PipMMF', 'mmEF']
#             correctionList = ['mm0', 'mmF', 'mmF_PipMMF', 'mmExF', 'mmEF', 'mmEF_PipMMEF', 'mmExF_PipMMEF']
            # correctionList = ['mm0', 'mmF', 'mmF_PipMMF', 'mmEF', 'mmEF_PipMMEF']
    
#             correctionList = ['mm0', 'mmEF', 'mmEF_PipMMEF']
            correctionList = ['mm0', 'mmEF', 'mmExF', 'mmEF_PipMMEF', 'mmExF_PipMMExF']
            # correctionList = ['mm0', 'mmF', 'mmF_PipMMF', 'mmEF', 'mmEF_PipMMEF', "mmExF_PipMMEF", "mmExF"]
            
    if(event_type == "DP"):
        if(datatype == "Inbending"):
            # # correctionList = ['mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F_NoELC', 'mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F']
            # # correctionList = ['mm0_NoELC', 'mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_F', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_F']
            # # correctionList = ['mm0_NoELC', 'mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_F', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF']
            # # correctionList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_QEF']
            # # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_QEF']
            # # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF']
            # # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF']
            # # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF']
            # # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_QEF', 'mmEF_PipMMEF_ProMMpro_LEF']
            # # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_REF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_REF']
            # # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_REF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_REF', 'mmEF_PipMMEF_ProMMpro_LEF', 'mmEF_PipMMEF_ProMMpro_QEF']
            # # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_S_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF', 'mmEF_PipMMEF_ProMMpro_S_LEF', 'mmEF_PipMMEF_ProMMpro_SEF']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_S_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEC_NoELC', 'mmEF_PipMMEF_ProMMpro_SERC_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF', 'mmEF_PipMMEF_ProMMpro_S_LEF', 'mmEF_PipMMEF_ProMMpro_SEF', 'mmEF_PipMMEF_ProMMpro_SEC', 'mmEF_PipMMEF_ProMMpro_SERC']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEC_NoELC', 'mmEF_PipMMEF_ProMMpro_SERC_NoELC', 'mmEF_PipMMEF_ProMMpro_SRE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_SEF', 'mmEF_PipMMEF_ProMMpro_SEC', 'mmEF_PipMMEF_ProMMpro_SERC', 'mmEF_PipMMEF_ProMMpro_SRE']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEC_NoELC', 'mmEF_PipMMEF_ProMMpro_SERC_NoELC', 'mmEF_PipMMEF_ProMMpro_SRE_NoELC', 'mmEF_PipMMEF_ProMMpro_SFRE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_SEF', 'mmEF_PipMMEF_ProMMpro_SEC', 'mmEF_PipMMEF_ProMMpro_SERC', 'mmEF_PipMMEF_ProMMpro_SRE', 'mmEF_PipMMEF_ProMMpro_SFRE']
            # correctionList = ['mmEF_PipMMEF_ProMMpro_SEF']
            # correctionList = ['mm0']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_FRE_NoELC', 'mmEF_PipMMEF_ProMMpro_SEC_NoELC', 'mmEF_PipMMEF_ProMMpro_SERC_NoELC', 'mmEF_PipMMEF_ProMMpro_SRE_NoELC', 'mmEF_PipMMEF_ProMMpro_SFRE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_FRE', 'mmEF_PipMMEF_ProMMpro_SEC', 'mmEF_PipMMEF_ProMMpro_SERC', 'mmEF_PipMMEF_ProMMpro_SRE', 'mmEF_PipMMEF_ProMMpro_SFRE']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_FRE_NoELC', 'mmEF_PipMMEF_ProMMpro_RE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_FRE', 'mmEF_PipMMEF_ProMMpro_RE']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_DRE_NoELC', 'mmEF_PipMMEF_ProMMpro_FRE_NoELC', 'mmEF_PipMMEF_ProMMpro_RE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_DRE', 'mmEF_PipMMEF_ProMMpro_FRE', 'mmEF_PipMMEF_ProMMpro_RE']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_NRE_NoELC', 'mmEF_PipMMEF_ProMMpro_FRE_NoELC', 'mmEF_PipMMEF_ProMMpro_RE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_NRE', 'mmEF_PipMMEF_ProMMpro_FRE', 'mmEF_PipMMEF_ProMMpro_RE']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_NRE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_NRE']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_NRE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_NRE']
            correctionList = ['mm0_NoELC', 'mm0_Test_P_NoELC', 'mm0_Test_M_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_NRE_NoELC', 'mm0', 'mm0_Test_P', 'mm0_Test_M', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_NRE']
            correctionList = ['mm0_NoELC', 'mm0_Test_P_NoELC', 'mm0_Test_M_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_Test_M_NoELC', 'mmEF_PipMMEF_Test_P_NoELC', 'mmEF_PipMMEF_ProMMpro_NRE_NoELC', 'mm0', 'mm0_Test_P', 'mm0_Test_M', 'mmEF_PipMMEF', 'mmEF_PipMMEF_Test_M', 'mmEF_PipMMEF_Test_P', 'mmEF_PipMMEF_ProMMpro_NRE']
            correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_NRE_NoELC', 'mmEF_PipMMEF_ProMMpro_NS_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_NRE', 'mmEF_PipMMEF_ProMMpro_NS']
            
            correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_NRE_NoELC', 'mmEF_PipMMEF_ProMMpro_NS_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_NRE', 'mmEF_PipMMEF_ProMMpro_NS']
            
        if(datatype == "Outbending"):
            # correctionList = ['mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F_NoELC', 'mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_F', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_F']
            correctionList = ['mm0_NoELC', 'mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_F', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF']

            
            
            
    if(event_type == "P0"):
        if(datatype == "Inbending"):
            # correctionList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F', 'mmEF', 'mmEF_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F', 'mmEF', 'mmEF_ProMMpro_EF']
            # correctionList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_ProMMpro_EF_NoELC', 'mmEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_EF', 'mmEF_ProMMpro_QEF']
            # correctionList = ['mm0_NoELC', 'mmEF_ProMMpro_EF_NoELC', 'mmEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF_ProMMpro_EF', 'mmEF_ProMMpro_QEF']
            # correctionList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_ProMMpro_EF_NoELC', 'mmEF_ProMMpro_QEF_NoELC', 'mmEF_ProMMpro_LEF_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_EF', 'mmEF_ProMMpro_QEF', 'mmEF_ProMMpro_LEF']
            # correctionList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_ProMMpro_EF_NoELC', 'mmEF_ProMMpro_REF_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_EF', 'mmEF_ProMMpro_REF']
            correctionList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_ProMMpro_EF_NoELC', 'mmEF_ProMMpro_REF_NoELC', 'mmEF_ProMMpro_LEF_NoELC', 'mmEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_EF', 'mmEF_ProMMpro_REF', 'mmEF_ProMMpro_LEF', 'mmEF_ProMMpro_QEF']
            
            correctionList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_ProMMpro_RE_NoELC', 'mmEF_ProMMpro_NRE_NoELC', 'mmEF_ProMMpro_FRE_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_RE', 'mmEF_ProMMpro_NRE', 'mmEF_ProMMpro_FRE']
            correctionList = ['mm0', 'mm0_Test_P', 'mm0_Test_M', 'mmEF', 'mmEF_Test_M', 'mmEF_Test_P', 'mmEF_ProMMpro_NRE']
            
            correctionList = ['mm0', 'mm0_Test_P', 'mm0_Test_M', 'mmEF', 'mmEF_ProMMpro_NRE', 'mmEF_ProMMpro_NS']
            correctionList = ['mm0', 'mm0_Test_P', 'mm0_Test_M']
            correctionList = ['mm0']

            
            
        if(datatype == "Outbending"):
            # correctionList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F', 'mmEF', 'mmEF_ProMMpro_F']
            correctionList = ['mm0_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F', 'mmEF', 'mmEF_ProMMpro_EF']
            
            
    if(event_type == "ES"):
        if(datatype == "Inbending"):
            # correctionList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F', 'mmEF_NoELC', 'mmEF_ProMMpro_F_NoELC', 'mmEF', 'mmEF_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF_ProMMpro_F', 'mmEF_NoELC', 'mmEF_ProMMpro_F_NoELC', 'mmEF', 'mmEF_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF_ProMMpro_F', 'mmEF_ProMMpro_F_NoELC', 'mmEF', 'mmEF_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mm0', 'mmF_ProMMpro_F']
            correctionList = ['mm0', 'mmF']
            
        if(datatype == "Outbending"):
            # correctionList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F', 'mmEF_NoELC', 'mmEF_ProMMpro_F_NoELC', 'mmEF', 'mmEF_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF_ProMMpro_F', 'mmEF_NoELC', 'mmEF_ProMMpro_F_NoELC', 'mmEF', 'mmEF_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF_ProMMpro_F', 'mmEF_ProMMpro_F_NoELC', 'mmEF', 'mmEF_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mm0', 'mmF_ProMMpro_F']
#             correctionList = ['mm0', 'mmF']
            correctionList = ['mm0', 'mmF', 'mmEF']
            
            
    if(event_type == "EO"):
        if(datatype == "Inbending"):
            # correctionList = ['mm0', 'mmF']
            # correctionList = ['mm0', 'mmF', 'mmEF', 'mmExF']
            # correctionList = ['mm0', 'mmF', 'mmEF']
            correctionList = ['mm0', 'mmEF']
            if("Spring 2019 - Pass " in str(pass_version)):
                correctionList.append("mmP2")
                correctionList.append("mmRP2")
                
        if(datatype == "Outbending"):
#             correctionList = ['mm0', 'mmF']
#             correctionList = ['mm0', 'mmF', 'mmEF']
            # correctionList = ['mm0', 'mmF', 'mmExF', 'mmEF']
            correctionList = ['mm0', 'mmExF', 'mmEF']



    binningList = ['1']
    # binningList = ['1','3','5']
    binningList = ['1', '3']
    # binningList = ['3']
    
    # if("E" in event_type):
    #     binningList = ['1']

    # Sector = 0 refers to all sectors so the code will start by making histograms that do not filter by sector
    # Any number 1-6 will correspond to the sector of that same number (do not go above 6)

    # SecRangeMin, SecRangeMax = 0, 6
    SecRangeAll = [0, 1, 2, 3, 4, 5, 6]
    # SecRangeAll = [0]

    # SecRangeMin = min(SecRangeAll)
    # SecRangeMax = max(SecRangeAll)
    # StartOfSRR = 0 if(SecRangeMin == 0 and SecRangeMax > 0) else (SecRangeMin - 1)





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
        print(color.BOLD, color.BLUE, "\nFor the Kinematic histograms...", color.END)
        print("".join(["Particles to be plotted include: ", str(particle_plot_List)]))
        print("".join(["Particles to be used for sector/phi binning include: ", str(particleList)]))

        print("".join(["Corrections included: ", str(correctionList)]))

        print("These Corrections correspond to the following:")
        cor_num = 1
        for cor_names in correctionList:
            print("".join(["   ", str(cor_num), ") ", str(cor_names), " -> '", corNameTitles(cor_names), "'"]))
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
        print("\n\033[1mNot running Kinematic Histograms...\033[0m")

    countHisto = 0


    if(Run_Missing_Mass_Histos == "yes"):
        for Cuts in kinematicCuts:
            # if(Cuts in [Calculated_Exclusive_Cuts if("E" not in event_type) else "esec != -2", Calculated_Exclusive_Cuts_v2, Calculated_Exclusive_Cuts_v3, Calculated_Exclusive_Cuts_v4, Calculated_Exclusive_Cuts_v5, Calculated_Exclusive_Cuts_v6, "Both", "Both_2", "All"]):
            #     continue
            for particle in particle_plot_List:
                for sector in SecRangeAll:
                    for correction in correctionList:
                        for binning in binningList:
                            for particle_filter in particleList:
                                if(same_particle_P_and_Sec_MM and particle != particle_filter):
                                    continue
                                regionList = regList_Call(binning, particle_filter, 1)
                                for region in regionList:
                                    if(Print_Names_Of_Histos_To_Be_Made_Q == 'yes'):
                                        print("Histo: " + str((correction, sector, "", binning, region, particle, particle_filter, "Cut" if(Cuts != "") else "")))
                                    countHisto += 1
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
                            for binning in binningList:
                                regionList = regList_Call(binning, particle_filter, 1)
                                for region in regionList:
                                    countHisto += 1


    print("".join(["\n\033[1mTotal Kinematic Histograms that will be made: \033[0m", str(countHisto)]))

    print("".join(["\033[1mWith the first half of the code, the total will be: \033[0m", str(Total_Extra + countHisto)]))

    count_Total = Total_Extra + countHisto


    if(datatype == "Inbending"):
        # This number should be set to the number of histograms expected to be made per minute while running this code (VERY rough estimate - often changes between runs)
        TimeToProcess = 720 if("DP" in event_type and file_location != "All") else 747 if("P0" in event_type) else 121.8 if("E" in event_type) else 1081 if("Pass" not in str(pass_version)) else 105
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










    #=======================================================================================================================================================================================================================================================#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #=======================================================================================================================================================================================================================================================#










    ################################################################################################################################################################
    ##============================================================================================================================================================##
    ##==========##==========##==========##==========##==========##         Making  Histograms         ##==========##==========##==========##==========##==========##
    ##============================================================================================================================================================##
    ################################################################################################################################################################

    print("".join([color.BOLD, color.BLUE, "\nMaking Histograms now...", color.END]))


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

                    correctionNAME = corNameTitles(correction, Form="splitline")
                    Erdf = Cut_rdf
                    if('pi+' in Delta_P_histo_CompareList and Delta_Pip_histo_Q == 'y'):
                        Erdf = CorDpp(Erdf, correction, "D_pip", event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                        Erdf_MM = CorDpp(Erdf, correction, "MM", event_type, MM_type, datatype, "")
                    if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                        # if("L" not in calc_option):
                        if(calc_option in ["D_p", "D_p_No_C"]):
                            Erdf    = CorDpp(Erdf, correction, "D_pro", event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                            Erdf_MM = CorDpp(Erdf, correction, "MM", event_type, MM_type, datatype, "")
                            Erdf_MM = CorDpp(Erdf_MM, correction, "D_p_L_pro", event_type, MM_type, datatype, "")
                        elif(calc_option in ["D_p_G", "D_p_gL"]):
                            Erdf    = CorDpp(Erdf, correction, "".join([calc_option, "_pro"]), event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                            Erdf_MM = CorDpp(Erdf, correction, "D_p_gL_pro" if(calc_option == "D_p_G") else "D_p_G_pro", event_type, MM_type, datatype, "")
                            Erdf_MM = CorDpp(Erdf_MM, correction, "MM", event_type, MM_type, datatype, "")
                            # Erdf_MM = CorDpp(Erdf_MM, correction, "D_pro", event_type, MM_type, datatype, "")
                            # Erdf_MM = CorDpp(Erdf_MM, correction, "D_p_L_pro", event_type, MM_type, datatype, "")
                        elif("D_p_L" not in calc_option):
                            Erdf    = CorDpp(Erdf, correction, "".join([calc_option, "_pro"]), event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                            Erdf_MM = CorDpp(Erdf, correction, "MM", event_type, MM_type, datatype, "")
                            Erdf_MM = CorDpp(Erdf_MM, correction, "D_p_L_pro", event_type, MM_type, datatype, "")
                            Erdf_MM = CorDpp(Erdf_MM, correction, "D_pro", event_type, MM_type, datatype, "")
                        else:
                            Erdf    = CorDpp(Erdf, correction, "".join([calc_option, "_pro"]), event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                            Erdf_MM = CorDpp(Erdf, correction, "MM", event_type, MM_type, datatype, "")
                            Erdf_MM = CorDpp(Erdf_MM, correction, "D_pro", event_type, MM_type, datatype, "")
                            # print("Printing the full list of variables (and their object types) in the DataFrame (Erdf)...")
                            # for ii in range(0, len(Erdf.GetColumnNames()), 1):
                            #     print("".join([str((Erdf.GetColumnNames())[ii]), " ( type -> ", Erdf.GetColumnType(Erdf.GetColumnNames()[ii]), " )"]))
                            # print("".join(["\tTotal length= ", str(len(Erdf.GetColumnNames()))]))
                            
                    if('el' in Delta_P_histo_CompareList and Delta_Pel_histo_Q == 'y'):
                        Erdf = CorDpp(Erdf, correction, "D_pel", event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                        Erdf_MM = CorDpp(Erdf, correction, "MM", event_type, MM_type, datatype, "")

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
                                                sdf = regFilter(Erdf.Filter("".join(["pip" if(event_type in ["SP", "MC"]) else "pro", "sec == ", str(sec)])), binning, sec, region, 'S', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", 'pip' if(event_type in ["SP", "MC"]) else 'pro')
                                                sdf_MM = regFilter(Erdf_MM.Filter("".join(["pip" if(event_type in ["SP", "MC"]) else "pro", "sec == ", str(sec)])), binning, sec, region, 'S', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", 'pip' if(event_type in ["SP", "MC"]) else 'pro')
                                            else:
                                                sdf = regFilter(Erdf, binning, sec, region, 'S', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", 'pip' if(event_type in ["SP", "MC"]) else 'pro')
                                                sdf_MM = regFilter(Erdf_MM, binning, sec, region, 'S', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", 'pip' if(event_type in ["SP", "MC"]) else 'pro')

                                            if(secEL not in ["all", 0]):
                                                sdf = sdf.Filter("".join(["esec == ", str(secEL)]))
                                                sdf_MM = sdf_MM.Filter("".join(["esec == ", str(secEL)]))


                                            if(binningEL != '1'):
                                                sdf = regFilter(sdf, binningEL, secEL, regionEL, 'S', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", 'el')
                                                histoName               = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title)
                                                histoName_3D            = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title, "MM_3D")
                                                histoName_3D_Dp         = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title, "Dp_3D")
                                                histoName_3D_Theta      = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title, "MM_Theta")
                                                histoName_3D_Theta_Dp   = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title, "Dp_Theta")
                                                histoName_3D_Theta_Dp_2 = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title, "Dp_3D_Theta")
                                                histoName_3D_Electron   = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title, "Dp_Electron")
                                                histoName_3D_El_Theta   = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title, "Dp_El_Theta")
                                            elif("D_p_L" in calc_option):
                                                histoName               = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp")
                                                histoName_3D            = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp", "MM_3D")
                                                histoName_3D_Dp         = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp", "Dp_MM_3D")
                                                histoName_3D_Theta      = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp", "MM_Theta")
                                                histoName_3D_Theta_Dp   = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp", "Dp_MM_Theta")
                                                histoName_3D_Theta_Dp_2 = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp", "Dp_3D_Theta")
                                                histoName_3D_Electron   = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp", "Dp_Electron")
                                                histoName_3D_El_Theta   = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp", "Dp_El_Theta")
                                            elif("No_C" in calc_option):
                                                histoName               = (correction, '', SecName, binning, region, Cut_Title, "No_C")
                                                histoName_3D            = (correction, '', SecName, binning, region, Cut_Title, "No_C", "MM_3D")
                                                histoName_3D_Dp         = (correction, '', SecName, binning, region, Cut_Title, "No_C", "Dp_3D")
                                                histoName_3D_Theta      = (correction, '', SecName, binning, region, Cut_Title, "No_C", "MM_Theta")
                                                histoName_3D_Theta_Dp   = (correction, '', SecName, binning, region, Cut_Title, "No_C", "Dp_Theta")
                                                histoName_3D_Theta_Dp_2 = (correction, '', SecName, binning, region, Cut_Title, "No_C", "Dp_3D_Theta")
                                                histoName_3D_Electron   = (correction, '', SecName, binning, region, Cut_Title, "No_C", "Dp_Electron")
                                                histoName_3D_El_Theta   = (correction, '', SecName, binning, region, Cut_Title, "No_C", "Dp_El_Theta")
                                            elif("S" in calc_option):
                                                histoName               = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp")
                                                histoName_3D            = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp", "MM_3D")
                                                histoName_3D_Dp         = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp", "Dp_3D")
                                                histoName_3D_Theta      = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp", "MM_Theta")
                                                histoName_3D_Theta_Dp   = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp", "Dp_Theta")
                                                histoName_3D_Theta_Dp_2 = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp", "Dp_3D_Theta")
                                                histoName_3D_Electron   = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp", "Dp_Electron")
                                                histoName_3D_El_Theta   = (correction, '', SecName, binning, region, Cut_Title, "Picked_Dp", "Dp_El_Theta")
                                            elif("F" in calc_option):
                                                histoName               = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp")
                                                histoName_3D            = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp", "MM_3D")
                                                histoName_3D_Dp         = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp", "Dp_3D")
                                                histoName_3D_Theta      = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp", "MM_Theta")
                                                histoName_3D_Theta_Dp   = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp", "Dp_Theta")
                                                histoName_3D_Theta_Dp_2 = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp", "Dp_3D_Theta")
                                                histoName_3D_Electron   = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp", "Dp_Electron")
                                                histoName_3D_El_Theta   = (correction, '', SecName, binning, region, Cut_Title, "Flipped_Dp", "Dp_El_Theta")
                                            elif(calc_option in ["D_p_G", "D_p_gL"]):
                                                histoName               = (correction, '', SecName, binning, region, Cut_Title, str(calc_option))
                                                histoName_3D            = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "MM_3D")
                                                histoName_3D_Dp         = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_3D" if(calc_option in ["D_p_G"]) else "Dp_MM_3D")
                                                histoName_3D_Theta      = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "MM_Theta")
                                                histoName_3D_Theta_Dp   = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "".join(["Dp_" if(calc_option in ["D_p_G"]) else "Dp_MM_", "Theta"]))
                                                histoName_3D_Theta_Dp_2 = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_3D_Theta")
                                                histoName_3D_Electron   = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_Electron")
                                                histoName_3D_El_Theta   = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_El_Theta")
                                            elif(str(calc_option) in ["D_p_a", "D_p_b", "D_p_c", "D_p_sqrt"]):
                                                histoName               = (correction, '', SecName, binning, region, Cut_Title, str(calc_option))
                                                histoName_3D            = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "MM_3D")
                                                histoName_3D_Dp         = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_3D")
                                                histoName_3D_Pars       = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_Pars")
                                                histoName_3D_Theta      = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_Theta")
                                                histoName_3D_Theta_Dp_2 = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_3D_Theta")
                                                histoName_3D_Electron   = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_Electron")
                                                histoName_3D_El_Theta   = (correction, '', SecName, binning, region, Cut_Title, str(calc_option), "Dp_El_Theta")
                                            else:
                                                histoName               = (correction, '', SecName, binning, region, Cut_Title)
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
                                            Title_Line_2 = ((("".join(["Correction: ", str(root_color.Bold), "{", str(correctionNAME), "}"]).replace("Pi+", "#pi^{+}")).replace("Pi-", "#pi^{-}")).replace("Phi", "#phi"))
                                            Title_Line_3 = "".join([str(SecName), "".join([" -- #phi_{", "#pi^{+} " if(event_type in ["SP", "MC"]) else "Pro", "} Bin: ", str(regionName)]) if(str(regionName) != "" and "No Phi Bins" not in regionName) else "", "".join([" -- #phi_{El} Bin: ", str(regionNameEL)]) if(str(regionNameEL) != "" and "No Phi Bins" not in regionNameEL) else ""])
                                            Title_Line_4 = "".join(["Cut Applied: ", str(Cut_Title) if(str(Cut_Title) != "") else "No Additional Cuts"])
                                            Title_Axis = "".join(["; p_{Particle}; #Delta p_{Particle}"])

                                            Title = "".join(["#splitline{#splitline{", str(Title_Line_1), "}{", str(Title_Line_2), "}}{#splitline{", str(Title_Line_3), "}{", str(Title_Line_4), "}}", Title_Axis])


                                            if('pi+' in Delta_P_histo_CompareList and Delta_Pip_histo_Q == 'y'):
                                                Dmom_pip_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pip_Histo", str(histoName)]), Title.replace("Particle", "#pi^{+}"), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pip', ''.join(['D_pip_', str(correction)]))
                                                # if(binningEL == '1'):
                                                #     Dmom_pip_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pip_Histo", str(histoName)]), "".join(["#splitline{" if(Cut_Title != "") else "", "(", str(datatype), ") #Delta p_{pip} vs p_{pip} ", str(SecName), " ", str(correctionNAME), " " , str(regionName), "".join(["}{Cut Applied: ", str(Cut_Title), "}"]) if(Cut_Title != "") else "", "; p_{pip}; #Delta p_{pip}"]), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pip', ''.join(['D_pip_', str(correction)]))
                                                # else:
                                                #     Dmom_pip_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pip_Histo", str(histoName)]), "".join(["#splitline{" if(Cut_Title != "") else "", "#splitline{#splitline{(", datatype,") #Delta p_{pip} vs p_{pip} -- ", str(SecName), "}{Correction: ", str(correctionNAME), "}}{Pi+: ", str(regionName) + " -- El: ", str(regionNameEL), "".join(["}{Cut Applied: ", str(Cut_Title)]) if(Cut_Title != "") else "", "}; p_{pip}; #Delta p_{pip}"]), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pip', ''.join(['D_pip_', str(correction)]))

                                                Delta_P_histo_Count += 1
                                                
#                                                 Title_3D_Pip = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "#Delta p_{Particle} vs Missing Mass vs p_{Particle}")).replace(Title_Axis, "; p_{Particle}; #Delta p_{Particle}; Missing Mass")).replace("Particle", "#pi^{+}")
#                                                 # Title_3D_Pip = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "#Delta p_{Particle} vs #theta_{Particle} vs p_{Particle}")).replace(Title_Axis, "; p_{Particle}; #Delta p_{Particle}; Missing Mass")).replace("Particle", "Pro")
#                                                 x_variable = 'pip'
#                                                 y_variable = ''.join(['D_pip_', str(correction)])
#                                                 z_variable = str(correction)
#                                                 # z_variable = "proth"
#                                                 # Dmom_pip_Histo[histoName_3D] = sdf_MM.Histo3D(("".join(["Dmom_pip_Histo", str(histoName_3D)]), Title_3D_Pip, 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max, Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max), x_variable, y_variable, str(correction))
#                                                 Dmom_pip_Histo[histoName_3D] = sdf_MM.Histo3D(("".join(["Dmom_pip_Histo", str(histoName_3D)]), Title_3D_Pip, 100, 0, 10, 100, -0.5, 0.5, 100, 0.5, 1.2), x_variable, y_variable, z_variable)
#                                                 # Dmom_pip_Histo[histoName_3D] = sdf_MM.Histo3D(("".join(["Dmom_pip_Histo", str(histoName_3D)]), Title_3D_Pip, 100, 0, 10, 100, -0.5, 0.5, 20, 0, 60), x_variable, y_variable, z_variable)
#                                                 Delta_P_histo_Count += 1


                                            if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                                                Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), Title.replace("Particle", "Pro"), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pro' if(("_NoELC" in correction) or ("No_C" in calc_option) or ("MC" in event_Name)) else "pro_cor", ''.join(['D_pro_' if(str(calc_option) in ["D_p", "D_p_No_C"]) else ''.join([str(calc_option), '_pro_']), str(correction)]))
                                                # if(binningEL == '1'):
                                                #     Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), "".join(["#splitline{" if(Cut_Title != "") else "", "(", str(datatype), ") #Delta p_{pro} vs p_{pro} ", str(SecName), " ", str(correctionNAME), " " ,str(regionName), "".join(["}{Cut Applied: ", str(Cut_Title), "}"]) if(Cut_Title != "") else "", "; ", "p_{pro}" if("_NoELC" in correction) else "Corrected p_{pro}", "; #Delta p_{pro}"]), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pro' if("_NoELC" in correction) else "pro_cor", ''.join(['D_pro_', str(correction)]))
                                                # else:
                                                #     Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), "".join(["#splitline{" if(Cut_Title != "") else "", "#splitline{#splitline{#Delta p_{pro} vs p_{pro} -- ", str(SecName), "}{Correction: ", str(correctionNAME), "}}{Pro: ", str(regionName) + " -- El: ", str(regionNameEL), "".join(["}{Cut Applied: ", str(Cut_Title)]) if(Cut_Title != "") else "", "}; ", "p_{pro}" if("_NoELC" in correction) else "Corrected p_{pro}", "; #Delta p_{pro}"]), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pro' if("_NoELC" in correction) else "pro_cor", ''.join(['D_pro_', str(correction)]))

                                                Delta_P_histo_Count += 1

                                                # # Dmom_pro_Histo[histoName_3D] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D)]), "".join([str(Title.replace("#Delta p_{Particle} vs p_{Particle}", "#Delta p_{Particle} vs p_{Particle} vs Missing Mass")).replace("Particle", "Pro"), "; Missing Mass"]), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max, Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max), 'pro' if("_NoELC" in correction or "No_C" in calc_option) else "pro_cor", ''.join(['D_pro_' if("L" not in calc_option) else 'D_p_L_pro_', str(correction)]), str(correction))
                                                # # Dmom_pro_Histo[histoName_3D] = sdf_MM.Histo2D(("".join(["Dmom_pro_Histo", str(histoName_3D)]), Title.replace("Particle", "Pro"), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pro' if("_NoELC" in correction or "No_C" in calc_option) else "pro_cor", ''.join(['D_pro_' if("L" not in calc_option) else 'D_p_L_pro_', str(correction)]))
                                                # Dmom_pro_Histo[histoName_3D] = sdf_MM.Histo2D(("".join(["Dmom_pro_Histo", str(histoName_3D)]), str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "#Delta p_{Particle} vs Missing Mass")).replace(Title_Axis, "; #Delta p_{Particle}; Missing Mass")).replace("Particle", "Pro"), NumOfExtendedBins, extendx_min, extendx_max, Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max), ''.join(['D_pro_' if("L" not in calc_option) else 'D_p_L_pro_', str(correction)]), str(correction))
                                                
                                                
                                                Title_3D_Pro = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "#Delta p_{Particle} vs Missing Mass^{2} vs p_{Particle}")).replace(Title_Axis, "; p_{Particle}; #Delta p_{Particle}; MM^{2}")).replace("Particle", "Pro")
                                                # Title_3D_Pro = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "#Delta p_{Particle} vs #theta_{Particle} vs p_{Particle}")).replace(Title_Axis, "; p_{Particle}; #Delta p_{Particle}; Missing Mass")).replace("Particle", "Pro")
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
                                                
                                                # if(str(calc_option) in ["D_p_sqrt"]):
                                                #     print("".join([color.BOLD, str(calc_option), ' in ["D_p_sqrt"]', color.BLUE, "\ndp_min = ", str(dp_min), "\ndp_max = ", str(dp_max), "\ndp_bin = ", str(dp_bin), color.END]))
                                                
                                                
                                                MM_min, MM_max = -0.1, 0.3
                                                if("(GEN)" in event_Name):
                                                    MM_min, MM_max = -0.05, 0.05
                                                # z_variable = "proth"
                                                # Dmom_pro_Histo[histoName_3D] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D)]), Title_3D_Pro, 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max, Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max), x_variable, y_variable, str(correction))
                                                Dmom_pro_Histo[histoName_3D] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D)]), Title_3D_Pro, 100, 0, 10, dp_bin, dp_min, dp_max, 200, MM_min, MM_max), x_variable, y_variable, z_variable)
                                                # Dmom_pro_Histo[histoName_3D] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D)]), Title_3D_Pro, 100, 0, 10, 100, -0.5, 0.5, 20, 0, 60), x_variable, y_variable, z_variable)
                                                Delta_P_histo_Count += 1
                                                
                                                Title_3D_Pro_EL       = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "#Delta p_{Pro} vs #theta_{Pro} vs #theta_{El}")).replace(str(Title_Axis), "; #theta_{Pro}; #Delta p_{Pro}; #theta_{El}"))
                                                Title_3D_Pro_EL_Theta = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "#Delta p_{Pro} vs #theta_{Pro} vs #theta_{El}")).replace(str(Title_Axis), "; #theta_{Pro}; #Delta p_{Pro}; #theta_{El}"))
                                                Dmom_pro_Histo[histoName_3D_Electron] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_Electron)]), Title_3D_Pro_EL,       100, 0, 10,  dp_bin, dp_bin, dp_min, 100, 0, 10),  "pro",   str(y_variable), "el")
                                                Dmom_pro_Histo[histoName_3D_El_Theta] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_El_Theta)]), Title_3D_Pro_EL_Theta, 100, 0, 100, dp_bin, dp_bin, dp_min, 100, 0, 100), "proth", str(y_variable), "elth")
                                                Delta_P_histo_Count += 2
                                                
                                                if(str(calc_option) in ["D_p", "D_p_L", "D_p_G", "D_p_gL"]):
                                                    # print("".join([color.BOLD, color.BLUE, "\n\ncalc_option = ", str(calc_option), "\n\n", color.END]))
                                                    Title_3D_Pro_Dp = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "(Both) #Delta p_{Particle} vs p_{Particle}")).replace(Title_Axis, "; p_{Particle}; (Best) #Delta p_{Particle}; (Secondary) #Delta p_{Particle}")).replace("Particle", "Pro")
                                                    if(calc_option in ["D_p_G", "D_p_gL"]):
                                                        Title_3D_Pro_Dp = str(Title_3D_Pro_Dp).replace("(Both)", "(Both - Generated)")
                                                    x_variable = 'pro' if(('_NoELC' in str(correction)) or ('No_C' in str(calc_option)) or ("MC" in event_Name)) else 'pro_cor'
                                                    x_bins, x_min, x_max = 100, 0, 10
                                                    
                                                    if(str(calc_option) in ["D_p_L", "D_p_gL"]):
                                                        x_variable = str(correction)
                                                        Title_3D_Pro_Dp = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "(Both) #Delta p_{Particle} vs MM^{2}")).replace(Title_Axis, "; MM^{2}; (Best) #Delta p_{Particle}; (Secondary) #Delta p_{Particle}")).replace("Particle", "Pro")
                                                        x_bins, x_min, x_max = 200, MM_min, MM_max
                                                    y_variable = ''.join(['D_pro_', str(correction)])     if(calc_option not in ["D_p_G", "D_p_gL"]) else ''.join(['D_p_G_pro_',  str(correction)])
                                                    z_variable = ''.join(['D_p_L_pro_', str(correction)]) if(calc_option not in ["D_p_G", "D_p_gL"]) else ''.join(['D_p_gL_pro_', str(correction)])
                                                    # Dmom_pro_Histo[histoName_3D_Dp] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_Dp)]), Title_3D_Pro_Dp, int(x_bins), x_min, x_max, dp_bin, dp_min, dp_max, 200, -0.5, 0.5), x_variable, y_variable, z_variable)
                                                    
                                                    Dmom_pro_Histo[histoName_3D_Dp]         = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_Dp)]),         str(Title_3D_Pro_Dp), int(x_bins), x_min, x_max, dp_bin, dp_min, dp_max, 201, -0.15025, 0.15025), x_variable, y_variable, z_variable)
                                                    Dmom_pro_Histo[histoName_3D_Theta_Dp_2] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_Theta_Dp_2)]), str((Title_3D_Pro_Dp.replace("MM^{2}", "#theta_{Pro}")).replace("p_{Pro}; (Best)", "#theta_{Pro}; (Best)")).replace("vs p_{Pro}", "vs #theta_{Pro}"), 100, 0, 100, dp_bin, dp_min, dp_max, 201, -0.15025, 0.15025), "proth", y_variable, z_variable)
                                                    Delta_P_histo_Count += 2

                                                if(str(calc_option) not in ["D_p_a", "D_p_b", "D_p_c", "D_p_sqrt"]):
                                                    Title_3D_Pro_Theta    = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "#Delta p_{Particle} vs #theta_{Particle} vs p_{Particle}")).replace(Title_Axis, "; p_{Particle}; #Delta p_{Particle}; #theta_{Particle}")).replace("Particle", "Pro")
                                                    Title_3D_Pro_Theta_MM = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "Missing Mass^{2} vs #theta_{Particle} vs p_{Particle}")).replace(Title_Axis, "; p_{Particle}; MM^{2}; #theta_{Particle}")).replace("Particle", "Pro")
                                                    if(str(calc_option) in ["D_p_a", "D_p_b", "D_p_c", "D_p_sqrt"]):
                                                        Title_3D_Pro_Theta    = Title_3D_Pro_Theta.replace("#Delta p_{Pro}", str(calc_option))
                                                        Title_3D_Pro_Theta_MM = Title_3D_Pro_Theta_MM.replace("#Delta p_{Pro}", str(calc_option))
                                                    y_variable = ''.join(['D_pro_' if(str(calc_option) in ["D_p", "D_p_No_C"]) else ''.join([str(calc_option), '_pro_']), str(correction)])
                                                    Dmom_pro_Histo[histoName_3D_Theta_Dp] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_Theta_Dp)]), Title_3D_Pro_Theta, 100, 0, 10, dp_bin, dp_min, dp_max, 100, 0, 100), "pro", str(y_variable), "proth")
                                                    Dmom_pro_Histo[histoName_3D_Theta]    = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_Theta)]), Title_3D_Pro_Theta_MM, 100, 0, 10, dp_bin, MM_min, MM_max, 100, 0, 100), "pro", str(correction), "proth")
                                                    Delta_P_histo_Count += 2
                                                else:
                                                    Title_3D_Pro_Dp       = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "".join([str(calc_option), " vs #Delta p_{Particle} vs p_{Particle}"]))).replace(Title_Axis, "".join(["; p_{Particle}; ", str(calc_option), "; #Delta p_{Particle}"]))).replace("Particle", "Pro")
                                                    Title_3D_Pro_Theta    = str((Title.replace("#Delta p_{Particle} vs p_{Particle}", "".join([str(calc_option), " vs #theta_{Particle} vs p_{Particle}"])).replace(Title_Axis,    "".join(["; p_{Particle}; ", str(calc_option), "; #theta_{Particle}"])))).replace("Particle", "Pro")
                                                    # pars_variable = ''.join(['D_pro_' if(str(calc_option) in ["D_p", "D_p_No_C"]) else ''.join([str(calc_option), '_pro_']), str(correction)])
                                                    pars_variable = ''.join([str(calc_option), '_pro_', str(correction)])
                                                    dp_variable   = ''.join(['D_pro_', str(correction)])
                                                    
                                                    Dmom_pro_Histo[histoName_3D_Dp]    = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_Dp)]),    Title_3D_Pro_Dp,    100, 0, 10, dp_bin, dp_min, dp_max, 201, -0.05025, 0.05025), "pro", str(pars_variable), str(dp_variable))
                                                    Dmom_pro_Histo[histoName_3D_Theta] = sdf_MM.Histo3D(("".join(["Dmom_pro_Histo", str(histoName_3D_Theta)]), Title_3D_Pro_Theta, 100, 0, 10, dp_bin, dp_min, dp_max, 100,  0,       100),     "pro", str(pars_variable), "proth")
                                                    Delta_P_histo_Count += 2
                                                    
                                                    # if(str(calc_option) in ["D_p_sqrt"]):
                                                    #     print("".join([color.BOLD, str(calc_option), ' in ["D_p_sqrt"] (CHECK 2)', color.BLUE, "\ndp_min = ", str(dp_min), "\ndp_max = ", str(dp_max), "\ndp_bin = ", str(dp_bin), color.END]))
                                                    #     print("".join([color.BLUE, "pars_variable = ", str(pars_variable), color.END]))
                                                    #     print("".join([color.BLUE, "Dmom_pro_Histo[histoName_3D_Dp].GetNbinsX() = ", str(Dmom_pro_Histo[histoName_3D_Dp].GetNbinsX()), "\nDmom_pro_Histo[histoName_3D_Dp].GetNbinsY() = ", str(Dmom_pro_Histo[histoName_3D_Dp].GetNbinsY()), "\nDmom_pro_Histo[histoName_3D_Dp].GetNbinsZ() = ", str(Dmom_pro_Histo[histoName_3D_Dp].GetNbinsZ()), "\n", color.END]))
                                                    # else:
                                                    #     print("".join([color.RED, "INCORRECT FOR D_p_sqrt", color.END]))
                                                    #     print("".join([color.RED, "calc_option = ", str(calc_option), color.BOLD, "\ndp_min = ", str(dp_min), "\ndp_max = ", str(dp_max), "\ndp_bin = ", str(dp_bin), color.END]))
                                                        



                                            if('el' in Delta_P_histo_CompareList and Delta_Pel_histo_Q == 'y'):
                                                # Dmom_pel_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pel_Histo", str(histoName)]), Title.replace("Particle", "El"), 120, 0, 12, NumOfExtendedBins, extendx_min, extendx_max), 'el', ''.join(['D_pel_', str(correction)]))
                                                Dmom_pel_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pel_Histo", str(histoName)]), Title.replace("Particle", "El"), 400, 0.5, 10.5, NumOfExtendedBins, extendx_min, extendx_max), 'el', ''.join(['D_pel_', str(correction)]))
                                                # Dmom_pel_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pel_Histo", str(histoName)]), Title.replace("Particle", "El"), 240 if("E" not in event_type) else 120, 0, 12, NumOfExtendedBins, extendx_min, extendx_max), 'el', ''.join(['D_pel_', str(correction)]))
                                                # if(binningEL == '1'):
                                                #     Dmom_pel_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pel_Histo", str(histoName)]), "".join(["#splitline{" if(Cut_Title != "") else "", "(", str(datatype), ") #Delta p_{el} vs p_{el} ", str(SecName), " ", str(correctionNAME), " ", str(regionName), "".join(["}{Cut Applied: ", str(Cut_Title), "}"]) if(Cut_Title != "") else "", "; p_{el}; #Delta p_{el}"]), 240 if(event_type != "ES") else 120, 0, 12, NumOfExtendedBins, extendx_min, extendx_max), 'el', ''.join(['D_pel_', str(correction)]))
                                                # else:
                                                #     Dmom_pel_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pel_Histo", str(histoName)]), "".join(["#splitline{" if(Cut_Title != "") else "", "#splitline{#splitline{(", datatype,") #Delta p_{el} vs p_{el} -- ", str(SecName), "}{Correction: ", str(correctionNAME), "}}{Pi+: ", str(regionName), " -- El: ", str(regionNameEL), "".join(["}{Cut Applied: ", str(Cut_Title)]) if(Cut_Title != "") else "", "}; p_{el}; #Delta p_{el}"]), 240 if(event_type != "ES") else 120, 0, 20 if(event_type != "ES") else 12, NumOfExtendedBins, extendx_min, extendx_max), 'el', ''.join(['D_pel_', str(correction)]))

                                                Delta_P_histo_Count += 1


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

                    correctionNAME = corNameTitles(correction, Form="splitline")
                    
                    Erdf = Cut_rdf
                    Erdf = CorDpp(Erdf, correction, Calc_Version, event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")

                    for sec in [0, 1, 2, 3, 4, 5, 6]:

                        SecName = "".join(["El Sector ", str(sec)]) if(sec != 0) else "All Sectors"

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
                        Title_Axis = "".join(["; p_{El}; #Delta", "#theta_{Pro}" if("V3" not in Calc_Version) else "#phi_{|El-Pro|}"])

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

                                    hmmCPARTall[name] = Missing_Mass_Histo_Maker(regFilter(sdf, binning, sector, region, '', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", particle_filter), correction, sector, region, '', binning, particle, particle_filter, Cut_Title)
                                    count += 1


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
                correctionNAME = corNameTitles(correction, Form="splitline")
                for particle in particleList:
                    for shift in shiftList:
                        for local_Q in ["", "local "]:
                            if(shift == "NS" and "local" in local_Q):
                                continue
                            for sector in SecRangeAll:
                                
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
                                
                                Title_Mom_The_Axis = "".join(["; p_{",    str(particle_title), "}; #theta_{", str(particle_title), "}"])
                                Title_Mom_Phi_Axis = "".join(["; p_{",    str(particle_title), "}; #phi_{",   str(particle_title), "}"])
                                Title_The_Phi_Axis = "".join(["; #phi_{", str(particle_title), "}; #theta_{", str(particle_title), "}"])

                                Title_Mom_The = "".join(["#splitline{#splitline{", str(Title_Mom_The_Line_1), " ", str(sector_title), "}{", str(Title_Line_2), "}}{", str(Title_Line_3), "}", str(Title_Mom_The_Axis)])
                                Title_Mom_Phi = "".join(["#splitline{#splitline{", str(Title_Mom_Phi_Line_1), " ", str(sector_title), "}{", str(Title_Line_2), "}}{", str(Title_Line_3), "}", str(Title_Mom_Phi_Axis)])
                                Title_The_Phi = "".join(["#splitline{#splitline{", str(Title_The_Phi_Line_1), " ", str(sector_title), "}{", str(Title_Line_2), "}}{", str(Title_Line_3), "}", str(Title_The_Phi_Axis)])
                                

                                # title_theta = "".join(["#splitline{" if(Cut_Title != "") else "", "#splitline{(", datatype, ") ", "#theta_{", particle_title, "} vs p_{", particle_title, "} ", sector_title, shiftTitle(shift), "}{Cor: ", corNameTitles(correction), "".join(["}{Cut Applied: ", str(Cut_Title)]) if(Cut_Title != "") else "", "}; p_{", particle_title, "}; #theta_{", particle_title, "} [#circ]"])
                                # title_phi = "".join(["#splitline{" if(Cut_Title != "") else "", "#splitline{(", datatype, ") ", local_Q, "#phi_{", particle_title, "} vs p_{", particle_title, "} ", sector_title, shiftTitle(shift), "}{Cor: ", corNameTitles(correction), "".join(["}{Cut Applied: ", str(Cut_Title)]) if(Cut_Title != "") else "", "}; p_{", particle_title, "}; ", local_Q, "#phi_{", particle_title, "} [#circ]"])
                                # title_theta_phi = "".join(["#splitline{" if(Cut_Title != "") else "", "(", str(datatype), ") ", "#theta_{", particle_title, "} vs ", local_Q, "#phi_{", particle_title, "} ", sector_title, shiftTitle(shift), "".join(["}{Cut Applied: ", str(Cut_Title), "}"]) if(Cut_Title != "") else "", "; ", local_Q, "#phi_{", particle_title, "} [#circ]; #theta_{", particle_title, "} [#circ]"])

                                # hPARTthall_ref_title = "".join(["hPARTthall_", particle, "thallSec", str(sector), shift, "" if correction == "mm0" else "".join(["_", correction]), local_Q])
                                # hPARTPhiall_ref_title = "".join(["hPARTPhiall_", particle, "PhiSec", str(sector), shift, "" if correction == "mm0" else "".join(["_", correction]), local_Q])
                                # hPARTthPhiall_ref_title = "".join(["hPARTthPhiall_", particle, "thPhiSec", str(sector), shift, local_Q])

                                Histo_Mom_The_ref_title = "".join(["Histo_P_v_Th_",   str(ref)])
                                Histo_Mom_Phi_ref_title = "".join(["Histo_P_v_Phi_",  str(ref)])
                                Histo_The_Phi_ref_title = "".join(["Histo_Th_v_Phi_", str(ref)])

                                if(sector == 0):
                                    sdf = CorDpp(rdf, correction, "".join(["Mom_", particle]), event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                                else:
                                    sdf = CorDpp(rdf.Filter("".join([particle.replace("l", ""), "sec", " == ", str(sector)])), correction, "".join(["Mom_", particle]), event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")

                                Histo_P_v_Phi[ref]      = sdf.Histo2D((Histo_Mom_Phi_ref_title, Title_Mom_Phi, 110,  0,   11,  720, -260, 460), "".join([particle, "_", correction]),                        "".join([local_Q.replace(" ", ""), particle, "Phi", shift]))
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

    Full_Crash_Check = "n"
    # Full_Crash_Check = "y"
    

    if(SaveResultsQ == 'yes'):
        print("\n\033[1mSaving Results Now...\033[0m")
        RoutputFile = ROOT.TFile(str(OutputFileName), 'recreate')
    elif(CheckDataFrameQ == "y"):
        print("\n\033[1mPrinting the Results to be Saved Now...\033[0m")
    else:
        print("\n\033[1mPrinting the Final Count...\033[0m")

    countSaved = 0


    # # # # # # # # # # # # # # # # # # # #    For the ∆P Histograms    # # # # # # # # # # # # # # # # # # # # 

    if(Delta_P_histo_Q == 'y'):

        if('pi+' in Delta_P_histo_CompareList and Delta_Pip_histo_Q == 'y'):
            for saving_Dp_pip_name in Dmom_pip_Histo:
                if(SaveResultsQ == 'yes'):
                    Dmom_pip_Histo[saving_Dp_pip_name].Write()
                elif(CheckDataFrameQ == "y"):
                    print("".join(["Dmom_pip_Histo[", str(saving_Dp_pip_name), "]"]))
                elif(Full_Crash_Check == "y"):
                    print("".join(["type = ", str(type(Dmom_pip_Histo[saving_Dp_pip_name]))]))
                countSaved += 1

        if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
            for saving_Dp_pro_name in Dmom_pro_Histo:
                if(SaveResultsQ == 'yes'):
                    Dmom_pro_Histo[saving_Dp_pro_name].Write()
                elif(CheckDataFrameQ == "y"):
                    print("".join(["Dmom_pro_Histo[", str(saving_Dp_pro_name), "]"]))
                elif(Full_Crash_Check == "y"):
                    print("".join(["type = ", str(type(Dmom_pro_Histo[saving_Dp_pro_name]))]))
                countSaved += 1

        if('el' in Delta_P_histo_CompareList and Delta_Pel_histo_Q == 'y'):
            for saving_Dp_pel_name in Dmom_pel_Histo:
                if(SaveResultsQ == 'yes'):
                    Dmom_pel_Histo[saving_Dp_pel_name].Write()
                elif(CheckDataFrameQ == "y"):
                    print("".join(["Dmom_pel_Histo[", str(saving_Dp_pel_name), "]"]))
                elif(Full_Crash_Check == "y"):
                    print("".join(["type = ", str(type(Dmom_pel_Histo[saving_Dp_pel_name]))]))
                countSaved += 1

                
                
                
    # # # # # # # # # # # # # # # # # # # #    For the ∆Angle Histograms    # # # # # # # # # # # # # # # # # # # # 
                
        
        
    if(event_type == "ES"):
        for saving_DAngle_name in Dmom_Angle_Histo:
            if(SaveResultsQ == 'yes'):
                Dmom_Angle_Histo[saving_DAngle_name].Write()
            elif(CheckDataFrameQ == "y"):
                print("".join(["Dmom_Angle_Histo[", str(saving_DAngle_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print("".join(["type = ", str(type(Dmom_Angle_Histo[saving_DAngle_name]))]))
            countSaved += 1
            
            
            

    # # # # # # # # # # # # # # # # # # Second half of code (Missing Mass Histograms) # # # # # # # # # # # # # # # # # #

    if(Run_Missing_Mass_Histos == "yes"):
        for saving_MM_name in hmmCPARTall:
            if(SaveResultsQ == 'yes'):
                hmmCPARTall[saving_MM_name].Write()
            elif(CheckDataFrameQ == "y"):
                print("".join(["hmmCPARTall[", str(saving_MM_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print("".join(["type = ", str(type(hmmCPARTall[saving_MM_name]))]))
            countSaved += 1


    # # # # # # # # # # # # # # #   Other Phase Space Histograms (without Missing Mass)   # # # # # # # # # # # # # # #

    if(Run_Phase_Space == 'yes'):
        for saving_th_name in Histo_P_v_Th:
            if(SaveResultsQ == 'yes'):
                Histo_P_v_Th[saving_th_name].Write()
            elif(CheckDataFrameQ == "y"):
                print("".join(["Histo_P_v_Th[", str(saving_th_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print("".join(["type = ", str(type(Histo_P_v_Th[saving_th_name]))]))
            countSaved += 1

        for saving_Phi_name in Histo_P_v_Phi:
            if(SaveResultsQ == 'yes'):
                Histo_P_v_Phi[saving_Phi_name].Write()
            elif(CheckDataFrameQ == "y"):
                print("".join(["Histo_P_v_Phi[", str(saving_Phi_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print("".join(["type = ", str(type(Histo_P_v_Phi[saving_Phi_name]))]))
            countSaved += 1

        for saving_thPhi_name in Histo_Th_v_Phi:
            if(SaveResultsQ == 'yes'):
                Histo_Th_v_Phi[saving_thPhi_name].Write()
            elif(CheckDataFrameQ == "y"):
                print("".join(["Histo_Th_v_Phi[", str(saving_thPhi_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print("".join(["type = ", str(type(Histo_Th_v_Phi[saving_thPhi_name]))]))
            countSaved += 1

    # # # # # # # # # # # # # # # # # # # # #     Invariant Mass Histograms     # # # # # # # # # # # # # # # # # # # # #

    if(Run_Invariant_Mass_Histos == 'yes'):
        for saving_WM_name in HWC_Histo_All:
            if(SaveResultsQ == 'yes'):
                HWC_Histo_All[saving_WM_name].Write()
            elif(CheckDataFrameQ == "y"):
                print("".join(["HWC_Histo_All[", str(saving_WM_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print("".join(["type = ", str(type(HWC_Histo_All[saving_WM_name]))]))
            countSaved += 1


    # # # # # # # # # # # # # # # # # # # # #               Done               # # # # # # # # # # # # # # # # # # # # #


    if(SaveResultsQ == 'yes'):
        RoutputFile.Close()
        print("".join(["\033[1mTotal Histograms Saved = \033[0m", str(countSaved)]))
    else:
        print("".join(["\033[1mTotal Histograms that would be saved = \033[0m", str(countSaved)]))


    ###############################################################################################################################################################
    ##===========================================================================================================================================================##
    ##==========##==========##==========##==========##==========##         Saved  Histograms         ##==========##==========##==========##==========##==========##
    ##===========================================================================================================================================================##
    ###############################################################################################################################################################
#     else:
#         print("\n\n\033[1mCode not set to make the histograms at this time.\033[0m")




    print("\n\033[1mThe code has finished running.\033[0m")

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

