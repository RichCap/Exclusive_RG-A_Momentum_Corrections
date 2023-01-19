import ROOT, numpy
import array
from datetime import datetime

from sys import argv
# Let there be 4 arguements in argv when running this code

# Arguement 1: Name of this code (File_Creation_Final_Momentum_Corrections_Github.py)

# Arguement 2: data-type (In/Out)
    # Options: 
    # 1) In -> Inbending
    # 2) Out -> Outbending

# Arguement 3: event-type (type of exclusive events)
    # Options: 
    # 1) SP -> Single Pion (i.e., ep->eπ+N)
    # 2) DP -> Double Pion (i.e., ep->epπ+π-)
    # 3) P0 -> Pi0 Channel (i.e., ep->epπ0)
    # 4) ES -> Elastic Scattering (i.e., ep->e'p')
    # 4) EO -> Electron Only (i.e., ep->e'X)
    # 5) MC -> Simulated Single Pion (i.e., ep->eπ+N  - same option as SP but file names will be different)


# Arguement 4: file number (Full file name)
    # If the file number is given as 'All', then all files will be run instead of a select number of them
    # If the file number is given as 'test', then the code will run without saving any of the histograms

# EXAMPLES: 
    # python File_Creation_Final_Momentum_Corrections_Github.py In SP All
        # The line above would run ALL INBENDING files together for the ep->eπ+N channel
    # python File_Creation_Final_Momentum_Corrections_Github.py Out DP test
        # The line above would test-run the OUTBENDING files for the ep->epπ+π- channel (no results would be saved)
        
        
        

code_name, datatype, event_type, file_location = argv

datatype, file_location, event_type = ''.join([str(datatype), "bending"]), str(file_location), str(event_type)

file_name = str(file_location)


pass_version = "NA"
Beam_Energy = 10.6041 # Fall 2018 Beam Energy

# Spring 2019 Data sets
if("P1" in event_type):
    pass_version = "Spring 2019 - Pass 1"
    Beam_Energy = 10.1998
if("P2" in event_type):
    pass_version = "Spring 2019 - Pass 2"
    Beam_Energy = 10.1998
if("C" in event_type):
    pass_version = "".join([pass_version, " - Central Detector"])
    
event_type = str(((event_type.replace("P1", "")).replace("P2", "")).replace("C", ""))
    
    
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
    π       = '#pi'
    Degrees = '#circ'
    
    Line = '#splitline'


event_Name = "error"

if(event_type == "E0"):
    print(color.RED + "ERROR: E0 is not the correct input type..." + color.END + "\n\tSetting to event_type = EO")
    event_type = "EO"


if(event_type in ["SP", "MC"]):
    event_Name = "Single Pion Channel"
    MM_type = "epipX"
    
if(event_type == "DP"):
    event_Name = "Double Pion Channel"
    # # Missing Mass Choice:
    MM_type = "eppipX"
    # MM_type = "eppippim"
    # MM_type = "eppimX"
    # MM_type = "epippimX"
    
if(event_type == "P0"):
    event_Name = "Pi0 Channel"
    MM_type = "eppi0X"
    
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
            auto Proton_Mass = 0.938;
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
            auto Proton_Mass = 0.938;
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
        
        
    if(event_type in ["SP", "SP_P1", "SP_P2", "MC"]):
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

    
    
#     Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V9"
#     # Increased the number of bins used in the ∆Theta_Pro Histograms
#     # Added an additional exclusivity cut (CutChoice_2) based on ∆Theta Calculation (D_Angle_V1)
#     # Exclusivity Cuts now do not use linear or quadratic equations, but instead use the gaussian widths of the fitted histograms
#     # "Cut_Function" now supports a combination of all of these added cuts (names updated somewhat from V8 to differentiate between all of the cut options)
#     # Removed Phi binning from the Elastic Channel (option was not being used)
    
#     Extra_Part_of_Name = "_GitHub_Cut_Tests_V7"
#     # Made the basic Invariant Mass cut tighter (i.e., "Calculated_Exclusive_Cuts_V2" --> W < 0.7 GeV and W > 1.2 GeV)
#     # Decreased the range of the y-axis of the ∆P plots (decreased to ±1 GeV with the same sizes of binning --> the ideal may be even lower as all desirable events are between ±0.3 Gev but the range has been extended to see more when necessary)
    
    
#     Extra_Part_of_Name = "_GitHub_Electron_Refinement_V1"
#     # Reintroduced the automatic baseline cut on Invariant Mass for elastic channels (W < 0.6 GeV and W > 1.3 GeV --- "Calculated_Exclusive_Cuts_V2" is not effected)
#     # Increased the bin sizes along the y-axis of the ∆P plots for the non-elastic channels (same bin ranges as before, but the bin sizes are now consistent with those from the elastic scattering channels)
#         # Other similar updates were also added so that these channels will produce plots which are consistent with the elastic scattering events
#     # Running with electron phi bins
#     # Phase space histograms now only create a plot for sector 0 (i.e., all sectors -- Optional condition that can be turned off -- does not affect other options)
#     # Only running electron kinematics and corrections (for elastic and single pion channels -- Pi+ corrections are included in the SP channel)
#     # Updated the default location of the SP files (compatible with current file names for the SP files made with the groovy script)
    
    
    
#     Extra_Part_of_Name = "_GitHub_Electron_Refinement_V2"
#     # Minor update to histogram titles (related to the phi binning parts of titles)
#     # Updated SP files to take in files using skim4 data (files which did not have the W cuts applied)
    
    
#     Extra_Part_of_Name = "_GitHub_Electron_Refinement_V3"
#     # Added new (extended) Electron Momentum Corrections (Kinematic Coverage is: 0.95-9.95 GeV)
#     # Not running Electron Only Correction (i.e., 'mmF') for the Single Pion Channel (may run it later during the refinement of the pion corrections)
    
    
#     Extra_Part_of_Name = "_GitHub_Electron_Refinement_V4"
#     # Updated Missing Mass histograms so that their momentum ranges are always from p = 0-12 GeV (does not depend on the plotted particle anymore)
#     # Refined Electron Corrections based on Extra_Part_of_Name = "_GitHub_Electron_Refinement_V3"
#         # (Kinematic Coverage changed to: 1.45-9.95 GeV)
#     # Running the pi+ pion corrections again
    
    
#     Extra_Part_of_Name = "_GitHub_Electron_Refinement_V5"
#     # Doubled the number of bins in the ∆P plots (both in x and y binning for the electron corrections, just in the y binning for all others)
#         # Changed the range of the electron momentum plotted in the ∆P histograms from 0-12 GeV (with 120 bins total) to the new dimensions of 0.5-10.5 GeV with 400 bins total (bin size is 0.025 GeV/bin)
#     # Added the Correction options where only the electron is corrected to the SP channel
#     # No new corrections since "_GitHub_Electron_Refinement_V4"
    
    
#     Extra_Part_of_Name = "_GitHub_Electron_Refinement_V6"
#     # Refined the Electron Corrections based on the new fits of the uncorrected ∆P plots

    
    
#     Extra_Part_of_Name = "_GitHub_Pion_Refinement_V1"
#     # Created new Pion Corrections using the new electron corrections (and fit methods)
#     # Minor issue noticed: there seems to be some print funtion which outputs empty lines during the running of this code - this should not effect the histograms, but is an oddity that I would like to fix (this was not noticed ever before)
    
#     Extra_Part_of_Name = "_GitHub_Pion_Refinement_V2"
#     # Refined the Pion Corrections from "GitHub_Pion_Refinement_V1"
#     # Fixed an issue with 'pass_version' being used with Fall2018 data (code check for pass_version != "NS" instead of pass_version != "NA")
    
#     Extra_Part_of_Name = "_GitHub_Pion_Refinement_V3"
#     # Refined the Pion Corrections from "GitHub_Pion_Refinement_V1" ("GitHub_Pion_Refinement_V2" refinements were accidentally applied to the electron instead of the pion)
#     # Set the initial beam energies used throughout the code at the beginning (based on file input) to avoid issues when loading other (i.e., Spring 2019) datasets
#     # Fixed the minor note mentioned for "GitHub_Pion_Refinement_V1"
    
#     Extra_Part_of_Name = "_GitHub_Pion_Refinement_V4"
#     # Refined the Pion Corrections from "GitHub_Pion_Refinement_V3"
    
    
#     Extra_Part_of_Name = "_GitHub_Proton_Refinement_V1"
#     # Starting the proton corrections
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V2"
    # New proton corrections (compatible with Elastic Corrections) - Quadratic but not phi dependent 
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V3"
    # New proton corrections added
        # More complex correction uses 2 quadratic equation
    # Ran more versions of the corrections which turned off the Energy Loss Corrections
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V4"
    # New proton corrections added
        # More complex correction uses a combination of a quadratic and then a linear equation
            # The correction added used the Energy Loss corrections when being created
            # These are the only proton (momentum) corrections that are applied in this file
    # The (new) corrections from "_GitHub_Proton_Refinement_V3" were not run again (did not work well)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V5"
    # New proton corrections added
        # Modified/replaced existing corrections to check how the number/size of momentum bins effects the corrections (updated the 'complex' corrections as well as the 'regular' quadratic corrections)
        
        
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V6"
    # Refined the Proton Corrections by limiting the contributions of the Pi0 channel
    # No longer plotting Pi- histograms (only electron, proton, and Pi+)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V7"
    # Refined the Proton Corrections (again)
    
    Extra_Part_of_Name = "_GitHub_Cut_Check_V1"
    # Running Missing Mass histograms WITH exclusivities cuts (investigating why the corrections are not working)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V8"
    # Refined the Proton Corrections (again)
    # Reset the exclusivity cuts to only run for the proper histograms
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V9"
    # Refined the Proton Corrections (again)
        # No Pi0 Contributions to the proton corrections
        
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V10"
    # Refined the Proton Corrections (Just the Quad+Linear and 'refined' Quad)
        # No Pi0 Contributions to the proton corrections
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V11"
    # Refined the Proton Corrections (All versions with 'REF' now including another double quadratic refinement)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V12"
    # Refined the Proton Corrections (New/Refined corrections to replace/improve those from V11)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V13"
    # Refined the Proton Corrections ("LEF" Corrections refined with normal quadratic OR linear corrections - depending on sector)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V14"
    # New the Proton Corrections (New versions of "LEF" and "QEF" that use 0.05 GeV Momentum slices of ∆P below p = 1 GeV)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V15"
    # Removed some corrections (all proton corrections that are not the quad+linear ones) but adds two new ones
        # New proton corrections are:
            # 1) A refinement of the quad+linear correction where the refinement uses the mean of each gaussian slice is used in their defined range instead of using a continuous function
            # 2) A new proton correction entirely pased on the method described in the above refinement
            
            
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V16"
    # Refined the sliced corrections
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V17"
    # Needed to fix the refinements from the last version
    # Changed the binning of the Missing Mass Squared plots (from 160 to 200 in the range of -0.5 to 0.5)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V18"
    # Changed the binning of the Missing Mass Squared plots (from 200 to 310 in the range of -0.3175 to 0.3025)
    # Removed plots which use different particle momentums and sectors
    # Checking Missing Mass Plots with exclusivity cuts
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V19"
    # Changed the binning of the Missing Mass Squared plots (from 310 to 320 in the range of -0.3275 to 0.3125 - Same size but the range is increased to make the bins easier to change while fitting)
    # Added alternative calculation of ∆P histograms
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V20"
    # Removed the alternative calculation of ∆P histograms but added the ∆P vs uncorrected proton momentum (i.e., without the energy loss correction - will be incompatible with current order that the proton corrections are applied)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V21"
    # New Proton Correction Refinement (Sliced)
    # Added Integrated Sector ∆P histograms
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V22"
    # New Proton Correction that uses slices WITHOUT the Energy Loss corrections
    # Updated the corNameTitles function so that histograms are made with the corrections already in multiple lines for each particle
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V23"
    # Added new type of exclusivity cut (simple cut on the MM2 < 0.2 and MM2 > -0.2)
        # Past cuts were too tight/baised higher missing mass at low momentum
    # No longer running invariant mass histograms (was not using them)
    # Removed the Proton Correction that used slices WITHOUT the Energy Loss corrections (i.e., the one added in the previous version)
        # Was not necessary (the problem with the corrections was not the order of the Energy Loss/Momentum corrections were applied)
    
    
    
    if(event_type == "MC"):
        Extra_Part_of_Name = "_GitHub_MC_Test_V1"
        # Testing the momentum corrections using Monte Carlo files (for use in SIDIS analysis)
        # Runs the same as event_type == "SP"
        
    if(pass_version not in ["NA", ""]):
        Extra_Part_of_Name = "".join(["_GitHub_Spring_2019_Pass_", "1" if("Pass 1" in pass_version) else "2", "_V1"])
        # Testing Spring 2019 data with pass 1 and pass 2 files
        
        Extra_Part_of_Name = "".join(["_GitHub_Spring_2019_Pass_", "1" if("Pass 1" in pass_version) else "2", "_V2"])
        # Update file locations to take in events from different file skims (MissingNeutron files instead of the nSidis files)
        # Removed "Extended" Electron Corrections (i.e., the refinements of the original corrections from the last collaboration meeting)
        
        Extra_Part_of_Name = "".join(["_GitHub_Spring_2019_Pass_", "1" if("Pass 1" in pass_version) else "2", "_V3"])
        # Fixed initial beam energies (was still using energy from Fall 2018 instead of from Spring 2019)
        # File locations take events from MissingNeutron files instead of the nSidis files (want to switch back to nSidis)
        
    if("Central" in pass_version):
        Extra_Part_of_Name = "".join(["_GitHub_Spring_2019_Pass_", "1" if("Pass 1" in pass_version) else "2", "_V3" if("Central" not in pass_version) else "_Central_V1"])
        # No changes to regular Spring 2019 files (as of V3 above), but added the option to plot using only central detector pions
        # Added option to include "C" in the 3rd arguement of this code's input in order to switch from the Forward dectector to the central detector
        
    
    
    
    if(event_type != "MC"):
        if(event_type != "P0"):
            if(Delta_P_histo_Q != 'y'):
                OutputFileName = "".join([event_Name.replace(" ", "_"), "_", str(MM_type), "_", str(datatype), "_No_Dp", Extra_Part_of_Name, "_File_", str(file_name), ".root"])
            else:
                OutputFileName = "".join([event_Name.replace(" ", "_"), "_", str(MM_type), "_", str(datatype), "_With_Dp", Extra_Part_of_Name, "_File_", str(file_name), ".root"])
        else:
            if(Delta_P_histo_Q != 'y'):
                OutputFileName = "".join([event_Name.replace(" ", "_"), "_", str(MM_type), "_", str(datatype), "_No_Dp", Extra_Part_of_Name, ".root"])
            else:
                OutputFileName = "".join([event_Name.replace(" ", "_"), "_", str(MM_type), "_", str(datatype), "_With_Dp", Extra_Part_of_Name, ".root"])
    else:
        if(Delta_P_histo_Q != 'y'):
            OutputFileName = "".join(["Simulated_", event_Name.replace(" ", "_"), "_", str(MM_type), "_", str(datatype), "_No_Dp", Extra_Part_of_Name, "_File_", str(file_name), ".root"])
        else:
            OutputFileName = "".join(["Simulated_", event_Name.replace(" ", "_"), "_", str(MM_type), "_", str(datatype), "_With_Dp", Extra_Part_of_Name, "_File_", str(file_name), ".root"])
            

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
            elif("Central" in pass_version):
                if("Pass 1" in pass_version):
                    running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Central_Tracking/Pass1/Inbending/ePip.Central.pass1.inb.qa.nSidis_00*"
                else:
                    running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Central_Tracking/Pass2/Inbending/ePip.Central.pass2.inb.qa.nSidis_00*"
            else:
                if("Pass 1" in pass_version):
                    running_code_with_these_files = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Spring2019/Pass1/Inbending_nSidis/ePip.pass1.inb.qa.nSidis_00*"
                    # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Spring2019/Pass1/Inbending/ePip.pass1.inb.qa.MissingNeutron_00*"
                else:
                    running_code_with_these_files = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Spring2019/Pass2/Inbending_nSidis/ePip.pass2.inb.qa.nSidis_00*"
                    # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Spring2019/Pass2/Inbending/ePip.pass2.inb.qa.MissingNeutron_00*"
                        
        if(event_type == "DP"):
            if(datatype == "Inbending"):
                # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/inb/epPipPim.inb.qa.nSidis_005*"
                running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Double_Pion_Channel_eppippim/Inbending_skim4/epPipPim.inb.qa.skim4_00*"
            else:
                # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/outb/epPipPim.outb.qa.nSidis_005*"
                running_code_with_these_files = "/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Double_Pion_Channel_eppippim/Outbending_skim4/epPipPim.outb.qa.skim4_00*"
                
            # running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Double_Pion_Channel_eppippim/", str(datatype), "/epPipPim.", "out" if("Out" in str(datatype)) else "in", "b.qa.nSidis_005*"])
                
        if(event_type == "P0"):
            if(datatype == "Inbending"):
                running_code_with_these_files = "/lustre19/expphy/volatile/clas12/kenjo/lvl2_eppi0.inb.qa.eloss.exclusiveselection.root"
                running_code_with_these_files = "/u/home/richcap/lvl2_eppi0.inb.qa.eloss.exclusiveselection.root"
                running_code_with_these_files = "/u/home/richcap/lvl2_eppi0.inb.qa.exclusiveselection.root"
            else:
                running_code_with_these_files = "/u/home/richcap/lvl2_eppi0.outb.qa.eloss.exclusiveselection.root"
                running_code_with_these_files = "/u/home/richcap/lvl2_eppi0.outb.qa.exclusiveselection.root"
                
        if(event_type == "ES"):
            # running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/", str(datatype), "/*.root"])
            # running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/", str(datatype), "/eP_Elastic_with_CDpro*.root"])
            running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/", str(datatype), "/eP_Elastic_with_CDpro_New*.root"])
            running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/Valerii_Files/eP_Elastic_with_CDpro_New", ".inb" if("In" in str(datatype)) else ".outb", "*root"])
            running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/Valerii_Files/eP_Elastic_with_CDpro", ".inb" if("In" in str(datatype)) else ".outb", "*root"])
            
        if(event_type == "EO"):
            running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Only_Electron_Channel/electron_only", ".inb" if("In" in str(datatype)) else ".outb", "*root"])

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
        auto Proton_Mass = 0.938;
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
        if("prox" not in rdf.GetColumnNames() and "px" in rdf.GetColumnNames()):
            rdf = rdf.Define("prox", "px")
        if("proy" not in rdf.GetColumnNames() and "py" in rdf.GetColumnNames()):
            rdf = rdf.Define("proy", "py")
        if("proz" not in rdf.GetColumnNames() and "pz" in rdf.GetColumnNames()):
            rdf = rdf.Define("proz", "pz")
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
            dE_loss = exp(-2.739 - 3.932*pro) + 0.002907;
        }
        if(proth > 27){
            dE_loss = exp(-1.2 - 4.228*pro) + 0.007502;
        }
        
        
        """ if("In" in datatype) else """
        
        // Outbending Energy Loss Correction //
        if(proth > 27){
            dE_loss = exp(-1.871 - 3.063*pro) + 0.007517;
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
        ##=====##    Momentum Magnitude    ##=====##
        rdf = rdf.Define("el", "sqrt(ex*ex + ey*ey + ez*ez)")
        ##=====##       Polar Angles       ##=====##
        rdf = rdf.Define("elth", "atan2(sqrt(ex*ex + ey*ey), ez)*(180/3.1415926)")
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
        if(event_type not in ["SP", "MC"]):
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
    #----------#      Last updated on: 1-15-2022      #----------#
    ##############################################################

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
                
            // corPip ==> Gives the 'generation' of the π+ Pion correction
                // corPip == 0 --> No Correction
                // corPip == 1 --> Old Version of Corrections
                // corPip == 2 --> Final Version of Corrections

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
                
                
                if(corPip == 2){
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
                    }
                }
                
                if(corPro == 8){ // Correction based on each momentum slice (without energy loss corrections)
                    if(sec == 1){
                        if(0.45 < pp && pp < 0.5){
                            dp = (0.01123);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.013562);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.013624);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.014539);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.02);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.02);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.012263);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.014836);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.02);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.02);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.02);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.02);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (0.0015552);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (3.5744e-04);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (-0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-0.0038939);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (0.01);
                        }
                    }
                    if(sec == 2){
                        if(0.45 < pp && pp < 0.5){
                            dp = (0.012351);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.013734);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.015132);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.013902);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.01307);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.012338);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.01);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.010163);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.01);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.0040067);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.01);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.0029197);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (0.010893);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (-0.0020681);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-0.012299);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (0.01);
                        }
                    }
                    if(sec == 3){
                        if(0.45 < pp && pp < 0.5){
                            dp = (0.011883);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.012983);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.012554);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.01);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.01);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.010972);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.014404);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.017351);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.017659);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.017966);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.01);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.0083356);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (0.006261);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (0.01);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (0.01);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (4.1173e-09);
                        }
                    }
                    if(sec == 4){
                        if(0.45 < pp && pp < 0.5){
                            dp = (0.012693);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.010836);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.01);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.01);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.010733);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.012659);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.014119);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.02);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.02);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.02);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.02);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.02);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (-7.4841e-09);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (-0.0095873);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (0.0084045);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (0.01);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (9.6902e-09);
                        }
                    }
                    if(sec == 5){
                        if(0.45 < pp && pp < 0.5){
                            dp = (0.011873);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.011523);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.01254);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.013227);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.011882);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.010248);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.012743);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.02);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.02);
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
                            dp = (2.0017e-04);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (-0.0038707);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (-0.0075556);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-0.0051937);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (-0.0070312);
                        }
                    }
                    if(sec == 6){
                        if(0.45 < pp && pp < 0.5){
                            dp = (0.01265);
                        }
                        if(0.5 < pp && pp < 0.55){
                            dp = (0.014984);
                        }
                        if(0.55 < pp && pp < 0.6){
                            dp = (0.015205);
                        }
                        if(0.6 < pp && pp < 0.65){
                            dp = (0.014542);
                        }
                        if(0.65 < pp && pp < 0.7){
                            dp = (0.01474);
                        }
                        if(0.7 < pp && pp < 0.75){
                            dp = (0.016186);
                        }
                        if(0.75 < pp && pp < 0.8){
                            dp = (0.013448);
                        }
                        if(0.8 < pp && pp < 0.85){
                            dp = (0.011864);
                        }
                        if(0.85 < pp && pp < 0.9){
                            dp = (0.017077);
                        }
                        if(0.9 < pp && pp < 0.95){
                            dp = (0.02);
                        }
                        if(0.95 < pp && pp < 1.0){
                            dp = (0.017459);
                        }
                        if(1.0 < pp && pp < 1.25){
                            dp = (0.0083508);
                        }
                        if(1.25 < pp && pp < 1.5){
                            dp = (1.3371e-07);
                        }
                        if(1.5 < pp && pp < 1.75){
                            dp = (0.0087474);
                        }
                        if(1.75 < pp && pp < 2.0){
                            dp = (0.005);
                        }
                        if(2.0 < pp && pp < 2.25){
                            dp = (-0.02);
                        }
                        if(2.25 < pp && pp < 2.75){
                            dp = (-0.0068833);
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
    #----------#     Last updated on: 8-13-2022     #----------#
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
                // corEl == 1 --> Final Version of Corrections

            // corPip ==> Gives the 'generation' of the π+ Pion correction
                // corPip == 0 --> No Correction
                // corPip == 1 --> Final Version of Corrections


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
            // After this line, the angular distribution will approximately go from 0 to 360˚
            if((sec == 4 && Phi < 0) || (sec > 4 && Phi < 90)){
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

        return coutN

    # // corPip ==> Gives the 'generation' of the π+ Pion correction
    #     // corPip == 0 --> No Correction
    #     // corPip == 1 --> Quad Momentum, Quad Phi (Old Version)
    #     // corPip == 2 --> Quad Momentum, Quad Phi (Final Version)
    def NamePipCor(corPip, datatype):
        coutN = 0
        if("Pip" not in corPip):
            coutN = 0
        else:
            if("PipMMEF" in corPip):
                coutN = 2                
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
        elif("MMpro_REF" in corPro):
            coutN = 5
        elif("MMpro_S_LEF" in corPro):
            coutN = 6
        elif("MMpro_SEF" in corPro):
            coutN = 7
        elif("MMpro_SE_NoELC" in corPro):
            coutN = 8
        else:
            coutN = 1
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
        corEl_Num  = str(NameElCor(Correction, Data_Type))
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
    auto fe = dppC(ex, ey, ez, esec, 0, """, str(corEl_Num), """, """, str(corPip_Num), """, """, str(corPim_Num), """, """, str(corPro_Num), """) + 1;
    auto eleC = ROOT::Math::PxPyPzMVector(ex*fe, ey*fe, ez*fe, 0);
        """])

        if("P0" not in Channel_Type and "E" not in Channel_Type and ("Mom_el" not in Out_Type and "Mom_pim" not in Out_Type and "Mom_pro" not in Out_Type)):
            Particles_for_Correction = "".join([Particles_for_Correction, """
    auto fpip = dppC(pipx, pipy, pipz, pipsec, 1, """, str(corEl_Num), """, """, str(corPip_Num), """, """, str(corPim_Num), """, """, str(corPro_Num), """) + 1;
    auto pipC = ROOT::Math::PxPyPzMVector(pipx*fpip, pipy*fpip, pipz*fpip, 0.13957);
        """])

        if("DP" in Channel_Type and "E" not in Channel_Type and ("Mom_el" not in Out_Type and "Mom_pip" not in Out_Type and "Mom_pro" not in Out_Type)):
            Particles_for_Correction = "".join([Particles_for_Correction, """
    auto fpim = dppC(pimx, pimy, pimz, pimsec, 2, """, str(corEl_Num), """, """, str(corPip_Num), """, """, str(corPim_Num), """, """, str(corPro_Num), """) + 1;
    auto pimC = ROOT::Math::PxPyPzMVector(pimx*fpim, pimy*fpim, pimz*fpim, 0.13957);
        """])


        if("SP" not in Channel_Type and "MC" not in Channel_Type and "EO" not in Channel_Type and ("Mom_el" not in Out_Type and "Mom_pip" not in Out_Type and "Mom_pim" not in Out_Type)):
            if("_NoELC" not in Correction):

                Particles_for_Correction = "".join(["""
            """, Particles_for_Correction, """
    auto fpro = dppC(prox_cor, proy_cor, proz_cor, prosec, 3, """, str(corEl_Num), """, """, str(corPip_Num), """, """, str(corPim_Num), """, """, str(corPro_Num), """) + 1;
    auto proC = ROOT::Math::PxPyPzMVector(prox_cor*fpro, proy_cor*fpro, proz_cor*fpro, 0.938);
            """])

            else: # If "_NoELC" is in 'Correction', then the proton energy loss correction is not applied

                Particles_for_Correction = "".join(["""

            """, Particles_for_Correction, """
    auto fpro = dppC(prox, proy, proz, prosec, 3, """, str(corEl_Num), """, """, str(corPip_Num), """, """, str(corPim_Num), """, """, str(corPro_Num), """) + 1;
    auto proC = ROOT::Math::PxPyPzMVector(prox*fpro, proy*fpro, proz*fpro, 0.938);
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

            if('eppipX' == MM_Type and Channel_Type == "DP"):
                Calculation_Code_Choice = """
    auto Output_Vectors = beam + targ - eleC - pipC - proC;

    auto Final_Output = Output_Vectors.M2();

                """

            if('eppimX' == MM_Type and Channel_Type == "DP"):
                Calculation_Code_Choice = """
    auto Output_Vectors = beam + targ - eleC - pimC - proC;

    auto Final_Output = Output_Vectors.M2();

                """

            if('epippimX' == MM_Type and Channel_Type == "DP"):
                Calculation_Code_Choice = """
    auto Output_Vectors = beam + targ - eleC - pipC - pimC;

    auto Final_Output = Output_Vectors.M();

                """

            if('epX' == MM_Type and Channel_Type == "DP"):
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
                Calculation_Code_Choice = """
    double neutronM2 = 0.9396*0.9396;
                """
                if("D_pip" in Out_Type):
                    ##================================================================================================##
                    ##=====================##         ∆P (Single Pion - π+) Calculations         ##===================##
                    ##================================================================================================##
                    Calculation_Code_Choice = "".join([Calculation_Code_Choice, """

    // Below are the kinematic calculations of the π+ momentum (from el+pro->el+Pip+N) based on the assumption that the π+ angle and electron reconstruction were measured by the detector correctly for exclusive events in the epipX channel
    // (The neutron is used as the "missing" particle)

    auto termA = (neutronM2 - (0.938*0.938) - (0.13957*0.13957))/2;
    auto termB = 0.938*(Beam_Energy - eleC.P()) - Beam_Energy*eleC.P()*(1 - cos(eleC.Theta()));
    auto termC = ((eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, pipC))) - (Beam_Energy*cos(pipC.Theta())));

    auto sqrtTerm = ((termA - termB)*(termA - termB)) + (0.13957*0.13957)*((termC*termC) - ((0.938 + Beam_Energy - eleC.P())*(0.938 + Beam_Energy - eleC.P())));
    auto denominator = ((0.938 + Beam_Energy - eleC.P()) + termC)*((0.938 + Beam_Energy - eleC.P()) - termC);
    auto numeratorP = (termA - termB)*termC + (0.938 + Beam_Energy - eleC.P())*sqrt(sqrtTerm);
    auto numeratorM = (termA - termB)*termC - (0.938 + Beam_Energy - eleC.P())*sqrt(sqrtTerm);

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

    // Below are the kinematic calculations of the electron momentum (from el+pro->el+Pip+N) based on the assumption that the electron angle and π+ reconstruction were measured by the detector correctly for exclusive events in the epipX channel
    // (The neutron is used as the "missing" particle)

    auto termA = ((neutronM2 - (0.938*0.938) - (0.13957*0.13957))/2) - 0.938*Beam_Energy;
        // termA --> (("Neutron Mass Squared" - "Proton Mass Squared" - "π+ Mass Squared")/2) - "Proton Mass"*"Initial Electron Beam Energy"

    auto termB = pipC.E() - pipC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, pipC)) - Beam_Energy*(1 - cos(eleC.Theta())) - 0.938;
        // termB --> "π+ Energy" - "π+ Momentum"*cos("Angle between Electron and π+") - "Initial Electron Beam Energy"*(1 - cos("Electron Theta")) - "Proton Mass"

    auto termC = Beam_Energy*(pipC.E() - pipC.P()*cos(pipC.Theta())) + 0.938*pipC.E();
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

    // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pip+pim) based on the assumption that the proton angle and electron/π+ reconstruction were measured by the detector correctly for exclusive events in the ep->epπ+π- channel 
    // (π- is used as a "missing" particle)

    auto termA1 = pipC.E() + eleC.P() - Beam_Energy - (0.938);
    // termA1 = "π+ Energy" + "Electron Momentum" - "Initial Beam Energy" - "Proton Mass"

    auto termB1 = Beam_Energy*cos(proC.Theta()) - eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC)) - pipC.P()*cos(ROOT::Math::VectorUtil::Angle(pipC, proC));
    // termB1 = "Initial Beam Energy"*cos("Proton Theta Angle") - "Electron Momentum" * cos("Angle between the Proton and Electron") - "π+ Momentum" * cos("Angle between the Proton and π+")

    auto termC1 = (0.938)*(Beam_Energy - eleC.P() - pipC.E() + (0.938)) - Beam_Energy*(eleC.P()*(1 - cos(eleC.Theta())) + (pipC.E() - pipC.P()*cos(pipC.Theta()))) + eleC.P()*(pipC.E() - pipC.P()*cos(ROOT::Math::VectorUtil::Angle(pipC, eleC)));
    // termC1 = "Proton Mass"*("Initial Beam Energy" - "Electron Momentum" - "π+ Energy" + "Proton Mass") - "Initial Beam Energy" * ("Electron Momentum" * (1 - cos("Electron Angle")) + ("π+ Energy" - "π+ Momentum" * cos("π+ Angle"))) + "Electron Momentum" * ("π+ Energy" - "π+ Momentum" * cos("Angle between the π+ and Electron"))

    auto termA2 = (termA1*termA1 - termB1*termB1);
    auto termB2 = -2*termB1*termC1;
    auto termC2 = termA1*termA1*(0.938)*(0.938) - termC1*termC1;

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
    
    // auto beam_test      = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
    // auto targ_test      = ROOT::Math::PxPyPzMVector(0, 0, 0, 0.938);
    // 
    // auto cor_Factor     = ((Final_Output)/proC.P()) + 1;
    // auto cor_FactorM    = ((pro_CalculateM - proC.P())/proC.P()) + 1;
    // auto cor_FactorP    = ((pro_CalculateP - proC.P())/proC.P()) + 1;
    // 
    // // auto cor_Factor     = ((pro_Calculate  - pro_cor)/pro_cor);
    // // auto cor_FactorM    = ((pro_CalculateM - pro_cor)/pro_cor);
    // // auto cor_FactorP    = ((pro_CalculateP - pro_cor)/pro_cor);
    // 
    // auto pro_OG         = ROOT::Math::PxPyPzMVector(prox_cor, proy_cor, proz_cor, 0.938);
    // 
    // auto proC_Calc      = ROOT::Math::PxPyPzMVector(proC.Px()*cor_Factor,  proC.Py()*cor_Factor,  proC.Pz()*cor_Factor,  0.938);
    // auto proC_Calc_M    = ROOT::Math::PxPyPzMVector(proC.Px()*cor_FactorM, proC.Py()*cor_FactorM, proC.Pz()*cor_FactorM, 0.938);
    // auto proC_Calc_P    = ROOT::Math::PxPyPzMVector(proC.Px()*cor_FactorP, proC.Py()*cor_FactorP, proC.Pz()*cor_FactorP, 0.938);
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
    //     std::cout<<"Proton Correction = """, str(Correction), """"<<std::endl;
    //     std::cout<<"Sector = "<<prosec<<std::endl;
    //     std::cout<<"Missing Mass Ideal                   = "<<(0.13957039*0.13957039)<<std::endl;
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
                    Calculation_Code_Choice = """

    // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pip+pim) based on the assumption that the proton angle and electron/π+ reconstruction were measured by the detector correctly for exclusive events in the ep->epπ+π- channel 
    // (π- is used as a "missing" particle)

    auto termA1 = pipC.E() + eleC.P() - Beam_Energy - (0.938);
    // termA1 = "π+ Energy" + "Electron Momentum" - "Initial Beam Energy" - "Proton Mass"

    auto termB1 = Beam_Energy*cos(proC.Theta()) - eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC)) - pipC.P()*cos(ROOT::Math::VectorUtil::Angle(pipC, proC));
    // termB1 = "Initial Beam Energy"*cos("Proton Theta Angle") - "Electron Momentum" * cos("Angle between the Proton and Electron") - "π+ Momentum" * cos("Angle between the Proton and π+")

    auto termC1 = (0.938)*(Beam_Energy - eleC.P() - pipC.E() + (0.938)) - Beam_Energy*(eleC.P()*(1 - cos(eleC.Theta())) + (pipC.E() - pipC.P()*cos(pipC.Theta()))) + eleC.P()*(pipC.E() - pipC.P()*cos(ROOT::Math::VectorUtil::Angle(pipC, eleC)));
    // termC1 = "Proton Mass"*("Initial Beam Energy" - "Electron Momentum" - "π+ Energy" + "Proton Mass") - "Initial Beam Energy" * ("Electron Momentum" * (1 - cos("Electron Angle")) + ("π+ Energy" - "π+ Momentum" * cos("π+ Angle"))) + "Electron Momentum" * ("π+ Energy" - "π+ Momentum" * cos("Angle between the π+ and Electron"))

    auto termA2 = (termA1*termA1 - termB1*termB1);
    auto termB2 = -2*termB1*termC1;
    auto termC2 = termA1*termA1*(0.938)*(0.938) - termC1*termC1;

    auto pro_CalculateP = (-termB2 + sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);
    auto pro_CalculateM = (-termB2 - sqrt(termB2*termB2 - 4*termA2*termC2)) / (2*termA2);

    auto pro_Calculate = pro_CalculateP;

    if(abs(proC.P() - pro_CalculateP) <= abs(proC.P() - pro_CalculateM)){
        pro_Calculate = pro_CalculateM;
    }
    else{
        pro_Calculate = pro_CalculateP;
    }

    auto Final_Output = pro_Calculate - proC.P();
    
    
                        """



    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



            ##=========================================================##
            ##===============||-----------------------||===============##
            ##===============||    π0 Pion Channel    ||===============##
            ##===============||-----------------------||===============##
            ##=========================================================## 
            if(Channel_Type == "P0"):
                if("D_pro" in Out_Type):
                    ##=====================================================================================================##
                    ##=====================##         ∆P (π0 Pion Channel - Pro) Calculations         ##===================##
                    ##=====================================================================================================##
                    Calculation_Code_Choice = """

    double pi0M2term = (0.13498*0.13498)/2;


    // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pi0) based on the assumption that the proton angle and electron reconstruction were measured by the detector correctly for exclusive events in the ep->epπ0 channel
    // (π0 is used as the "missing" particle)


    auto termA1 = pi0M2term - (0.938)*((Beam_Energy) - eleC.P() + (0.938)) + (Beam_Energy)*eleC.P()*(1 - cos(eleC.Theta()));
        // termA1 = pi0M2term - "Proton Mass"*("Initial Beam Energy" - "Electron Momentum" + "Proton Mass") + "Initial Beam Energy"*"Electron Momentum"*(1 - cos("Electron Theta Angle"))

    auto termB1 = (Beam_Energy)*cos(proC.Theta()) - eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC,proC));
        // termB1 = "Initial Beam Energy"*cos("Proton Theta Angle") - "Electron Momentum"*cos("Angle between the Proton and Electron")

    auto termC1 = eleC.P() - (Beam_Energy) - (0.938);
        // termC1 = "Electron Momentum" - "Initial Beam Energy" - "Proton Mass"

    auto termA2 = (termB1*termB1 - termC1*termC1);
    auto termB2 = -2*termB1*termA1;
    auto termC2 = termA1*termA1 - termC1*termC1*(0.938)*(0.938);

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

                        """



                if("D_pel" in Out_Type):
                    ##==========================================================================================================##
                    ##=====================##         ∆P (π0 Pion Channel - Electron) Calculations         ##===================##
                    ##==========================================================================================================##
                    Calculation_Code_Choice = """

    // Below are the kinematic calculations of the electron momentum (from el+pro->el+pro+pi0) based on the assumption that the electron angle and proton reconstruction were measured by the detector correctly for exclusive events in the epπ0 channel
    // (π0 is used as the "missing" particle)


    auto termA = (0.13498*0.13498)/2;
        // termA --> "(Pi0 Mass Squared)/2"

    auto termB = termA - (0.938)*((Beam_Energy) - proC.E() + (0.938)) + (Beam_Energy)*(proC.E() - proC.P()*cos(proC.Theta()));
        // termB --> "0.5*Pi0 Mass^2" - "Proton Mass" * ("Initial Electron Beam Energy" - "Proton Energy" + "Proton Mass") + "Initial Electron Beam Energy" * ("Proton Energy" - "Proton Momentum"*cos("Proton Theta"))

    auto termC = proC.E() - 0.938 - proC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC)) - Beam_Energy*(1 - cos(eleC.Theta()));
        // termC --> "Proton Energy" - "Proton Mass" - "Proton Momentum"*cos("Angle between Electron and Proton") - "Initial Electron Beam Energy"*(1 - cos("Electron Theta"))

    auto pel_Calculated = termB/termC;

    auto Final_Output = pel_Calculated - eleC.P();

                    """



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
                    Calculation_Code_Choice = """

    // Below are the kinematic calculations of the proton momentum (from el+pro->el'+pro') based on the assumption that the proton angle and electron reconstruction were measured by the detector correctly for elastic events in the ep->e'p' channel

    auto termA1 = 2*eleC.P() - (Beam_Energy);
        // termA1 = 2*"Electron Momentum" - "Initial Beam Energy"

    auto termB1 = eleC.P()*cos(ROOT::Math::VectorUtil::Angle(eleC, proC)) - (Beam_Energy)*cos(proC.Theta());
        // termB1 = "Electron Momentum"*cos("Angle between the Proton and Electron") - "Initial Beam Energy"*cos("Proton Theta Angle")
        
    auto termC1 = 2*(Beam_Energy)*eleC.P()*(1 - cos(eleC.Theta()));
        // termC1 = 2*"Initial Beam Energy"*"Electron Momentum"*(1 - cos("Electron Theta Angle"))


    auto termA2 = (termB1*termB1 - termA1*termA1);
    auto termB2 = 2*termB1*termC1;
    auto termC2 = termC1*termC1 - termA1*termA1*(0.938)*(0.938);

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

                        """


                if("D_pel" in Out_Type):
                    ##=============================================================================================================##
                    ##=====================##         ∆P (Elastic Scattering - Electron) Calculations         ##===================##
                    ##=============================================================================================================##
                    Calculation_Code_Choice = """
                    
    // Below are the kinematic calculations of the electron momentum (from el+pro->el'+pro') based on the assumption that the electron angle was measured by the detector correctly
    
    auto termA = Beam_Energy*(1 - cos(eleC.Theta())) + 0.938;
        // termA --> "Initial Electron Beam Energy"*(1 - cos("Electron Theta")) + "Proton Mass"
        
    auto termB = Beam_Energy*0.938;
        // termB --> "Initial Electron Beam Energy" * "Proton Mass"
        

    auto pel_Calculated = termB/termA;
    
    auto Final_Output = pel_Calculated - eleC.P();
                    """


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

    // Below are the kinematic calculations of the proton angle (theta) (from elastic scattering) 
    // To be used for exclusivity cuts

    auto Pro_Th_Calc = (proC.Theta())*(180/3.1415926); // Initialize the calculated proton angle as the same value as the measured/corrected proton angle (converted to degrees)

    Pro_Th_Calc = atan(0.938/((Beam_Energy + 0.938)*tan(eleC.Theta()/2)))*(180/3.1415926);

    auto Delta_Theta = ((proC.Theta())*(180/3.1415926)) - Pro_Th_Calc;

    auto Final_Output = Delta_Theta;

                    """])
                except Exception as e:
                    print("\nFAILED ∆Theta CALCULATION (Version 1)\n")
                    print("".join(["ERROR: ", str(e)]))
            elif("D_Angle_V2" in Out_Type):
                try:
                    Calculation_Code_Choice = "".join([Calculation_Code_Choice, """

    // Below are the kinematic calculations of the proton angle (theta) (from elastic scattering) 
    // To be used for exclusivity cuts

    auto Pro_Th_Calc = (proC.Theta())*(180/3.1415926); // Initialize the calculated proton angle as the same value as the measured/corrected proton angle (converted to degrees)

    Pro_Th_Calc = acos(((Beam_Energy + 0.938)*(proC.E() - + 0.938))/(Beam_Energy*proC.P()))*(180/3.1415926);

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

    // Below are the kinematic calculations of the proton angle (theta) (from elastic scattering) 
    // To be used for exclusivity cuts

    auto Pro_Th_Calc = (proC.Theta())*(180/3.1415926); // Initialize the calculated proton angle as the same value as the measured/corrected proton angle (converted to degrees)

    auto Calc_P_El = (Beam_Energy*0.938)/((Beam_Energy*(1 - cos(eleC.Theta()))) + 0.938);
    auto Calc_Terms_1 = Beam_Energy*Calc_P_El*(1 - cos(eleC.Theta()));
    
    auto denomintator = Beam_Energy*sqrt(Calc_Terms_1*Calc_Terms_1 - 2*Calc_Terms_1*0.938*0.938);
    auto numerator = (Beam_Energy + 0.938)*(Calc_Terms_1 - 2*0.938*0.938);

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

    // Below are the kinematic calculations of the proton angle (theta) (from elastic scattering) 
    // To be used for exclusivity cuts

    auto Pro_Th_Calc = (proC.Theta())*(180/3.1415926); // Initialize the calculated proton angle as the same value as the measured/corrected proton angle (converted to degrees)

    Pro_Th_Calc = atan(0.938/((Beam_Energy + 0.938)*tan(eleC.Theta()/2)))*(180/3.1415926);

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



        Full_Correction_Output = "".join([Correction_Code, """

    auto Beam_Energy = """, str(Beam_Energy), """;
    // Defined by the run group/data set

    """, "// " if("MM" not in Out_Type and "WM" not in Out_Type) else "", """auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
    """, "// " if("MM" not in Out_Type and "WM" not in Out_Type) else "", """auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, 0.938);
        """, Particles_for_Correction, """
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
                if("D_Angle" in Out_Type):
                    print("".join([color.BOLD, "\n\n\nCut Code: \n", color.END, str(Extra_Cut)]))
                # print("".join([color.BOLD, "\n\n\nCut Code: \n", color.END, str(Extra_Cut)]) if("D_Angle" in Out_Type) else "")
            # if("D_Angle_V4" in Out_Type and Correction == "mm0" and Extra_Cut != ""):
            #     Output.Display(str(Output_Title), 10).Print()
        except Exception as e:
            print("".join([color.RED, color.BOLD, """ERROR: Failed to create the DataFrame Column...\nCode is written as:
            """, color.END, "Output = Data_Frame.Define(", str(Output_Title), ", ", str(Full_Correction_Output), """)
            
            if(Extra_Cut != "none" and Extra_Cut != ""):
                Output = Output.Filter(""", str(Extra_Cut), ")"]))
            
            
            print("".join([color.BLUE, color.BOLD, "\nINPUTS: CorDpp(Data_Frame, ", str(Correction), ", ", str(Out_Type), ", ", str(Channel_Type), ", ", str(MM_Type), ", ", str(Data_Type), ", ", str(Extra_Cut), ")", color.END]))
            print("".join([color.RED, color.BOLD, "ERROR GIVEN: \n", str(e), color.END, "\n\n"]))
            print("".join([color.RED, color.BOLD, "TRACEBACK: \n", str(traceback.format_exc()), color.END, "\n\n"]))
            

        
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

        if('mm0' in CorrectionNameIn):
            CorrectionName1 = 'No El Cor'
        if('mm1' in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Linear - No Phi)'
        if('mmPhi' in CorrectionNameIn):
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
        if('mmF' in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Quad - Quad Phi)'
        if('mmEF' in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Quad - Quad Phi - With Elastic Cors)'
        if('mmExF' in CorrectionNameIn):
            CorrectionName1 = 'El Cor (Quad - Quad Phi - Extended)'
            
        if(event_type in ["EO"]):
            if(CorrectionNameIn == "mm0"):
                CorrectionName = "No Momentum Corrections"
            else:
                CorrectionName = CorrectionName1
            return CorrectionName

        if('Pip' not in CorrectionNameIn):
            CorrectionName2 = 'No Pi+ Cor' if(event_type not in ["P0"]) else ""
        if('Pip' in CorrectionNameIn):
            if('MMQ' in CorrectionNameIn):
                CorrectionName2 = 'Pi+ Cor (Quad - No Phi)'
            if('MMPhi' in CorrectionNameIn):
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
            if('MMF' in CorrectionNameIn):
                CorrectionName2 = 'Pi+ Cor (Quad - Quad Phi)'
            if('MMEF' in CorrectionNameIn):
                CorrectionName2 = 'Pi+ Cor (Quad - Quad Phi - With Elastic Cors)'

        if('Pim' not in CorrectionNameIn):
            CorrectionName3 = 'No Pi- Cor' if(event_type in ["DP"]) else ""
        if('Pim' in CorrectionNameIn):
            if('MMpimPhi' in CorrectionNameIn):
                CorrectionName3 = 'Pi- Cor (Linear - Linear Phi)'
            if('MMpim_qPhi' in CorrectionNameIn):
                CorrectionName3 = 'Pi- Cor (Quad - Quad Phi)'
            if('MMpim_F' in CorrectionNameIn):
                CorrectionName3 = 'Pi- Cor (Quad - Quad Phi - Rounded)'

        if('Pro' not in CorrectionNameIn):
            CorrectionName4 = 'No Pro Cor' if(event_type not in ["SP", "MC"]) else ""
            # if(('_NoELC' not in CorrectionNameIn and event_type == "DP") or (event_type == "P0")):
            if('_NoELC' not in CorrectionNameIn and CorrectionName4 != ""):
                CorrectionName4 = ''.join([CorrectionName4, " (Energy Loss Cor)"])
        if('Pro' in CorrectionNameIn):
            if('MMproPhi' in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Linear - Linear Phi)'
            if("MMpro_qPhi" in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad - Quad Phi)'
            if('MMpro_pi0Phi' in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad - Quad Phi - From Pi0)'
            if('MMpro_pi2Phi' in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad - Quad Phi - From Double Pion)'
            if('MMpro_NoPhi' in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Linear - No Phi)'
            if('MMpro_qNoPhi' in CorrectionNameIn or 'MMpro_F' in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad - No Phi)'
            if('MMpro_EF' in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad - No Phi - With Elastic Cors)'
            if('MMpro_REF' in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad - Refined - With Elastic Cors)'
            if('MMpro_QEF' in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Double Quad - With Elastic Cors)'
            if('MMpro_LEF' in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad+Linear - With Elastic Cors)'
            if('MMpro_S_LEF' in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad+Linear+Slices - With Elastic Cors)'
            if('MMpro_SEF' in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Sliced - With Elastic Cors)'
            if('MMpro_SE_NoELC' in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Sliced - With Elastic Cors - Before Energy Loss)'
            if('_NoELC' not in CorrectionNameIn):
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
            CorrectionName = "".join(["No Momentum Corrections", " (Energy Loss Cor)" if(event_type not in ["SP", "MC"] and "NoELC" not in CorrectionNameIn) else ""])

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
                    PhiFilter = "".join([binName, '>-5 && ', binName, '<5'])
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
                PhiFilter = "".join([binName, '>5 && ', binName, '<15'])
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
            RegList_Out = [['No Phi Bins','regall']]

            if(Bin == '1'):
                RegList_Out = [['No Phi Bins','regall']]
            if(Bin == '3'):
                if(Particle == 'el'):
                    RegList_Out = [[' (-5 < localelPhiS < 5)', 'reg1'], [' (localelPhiS < -5)', 'reg2'], [' (localelPhiS > 5)', 'reg3']]
                else:
                    RegList_Out = [[''.join([' (-10 < local', str(Particle), 'PhiS < 10)']), 'reg1'], [''.join([' (local', str(Particle), 'PhiS < -10)']), 'reg2'], [''.join([' (local', str(Particle), 'PhiS > 10)']), 'reg3']]
            if(Bin == '5'):
                RegList_Out = [[''.join([' (-5 < local', str(Particle), 'PhiS < 5)']),'reg1'], [''.join([' (-15 < local', str(Particle), 'PhiS < -5)']), 'reg2'], [''.join([' (local', str(Particle), 'PhiS < -15)']), 'reg3'], [''.join([' (5 < local', str(Particle), 'PhiS < 15)']), 'reg4'], [''.join([' (local', str(Particle), 'PhiS > 15)']), 'reg5']]


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
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -5 < #phi_{' if(Region == 'reg1') else ' Bin: #phi_{', str(Particle_Formatting), '} < 5' if(Region == 'reg1') else '} < -5' if(Region == 'reg2') else '} > 5'])
            else:
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -10 < #phi_{' if(Region == 'reg1') else ' Bin: #phi_{', str(Particle_Formatting), '} < 10' if(Region == 'reg1') else '} < -10' if(Region == 'reg2') else '} > 10'])

        # 5 Phi Bin Region
        if(Binning == '5'):
            if(Region == 'reg1'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -5 < #phi_{', str(Particle_Formatting), '} < 5'])
            if(Region == 'reg2'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -15 < #phi_{', str(Particle_Formatting), '} < -5'])
            if(Region == 'reg3'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: #phi_{', str(Particle_Formatting), '} < -15'])
            if(Region == 'reg4'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: 5 < #phi_{', str(Particle_Formatting), '} < 15'])
            if(Region == 'reg5'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: #phi_{', str(Particle_Formatting), '} > 15'])



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
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -5 < #phi_{' if(Region == 'reg1') else ' Bin: #phi_{', str(Particle_Formatting), '} < 5' if(Region == 'reg1') else '} < -5' if(Region == 'reg2') else '} > 5'])
            else:
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -10 < #phi_{' if(Region == 'reg1') else ' Bin: #phi_{', str(Particle_Formatting), '} < 10' if(Region == 'reg1') else '} < -10' if(Region == 'reg2') else '} > 10'])

        # 5 Phi Bin Region
        if(Binning == '5'):

            if(Region == 'reg1'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -5 < #phi_{', str(Particle_Formatting), '} < 5'])
            if(Region == 'reg2'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: -15 < #phi_{', str(Particle_Formatting), '} < -5'])
            if(Region == 'reg3'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: #phi_{', str(Particle_Formatting), '} < -15'])
            if(Region == 'reg4'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: 5 < #phi_{', str(Particle_Formatting), '} < 15'])
            if(Region == 'reg5'):
                regionName = ''.join([' for #phi_{', str(Particle_Formatting) , '} Bin: #phi_{', str(Particle_Formatting), '} > 15'])

            
        SecName = 'All Sectors' if(Sector == 0) else ''.join([str(Particle_Formatting) , ' Sector ', str(Sector)])

        CorrrectionName = corNameTitles(Correction, Form="splitline")

        name = (Correction, Sector, '', Binning, Region, Particle_Plot, Particle, Extra_Cut)

                
        start_title = "".join(["#splitline{(", str(datatype), ") MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "} ", str(SecName), "}"])
        if(pass_version not in ["NA", ""]):
            start_title = "".join(["#splitline{", str(start_title), "{", str(pass_version), "}}"])
                
        output_title = "".join([str(start_title), "{Correction:", str(CorrrectionName), "};p_{", str(Particle_Plot_Formatting), "} [GeV];MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}"])
        if(regionName != "" and Extra_Cut != ""):
            output_title = "".join(["#splitline{", str(start_title), "{Correction:", str(CorrrectionName), "}}{", str(regionName), "};p_{", str(Particle_Plot_Formatting), "} [GeV];MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}"])
        if(Extra_Cut != "" and regionName == ""):
            output_title = "".join(["#splitline{", str(start_title), "{Correction:", str(CorrrectionName), "}}{Cut Applied: ", str(Extra_Cut), "};p_{", str(Particle_Plot_Formatting), "} [GeV];MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}"])
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
    Calculated_Exclusive_Cuts_V2, Calculated_Exclusive_Cuts_V3, Calculated_Exclusive_Cuts_V4 = "esec != -2", "esec != -2", "esec != -2"



    ###########################################################################################################################
    ##=======================================================================================================================##
    ##===============##=============##         Exclusivity Cuts (Using MM from eπ+(N))         ##=============##=============##
    ##=======================================================================================================================##
    ###########################################################################################################################
    if(MM_type == "epipX"):
        
        if("In" in datatype):

            Calculated_Exclusive_Cuts = "".join(["""
            
                auto beam = ROOT::Math::PxPyPzMVector(0, 0, """, str(Beam_Energy), """, 0);
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, 0.938);
                auto ele = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, 0.13957);

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
            
        if("Out" in datatype):

            Calculated_Exclusive_Cuts = "".join(["""
            
                auto beam = ROOT::Math::PxPyPzMVector(0, 0, """, str(Beam_Energy), """, 0);
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, 0.938);
                auto ele = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, 0.13957);

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
            Calculated_Exclusive_Cuts_V4 = "".join(["""
                auto beam = ROOT::Math::PxPyPzMVector(0, 0, """, str(Beam_Energy), """, 0);
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, 0.938);
                auto ele = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, 0.13957);
                auto pro0 = ROOT::Math::PxPyPzMVector(prox, proy, proz, 0.938);
                auto MM_Vector = beam + targ - ele - pip0 - pro0;
                auto cut_up = 0.2;
                auto cut_down = -0.2;
                return (MM_Vector.M2() < cut_up && MM_Vector.M2() > cut_down);
            
            """])
            Calculated_Exclusive_Cuts = "".join(["""
                auto beam = ROOT::Math::PxPyPzMVector(0, 0, """, str(Beam_Energy), """, 0);
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, 0.938);
                auto ele = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, 0.13957);
                auto pro0 = ROOT::Math::PxPyPzMVector(prox, proy, proz, 0.938);
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
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, 0.938);
                auto ele = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, 0.13957);
                auto pro0 = ROOT::Math::PxPyPzMVector(prox, proy, proz, 0.938);
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
    if(MM_type == "eppi0X"):

        if("In" in datatype):
            Calculated_Exclusive_Cuts = "".join(["""

                auto beam = ROOT::Math::PxPyPzMVector(0, 0, """, str(Beam_Energy), """, 0);
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, 0.938);
                auto ele = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                auto pro0 = ROOT::Math::PxPyPzMVector(prox, proy, proz, 0.938);

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

                auto beam = ROOT::Math::PxPyPzMVector(0, 0, """, str(Beam_Energy), """, 0);
                auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, 0.938);
                auto ele = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                auto pro0 = ROOT::Math::PxPyPzMVector(prox, proy, proz, 0.938);

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
        Calculated_Exclusive_Cuts = "".join(["""        
        // For Invariant Mass Cut (Determined with the help of Azimuthal Kinematic Cut applied on the invariant mass histogram):
        auto Beam_Energy = """, str(Beam_Energy), """;
        auto Proton_Mass = 0.938;
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
        """])
        Calculated_Exclusive_Cuts_V2 = "".join(["""
        auto Beam_Energy = """, str(Beam_Energy), """;
        auto Proton_Mass = 0.938;
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
    
    if(Calculated_Exclusive_Cuts_V2 != "esec != -2"):
        kinematicCuts.append(Calculated_Exclusive_Cuts_V2)
    if(Calculated_Exclusive_Cuts_V3 != "esec != -2"):
        kinematicCuts.append(Calculated_Exclusive_Cuts_V3)
    if(Calculated_Exclusive_Cuts_V4 != "esec != -2"):
        kinematicCuts.append(Calculated_Exclusive_Cuts_V4)
        
        
    def Cut_Function(Data_Frame, Input_Cut, Output_Type="Default"):
        
        Cut_Title = ""
        if(str(Input_Cut) == str(Calculated_Exclusive_Cuts)):
            Cut_Title = "Calculated Exclusivity Cuts"
        if(str(Input_Cut) == str(Calculated_Exclusive_Cuts_V2)):
            Cut_Title = "Calculated Exclusivity Cuts (Basic)"
        if(str(Input_Cut) == str(Calculated_Exclusive_Cuts_V3)):
            Cut_Title = "Calculated Exclusivity Cuts (Based on Both Angles)"
        if(str(Input_Cut) == str(Calculated_Exclusive_Cuts_V4)):
            Cut_Title = "Missing Mass Squared Cut"
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

            
        if(Output_Type == "Title"):
            return Cut_Title

        Cut_Data_Frame = Data_Frame
        if(Input_Cut not in ["", "none"]):
            try:
                if("Both" == Input_Cut and CutChoice != "none"):
                    Cut_Data_Frame = Cut_Data_Frame.Filter(Calculated_Exclusive_Cuts)
                    Cut_Data_Frame = Cut_Data_Frame.Filter(CutChoice)
                elif("Both_2" == Input_Cut and CutChoice_2 != "" and CutChoice_2 != "none"):
                    Cut_Data_Frame = Cut_Data_Frame.Filter(Calculated_Exclusive_Cuts)
                    Cut_Data_Frame = Cut_Data_Frame.Filter(CutChoice_2)
                elif("Both_3" == Input_Cut and CutChoice != "none" and CutChoice_2 not in ["", "none"]):
                    Cut_Data_Frame = Cut_Data_Frame.Filter(CutChoice)
                    Cut_Data_Frame = Cut_Data_Frame.Filter(CutChoice_2)
                elif("All" == Input_Cut and CutChoice != "none" and CutChoice_2 not in ["", "none"]):
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


    Delta_P_histo_CorList = ['mm0']

    
    
    if(event_type in ["SP", "MC"]):
        if(datatype == "Inbending"):
            # Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_PipMMF']
            # Delta_P_histo_CorList = ['mm0', 'mmF_PipMMF', 'mmExF_PipMMF', 'mmEF_PipMMF']
            # Delta_P_histo_CorList = ['mm0', 'mmF', 'mmEF', 'mmExF', 'mmF_PipMMF', 'mmExF_PipMMF', 'mmEF_PipMMF']
            # Delta_P_histo_CorList = ['mm0', 'mmF', 'mmEF', 'mmF_PipMMF', 'mmEF_PipMMF']
            Delta_P_histo_CorList = ['mm0', 'mmF', 'mmEF', 'mmF_PipMMF', 'mmEF_PipMMF', 'mmEF_PipMMEF']

        if(datatype == "Outbending"):
            Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_PipMMF']
            
        # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        Delta_P_histo_CompareList = ['pi+', 'el']
#         Delta_P_histo_CompareList = ['el']
        # Delta_P_histo_CompareList = ['pi+']
            
            
    if(event_type == "DP"):
        if(datatype == "Inbending"):
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F_NoELC', 'mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_F', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_F']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_F', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_QEF']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_QEF']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_QEF', 'mmEF_PipMMEF_ProMMpro_LEF']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_REF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_REF']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_REF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_REF', 'mmEF_PipMMEF_ProMMpro_LEF', 'mmEF_PipMMEF_ProMMpro_QEF']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_S_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF', 'mmEF_PipMMEF_ProMMpro_S_LEF', 'mmEF_PipMMEF_ProMMpro_SEF']
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_S_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF', 'mmEF_PipMMEF_ProMMpro_S_LEF', 'mmEF_PipMMEF_ProMMpro_SEF']
#             Delta_P_histo_CorList = ['mmEF_PipMMEF_ProMMpro_SEF']
#             Delta_P_histo_CorList = ['mm0']
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
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmF']
            
            
        # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        # Delta_P_histo_CompareList = ['pro', 'el']
        Delta_P_histo_CompareList = ['el']
        
        
        
    if(event_type == "EO"):
        if(datatype == "Inbending"):
            # Delta_P_histo_CorList = ['mm0', 'mmF', 'mmEF', 'mmExF']
            Delta_P_histo_CorList = ['mm0', 'mmF', 'mmEF']
        if(datatype == "Outbending"):
            Delta_P_histo_CorList = ['mm0', 'mmF']
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
        
        
    NumOfExtendedBins = round((extendx_max - extendx_min)/size_of_Dp_Bins)


    # For using ShowBackground() with the slices of the extra 2D histograms
    # SBehQ = 'yes'
    SBehQ = 'no'
    
    
    if('pro' in Delta_P_histo_CompareList):
        # extra_Dp_calc = ["D_p", "D_p_L"]
        extra_Dp_calc = ["D_p", "D_p_No_C"]
    else:
        extra_Dp_calc = ["D_p"]


    # Number of (π+/pro) phi bins
    # NumPhiBins = ['1', '3']
    NumPhiBins = ['1']
    
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

                                            if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
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
        
        # particle_plot_List = ['el', 'pip', 'pro', 'pim']
        particle_plot_List = ['el', 'pip', 'pro']
        
        
    if(event_type == "P0"):
        particleList = ['el', 'pro']
        
        particle_plot_List = ['el', 'pro']

        
    if(event_type == "ES"):
        # particleList = ['el', 'pro']
        # particle_plot_List = ['el', 'pro']
        particleList = ['el']
        particle_plot_List = ['el']
        
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
        if(datatype == "Outbending"):
            correctionList = ['mm0', 'mmF', 'mmF_PipMMF']
            
    if(event_type == "DP"):
        if(datatype == "Inbending"):
            # correctionList = ['mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F_NoELC', 'mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_F', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_F', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF']
            # correctionList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_QEF']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_QEF']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_QEF', 'mmEF_PipMMEF_ProMMpro_LEF']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_REF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_REF']
            # correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_EF_NoELC', 'mmEF_PipMMEF_ProMMpro_REF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_QEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF', 'mmEF_PipMMEF_ProMMpro_REF', 'mmEF_PipMMEF_ProMMpro_LEF', 'mmEF_PipMMEF_ProMMpro_QEF']
            correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_S_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEF_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF', 'mmEF_PipMMEF_ProMMpro_S_LEF', 'mmEF_PipMMEF_ProMMpro_SEF']
#             correctionList = ['mm0_NoELC', 'mmEF_PipMMEF_NoELC', 'mmEF_PipMMEF_ProMMpro_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_S_LEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SEF_NoELC', 'mmEF_PipMMEF_ProMMpro_SE_NoELC', 'mm0', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_LEF', 'mmEF_PipMMEF_ProMMpro_S_LEF', 'mmEF_PipMMEF_ProMMpro_SEF']
#             correctionList = ['mmEF_PipMMEF_ProMMpro_SEF']
#             correctionList = ['mm0']
            
        if(datatype == "Outbending"):
            # correctionList = ['mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F_NoELC', 'mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_F', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_F']
            # correctionList = ['mm0_NoELC', 'mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_F', 'mmEF_PipMMEF', 'mmEF_PipMMEF_ProMMpro_EF']
            correctionList = ['mm0_NoELC', 'mmEF_NoELC', 'mmEF_ProMMpro_LEF_NoELC', 'mm0', 'mmEF', 'mmEF_ProMMpro_LEF']
            
            
            
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
            correctionList = ['mm0', 'mmF']
            
            
    if(event_type == "EO"):
        if(datatype == "Inbending"):
            # correctionList = ['mm0', 'mmF']
            # correctionList = ['mm0', 'mmF', 'mmEF', 'mmExF']
            correctionList = ['mm0', 'mmF', 'mmEF']
        if(datatype == "Outbending"):
            correctionList = ['mm0', 'mmF']




    # binningList = ['1','3','5']
    binningList = ['1', '3']
    # binningList = ['3']
    
    # if("E" in event_type):
    #     binningList = ['1']

    # Sector = 0 refers to all sectors so the code will start by making histograms that do not filter by sector
    # Any number 1-6 will correspond to the sector of that same number (do not go above 6)

    # SecRangeMin, SecRangeMax = 0, 6
    SecRangeAll = [0, 1, 2, 3, 4, 5, 6]

    # SecRangeMin = min(SecRangeAll)
    # SecRangeMax = max(SecRangeAll)
    # StartOfSRR = 0 if(SecRangeMin == 0 and SecRangeMax > 0) else (SecRangeMin - 1)





    ##-------------------------------------------------------##
    ##=====##=====##     Histogram Options     ##=====##=====##
    ##-------------------------------------------------------##
    
    Run_Missing_Mass_Histos = 'yes'
    # Run_Missing_Mass_Histos = 'no'
    
    if("E" in event_type):
        Run_Missing_Mass_Histos = 'no'
    

    # Letting Run_Phase_Space = 'yes' allows for the histograms without the missing mass values to be run
    Run_Phase_Space = 'yes'
    # Run_Phase_Space = 'no'
    
    Skip_Sector_Phase_Space = "yes"
    # Skip_Sector_Phase_Space = "no"


    # This list is for the extra phase space histograms which can be run with or without shifts      
    shiftList = ['', 'S', 'NS']
    shiftList = ['', 'S']
    
    
    # same_particle_P_and_Sec_MM = False  # Will allow for different particle momentum/sector to be plotted in the same histogram (mixes particles)
    same_particle_P_and_Sec_MM = True   # The particle momentum and sector will always be the same with this option


    
    # Run with the Invariant Mass histograms?
    # Letting Run_Invariant_Mass_Histos = 'yes' causes the code to also create histograms for Invariant Mass versus the particle momentum
    # Run_Invariant_Mass_Histos = 'yes'
    Run_Invariant_Mass_Histos = 'no'

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
        print(color.BOLD + color.BLUE + "\nFor the Kinematic histograms..." + color.END)
        print("".join(["Particles to be plotted include: ", str(particle_plot_List)]))
        print("".join(["Particles to be used for sector/phi binning include: ", str(particleList)]))

        print("".join(["Corrections included: ", str(correctionList)]))

        print("These Corrections correspond to the following:")
        cor_num = 1
        for cor_names in correctionList:
            print("".join(["\t", str(cor_num), ") ", str(cor_names), " -> '", corNameTitles(cor_names), "'"]))
            cor_num += 1

        print("".join(["The number of phi bins will include: ", str(binningList)]))

        print("".join(["The sectors to be included are: ", str(SecRangeAll), "\n"]))
        
        if(Run_Missing_Mass_Histos != "yes"):
            print(color.BOLD + "Will NOT be running the Missing Mass histograms." + color.END)
        if(Run_Phase_Space != 'yes'):
            print(color.BOLD + "Will NOT be running the phase space histograms." + color.END)
        elif('y' in Skip_Sector_Phase_Space and (len(SecRangeAll) > 1 and 0 in SecRangeAll)):
            print(color.BOLD + "Running the phase space histograms but NOT with separate sectors (only plots showing all sectors will be included)." + color.END)
        if(Run_Invariant_Mass_Histos != 'yes'):
            print(color.BOLD + "Will NOT be running histograms with Invariant Mass." + color.END)

        if(str(ShowBGq) != 'no'):
            print("".join(["Using ShowBackground()?: ", ShowBGq]))

    else:
        print("\n\033[1mNot running Kinematic Histograms...\033[0m")

    countHisto = 0


    if(Run_Missing_Mass_Histos == "yes"):
        for Cuts in kinematicCuts:
            # if(Cuts in [Calculated_Exclusive_Cuts if("E" not in event_type) else "esec != -2", Calculated_Exclusive_Cuts_V2, Calculated_Exclusive_Cuts_V3, Calculated_Exclusive_Cuts_V4, "Both", "Both_2", "All"]):
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
            if(Cuts in [Calculated_Exclusive_Cuts if("E" in event_type) else "esec != -2", Calculated_Exclusive_Cuts_V2, Calculated_Exclusive_Cuts_V3, Calculated_Exclusive_Cuts_V4, "Both", "Both_2", "All"]):
                continue
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
        TimeToProcess = 720 if("DP" in event_type and file_location != "All") else 747 if("P0" in event_type) else 121.8 if("E" in event_type) else 1081
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
                    if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                        if("L" not in calc_option):
                            Erdf = CorDpp(Erdf, correction, "D_pro", event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                        else:
                            Erdf = CorDpp(Erdf, correction, "D_p_L_pro", event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                            
                            # print("Printing the full list of variables (and their object types) in the DataFrame (Erdf)...")
                            # for ii in range(0, len(Erdf.GetColumnNames()), 1):
                            #     print("".join([str((Erdf.GetColumnNames())[ii]), " ( type -> ", Erdf.GetColumnType(Erdf.GetColumnNames()[ii]), " )"]))
                            # print("".join(["\tTotal length= ", str(len(Erdf.GetColumnNames()))]))
                            
                    if('el' in Delta_P_histo_CompareList and Delta_Pel_histo_Q == 'y'):
                        Erdf = CorDpp(Erdf, correction, "D_pel", event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")

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
                                            else:
                                                sdf = regFilter(Erdf, binning, sec, region, 'S', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", 'pip' if(event_type in ["SP", "MC"]) else 'pro')

                                            if(secEL not in ["all", 0]):
                                                sdf = sdf.Filter("".join(["esec == ", str(secEL)]))


                                            if(binningEL != '1'):
                                                sdf = regFilter(sdf, binningEL, secEL, regionEL, 'S', Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "", 'el')
                                                histoName = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title)
                                            elif("L" in calc_option):
                                                histoName = (correction, '', SecName, binning, region, Cut_Title, "Larger_Dp")
                                            elif("No_C" in calc_option):
                                                histoName = (correction, '', SecName, binning, region, Cut_Title, "No_C")
                                            else:
                                                histoName = (correction, '', SecName, binning, region, Cut_Title)


                                            Title_Line_1 = "".join(["(", str(datatype), ") #Delta p_{Particle} vs p_{Particle}"])
                                            if("L" in calc_option):
                                                Title_Line_1 = "".join(["(", str(datatype), ") Larger #Delta p_{Particle} vs p_{Particle}"])
                                            if("No_C" in calc_option):
                                                Title_Line_1 = "".join(["(", str(datatype), ") #Delta p_{Particle} vs (Uncorrected) p_{Particle}"])
                                                
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


                                            if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                                                Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), Title.replace("Particle", "Pro"), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pro' if("_NoELC" in correction or "No_C" in calc_option) else "pro_cor", ''.join(['D_pro_' if("L" not in calc_option) else 'D_p_L_pro_', str(correction)]))
                                                # if(binningEL == '1'):
                                                #     Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), "".join(["#splitline{" if(Cut_Title != "") else "", "(", str(datatype), ") #Delta p_{pro} vs p_{pro} ", str(SecName), " ", str(correctionNAME), " " ,str(regionName), "".join(["}{Cut Applied: ", str(Cut_Title), "}"]) if(Cut_Title != "") else "", "; ", "p_{pro}" if("_NoELC" in correction) else "Corrected p_{pro}", "; #Delta p_{pro}"]), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pro' if("_NoELC" in correction) else "pro_cor", ''.join(['D_pro_', str(correction)]))
                                                # else:
                                                #     Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), "".join(["#splitline{" if(Cut_Title != "") else "", "#splitline{#splitline{#Delta p_{pro} vs p_{pro} -- ", str(SecName), "}{Correction: ", str(correctionNAME), "}}{Pro: ", str(regionName) + " -- El: ", str(regionNameEL), "".join(["}{Cut Applied: ", str(Cut_Title)]) if(Cut_Title != "") else "", "}; ", "p_{pro}" if("_NoELC" in correction) else "Corrected p_{pro}", "; #Delta p_{pro}"]), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pro' if("_NoELC" in correction) else "pro_cor", ''.join(['D_pro_', str(correction)]))

                                                Delta_P_histo_Count += 1


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
            # if(Cuts in [Calculated_Exclusive_Cuts if("E" not in event_type) else "esec != -2", Calculated_Exclusive_Cuts_V2, Calculated_Exclusive_Cuts_V3, Calculated_Exclusive_Cuts_V4, "Both", "Both_2", "All"]):
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
            if(Cuts in [Calculated_Exclusive_Cuts if("E" in event_type) else "esec != -2", Calculated_Exclusive_Cuts_V2, Calculated_Exclusive_Cuts_V3, Calculated_Exclusive_Cuts_V4, "Both", "Both_2", "All"]):
                continue
                # Do not plot variables with cuts applied to them that are based on themselves
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
                                
                                
                                Title_Mom_The_Line_1 = "".join(["(", str(datatype), ") #theta_{", str(particle_title), "} vs p_{", str(particle_title), "}"])
                                Title_Mom_Phi_Line_1 = "".join(["(", str(datatype), ") p_{", str(particle_title), "} vs #phi_{", str(particle_title), "}", str(shiftTitle(shift))])
                                Title_The_Phi_Line_1 = "".join(["(", str(datatype), ") #theta_{", str(particle_title), "} vs ", str(local_Q), "#phi_{", str(particle_title), "}", str(shiftTitle(shift))])
                
                                if(pass_version not in ["NA", ""]):
                                    Title_Mom_The_Line_1 = "".join(["#splitline{", str(pass_version), "}{", str(Title_Mom_The_Line_1), "}"])
                                    Title_Mom_Phi_Line_1 = "".join(["#splitline{", str(pass_version), "}{", str(Title_Mom_Phi_Line_1), "}"])
                                    Title_The_Phi_Line_1 = "".join(["#splitline{", str(pass_version), "}{", str(Title_The_Phi_Line_1), "}"])
                                
                                Title_Line_2 = ((("".join(["Correction: ", str(root_color.Bold), "{", str(correctionNAME), "}"]).replace("Pi+", "#pi^{+}")).replace("Pi-", "#pi^{-}")).replace("Phi", "#phi"))
                                Title_Line_3 = "".join(["Cut Applied: ", str(Cut_Title) if(str(Cut_Title) != "") else "No Additional Cuts"])
                                
                                Title_Mom_The_Axis = "".join(["; p_{", str(particle_title), "}; #theta_{", str(particle_title), "}"])
                                Title_Mom_Phi_Axis = "".join(["; p_{", str(particle_title), "}; #phi_{", str(particle_title), "}"])
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

                                Histo_Mom_The_ref_title = "".join(["Histo_P_v_Th_", str(ref)])
                                Histo_Mom_Phi_ref_title = "".join(["Histo_P_v_Phi_", str(ref)])
                                Histo_The_Phi_ref_title = "".join(["Histo_Th_v_Phi_", str(ref)])

                                if(sector == 0):
                                    sdf = CorDpp(rdf, correction, "".join(["Mom_", particle]), event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")
                                else:
                                    sdf = CorDpp(rdf.Filter("".join([particle.replace("l", ""), "sec", " == ", str(sector)])), correction, "".join(["Mom_", particle]), event_type, MM_type, datatype, Cuts if(Cuts in [Calculated_Exclusive_Cuts, CutChoice]) else "")

                                Histo_P_v_Phi[ref] = sdf.Histo2D((Histo_Mom_Phi_ref_title, Title_Mom_Phi, 110, 0, 11, 720, -260, 460), "".join([particle, "_", correction]), "".join([local_Q.replace(" ", ""), particle, "Phi", shift]))
                                count += 1
                                
                                if("" == shift and "" == local_Q):
                                    Histo_P_v_Th[ref] = sdf.Histo2D((Histo_Mom_The_ref_title, Title_Mom_The, 110, 0, 11, 150, 0, 40), "".join([particle, "_", correction]), "".join([particle, "th"]))
                                    count += 1
                                if('mm0' in correction):
                                    Histo_Th_v_Phi[ref] = sdf.Histo2D((Histo_The_Phi_ref_title, Title_The_Phi, 720, -260, 460, 150, 0, 40), "".join([local_Q.replace(" ", ""), particle, "Phi", shift]), "".join([particle, "th"]))
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
    1) SP -> For Single Pion Channel (i.e., ep->eπ+N)
    2) DP -> For Double Pion Channel (i.e., ep->epπ+π-)
    3) P0 -> For Pi0 Channel (i.e., ep->epπ0)
    4) ES -> For Elastic Scattering (i.e., ep->e'p')
    5) E0 -> For Electron Only Channnel (i.e., ep->e'(p'))
    5) MC -> Uses Monte Carlo Simulation for Single Pion Channel (i.e., same as SP but with simulated data)
    
Ending Code...
    """]))

