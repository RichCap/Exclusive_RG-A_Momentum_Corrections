#!/usr/bin/env python3

import ROOT
import numpy as np
import traceback

from CommonPythonFunctions import *


# Inbending or Outbending files?
Selection_of_In_or_Out = "Inbending"
# Selection_of_In_or_Out = "Outbending"

# Data set from RG-A (Spring data may not be currently compatible - need to rerun)
# Selection_Data_Set = "Fall2018"

Selection_Data_Set = "Fall2018_Pass2_Forward"
# Selection_Data_Set = "Fall2018_Pass2"

# Selection_Data_Set = "Fall2018_Pass2_Central"
# Selection_Data_Set = "Spring2019"
# Selection_Data_Set = "Spring2019_Pass1"
# Selection_Data_Set = "Spring2019_Pass2"
# # Selection_Data_Set = "Monte Carlo"

# Selection_Data_Set = "Monte_Carlo"

# Selection_Data_Set = "Monte_Carlo_Pass2"

# Selection_Data_Set = "Spring2019_Pass1_Central"
# Selection_Data_Set = "Spring2019_Pass2_Central"


# Type of exclusive event
event_type = "SP" # Single Pion Channel (ep->eπ+N)
# event_type = "DP" # Double Pion Channel (ep->epπ+π- --- also uses the π0 channel for the ∆P histograms)
# event_type = "P0" # π0 Channel (ep->epπ0)
# event_type = "ES" # Elastic Scattering Channel (ep->e'p')
# event_type = "EO" # Electron Only Channel (ep->e'X)

MM_type = "epipX" # Use for single pion channel (select with event_type = "SP")
# MM_type = "eppipX" # Use for double pion channel (select with event_type = "DP")
# MM_type = "eppi0X" # Use for π0 channel (select with event_type = "P0")
# MM_type = "epX" # Use for elastic scattering channel (select with event_type = "ES")
# MM_type = "eX" # Use for electron only channel (select with event_type = "EO")

print("".join(["\nStarting ", MM_type if("E" not in event_type) else "Elastic Scattering" if(event_type == "ES") else "Electron Only", " (", str(Selection_of_In_or_Out), ") Corrections (from RG-A ", str(Selection_Data_Set.replace("20", " 20")).replace("_", " "), ")...\n"]))





# Setting SaveResultsQ = 'yes' will cause this code to save the images produced as .png files in its local directory
# Setting SaveResultsQ = 'no' will let the code run normally but will not individually same any of the images
SaveResultsQ = 'yes'
# SaveResultsQ = 'no'
print("".join(["\nSaving results? ", color.BOLD, str(SaveResultsQ), color.END, "\n"]))




# print_method = "ver"
print_method = "hor"
if(print_method not in ["hor"]):
    print("".join(["\nSaving Vertically or Horizontally? ", color.BOLD, "Vertically" if(print_method == "ver") else "Horizontally", color.END, "\n"]))
# print_method decides which orientation the plots will be drawn in (not affected by the choice to save)






# For file: 'Mom_Cors_Main_python.py'
CheckDataFrameQ2 = 'n'
CheckDataFrameQ2 = 'y' # Used for searching with List_of_Locate_name (see below)
# CheckDataFrameQ2 = 'yf' # Prints full list of available histograms
# CheckDataFrameQ2 = 'ys' # Prints a reduced list of available histograms (same list as would be drawn if option 'y' was chosen)





















# Run with ∆p? (This option is to make sure that the ∆p histograms are only run when the file is known to have that information available - Just a small safety measure to prevent some crashes)
RunDpQ = 'yes'
# RunDpQ = 'no'


def DataFrame_Find(Event_Type=event_type, In_or_Out=Selection_of_In_or_Out, Selection_Data_Set_In=Selection_Data_Set, MC_Test="Norm"):
    
    general_batch_file_location, file_name = "error", "error"
    
    # main_location = "/w/hallb-scshelf2102/clas12/richcap/Exclusive_RG-A_Momentum_Corrections/Data_Files/"
    main_location = "../Data_Files/" # This is more compatible with the version of the code that is run when downloading the git repository
    
    if("Fall2018"  in Selection_Data_Set_In):
        if("Pass2" in Selection_Data_Set_In):
            if(Event_Type == "SP"):
                if("Out" in In_or_Out):
                    Extra_Part_of_Name     = "_Central_Fall_Pass2_V1"
                    Extra_Part_of_Name     = "_Fall_Pass2_V1"
                    Extra_Part_of_Name     = "_Forward_Fall_Pass2_V1"
                    Extra_Part_of_Name     = "".join(["_Forward" if("Forward" in Selection_Data_Set_In) else "_Central" if("Central" in Selection_Data_Set_In) else "", "_Fall_Pass2_V4"])
                    Extra_Part_of_Name     = Extra_Part_of_Name.replace("Fall_Pass2_V4", "Shift_Test_V4")
                    Extra_Part_of_Name     = "".join(["_Forward" if("Forward" in Selection_Data_Set_In) else "_Central" if("Central" in Selection_Data_Set_In) else "", "_Fall2018_P2_New_Out_V20"])
                else:
                    Extra_Part_of_Name     = "".join(["_Forward" if("Forward" in Selection_Data_Set_In) else "_Central" if("Central" in Selection_Data_Set_In) else "", "_In_Forward_Test_V1"])
                    Extra_Part_of_Name     = "".join(["_Forward" if("Forward" in Selection_Data_Set_In) else "_Central" if("Central" in Selection_Data_Set_In) else "", "_Fall2018_P2_Test_V9"])
                    # Extra_Part_of_Name     = "".join(["_Forward" if("Forward" in Selection_Data_Set_In) else "_Central" if("Central" in Selection_Data_Set_In) else "", "_Fall2018_P2_Test_V6"])
                    
                    Extra_Part_of_Name     = "".join(["_Forward" if("Forward" in Selection_Data_Set_In) else "_Central" if("Central" in Selection_Data_Set_In) else "", "_Fall2018_P2_In_Refine_V6"])

                general_batch_file_location = "".join([str(main_location), "Single_Pion_Channel_epipN/Pass2/", str(In_or_Out), "/"])
                file_name                   = "".join([                    "Single_Pion_Channel_epipX_",       str(In_or_Out), "_With_Dp", str(Extra_Part_of_Name), "_File_All.root"])
            if(Event_Type == "EO"):
                if("Out" in In_or_Out):
                    Extra_Part_of_Name     = "_Central_Fall_Pass2_V1"
                    Extra_Part_of_Name     = "_Fall_Pass2_V1"
                    Extra_Part_of_Name     = "_Forward_Fall_Pass2_V1"

                    Extra_Part_of_Name     = "".join(["_Forward" if("Forward" in Selection_Data_Set_In) else "_Central" if("Central" in Selection_Data_Set_In) else "", "_Fall_Pass2_V4"])

                    Extra_Part_of_Name     = Extra_Part_of_Name.replace("Fall_Pass2_V4", "Shift_Test_V1")
                    Extra_Part_of_Name     = "_Fall2018_P2_New_Out_V17"
                else:
                    Extra_Part_of_Name     = "".join(["_Forward" if("Forward" in Selection_Data_Set_In) else "_Central" if("Central" in Selection_Data_Set_In) else "", "_In_Forward_Test_V1"])
                    Extra_Part_of_Name     = "".join(["_Forward" if("Forward" in Selection_Data_Set_In) else "_Central" if("Central" in Selection_Data_Set_In) else "", "_Fall2018_P2_Test_V8"])
                    # Extra_Part_of_Name     = "".join(["_Forward" if("Forward" in Selection_Data_Set_In) else "_Central" if("Central" in Selection_Data_Set_In) else "", "_Fall2018_P2_Test_V4"])
                    
                    Extra_Part_of_Name     = "".join(["_Forward" if("Forward" in Selection_Data_Set_In) else "_Central" if("Central" in Selection_Data_Set_In) else "", "_Fall2018_P2_In_Refine_V6"])

                general_batch_file_location = "".join([str(main_location), "Only_Electron_Channel/Pass2/",      str(In_or_Out), "/"])
                file_name                   = "".join([                    "Electron_Only_eX_",                 str(In_or_Out), "_With_Dp", str(Extra_Part_of_Name), "_File_All.root"])
                
        else:
            if(Event_Type == "SP"):
                # Extra_Part_of_Name     = "_GitHub_SP_New_W"
                # Extra_Part_of_Name     = "_GitHub_Electron_Refinement_V6"
                Extra_Part_of_Name     = "_GitHub_Pion_Refinement_V4"
    #             Extra_Part_of_Name     = "_Pass1_Final_Tests_V1"


                if("Out" in In_or_Out):
                    Extra_Part_of_Name = "_New_Extended_Out_V2"
                    Extra_Part_of_Name = "_New_Extended_El_Cor_V9"
                    Extra_Part_of_Name = "_New_Pip_Cor_V3"
                    Extra_Part_of_Name = "_New_Final_El_Cor_V1"
                    Extra_Part_of_Name = "_New_Final_Pip_Cor_V2"
                    Extra_Part_of_Name = "_New_Final_El_Cor_V4"
                    Extra_Part_of_Name = "_Final_Outbending"

                # general_batch_file_location = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Single_Pion_Channel_epipN/", str(In_or_Out), "/"])
                general_batch_file_location = "".join([str(main_location), "Single_Pion_Channel_epipN/",           str(In_or_Out), "/"])
                file_name                   = "".join([                    "Single_Pion_Channel_epipX_",           str(In_or_Out), "_With_Dp", str(Extra_Part_of_Name), "_File_All.root"])

            if(Event_Type == "MC"):
                Extra_Part_of_Name     = "_GitHub_MC_Test_V1"

                if("Out" in In_or_Out):
                    Extra_Part_of_Name = "_New_Extended_Out_V1"

                # general_batch_file_location = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Monte_Carlo_SIDIS/"
                general_batch_file_location = "".join([str(main_location),     "Monte_Carlo_SIDIS/"])
                
                if("Pass2" in Selection_Data_Set_In):
                    general_batch_file_location = "".join([str(main_location), "Monte_Carlo_SIDIS/Pass2/"])
                    Extra_Part_of_Name = "_Fa18_P2_MC_V2"
                file_name                   = "".join([                        "Simulated_Single_Pion_Channel_epipX_", str(In_or_Out), "_With_Dp", str(Extra_Part_of_Name), "_File_All.root"])

            if("P0" in Event_Type):
                Extra_Part_of_Name = "MC_Testing_Normal_V2"
                Extra_Part_of_Name = "MC_Testing_Plus_V2"
                # Extra_Part_of_Name = "MC_Testing_Minus_V2"
                Extra_Part_of_Name = "MC_Testing_Normal_V9" if(MC_Test in ["Norm"]) else "MC_Testing_Plus_V2" if(MC_Test in ["Plus"]) else "MC_Testing_Minus_V2"

                general_batch_file_location = "/w/hallb-scshelf2102/clas12/richcap/Exclusive_RG-A_Momentum_Corrections/Data_Files/Pi0_Channel_eppi0/Inbending/Simulated_Pi0/"
                file_name                   = "".join(["Pi0_Channel_eppi0X_Inbending_With_Dp_", str(Extra_Part_of_Name), ".root"])
                file_name                   = "".join(["Pi0_Channel_epX_Inbending_With_Dp_",    str(Extra_Part_of_Name), ".root"])

    #         if("E" not in Event_Type and Event_Type not in ["SP", "MC"]):          
            if("E" not in Event_Type and Event_Type not in ["SP", "MC", "P0"]):
                # Inbending_Version = "_VFinal_SP_V8_Pro"
                # Outbending_Version = "_VFinal_SP_V5_Pro"

                Inbending_Version  = "_GitHub_F2_Pro"
                Outbending_Version = "_GitHub_F2_Pro"

                Inbending_Version  = "_New_Proton_Refinement_V3"
    #             Inbending_Version = "_GitHub_Cut_Check_V1"
    #             Inbending_Version = "_Proton_Testing_V1_Failed"
                Outbending_Version = "_GitHub_Proton_Refinement_V2"


                # batch_pi0_file_location = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Pi0_Channel_eppi0/", str(In_or_Out), "/"])
                # batch_2pion_file_location = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Double_Pion_Channel_eppippim/", str(In_or_Out), "/"])

                # batch_pi0_file_location = "".join(["/lustre19/expphy/volatile/clas12/richcap/Exclusive_RG-A_Momentum_Corrections/Data_Files/Pi0_Channel_eppi0/", str(In_or_Out), "/"])
                # batch_2pion_file_location = "".join(["/lustre19/expphy/volatile/clas12/richcap/Exclusive_RG-A_Momentum_Corrections/Data_Files/Double_Pion_Channel_eppippim/", str(In_or_Out), "/"])

                batch_pi0_file_location   = "".join([str(main_location), "Pi0_Channel_eppi0/",           str(In_or_Out), "/"])
                batch_2pion_file_location = "".join([str(main_location), "Double_Pion_Channel_eppippim/", str(In_or_Out), "/"])

                file_name_pi0   = "".join(["Pi0_Channel_eppi0X_",         str(In_or_Out), "_With_Dp", str(Inbending_Version) if("In" in In_or_Out) else str(Outbending_Version), ".root"])
                # file_name_2pion = "".join(["Double_Pion_Channel_eppipX_", str(In_or_Out), "_With_Dp", str(Inbending_Version) if("In" in In_or_Out) else str(Outbending_Version) , "_File_Most.root"])
                file_name_2pion = "".join(["Double_Pion_Channel_eppipX_", str(In_or_Out), "_With_Dp", str(Inbending_Version) if("In" in In_or_Out) else str(Outbending_Version) , "_File_All.root"])


                if(Event_Type == "DP"):
                    general_batch_file_location = batch_2pion_file_location
                    file_name                   = file_name_2pion

                if(Event_Type == "P0"):
                    general_batch_file_location = batch_pi0_file_location
                    file_name                   = file_name_pi0

            if("ES" == Event_Type):
                # Extra_Part_of_Name = "_GitHub_Elastic_V3"
                # Extra_Part_of_Name = "_GitHub_Elastic_CD_V1"
                # Extra_Part_of_Name = "_GitHub_Valerii_V5"
                # Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V9"
                # Extra_Part_of_Name = "_GitHub_Cut_Tests_V6"
                Extra_Part_of_Name = "_GitHub_Electron_Refinement_V1"

                if("Out" in In_or_Out):
                    Extra_Part_of_Name = "_New_Extended_Out_V1"


                # general_batch_file_location = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Elastic_Scattering_Channel_ep/", str(In_or_Out), "/"])
                general_batch_file_location = "".join([str(main_location), "Elastic_Scattering_Channel_ep/", str(In_or_Out), "/"])
                file_name                   = "".join([                    "Elastic_Scattering_epX_",        str(In_or_Out), "_With_Dp", str(Extra_Part_of_Name), "_File_All.root"])

            if("EO" == Event_Type):
                Extra_Part_of_Name     = "_GitHub_Cut_Tests_V6"
                Extra_Part_of_Name     = "_GitHub_Electron_Refinement_V6"

                if("Out" in In_or_Out):
                    Extra_Part_of_Name = "_New_Extended_Out_V5"
                    Extra_Part_of_Name = "_New_Extended_El_Cor_V9"
                    Extra_Part_of_Name = "_New_Final_El_Cor_V1"
                    Extra_Part_of_Name = "_New_Final_El_Cor_V4"

                # general_batch_file_location = "".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Only_Electron_Channel/", str(In_or_Out), "/"])
                general_batch_file_location = "".join([str(main_location), "Only_Electron_Channel/", str(In_or_Out), "/"])
                file_name                   = "".join([                    "Electron_Only_eX_",      str(In_or_Out), "_With_Dp", str(Extra_Part_of_Name), "_File_All.root"])




    if("Spring2019" in Selection_Data_Set_In):
        general_batch_file_location = "/lustre19/expphy/volatile/clas12/richcap/Summer2021/jupyter/Batch_Code/Data_Files/Spring2019/Root_Histogram_Creation/"
        file_name                   = "epipX_Inbending_With_Dp_Spring2019_File_ePiNCND_All.root"        
        # Extra_Part_of_Name          = "_NEW_V1"
        Extra_Part_of_Name          = "_V7"
        # if("Central" in Selection_Data_Set_In):
        #     if(Event_Type == "SP"):
        #         if("Pass1" in Selection_Data_Set_In):
        #             Extra_Part_of_Name = "_Central_V1"
        #             general_batch_file_location = "".join([main_location, "Spring_2019_epipN/Central_Tracking/Pass1/", str(In_or_Out), "/"])
        #             file_name = "".join(["Single_Pion_Channel_epipX_", str(In_or_Out), "_With_Dp_GitHub_Spring_2019_Pass_1", str(Extra_Part_of_Name), "_File_All.root"])
        #         if("Pass2" in Selection_Data_Set_In):
        #             Extra_Part_of_Name = "_Central_V1"
        #             general_batch_file_location = "".join([main_location, "Spring_2019_epipN/Central_Tracking/Pass2/", str(In_or_Out), "/"])
        #             file_name = "".join(["Single_Pion_Channel_epipX_", str(In_or_Out), "_With_Dp_GitHub_Spring_2019_Pass_2", str(Extra_Part_of_Name), "_File_All.root"])
        # 
        # else:
        if(Event_Type in ["SP", "SPC", "SPF"] or "SP" in Selection_Data_Set_In):
            if("Pass1" in Selection_Data_Set_In):
                Extra_Part_of_Name = "_V3"
                Extra_Part_of_Name = "_V4"
                Extra_Part_of_Name = "_V7"
                # general_batch_file_location = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Spring_2019_epipN/Pass1/"
                general_batch_file_location = "".join([main_location, "Spring_2019_epipN/Pass1/"])
                # file_name = "".join(["Single_Pion_Channel_epipX_", str(In_or_Out), "_With_Dp_GitHub_Spring_2019_Pass_1", str(Extra_Part_of_Name), "_File_nSidis_All.root"])
                file_name = "".join(["Single_Pion_Channel_epipX_", str(In_or_Out), "_With_Dp_GitHub_Spring_2019_Pass_1",   str(Extra_Part_of_Name), "_File_All.root"])
                file_name = "".join(["Single_Pion_Channel_epipX_", str(In_or_Out), "_With_Dp_Spring_2019_Pass_1",                                          "_Forward" if(("F" in Event_Type) or ("Forward" in Selection_Data_Set_In)) else "_Central" if(("C" in Event_Type) or ("Central" in Selection_Data_Set_In)) else "", "_rec_clas", str(Extra_Part_of_Name), "_File_All.root"])
            if("Pass2" in Selection_Data_Set_In):
                Extra_Part_of_Name = "_rec_clas_V5"
                Extra_Part_of_Name = "_rec_clas_NEW_V1"
                Extra_Part_of_Name = "_rec_clas_V3"
                Extra_Part_of_Name = "_rec_clas_V4"
                Extra_Part_of_Name = "_rec_clas_V11"
                
                Extra_Part_of_Name = "_Sp19_P2_Refine_V5"
                # general_batch_file_location = "/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Spring_2019_epipN/Pass2/"
                general_batch_file_location = "".join([main_location, "Spring_2019_epipN/Pass2/"])
                # # file_name                 = "".join(["Single_Pion_Channel_epipX_",                 str(In_or_Out), "_With_Dp_GitHub_Spring_2019_Pass_2", str(Extra_Part_of_Name), "_File_nSidis_All.root"])
                # # file_name                 = "".join(["Single_Pion_Channel_epipX_",                 str(In_or_Out), "_With_Dp_GitHub_Spring_2019_Pass_2", str(Extra_Part_of_Name), "_File_All.root"])
                # file_name                   = "".join(["Single_Pion_Channel_epipX_",                 str(In_or_Out), "_With_Dp_GitHub_Spring_2019_Pass_2",                                                                                                                                                                                   str(Extra_Part_of_Name), "_File_nSidis_All.root"])
                # file_name                   = "".join(["Single_Pion_Channel_epipX_",                 str(In_or_Out), "_With_Dp_GitHub_Spring_2019_Pass_2",                                                                                                                                                                                   str(Extra_Part_of_Name), "_File_All.root"])
                # file_name                   = "".join(["Single_Pion_Channel_epipX_",                 str(In_or_Out), "_With_Dp_Spring_2019_Pass_2",        "_Forward" if(("F" in Event_Type) or ("Forward" in Selection_Data_Set_In)) else "_Central" if(("C" in Event_Type) or ("Central" in Selection_Data_Set_In)) else "", "_rec_clas", str(Extra_Part_of_Name), "_File_All.root"])
                file_name                   = "".join(["Single_Pion_Channel_epipX_",                 str(In_or_Out), "_With_Dp_Forward", str(Extra_Part_of_Name), "_File_All.root"])
        if(Event_Type in ["EO", "EOC", "EOF"] or "EO" in Selection_Data_Set_In):
            if("Pass2" in Selection_Data_Set_In):
                Extra_Part_of_Name = "_rec_clas_V11"
                Extra_Part_of_Name = "_Sp19_P2_Refine_V5"
                general_batch_file_location = "".join([str(main_location), "Only_Electron_Channel/", str(In_or_Out), "/Spring2019_Pass2/"])
                # file_name                   = "".join([                    "Electron_Only_eX_",      str(In_or_Out), "_With_Dp_GitHub_Spring_2019_Pass_2",                                                                                                                                                                                   str(Extra_Part_of_Name), "_File_All.root"])
                # file_name                   = "".join([                    "Electron_Only_eX_",      str(In_or_Out), "_With_Dp_Spring_2019_Pass_2",        "_Forward" if(("F" in Event_Type) or ("Forward" in Selection_Data_Set_In)) else "_Central" if(("C" in Event_Type) or ("Central" in Selection_Data_Set_In)) else "", "_rec_clas", str(Extra_Part_of_Name), "_File_All.root"])
                file_name                   = "".join(["Electron_Only_eX_",                          str(In_or_Out), "_With_Dp_Forward", str(Extra_Part_of_Name), "_File_All.root"])
            else:
                Extra_Part_of_Name = "_V7"
                general_batch_file_location = "".join([str(main_location), "Only_Electron_Channel/", str(In_or_Out), "/Spring2019_Pass1/"])
                file_name                   = "".join([                    "Electron_Only_eX_",      str(In_or_Out), "_With_Dp_Spring_2019_Pass_1",        "_Forward" if(("F" in Event_Type) or ("Forward" in Selection_Data_Set_In)) else "_Central" if(("C" in Event_Type) or ("Central" in Selection_Data_Set_In)) else "", "_rec_clas", str(Extra_Part_of_Name), "_File_All.root"])
                
                
    if("Monte_Carlo_Pass2" in Selection_Data_Set_In):
        Extra_Part_of_Name = "Fa18_P2_MC_V3"
        general_batch_file_location = "/w/hallb-scshelf2102/clas12/richcap/Exclusive_RG-A_Momentum_Corrections/Data_Files/Monte_Carlo_SIDIS/Pass2/"
        file_name = f"Simulated_Single_Pion_Channel_epipX_Inbending_With_Dp_{Extra_Part_of_Name}_File_All.root"
        file_name = f"Simulated_Single_Pion_Channel_epipX_Inbending_With_Dp_{Extra_Part_of_Name}_File_Incomplete.root"
    elif("Monte_Carlo"     in Selection_Data_Set_In):
        Extra_Part_of_Name = "Fa18_P1_MC_V1"
        general_batch_file_location = "/w/hallb-scshelf2102/clas12/richcap/Exclusive_RG-A_Momentum_Corrections/Data_Files/Monte_Carlo_SIDIS/"
        file_name = f"Simulated_Single_Pion_Channel_epipX_Inbending_With_Dp_{Extra_Part_of_Name}_File_All.root"
    
    if("error" in [general_batch_file_location, file_name]):
        print("".join([color.Error, "ERROR: Dataframe not found...", color.END]))
        
    else:
        print("".join([color.BOLD, "Dataframe found for: ", color.BLUE, "Single Pion (eπ+N)" if("SP" == Event_Type) else "(MC) Single Pion (π+)" if("MC" == Event_Type) else "Double Pion (epπ+π-)" if("DP" == Event_Type) else "π0 Channel (epπ0)" if("P0" == Event_Type) else "Elastic Scattering" if("ES" == Event_Type) else "Electron Only", " (", str(In_or_Out), ") Corrections (from RG-A ", str(Selection_Data_Set_In.replace("20", " 20")).replace("_", " "), ")...", color.END]))
        print("".join(["Running code with files located here: \n\t", str(file_name)]))

        running_code_with_these_files = "".join([str(general_batch_file_location), str(file_name)])
        if(__name__ in ["__main__"]):
            print(f"{color.BOLD}running_code_with_these_files =\t{color.UNDERLINE}{running_code_with_these_files}{color.END}\n\n")

        rdf_out = ROOT.TFile(str(running_code_with_these_files))

        return rdf_out
    

if(__name__ in ["__main__"]):
    rdf = DataFrame_Find()






























if(__name__ in ["__main__"]):
    CheckDataFrameQ = 'y'
    CheckDataFrameQ = 'n'
    count = 1
    if(CheckDataFrameQ == 'y'):
        print("\nPrinting the full list of histogram names saved in the root file loaded...\n")
        for ii in rdf.GetListOfKeys():
    #         if("Dmom_pro_Histo(" in str(ii.GetName()) and '_NoELC' in str(ii.GetName())):
    #             print(str(ii.GetName()) + "   -----   object type: " + str(type(rdf.Get(ii.GetName()))))
    #         if("HWC_Histo_All_('mm0'" in str(ii.GetName())):
    #         if("Histo_P_v_Phi_" in str(ii.GetName())):
    #             print("".join([str(count), ") ", str(ii.GetName()), "\n\t-- object type: ", str(type(rdf.Get(ii.GetName()))), "\n"]))
    #         print("".join([str(count), ") ", str(ii.GetName()), "\n\t-- object type: ", str(type(rdf.Get(ii.GetName()))), "\n"]))
            if("Dmom_pel" in str(ii.GetName())):
                print("".join([str(count), ") ", str(ii.GetName()), "\n\t-- object type: ", str(type(rdf.Get(ii.GetName()))), "\n"]))
#             print("".join([str(count), ") ", str(ii.GetName()), "\n\t-- object type: ", str(type(rdf.Get(ii.GetName()))), "\n"]))
            count += 1
        print("".join(["\tTotal length= ", str(len(rdf.GetListOfKeys()))]))

    else:
        print("\nNot printing the full list of histograms saved in the file loaded.")
        print("\n\tTo see what variables are available to be referenced by the code, let CheckDataFrameQ = 'y'\n\t(Does not affect how the rest of the code runs)")
    print("".join(["\nTotal number of histograms available = ", str(len(rdf.GetListOfKeys()))]))
