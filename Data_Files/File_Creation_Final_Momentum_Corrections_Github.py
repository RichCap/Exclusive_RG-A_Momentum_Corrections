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

# if(datatype == "Outbending"):
#     file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/shrestha/clas12momcorr/data/outbending/ePipX/", ""))
#     file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/kenjo/ntuple_epippimp/inb/lvl1_eppimpip.skim4_00", ""))
#     file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/outb/epPipPim.outb.qa.nSidis_00", ""))
#     file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/kenjo/", ""))
#     file_name = str(file_name.replace(".hipo.epip.root", ""))
#     file_name = str(file_name.replace(".hipo.root", ""))
#     file_name = str(file_name.replace("/u/home/richcap/", ""))
#     file_name = str(file_name.replace("qa.", ""))
#     file_name = str(file_name.replace("exclusiveselection.root", "Ex_Select"))
#     file_name = str(file_name.replace("/work/clas12/shrestha/clas12momcorr/utsav/dataFiles/inbending/ePipX/epip.skim4_00", ""))
                                      
# if(datatype == "Inbending"):
#     file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/shrestha/clas12momcorr/data/inbending/ePipX/epip.", ""))
#     file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/kenjo/ntuple_epippimp/inb/lvl1_eppimpip.skim4_00", ""))
#     file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/inb/epPipPim.inb.qa.nSidis_00", ""))
#     file_name = str(file_name.replace(".epippimp", ""))
#     file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/kenjo/", ""))
#     file_name = str(file_name.replace(".hipo.root", ""))
#     file_name = str(file_name.replace(".root", ""))
#     file_name = str(file_name.replace("/u/home/richcap/", ""))
#     file_name = str(file_name.replace("qa.", ""))
#     file_name = str(file_name.replace("exclusiveselection.root", "Ex_Select"))
#     file_name = str(file_name.replace("/work/clas12/shrestha/clas12momcorr/utsav/dataFiles/outbending/ePipX/skim4_00", ""))
    
    
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

file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Single_Pion_Channel_epipN/Inbending/ePip.inb.qa.nSidis_00", ""))

file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Single_Pion_Channel_epipN/Inbending_skim4/ePip.inb.qa.", ""))
    
ROOT.gStyle.SetTitleOffset(1.3, 'y')
ROOT.gStyle.SetGridColor(17)
ROOT.gStyle.SetPadGridX(1)
ROOT.gStyle.SetPadGridY(1)


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DELTA = '\u0394' # symbol
    END = '\033[0m'

    
class root_color:
    # Colors
    Black = 0
    Red = 2
    Green = 3
    Blue = 4
    Yellow = 5
    Pink = 6
    Cyan = 7
    DGreen = 8 # Dark Green
    Purple = 9
    Grey = 13
    Brown = 28
    Gold = 41
    Rust = 46
    
    # Fonts
    Bold = '#font[22]'
    Italic = '#font[12]'
    
    # Symbols
    Delta = '#Delta'
    Phi = '#phi'
    π = '#pi'
    Degrees = '#circ'
    
    Line = '#splitline'

event_Name = "error"

if(event_type == "E0"):
    print(color.RED + "ERROR: E0 is not the correct input type..." + color.END + "\n\tSetting to event_type = EO")
    event_type = "EO"


if(event_type == "SP" or event_type == "MC"):
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
    Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max = 160, -0.5, 0.5
else:
    Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max = 120, -0.1, 0.1

if(event_Name != "error"):
    
    print("".join([color.BOLD, color.BLUE, "\n\n\nStarting ", str(event_Name), " ", str(datatype), "...\n", color.END]))

    # These lines are left over from older versions of the code. Do not change or remove them without editing all other parts of code that reference them.
    CutChoice, CutChoice_2 = 'none', 'none'
    if(event_type == "ES"):
        CutChoice = """
            // For ∆Phi Cuts:
            auto Beam_Energy = 10.6041;
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
        """
        CutChoice_2 = """
            // For ∆Theta Cuts:
            auto Beam_Energy = 10.6041;
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
        """


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
        
        
    if(event_type == "SP" or event_type == "MC"):
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

    if(file_location == "Test" or file_location == "test" or file_location == "time"):
        SaveResultsQ = 'no'

    if(SaveResultsQ == 'no'):
        print("\033[1mNot saving results...\033[0m")
    else:
        print("\033[1mResults WILL be saved\033[0m")

    
    
    Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V1"
    # Added new back-to-back cuts based on the electron's and proton's theta angles (should add up to about 180˚ with the current condition giving a ±5˚ margin of error)
    
    
    Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V2"
    # Replaced the last cut with the particle angles with a cut on particle sectors and testing new cuts on the calculated proton angle (∆Theta_Proton < 5˚)
    # Also simplified how the histograms are eventually saved (added an option to print/test the histograms to be saved)
    # Started to add code to create ∆Theta histograms for more refined exclusive elastic cuts (still being developed)
    
    
    Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V3"
    # Last cuts on the calculated proton angle (∆Theta_Proton < 5˚) did not work =====> Changed how ∆Theta_Proton is calculated (now does not use electron info) - Also changed the cut to 10˚ instead of 5˚
    # Added ∆Theta histograms for more refined exclusive elastic cuts (still use the prior method of calculating ∆Theta_Proton)
    
    Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V4"
    # Replaced the calculated proton angle cuts with another back-to-back cut on the absolute difference in the azimuthal angles of each particle =====> CutChoice is that this ∆Phi should be about 180˚ ±5˚
    # Changed ∆Theta histograms to being ∆Angle histograms (added ∆Phi to the ∆Theta versions of the caclculation)
    
    Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V5"
    # Back-to-back cut now features a cut on the absolute difference of the phi angles of the elastic particles (cut is a pol2 function of the proton momentum - unique to each proton sector AND cuts off for |∆Phi - 180| > 5˚)
    # Modified the Invariant Mass cut using prior back-to-back cut (|∆Phi - 180| > 5˚)
    
    
    Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V6"
    # Back-to-back cut now features a cut on the absolute difference of the phi angles of the elastic particles (cut is a pol2 function of the proton momentum - cut is now tighter than the previous version - unique to each proton sector AND cuts off for |∆Phi - 180| > 3˚)
    # Modified the Invariant Mass cut using prior back-to-back cut
    
    Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V7"
    # Reduced number of corrections being run
    # Added another version of ∆Theta_pro calculation ("D_Angle_V3" gives the proper ∆Phi histograms while "D_Angle_V4" gives the proper ∆Theta_pro calculations)
    # D_Angle plots are now plotted vs the electron momentum (even if calculating proton angle)
    # Multiple exclusivity cuts can now be applied seperately and together
    # Removed the Back-to-Back SECTOR cut (was an automated cut that is covered more directly by other existing cuts)
    # Removed old code that was no longer in use including:
    #  * 1D Missing Mass Histograms
    #  * Missing Mass vs Particle Angles (theta and phi)
    # Changed how the kinematic momentum/angle plots are named and made (better naming convensions used)
    #  * hPARTthall -> Histo_P_v_Th
    #  * hPARTPhiall -> Histo_P_v_Phi
    #  * hPARTthPhiall -> Histo_Th_v_Phi
    #  * histoMakerhmmCPARTall -> Missing_Mass_Histo_Maker
    
    Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V8"
    # Had to update the newest ∆Theta_Pro calculation (did not work again)
    # Updated the way that the default histogram titles were made
    # Changed the ranges on some histograms
    
    
    Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V9"
    # Increased the number of bins used in the ∆Theta_Pro Histograms
    # Added an additional exclusivity cut (CutChoice_2) based on ∆Theta Calculation (D_Angle_V1)
    # Exclusivity Cuts now do not use linear or quadratic equations, but instead use the gaussian widths of the fitted histograms
    # "Cut_Function" now supports a combination of all of these added cuts (names updated somewhat from V8 to differentiate between all of the cut options)
    # Removed Phi binning from the Elastic Channel (option was not being used)

    
    Extra_Part_of_Name = "_GitHub_Cut_Tests_V1"
    # Added a base Invariant Mass Cut that is always applied to the Elastic Events (WM range is set to be between at least 0.6 and 1.3 GeV always)
    # Removed options to plot versus proton momentum and with any additional cuts (done for time constraints)
    
    Extra_Part_of_Name = "_GitHub_Cut_Tests_V2"
    # Added New ∆Phi Cuts with more momentum bins
    # Only the above cut (and the baseline cut from "_GitHub_Cut_Tests_V1") was run
    
    Extra_Part_of_Name = "_GitHub_Cut_Tests_V3"
    # Added New ∆Theta Cuts based on the cuts from "_GitHub_Cut_Tests_V2"
    # Turned off 'phase space' plots (plots that did not involve ∆P, ∆Theta, ∆Phi, or Invariant/Missing Mass)
    

    Extra_Part_of_Name = "_GitHub_Cut_Tests_V4"
    # Added New Invariant Mass Cuts based on the cuts from "_GitHub_Cut_Tests_V3"
        # 3 options of Invariant Mass Cuts have been added based on combinations of the above cuts
    # Turned back on 'phase space' plots but turned off Missing Mass plots (using Invariant Mass instead)
    
    
    Extra_Part_of_Name = "_GitHub_Cut_Tests_V5"
    # Changed the base invariant mass cut to be wider (range extended to W < 1.8 GeV - does not affect existing cuts)
    # Suppressed histograms with cuts that were made with the same variable being plotted
    # Turned off phase space histograms (to run faster)
    # Turned off some cuts - Running the code with the following cuts (only):
        # (*) No (Additonal) Cuts
        # (*) Calculated Exclusivity Cuts
        # (*) Azimuthal Kinematic Cut
        # (*) Calculated Polar Kinematic Cut
        # (*) Azimuthal and Polar Angle Cuts
        # (*) All Additional Cuts)
    # Changed which corrections are being applied to the histograms (without the proton, only electron corrections are needed for ∆P and Invariant Mass)
    # Turned off extra angle calculation types (just V1 and V3 are running - these are the only working versions of ∆Theta and ∆Phi)
    # Only ran for the "ES" channel (not "EO")
    
    Extra_Part_of_Name = "_GitHub_Cut_Tests_V6"
    # The basic Invariant Mass cut is now not made automatically --> testing new cut which is just a basic cut at W < 0.7 GeV and W > 1.4 GeV (called "Calculated_Exclusive_Cuts_V2")
    # Updated the tighter Invariant Mass cut using the Invariant mass plots from the tagged proton channel (i.e., "ES")
    # Increased the range of the y-axis of the ∆P plots (increased to ±2 GeV with the same sizes of binning)
    # Turned the phase space histograms back on
    
    
    Extra_Part_of_Name = "_GitHub_Cut_Tests_V7"
    # Made the basic Invariant Mass cut tighter (i.e., "Calculated_Exclusive_Cuts_V2" --> W < 0.7 GeV and W > 1.2 GeV)
    # Decreased the range of the y-axis of the ∆P plots (decreased to ±1 GeV with the same sizes of binning --> the ideal may be even lower as all desirable events are between ±0.3 Gev but the range has been extended to see more when necessary)
    
    
    Extra_Part_of_Name = "_GitHub_Electron_Refinement_V1"
    # Reintroduced the automatic baseline cut on Invariant Mass for elastic channels (W < 0.6 GeV and W > 1.3 GeV --- "Calculated_Exclusive_Cuts_V2" is not effected)
    # Increased the bin sizes along the y-axis of the ∆P plots for the non-elastic channels (same bin ranges as before, but the bin sizes are now consistent with those from the elastic scattering channels)
        # Other similar updates were also added so that these channels will produce plots which are consistent with the elastic scattering events
    # Running with electron phi bins
    # Phase space histograms now only create a plot for sector 0 (i.e., all sectors -- Optional condition that can be turned off -- does not affect other options)
    # Only running electron kinematics and corrections (for elastic and single pion channels -- Pi+ corrections are included in the SP channel)
    # Updated the default location of the SP files (compatible with current file names for the SP files made with the groovy script)
    
    
    
    Extra_Part_of_Name = "_GitHub_Electron_Refinement_V2"
    # Minor update to histogram titles (related to the phi binning parts of titles)
    # Updated SP files to take in files using skim4 data (files which did not have the W cuts applied)
    
    
    if(event_type == "MC"):
        Extra_Part_of_Name = "_GitHub_MC_Test_V1"
        # Testing the momentum corrections using Monte Carlo files (for use in SIDIS analysis)
        # Runs the same as event_type == "SP"
    
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

    if(file_location == "All" or file_location == "Test" or file_location == "test" or file_location == "time"):
        if(event_type == "SP" or event_type == "MC"):
            if(datatype == "Inbending"):
                # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/shrestha/clas12momcorr/data/inbending/ePipX/epip.skim4_00*"
                # running_code_with_these_files = "/work/clas12/shrestha/clas12momcorr/utsav/dataFiles/inbending/ePipX/epip.skim4_005*"
                running_code_with_these_files = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Single_Pion_Channel_epipN/Inbending/ePip.inb.qa.nSidis_005*"
            else:
                # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/shrestha/clas12momcorr/outbending/ePipX/skim4_00*"
                # running_code_with_these_files = "/work/clas12/shrestha/clas12momcorr/utsav/dataFiles/outbending/ePipX/skim4_005*"
                running_code_with_these_files = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Single_Pion_Channel_epipN/Outbending/ePip.outb.qa.nSidis_005*"

        if(event_type == "DP"):
            if(datatype == "Inbending"):
                running_code_with_these_files = "/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/inb/epPipPim.inb.qa.nSidis_005*"
            else:
                running_code_with_these_files = "/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/outb/epPipPim.outb.qa.nSidis_005*"
                
            running_code_with_these_files = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Double_Pion_Channel_eppippim/", str(datatype), "/epPipPim.", "out" if("Out" in str(datatype)) else "in", "b.qa.nSidis_005*"])
                
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
        rdf = rdf.Filter("""
        auto Beam_Energy = 10.6041;
        auto Proton_Mass = 0.938;
        auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
        auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
        auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
        auto Cut_Variable = (beam + targ - eleC).M();
        double Cut_Upper = 1.3;
        double Cut_Lower = 0.6;
        return ((Cut_Variable < Cut_Upper) && (Cut_Variable > Cut_Lower));
        """)

    #############################################################################
    ##=====##=====##=====##=====##   Loading RDF   ##=====##=====##=====##=====##
    #############################################################################

    if(See_Num_of_Events_Q != 'n'):
        print("".join(["Number of events = ", str(rdf.Count().GetValue())]))
    print("".join([color.BOLD, color.BLUE, "Running code with files located here:\n", color.END, str(running_code_with_these_files), "\n"]))




    if(event_type != "SP" and event_type != "MC" and event_type != "EO"):
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
    if(event_type != "SP" and event_type != "MC" and event_type != "EO"):
        
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
        if(event_type != "P0" and event_type != "ES"):
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
        if(event_type != "SP" and event_type != "MC"):
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
        if(event_type != "SP" and event_type != "MC"):
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

    ############################################################
    #----------#     Last updated on: 9-11-2022     #----------#
    ############################################################

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
                // corEl == 2 --> Modified Correction for the Elastic Events

            // corPip ==> Gives the 'generation' of the π+ Pion correction
                // corPip == 0 --> No Correction
                // corPip == 1 --> Final Version of Corrections


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
                
                if(corEl == 2){
                    if(sec == 1){
                        // The QUADRATIC function predicted for Δp_{el} for [Inbending][Cor = El Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 1] is:
                        dp = dp + ((7.8940e-05)*pp*pp + (-2.6436e-03)*pp + (0.06115));
                    }

                    if(sec == 2){
                        // The QUADRATIC function predicted for Δp_{el} for [Inbending][Cor = El Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 2] is:
                        dp = dp + ((7.8694e-04)*pp*pp + (-2.0503e-03)*pp + (-0.01185));
                    }

                    if(sec == 3){
                        // The QUADRATIC function predicted for Δp_{el} for [Inbending][Cor = El Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 3] is:
                        dp = dp + ((4.7172e-03)*pp*pp + (-0.04838)*pp + (0.10936));
                    }

                    if(sec == 4){
                        // The QUADRATIC function predicted for Δp_{el} for [Inbending][Cor = El Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 4] is:
                        dp = dp + ((2.5303e-03)*pp*pp + (-0.02057)*pp + (0.01269));
                    }

                    if(sec == 5){
                        // The QUADRATIC function predicted for Δp_{el} for [Inbending][Cor = El Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 5] is:
                        dp = dp + ((1.9005e-03)*pp*pp + (-0.02135)*pp + (0.05793));
                    }

                    if(sec == 6){
                        // The QUADRATIC function predicted for Δp_{el} for [Inbending][Cor = El Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 6] is:
                        dp = dp + ((1.6142e-04)*pp*pp + (8.2249e-03)*pp + (-0.05631));
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
    #     // corEl == 2 --> Modified for elastic corrections
    def NameElCor(corEl, datatype):
        coutN = 0
        if('mm0' in corEl):
            coutN = 0
        else:
            if("mmEF" not in corEl):
                coutN = 1
            else:
                coutN = 2
        return coutN

    # // corPip ==> Gives the 'generation' of the π+ Pion correction
    #     // corPip == 0 --> No Correction
    #     // corPip == 1 --> Quad Momentum, Quad Phi (Final Version)
    def NamePipCor(corPip, datatype):
        coutN = 0
        if("Pip" not in corPip):
            coutN = 0
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
        corEl_Num = str(NameElCor(Correction, Data_Type))
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

    auto Final_Output = Output_Vectors.M""", "2" if Out_Type == "WM2" else "","""();

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

            ##===============================##
            ##=====##   Pi0 Channel   ##=====##
            ##===============================##
            if('eppi0X' == MM_Type or Channel_Type == "P0"):
                Calculation_Code_Choice = """
    auto Output_Vectors = beam + targ - eleC - proC;

    auto Final_Output = Output_Vectors.M2();

                """
                
            ##======================================##
            ##=====##   Elastic Scattering   ##=====##
            ##======================================##
            if('epX' == MM_Type or Channel_Type == "ES"):
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
            if(Channel_Type == "SP" or Channel_Type == "MC"):
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
        pro_Calculate = pro_CalculateP;
    }

    else{
        pro_Calculate = pro_CalculateM;
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

    Pro_Th_Calc = acos(((10.6041 + 0.938)*(proC.E() - + 0.938))/(10.6041*proC.P()))*(180/3.1415926);

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

    auto Final_Output = """, "ele" if "p" not in Out_Type else str(Out_Type.replace("Mom_", "")), """C.P();

            """])



        Full_Correction_Output = "".join([Correction_Code, """

    auto Beam_Energy = 10.6041;
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


        try:
            Output = Data_Frame.Define(str(Output_Title), str(Full_Correction_Output))
            # print("".join([color.BOLD, "Correction Code: \n", color.END, str(Full_Correction_Output)]) if("D_Angle" in Out_Type) else "")
            if(Extra_Cut != "none" and Extra_Cut != ""):
                Output = Output.Filter(Extra_Cut)
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

    def corNameTitles(CorrectionNameIn):
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
            CorrectionName1 = 'El Cor (Quad - Linear Phi - Refined 1)'.replace('Linear', 'Linear' if "In" in datatype else 'Quad')
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
            CorrectionName1 = 'El Cor (Quad - Quad Phi - Elastic Cor)'
            
        if(event_type == "EO"):
            if(CorrectionNameIn == "mm0"):
                CorrectionName = "No Momentum Corrections"
            else:
                CorrectionName = CorrectionName1
            return CorrectionName

        if('Pip' not in CorrectionNameIn):
            CorrectionName2 = 'No Pi+ Cor' if event_type != "P0" else ""
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

        if('Pim' not in CorrectionNameIn):
            CorrectionName3 = 'No Pi- Cor' if event_type == "DP" else ""
        if('Pim' in CorrectionNameIn):
            if('MMpimPhi' in CorrectionNameIn):
                CorrectionName3 = 'Pi- Cor (Linear - Linear Phi)'
            if('MMpim_qPhi' in CorrectionNameIn):
                CorrectionName3 = 'Pi- Cor (Quad - Quad Phi)'
            if('MMpim_F' in CorrectionNameIn):
                CorrectionName3 = 'Pi- Cor (Quad - Quad Phi - Rounded)'

        if('Pro' not in CorrectionNameIn):
            CorrectionName4 = 'No Pro Cor' if(event_type != "SP" and event_type != "MC") else ""
            # if(('_NoELC' not in CorrectionNameIn and event_type == "DP") or (event_type == "P0")):
            if('_NoELC' not in CorrectionNameIn):
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
            if('_NoELC' not in CorrectionNameIn):
                CorrectionName4 = CorrectionName4.replace(")", " - Energy Loss Cor)")

        if(CorrectionName1 == 'Error'):
            print("".join(["Error with the Electron Correction in CorrectionNameInput = ", str(CorrectionNameIn)]))
            CorrectionName1 = "El Cor (ERROR)"

        if(CorrectionName2 == 'Error' and event_type != "P0" and event_type != "ES"):
            print("".join(["Error with the Pi+ Pion Correction in CorrectionNameInput = ", str(CorrectionNameIn)]))
            CorrectionName2 = "Pi+ Cor (ERROR)"

        if(CorrectionName3 == 'Error' and event_type != "P0" and event_type != "SP" and event_type != "MC" and event_type != "ES"):
            print("".join(["Error with the Pi- Pion Correction in CorrectionNameInput = ", str(CorrectionNameIn)]))
            CorrectionName3 = "Pi- Cor (ERROR)"

        if(CorrectionName4 == 'Error' and event_type != "SP" and event_type != "MC"):
            print("".join(["Error with the Proton Correction in CorrectionNameInput = ", str(CorrectionNameIn)]))
            CorrectionName4 = "Pro Cor (ERROR)"

        CorrectionName = "".join([CorrectionName1, " - " if CorrectionName2 != "" else "", CorrectionName2, " - " if CorrectionName3 != "" else "", CorrectionName3, " - " if CorrectionName4 != "" else "", CorrectionName4])
        
        if(event_type == "SP" or event_type == "MC"):
            CorrectionName = "".join([CorrectionName1, " - " if CorrectionName2 != "" else "", CorrectionName2])
        elif(event_type != "ES"):
            CorrectionName = "".join([CorrectionName1, " - " if CorrectionName2 != "" else "", CorrectionName2, " - " if CorrectionName3 != "" else "", CorrectionName3, " - " if CorrectionName4 != "" else "", CorrectionName4])
        else:
            CorrectionName = "".join([CorrectionName1, " - " if CorrectionName4 != "" else "", CorrectionName4])


        if(CorrectionName1 == 'El Cor (Quad - Quad Phi)' and CorrectionName2 == 'Pi+ Cor (Quad - Quad Phi)'):
            if(event_type == "SP" or event_type == "MC"):
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

        if(event_type != "SP" and event_type != "MC"):
            if("Energy Loss Cor" not in CorrectionName and '_NoELC' not in CorrectionNameIn):
                CorrectionName = CorrectionName.replace('Pro Cor (Quad - Quad Phi)', 'Pro Cor (Quad - Quad Phi - Energy Loss Cor)')
                

        if(CorrectionNameIn == "mm0" or CorrectionNameIn == "mm0_NoELC"):
            CorrectionName = "".join(["No Momentum Corrections", " (Energy Loss Cor)" if(event_type != "SP" and event_type != "MC" and "NoELC" not in CorrectionNameIn) else ""])

        

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
        if(Extra_Cut == "" or Extra_Cut == "none" or Extra_Cut == "Both" or Extra_Cut == "Both_2" or Extra_Cut == "Both_3" or Extra_Cut == "All"):
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

        CorrrectionName = corNameTitles(Correction)

        name = (Correction, Sector, Binning, Region, Particle_Plot, Particle, Extra_Cut)
        
        output_title = "".join(["#splitline{", datatype, " Invariant Mass}{", str(CorrrectionName), " -- ", SecName, "}; p_{", Particle_Plot_Formatting, "} [GeV]; W [GeV]"])
        if(regionName != "" and Extra_Cut != ""):
            output_title = "".join(["#splitline{", datatype, " Invariant Mass}{#splitline{", str(CorrrectionName), " -- ", SecName, "}{", regionName, "}}; p_{", Particle_Plot_Formatting, "} [GeV]; W [GeV]"])
        if(Extra_Cut != "" and regionName == ""):
            output_title = "".join(["#splitline{", datatype, " Invariant Mass}{#splitline{", str(CorrrectionName), " -- ", SecName, "}{Cut Applied: ", Extra_Cut, "}}; p_{", Particle_Plot_Formatting, "} [GeV]; W [GeV]"])
        if(Extra_Cut != "" and regionName != ""):
            output_title = "".join(["#splitline{", datatype, " Invariant Mass}{#splitline{", str(CorrrectionName), " -- ", SecName, "}{#splitline{Cut Applied: ", Extra_Cut, "}{", regionName, "}}}; p_{", Particle_Plot_Formatting, "} [GeV]; W [GeV]"])
            
        WC_out = "".join(["WM_", Correction])

        output = Bank.Histo2D(("".join(["HWC_Histo_All_", str(name)]), str(output_title), 200, 2 if 'el' in Particle_Plot else 0, 12 if 'el' in Particle_Plot else 10, 200, 0, 5), Particle_Plot, WC_out)

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

        CorrrectionName = corNameTitles(Correction)

        name = (Correction, Sector, '', Binning, Region, Particle_Plot, Particle, Extra_Cut)

        
        output_title = "".join(["#splitline{(", str(datatype), ") MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "} ", str(SecName), "}{Correction:", str(CorrrectionName), "};p_{", str(Particle_Plot_Formatting), "} [GeV];MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}"])
        if(regionName != "" and Extra_Cut != ""):
            output_title = "".join(["#splitline{#splitline{(", str(datatype), ") MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "} ", str(SecName), "}{Correction:", str(CorrrectionName), "}}{", str(regionName), "};p_{", str(Particle_Plot_Formatting), "} [GeV];MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}"])
        if(Extra_Cut != "" and regionName == ""):
            output_title = "".join(["#splitline{#splitline{(", str(datatype), ") MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "} ", str(SecName), "}{Correction:", str(CorrrectionName), "}}{Cut Applied: ", str(Extra_Cut), "};p_{", str(Particle_Plot_Formatting), "} [GeV];MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}"])
        if(Extra_Cut != "" and regionName != ""):
            output_title = "".join(["#splitline{#splitline{#splitline{(", str(datatype), ") MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "} ", str(SecName), "}{Correction:", str(CorrrectionName), "}}{Cut Applied: ", str(Extra_Cut), "}}{", str(regionName), "};p_{", str(Particle_Plot_Formatting), "} [GeV];MM", "^{2}" if(MM_type != "epipX") else "", "_{", str((MM_type).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}"), "}"])

        output = Bank.Histo2D(("".join(["hmmCPARTall_", str(name)]), str(output_title), 200, 2 if 'el' in Particle_Plot else 0, 12 if 'el' in Particle_Plot else 10, Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max), Particle_Plot, Correction)

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
    Calculated_Exclusive_Cuts_V2, Calculated_Exclusive_Cuts_V3 = "esec != -2", "esec != -2"



    ###########################################################################################################################
    ##=======================================================================================================================##
    ##===============##=============##         Exclusivity Cuts (Using MM from eπ+(N))         ##=============##=============##
    ##=======================================================================================================================##
    ###########################################################################################################################
    if(MM_type == "epipX"):
        
        if("In" in datatype):

            Calculated_Exclusive_Cuts = """
            
                auto beam = ROOT::Math::PxPyPzMVector(0, 0, 10.6041, 0);
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

            """
            
        if("Out" in datatype):

            Calculated_Exclusive_Cuts = """
            
                auto beam = ROOT::Math::PxPyPzMVector(0, 0, 10.6041, 0);
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

            """


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
            Calculated_Exclusive_Cuts = """

                auto beam = ROOT::Math::PxPyPzMVector(0, 0, 10.6041, 0);
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

            """
            


            
        if("Out" in datatype):
            

            Calculated_Exclusive_Cuts = """

                auto beam = ROOT::Math::PxPyPzMVector(0, 0, 10.6041, 0);
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

            """
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
            Calculated_Exclusive_Cuts = """

                auto beam = ROOT::Math::PxPyPzMVector(0, 0, 10.6041, 0);
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
                
            """
            
        if("Out" in datatype):
            Calculated_Exclusive_Cuts = """

                auto beam = ROOT::Math::PxPyPzMVector(0, 0, 10.6041, 0);
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
                
            """
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
        Calculated_Exclusive_Cuts = """        
        // For Invariant Mass Cut (Determined with the help of Azimuthal Kinematic Cut applied on the invariant mass histogram):
        auto Beam_Energy = 10.6041;
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
        """
        Calculated_Exclusive_Cuts_V2 = """
        auto Beam_Energy = 10.6041;
        auto Proton_Mass = 0.938;
        auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
        auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
        auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
        auto Cut_Variable = (beam + targ - eleC).M();
        double Cut_Upper = 1.2;
        double Cut_Lower = 0.7;
        return ((Cut_Variable < Cut_Upper) && (Cut_Variable > Cut_Lower));
        """
        
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
    
    
    if(CutChoice == '' or CutChoice == 'none'):
        kinematicCuts = ["", Calculated_Exclusive_Cuts]
    elif(CutChoice_2 != "" and CutChoice_2 != "none"):
        kinematicCuts = ["", Calculated_Exclusive_Cuts, CutChoice, CutChoice_2, "Both", "Both_2", "Both_3", "All"]
    else:
        kinematicCuts = ["", Calculated_Exclusive_Cuts, CutChoice, "Both"]
        
    if("ES" == event_type):
        kinematicCuts = ["", Calculated_Exclusive_Cuts, CutChoice, CutChoice_2, "Both_3", "All"]
    
    if(Calculated_Exclusive_Cuts_V2 != "esec != -2"):
        kinematicCuts.append(Calculated_Exclusive_Cuts_V2)
    if(Calculated_Exclusive_Cuts_V3 != "esec != -2"):
        kinematicCuts.append(Calculated_Exclusive_Cuts_V3)
        
        
    def Cut_Function(Data_Frame, Input_Cut, Output_Type="Default"):
        
        Cut_Title = ""
        if(str(Input_Cut) == str(Calculated_Exclusive_Cuts)):
            Cut_Title = "Calculated Exclusivity Cuts"
        if(str(Input_Cut) == str(Calculated_Exclusive_Cuts_V2)):
            Cut_Title = "Calculated Exclusivity Cuts (Basic)"
        if(str(Input_Cut) == str(Calculated_Exclusive_Cuts_V3)):
            Cut_Title = "Calculated Exclusivity Cuts (Based on Both Angles)"
        if(str(Input_Cut) == str(CutChoice)):
            Cut_Title = "Azimuthal Kinematic Cut"
        if(CutChoice_2 != "" and CutChoice_2 != "none" and str(Input_Cut) == str(CutChoice_2)):
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
        if(Input_Cut != "" and Input_Cut != "none"):
            try:
                if("Both" == Input_Cut and CutChoice != "none"):
                    Cut_Data_Frame = Cut_Data_Frame.Filter(Calculated_Exclusive_Cuts)
                    Cut_Data_Frame = Cut_Data_Frame.Filter(CutChoice)
                elif("Both_2" == Input_Cut and CutChoice_2 != "" and CutChoice_2 != "none"):
                    Cut_Data_Frame = Cut_Data_Frame.Filter(Calculated_Exclusive_Cuts)
                    Cut_Data_Frame = Cut_Data_Frame.Filter(CutChoice_2)
                elif("Both_3" == Input_Cut and CutChoice != "none" and CutChoice_2 != "" and CutChoice_2 != "none"):
                    Cut_Data_Frame = Cut_Data_Frame.Filter(CutChoice)
                    Cut_Data_Frame = Cut_Data_Frame.Filter(CutChoice_2)
                elif("All" == Input_Cut and CutChoice != "none" and CutChoice_2 != "" and CutChoice_2 != "none"):
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
        Delta_Pip_histo_SecList = [1, 2, 3, 4, 5, 6] # Only the proton correction is available for the double pion channel (Turned off π0 channel as well)
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

    
    
    if(event_type == "SP" or event_type == "MC"):
        if(datatype == "Inbending"):
            Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_PipMMF']

        if(datatype == "Outbending"):
            Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_PipMMF']
            
        # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        # Delta_P_histo_CompareList = ['pi+', 'el']
        Delta_P_histo_CompareList = ['el']
        # Delta_P_histo_CompareList = ['pi+']
            
            
    if(event_type == "DP"):
        if(datatype == "Inbending"):
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F_NoELC', 'mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F']
            
        if(datatype == "Outbending"):
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F_NoELC', 'mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F']
            
        # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        Delta_P_histo_CompareList = ['pro']
            
            
    if(event_type == "P0"):
        if(datatype == "Inbending"):
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F']

        if(datatype == "Outbending"):
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F']
            
        # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        # Delta_P_histo_CompareList = ['pro', 'el']
        Delta_P_histo_CompareList = ['pro']
        
        
    if(event_type == "ES"):
        if(datatype == "Inbending"):
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F', 'mmEF_NoELC', 'mmEF_ProMMpro_F_NoELC', 'mmEF', 'mmEF_ProMMpro_F']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF_ProMMpro_F', 'mmEF_ProMMpro_F_NoELC', 'mmEF', 'mmEF_ProMMpro_F']
            Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmF_ProMMpro_F']
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmF']
            
        if(datatype == "Outbending"):
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F', 'mmEF_NoELC', 'mmEF_ProMMpro_F_NoELC', 'mmEF', 'mmEF_ProMMpro_F']
            # Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF_ProMMpro_F', 'mmEF_ProMMpro_F_NoELC', 'mmEF', 'mmEF_ProMMpro_F']
            Delta_P_histo_CorList = ['mm0_NoELC', 'mm0', 'mmF_ProMMpro_F']
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmF']
            
            
        # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        # Delta_P_histo_CompareList = ['pro', 'el']
        Delta_P_histo_CompareList = ['el']
        
        
        
    if(event_type == "EO"):
        if(datatype == "Inbending"):
            Delta_P_histo_CorList = ['mm0', 'mmF']
        if(datatype == "Outbending"):
            Delta_P_histo_CorList = ['mm0', 'mmF']
        Delta_P_histo_CompareList = ['el']






    if("pi+" not in Delta_P_histo_CompareList and 'pro' not in Delta_P_histo_CompareList):
        Delta_Pip_histo_SecList = ["all"]



    
    # Set the y-axis range od the ∆P histograms:
        # Note: original default binning was set to 200 bins for a range of -1 to 1 (halved for the elastic colisions)
    if("E" not in event_type):
        extendx_min, extendx_max = -3, 3
        # size_of_Dp_Bins = 0.005
        size_of_Dp_Bins = 0.01
    else:
        # extendx_min, extendx_max = -0.3, 0.3
        extendx_min, extendx_max = -1, 1
        size_of_Dp_Bins = 0.01
        
        
    NumOfExtendedBins = round((extendx_max - extendx_min)/size_of_Dp_Bins)


    # For using ShowBackground() with the slices of the extra 2D histograms
    # SBehQ = 'yes'
    SBehQ = 'no'


    # Number of (π+/pro) phi bins
    NumPhiBins = ['1', '3']
    
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
            print("".join(["The ", "Pi+" if(event_type == "SP" or event_type == "MC") else "proton", " sectors being run are: ", str(Delta_Pip_histo_SecList)]))
        print("".join(["The electron sectors being run are: ", str(ExtraElectronSecListFilter)]))
        # if(event_type != "EO" and ("pi+" in Delta_P_histo_CompareList or 'pro' in Delta_P_histo_CompareList)):
        if(event_type != "EO"):
            print("".join(["The list of (", "Pi+" if(event_type == "SP" or event_type == "MC") else "Proton", ") phi bins that will be run is: ", str(NumPhiBins)]))
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
            for correction in Delta_P_histo_CorList:
                for sec in Delta_Pip_histo_SecList:
                    for secEL in ExtraElectronSecListFilter:
                        for binning in NumPhiBins:
                            reglist = regList_Call(binning, 'pip' if(event_type == "SP" or event_type == "MC") else "pro", 1)
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


    particleList = []
    particle_plot_List = []
    
    if(event_type == "SP" or event_type == "MC"):
        # particleList = ['el', 'pip']
        # particle_plot_List = ['el', 'pip']
        particleList = ['el']
        particle_plot_List = ['el']
        
        
    if(event_type == "DP"):
        particleList = ['el', 'pip', 'pro', 'pim']
        
        particle_plot_List = ['el', 'pip', 'pro', 'pim']
        
        
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
    
    
    if(event_type == "SP" or event_type == "MC"):
        if(datatype == "Inbending"):
            correctionList = ['mm0', 'mmF', 'mmF_PipMMF']
        if(datatype == "Outbending"):
            correctionList = ['mm0', 'mmF', 'mmF_PipMMF']
            
    if(event_type == "DP"):
        if(datatype == "Inbending"):
            correctionList = ['mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F_NoELC', 'mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F']
            
        if(datatype == "Outbending"):
            correctionList = ['mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F_NoELC', 'mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_F']
            
            
    if(event_type == "P0"):
        if(datatype == "Inbending"):
            correctionList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F']
            
        if(datatype == "Outbending"):
            correctionList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_F_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_F']
            
            
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
            correctionList = ['mm0', 'mmF']
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


    
    # Run with the Invariant Mass histograms?
    # Letting Run_Invariant_Mass_Histos = 'yes' causes the code to also create histograms for Invariant Mass versus the particle momentum
    Run_Invariant_Mass_Histos = 'yes'
    # Run_Invariant_Mass_Histos = 'no'

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

        print("".join(["The sectors to be included are: ", str(SecRangeAll)]))

        print("")
        
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
            if(Cuts in [Calculated_Exclusive_Cuts if("E" not in event_type) else "esec != -2", Calculated_Exclusive_Cuts_V2, Calculated_Exclusive_Cuts_V3, "Both", "Both_2", "All"]):
                continue
            for particle in particle_plot_List:
                for sector in SecRangeAll:
                    for correction in correctionList:
                        for binning in binningList:
                            for particle_filter in particleList:
                                regionList = regList_Call(binning, particle_filter, 1)
                                for region in regionList:
                                    if(Print_Names_Of_Histos_To_Be_Made_Q == 'yes'):
                                        print(str((correction, sector, "", binning, region, particle, particle_filter, "Cut" if(Cuts != "") else "")))
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
                                    if('mm0' == correction):
                                        countHisto += 1
                                
    if(Run_Invariant_Mass_Histos == 'yes'): 
        for Cuts in kinematicCuts:
            if(Cuts in [Calculated_Exclusive_Cuts if("E" in event_type) else "esec != -2", Calculated_Exclusive_Cuts_V2, Calculated_Exclusive_Cuts_V3, "Both", "Both_2", "All"]):
                continue
            for particle in particle_plot_List:
                for particle_filter in particleList:
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

    print(color.BOLD + color.BLUE + "\nMaking Histograms now..." + color.END)


    #############################################################################################################
    ##=====##=====##=====##=====##=====##     Making Delta P Histograms     ##=====##=====##=====##=====##=====##
    #############################################################################################################

    if(Delta_P_histo_Q == 'y'):

        Dmom_pip_Histo, Dmom_pel_Histo, Dmom_pro_Histo = {}, {}, {}

        # print("Making the ∆P Histograms...")
        for Cuts in kinematicCuts:

            Cut_rdf, Cut_Title = Cut_Function(rdf, Cuts)

            for correction in Delta_P_histo_CorList:

                correctionNAME = corNameTitles(correction)
                Erdf = Cut_rdf
                if('pi+' in Delta_P_histo_CompareList and Delta_Pip_histo_Q == 'y'):
                    Erdf = CorDpp(Erdf, correction, "D_pip", event_type, MM_type, datatype, Cuts if(Cuts == Calculated_Exclusive_Cuts or Cuts == CutChoice) else "")
                if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                    Erdf = CorDpp(Erdf, correction, "D_pro", event_type, MM_type, datatype, Cuts if(Cuts == Calculated_Exclusive_Cuts or Cuts == CutChoice) else "")
                if('el' in Delta_P_histo_CompareList and Delta_Pel_histo_Q == 'y'):
                    Erdf = CorDpp(Erdf, correction, "D_pel", event_type, MM_type, datatype, Cuts if(Cuts == Calculated_Exclusive_Cuts or Cuts == CutChoice) else "")

                for sec in Delta_Pip_histo_SecList:

                    SecName = "".join(["Pi+" if(event_type == "SP" or event_type == "MC") else "Pro", " Sector ", str(sec)]) if(sec != "all" and sec != 0) else ""

                    for secEL in ExtraElectronSecListFilter:

                        if(secEL != "all" and secEL != 0):
                            if(sec != "all" and sec != 0):
                                SecName = ''.join(["Pi+" if(event_type == "SP" or event_type == "MC") else "Pro", " Sector ", str(sec), " and El Sector ", str(secEL)])
                            else:
                                SecName = ''.join(['El Sector ', str(secEL)])
                                
                        if(SecName == ""):
                            SecName = "All Sectors"

                        for binning in NumPhiBins:

                            reglist = regList_Call(binning, 'pip' if(event_type == "SP" or event_type == "MC") else 'pro', 2)

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

                                        if(sec != "all" and sec != 0):
                                            sdf = regFilter(Erdf.Filter("".join(["pip" if(event_type == "SP" or event_type == "MC") else "pro", "sec == ", str(sec)])), binning, sec, region, 'S', Cuts if(Cuts == Calculated_Exclusive_Cuts or Cuts == CutChoice) else "", 'pip' if(event_type == "SP" or event_type == "MC") else 'pro')
                                        else:
                                            sdf = regFilter(Erdf, binning, sec, region, 'S', Cuts if(Cuts == Calculated_Exclusive_Cuts or Cuts == CutChoice) else "", 'pip' if(event_type == "SP" or event_type == "MC") else 'pro')

                                        if(secEL != "all" and secEL != 0):
                                            sdf = sdf.Filter("".join(["esec == ", str(secEL)]))


                                        if(binningEL != '1'):
                                            sdf = regFilter(sdf, binningEL, secEL, regionEL, 'S', Cuts if(Cuts == Calculated_Exclusive_Cuts or Cuts == CutChoice) else "", 'el')
                                            histoName = (correction, '', SecName, binning, region, binningEL, regionEL, Cut_Title)
                                        else:
                                            histoName = (correction, '', SecName, binning, region, Cut_Title)
                                            
                                            
                                        Title_Line_1 = "".join(["(", str(datatype), ") #Delta p_{Particle} vs p_{Particle}"])
                                        Title_Line_2 = ((("".join(["Correction: ", str(root_color.Bold), "{", correctionNAME, "}"]).replace("Pi+", "#pi^{+}")).replace("Pi-", "#pi^{-}")).replace("Phi", "#phi"))
                                        Title_Line_3 = "".join([str(SecName), "".join([" -- #phi_{", "#pi^{+} " if(event_type == "SP" or event_type == "MC") else "Pro", "} Bin: ", str(regionName)]) if(str(regionName) != "" and "No Phi Bins" not in regionName) else "", "".join([" -- #phi_{El} Bin: ", str(regionNameEL)]) if(str(regionNameEL) != "" and "No Phi Bins" not in regionNameEL) else ""])
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
                                            Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), Title.replace("Particle", "Pro"), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pro' if("_NoELC" in correction) else "pro_cor", ''.join(['D_pro_', str(correction)]))
                                            # if(binningEL == '1'):
                                            #     Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), "".join(["#splitline{" if(Cut_Title != "") else "", "(", str(datatype), ") #Delta p_{pro} vs p_{pro} ", str(SecName), " ", str(correctionNAME), " " ,str(regionName), "".join(["}{Cut Applied: ", str(Cut_Title), "}"]) if(Cut_Title != "") else "", "; ", "p_{pro}" if("_NoELC" in correction) else "Corrected p_{pro}", "; #Delta p_{pro}"]), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pro' if("_NoELC" in correction) else "pro_cor", ''.join(['D_pro_', str(correction)]))
                                            # else:
                                            #     Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), "".join(["#splitline{" if(Cut_Title != "") else "", "#splitline{#splitline{#Delta p_{pro} vs p_{pro} -- ", str(SecName), "}{Correction: ", str(correctionNAME), "}}{Pro: ", str(regionName) + " -- El: ", str(regionNameEL), "".join(["}{Cut Applied: ", str(Cut_Title)]) if(Cut_Title != "") else "", "}; ", "p_{pro}" if("_NoELC" in correction) else "Corrected p_{pro}", "; #Delta p_{pro}"]), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pro' if("_NoELC" in correction) else "pro_cor", ''.join(['D_pro_', str(correction)]))

                                            Delta_P_histo_Count += 1


                                        if('el' in Delta_P_histo_CompareList and Delta_Pel_histo_Q == 'y'):
                                            Dmom_pel_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pel_Histo", str(histoName)]), Title.replace("Particle", "El"), 120, 0, 12, NumOfExtendedBins, extendx_min, extendx_max), 'el', ''.join(['D_pel_', str(correction)]))
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

                    correctionNAME = corNameTitles(correction)
                    
                    Erdf = Cut_rdf
                    Erdf = CorDpp(Erdf, correction, Calc_Version, event_type, MM_type, datatype, Cuts if(Cuts == Calculated_Exclusive_Cuts or Cuts == CutChoice) else "")

                    for sec in [0, 1, 2, 3, 4, 5, 6]:

                        SecName = "".join(["El Sector ", str(sec)]) if(sec != 0) else "All Sectors"

                        if(sec != 0):
                            sdf = regFilter(Erdf.Filter("".join(["esec == ", str(sec)])), '1', sec, 'regall', 'S', Cuts if(Cuts == Calculated_Exclusive_Cuts or Cuts == CutChoice) else "", 'el')
                        else:
                            sdf = regFilter(Erdf, '1', sec, 'regall', 'S', Cuts if(Cuts == Calculated_Exclusive_Cuts or Cuts == CutChoice) else "", 'el')
                            
                        histoName = (correction, '', SecName, binning, region, Cut_Title, str(Calc_Version))

                        Min_Delta_Angle = -50 if("V3" not in Calc_Version) else 155
                        Max_Delta_Angle = 50 if("V3" not in Calc_Version) else 205

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
            if(Cuts in [Calculated_Exclusive_Cuts if("E" not in event_type) else "esec != -2", Calculated_Exclusive_Cuts_V2, Calculated_Exclusive_Cuts_V3, "Both", "Both_2", "All"]):
                continue
                # Do not plot variables with cuts applied to them that are based on themselves
            Cut_rdf, Cut_Title = Cut_Function(rdf, Cuts)
            for particle in particle_plot_List:
                for sector in SecRangeAll:

                    for correction in correctionList:
                        sdf1 = CorDpp(Cut_rdf, correction, "MM", event_type, MM_type, datatype, Cuts if(Cuts == Calculated_Exclusive_Cuts or Cuts == CutChoice) else "")

                        for binning in binningList:
                            for particle_filter in particleList:
                                secfilter = 'esec' if(particle_filter == 'el') else 'pipsec' if(particle_filter == 'pip') else 'pimsec' if(particle_filter == 'pim') else 'prosec' if(particle_filter == 'pro') else 'error'

                                if(secfilter == "error"):
                                    print("\nERROR IN SECTOR DEFINITION (Missing Mass)\n")

                                if(sector != 0):
                                    sdf = sdf1.Filter("".join([secfilter, ' == ', str(sector)]))
                                else:
                                    sdf = sdf1

                                regionList = regList_Call(binning, particle_filter, 1)

                                for region in regionList:

                                    name = (correction, sector, '', binning, region, particle, particle_filter, Cut_Title)

                                    hmmCPARTall[name] = Missing_Mass_Histo_Maker(regFilter(sdf, binning, sector, region, '', Cuts if(Cuts == Calculated_Exclusive_Cuts or Cuts == CutChoice) else "", particle_filter), correction, sector, region, '', binning, particle, particle_filter, Cut_Title)
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
            if(Cuts in [Calculated_Exclusive_Cuts if("E" in event_type) else "esec != -2", Calculated_Exclusive_Cuts_V2, Calculated_Exclusive_Cuts_V3, "Both", "Both_2", "All"]):
                continue
                # Do not plot variables with cuts applied to them that are based on themselves
            Cut_rdf, Cut_Title = Cut_Function(rdf, Cuts)
            for correction in correctionList:
                sdf1 = CorDpp(Cut_rdf, correction, "WM", event_type, MM_type, datatype, Cuts if(Cuts == Calculated_Exclusive_Cuts or Cuts == CutChoice) else "")
                for sector in SecRangeAll:
                    for particle in particle_plot_List:
                        for particle_filter in particleList:
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
                                    HWC_Histo_All[name] = histoMaker_HWC_Histo_All(regFilter(sdf, binning, sector, region, "", Cuts if(Cuts == Calculated_Exclusive_Cuts or Cuts == CutChoice) else "", particle_filter), correction, sector, region, binning, particle, particle_filter, Cut_Title)

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
                correctionNAME = corNameTitles(correction)
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
                                
                                Title_Line_2 = ((("".join(["Correction: ", str(root_color.Bold), "{", correctionNAME, "}"]).replace("Pi+", "#pi^{+}")).replace("Pi-", "#pi^{-}")).replace("Phi", "#phi"))
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
                                    sdf = CorDpp(rdf, correction, "".join(["Mom_", particle]), event_type, MM_type, datatype, Cuts if(Cuts == Calculated_Exclusive_Cuts or Cuts == CutChoice) else "")
                                else:
                                    sdf = CorDpp(rdf.Filter("".join([particle.replace("l", ""), "sec", " == ", str(sector)])), correction, "".join(["Mom_", particle]), event_type, MM_type, datatype, Cuts if(Cuts == Calculated_Exclusive_Cuts or Cuts == CutChoice) else "")

                                Histo_P_v_Phi[ref] = sdf.Histo2D((Histo_Mom_Phi_ref_title, Title_Mom_Phi, 110, 0, 11, 720, -260, 460), "".join([particle, "_", correction]), "".join([local_Q.replace(" ", ""), particle, "Phi", shift]))
                                count += 1
                                
                                if("" == shift and "" == local_Q):
                                    Histo_P_v_Th[ref] = sdf.Histo2D((Histo_Mom_The_ref_title, Title_Mom_The, 110, 0, 11, 150, 0, 40), "".join([particle, "_", correction]), "".join([particle, "th"]))
                                    count += 1
                                if('mm0' == correction):
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
                    print(type(Dmom_pip_Histo[saving_Dp_pip_name]))
                countSaved += 1

        if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
            for saving_Dp_pro_name in Dmom_pro_Histo:
                if(SaveResultsQ == 'yes'):
                    Dmom_pro_Histo[saving_Dp_pro_name].Write()
                elif(CheckDataFrameQ == "y"):
                    print("".join(["Dmom_pro_Histo[", str(saving_Dp_pro_name), "]"]))
                elif(Full_Crash_Check == "y"):
                    print(type(Dmom_pro_Histo[saving_Dp_pro_name]))
                countSaved += 1

        if('el' in Delta_P_histo_CompareList and Delta_Pel_histo_Q == 'y'):
            for saving_Dp_pel_name in Dmom_pel_Histo:
                if(SaveResultsQ == 'yes'):
                    Dmom_pel_Histo[saving_Dp_pel_name].Write()
                elif(CheckDataFrameQ == "y"):
                    print("".join(["Dmom_pel_Histo[", str(saving_Dp_pel_name), "]"]))
                elif(Full_Crash_Check == "y"):
                    print(type(Dmom_pel_Histo[saving_Dp_pel_name]))
                countSaved += 1

                
                
                
    # # # # # # # # # # # # # # # # # # # #    For the ∆Angle Histograms    # # # # # # # # # # # # # # # # # # # # 
                
        
        
    if(event_type == "ES"):
        for saving_DAngle_name in Dmom_Angle_Histo:
            if(SaveResultsQ == 'yes'):
                Dmom_Angle_Histo[saving_DAngle_name].Write()
            elif(CheckDataFrameQ == "y"):
                print("".join(["Dmom_Angle_Histo[", str(saving_DAngle_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print(type(Dmom_Angle_Histo[saving_DAngle_name]))
            countSaved += 1
            
            
            

    # # # # # # # # # # # # # # # # # # Second half of code (Missing Mass Histograms) # # # # # # # # # # # # # # # # # #

    if(Run_Missing_Mass_Histos == "yes"):
        for saving_MM_name in hmmCPARTall:
            if(SaveResultsQ == 'yes'):
                hmmCPARTall[saving_MM_name].Write()
            elif(CheckDataFrameQ == "y"):
                print("".join(["hmmCPARTall[", str(saving_MM_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print(type(hmmCPARTall[saving_MM_name]))
            countSaved += 1


    # # # # # # # # # # # # # # #   Other Phase Space Histograms (without Missing Mass)   # # # # # # # # # # # # # # #

    if(Run_Phase_Space == 'yes'):
        for saving_th_name in Histo_P_v_Th:
            if(SaveResultsQ == 'yes'):
                Histo_P_v_Th[saving_th_name].Write()
            elif(CheckDataFrameQ == "y"):
                print("".join(["Histo_P_v_Th[", str(saving_th_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print(type(Histo_P_v_Th[saving_th_name]))
            countSaved += 1

        for saving_Phi_name in Histo_P_v_Phi:
            if(SaveResultsQ == 'yes'):
                Histo_P_v_Phi[saving_Phi_name].Write()
            elif(CheckDataFrameQ == "y"):
                print("".join(["Histo_P_v_Phi[", str(saving_Phi_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print(type(Histo_P_v_Phi[saving_Phi_name]))
            countSaved += 1

        for saving_thPhi_name in Histo_Th_v_Phi:
            if(SaveResultsQ == 'yes'):
                Histo_Th_v_Phi[saving_thPhi_name].Write()
            elif(CheckDataFrameQ == "y"):
                print("".join(["Histo_Th_v_Phi[", str(saving_thPhi_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print(type(Histo_Th_v_Phi[saving_thPhi_name]))
            countSaved += 1

    # # # # # # # # # # # # # # # # # # # # #     Invariant Mass Histograms     # # # # # # # # # # # # # # # # # # # # #

    if(Run_Invariant_Mass_Histos == 'yes'):
        for saving_WM_name in HWC_Histo_All:
            if(SaveResultsQ == 'yes'):
                HWC_Histo_All[saving_WM_name].Write()
            elif(CheckDataFrameQ == "y"):
                print("".join(["HWC_Histo_All[", str(saving_WM_name), "]"]))
            elif(Full_Crash_Check == "y"):
                print(type(HWC_Histo_All[saving_WM_name]))
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
    5) MC -> Uses Monte Carlo Simulation for Single Pion Channel (i.e., same as SP but with simulated data)
    
Ending Code...
    """]))

