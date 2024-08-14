#!/usr/bin/env python3

import ROOT
import array
# from datetime import datetime
import numpy as np
import traceback
ROOT.gStyle.SetTitleOffset(1.3,'y')
ROOT.gStyle.SetGridColor(17)
ROOT.gStyle.SetPadGridX(1)
ROOT.gStyle.SetPadGridY(1)

ll, ll2 = ROOT.TLine(), ROOT.TLine()
ll.SetLineColor(2)
ll2.SetLineColor(1)

from Extra_Functions_for_Histo_Creation import *


##==========================================================================##
##==========##==========##     DATA RUN CHOICES     ##==========##==========##
##==========================================================================##

# Data_Run_List = ["Fall2018", "Spring2019_Pass1", "Spring2019_Pass2"]
# Data_Run_List = ["Fall2018"]
Data_Run_List = ["Fall2018_Pass2"]

# # Data_Run_List = ["Spring2019_Pass1", "Spring2019_Pass2"]
# # Data_Run_List = ["Spring2019_Pass1_Central", "Spring2019_Pass2_Central"]

# # Data_Run_List = ["Fall2018", "Spring2019_Pass2"]
# # Data_Run_List = ["Spring2019_Pass1"]
# Data_Run_List = ["Spring2019_Pass2"]

# # Data_Run_List = ["Fall2018_Pass2_Central"]
Data_Run_List = ["Fall2018_Pass2_Forward"]

# Data_Run_List = ["Monte_Carlo"]
# Data_Run_List = ["Monte_Carlo_Pass2"]

##==========================================================================##
##==========##==========##     DATA RUN CHOICES     ##==========##==========##
##==========================================================================##










##==========================================================================##
##==========##==========##    EVENT TYPE CHOICES    ##==========##==========##
##==========================================================================##

# EvntType_List = ["ES", "EO"]
# EvntType_List = ["SP", "EO"]
EvntType_List = ["EO", "SP"]
# EvntType_List = ["SP"]
# EvntType_List = ["DP", "P0"]
# EvntType_List = ["DP"]
# EvntType_List = ["P0"]
# EvntType_List = ["EO"]


##==========================================================================##
##==========##==========##    EVENT TYPE CHOICES    ##==========##==========##
##==========================================================================##










##==========================================================================##
##==========##==========##  IN/OUT-BENDING CHOICES  ##==========##==========##
##==========================================================================##

# Bending_Type_List = ["Inbending", "Outbending"]
# Bending_Type_List = ["Inbending"]
Bending_Type_List = ["Outbending"]

##==========================================================================##
##==========##==========##  IN/OUT-BENDING CHOICES  ##==========##==========##
##==========================================================================##





##==========================================================================##
##==========##==========##     PARTICLE CHOICES     ##==========##==========##
##==========================================================================##

# Particle_Mom_List = ['el', 'pro']
# Particle_Sec_List = ['el', 'pro']

Particle_Mom_List = ['el', 'pip']
Particle_Sec_List = ['el', 'pip']

# Particle_Mom_List = ['pip']
# Particle_Sec_List = ['pip']

# Particle_Mom_List = ['el']
# Particle_Sec_List = ['el']


# Particle_Mom_List = ['pro']
# Particle_Sec_List = ['pro']

# Particle_Mom_List = ['el', 'pro', 'pip']
# Particle_Sec_List = ['el', 'pro', 'pip']

##==========================================================================##
##==========##==========##     PARTICLE CHOICES     ##==========##==========##
##==========================================================================##



import argparse

# Create the parser with a description of the script
parser = argparse.ArgumentParser(description='Process some histograms.')

# Add a positional argument that is optional with help text
parser.add_argument('Histogram_Type_Option', nargs='?', choices=['MM', 'Dp', 'MM_el', 'Dp_el', 'MM_pip', 'Dp_pip', 'Out_MM', 'Out_Dp', 'Out_MM_el', 'Out_Dp_el', 'Out_MM_pip', 'Out_Dp_pip', 'In_MM', 'In_Dp', 'In_MM_el', 'In_Dp_el', 'In_MM_pip', 'In_Dp_pip'], help='Specify the histogram type (MM or Dp).')
# Parse the arguments
args = parser.parse_args()
# Access the argument
histogram_type = args.Histogram_Type_Option


if('In'   in str(histogram_type)):
    print(f"{color.BGREEN}\nInbending Files Selected\n{color.END}")
    Bending_Type_List = ["Inbending"]
if('Out'  in str(histogram_type)):
    print(f"{color.BGREEN}\nOutbending Files Selected\n{color.END}")
    Bending_Type_List = ["Outbending"]

if('el'   in str(histogram_type)):
    print(f"{color.BGREEN}\nElectron Particle option selected\n{color.END}")
    Particle_Mom_List = ['el']
    Particle_Sec_List = ['el']
    if(("Dp" in str(histogram_type)) and ("EO" not in EvntType_List)):
        EvntType_List = ["EO", "SP"]
if('pip'  in str(histogram_type)):
    print(f"{color.BGREEN}\nPi+ Pion Particle option selected\n{color.END}")
    Particle_Mom_List = ['pip']
    Particle_Sec_List = ['pip']
    if("EO" in EvntType_List):
        EvntType_List.remove("EO")



##==========================================================================##
##==========##==========##      SECTOR CHOICES      ##==========##==========##
##==========================================================================##

# Sector_Number_List = [0, 1, 2, 3, 4, 5, 6]
# Sector_Number_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Sector_Number_List = [1, 2, 3, 4, 5, 6]
# Sector_Number_List = [0]


# Sector_Number_List = [0, 7, 8, 9, 10, 11, 12]

if("pip" not in Particle_Mom_List):
    for central_sec in [7, 8, 9, 10, 11, 12]:
        if(central_sec in Sector_Number_List):
            Sector_Number_List.remove(central_sec)

##==========================================================================##
##==========##==========##      SECTOR CHOICES      ##==========##==========##
##==========================================================================##





##==========================================================================##
##==========##==========##    CORRECTION CHOICES    ##==========##==========##
##==========================================================================##

Correction_Name_List = ["mm0", "mm0_ELPipMM0"]
Correction_Name_List = ["mm0_ELPipMM0", "mmfaP2_ELPipMM0"]
Correction_Name_List = ["mmfaP2_ELPipMM0"]
Correction_Name_List = ["mmfaP2_ELPipMM0", "mmfaP2_ELPipMMfaP2"]
Correction_Name_List = ["mmfaP2_ELPipMMfaP2"]
Correction_Name_List = ["mm0", "mm0_ELPipMM0", "mmfaP2", "mmfaP2_ELPipMM0", "mmfaP2_ELPipMMfaP2"]
# Correction_Name_List = ["mmfaP2_ELPipMM0"]
# Correction_Name_List = ["mmfaP2", "mmfaP2_ELPipMMfaP2"]
Correction_Name_List = ["mm0"]
Correction_Name_List = ["mmfaP2"]
# Correction_Name_List = ["mm0", "mm0_ELPipMM0", "mmfaP2_ELPipMM0", "mmfaP2_ELPipMMfaP2"]
Correction_Name_List = ["mmfaP2", "mmfaP2_ELPipMM0"]
Correction_Name_List = ["mmfaP2_ELPipMMfaP2"]
Correction_Name_List = ["mmfaP2", "mmfaP2_ELPipMMfaP2"]

##==========================================================================##
##==========##==========##    CORRECTION CHOICES    ##==========##==========##
##==========================================================================##





##==========================================================================##
##==========##==========##  REGION/BINNING CHOICES  ##==========##==========##
##==========================================================================##

Binning_Option_List = [1, 3]
# Binning_Option_List = [1]
# Binning_Option_List = [3]
Region_Option_List = ['regall', 'reg1', 'reg2', 'reg3']
# Region_Option_List = ['regall']

# Region_Option_List = ['reg1', 'reg2', 'reg3']
# Region_Option_List = ['reg1', 'reg2']
# Region_Option_List = ['reg1']

##==========================================================================##
##==========##==========##  REGION/BINNING CHOICES  ##==========##==========##
##==========================================================================##





##==========================================================================##
##==========##==========##      ∆ANGLE CHOICES      ##==========##==========##
##==========================================================================##

# D_Angle_Type = ["D_Angle_V1", "D_Angle_V2", "D_Angle_V3", "D_Angle_V4"]

D_Angle_Type = ["D_Angle_V1", "D_Angle_V3"]

# D_Angle_Type = ["D_Angle_V1"]
# D_Angle_Type = ["D_Angle_V3"]

# D_Angle_Type = ["D_Angle_V1", "D_Angle_V2", "D_Angle_V3"]

##==========================================================================##
##==========##==========##      ∆ANGLE CHOICES      ##==========##==========##
##==========================================================================##





##=========================================================================##
##==========##==========##       CUT CHOICES       ##==========##==========##
##=========================================================================##

Extra_Cut_Option = [""]
# # Extra_Cut_Option = ["", "Corrected (Full) Missing Mass Squared Cut"]
Extra_Cut_Option = ["Calculated Exclusivity Cuts"]
# Extra_Cut_Option = ["", "Calculated Exclusivity Cuts"]

##=========================================================================##
##==========##==========##       CUT CHOICES       ##==========##==========##
##=========================================================================##





################================================#############################================================################
##============##================================##=========================##================================##============##
##=====##=====##===============##===============##    HISTOGRAM CHOICES    ##===============##===============##=====##=====##
##============##================================##=========================##================================##============##
################================================#############################================================################


List_of_Locate_name = []


##==========================================================================##
##==========##==========##       MISSING MASS       ##==========##==========##
##==========================================================================##

if("SP" in EvntType_List or "DP" in EvntType_List or ("P0" in EvntType_List or "P0_MC" in EvntType_List)):
    print(f"{color.BOLD}Missing Mass plots are available...{color.END}")
    # List_of_Locate_name.append("hmmCPARTall_('Correction_Name_List', Sector_Number_List, '', 'Binning_Option_List', 'Region_Option_List', 'Particle_Mom_List', 'Particle_Sec_List'")
    # # List_of_Locate_name.append("hmmCPARTall_('Correction_Name_List', Sector_Number_List, '', 'Binning_Option_List', 'Region_Option_List', 'Particle_Mom_List', 'Particle_Sec_List'")
    List_of_Locate_name.append("hmmCPARTall_('Correction_Name_List', Sector_Number_List, '', 'Binning_Option_List', 'Region_Option_List', 'Particle_Mom_List', 'Particle_Sec_List', '')")
    # List_of_Locate_name.append("hmmCPARTall_('Correction_Name_List', Sector_Number_List, '', 'Binning_Option_List', 'Region_Option_List', 'Particle_Mom_List', 'Particle_Sec_List', 'Calculated Exclusivity Cuts')")
    # List_of_Locate_name.append("hmmCPARTall_('Correction_Name_List', Sector_Number_List, '', '3', 'Region_Option_List', 'Particle_Mom_List', 'Particle_Sec_List', '')")

##==========================================================================##
##==========##==========##       MISSING MASS       ##==========##==========##
##==========================================================================##





##==========================================================================##
##==========##==========##      INVARIANT MASS      ##==========##==========##
##==========================================================================##


# # List_of_Locate_name.append("HWC_Histo_All_('Correction_Name_List', Sector_Number_List, 'Binning_Option_List', 'Region_Option_List', 'Particle_Mom_List', 'Particle_Sec_List', 'Extra_Cut_Option'")
# # List_of_Locate_name.append("HWC_Histo_All_('Correction_Name_List', Sector_Number_List, '1', 'regall', 'Particle_Mom_List', 'Particle_Sec_List', 'Extra_Cut_Option'")
# List_of_Locate_name.append("HWC_Histo_All_('Correction_Name_List', Sector_Number_List, '1', 'regall', 'Particle_Mom_List', 'Particle_Sec_List', ''")

##==========================================================================##
##==========##==========##      INVARIANT MASS      ##==========##==========##
##==========================================================================##





##==========================================================================##
##==========##==========##         ∆ ANGLES         ##==========##==========##
##==========================================================================##

if("ES" in EvntType_List):
    print(f"{color.BOLD}\n∆ Angles are available...{color.END}")
#     List_of_Locate_name.append("Dmom_Angle_Histo('Correction_Name_List', '', 'El Sector Sector_Number_List', 'Binning_Option_List', 'Region_Option_List', 'Extra_Cut_Option', 'D_Angle_Type'")

##==========================================================================##
##==========##==========##         ∆ ANGLES         ##==========##==========##
##==========================================================================##





##==========================================================================##
##==========##==========##        ∆ MOMENTUM        ##==========##==========##
##==========================================================================##


if("el" in Particle_Mom_List):
    print(f"{color.BOLD}\nElectron Corrections available...{color.END}")
#     List_of_Locate_name.append("Dmom_pel_Histo('Correction_Name_List', '', 'El Sector Sector_Number_List', '1', 'regall', 'Extra_Cut_Option'")
#     List_of_Locate_name.append("Dmom_pel_Histo('Correction_Name_List', '', 'El Sector Sector_Number_List', 'Binning_Option_List', 'Region_Option_List', 'Extra_Cut_Option'")
    List_of_Locate_name.append("Dmom_pel_Histo('Correction_Name_List', '', 'El Sector Sector_Number_List', '1', 'regall', 'Binning_Option_List', 'Region_Option_List', 'Extra_Cut_Option'")
    
    
if("pip" in Particle_Mom_List):
    print(f"{color.BOLD}\nPi+ Corrections available...{color.END}")
    List_of_Locate_name.append("Dmom_pip_Histo('Correction_Name_List', '', 'Pi+ Sector Sector_Number_List', 'Binning_Option_List', 'Region_Option_List', 'Extra_Cut_Option'")

    
if("pro" in Particle_Mom_List):
    print(f"{color.BOLD}\nProton Corrections available...{color.END}")
#     List_of_Locate_name.append("Dmom_pro_Histo('Correction_Name_List', '', 'Pro Sector Sector_Number_List', 'Binning_Option_List', 'Region_Option_List', 'Extra_Cut_Option'")
# #     List_of_Locate_name.append("Dmom_pro_Histo('Correction_Name_List', '', 'Pro Sector Sector_Number_List', 'Binning_Option_List', 'Region_Option_List', ''")


##==========================================================================##
##==========##==========##        ∆ MOMENTUM        ##==========##==========##
##==========================================================================##


if('MM'   in str(histogram_type)):
    print(f"\n{color.BGREEN}Missing Mass Histogram(s) option selected{color.END}")
    List_of_Locate_name = ["hmmCPARTall_('Correction_Name_List', Sector_Number_List, '', 'Binning_Option_List', 'Region_Option_List', 'Particle_Mom_List', 'Particle_Sec_List', '')"]
    if("EO" in EvntType_List):
        EvntType_List.remove("EO")
elif('Dp' in str(histogram_type)):
    print(f"\n{color.BGREEN}∆P Histogram(s) option selected{color.END}")
    if("el" in Particle_Mom_List):
        List_of_Locate_name = ["Dmom_pel_Histo('Correction_Name_List', '', 'El Sector Sector_Number_List', '1', 'regall', 'Binning_Option_List', 'Region_Option_List', 'Extra_Cut_Option'"]
    if("pip" in Particle_Mom_List):
        List_of_Locate_name = ["Dmom_pip_Histo('Correction_Name_List', '', 'Pi+ Sector Sector_Number_List', 'Binning_Option_List', 'Region_Option_List', 'Extra_Cut_Option'"]




##==========================================================================##
##==========##==========##          OTHERS          ##==========##==========##
##==========================================================================##

# # List_of_Locate_name.append("Histo_P_v_Th_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', '')")
# # # List_of_Locate_name.append("Histo_P_v_Th_('Correction_Name_List', 0, 'Particle_Mom_List', 'Extra_Cut_Option', '', '')")
# # # List_of_Locate_name.append("Histo_P_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', ''")
# # # List_of_Locate_name.append("Histo_P_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', 'S'")

# # # List_of_Locate_name.append("Histo_P_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', 'local', ''")
# # List_of_Locate_name.append("Histo_P_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', 'local', 'S'")

# # # List_of_Locate_name.append("Histo_P_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', ''")
# # # List_of_Locate_name.append("Histo_P_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', 'S'")
# # # List_of_Locate_name.append("Histo_P_v_Phi_('Correction_Name_List', 0, 'Particle_Mom_List', 'Extra_Cut_Option', 'local', 'S')")
# # # List_of_Locate_name.append("Histo_P_v_Phi_('Correction_Name_List', 0, 'Particle_Mom_List', 'Extra_Cut_Option', '', '')")
# # # List_of_Locate_name.append("Histo_P_v_Phi_('Correction_Name_List', 0, 'Particle_Mom_List', 'Extra_Cut_Option', '', 'S')")
# # # # List_of_Locate_name.append("Histo_P_v_Phi_('Correction_Name_List', 0, 'Particle_Mom_List', 'Extra_Cut_Option', 'local', '')")
# # # # List_of_Locate_name.append("Histo_Th_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', '')")
# # # # List_of_Locate_name.append("Histo_Th_v_Phi_('Correction_Name_List', 0, 'Particle_Mom_List', 'Extra_Cut_Option', '', '')")
# # # List_of_Locate_name.append("Histo_Th_v_Phi_('Correction_Name_List', 0, 'Particle_Mom_List', 'Extra_Cut_Option', 'local', 'S')")
# # # # List_of_Locate_name.append("Histo_Th_v_Phi_('Correction_Name_List', 0, 'Particle_Mom_List', 'Extra_Cut_Option', 'local', '')")

# # List_of_Locate_name.append("Histo_Th_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', 'local', 'S'")
# # # List_of_Locate_name.append("Histo_Th_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', 'local', ''")

# # # List_of_Locate_name.append("Histo_Th_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', 'S'")
# # # List_of_Locate_name.append("Histo_Th_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', ''")


# # List_of_Locate_name.append("Histo_P_v_Th_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', '')")
# List_of_Locate_name.append("Histo_P_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', ''")
# List_of_Locate_name.append("Histo_P_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', 'local', ''")
# List_of_Locate_name.append("Histo_P_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', 'S'")
# List_of_Locate_name.append("Histo_Th_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', ''")
# List_of_Locate_name.append("Histo_Th_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', 'local', ''")
# List_of_Locate_name.append("Histo_Th_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', 'S'")

# List_of_Locate_name.append("Histo_P_v_Th_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', '')")
# List_of_Locate_name.append("Histo_P_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', 'local', 'S'")
# List_of_Locate_name.append("Histo_Th_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', 'local', 'S'")
##==========================================================================##
##==========##==========##          OTHERS          ##==========##==========##
##==========================================================================##





##==========================================================================##
##==========##==========##         DEFAULTS         ##==========##==========##
##==========================================================================##


# List_of_Locate_name = ["Dmom_pel_Histo('Correction_Name_List', '', 'El Sector Sector_Number_List', 'Binning_Option_List', 'Region_Option_List', 'Extra_Cut_Option'"]

# # List_of_Locate_name = ["Dmom_pel_Histo('Correction_Name_List', '', 'El Sector Sector_Number_List', '1', 'regall', 'Extra_Cut_Option')", "HWC_Histo_All_('Correction_Name_List', Sector_Number_List, 'Binning_Option_List', 'Region_Option_List', 'Particle_Mom_List', 'Particle_Sec_List', 'Extra_Cut_Option'"]


# # # List_of_Locate_name = ["hPARTthall_Particle_Mom_ListthallSecSector_Number_ListS_Correction_Name_List"]

# List_of_Locate_name = ["Histo_P_v_Th_('Correction_Name_List', 0, 'Particle_Mom_List', 'Extra_Cut_Option', '', '')"]
# List_of_Locate_name = ["Histo_P_v_Th_"]

# # All (Main) Options:
# List_of_Locate_name = ["Dmom_pel_Histo('Correction_Name_List', '', 'El Sector Sector_Number_List', '1', 'regall', 'Extra_Cut_Option')", "HWC_Histo_All_('Correction_Name_List', Sector_Number_List, 'Binning_Option_List', 'Region_Option_List', 'Particle_Mom_List', 'Particle_Sec_List', 'Extra_Cut_Option'", "Histo_P_v_Phi_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', ''", "Histo_P_v_Th_('Correction_Name_List', Sector_Number_List, 'Particle_Mom_List', 'Extra_Cut_Option', '', '')"]
# List_of_Locate_name = ["Dmom_pel_Histo('Correction_Name_List', '', 'El Sector Sector_Number_List', '1', 'regall', 'Extra_Cut_Option')", "HWC_Histo_All_('Correction_Name_List', Sector_Number_List, 'Binning_Option_List', 'Region_Option_List', 'Particle_Mom_List', 'Particle_Sec_List', 'Extra_Cut_Option'", "Histo_P_v_Phi_('Correction_Name_List', 0, 'Particle_Mom_List', 'Extra_Cut_Option', '', ''", "Histo_P_v_Th_('Correction_Name_List', 0, 'Particle_Mom_List', 'Extra_Cut_Option', '', '')"]


# List_of_Locate_name = ["Dmom_pel_Histo('Correction_Name_List', '', 'El Sector Sector_Number_List', 'Binning_Option_List', 'Region_Option_List', 'Extra_Cut_Option'"]
# List_of_Locate_name = ["Dmom_pel_Histo('Correction_Name_List', '', 'El Sector Sector_Number_List', '1', 'regall', 'Binning_Option_List', 'Region_Option_List', 'Extra_Cut_Option'"]
# List_of_Locate_name = ["Dmom_pel_Histo('Correction_Name_List', '', 'El Sector Sector_Number_List', 'Binning_Option_List', 'Region_Option_List', 'Extra_Cut_Option'", "Dmom_pel_Histo('Correction_Name_List', '', 'El Sector Sector_Number_List', '1', 'regall', 'Binning_Option_List', 'Region_Option_List', 'Extra_Cut_Option'"]



# List_of_Locate_name = ["hmmCPARTall_('Correction_Name_List', Sector_Number_List, '', 'Binning_Option_List', 'Region_Option_List', 'Particle_Mom_List', 'Particle_Sec_List', '')"]
# List_of_Locate_name.append("Dmom_pel_Histo('Correction_Name_List', '', 'El Sector Sector_Number_List', '1', 'regall', 'Binning_Option_List', 'Region_Option_List', 'Extra_Cut_Option'")
    
# List_of_Locate_name = ["Dmom_pro_Histo"]


print("".join(["\n\nWill be running data for:\n", color.BOLD, "In/Out-Bending Options:", color.BLUE, "\n\t(*)\t", "\n\t(*)\t".join(Bending_Type_List), color.END_B, "\nEvent Types:", color.BLUE, "\n\t(*)\t", "\n\t(*)\t".join(EvntType_List), color.END_B, "\nData Sets to be used:", color.BLUE, "\n\t(*)\t", "\n\t(*)\t".join(Data_Run_List), color.END]))

print("".join([color.BOLD, "Corrections to be used:", color.END]))
for cor in Correction_Name_List:
    # print("".join([color.BBLUE, "\t(*)\t", corNameTitles(str(cor)), color.END]))
    print("".join([color.BBLUE, "\t(*)\t", corNameTitles(str(cor), Form="Default", EVENT_TYPE="SP" if("SP" in EvntType_List) else EvntType_List[0], BENDING_TYPE=Bending_Type_List[0]), color.END]))
    
print("".join([color.BOLD, "Additional Cuts to be used:", color.END]))
for cut in Extra_Cut_Option:
    print("".join([color.BBLUE, "\t(*)\t ", str(cut) if(cut != "") else "".join(["''", color.END, color.BLUE, "\t(a.k.a., No Additional Cuts Applied)"]), color.END]))

print("".join([color.BOLD, "Type(s) of Phi Binning in (potential) use:", color.END]))
if(1 in Binning_Option_List and "regall" in Region_Option_List):
    print("".join([color.BBLUE, "\t(*)\tWill include the Integrated Phi Bin", color.END, color.BLUE, " (regall - also may be required to plot the individual phi bins together)", color.END]))
if(3 in Binning_Option_List and "reg1" in Region_Option_List):
    print("".join([color.BBLUE, "\t(*)\tWill include the    Central Phi Bin", color.END, color.BLUE, " (reg1)", color.END]))
if(3 in Binning_Option_List and "reg2" in Region_Option_List):
    print("".join([color.BBLUE, "\t(*)\tWill include the   Negative Phi Bin", color.END, color.BLUE, " (reg2)", color.END]))
if(3 in Binning_Option_List and "reg3" in Region_Option_List):
    print("".join([color.BBLUE, "\t(*)\tWill include the   Positive Phi Bin", color.END, color.BLUE, " (reg3)", color.END]))
if(3 not in Binning_Option_List and ("reg1" in Region_Option_List or "reg2" in Region_Option_List or "reg3" in Region_Option_List)):
    print("".join([color.Error, "\tPossible Error: ", color.END_R, "To make plots with different phi bins, the Binning_Option_List must include 3.", color.BOLD, "\n\tSuggestion: ", color.END_R, "Either adjust the contents of Binning_Option_List or Region_Option_List to run this code more efficiently.", color.END]))
if(1 not in Binning_Option_List and ("regall" in Region_Option_List)):
    print("".join([color.Error, "\tPossible Error: ", color.END_R, "To make plots without phi bins (i.e., with an integrated phi bin), the Binning_Option_List must include 1.", color.BOLD, "\n\tSuggestion: ", color.END_R, "Either adjust the contents of Binning_Option_List or Region_Option_List to run this code more efficiently.", color.END]))

print("".join([color.BOLD, "Sectors to be used:", color.END]))
if([1, 2, 3, 4, 5, 6] == sorted(Sector_Number_List) or [0, 1, 2, 3, 4, 5, 6] == sorted(Sector_Number_List)):
    print("".join([color.BBLUE, "\t(*)\tAll (Default) Sectors in use", color.END, "".join([color.BLUE, " (Including the combined sector plots)", color.END]) if(0 in Sector_Number_List) else ""]))
else:
    for sec in Sector_Number_List:
        print("".join([color.BBLUE, "\t(*)\t ", "".join(["Sector ", str(sec)]) if(sec != 0) else "All Sectors (Together)", color.END]))
print("\n")

print("".join([color.BGREEN, "Choices Selected...", color.END_B, "\n\nHistograms included are:\n", color.END]))
if(List_of_Locate_name == []):
    print(f"{color.RED}NONE{color.END}")
else:
    for ii in List_of_Locate_name:
        print(f"\t(*) {str(ii)}\n")

        
        
        
