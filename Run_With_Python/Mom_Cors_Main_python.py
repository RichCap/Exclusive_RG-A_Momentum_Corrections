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

# Turns off the canvases when running in the command line
ROOT.gROOT.SetBatch(1)

from Main_python_Options import *


import argparse

# Create the parser with a description of the script
parser = argparse.ArgumentParser(description='Process some histograms.')

# Add a positional argument that is optional with help text
parser.add_argument('Histogram_Type_Option', nargs='?', choices=['MM', 'Dp', 'MM_el', 'Dp_el', 'MM_pip', 'Dp_pip', 'Out_MM', 'Out_Dp', 'Out_MM_el', 'Out_Dp_el', 'Out_MM_pip', 'Out_Dp_pip', 'In_MM', 'In_Dp', 'In_MM_el', 'In_Dp_el', 'In_MM_pip', 'In_Dp_pip'], help='Specify the histogram type (MM or Dp).')
# Parse the arguments
args = parser.parse_args()
# Access the argument
histogram_type = args.Histogram_Type_Option

if(str(histogram_type) in ['MM', 'Dp', 'MM_el', 'Dp_el', 'MM_pip', 'Dp_pip', 'Out_MM', 'Out_Dp', 'Out_MM_el', 'Out_Dp_el', 'Out_MM_pip', 'Out_Dp_pip', 'In_MM', 'In_Dp', 'In_MM_el', 'In_Dp_el', 'In_MM_pip', 'In_Dp_pip']):
    print(f"\n\n{color.Error}Default Option(s) Not In Use {color.END_R}(run the given arguement with 'Main_python_Options.py' to see more details about the option selected)\n{color.END}")

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
        
        
# CheckDataFrameQ2 = 'n'
# CheckDataFrameQ2 = 'y' # Used for searching with List_of_Locate_name (see below)
# # CheckDataFrameQ2 = 'yf' # Prints full list of available histograms
# # CheckDataFrameQ2 = 'ys' # Prints a reduced list of available histograms (same list as would be drawn if option 'y' was chosen)

Searching_Q = (CheckDataFrameQ2 in ['yf', 'ys'])

Run_1D_Q = True
# Run_1D_Q = False


Extra_Saving_Name = " (zoom)"

Extra_Saving_Name = ""


Print_Canvas_Q = 'n'
Print_Canvas_Q = 'y'

Print_MM_Together = "n"
Print_MM_Together = "y"



Get_WM_Cuts = "yes"
# Get_WM_Cuts = "no"
# Get_WM_Cuts = "not_at_all"


Get_Dp_Cors_Master = "yes"
Get_Dp_Cors_Master = "no"


if(Print_Canvas_Q == 'y' and 'y' != CheckDataFrameQ2):
    Print_Canvas_Q = 'n'


max_print_allowed = 500 # Change this number to limit the number of canvases drawn (will stop drawing after this number is exceeded)



if(CheckDataFrameQ2 == 'yf'):
    List_of_Locate_name2 = ['']
else:
    List_of_Locate_name2 = List_of_Locate_name
    

Particle_Mom_List_Particle_Sec_List_Same_Q = "y"
# Particle_Mom_List_Particle_Sec_List_Same_Q = "n"

rdf_List, WM_Cuts_List, Correction_Fit_Line, Legend, List_of_WM_Peaks = {}, {}, {}, {}, {}

search_count = 0

List_of_Saved_Images = []

if('y' in CheckDataFrameQ2):
    
    if(Print_Canvas_Q == 'y'):
        print("Printing requested histograms...\n")
        histo_search, canvas_search, stats_box_all, Histo_Title_New, Histo_WM_Cut_Up, Histo_WM_Cut_Down, histo_clone = {}, {}, {}, {}, {}, {}, {}

    for EvntType in EvntType_List:
        event_type = EvntType
        MM_type = "epipX" if("SP" in event_type) else "eppipX" if("DP" in event_type) else "eppi0X" if("P0" in event_type) else "epX" if("ES" in event_type) else "eX" if("EO" in event_type) else "ERROR"
        if(MM_type == "ERROR"):
            print("".join([color.RED, "ERROR IN MISSING MASS TYPE (", str(event_type),")", color.END]))
            continue
        for Bending_Type in Bending_Type_List:
            Selection_of_In_or_Out = Bending_Type
            for Data_Run in Data_Run_List:
                Selection_Data_Set = Data_Run
                rdf_List_Name = str((EvntType, Bending_Type, Data_Run))
                try:
                    print("\n\n\n\n\n")
                    rdf_List[str((EvntType, Bending_Type, Data_Run))] = DataFrame_Find(EvntType, In_or_Out=Bending_Type, Selection_Data_Set_In=Data_Run)
                    # event_type = EvntType
                    print("\n\n\n")
                except Exception as e:
                    print("".join([color.BOLD, "ERROR: ", color.RED, str(e), color.END_B, "\nTRACEBACK:\n", color.RED, str(traceback.format_exc()), "\n", color.END]))
                    
                for Locate_Name_Full in List_of_Locate_name2:

                    Locate_name, Correction_Name_List_2, Sector_Number_List_2, Binning_Option_List_2, Region_Option_List_2, Particle_Mom_List_2, Particle_Sec_List_2, Extra_Cut_Option_2, D_Angle_Type_2, Get_Dp_Cors = Full_List_of_Histo_Options(Locate_Name_Full, Correction_Name_List, Sector_Number_List, Binning_Option_List, Region_Option_List, Particle_Mom_List, Particle_Sec_List, Extra_Cut_Option, D_Angle_Type, Get_Dp_Cors_Master)
                    
                    for Cut_Name in Extra_Cut_Option_2:
                    
                        for Correction_Name in Correction_Name_List_2:
                            
                            for Sector_Num in Sector_Number_List_2:

                                for ii in rdf_List[str((EvntType, Bending_Type, Data_Run))].GetListOfKeys():

                                    out_print = str(ii.GetName())
                                    # if("Dmom_pro" in out_print and "P0" == EvntType):
                                    #     print(out_print)
                                    # else:
                                    #     continue
                                    # if("Dmom_pel_Histo('mmEF_PipMMEF'" not in str(out_print)):
                                    #     continue
                                    
                                    if("Dmom_pro" in out_print and "Larger_Dp" in out_print):
                                        # print("skip alternative ∆P calculation")
                                        continue

                                    if(True in Continue_Loops(out_print, Cut_Name_In=Cut_Name, EVENTS=event_type)):
                                        # print(out_print)
                                        # print(Continue_Loops(out_print, Cut_Name_In=Cut_Name, EVENTS=event_type))
                                        continue

                                    if(True in Continue_Loops(out_print, Cut_Name_In=Cut_Name, Correction_Name_In=Correction_Name, EVENTS=event_type)):
                                        # print(out_print)
                                        # print(Continue_Loops(out_print, Cut_Name_In=Cut_Name, EVENTS=event_type))
                                        continue

                                    for DAngle_Type in D_Angle_Type_2:

                                        for Binning_Option in Binning_Option_List_2:

                                            for Region_Option in Region_Option_List_2:

                                                if(True in Continue_Loops(out_print, Cut_Name_In=Cut_Name, Correction_Name_In=Correction_Name, Binning_Option_In=Binning_Option, Region_Option_In=Region_Option, Searching_Q_In=Searching_Q, Region_Option_List_2_In=Region_Option_List_2, EVENTS=event_type)):
                                                    # print(out_print)
                                                    # print(Continue_Loops(out_print, Cut_Name_In=Cut_Name, EVENTS=event_type))
                                                    continue

                                                if("Dmom_pro" in out_print and Region_Option != "regall"):
                                                    # print("Not using phi bins for proton corrections...")
                                                    continue

                                                for Particle_Mom in Particle_Mom_List_2:

                                                    if("Dmom_pip"   in out_print and Particle_Mom != "pip" and "pip" not in Particle_Mom_List_2):
                                                        Particle_Mom = "pip"
                                                    elif("Dmom_pip" in out_print and Particle_Mom != "pip" and "pip"     in Particle_Mom_List_2):
                                                        continue

                                                    if("Dmom_pel"   in out_print and Particle_Mom != "el"  and "el"  not in Particle_Mom_List_2):
                                                        Particle_Mom = "el"
                                                    elif("Dmom_pel" in out_print and Particle_Mom != "el"  and "el"      in Particle_Mom_List_2):
                                                        continue

                                                    if("Dmom_pro"   in out_print and Particle_Mom != "pro" and "pro" not in Particle_Mom_List_2):
                                                        Particle_Mom = "pro"
                                                    elif("Dmom_pro" in out_print and Particle_Mom != "pro" and "pro"     in Particle_Mom_List_2):
                                                        continue


                                                    for Particle_Sec in Particle_Sec_List_2:

                                                        if("y" in Particle_Mom_List_Particle_Sec_List_Same_Q):
                                                            if("Dmom_pip"   in out_print and Particle_Sec != "pip" and "pip" not in Particle_Sec_List_2):
                                                                Particle_Sec = "pip"
                                                            elif("Dmom_pip" in out_print and Particle_Sec != "pip" and "pip"     in Particle_Sec_List_2):
                                                                continue

                                                            if("Dmom_pel"   in out_print and Particle_Sec != "el"  and "el"  not in Particle_Sec_List_2):
                                                                Particle_Sec = "el"
                                                            elif("Dmom_pel" in out_print and Particle_Sec != "el"  and "el"      in Particle_Sec_List_2):
                                                                continue

                                                            if("Dmom_pro"   in out_print and Particle_Sec != "pro" and "pro" not in Particle_Sec_List_2):
                                                                Particle_Sec = "pro"
                                                            elif("Dmom_pro" in out_print and Particle_Sec != "pro" and "pro"     in Particle_Sec_List_2):
                                                                continue

                                                        if(("y" in Particle_Mom_List_Particle_Sec_List_Same_Q and Particle_Mom != Particle_Sec) and not Searching_Q):
                                                            continue
                                                            
                                                        
                                                        Locate_Name_Canvas = ((((((Locate_name.replace("Correction_Name_List", Correction_Name)).replace("Binning_Option_List", str(Binning_Option))).replace("Region_Option_List", str(Region_Option)).replace("Particle_Mom_List", str(Particle_Mom))).replace("Particle_Sec_List", str(Particle_Sec)))).replace("Extra_Cut_Option", str(Cut_Name))).replace("D_Angle_Type", str(DAngle_Type))
                                                        Locate_Name_Sec    = (((((Locate_Name_Canvas.replace("Sector_Number_List", str(Sector_Num))).replace('El Sector 0', '')).replace('Pi+ Sector 0', '')).replace('Pro Sector 0', '')).replace("Extra_Cut_Option", str(Cut_Name))).replace("D_Angle_Type", str(DAngle_Type))

                                                        if(Condition_Check_Full(Locate_Name_Full, CheckDataFrameQ2, Locate_Name_Sec, out_print)):

#                                                             if((("Histo_P_v_Th_"     in str(out_print))  or ("Histo_P_v_Phi_"     in str(out_print))  or ("Histo_Th_v_Phi_"     in str(out_print))) and (Sector_Num not in [0, "All"])):
#                                                                 print("".join([color.RED, "Wrong Sector for histogram choice", color.END]))
#                                                                 continue
#                                                             if((("Histo_P_v_Th_" not in str(out_print)) and ("Histo_P_v_Phi_" not in str(out_print)) and ("Histo_Th_v_Phi_" not in str(out_print))) and (Sector_Num     in [0, "All"])):
#                                                                 print("".join([color.RED, "Wrong Sector for histogram choice", color.END]))
#                                                                 continue

                                                            search_count += 1
                                                            if(Get_Dp_Cors == "no"):
                                                                # print("".join(["Histo ", str(search_count), ") ", out_print, "   -----   object type: ", str(type(rdf_List[str((EvntType, Bending_Type, Data_Run))].Get(out_print)))]))
                                                                print("".join(["Histo ", str(search_count), ") ", out_print]))

            ##=========================================================##===================================##=========================================================##
            ##=========================================================##  Printing Results Output (Start)  ##=========================================================##
            ##=========================================================##===================================##=========================================================##

                                                            if((max_print_allowed <= search_count) and not Searching_Q):
                                                                print("\nWent Beyond the Maximum Number of Histograms to be Printed...\n\tPlease change 'max_print_allowed' to display more histograms")
                                                                break
                                                            
                                                            No_divide_condition = (Sector_Num in [0, "all"] or "Histo_P_v_Th_" in out_print or "Histo_P_v_Phi_" in out_print or "Histo_Th_v_Phi_" in out_print)
                                    
                                                            # if(No_divide_condition):
                                                            #     print(color.BGREEN + "TEST: " + str(out_print) + color.END)
                                                            
                                                            if(Print_Canvas_Q == 'y' and max_print_allowed > search_count):
                                                                # Divide_1 = 1 if(No_divide_condition) else 3
                                                                # Divide_2 = 1 if(No_divide_condition) else 2
                                                                # Canvas_Size_1 = 800 if(No_divide_condition) else 1500
                                                                # Canvas_Size_2 = 800 if(No_divide_condition) else 1200
                                                                Divide_1, Divide_2, Canvas_Size_1, Canvas_Size_2 = 3, 2 if(9 not in Sector_Number_List_2) else 3 if(12 not in Sector_Number_List_2) else 4, 1500, 1200
                                                                if(Sector_Num in [0, "All"]):
                                                                    Divide_1, Divide_2, Canvas_Size_1, Canvas_Size_2 = 1, 1, 1500, 1200
                                                                Canvas_Search_Name = Locate_Name_Canvas if(Sector_Num != 0) else out_print
                                                                if(Print_MM_Together == "y" and "hmmCPARTall" in out_print and (Binning_Option != 1 or Region_Option != "regall")):
                                                                    Canvas_Search_Name = ((Locate_Name_Canvas.replace("reg1", "Region_Option_List")).replace("reg2", "Region_Option_List")).replace("reg3", "Region_Option_List")
                                                                    if(Sector_Num in [0, "all"]):
                                                                        Canvas_Search_Name = ((out_print.replace("reg1", "Region_Option_List")).replace("reg2", "Region_Option_List")).replace("reg3", "Region_Option_List")
                                                                        
                                                                        
                                                                multi_file_str = "".join(["_", EvntType, "_", str(Bending_Type).replace("bending", ""), "_", str(Data_Run)])
                                                                
                                                                canvas_name_full = "".join([Canvas_Search_Name, multi_file_str])
                                                                out_print_name = "".join([out_print, multi_file_str])

                                                                try:
                                                                    canvas_search[canvas_name_full]
                                                                except:
                                                                    if(print_method == "hor"):
                                                                        canvas_search[canvas_name_full] = ROOT.TCanvas(canvas_name_full, canvas_name_full, int(1.5*Canvas_Size_1), int(1.5*Canvas_Size_2))
                                                                        canvas_search[canvas_name_full].Divide(Divide_1, Divide_2, 0, 0)
                                                                    else:
                                                                        canvas_search[canvas_name_full] = ROOT.TCanvas(canvas_name_full, canvas_name_full, int(1.5*Canvas_Size_2), int(1.5*Canvas_Size_1))
                                                                        canvas_search[canvas_name_full].Divide(Divide_2, Divide_1, 0, 0)
                                                                    canvas_search[canvas_name_full].SetGrid()
                                                                    # canvas_search[canvas_name_full] = Canvas_Create(Name=canvas_name_full, Num_Columns=Divide_1, Num_Rows=Divide_2, Size_X=Canvas_Size_1, Size_Y=Canvas_Size_2, cd_Space=0)
                                                                    # canvas_search[canvas_name_full] = Canvas_Create(Name=canvas_name_full, Num_Columns=Divide_2, Num_Rows=Divide_2, Size_X=Canvas_Size_2, Size_Y=Canvas_Size_2, cd_Space=0)
                                                                    
                                                                    
                                                                Legend_Name = str(canvas_name_full).replace("Region_Option_List", "Integrated Regions" if(Region_Option == "regall") else "Individual Regions")
                                                                # Legend_Name = str(canvas_name_full).replace("Region_Option_List", Region_Option)
                                                                Legend[Legend_Name] = ROOT.TLegend(0.15, 0.25, 0.85, 0.1)

                                                                # ROOT.gStyle.SetOptFit(0)
                                                                ROOT.gStyle.SetOptFit(1)
                                                                ROOT.gStyle.SetOptStat("emr")
                                                                # ROOT.gStyle.SetOptStat(0)
                                                                ROOT.gStyle.SetTitleY(1)
                                                                ROOT.gStyle.SetTitleX(0.5)
                                                                ROOT.gStyle.SetLegendTextSize(0.0275)

                                                                # blank_Canvas = Canvas_Create(Name="test_blank_func", Num_Columns=1, Num_Rows=1, Size_X=600, Size_Y=800, cd_Space=0)

                                                                # print("".join(["cd_num = ", str(1 if(Sector_Num in [0, "all"]) else Sector_Num), "\n"]))
                                                                histo_search[out_print_name], Histo_Title_New[out_print_name] = Find_And_Slice_Histo(RDF=rdf_List[str((EvntType, Bending_Type, Data_Run))], NAME=out_print, EVENT=EvntType, PARTICLE=Particle_Mom, BENDING=Bending_Type, Pass_Type=Data_Run)
                                                                
                                                                Histo_Title_New[out_print_name] = Histo_Title_New[out_print_name].replace("localelPhiS", "#phi_{El}")
                                                                histo_search[out_print_name].SetTitle(str(histo_search[out_print_name].GetTitle()).replace("localelPhiS", "#phi_{El}"))
                                                                histo_search[out_print_name].SetTitle(str(histo_search[out_print_name].GetTitle()).replace("Pi+", "#pi^{+}"))
                                                                
                                                                # print("(histo_search[out_print_name]).GetTitle() =", str(histo_search[out_print_name].GetTitle()))
                                                                histo_search[out_print_name].SetTitle(str(histo_search[out_print_name].GetTitle()).replace("El Cor (Quad - Quad Phi - With Elastic Cors) - #pi^{+} Cor (Quad - Quad Phi - With Elastic Cors)", "#splitline{El Cor (Quad - Quad Phi - With Elastic Cors)}{#pi^{+} Cor (Quad - Quad Phi - With Elastic Cors)}"))
                                                                histo_search[out_print_name].SetTitle(str(histo_search[out_print_name].GetTitle()).replace("El Cor (Quad - Quad Phi - With Elastic Cors) - No #pi^{+} Cor", "#splitline{El Cor (Quad - Quad Phi - With Elastic Cors)}{No #pi^{+} Cor}"))
                                                                # Tline_Simple = ROOT.TLine()
                                                                # Tline_Simple.SetLineColor(2)
                                                                # Tline_Simple.SetLineWidth(2)

                                                                # Fit_Pars, TLine_Simple_Pars = Fitting_Lines(out_print, event_type, Selection_of_In_or_Out, Particle_Mom, Data_Run)
                                                                Fit_Pars, TLine_Simple_Pars = Fitting_Lines(Histo_Type=out_print, Event_Type=event_type, Bending_Type=Selection_of_In_or_Out, Particle=Particle_Mom, DataSet=Data_Run, Sector=Sector_Num)
                                                                MinRange_Fit, MaxRange_Fit, Increment_Fit = Fit_Pars
                                                                Tline_Simple_X1, Tline_Simple_Y1, Tline_Simple_X2, Tline_Simple_Y2 = TLine_Simple_Pars

                                                                canvas_search[canvas_name_full].Draw()

                                                                if("hmmCPARTall" not in out_print):
                                                                    Draw_Canvas(canvas_search[canvas_name_full], 1 if(Sector_Num in [0, "all"]) else Sector_Num, 0.05, 0, -0.02, 0)
                                                                else:
                                                                    # Draw_Canvas(canvas_search[canvas_name_full], 1 if(Sector_Num == 0 or Sector_Num == "all") else Sector_Num, 0.05, 0, -0.02, -0.02)
                                                                    try:
                                                                        Draw_Canvas(canvas_search[canvas_name_full], Sector_Num, 0.05, 0, -0.02, -0.02)
                                                                    except:
                                                                        print("".join([color.Error, "\nFailed Draw_Canvas.cd(Sector_Num)\n", color.END]))
                                                                        Draw_Canvas(canvas_search[canvas_name_full], 1, 0.05, 0, -0.02, -0.02)


            ##=========================================================##===================================##=========================================================##
            ##=========================================================##       Fitting 2D Histograms       ##=========================================================##
            ##=========================================================##===================================##=========================================================##

                                   ###############################################################################################################
                                   ##==================================#######################################==================================##
                                   ##==========##==========##==========##     Invariant Mass Histograms     ##==========##==========##==========##
                                   ##==================================#######################################==================================##
                                   ###############################################################################################################
                                                                if("HWC_Histo_All" in out_print and "SP" not in event_type):
                                                                    List_of_WM_Peaks[str((Cut_Name, Sector_Num))] = histo_search[out_print_name].FindPeak_x
                                                                    List_of_WM_Peaks[str((Cut_Name, Sector_Num, "Upper"))] = histo_search[out_print_name].FindPeak_Cut_Up
                                                                    List_of_WM_Peaks[str((Cut_Name, Sector_Num, "Lower"))] = histo_search[out_print_name].FindPeak_Cut_Down
                                                                    Upper_Cut_Func = ROOT.TF1("Upper_Cut_Func","[p0_Up] + [p1_Up]*x",     MinRange_Fit - 0.5*Increment_Fit, MaxRange_Fit + 0.5*Increment_Fit)
                                                                    Lower_Cut_Func = ROOT.TF1("Lower_Cut_Func","[p0_Down] + [p1_Down]*x", MinRange_Fit - 0.5*Increment_Fit, MaxRange_Fit + 0.5*Increment_Fit)
                                                                    Upper_Cut_Func.SetLineColor(root_color.Green)
                                                                    Lower_Cut_Func.SetLineColor(root_color.Green)
                                                                    Histo_WM_Cut_Up[str((out_print_name,     "up"))] = (histo_search[out_print_name].gr2_Cut_Range_Up).Clone()
                                                                    Histo_WM_Cut_Down[str((out_print_name, "down"))] = (histo_search[out_print_name].gr2_Cut_Range_Down).Clone()
                                                                    if("no" not in Get_WM_Cuts):
                                                                        Histo_WM_Cut_Up[str((out_print_name,     "up"))].Fit("Upper_Cut_Func", "RQ")
                                                                        Histo_WM_Cut_Down[str((out_print_name, "down"))].Fit("Lower_Cut_Func", "RQ")
                                                                        WM_Cuts_List[str((out_print_name, Particle_Mom, Sector_Num, "Function_Upper"))] = ROOT.TF1("".join(["WM_Fit_Line[", str((Particle_Mom, Sector_Num, "Function_Upper")) ,"]"]), "".join(["(", str(round(Histo_WM_Cut_Up[str((out_print_name, "up"))].GetFunction("Upper_Cut_Func").GetParameter(1), 6)), ")*x + (", str(round(Histo_WM_Cut_Up[str((out_print_name, "up"))].GetFunction("Upper_Cut_Func").GetParameter(0), 6)), ")"]), Tline_Simple_X1, Tline_Simple_X2)
                                                                        WM_Cuts_List[str((out_print_name, Particle_Mom, Sector_Num, "Function_Lower"))] = ROOT.TF1("".join(["WM_Fit_Line[", str((Particle_Mom, Sector_Num, "Function_Lower")) ,"]"]), "".join(["(", str(round(Histo_WM_Cut_Down[str((out_print_name, "down"))].GetFunction("Lower_Cut_Func").GetParameter(1), 6)), ")*x + (", str(round(Histo_WM_Cut_Down[str((out_print_name, "down"))].GetFunction("Lower_Cut_Func").GetParameter(0), 6)), ")"]), Tline_Simple_X1, Tline_Simple_X2)
                                                                    stats_box_all[str((out_print_name, "up"))] = Histo_WM_Cut_Up[str((out_print_name, "up"))].GetListOfFunctions().FindObject("stats")
                                                                    stats_box_all[str((out_print_name, "down"))] = Histo_WM_Cut_Down[str((out_print_name, "down"))].GetListOfFunctions().FindObject("stats")
                                                                    WM_Cuts_List[str((Particle_Mom, Sector_Num))] = [Histo_WM_Cut_Up[str((out_print_name, "up"))], Histo_WM_Cut_Down[str((out_print_name, "down"))]]
                                   ###############################################################################################################
                                   ##==================================#######################################==================================##
                                   ##==========##==========##==========##     Invariant Mass Histograms     ##==========##==========##==========##
                                   ##==================================#######################################==================================##
                                   ###############################################################################################################

            ##=========================================================##===================================##=========================================================##
            ##=========================================================##       Drawing 2D Histograms       ##=========================================================##
            ##=========================================================##===================================##=========================================================##

                                                                ROOT.gPad.SetLogz(0)

                                                                if(not (Print_MM_Together == "y" and "hmmCPARTall" in out_print and "regall" not in out_print)):
                        
                                                                    # if(print_method == "hor"):
                                                                    #     canvas_search[canvas_name_full].Divide(Divide_1, Divide_2, 0, 0)
                                                                    # else:
                                                                    #     canvas_search[canvas_name_full].Divide(Divide_2, Divide_1, 0, 0)
                                                                    # Draw_Canvas(canvas_search[canvas_name_full], 1 if(Sector_Num in [0, "all"]) else Sector_Num, 0.05, 0, -0.02, 0)
                                                
                        
                                                                    if("hmmCPARTall" in out_print and EvntType == "DP"):
#                                                                         histo_search[out_print_name].GetYaxis().SetRangeUser(-0.04, 0.08)
                                                                        histo_search[out_print_name].GetYaxis().SetRangeUser(-0.04, 0.06)
                                                                        histo_search[out_print_name].GetXaxis().SetRangeUser(0.4, 3)
                                                                        # print(histo_search[out_print_name].GetTitle())
                                        
                                                                    histo_search[out_print_name].Draw("colz" if("TH2D" in str(type(rdf_List[str((EvntType, Bending_Type, Data_Run))].Get(out_print)))) else "same")
                                                                    canvas_search[canvas_name_full].Modified()
                                                                    canvas_search[canvas_name_full].Update()

                                                                    # if("hmmCPARTall" not in out_print):
                                                                    palette_move(canvas_search[canvas_name_full], histo_search[out_print_name], 0, 0.005, -0.25 if("Dmom" not in out_print and "HWC_Histo_All" not in out_print and "hmmCPARTall" not in out_print) else 0, 0.01)
                                                                    # stats_box_all[out_print_name] = ""
                                                                    # statbox_move(histo_search[out_print_name], canvas_search["".join([Canvas_Search_Name, "_", EvntType, "_",  str(Bending_Type).replace("bending", ""), "_", str(Data_Run)])], stats_box_all[out_print_name], Sector_Num, "norm" if("Dmom" not in out_print and "HWC_Histo_All" not in out_print and "hmmCPARTall" not in out_print and "Histo_P_v_Th_" not in out_print and "Histo_P_v_Phi_" not in out_print and "Histo_Th_v_Phi_" not in out_print) else "off", 0.65, 0.65, 0.5, 0.5)
                                                                    # else:
                                                                    #     ROOT.gStyle.SetOptStat(0)
                                                                else:
                                                                    canvas_search[canvas_name_full].Modified()
                                                                    canvas_search[canvas_name_full].Update()

                                                                if("Histo_P_v_Th_" not in out_print and "Histo_P_v_Phi_" not in out_print and "Histo_Th_v_Phi_" not in out_print and not ("HWC_Histo_All" in out_print and "SP" in event_type)):
                                                                    try:
                                                                        # canvas_search["".join([Canvas_Search_Name, "_", EvntType, "_",  str(Bending_Type).replace("bending", ""), "_", str(Data_Run)])] = Canvas_Create(Name="".join([Canvas_Search_Name, "_", EvntType, "_",  str(Bending_Type).replace("bending", ""), "_", str(Data_Run)]), Num_Columns=3, Num_Rows=2, Size_X=600, Size_Y=800, cd_Space=0)
                                                                        # Draw_Canvas(canvas_search["".join([Canvas_Search_Name, "_", EvntType, "_",  str(Bending_Type).replace("bending", ""), "_", str(Data_Run)])], 1 if(Sector_Num in [0, "all"]) else Sector_Num, 0.05, 0, -0.02, -0.02)
                                                                        # print(Sector_Num)
                                                                        if(Print_MM_Together == "y" and "hmmCPARTall" in out_print and "regall" not in out_print):
                                                                            try:
                                                                                Legend[Legend_Name].SetNColumns(3)
                                                                                region_1_Name = (((out_print_name.replace("regall", "reg1")).replace("reg2", "reg1")).replace("reg3", "reg1")).replace("'1'", "'3'")
                                                                                try:
                                                                                    histo_search[region_1_Name].gr2.SetMarkerColor(1 if("mm0" not in Correction_Name) else 12)
                                                                                except:
                                                                                    try:
                                                                                        histo_search[region_1_Name] = Find_And_Slice_Histo(RDF=rdf_List[str((EvntType, Bending_Type, Data_Run))], NAME=(((out_print.replace("regall", "reg1")).replace("reg2", "reg1")).replace("reg3", "reg1")).replace("'1'", "'3'"), EVENT=EvntType, PARTICLE=Particle_Mom, BENDING=Bending_Type, OUT_Q="Histo", Pass_Type=Data_Run)
                                                                                    except Exception as e:
                                                                                        print("".join([color.RED, "\n\n", str(e), "\n\n", color.END]))
                                                                                histo_search[region_1_Name].gr2.SetMarkerColor(1 if("mm0" not in Correction_Name) else 12)
                                                                                histo_search[region_1_Name].gr2.SetLineColor(1   if("mm0" not in Correction_Name) else 12)
                                                                                histo_search[region_1_Name].gr2.SetMarkerStyle(1 if("mm0" in     Correction_Name) else 8)
                                                                                histo_search[region_1_Name].gr2.SetLineStyle(2   if("mm0" in     Correction_Name) else 47)
                                                                                histo_search[region_1_Name].gr2.SetLineWidth(2   if("mm0" not in Correction_Name) else 4)
                                                                                histo_search[region_1_Name].gr2.SetMarkerSize(3  if("mm0" in     Correction_Name) else 1)
                                                                                histo_search[region_1_Name].gr2.Draw("AP same"   if("mm0" not in Correction_Name) else "APL same")
                                                                                histo_search[region_1_Name].gr2.SetTitle("".join(["#splitline{", str(histo_search[out_print_name].GetTitle()), "}{All 3 #phi Bins  ", str(root_color.Bold), "{#scale[0.85]{(Central Bin - #color[3]{Positive Bin} - #color[2]{Negative Bin})}}}; ", str(histo_search[out_print_name].GetXaxis().GetTitle()), ";", str(histo_search[out_print_name].GetYaxis().GetTitle())]))
                                                                                if(EvntType == "SP"):
                                                                                    histo_search[region_1_Name].gr2.GetYaxis().SetRangeUser(0.88, 1)
                                                                                else:
                                                                                    histo_search[region_1_Name].gr2.GetYaxis().SetRangeUser((Tline_Simple_Y1 - 0.1) if(EvntType != "DP") else -0.05, (Tline_Simple_Y1 + 0.1) if(EvntType != "DP") else 0.1)

                                                                                region_2_Name = (((out_print_name.replace("regall", "reg2")).replace("reg1", "reg2")).replace("reg3", "reg2")).replace("'1'", "'3'")
                                                                                try:
                                                                                    histo_search[region_2_Name].gr2.SetMarkerColor(2 if("mm0" not in Correction_Name) else 46)
                                                                                except:
                                                                                    try:
                                                                                        histo_search[region_2_Name] = Find_And_Slice_Histo(RDF=rdf_List[str((EvntType, Bending_Type, Data_Run))], NAME=(((out_print.replace("regall", "reg2")).replace("reg1", "reg2")).replace("reg3", "reg2")).replace("'1'", "'3'"), EVENT=EvntType, PARTICLE=Particle_Mom, BENDING=Bending_Type, OUT_Q="Histo", Pass_Type=Data_Run)
                                                                                    except Exception as e:
                                                                                        print("".join([color.RED, "\n\n", str(e), "\n\n", color.END]))
                                                                                histo_search[region_2_Name].gr2.SetMarkerColor(2 if("mm0" not in Correction_Name) else 46)
                                                                                histo_search[region_2_Name].gr2.SetLineColor(2   if("mm0" not in Correction_Name) else 46)
                                                                                histo_search[region_2_Name].gr2.SetMarkerStyle(1 if("mm0" in     Correction_Name) else 8)
                                                                                histo_search[region_2_Name].gr2.SetLineStyle(2   if("mm0" in     Correction_Name) else 47)
                                                                                histo_search[region_2_Name].gr2.SetLineWidth(2   if("mm0" not in Correction_Name) else 4)
                                                                                histo_search[region_2_Name].gr2.SetMarkerSize(3  if("mm0" in     Correction_Name) else 1)
                                                                                histo_search[region_2_Name].gr2.Draw("P same"    if("mm0" not in Correction_Name) else "PL same")

                                                                                region_3_Name = (((out_print_name.replace("regall", "reg3")).replace("reg2", "reg3")).replace("reg1", "reg3")).replace("'1'", "'3'")
                                                                                try:
                                                                                    histo_search[region_3_Name].gr2.SetMarkerColor(3 if("mm0" not in Correction_Name) else 8)
                                                                                except:
                                                                                    try:
                                                                                        histo_search[region_3_Name] = Find_And_Slice_Histo(RDF=rdf_List[str((EvntType, Bending_Type, Data_Run))], NAME=(((out_print.replace("regall", "reg3")).replace("reg2", "reg3")).replace("reg1", "reg3")).replace("'1'", "'3'"), EVENT=EvntType, PARTICLE=Particle_Mom, BENDING=Bending_Type, OUT_Q="Histo", Pass_Type=Data_Run)
                                                                                    except Exception as e:
                                                                                        print("".join([color.RED, "\n\n", str(e), "\n\n", color.END]))
                                                                                histo_search[region_3_Name].gr2.SetMarkerColor(3 if("mm0" not in Correction_Name) else 8)
                                                                                histo_search[region_3_Name].gr2.SetLineColor(3   if("mm0" not in Correction_Name) else 8)
                                                                                histo_search[region_3_Name].gr2.SetMarkerStyle(1 if("mm0" in     Correction_Name) else 8)
                                                                                histo_search[region_3_Name].gr2.SetLineStyle(2   if("mm0" in     Correction_Name) else 47)
                                                                                histo_search[region_3_Name].gr2.SetLineWidth(2   if("mm0" not in Correction_Name) else 4)
                                                                                histo_search[region_3_Name].gr2.SetMarkerSize(3  if("mm0" in     Correction_Name) else 1)
                                                                                histo_search[region_3_Name].gr2.Draw("P same"    if("mm0" not in Correction_Name) else "PL same")

                                                                                Legend[Legend_Name].AddEntry(histo_search[region_1_Name].gr2, "".join(["#color[", str(1 if("mm0" not in Correction_Name) else 12), "]{#splitline{", "Corrected" if("mm0" not in Correction_Name) else "Uncorrected", "}{Central #phi Bin}}"]),  "p" if("mm0" not in Correction_Name) else "lp")
                                                                                Legend[Legend_Name].AddEntry(histo_search[region_2_Name].gr2, "".join(["#color[", str(2 if("mm0" not in Correction_Name) else 46), "]{#splitline{", "Corrected" if("mm0" not in Correction_Name) else "Uncorrected", "}{Negative #phi Bin}}"]), "p" if("mm0" not in Correction_Name) else "lp")
                                                                                Legend[Legend_Name].AddEntry(histo_search[region_3_Name].gr2, "".join(["#color[", str(3 if("mm0" not in Correction_Name) else 8),  "]{#splitline{", "Corrected" if("mm0" not in Correction_Name) else "Uncorrected", "}{Positive #phi Bin}}"]), "p" if("mm0" not in Correction_Name) else "lp")


                                                                                if(Sector_Num in [6, 0, "all"]):
                                                                                    # print("".join(["\n\nLegend name: ", Legend_Name]))
                                                                                    Draw_Canvas(canvas_search[canvas_name_full], 1 if(Sector_Num in [0, "all"]) else Sector_Num, 0.05, 0, -0.02, -0.02)
                                                                                    Legend[Legend_Name].Draw()

                                                                            except Exception as e:
                                                                                print("".join([color.Error, "PHI BINNING ERROR: \n", str(e), "\n", color.END]))
                                                                                # Printing currently available points...
                                                                                histo_search[out_print_name].gr2.Draw("P same")
                                                                                Legend[Legend_Name].AddEntry(histo_search[out_print_name].gr2, "Corrected" if("mm0" not in Correction_Name) else "Uncorrected", "p" if("mm0" not in Correction_Name) else "lp")

                                                                        else:
                                                                            histo_search[out_print_name].gr2.SetMarkerColor(1)
                                                                            histo_search[out_print_name].gr2.SetLineColor(1)
                                                                            histo_search[out_print_name].gr2.SetMarkerStyle(8)
                                                                            histo_search[out_print_name].gr2.SetMarkerSize(1)
                                                                            histo_search[out_print_name].gr2.SetLineStyle(47)
                                                                            histo_search[out_print_name].gr2.SetLineWidth(2 if("mm0" not in Correction_Name) else 4)
                                                                            histo_search[out_print_name].gr2.Draw("P same")
                                                                            if("hmmCPARTall" in out_print): # and EvntType not in ["DP", "P0"]):
                                                                                Legend[Legend_Name].SetNColumns(3)
                                                                                Legend[Legend_Name].AddEntry(histo_search[out_print_name].gr2, "All Corrections" if(EvntType in ["DP"] and "Pro" in Correction_Name and "No_ELC" not in Correction_Name) else "Corrected" if("mm0" not in Correction_Name) else "Uncorrected", "p" if("mm0" not in Correction_Name) else "lp")
                                                                                if("mm0" not in Correction_Name):
                                                                                    if(event_type not in ["DP"]):
                                                                                        try:
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mm0")].gr2.SetMarkerColor(12)
                                                                                        except:
                                                                                            try:
                                                                                                histo_search[out_print_name.replace(Correction_Name, "mm0")] = Find_And_Slice_Histo(RDF=rdf_List[str((EvntType, Bending_Type, Data_Run))], NAME=out_print.replace(Correction_Name, "mm0"), EVENT=EvntType, PARTICLE=Particle_Mom, BENDING=Bending_Type, OUT_Q="Histo", Pass_Type=Data_Run)
                                                                                            except Exception as e:
                                                                                                print("".join([color.RED, "\n\n", str(e), "\n\n", color.END]))

                                                                                        if("E" not in event_type and event_type not in ["SP", "MC"]):
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mm0")].gr2.SetMarkerColor(7)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mm0")].gr2.SetLineColor(7)
                                                                                        else:
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mm0")].gr2.SetMarkerColor(12)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mm0")].gr2.SetLineColor(12)
                                                                                        histo_search[out_print_name.replace(Correction_Name, "mm0")].gr2.SetMarkerStyle(1)
                                                                                        histo_search[out_print_name.replace(Correction_Name, "mm0")].gr2.SetMarkerSize(1)
                                                                                        histo_search[out_print_name.replace(Correction_Name, "mm0")].gr2.SetLineStyle(2)
                                                                                        histo_search[out_print_name.replace(Correction_Name, "mm0")].gr2.SetLineWidth(4)

                                                                                        Draw_Canvas(canvas_search[canvas_name_full], 1 if(Sector_Num in [0, "all"]) else Sector_Num, 0.05, 0, -0.02, -0.02)
                                                                                        histo_search[out_print_name.replace(Correction_Name, "mm0")].gr2.Draw("PL same")
                                                                                        Legend[Legend_Name].AddEntry(histo_search[out_print_name.replace(Correction_Name, "mm0")].gr2, "#color[4]{Energy Loss Only}" if(event_type not in ["ES", "SP", "MC"]) else "#color[12]{Uncorrected}", "lp")

                                                                                    if("E" not in event_type and event_type not in ["SP", "MC"]):
                                                                                        try:
                                                                                            try:
                                                                                                histo_search[out_print_name.replace(Correction_Name, "mm0_NoELC")].gr2.SetMarkerColor(12)
                                                                                            except:
                                                                                                try:
                                                                                                    histo_search[out_print_name.replace(Correction_Name, "mm0_NoELC")] = Find_And_Slice_Histo(RDF=rdf_List[str((EvntType, Bending_Type, Data_Run))], NAME=out_print.replace(Correction_Name, "mm0_NoELC"), EVENT=EvntType, PARTICLE=Particle_Mom, BENDING=Bending_Type, OUT_Q="Histo", Pass_Type=Data_Run)
                                                                                                except Exception as e:
                                                                                                    print("".join([color.RED, "\n\n", str(e), "\n\n", color.END]))
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mm0_NoELC")].gr2.SetMarkerColor(12)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mm0_NoELC")].gr2.SetLineColor(12)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mm0_NoELC")].gr2.SetMarkerStyle(1)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mm0_NoELC")].gr2.SetMarkerSize(1)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mm0_NoELC")].gr2.SetLineStyle(2)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mm0_NoELC")].gr2.SetLineWidth(4)

                                                                                            Draw_Canvas(canvas_search[canvas_name_full], 1 if(Sector_Num in [0, "all"]) else Sector_Num, 0.05, 0, -0.02, -0.02)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mm0_NoELC")].gr2.Draw("PL same")
                                                                                            Legend[Legend_Name].AddEntry(histo_search[out_print_name.replace(Correction_Name, "mm0_NoELC")].gr2, "#color[12]{Uncorrected}" if(event_type not in ["DP"]) else "#color[12]{#splitline{Uncorrected}{(No Mom/Energy Cors)}}", "lp")
                                                                                        except:
                                                                                            Legend[Legend_Name].SetNColumns(2)
                                                                                    else:
                                                                                        Legend[Legend_Name].SetNColumns(2)
                                                                                        
                                                                                    if(event_type in ["DP"] and Correction_Name not in ["mmEF_PipMMEF", "mmEF_PipMMEF_NoELC"]):
                                                                                        Legend[Legend_Name].SetNColumns(2)
                                                                                        try:
                                                                                            try:
                                                                                                histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2.SetMarkerColor(3)
                                                                                                histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF_NoELC")].gr2.SetMarkerColor(6)
                                                                                            except:
                                                                                                try:
                                                                                                    histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")]       = Find_And_Slice_Histo(RDF=rdf_List[str((EvntType, Bending_Type, Data_Run))], NAME=out_print.replace(Correction_Name, "mmEF_PipMMEF"),       EVENT=EvntType, PARTICLE=Particle_Mom, BENDING=Bending_Type, OUT_Q="Histo", Pass_Type=Data_Run)
                                                                                                    histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF_NoELC")] = Find_And_Slice_Histo(RDF=rdf_List[str((EvntType, Bending_Type, Data_Run))], NAME=out_print.replace(Correction_Name, "mmEF_PipMMEF_NoELC"), EVENT=EvntType, PARTICLE=Particle_Mom, BENDING=Bending_Type, OUT_Q="Histo", Pass_Type=Data_Run)
                                                                                                except Exception as e:
                                                                                                    print("".join([color.RED, "\n\n", str(e), "\n\n", color.END]))
#                                                                                             histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2.SetMarkerColor(8)
#                                                                                             histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2.SetLineColor(8)
#                                                                                             histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2.SetMarkerStyle(3)# 33)
#                                                                                             histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2.SetMarkerSize(1)
#                                                                                             histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2.SetLineStyle(2)
#                                                                                             histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2.SetLineWidth(3)

                                                                                            histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2.SetMarkerColor(46)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2.SetLineColor(46)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2.SetMarkerStyle(3)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2.SetMarkerSize(1)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2.SetLineStyle(2)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2.SetLineWidth(3)
                                                                                            
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF_NoELC")].gr2.SetMarkerColor(6)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF_NoELC")].gr2.SetLineColor(6)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF_NoELC")].gr2.SetMarkerStyle(1)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF_NoELC")].gr2.SetMarkerSize(1)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF_NoELC")].gr2.SetLineStyle(2)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF_NoELC")].gr2.SetLineWidth(4)

                                                                                            Draw_Canvas(canvas_search[canvas_name_full], 1 if(Sector_Num in [0, "all"]) else Sector_Num, 0.05, 0, -0.02, -0.02)
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2.Draw("PL same")
                                                                                            histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF_NoELC")].gr2.Draw("PL same")
                                                                                            histo_search[out_print_name].gr2.Draw("P same")
                                                                                            
#                                                                                             Legend[Legend_Name].AddEntry(histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2, "#color[8]{No Proton (Mom) Cors}", "lp")
                                                                                            Legend[Legend_Name].AddEntry(histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")].gr2, "#color[46]{No Proton (Mom) Cors}", "lp")
                                                                                            Legend[Legend_Name].AddEntry(histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF_NoELC")].gr2, "#color[6]{#splitline{No Proton Corrections}{(Energy/Mom)}}", "lp")
                                                                                        except:
                                                                                            Legend[Legend_Name].SetNColumns(2)
                                                                                    else:
                                                                                        Legend[Legend_Name].SetNColumns(2)
                                                                                        
                                                                                        

                                                                                    if(Sector_Num in [6, 0, "all"]):
                                                                                        print("".join(["\n\nLegend name: ", Legend_Name]))
                                                                                        Draw_Canvas(canvas_search[canvas_name_full], 1 if(Sector_Num in [0, "all"]) else Sector_Num, 0.05, 0, -0.02, -0.02)
                                                                                        Legend[Legend_Name].Draw()


                                                                        if("Dmom_" in str(out_print)):
                                                                            type_of_correction = "pol2"

                                                                            histo_clone[out_print_name] = histo_search[out_print_name].gr2.Clone()

                                                                            try:
                                                                                histo_clone[(out_print_name, "up")]   = histo_search[out_print_name].gr2_sigma_up.Clone()
                                                                                histo_clone[(out_print_name, "down")] = histo_search[out_print_name].gr2_sigma_down.Clone()
                                                                                histo_clone[(out_print_name, "up")].SetMarkerColor(root_color.Green)
                                                                                histo_clone[(out_print_name, "up")].SetLineColor(root_color.Green)
                                                                                histo_clone[(out_print_name, "down")].SetMarkerColor(root_color.Green)
                                                                                histo_clone[(out_print_name, "down")].SetLineColor(root_color.Green)

                                                                                histo_clone[(out_print_name, "up")].Draw("EP same")
                                                                                histo_clone[(out_print_name, "down")].Draw("EP same")

                                                                                canvas_search[canvas_name_full].Modified()
                                                                                canvas_search[canvas_name_full].Update()

                                                                                if("D_Angle_V3" in out_print):
                                                                                    Tline_Simple_Test_1 = ROOT.TLine()
                                                                                    Tline_Simple_Test_1.SetLineColor(2)
                                                                                    Tline_Simple_Test_1.SetLineWidth(2)

                                                                                    Tline_Simple_Test_1.DrawLine(5.5, 183, 9.6, 183)

                                                                                    Tline_Simple_Test_2 = ROOT.TLine()
                                                                                    Tline_Simple_Test_2.SetLineColor(2)
                                                                                    Tline_Simple_Test_2.SetLineWidth(2)

                                                                                    Tline_Simple_Test_2.DrawLine(5.5, 177, 9.6, 177)

                                                                            except Exception as e:
                                                                                print("".join([color.Error, "Error with Sigmas (Angles)", color.END, "\n", str(e)]))

                                                                            if(Get_Dp_Cors == "yes"):
                                                                                Print_Correction_Function(histo_clone[out_print_name], "none", Correction_Name, Sector_Num, "el" if("Dmom_pel" in str(out_print)) else "pip" if("Dmom_pip" in str(out_print)) else "pro" if("Dmom_pro" in str(out_print)) else "error", "", type_of_correction)

                                                                        if("HWC_Histo_All" in out_print and "SP" != event_type):
                                                                            histo_search[out_print_name].gr2.SetMarkerColor(root_color.Red)
                                                                            if("not" not in Get_WM_Cuts):
                                                                                histo_search[out_print_name].gr2_Cut_Range_Up.SetMarkerColor(root_color.Green)
                                                                                histo_search[out_print_name].gr2_Cut_Range_Up.SetLineColor(root_color.Green)
                                                                                histo_search[out_print_name].gr2_Cut_Range_Down.SetMarkerColor(root_color.Green)
                                                                                histo_search[out_print_name].gr2_Cut_Range_Down.SetLineColor(root_color.Green)

                                                                                histo_search[out_print_name].gr2_Cut_Range_Up.Draw("P same")
                                                                                histo_search[out_print_name].gr2_Cut_Range_Down.Draw("P same")

                                                                    except Exception as e:
                                                                        print("".join([color.Error, "\nFailed to print peak positions...\nERROR: ", color.END, str(e), "\n"]))

                                                                if("Histo_P_v_Th_" in out_print and "local" in out_print):
                                                                    histo_search[out_print_name].GetYaxis().SetRangeUser(-35, 45)
                                                                if("Histo_P_v_Th_" in out_print):# and 'Calculated Exclusivity Cuts' in out_print):
                                                                    
                                                                    Mom_Cut_Upper = 7.25 if(Particle_Mom == "pip") else (9.7 if("SP" not in event_type) else 9.5) if(Particle_Mom == "el") else 3.2  if(Particle_Mom == "pro") else 0
                                                                    Mom_Cut_Lower = 0.75 if(Particle_Mom == "pip") else (9.2 if("SP" not in event_type) else 2.0) if(Particle_Mom == "el") else 0.45 if(Particle_Mom == "pro") else 0
                                                                    
                                                                    if(("Spring" not in str(Data_Run)) and False):
                                                                        if(event_type not in ["DP", "P0"] or Particle_Mom != "el"):
                                                                            Tline_Simple_Cut_Upper = ROOT.TLine()
                                                                            Tline_Simple_Cut_Upper.SetLineWidth(3)
                                                                            Tline_Simple_Cut_Upper.SetLineColor(root_color.Red)
                                                                            Tline_Simple_Cut_Upper.DrawLine(Mom_Cut_Upper, 0, Mom_Cut_Upper, 33 if(Particle_Mom != "el") else 40)

                                                                            Tline_Simple_Cut_Lower = ROOT.TLine()
                                                                            Tline_Simple_Cut_Lower.SetLineWidth(3)
                                                                            Tline_Simple_Cut_Lower.SetLineColor(root_color.Red)
                                                                            Tline_Simple_Cut_Lower.DrawLine(Mom_Cut_Lower, 0, Mom_Cut_Lower, 40 if(Particle_Mom != "el") else 33)
                                                                    else:
                                                                        histo_search[out_print_name].GetYaxis().SetRangeUser(-35, 75 if(Particle_Mom != "el") else 55)
                                                                        if("Spring" in str(Data_Run)):
                                                                            Mom_Cut_Upper = 7.25 if(Particle_Mom == "pip") else (9.5 if("SP" not in event_type) else 9.0) if(Particle_Mom == "el") else 3.2  if(Particle_Mom == "pro") else 0
                                                                            Mom_Cut_Lower = 0.75 if(Particle_Mom == "pip") else (8.0 if("SP" not in event_type) else 2.0) if(Particle_Mom == "el") else 0.45 if(Particle_Mom == "pro") else 0
                                                                        else:
                                                                            Title_Temp = histo_search[out_print_name].GetTitle()
                                                                            Title_Temp = Title_Temp.replace("Cut Applied: Calculated Exclusivity Cuts", "")
                                                                            # Title_Temp = Title_Temp.replace("- Shifted", "")
                                                                            histo_search[out_print_name].SetTitle(Title_Temp)
                                                                            Mom_Cut_Lower, Mom_Cut_Upper, Mom_Cut_Increment = Fitting_Lines(Histo_Type="Dmom_p", Event_Type=event_type, Bending_Type=Bending_Type, Particle=Particle_Mom, Missing_Mass_Type="None", DataSet=Data_Run, Sector=1)[0]
                                                                            # if(("SP" in event_type) and ("el" in Particle_Mom)):
                                                                            #     Mom_Cut_Upper = Fitting_Lines(Histo_Type="Dmom_p", Event_Type="EO", Bending_Type=Bending_Type, Particle=Particle_Mom, Missing_Mass_Type="None", DataSet=Data_Run, Sector=1)[0][1]
                                                                            if("EO" in event_type):
                                                                                Mom_Cut_Lower = Mom_Cut_Upper - 2*Mom_Cut_Increment
                                                                                print(f"Mom_Cut_Lower = {Mom_Cut_Lower}")
                                                                                print(f"Mom_Cut_Upper = {Mom_Cut_Upper}")
                                                                                
                                                                            
                                                                        if(event_type not in ["DP", "P0"] or Particle_Mom != "el"):
                                                                            Tline_Simple_Cut_Upper = ROOT.TLine()
                                                                            Tline_Simple_Cut_Upper.SetLineWidth(3)
                                                                            Tline_Simple_Cut_Upper.SetLineColor(root_color.Red)
                                                                            Tline_Simple_Cut_Upper.DrawLine(Mom_Cut_Upper, 0, Mom_Cut_Upper, 45 if(Particle_Mom != "el") else 35)

                                                                            Tline_Simple_Cut_Lower = ROOT.TLine()
                                                                            Tline_Simple_Cut_Lower.SetLineWidth(3)
                                                                            Tline_Simple_Cut_Lower.SetLineColor(root_color.Red)
                                                                            Tline_Simple_Cut_Lower.DrawLine(Mom_Cut_Lower, 0, Mom_Cut_Lower, 45 if(Particle_Mom != "el") else 35)

                                                                if("Histo_Th_v_Phi_" in out_print and "local" in out_print):
                                                                    histo_search[out_print_name].GetXaxis().SetRangeUser(-35, 45)
                                                                    
                                                                    if(("Spring" in str(Data_Run)) or True):
                                                                        Phi_Bin_ranges = 5 if(Particle_Mom == "el") else 10
                                                                        
                                                                        histo_search[out_print_name].GetXaxis().SetRangeUser(-35, 35)
                                                                        histo_search[out_print_name].GetYaxis().SetRangeUser(0,   60)
                                                                        
                                                                        Title_Temp = histo_search[out_print_name].GetTitle()
                                                                        Title_Temp = Title_Temp.replace("Cut Applied: Calculated Exclusivity Cuts", "")
                                                                        # Title_Temp = Title_Temp.replace("- Shifted", "")
                                                                        histo_search[out_print_name].SetTitle(Title_Temp)
                                                                        
                                                                        Tline_Simple_Bin_Upper = ROOT.TLine()
                                                                        Tline_Simple_Bin_Upper.SetLineWidth(4)
                                                                        Tline_Simple_Bin_Upper.SetLineColor(root_color.Green)
                                                                        Tline_Simple_Bin_Upper.DrawLine(Phi_Bin_ranges,  0,  Phi_Bin_ranges, 40)

                                                                        Tline_Simple_Bin_Lower = ROOT.TLine()
                                                                        Tline_Simple_Bin_Lower.SetLineWidth(4)
                                                                        Tline_Simple_Bin_Lower.SetLineColor(root_color.Green)
                                                                        Tline_Simple_Bin_Lower.DrawLine(-Phi_Bin_ranges, 0, -Phi_Bin_ranges, 40)
                                                                        
                                                                        
                                                                        latex_Center_Title = "".join(["#splitline{Center Bin}{-",        str(Phi_Bin_ranges), "#circ < #phi_{", "#pi^{+}" if(Particle_Mom == "pip") else str(Particle_Mom), "} < ",  str(Phi_Bin_ranges), "#circ}"])
                                                                        latex_Lower_Title  = "".join(["#splitline{Negative Bin}{#phi_{",                                        "#pi^{+}" if(Particle_Mom == "pip") else str(Particle_Mom), "} < -", str(Phi_Bin_ranges), "#circ}"])
                                                                        latex_Upper_Title  = "".join(["#splitline{Positive Bin}{#phi_{",                                        "#pi^{+}" if(Particle_Mom == "pip") else str(Particle_Mom), "} > ",  str(Phi_Bin_ranges), "#circ}"])
                                                                        latex_Center = ROOT.TLatex()
                                                                        latex_Center.SetTextSize(0.025)
                                                                        latex_Center.SetTextAlign(12)
                                                                        latex_Center.DrawLatex(-4,                      3, latex_Center_Title)
                                                                        
                                                                        latex_Lower  = ROOT.TLatex()
                                                                        latex_Lower.SetTextSize(0.025)
                                                                        latex_Lower.SetTextAlign(12)
                                                                        latex_Lower.DrawLatex(-Phi_Bin_ranges - 9.25,  3, latex_Lower_Title)
                                                                        
                                                                        latex_Upper  = ROOT.TLatex()
                                                                        latex_Upper.SetTextSize(0.025)
                                                                        latex_Upper.SetTextAlign(12)
                                                                        latex_Upper.DrawLatex(Phi_Bin_ranges  + 1.25,  3, latex_Upper_Title)
                                                                    
                                                                    
                                                                    
#                                                                 if("Histo_Th_v_Phi_" in out_print):

#                                                                     Tline_Simple_Bin_Upper = ROOT.TLine()
#                                                                     Tline_Simple_Bin_Upper.SetLineWidth(4)
#                                                                     Tline_Simple_Bin_Upper.SetLineColor(root_color.Green)
#                                                                     Tline_Simple_Bin_Upper.DrawLine(5  if(Particle_Mom == "el") else  10, 0,  5 if(Particle_Mom == "el") else  10, 32)

#                                                                     Tline_Simple_Bin_Lower = ROOT.TLine()
#                                                                     Tline_Simple_Bin_Lower.SetLineWidth(4)
#                                                                     Tline_Simple_Bin_Lower.SetLineColor(root_color.Green)
#                                                                     Tline_Simple_Bin_Lower.DrawLine(-5 if(Particle_Mom == "el") else -10, 0, -5 if(Particle_Mom == "el") else -10, 32)
                                                                    
                                                                    
                                                                if("Histo_P_v_Phi_" in out_print and "local" in out_print):
                                                                    histo_search[out_print_name].GetYaxis().SetRangeUser(-100, 100)
                                                                    # if('Calculated Exclusivity Cuts' in out_print):

                                                                    Mom_Cut_Upper = 7.25 if(Particle_Mom == "pip") else (9.7 if("SP" not in event_type) else 9.5) if(Particle_Mom == "el") else 3.2  if(Particle_Mom == "pro") else 0
                                                                    Mom_Cut_Lower = 0.75 if(Particle_Mom == "pip") else (9.2 if("SP" not in event_type) else 2.0) if(Particle_Mom == "el") else 0.45 if(Particle_Mom == "pro") else 0
                                                                    
                                                                    if(("Spring" not in str(Data_Run)) and False):
                                                                        if(event_type not in ["DP", "P0"] or Particle_Mom != "el"):
                                                                            Tline_Simple_Cut_Upper = ROOT.TLine()
                                                                            Tline_Simple_Cut_Upper.SetLineWidth(3)
                                                                            Tline_Simple_Cut_Upper.SetLineColor(root_color.Red)
                                                                            Tline_Simple_Cut_Upper.DrawLine(Mom_Cut_Upper, -100, Mom_Cut_Upper, 70 if(Particle_Mom != "el") else 100)

                                                                            Tline_Simple_Cut_Lower = ROOT.TLine()
                                                                            Tline_Simple_Cut_Lower.SetLineWidth(3)
                                                                            Tline_Simple_Cut_Lower.SetLineColor(root_color.Red)
                                                                            Tline_Simple_Cut_Lower.DrawLine(Mom_Cut_Lower, -100, Mom_Cut_Lower, 100 if(Particle_Mom != "el") else 70)

                                                                        # Tline_Simple_Bin_Upper = ROOT.TLine()
                                                                        # Tline_Simple_Bin_Upper.SetLineWidth(4)
                                                                        # Tline_Simple_Bin_Upper.SetLineColor(root_color.Green)
                                                                        # Tline_Simple_Bin_Upper.DrawLine(0,  5 if(Particle_Mom == "el") else  10, 32,  5 if(Particle_Mom == "el") else 10)

                                                                        # Tline_Simple_Bin_Lower = ROOT.TLine()
                                                                        # Tline_Simple_Bin_Lower.SetLineWidth(4)
                                                                        # Tline_Simple_Bin_Lower.SetLineColor(root_color.Green)
                                                                        # Tline_Simple_Bin_Lower.DrawLine(0, -5 if(Particle_Mom == "el") else -10, 32, -5 if(Particle_Mom == "el") else -10)
                                                                    else:
                                                                        histo_search[out_print_name].GetYaxis().SetRangeUser(-40, 90 if(Particle_Mom != "el") else 80)
                                                                        if("Spring" in str(Data_Run)):
                                                                            Mom_Cut_Upper = 7.25 if(Particle_Mom == "pip") else (9.5 if("SP" not in event_type) else 9.0) if(Particle_Mom == "el") else 3.2  if(Particle_Mom == "pro") else 0
                                                                            Mom_Cut_Lower = 0.75 if(Particle_Mom == "pip") else (8.0 if("SP" not in event_type) else 2.0) if(Particle_Mom == "el") else 0.45 if(Particle_Mom == "pro") else 0
                                                                        else:
                                                                            Title_Temp = histo_search[out_print_name].GetTitle()
                                                                            Title_Temp = Title_Temp.replace("Cut Applied: Calculated Exclusivity Cuts", "")
                                                                            # Title_Temp = Title_Temp.replace("- Shifted", "")
                                                                            histo_search[out_print_name].SetTitle(Title_Temp)
                                                                            Mom_Cut_Lower, Mom_Cut_Upper, Mom_Cut_Increment = Fitting_Lines(Histo_Type="Dmom_p", Event_Type=event_type, Bending_Type=Bending_Type, Particle=Particle_Mom, Missing_Mass_Type="None", DataSet=Data_Run, Sector=1)[0]
                                                                            # if(("SP" in event_type) and ("el" in Particle_Mom)):
                                                                            #     Mom_Cut_Upper = Fitting_Lines(Histo_Type="Dmom_p", Event_Type="EO", Bending_Type=Bending_Type, Particle=Particle_Mom, Missing_Mass_Type="None", DataSet=Data_Run, Sector=1)[0][1]
                                                                            if("EO" in event_type):
                                                                                Mom_Cut_Lower = Mom_Cut_Upper - 2*Mom_Cut_Increment
                                                                                print(f"Mom_Cut_Lower = {Mom_Cut_Lower}")
                                                                            
                                                                        if(event_type not in ["DP", "P0"] or Particle_Mom != "el"):
                                                                            Phi_Bin_ranges = 5 if(Particle_Mom == "el") else 10
                                                                            Tline_Simple_Bin_Upper = ROOT.TLine()
                                                                            Tline_Simple_Bin_Upper.SetLineWidth(3)
                                                                            Tline_Simple_Bin_Upper.SetLineColor(root_color.Green)
                                                                            Tline_Simple_Bin_Upper.DrawLine(0,  Phi_Bin_ranges, Mom_Cut_Upper,  Phi_Bin_ranges)

                                                                            Tline_Simple_Bin_Lower = ROOT.TLine()
                                                                            Tline_Simple_Bin_Lower.SetLineWidth(3)
                                                                            Tline_Simple_Bin_Lower.SetLineColor(root_color.Green)
                                                                            Tline_Simple_Bin_Lower.DrawLine(0, -Phi_Bin_ranges, Mom_Cut_Upper, -Phi_Bin_ranges)
                                                                            
                                                                            Tline_Simple_Cut_Upper = ROOT.TLine()
                                                                            Tline_Simple_Cut_Upper.SetLineWidth(3)
                                                                            Tline_Simple_Cut_Upper.SetLineColor(root_color.Red)
                                                                            Tline_Simple_Cut_Upper.DrawLine(Mom_Cut_Upper, -40, Mom_Cut_Upper, 40)

                                                                            Tline_Simple_Cut_Lower = ROOT.TLine()
                                                                            Tline_Simple_Cut_Lower.SetLineWidth(3)
                                                                            Tline_Simple_Cut_Lower.SetLineColor(root_color.Red)
                                                                            Tline_Simple_Cut_Lower.DrawLine(Mom_Cut_Lower, -40, Mom_Cut_Lower, 40)


                                                                if((("Histo_P_v_Th_" in out_print) or ("Histo_P_v_Phi_" in out_print)) and (Particle_Mom == "pro") and (event_type in ["P0"])):
                                                                    histo_search[out_print_name].GetXaxis().SetRangeUser(0, 6)
                                                                    
                                                                ROOT.gStyle.SetOptStat("i")
                                                                canvas_search[canvas_name_full].Modified()
                                                                canvas_search[canvas_name_full].Update()

                                                                # if("hmmCPARTall" not in out_print):
                                                                #     palette_move(canvas_search["".join([Canvas_Search_Name, "_", EvntType, "_",  str(Bending_Type).replace("bending", ""), "_", str(Data_Run)])], histo_search[out_print_name], 0, 0.005, -0.25 if("Dmom" not in out_print and "HWC_Histo_All" not in out_print and "hmmCPARTall" not in out_print) else 0, 0.01)
                                                                #     stats_box_all[out_print_name] = ""
                                                                #     statbox_move(histo_search[out_print_name], canvas_search["".join([Canvas_Search_Name, "_", EvntType, "_",  str(Bending_Type).replace("bending", ""), "_", str(Data_Run)])], stats_box_all[out_print_name], Sector_Num, "norm" if("Dmom" not in out_print and "HWC_Histo_All" not in out_print and "hmmCPARTall" not in out_print and "Histo_P_v_Th_" not in out_print and "Histo_P_v_Phi_" not in out_print and "Histo_Th_v_Phi_" not in out_print) else "off", 0.65, 0.65, 0.5, 0.5)
                                                                # else:
                                                                #     ROOT.gStyle.SetOptStat(0)

                                                                if("Histo_P_v_Th_" not in out_print and "Histo_P_v_Phi_" not in out_print and "Histo_Th_v_Phi_" not in out_print):
                                                                    try:
                                                                        Draw_Canvas(canvas_search[canvas_name_full], 1 if(Sector_Num in [0, "all"]) else Sector_Num, 0.05, 0, -0.02, -0.02)
                                                                        Tline_Simple = ROOT.TLine()
                                                                        Tline_Simple.SetLineWidth(2)
                                                                        Tline_Simple.SetLineColor(root_color.Black)
                                                                        Tline_Simple.DrawLine(Tline_Simple_X1, Tline_Simple_Y1, Tline_Simple_X2 + 0.5, Tline_Simple_Y2)
                                                                    except Exception as e:
                                                                        print("".join([color.Error, "Error in drawing standard line...\nERROR: ", color.END, str(e)]))
                                                                        
                                                                else:
                                                                    ROOT.gStyle.SetTitleH(0)
#                                                                     print(ROOT.gStyle.GetTitleH())
#                                                                     # histo_search[out_print_name].SetTitle(str(histo_search[out_print_name].GetTitle()).replace("Cuts}}}", "Cuts}}"))
#                                                                     # histo_search[out_print_name].SetTitle(str(histo_search[out_print_name].GetTitle()).replace(" }}}}{Cut", " }}}}}{Cut"))
#                                                                     # # histo_search[out_print_name].SetTitle(str(histo_search[out_print_name].GetTitle()).replace("Channel}{#splitline{#color[2]{", "Channel}{#color[2]{"))
#                                                                     print(histo_search[out_print_name].GetTitle())

                                                                    canvas_search[canvas_name_full].Modified()
                                                                    canvas_search[canvas_name_full].Update()

                                                                # print("".join(["\nWould be saving: \n", color.BBLUE]) + str("".join([str(canvas_name_full).replace(Correction_Name, corNameTitles(Correction_Name).replace("/", "_")), str(Extra_Saving_Name), ".png"])).replace(" ", "_") + color.END + "\n")    
                                                                if(SaveResultsQ == 'yes'):
                                                                    if(Sector_Num == Sector_Number_List_2[len(Sector_Number_List_2)-1]):
                                                                        # Save_Name = ("".join([str(canvas_name_full).replace(Correction_Name, corNameTitles(Correction_Name).replace("/", "_")), str(Extra_Saving_Name), ".png"])).replace(" ", "_")
                                                                        Save_Name = ("".join([str(canvas_name_full), str(Extra_Saving_Name), ".png"])).replace(" ", "_")
                                                                        Save_Name = str(str(str(str(Save_Name.replace("'", "")).replace(",", "_")).replace("(", "_")).replace(")", "")).replace("Sector_Number_List", "")
                                                                        while("__" in str(Save_Name)):
                                                                            Save_Name = str(Save_Name.replace("__", "_"))
                                                                        Save_Name = str(Save_Name.replace("_1_regall_3_", "_"))
                                                                        Save_Name = str(Save_Name.replace("_-_", "-"))
                                                                        Save_Name = str(Save_Name.replace("3_Region_Option_List", "All_Phi_Bins"))
                                                                        Save_Name = str(Save_Name.replace("el_el", "el")).replace("pip_pip", "pip")
                                                                        if((Save_Name in List_of_Saved_Images) and ("hmmCPARTall" not in str(Save_Name))):
                                                                            for ii in range(2, 21):
                                                                                if(str(str(Save_Name.replace(".png", f"_Version_{ii}.png")).replace(".pdf", f"_Version_{ii}.pdf")) not in List_of_Saved_Images):
                                                                                    Save_Name = str(str(Save_Name.replace(".png", f"_Version_{ii}.png")).replace(".pdf", f"_Version_{ii}.pdf"))
                                                                                    break
                                                                                elif(ii >= 20):
                                                                                    print(f"\n{color.ERROR}More than 20 versions of {color.UNDERLINE}Save_Name = {Save_Name}{color.END_B}{color.RED} were made...{color.END}\n")
                                                                                    Save_Name = str(str(Save_Name.replace(".png", f"_Version_Last.png")).replace(".pdf", f"_Version_Last.pdf"))
                                                                        List_of_Saved_Images.append(Save_Name)
                                                                        print(str(f"\nSaving: \n{color.BBLUE}{Save_Name}{color.END}\n"))
                                                                        # print(str(f"\nSaving: \n{color.BBLUE}{Save_Name}{color.END}\n").replace(".png", ".pdf"))
                                                                        try:
                                                                            # Get the list of all objects in the TCanvas and filter TPads
                                                                            pads = [obj for obj in canvas_search[canvas_name_full].GetListOfPrimitives() if isinstance(obj, ROOT.TPad)]
                                                                            # Check if there are exactly 6 TPads
                                                                            if(len(pads) == 6):
                                                                                # Set the position and size of each TPad for a 2x3 layout
                                                                                pads[0].SetPad(0.0, 0.5, 0.33, 1.0)  # Top-left
                                                                                pads[2].SetPad(0.33, 0.5, 0.66, 1.0) # Top-middle
                                                                                pads[4].SetPad(0.66, 0.5, 1.0, 1.0)  # Top-right
                                                                                pads[1].SetPad(0.0, 0.0, 0.33, 0.5)  # Bottom-left
                                                                                pads[3].SetPad(0.33, 0.0, 0.66, 0.5) # Bottom-middle
                                                                                pads[5].SetPad(0.66, 0.0, 1.0, 0.5)  # Bottom-right
                                                                                # # Adjust margins for each TPad if necessary
                                                                                # for pad in pads:
                                                                                #     pad.SetLeftMargin(0.1)
                                                                                #     pad.SetRightMargin(0.05)
                                                                                #     pad.SetTopMargin(0.05)
                                                                                #     pad.SetBottomMargin(0.1)
                                                                                #     pad.Update()
                                                                            else:
                                                                                print(f"The TCanvas contains {len(pads)} TPads, which is not equal to 6. No adjustments made.")
                                                                        except:
                                                                            print(f"{color.RED}Error in redrawing the TPads...\nTraceback: \n{color.END_B}{str(traceback.format_exc())}{color.END}")
                                                                        # canvas_search[canvas_name_full].SetLeftMargin(0.1)    # Adjust the left margin if necessary
                                                                        # canvas_search[canvas_name_full].SetRightMargin(0.01)  # Adjust the right margin
                                                                        # canvas_search[canvas_name_full].SetTopMargin(0.01)    # Adjust the top margin
                                                                        # canvas_search[canvas_name_full].SetBottomMargin(0.1)  # Adjust the bottom margin if necessary
                                                                        canvas_search[canvas_name_full].Update()
                                                                        canvas_search[canvas_name_full].SaveAs(Save_Name)
                                                                        # canvas_search[canvas_name_full].SaveAs(Save_Name.replace(".png", ".pdf"))

            ##=========================================================##===================================##=========================================================##
            ##=========================================================##       Drawing 1D Histograms       ##=========================================================##
            ##=========================================================##===================================##=========================================================##

                                                                if("zoom" not in Extra_Saving_Name and Run_1D_Q and "Histo_P_v_Th_" not in out_print and "Histo_P_v_Phi_" not in out_print and "Histo_Th_v_Phi_" not in out_print and not ("HWC_Histo_All" in out_print and "SP" in event_type)):
                                                                    # blank_Canvas = Canvas_Create(Name="test_blank", Num_Columns=1, Num_Rows=1, Size_X=600, Size_Y=800, cd_Space=0)
                                                                    try:
                                                                        # if(Sector_Num == Sector_Number_List_2[0]):
                                                                        Canvas_Name_1D = "".join([str(Canvas_Search_Name.replace("Region_Option_List", str(Region_Option))), str(multi_file_str)])#.replace("Sector_Number_List", "".join(["Sector_", str(Sector_Num)]))
                                                                        # print("".join([color.BGREEN, '\nout_print_name = \n\t', str(out_print_name), '\nCanvas_Search_Name = \n\t', str(Canvas_Search_Name), '\nCanvas_Name_1D = \n\t', str(Canvas_Name_1D), '\nSector_Num = \n\t', str(Sector_Num), "\n", color.END]))
                                            
                                                                        if(False or ((event_type in ["DP"]) and (Correction_Name not in ["mmEF_PipMMEF", "mm0_NoELC"]) and ("hmmCPARTall" in out_print))):
                                                                            try:
                                                                                Draw_1D_Histos_with_Canvas([histo_search[out_print_name], histo_search[out_print_name.replace(Correction_Name, "mm0_NoELC")], histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF")], histo_search[out_print_name.replace(Correction_Name, "mmEF_PipMMEF_NoELC")]], canvas_search, Canvas_Name_1D, Sector_Num, SaveResultsQ)
                                                                            except Exception as e:
                                                                                print("".join([color.Error, "ERROR IN INCLUDING THE EXTRA 1D HISTOGRAMS: ", str(e), color.END_R, "\nTraceback: \n", color.END, str(traceback.format_exc())]))
                                                                                Draw_1D_Histos_with_Canvas(histo_search[out_print_name], canvas_search, Canvas_Name_1D, Sector_Num, SaveResultsQ)
#                                                                         else:
#                                                                             Draw_1D_Histos_with_Canvas(histo_search[out_print_name], canvas_search, Canvas_Name_1D, Sector_Num, SaveResultsQ)
                                                                        # blank_Canvas = Canvas_Create(Name="test_blank", Num_Columns=3, Num_Rows=2, Size_X=1500, Size_Y=1200, cd_Space=0)
                                                                        break


                                                                    except:
                                                                        print("".join([color.Error, "Failed to print 1D Histograms for: ", color.END, "histo_search[", str(out_print_name), "]\n", str(traceback.format_exc())]))



    print(f"\n\nTotal number found: {color.BOLD}{str(search_count)}{color.END}")
else:
    print("\nNot running this cell\n")
    
    
# if(List_of_WM_Peaks != {}):
#     try:
#         if("no" not in Get_WM_Cuts and Print_Canvas_Q == 'y'):
#             for Part in Particle_Mom_List:

#                 print("".join(["\n\n\n\nCuts for ", color.BOLD, Part, color.END, ":\n"]))

#                 print(""" 
#                     auto beam = ROOT::Math::PxPyPzMVector(0, 0, 10.6041, 0);
#                     auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, 0.938);
#                     auto ele = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);

#                     auto WM_Vector = beam + targ - ele;

#                     auto cut_up = 1.3;
#                     auto cut_down = 0.7;
#                 """)

#                 for Sec in Sector_Number_List:
#                     if(Sec == 0 or Sec == "all"):
#                         continue
#                     Print_Cut_Func(WM_Cuts_List[str((Part, Sec))][0], WM_Cuts_List[str((Part, Sec))][1], Part, Sec)

#                 print("""
#                     return (WM_Vector.M() < cut_up && WM_Vector.M() > cut_down);
#                 """)
#     except:
#         print(color.BOLD + "\nFailed to get the Invarient Mass Cuts\n" + color.END)
        
        
#     for Cut in Extra_Cut_Option:
#         if("Calculated Exclusivity" in Cut or "Invariant" in Cut):
#             continue
#         histo_title = "".join(["HWC_Histo_All_('mm0', SEC_NUM, '1', 'regall', 'el', 'el', '", str(Cut),"')"])
#         Cut_Final = ""
#         print("".join(["""
#         // For Invariant Mass Cut (Based on """, color.BBLUE, str(Cut) if(str(Cut) != "") else "No Additional Cuts", color.END, "):"]))
#         for sec_num in [1, 2, 3, 4, 5, 6]:
#             try:
#                 Cut_Final = Print_Cut_By_Points(histo_search[histo_title.replace("SEC_NUM", str(sec_num))], sec_num, "el", "WM", Cut_Final)
#             except Exception as e:
#                 print("".join([color.Error, "ERROR: ", color.END, str(e)]))
#         print(Cut_Final)
#         print(color.RED + "\n===========================================================================\n" + color.END)

    
# for Extra_Cuts in D_Angle_Type:
#     # histo_title = "".join(["Dmom_Angle_Histo('mm0_NoELC', '', 'El Sector SEC_NUM', '1', 'regall', 'All Additional Cuts', '", str(Extra_Cuts), "')"])
#     # histo_title = "".join(["Dmom_Angle_Histo('mm0_NoELC', '', 'El Sector SEC_NUM', '1', 'regall', 'Extra Kinematic Cut', '", str(Extra_Cuts), "')"])
#     # histo_title = "".join(["Dmom_Angle_Histo('mm0_NoELC', '', 'El Sector SEC_NUM', '1', 'regall', 'Calculated Exclusivity Cuts', '", str(Extra_Cuts), "')"])
#     # histo_title = "".join(["Dmom_Angle_Histo('mm0_NoELC', '', 'El Sector SEC_NUM', '1', 'regall', ", "''" if("V3" in str(Extra_Cuts)) else "'Azimuthal Kinematic Cut'", ", '", str(Extra_Cuts), "')"])
#     histo_title = "".join(["Dmom_Angle_Histo('mm0', '', 'El Sector SEC_NUM', '1', 'regall', ", "''", ", '", str(Extra_Cuts), "')"])
#     print("".join(["    // For ", "∆Phi Cuts" if("V3" in Extra_Cuts) else "∆Theta Cuts", ":"]))
#     Cut_Final = ""
#     for sec_num in [1, 2, 3, 4, 5, 6]:
#         try:
#             Cut_Final = Print_Cut_By_Points(histo_search[histo_title.replace("SEC_NUM", str(sec_num))], sec_num, "el", "Phi" if("V3" in Extra_Cuts) else "Theta", Cut_Final)
#         except Exception as e:
#             print("".join([color.Error, "ERROR: ", color.END, str(e)]))
#     print(Cut_Final)














print("".join(["""
==============================================================================================================================================================
\n\t""", color.BBLUE, ".\n\n.\n\n.\n\n.\n\nDONE\n\n.\n\n.\n\n.\n\n.\n\n".replace("\n", "\n\t"), color.END, """
==============================================================================================================================================================
"""]))













if(any("Dmom" in histos_selected for histos_selected in List_of_Locate_name)):
    Tline_Simple_Baseline_Dp, Legend_test, canvas_test, Combined_Histo = {}, {}, {}, {}

    correction_type = "linear"
    correction_type = "quadratic"
    # correction_type = "complex_L"
    # correction_type = "complex_Q"
    
    Use_Split_Cor = "lower"
    Use_Split_Cor = "upper"
    Use_Split_Cor = "no"
    Used_Split_Op = False

    try:
        for Data_Run in Data_Run_List:
            print("".join(["\n\n", color.BGREEN, "Data From: ", color.BLUE, str(Data_Run).replace("_", " "), color.END]))

            for Bending_Type in Bending_Type_List:
                print("".join(["\n\t", color.BGREEN, str(Bending_Type), " Corrections", color.END]))

                for Particle in Particle_Mom_List:
                    print("".join(["\n\t", color.BGREEN, "∆P (", (str(Particle.replace("el", "El")).replace("pip", "Pi+")).replace("pro", "Pro"), ") Corrections\n", color.END]))

                    for region in Region_Option_List:
                        if(("regall" in [region]) and (len(Region_Option_List) > 1)):
                            continue
                        for ii in histo_search:

                            if("Sector 1" not in str(ii)):
                                continue

                            ii_true = ii

                            # print("\t", color.BOLD, ii_true, color.END)
                            if("Calculated Exclusivity Cuts" not in ii_true):
                                print(f"{color.RED} {ii_true} {color.END}is missing the exclusivity cuts...\n")
                                continue

                            for sec in [1, 2, 3, 4, 5, 6]:

                                ii = ii_true.replace("Sector 1", "".join(["Sector ", str(sec)]))

                                cd_num = 1 if("Sector 1" in ii) else 2 if("Sector 2" in ii) else 3 if("Sector 3" in ii) else 4 if("Sector 4" in ii) else 5 if("Sector 5" in ii) else 6 if("Sector 6" in ii) else "error"

                                if(True in Correction_Histo_Loop_Conditions(histo_ID=ii, CD_Check=cd_num, Sector=sec, Region=region, Particle_Option=Particle)):
                                    # print(color.RED, str(ii), color.END)
                                    # print(str(Correction_Histo_Loop_Conditions(histo_ID=ii, CD_Check=cd_num, Sector=sec, Region=region, Particle_Option=Particle)))
                                    continue

                                ii2 = ii
    #                             if("F_PipMM" not in str(ii)):
    #                                 continue


    #                             if("Pass2" not in Data_Run):
                                if(("SP" in str(ii)) and (Particle == "el")):
                                    # ii2 = (ii.replace("mmF_PipMMF", "mmF")).replace("SP", "EO")
                                    ii2 = (ii.replace( "F_PipMMF",      "F")).replace("SP", "EO")
                                    ii2 = (ii2.replace("F_PipMMEF",     "F"))
                                    ii2 = (ii2.replace( "_ELPipMM0",    ""))
                                    ii2 = (ii2.replace( "_ELPipMMfaP2", ""))
                                    if("EO" not in ii2):
                                        print("".join([color.RED, "\nERROR IN CHANNEL SELECTION...\n", color.END]))

                                if("DP" in str(ii)):
                                    # ii2 = (ii.replace("mmF_PipMMF", "mmF")).replace("SP", "EO")
                                    ii2 = (ii.replace( "F_PipMMF",  "F")).replace("DP", "P0")
                                    ii2 = (ii2.replace("F_PipMMEF", "F")).replace("DP", "P0")
                                    if("P0" not in ii2):
                                        print("".join([color.RED, "\nERROR IN CHANNEL SELECTION...\n", color.END]))


                                if("mm0" not in str(ii)):
                                    cor_Q = "".join(["Corrected", "".join([" (", "With (New) Pion" if("PipMMEF" in str(ii)) else "With (Old) Pion" if("PipMMF" in str(ii)) else "Without Pion" , " - Extended)" if("mmExF" in str(ii)) else " - With Elastic)" if("mmEF" in str(ii)) else ")"])])
                                    if("ProMMpro" in str(ii) and "Pro" not in cor_Q and "Elastic" in cor_Q):
                                        # print(ii)
                                        cor_Q = "".join([cor_Q.replace("Elastic)", "".join(["Elastic - Proton Cor", " (Double)" if("pro_QEF" in str(ii)) else "", " - Energy Loss" if("_NoELC" not in str(ii)) else "", ")"]))])
                                        # print(cor_Q)
                                    elif(("_NoELC" not in str(ii)) and (" - Energy Loss" not in cor_Q) and (Particle == "pro")):
                                        # print(ii)
                                        cor_Q = "".join([cor_Q.replace("Elastic)", "Elastic"), " - Energy Loss)"])
                                        # print(cor_Q)
                                else:
                                    cor_Q = "Uncorrected"

                                correction_Code_Name = "mm0" if("mm0" in str(ii)) else "mmEF" if("mmEF" in str(ii)) else "mmP2" if("mmP2" in str(ii)) else "mmRP2" if("mmRP2" in str(ii)) else "mmfaP2" if("mmfaP2" in str(ii)) else "mmError"
                                if(f"{correction_Code_Name}_" in str(ii)):
                                    correction_Code_Name = "".join([correction_Code_Name, "_", "EL" if("_ELPipMM"      in str(ii)) else ""])
                                correction_Code_Name = "".join([str(correction_Code_Name), ""       if( "PipMM"    not in str(ii)) else  "PipMMEF"     if("PipMMEF"     in str(ii)) else  "PipMMP2"      if("PipMMP2"      in str(ii)) else  "PipMM0"       if("PipMM0"       in str(ii)) else  "PipMMfaP2"    if("PipMMfaP2"    in str(ii)) else  "PipMMError"])
                                correction_Code_Name = "".join([str(correction_Code_Name), ""       if("_ProMMpro" not in str(ii)) else "_ProMMpro_EF" if("ProMMpro_EF" in str(ii)) else "_ProMMpro_REF" if("ProMMpro_REF" in str(ii)) else "_ProMMpro_LEF" if("ProMMpro_LEF" in str(ii)) else "_ProMMpro_QEF" if("ProMMpro_QEF" in str(ii)) else "_PipMMError"])
                                correction_Code_Name = "".join([str(correction_Code_Name), ""       if("_NoELC"    not in str(ii)) else "_NoELC"])

                                cor_Q = correction_Code_Name

                                if((any("_ELPipMM" in cor_test_str for cor_test_str in Correction_Name_List)) and ("_ELPipMM" not in correction_Code_Name)):
                                    print(f"{color.RED}\nSkipping Single Pion Corrections that lack the Pion Energy Loss Correction{color.END}")
                                    break



                                ref_can = "".join(["Dmom_pel_Histo_Combined_" if(Particle == "el") else "Dmom_pip_Histo_Final_" if(Particle == "pip") else "Dmom_pro_Histo_Final_" if(Particle == "pro") else "ERROR", str((region, cor_Q, Bending_Type, Data_Run))])
                                # ref_can = "".join(["Dmom_pel_Histo_Combined_" if(Particle == "el") else f"Dmom_{Particle}_Histo_Final_", str((region, cor_Q, Bending_Type, Data_Run))])

                                try:
                                    Legend_test[ref_can]
                                except:
                                    Legend_test[ref_can] = ROOT.TLegend(0.485, 0.325, 0.85, 0.125)
                                    Legend_test[ref_can].SetNColumns(1)
                                try:
                                    canvas_test[ref_can]
                                except:
                                    if(print_method == "hor"):
                                        canvas_test[ref_can] = ROOT.TCanvas(ref_can, ref_can, 1500, 1200)
                                        canvas_test[ref_can].Divide(3, 2, 0, 0)
                                    else:
                                        canvas_test[ref_can] = ROOT.TCanvas(ref_can, ref_can, 900, 1200)
                                        canvas_test[ref_can].Divide(2, 3, 0, 0)
                                    canvas_test[ref_can].SetGrid()

                                    ROOT.gStyle.SetAxisColor(16,'xy')
                                    ROOT.gStyle.SetOptFit(1)
                                    ROOT.gStyle.SetOptStat("emr")
                                    # ROOT.gStyle.SetOptStat(0)
                                    ROOT.gStyle.SetTitleY(1)
                                    ROOT.gStyle.SetTitleX(0.5)
                                    ROOT.gStyle.SetLegendTextSize(0.0275)

                                    canvas_test[ref_can].Draw()

                                # print(ii)
                                # print(ii2)

                                if(str(ii2) not in histo_search and Particle in ["el"]): # and Particle in ["el", "pro"]):
                                    print(f"{color.RED}\nError: Missing histogram...\n{color.END}")


                                Draw_Canvas(canvas_test[ref_can], cd_num, 0.05, 0, -0.02, 0)


                                Combined_Title = Find_And_Slice_Histo(RDF=rdf_List[str(("SP" if("SP" in str(ii)) else "DP", Bending_Type, Data_Run))], NAME=ii.replace("".join(["_SP" if("SP" in str(ii)) else "_DP", "_", str(Bending_Type).replace("bending", ""), "_", str(Data_Run)]), ""), EVENT="SP" if("SP" in str(ii)) else "DP", PARTICLE=Particle, BENDING=Bending_Type, OUT_Q="Title", Pass_Type=Data_Run)
                                Combined_Title = Combined_Title.replace("Cut Applied: Calculated Exclusivity Cuts", "")
                                histo_search[ii].SetTitle(Combined_Title)
                                histo_search[ii].gr2.SetTitle(Combined_Title)
                                if(Particle == "el"):
                                    if("In" in Bending_Type):
                                        if(sec == 3 and region == 'reg3'):
                                            Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])] = Merge_Histos(histo_search[ii], histo_search[ii2].gr2, "Extend", Num_Overlap=1)
                                        else:
                                            Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])] = Merge_Histos(histo_search[ii], histo_search[ii2].gr2, "Extend")
                                    else:
                                        # Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])]     = Merge_Histos(histo_search[ii], histo_search[ii2].gr2, "Extend", Num_Overlap=1)
                                        # Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])]     = Merge_Histos(histo_search[ii], histo_search[ii2].gr2, "Extend", Num_Overlap=3)
                                        Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])]     = Merge_Histos(histo_search[ii], histo_search[ii2].gr2, "Extend", Num_Overlap=2)
                                elif(Particle == "pip"):
                                    Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])] = histo_search[ii].gr2
                                    Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetXaxis().SetTitle("p_{#pi^{+}}")
                                    Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetYaxis().SetTitle("#Delta p_{#pi^{+}}")
                                elif(Particle == "pro"):
                                    try:
                                        fail_manual
                                        Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])] = Merge_Histos(histo_search[ii].gr2, histo_search[ii2].gr2)
                                    except:
                                        if("fail_manual" not in str(traceback.format_exc())):
                                            print("".join([color.Error, "Error:\n", color.END_R, str(traceback.format_exc()), color.END]))
                                        Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])] = histo_search[ii].gr2
                                    Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetXaxis().SetTitle("p_{Pro}")
                                    Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetYaxis().SetTitle("#Delta p_{Pro}")
                                    Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetXaxis().SetRangeUser(0, 3.5)




    #                             Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetYaxis().SetRangeUser(-0.15, 0.1)#-0.08, 0.1)
                                Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetYaxis().SetRangeUser(-0.1, 0.1)#-0.08, 0.1)
                                Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].SetMarkerColor(root_color.Red if(cor_Q != "Uncorrected") else root_color.Rust)
                                Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].SetLineColor(  root_color.Red if(cor_Q != "Uncorrected") else root_color.Rust)

                                Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].Draw("AP same")

                                if(Particle in ["el", "pro"]):
                                    histo_search[ii].gr2.SetMarkerStyle(20)
                                    histo_search[ii].gr2.SetMarkerSize(1)
                                    histo_search[ii].gr2.SetMarkerColor(root_color.Blue if(cor_Q != "Uncorrected") else root_color.Cyan)
                                    histo_search[ii].gr2.SetLineColor(  root_color.Blue if(cor_Q != "Uncorrected") else root_color.Cyan)

                                    histo_search[ii].gr2.Draw("P same")

                                Tline_Simple_Baseline_Dp[ii] = ROOT.TLine()
                                Tline_Simple_Baseline_Dp[ii].SetLineColor(root_color.Black)
                                Tline_Simple_Baseline_Dp[ii].SetLineWidth(2)

                                Tline_Simple_Baseline_Dp[ii].DrawLine(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetXaxis().GetXmin(), 0, Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetXaxis().GetXmax(), 0)

                                if(cd_num == 6):
                                    if("SP" in str(ii)):
                                        if(Particle == "el"):
                                            Legend_test[ref_can].AddEntry(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])], "#splitline{Contributions from}{Electron Only Channel}", "pl")
                                            Legend_test[ref_can].AddEntry(histo_search[ii].gr2, "#splitline{Contributions from}{e#pi^{+}(N) Channel}", "pl")
                                        else:
                                            Legend_test[ref_can].AddEntry(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])], "#splitline{Peaks from #Delta P Plots}{e#pi^{+}(N) Channel}", "pl")
                                    elif("DP" in str(ii)):
                                        # Legend_test[ref_can].AddEntry(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])], "#splitline{Contributions from}{ep(#pi^{0}) Channel}", "pl")
                                        Legend_test[ref_can].AddEntry(histo_search[ii].gr2, "#splitline{Contributions from}{ep#pi^{+}(#pi^{-}) Channel}", "pl")
                                    else:
                                        print("".join([color.RED, "\nUndefined Legend(?)\n", color.END]))

                                    Legend_test[ref_can].Draw()

                                fit_function = "pol1"
                                if(correction_type == "linear"):
                                    fit_function = "pol1"
                                if(correction_type == "quadratic"):
                                    fit_function = "pol2"


                                min_fit_range = 1.15*Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetXaxis().GetXmin()
                                if(min_fit_range < 0):
                                    min_fit_range = 0 if(Particle != "pro") else 0.25
                                # max_fit_range = 0.98*Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetXaxis().GetXmax()
                                max_fit_range = 0.9*Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetXaxis().GetXmax()

                                # print("min_fit_range =", min_fit_range, "max_fit_range =", max_fit_range)
                                if(("Out" in Bending_Type) and ("el" in Particle)):
                                    min_fit_range =  1.8
                                    max_fit_range = 10.4
                                #     print("(New) min_fit_range =", min_fit_range, "max_fit_range =", max_fit_range)

    #                             if((correction_type == "complex_Q") and (sec in [5, 6])):
    #                                 correction_type = "complex_L"

                                if(("Pass2" in Data_Run) and ("el" in Particle)):
                                    min_fit_range = 2.0
                                    max_fit_range = 9.5
                                if(("Pass2" in Data_Run) and ("pip" in Particle)):
                                    max_fit_range = 0.95*Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetXaxis().GetXmax()

                                if("Fall2018_Pass2" in Data_Run):
                                    # Switch_Point_EL   = 6.5 if(((sec in [1, 2, 3, 4, 6]) and (region in ['reg1'])) or ((sec in [1, 2, 4]) and (region in ['reg2'])) or ((sec in [1, 2, 3, 4, 5]) and (region in ['reg3']))) else 4.75
                                    Switch_Point_EL   = 6.5 if(sec in [1, 2, 4]) else 4.75
                                    if("In" in str(Bending_Type)):
                                        Switch_Point_EL = 7
                                    min_fit_range     = Fitting_Lines(Histo_Type="Dmom_p", Event_Type="SP", Bending_Type=Bending_Type, Particle=Particle, Missing_Mass_Type="None", DataSet="Fall2018_Pass2", Sector=1)[0][0]
                                    if("pip" in Particle):
                                        max_fit_range = Fitting_Lines(Histo_Type="Dmom_p", Event_Type="SP", Bending_Type=Bending_Type, Particle=Particle, Missing_Mass_Type="None", DataSet="Fall2018_Pass2", Sector=1)[0][1]
                                        if(Use_Split_Cor not in ["no"]):
                                            Used_Split_Op = True
                                            Switch_Point_Pip = 4.5 if(sec in [4, 5, 6]) else 5
                                            if("In" in str(Bending_Type)):
                                                Switch_Point_Pip = 2.5
                                            if(Use_Split_Cor in ["min", "low", "lower"]):
                                                max_fit_range = Switch_Point_Pip
                                                print(f"{color.BOLD}\n\n\n\n\n\nNEW MAX RANGE = {max_fit_range}\n\n\n\n\n{color.END}")
                                            else:
                                                min_fit_range = Switch_Point_Pip
                                                print(f"{color.BOLD}\n\n\n\n\n\nNEW MIN RANGE = {min_fit_range}\n\n\n\n\n{color.END}")
                                    else:
                                        max_fit_range = Fitting_Lines(Histo_Type="Dmom_p", Event_Type="EO", Bending_Type=Bending_Type, Particle=Particle, Missing_Mass_Type="None", DataSet="Fall2018_Pass2", Sector=1)[0][1]
                                        if(Use_Split_Cor not in ["no"]):
                                            Used_Split_Op = True
                                            if(Use_Split_Cor in ["min", "low", "lower"]):
                                                max_fit_range = Switch_Point_EL
                                                print(f"{color.BOLD}\n\n\n\n\n\nNEW MAX RANGE = {max_fit_range}\n\n\n\n\n{color.END}")
                                            else:
                                                min_fit_range = Switch_Point_EL
                                                print(f"{color.BOLD}\n\n\n\n\n\nNEW MIN RANGE = {min_fit_range}\n\n\n\n\n{color.END}")

                                fitting_line = ROOT.TF1("fit_function", "".join([fit_function, "(0)"]), min_fit_range, max_fit_range)
                                if(Particle == "pro" and "complex" in correction_type):
                                    min_fit_range = 0.4
    #                                 switch_point = 1.15 if(sec in [3]) else 1.25 if(sec in [1, 2, 5]) else 0.95 if(sec in [6]) else 1.5
                                    # switch_point = 1.25 if(sec in [1]) else 1.5 if(sec in [2]) else 1.05 if(sec in [3]) else 1.6 if(sec in [4]) else 1.3 if(sec in [5]) else 1.15 if(sec in [6]) else 1
                                    switch_point = 1.275 if(sec in [1]) else 1.5 if(sec in [2]) else 1.05 if(sec in [3]) else 1.6 if(sec in [4]) else 1.3 if(sec in [5]) else 1.15 if(sec in [6]) else 1
                                    switch_point = switch_point if(sec in [2, 3, 6]) else 1.4 if(sec in [1, 4]) else 1.5 if(sec in [5]) else switch_point
                                    if(correction_type == "complex_L"):
                                        fitting_line = ROOT.TF1("pol2_then_pol1", "".join(["((1 + TMath::Sign(1, (x - ", str(switch_point), ")))/2)*([pl1]*x + [pl0]) + ((1 + TMath::Sign(1, -(x - ", str(switch_point), ")))/2)*([pq2]*(x - ", str(switch_point), ")*(x - ", str(switch_point), ") + [pq1]*(x - ", str(switch_point), ") + ([pl1]*", str(switch_point), " + [pl0]))"]), min_fit_range, max_fit_range)
                                    else:
                                        fitting_line = ROOT.TF1("pol2_then_pol2", "".join(["((1 + TMath::Sign(1, -(x - ", str(switch_point), ")))/2)*([pf2]*x*x + [pf1]*x + [pf0]) + ((1 + TMath::Sign(1, (x - ", str(switch_point), ")))/2)*([ps2]*(x - ", str(switch_point), ")*(x - ", str(switch_point), ") + [ps1]*(x - ", str(switch_point), ") + ([pf2]*", str(switch_point), "*", str(switch_point), " + [pf1]*", str(switch_point), " + [pf0]))"]), min_fit_range, max_fit_range)
                                reg_color = root_color.Black if(region in ["regall", "reg1"]) else root_color.Red if(region == "reg2") else root_color.Green if(region == "reg3") else "error"

                                fitting_line.SetLineColor(reg_color)

                                fitting_line.SetParameter(0, 0)
                                fitting_line.SetParLimits(0, -1, 1)
                                fitting_line.SetParameter(1, 0)
                                fitting_line.SetParLimits(1, -10, 10)
                                if(correction_type == "quadratic"):
                                    fitting_line.SetParameter(2, 0)
                                    fitting_line.SetParLimits(2, -10, 10)


                                # print(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetTitle())
                                Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].Fit(fitting_line, "RQ")

                                statbox_move(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])], canvas_test[ref_can], Default_Stat_Obj={}, Sector=cd_num, Print_Method="norm", Y1_add=0.075, Y2_add=0.075, X1_add=0, X2_add=0)
                                # Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetFunction(str("fit_function")).SetLineColor(root_color.Black)
                                # Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].Fit(fit_function, "RQ")
                                # Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetFunction(fit_function).SetLineColor(root_color.Black)


    #                             if(correction_type in ["linear", "quadratic"]):
    #                                 cor_id_str = "".join(["// Sector ", str(sec) , " - Phi Region: ", "All" if("regall" in ref_can) else "Center" if("reg1" in ref_can) else "Negative" if("reg2" in ref_can) else "Positive" if("reg3" in ref_can) else "ERROR"])
    #                                     print("".join(["""
    #         // Sector """, str(sec) , " - Phi Region: ", "All" if("regall" in ref_can) else "Center" if("reg1" in ref_can) else "Negative" if("reg2" in ref_can) else "Positive" if("reg3" in ref_can) else "ERROR", """
    #         dp = """,  " dp +" if(("mm0" not in str(ii) and not ("el" not in Particle and ))) else "", """ ((1 + TMath::Sign(1, -(pp - """, str(switch_point), ")))/2)*((", str(par_pf2), ")*pp*pp + (", str(par_pf1), ")*pp + (", str(par_pf0), ")) + ((1 + TMath::Sign(1, (pp - ", str(switch_point), ")))/2)*((", str(par_ps2), ")*(pp - ", str(switch_point), ")*(pp - ", str(switch_point), ") + (", str(par_ps1), ")*(pp - ", str(switch_point), ") + ((", str(par_pf2), ")*", str(switch_point), "*", str(switch_point), " + (", str(par_pf1), ")*", str(switch_point), " + (", str(par_pf2), """)));
    #                                     """]))

                                try:
                                    # if("regall" in ref_can and (correction_type != "complex" and cor_Q != "Uncorrected")):
                                    if(("regall" in ref_can and (correction_type != "complex" and cor_Q != "Uncorrected")) or ("Out" in Bending_Type)):

                                        # Print_Correction_Function(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])], "".join([str(ref_can), "_Sector_", str(cd_num)]), "mm0" if(cor_Q == "Uncorrected") else "Corrected - New" if("mmEF" in str(ii)) else "Corrected", cd_num, Particle, region, correction_type, "Extended", Extra_Fit_Name="fit_function")
                                        Print_Correction_Function(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])], "".join([str(ref_can), "_Sector_", str(cd_num)]), str(correction_Code_Name), cd_num, Particle, region, correction_type, "Extended", Extra_Fit_Name="fit_function")

                                    if(Particle == "pro" and (correction_type == "complex_Q")):

                                        par_pf2 = round(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetFunction("pol2_then_pol2").GetParameter("pf2"), 8)
                                        if(abs(par_pf2) < 0.01):
                                            par_pf2 = "{:.4e}".format(par_pf2)
                                        else:
                                            par_pf2 = round(par_pf2, 5)

                                        par_pf1 = round(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetFunction("pol2_then_pol2").GetParameter("pf1"), 8)
                                        if(abs(par_pf1) < 0.01):
                                            par_pf1 = "{:.4e}".format(par_pf1)
                                        else:
                                            par_pf1 = round(par_pf1, 5)

                                        par_pf0 = round(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetFunction("pol2_then_pol2").GetParameter("pf0"), 8)
                                        if(abs(par_pf0) < 0.01):
                                            par_pf0 = "{:.4e}".format(par_pf0)
                                        else:
                                            par_pf0 = round(par_pf0, 5)

                                        par_ps2 = round(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetFunction("pol2_then_pol2").GetParameter("ps2"), 8)
                                        if(abs(par_ps2) < 0.01):
                                            par_ps2 = "{:.4e}".format(par_ps2)
                                        else:
                                            par_ps2 = round(par_ps2, 5)

                                        par_ps1 = round(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetFunction("pol2_then_pol2").GetParameter("ps1"), 8)
                                        if(abs(par_ps1) < 0.01):
                                            par_ps1 = "{:.4e}".format(par_ps1)
                                        else:
                                            par_ps1 = round(par_ps1, 5)


                                        print("".join(["""

            // Sector """, str(sec) , """
            dp = """,  " dp +" if("ProMMpro" in str(ii)) else "", """ ((1 + TMath::Sign(1, -(pp - """, str(switch_point), ")))/2)*((", str(par_pf2), ")*pp*pp + (", str(par_pf1), ")*pp + (", str(par_pf0), ")) + ((1 + TMath::Sign(1, (pp - ", str(switch_point), ")))/2)*((", str(par_ps2), ")*(pp - ", str(switch_point), ")*(pp - ", str(switch_point), ") + (", str(par_ps1), ")*(pp - ", str(switch_point), ") + ((", str(par_pf2), ")*", str(switch_point), "*", str(switch_point), " + (", str(par_pf1), ")*", str(switch_point), " + (", str(par_pf2), """)));

                                        """]))


                                    if(Particle == "pro" and (correction_type == "complex_L")):

                                        par_pl1 = round(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetFunction("pol2_then_pol1").GetParameter("pl1"), 8)
                                        if(abs(par_pl1) < 0.01):
                                            par_pl1 = "{:.4e}".format(par_pl1)
                                        else:
                                            par_pl1 = round(par_pl1, 5)

                                        par_pl0 = round(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetFunction("pol2_then_pol1").GetParameter("pl0"), 8)
                                        if(abs(par_pl0) < 0.01):
                                            par_pl0 = "{:.4e}".format(par_pl0)
                                        else:
                                            par_pl0 = round(par_pl0, 5)

                                        par_pq2 = round(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetFunction("pol2_then_pol1").GetParameter("pq2"), 8)
                                        if(abs(par_pq2) < 0.01):
                                            par_pq2 = "{:.4e}".format(par_pq2)
                                        else:
                                            par_pq2 = round(par_pq2, 5)

                                        par_pq1 = round(Combined_Histo["".join([str(ref_can), "_Sector_", str(cd_num)])].GetFunction("pol2_then_pol1").GetParameter("pq1"), 8)
                                        if(abs(par_pq1) < 0.01):
                                            par_pq1 = "{:.4e}".format(par_pq1)
                                        else:
                                            par_pq1 = round(par_pq1, 5)



                                        print("".join(["""

            // Sector """, str(sec) , """ (""", str(cor_Q), """)
            dp =""",  " dp +" if("ProMMpro" in str(ii)) else "", """ ((1 + TMath::Sign(1, (pp - """, str(switch_point), ")))/2)*((", str(par_pl1), ")*pp + (", str(par_pl0), ")) + ((1 + TMath::Sign(1, -(pp - ", str(switch_point), ")))/2)*((", str(par_pq2), ")*(pp - ", str(switch_point), ")*(pp - ", str(switch_point), ") + (", str(par_pq1), ")*(pp - ", str(switch_point), ") + ((", str(par_pl1), ")*", str(switch_point), " + (", str(par_pl0) ,""")));
                                        """]))


                                except:
                                    print("".join([color.RED, "\nPRINTING ERROR: \n\t", str(traceback.format_exc()), "\n\n", color.END]))

                                if(sec == 6):
                                    try:
                                        # Save_Name = ("".join([str(ref_can).replace(Correction_Name, corNameTitles(Correction_Name).replace("/", "_")), "_", str(Selection_of_In_or_Out), "".join(["_", str(Extra_Saving_Name)]) if(str(Extra_Saving_Name) != "") else "", ".png"])).replace(" ", "_")
                                        if(str(Selection_of_In_or_Out) not in str(ref_can)):
                                            Save_Name = ("".join([str(ref_can), "_", str(Selection_of_In_or_Out), "".join(["_", str(Extra_Saving_Name)]) if(str(Extra_Saving_Name) != "") else "", ".png"])).replace(" ", "_")
                                        else:
                                            Save_Name = ("".join([str(ref_can), "".join(["_", str(Extra_Saving_Name)]) if(str(Extra_Saving_Name) != "") else "", ".png"])).replace(" ", "_")
                                        Save_Name = str(str(str(str(Save_Name.replace("'", "")).replace(",", "_")).replace("(", "_")).replace(")", "")).replace("Sector_Number_List", "")
                                        while("__" in str(Save_Name)):
                                            Save_Name = str(Save_Name.replace("__", "_"))
                                        Save_Name = str(Save_Name.replace("_-_", "-"))
                                        if(Used_Split_Op and (f"_{Use_Split_Cor}." not in str(Save_Name))):
                                            Save_Name = str(Save_Name.replace(".png", f"_{Use_Split_Cor}.png")).replace(".pdf", f"_{Use_Split_Cor}.pdf")
                                        if(Save_Name in List_of_Saved_Images):
                                            for ii in range(2, 21):
                                                if(str(str(Save_Name.replace(".png", f"_Version_{ii}.png")).replace(".pdf", f"_Version_{ii}.pdf")) not in List_of_Saved_Images):
                                                    Save_Name = str(str(Save_Name.replace(".png", f"_Version_{ii}.png")).replace(".pdf", f"_Version_{ii}.pdf"))
                                                    break
                                                elif(ii >= 20):
                                                    print(f"\n{color.ERROR}More than 20 versions of {color.UNDERLINE}Save_Name = {Save_Name}{color.END_B}{color.RED} were made...{color.END}\n")
                                                    Save_Name = str(str(Save_Name.replace(".png", f"_Version_Last.png")).replace(".pdf", f"_Version_Last.pdf"))
                                        List_of_Saved_Images.append(Save_Name)
                                        print(("".join([color.BLUE if(SaveResultsQ == 'yes') else color.BOLD, "\n\n\n\n\tSaving:\t" if(SaveResultsQ == 'yes') else "\n\n\tWould be saving:\t", Save_Name, color.END])))
                                        if(SaveResultsQ == 'yes'):
                                            try:
                                                # Get the list of all objects in the TCanvas and filter TPads
                                                pads = [obj for obj in canvas_test[ref_can].GetListOfPrimitives() if isinstance(obj, ROOT.TPad)]
                                                # Check if there are exactly 6 TPads
                                                if(len(pads) == 6):
                                                    # Set the position and size of each TPad for a 2x3 layout
                                                    pads[0].SetPad(0.0, 0.5, 0.33, 1.0)  # Top-left
                                                    pads[2].SetPad(0.33, 0.5, 0.66, 1.0) # Top-middle
                                                    pads[4].SetPad(0.66, 0.5, 1.0, 1.0)  # Top-right
                                                    pads[1].SetPad(0.0, 0.0, 0.33, 0.5)  # Bottom-left
                                                    pads[3].SetPad(0.33, 0.0, 0.66, 0.5) # Bottom-middle
                                                    pads[5].SetPad(0.66, 0.0, 1.0, 0.5)  # Bottom-right
                                                    # # Adjust margins for each TPad if necessary
                                                    # for pad in pads:
                                                    #     pad.SetLeftMargin(0.1)
                                                    #     pad.SetRightMargin(0.05)
                                                    #     pad.SetTopMargin(0.05)
                                                    #     pad.SetBottomMargin(0.1)
                                                    #     pad.Update()
                                                    canvas_test[ref_can].Update()
                                                else:
                                                    print(f"The TCanvas contains {len(pads)} TPads, which is not equal to 6. No adjustments made.")
                                            except:
                                                print(f"{color.RED}Error in redrawing the TPads...\nTraceback: \n{color.END_B}{str(traceback.format_exc())}{color.END}")
                                            canvas_test[ref_can].SaveAs(Save_Name)
                                    except:
                                        print("".join([color.RED, "\n\nSAVE ERROR: \n\t", str(traceback.format_exc()), "\n\n", color.END]))


                    print("".join(["\n\n\n\n", color.GREEN, """
    ==============================================================================================================================================================
                    """, color.END, "\n"]))
    except:
        print("".join([color.Error, "ERROR:\n", color.END_R, str(traceback.format_exc()), color.END, "\n"]))














    print("".join(["""
    ==============================================================================================================================================================
    \n\t""", color.BBLUE, ".\n\n.\n\n.\n\n.\n\nDone with Individual Phi Bins (Moving to Continuous Corrections)\n\n.\n\n.\n\n.\n\n.\n\n".replace("\n", "\n\t"), color.END_B, """
    ==============================================================================================================================================================
    """, color.END]))













    # for region in Region_Option_List:
    #     for ii in histo_search:
    #         if("Sector 1" not in str(ii)):
    #             continue
    #         ii_true = ii
    #         for sec in [1]:
    # #         for sec in [1, 2, 3, 4, 5, 6]:
    #             ii = ii_true.replace("Sector 1", "".join(["Sector ", str(sec)]))
    # #             cd_num = 1 if("Sector 1" in ii) else 2 if("Sector 2" in ii) else 3 if("Sector 3" in ii) else 4 if("Sector 4" in ii) else 5 if("Sector 5" in ii) else 6 if("Sector 6" in ii) else "error"
    #             if("Dmom_pel" not in str(ii) or cd_num == "error"):
    #                 continue
    #             if(region not in str(ii) or ("regall" == region and ("reg1" in str(ii) or "reg2" in str(ii) or "reg3" in str(ii)))):
    #                 continue
    #             if(("SP" in str(ii)) and (("mmF_PipMMF" not in str(ii) and "mm0" not in str(ii)) or "Basic" in str(ii))):
    #                 continue
    #             if(("EO" in str(ii)) and (("mmF" not in str(ii) and "mm0" not in str(ii)) or "Basic" in str(ii))):
    #                 continue

    #             print(ii)
    try:         
        print(f"Type of Momentum correction in use: {color.BOLD}{str(fit_function)}{color.END}\n\n\n\n")

        canvas_phi, histo_phi = {}, {}
        for particle in Particle_Mom_List:
            for ii in Combined_Histo:
                sector = 1 if("Sector_1" in ii) else 2 if("Sector_2" in ii) else 3 if("Sector_3" in ii) else 4 if("Sector_4" in ii) else 5 if("Sector_5" in ii) else 6 if("Sector_6" in ii) else "ERROR"
                if("reg1" not in str(ii) or sector == "ERROR" or particle not in str(ii) or "Compare" in str(ii)):
                    # print("ii =", ii)
                    continue

                # print(color.BLUE + "\n" + str(ii) + "\n" + color.END)
                HistoBinC = Combined_Histo[ii]
                HistoBinN = Combined_Histo[ii.replace("reg1", "reg2")]
                HistoBinP = Combined_Histo[ii.replace("reg1", "reg3")]


                # if((particle == "pip") and (("mm0" not in str(ii)) and ("mmEF" not in str(ii)) and ("mmP2" not in str(ii)) and ("mmRP2" not in str(ii)))):
                if((particle == "pip") and (not any(pip_correction_check in str(ii) for pip_correction_check in ["mm0", "mmEF", "mmP2", "mmRP2", "mmfaP2"]))):
                    print(fail)
                    continue

    #             if("mmEF_MMPip" not in str(ii)):
    #                 continue

                canvas_name = (ii.replace("reg1", "PHI")).replace("".join(["_Sector_", str(sector)]), "")

                # Cor_name = "Uncorrected" if("Uncorrected" in str(ii)) else "".join(["Corrected", " (", "With Pion" if("With Pion" in str(ii)) else "Without Pion", " - Extended)" if("Extended" in str(ii)) else " - With Elastic)" if("With Elastic" in str(ii)) else ")"])

                Cor_name = "Uncorrected" if("Uncorrected" in str(ii)) else "Corrected (Full Elastic)" if("mmEF_PipMMEF" in str(ii)) else "".join(["Corrected", "".join([" (", "With (New) Pion" if("With (New) Pion" in str(ii)) else "With (Old) Pion" if("With (Old) Pion" in str(ii)) else "Without Pion" , " - Extended)" if("Extended" in str(ii)) else " - With Elastic)" if("With Elastic" in str(ii)) else ")"])])


                Cor_name = "mmP2_PipMMP2 (Pass 2 Correction - With Pion)" if("mmP2_PipMMP2" in str(ii)) else "mmRP2_PipMMP2 (Pass 2 Refined Electron Correction - With Pion)" if("mmRP2_PipMMP2" in str(ii)) else "mmP2 (Pass 2 Correction)" if("mmP2" in str(ii)) else "mmRP2 (Refined Pass 2 Correction)" if("mmRP2" in str(ii)) else Cor_name
                correction_Code_Name = "mm0" if("mm0" in str(ii)) else "mmEF" if("mmEF" in str(ii)) else "mmP2" if("mmP2" in str(ii)) else "mmRP2" if("mmRP2" in str(ii)) else "mmfaP2" if("mmfaP2" in str(ii)) else "mmError"
                if(f"{correction_Code_Name}_" in str(ii)):
                    correction_Code_Name = "".join([correction_Code_Name, "_", "EL" if("_ELPipMM"      in str(ii)) else ""])
                correction_Code_Name = "".join([str(correction_Code_Name), ""       if( "PipMM"    not in str(ii)) else  "PipMMEF"     if("PipMMEF"     in str(ii)) else  "PipMMP2"      if("PipMMP2"      in str(ii)) else  "PipMM0"       if("PipMM0"       in str(ii)) else  "PipMMfaP2"    if("PipMMfaP2"    in str(ii)) else  "PipMMError"])
                correction_Code_Name = "".join([str(correction_Code_Name), ""       if("_ProMMpro" not in str(ii)) else "_ProMMpro_EF" if("ProMMpro_EF" in str(ii)) else "_ProMMpro_REF" if("ProMMpro_REF" in str(ii)) else "_ProMMpro_LEF" if("ProMMpro_LEF" in str(ii)) else "_ProMMpro_QEF" if("ProMMpro_QEF" in str(ii)) else "_PipMMError"])
                correction_Code_Name = "".join([str(correction_Code_Name), ""       if("_NoELC"    not in str(ii)) else "_NoELC"])

                Cor_name = correction_Code_Name

                if((any("_ELPipMM" in cor_test_str for cor_test_str in Correction_Name_List)) and ("_ELPipMM" not in correction_Code_Name)):
                    print(f"{color.RED}\nSkipping Single Pion Corrections that lack the Pion Energy Loss Correction{color.END}")
                    break

                # print("str(ii)  =", str(ii))
                # print("Cor_name =", str(Cor_name))
                # print("")

                print("".join(["if(sec == ", str(sector), "){"]))
                # canvas_phi, histo_phi = PhiCor_Function(canvas_name, HistoBinC, HistoBinN, HistoBinP, sector, Particle="el", LineOrQuad_Phi="pol2", LineOrQuad=fit_function, cCor_Phi=canvas_phi, gCor_Par=histo_phi, Extra_Fit_Name="fit_function", Correction="Uncorrected" if("Uncorrected" in ii) else "Corrected" if("Corrected" in ii) else "Error")
                canvas_phi, histo_phi = PhiCor_Function(canvas_name, HistoBinC, HistoBinN, HistoBinP, sector, Particle=particle, LineOrQuad_Phi="pol2", LineOrQuad=fit_function, cCor_Phi=canvas_phi, gCor_Par=histo_phi, Extra_Fit_Name="fit_function", Correction=Cor_name if(particle == "el") else Cor_name.replace("Without", "Uncorrected"))
                print("}")
                # canvas_phi[canvas_name].Draw()

                if(sector == 6):
                    # print("\n\n\n")
                    print("".join(["\n\n\n", color.BLUE, """
    ==============================================================================================================================================================
                    """, color.END, "\n\n"]))



            print("\n\n\n\n\n\n\n\nDone\n")
            for ii2 in canvas_phi:
    #             print(ii2)
                canvas_phi[ii2].Draw()

        # test = {}
        # for jj in histo_phi:
        # #     print(jj)
        #     test[jj] = Canvas_Create(jj, Num_Columns=1, Num_Rows=1, Size_X=620, Size_Y=610)
        #     test[jj].Draw()
        #     test[jj].cd(1)
        #     histo_phi[jj].Draw()
        # test = Canvas_Create("test", Num_Columns=2, Num_Rows=1, Size_X=620, Size_Y=610)
        # test.Draw()
        # test.cd(1)
        # histo_phi["(Dmom_pel_Histo_Combined_('PHI', 'Uncorrected')_Sector_1_pol2_pol1)_par1_1"].Draw()
        # test.cd(2)
        # histo_phi["(Dmom_pel_Histo_Combined_('PHI', 'Uncorrected')_Sector_1_pol2_pol1)_par0_1"].Draw()
    except Exception as e:
        print("".join(["\n\n", color.RED, "ERROR: \n", str(e), color.END, "\n\n"]))
        print("".join([color.Error, "ERROR (Traceback):\n", color.END_R, str(traceback.format_exc()), color.END, "\n"]))




    try:
        for ref_can in canvas_phi:
            Save_Name = str("".join([str(ref_can), ".png"])).replace(" ", "_")
            Save_Name = str(str(str(str(Save_Name.replace("'", "")).replace(",", "_")).replace("(", "_")).replace(")", "")).replace("Sector_Number_List", "")
            while("__" in str(Save_Name)):
                Save_Name = str(Save_Name.replace("__", "_"))
            Save_Name = str(Save_Name.replace("_-_", "-"))
            Save_Name = str(Save_Name.replace("_Dmom", "Dmom")).replace("_pol2", "")
            if(Used_Split_Op and (f"_{Use_Split_Cor}." not in str(Save_Name))):
                Save_Name = str(Save_Name.replace(".png", f"_{Use_Split_Cor}.png")).replace(".pdf", f"_{Use_Split_Cor}.pdf")
            if(Save_Name in List_of_Saved_Images):
                for ii in range(2, 21):
                    if(str(str(Save_Name.replace(".png", f"_Version_{ii}.png")).replace(".pdf", f"_Version_{ii}.pdf")) not in List_of_Saved_Images):
                        Save_Name = str(str(Save_Name.replace(".png", f"_Version_{ii}.png")).replace(".pdf", f"_Version_{ii}.pdf"))
                        break
                    elif(ii >= 20):
                        print(f"\n{color.ERROR}More than 20 versions of {color.UNDERLINE}Save_Name = {Save_Name}{color.END_B}{color.RED} were made...{color.END}\n")
                        Save_Name = str(str(Save_Name.replace(".png", f"_Version_Last.png")).replace(".pdf", f"_Version_Last.pdf"))
            List_of_Saved_Images.append(Save_Name)
            print(("".join([color.BLUE if(SaveResultsQ == 'yes') else color.BOLD, "\n\n\nSaving:\n\t" if(SaveResultsQ == 'yes') else "\nWould be saving:\n\t", Save_Name, color.END])))
            if(SaveResultsQ == 'yes'):
                canvas_phi[ref_can].SaveAs(Save_Name)
    except:
        print("".join([color.Error, "\n\nSAVE ERROR: \n\t", str(traceback.format_exc()), "\n\n", color.END]))
        
        
else:
    print(f"\n\n\n{color.BOLD}Not Running Momentum Corrections ({color.DELTA}P) Plots{color.END}\n\n")









# print("".join([color.BOLD, color.PURPLE, color_bg.YELLOW, "\t\t\t\t\t\t\n\t\n\t\t\t\t\t\t\t\n\t    The Code has Finished Running...    \t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n", color.END, "\n"]))
print("".join([color.BOLD, color.PURPLE, color_bg.YELLOW, "\n\n\n\t    The Code has Finished Running...    \t\n\n", color.END, "\n"]))