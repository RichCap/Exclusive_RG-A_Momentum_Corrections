#!/usr/bin/env python3

import ROOT
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



# Selection_of_In_or_Out = "Inbending"
Selection_of_In_or_Out = "Outbending"
# Selection_Data_Set = "Fall2018"
Selection_Data_Set = "Fall2018_Pass2"
# Selection_Data_Set = "Fall2018_Pass2_Central"
Selection_Data_Set = "Fall2018_Pass2_Forward"
# Selection_Data_Set = "Spring2019_Pass2"
# Selection_Data_Set = "Spring2019_Pass1"


# Selection_Data_Set = "Monte_Carlo_Pass2"

event_type = "EO" # Single Pion Channel (ep->eπ+N)
MM_type = "eX" # Use for single pion channel (select with event_type = "SP")

event_type = "SP" # Single Pion Channel (ep->eπ+N)
MM_type = "epipX" # Use for single pion channel (select with event_type = "SP")

Single_Histogram_Canvas, histo_search_count_single = {}, {}

# Single_EvntType = "DP"
# Single_EvntType = "P0"
Single_EvntType = "EO"
Single_EvntType = "SP"
# Single_Bending_Type = "Inbending"
Single_Bending_Type = "Outbending"
# Single_Data_Run = "Fall2018"
Single_Data_Run = "Fall2018_Pass2"
# Single_Data_Run = "Fall2018_Pass2_Central"
Single_Data_Run = "Fall2018_Pass2_Forward"
# Single_Data_Run = "Spring2019_Pass1_Central"
# Single_Data_Run = "Spring2019_Pass2_Central"
# Single_Data_Run = "Spring2019_Pass2"

# Single_Data_Run = "Monte_Carlo_Pass2"

# Particle_Search = "pro"
Particle_Search = "el"
# Particle_Search = "pip"

Use_Missing_Mass_Plots = not True

Use_Invariant_Mass_Plots = not True

Make_MM_Cuts = not True
if((not Use_Missing_Mass_Plots) and (not Use_Invariant_Mass_Plots)):
    Make_MM_Cuts = False
elif(Make_MM_Cuts):
    Cut_Fit_Line_Upper, Cut_Fit_Line_Lower = {}, {}

def Filter_Conditions_Single(Input):
    Condition_list = []
    # Code checks for if 'True' is in Condition_list (i.e., set the conditions below so that 'True' is appended into the list if a condition you want filtered/not shown is met by the Input)
    Condition_list.append("Square Root Term Cut" in str(Input))

    if("(Basic)"  in str(Input)):
        Condition_list.append(True)
    if("3D"       in str(Input)):
        Condition_list.append(True)
    if("Dp_Theta" in str(Input)):
        Condition_list.append(True)
    if("_Vs_Theta" in str(Input)):
        Condition_list.append(True)
    if("Error: Undefined Cut" in str(Input)):
        Condition_list.append(True)

    if(Particle_Search not in str(Input)):
        # print('Particle_Search not in str(Input)')
        Condition_list.append(True)

    # if("reg2" not in str(Input)):
    #     # print('"regall" not in str(Input)')
    #     Condition_list.append(True)


#     if("mmfaP2" not in str(Input)):
#         Condition_list.append(True)

#     Condition_list.append("ELPipMMfaP2" not in str(Input))
# #     Condition_list.append("ELPipMM0" not in str(Input))

    # if("ELPipMM" not in str(Input)):
    #     Condition_list.append(True)


    if(Use_Missing_Mass_Plots):
        # print("Running Missing Mass...")
        if(Single_EvntType not in ["EO"]):
            if("hmmCPARTall_" not in str(Input)):
                Condition_list.append(True)

        # if("".join([str(Particle_Search), "', '", str(Particle_Search)]) not in str(Input)):
        #     Condition_list.append(True)

        if(("'pip', 'pip'"  not in str(Input)) and (Particle_Search in ["pip"])):
            Condition_list.append(True)
        if(("'el', 'el'"    not in str(Input)) and (Particle_Search in ["el"])):
            Condition_list.append(True)

        if("'')" not in str(Input)):
            # for cuts...
            Condition_list.append(True)
        # if("'Missing Mass Squared Cut'" not in str(Input)):
        #     # for cuts...
        #     Condition_list.append(True)

        # Sector Filters
        if(" 0," in str(Input)):
            Condition_list.append(True)
#         if("3," not in str(Input)):
#             Condition_list.append(True)

#         if(("1," not in str(Input)) and ("2," not in str(Input))):
#             Condition_list.append(True)

        if((Particle_Search == "pip") and ("Central" in Single_Data_Run)):
            # Cutting on Forward Sectors
            for ii in range(1, 7, 1):
                if(f" {ii}," in str(Input)):
                    Condition_list.append(True)

        if("regall" in str(Input)):
            # print('"regall" not in str(Input)')
            Condition_list.append(True)



    elif(Use_Invariant_Mass_Plots):
        Condition_list.append("HWC_Histo_All_" not in str(Input))
        Condition_list.append("regall"         not in str(Input))
        # Condition_list.append("reg1"               in str(Input))
        # Condition_list.append("reg2"               in str(Input))
        # Condition_list.append("reg3"               in str(Input))

        # Sector Filters
        Condition_list.append(", 0," in str(Input)) # All Sectors
        # Condition_list.append(", 1," in str(Input))
        # Condition_list.append(", 2," in str(Input))
        # Condition_list.append(", 3," in str(Input))
        # Condition_list.append(", 4," in str(Input))
        # Condition_list.append(", 5," in str(Input))
        # Condition_list.append(", 6," in str(Input))


    else:
        # print("Running ∆P...")
        if("Dmom" not in str(Input)):
            # print('"hmmCPARTall_" not in str(Input)')
            Condition_list.append(True)
        if("All Sector" in str(Input)):
            # print('"0," not in str(Input)')
            Condition_list.append(True)
        # if("Pro Sector 6" not in str(Input)):
        #     Condition_list.append(True)
        # if("El Sector 3" not in str(Input)):
        #     Condition_list.append(True)  
        if(("Pi+ Sector" in str(Input)) and (Particle_Search != "pip")):
            Condition_list.append(True)
        if(("El Sector"  in str(Input)) and (Particle_Search != "el")):
            Condition_list.append(True)
        if("Exclusivity" not in str(Input)):
            Condition_list.append(True)  
        # if("'')" in str(Input)):
        #     # for cuts...
        #     Condition_list.append(True)
        if("Larger" in str(Input)):
            Condition_list.append(True)
        if("No_C" in str(Input)):
            Condition_list.append(True)

            
        if(Particle_Search in ["el"]):
            # Require EL Phi Binning
            Condition_list.append("regall" not in str(Input))
        else:
            # Require Pi+ Phi Binning
            Condition_list.append("regall"     in str(Input))
        
        # Require (Either) Phi Binning
        if("reg1" not in str(Input) and "reg2" not in str(Input) and "reg3" not in str(Input)):
            Condition_list.append(True)


#         Condition_list.append("reg3"     not in str(Input))
#         Condition_list.append("Sector 4" not in str(Input))



        # if("reg1" not in str(Input) and "reg2" not in str(Input) and "reg3" not in str(Input)):
        #     # Require Pi+ Phi Binning
        #     Condition_list.append("regall" not in str(Input))
        # if("reg1" in str(Input) or "reg2" in str(Input) or "reg3" in str(Input)):
        #     # No Phi Binning
        #     Condition_list.append(True)
        # if("reg1" not in str(Input) and "reg2" not in str(Input) and "reg3" not in str(Input)):
        #     # Require Phi Binning
        # #     Condition_list.append(False)
        # # else:
        #     Condition_list.append(True)
        # if("'Calculated Exclusivity Cuts'" not in str(Input)):
        #     # for cuts...
        #     Condition_list.append(True)
        # if("'Missing Mass Squared Cut')" not in str(Input)):
        #     # for cuts...
        #     Condition_list.append(True)
        # if("'Corrected (EL) Missing Mass Squared Cut'" not in str(Input)):
        #     # for cuts...
        #     Condition_list.append(True)
        # if(("'Corrected (EL) Missing Mass Squared Cut'" not in str(Input)) and ("'Corrected (Full) Missing Mass Squared Cut'" not in str(Input))):
        #     # for cuts...
        #     Condition_list.append(True)
        # if(("'Corrected (Full) Missing Mass Squared Cut'" not in str(Input)) and ("'')" not in str(Input))):
        #     # for cuts...
        #     Condition_list.append(True)

        # if("regall" not in str(Input)):
        #     # print('"regall" not in str(Input)')
        #     Condition_list.append(True)

#         if("reg1" in str(Input)):
#             Condition_list.append(True)
#         if("reg2" in str(Input)):
#             Condition_list.append(True)
#         if("reg3" in str(Input)):
#             Condition_list.append(True)



#     if("Test_M" not in str(Input)):
#         Condition_list.append(True)            



#     if("PipMME" not in str(Input)):
#         # print('"mm0" not in str(Input)')
#         Condition_list.append(True)

#     if("mmEF" not in str(Input)):
#         # print('"mm0" not in str(Input)')
#         Condition_list.append(True)

#     if((("mmP2" not in str(Input)) and ("mmRP2" not in str(Input))) and ("Spring2019_Pass2" in Single_Data_Run)):
#         # Correction Select
#         Condition_list.append(True)


#     if("mm0_ELPipMM0" not in str(Input)):
#         Condition_list.append(True)

#     if("mm0'" not in str(Input)):
#         Condition_list.append(True)


    if(Make_MM_Cuts):
        if("mm0'" not in str(Input)):
            Condition_list.append(True)
    else:
        # # No pi+ corrections w/out energy loss
        if(("PipMM" in str(Input)) and ("ELPipMM" not in str(Input))):
            Condition_list.append(True)
        
        
#         # if("mm0_ELPipMM0" not in str(Input)):
#         #     Condition_list.append(True)
#         if(("mmfaP2_ELPipMM0"    not in str(Input)) and (Single_EvntType not in ["EO"])):
#             Condition_list.append(True)
        if(("mmfaP2_ELPipMMfaP2" not in str(Input)) and (Single_EvntType not in ["EO"])):
            Condition_list.append(True)
        if(("mmfaP2"             not in str(Input)) and (Single_EvntType     in ["EO"])):
            Condition_list.append(True)

    return Condition_list



    
    
#     for MC_Test_Type in ["Norm", "Plus", "Minus"]:
#         print("")
#     for MC_Test_Type in ["Norm"]:
#         print("")
# #     for MC_Test_Type in ["Norm", "Plus"]:
# #         print("")
# #     for MC_Test_Type in ["Minus"]:
for loop_test in ["Ignore_These_Loops"]:
    for MC_Test_Type in ["Norm"]:

        print("\n")
        event_type   = Single_EvntType
        Frame_Single = DataFrame_Find(Single_EvntType, In_or_Out=Single_Bending_Type, Selection_Data_Set_In=Single_Data_Run, MC_Test=MC_Test_Type)
        print("".join(["\nSearching for Particle: ", str(Particle_Search), "\n\n"]))

        search_count_single = 0
        for ii in Frame_Single.GetListOfKeys():
            out_print = str(ii.GetName())
            if(True in Filter_Conditions_Single(out_print)):
                continue
            search_count_single += 1
            print("".join(["Histo ", str(search_count_single), ") ", " " if(search_count_single < 10) else "", str(out_print)]))
            if(search_count_single == 1 or True):
                # print("".join([color.BOLD, color.PURPLE, "\n", out_print, color.END]))
                histo_search_count_single[out_print], Single_Histo_Title_New = Find_And_Slice_Histo(RDF=Frame_Single, NAME=out_print, EVENT=Single_EvntType, PARTICLE=Particle_Search, BENDING=Single_Bending_Type, Pass_Type=Single_Data_Run) # Find_And_Slice_Histo(RDF=Frame_Single, NAME=out_print, EVENT=Single_EvntType, PARTICLE=Particle_Search, Pass_Type=Single_Data_Run)
                out_print_single = out_print


    #         if(search_count_single != 1):
    #             # print(search_count_single)
    #             print("")
            if(search_count_single == 1 or True):
                Canvas_Name = "".join([str(histo_search_count_single[out_print].GetName()), "_", str(MC_Test_Type)])
                
                # print("".join([color.BOLD, color.GREEN, "\n", histo_search_count_single[out_print].GetName(), color.END]))
    #             print(Single_Histo_Title_New)
                # Single_Histogram_Canvas = Canvas_Create(Name="Single_Histogram_(Base)", Num_Columns=1, Num_Rows=2, Size_X=2400, Size_Y=3600)#2100, cd_Space=0)
        #         Single_Histogram_Canvas = Canvas_Create(Name="Single_Histogram_(Base)", Num_Columns=1, Num_Rows=2, Size_X=1600, Size_Y=2400)#2100, cd_Space=0)
                Single_Histogram_Canvas[Canvas_Name] = Canvas_Create(Name=Canvas_Name, Num_Columns=1, Num_Rows=2, Size_X=2400, Size_Y=3000)#2100, cd_Space=0)
                Single_Histogram_Canvas[Canvas_Name].Draw()
#                 ROOT.gStyle.SetOptFit(1)
#                 ROOT.gStyle.SetOptStat("emr")

    #             print(histo_search_count_single[out_print].GetTitle())

                histo_search_count_single[out_print].SetTitle(str(histo_search_count_single[out_print].GetTitle()).replace("Pi+", "#pi^{+}"))
                Draw_Canvas(Single_Histogram_Canvas[Canvas_Name], 1, 0.05, 0, -0.02, 0)
                histo_search_count_single[out_print].SetTitle(str(histo_search_count_single[out_print].GetTitle().replace("El Cor (Quad - Quad Phi - With Elastic Cors) - #pi^{+} Cor (Quad - Quad Phi - With Elastic Cors)", "#splitline{El Cor (Quad - Quad Phi - With Elastic Cors)}{#pi^{+} Cor (Quad - Quad Phi - With Elastic Cors)}")))
                histo_search_count_single_out_print_Title = histo_search_count_single[out_print].GetTitle()
                # print(histo_search_count_single_out_print_Title)
                if((" Bin" not in histo_search_count_single_out_print_Title) and any(region_single in out_print for region_single in ["reg1", "reg2", "reg3"])):
                    title_color, title_bin = [root_color.Black, "Center"] if("reg1" in out_print) else [root_color.Red, "Negative"] if("reg2" in out_print) else [root_color.Green, "Positive"] if("reg3" in out_print) else [root_color.Red, "Error in"]
                    histo_search_count_single_out_print_Title = "".join(["#splitline{", str(histo_search_count_single_out_print_Title), "}{#scale[1]{#color[", str(title_color), "]{", str(title_bin), " #phi Bin}}}"])
                    histo_search_count_single[out_print].SetTitle(histo_search_count_single_out_print_Title)
                    
                # if(not Use_Missing_Mass_Plots):
                #     if("(GeV)" not in str(histo_search_count_single[out_print].GetYaxis().GetTitle())):
                #         histo_search_count_single[out_print].GetYaxis().SetTitle("".join([str(histo_search_count_single[out_print].GetYaxis().GetTitle()), " (GeV)"]))
                # else:
                #     if("(GeV^{2})" not in str(histo_search_count_single[out_print].GetYaxis().GetTitle())):
                #         histo_search_count_single[out_print].GetYaxis().SetTitle(str("".join([str(histo_search_count_single[out_print].GetYaxis().GetTitle()), " (GeV^{2})"])).replace("(GeV) (GeV^{2})", "(GeV)"))
                
                if("^{2}"        not in str(histo_search_count_single[out_print].GetTitle())):
                    if("GeV"     not in str(histo_search_count_single[out_print].GetYaxis().GetTitle())):
                        histo_search_count_single[out_print].GetYaxis().SetTitle("".join([str(histo_search_count_single[out_print].GetYaxis().GetTitle()), " (GeV)"]))
                else:
                    if("GeV^{2}" not in str(histo_search_count_single[out_print].GetYaxis().GetTitle())):
                        histo_search_count_single[out_print].GetYaxis().SetTitle(str("".join([str(histo_search_count_single[out_print].GetYaxis().GetTitle()), " (GeV^{2})"])).replace("(GeV) (GeV^{2})", "(GeV)"))
                    
                if(not any(angle     in str(histo_search_count_single[out_print].GetXaxis().GetTitle()) for angle in ["phi", "th", "GeV", "#circ"])):
                    histo_search_count_single[out_print].GetXaxis().SetTitle("".join([str(histo_search_count_single[out_print].GetXaxis().GetTitle()), " (GeV)"]))
                    
                histo_search_count_single[out_print].GetXaxis().SetTitle(str(str(histo_search_count_single[out_print].GetXaxis().GetTitle()).replace("[", "(")).replace("]", ")"))
                histo_search_count_single[out_print].Draw("colz" if("2D" in str(type(histo_search_count_single[out_print]))) else "same")

                if(Single_EvntType in ["P0"]):
                    histo_search_count_single[out_print].SetTitle("".join([str(str((histo_search_count_single[out_print].GetTitle()).replace("p#pi^{0}X", "p(X)")).replace("{#pi^{0} Channel", "".join(["{(", str(MC_Test_Type), ") #pi^{0} Channel"]))), "; ", str((histo_search_count_single[out_print].GetXaxis().GetTitle()).replace("p#pi^{0}X", "p(X)")), "; ", str((histo_search_count_single[out_print].GetYaxis().GetTitle().replace("p#pi^{0}X", "p(X)")))]))

                Tline_Simple_Ideal = ROOT.TLine()
                Tline_Simple_Ideal.SetLineColor(root_color.Black)
                Tline_Simple_Ideal.SetLineWidth(2)

                Tline_Simple_Ideal_Y = 0 if("Dmom" in out_print_single) else 0.9383 if("HWC_Histo_All" in out_print_single) else (0.13957*0.13957) if(Single_EvntType == "DP") else (0.1349768*0.1349768) if(Single_EvntType == "P0") else 0.9396 if("SP" in Single_EvntType) else 0

        #         if(Tline_Simple_Ideal_Y == (0.13957*0.13957)):
        #             print("GOOD")
        #         else:
        #             print("BAD")

    #             print(Tline_Simple_Ideal_Y)

                Tline_Simple_Ideal_X_Min = histo_search_count_single[out_print].GetXaxis().GetBinCenter(0)
                Tline_Simple_Ideal_X_Max = histo_search_count_single[out_print].GetXaxis().GetBinCenter(histo_search_count_single[out_print].GetXaxis().GetNbins())

                Tline_Simple_Ideal.DrawLine(Tline_Simple_Ideal_X_Min, Tline_Simple_Ideal_Y, Tline_Simple_Ideal_X_Max, Tline_Simple_Ideal_Y)
                    
                    
                Histo_Title = str(histo_search_count_single[out_print].GetTitle())
                if("HWC_Histo_All" not in str(out_print)):
                    if(Single_EvntType == "DP"):
                        # histo_search_count_single[out_print].RebinY(4)
                        # histo_search_count_single[out_print].GetYaxis().SetRangeUser(-0.04, 0.06)
                        histo_search_count_single[out_print].GetYaxis().SetRangeUser(-0.07, 0.07)
                        # histo_search_count_single[out_print].GetXaxis().SetRangeUser(0.4, 3.75)
                        # histo_search_count_single[out_print].GetXaxis().SetRangeUser(0.4, 2.75)
                        histo_search_count_single[out_print].GetXaxis().SetRangeUser(0.4, 3.25)
                        # histo_search_count_single[out_print].GetXaxis().SetRangeUser(-0.5, 0.5)
                    else:
                        histo_search_count_single[out_print].GetYaxis().SetRangeUser(-0.2, 0.2)
                        histo_search_count_single[out_print].GetXaxis().SetRangeUser(0, 12)
                else:
                    histo_search_count_single[out_print].GetYaxis().SetRangeUser(0.6, 1.3)
                    # print("".join(["if(esec == ", str(1 if("Sector 1" in Histo_Title) else 2 if("Sector 2" in Histo_Title) else 3 if("Sector 3" in Histo_Title) else 4 if("Sector 4" in Histo_Title) else 5 if("Sector 5" in Histo_Title) else 6 if("Sector 6" in Histo_Title) else 0), "){"]))
                    if(("Spring2019" not in str(Single_Data_Run)) and ("Pass2" not in str(Single_Data_Run))):
                        a_upper = -0.01
                        b_upper = 0.129
                        c_upper = 0.8001

                        a_upper = 0
                        b_upper = -0.0346
                        c_upper = 1.4574

                        a_upper = 0
                        b_upper = 0.0036
                        c_upper = 1.05

                        Cut_Function_Upper = "".join(["(", str(a_upper), ")*x*x + (", str(b_upper), ")*x + (", str(c_upper), ")"])
                        # print(Cut_Function_Upper)

                        a_lower = -0.0198
                        b_lower = 0.3254
                        c_lower = -0.4856

                        a_lower = 0
                        b_lower = -0.0047
                        c_lower = 0.8646

                        a_lower = -0.0208
                        b_lower = 0.3533
                        c_lower = -0.6681

                        Cut_Function_Lower = "".join(["(", str(a_lower), ")*x*x + (", str(b_lower), ")*x + (", str(c_lower), ")"])

                        Cut_Line_Upper = ROOT.TF1("".join(["myfunc_upper_", str(out_print)]), Cut_Function_Upper, 4, 11)
                        # Cut_Line_Upper = ROOT.TLine(4, slope_upper*(4) + y_int_upper, 11, slope_upper*(11) + y_int_upper)
                        Cut_Line_Upper.SetLineColor(root_color.Pink)
                        Cut_Line_Upper.SetLineWidth(3)
                        Cut_Line_Upper.Draw("same")

                        # Cut_Line_Lower = ROOT.TLine(4, slope_lower*(4) + y_int_lower, 11, slope_lower*(11) + y_int_lower)
                        Cut_Line_Lower = ROOT.TF1("".join(["myfunc_lower_", str(out_print)]), Cut_Function_Lower, 4, 11)
                        Cut_Line_Lower.SetLineColor(root_color.Pink)
                        Cut_Line_Lower.SetLineWidth(3)
                        Cut_Line_Lower.Draw("same")

                # Single_Histogram_Canvas.Modified()
                # Single_Histogram_Canvas.Update()
                # palette_move(Single_Histogram_Canvas, histo_search_count_single[out_print], 0.1, 0.1, 0.1, 0.1)
                try:
                    palette_move(canvas=Single_Histogram_Canvas[Canvas_Name], histo=histo_search_count_single[out_print], x_left=0, x_right=0, y_up=0, y_down=0)
                except:
                    print("Palette Fail...")

                try:
                    histo_search_count_single[out_print].gr2.SetLineColor(root_color.Red)
                    histo_search_count_single[out_print].gr2.SetLineWidth(2)

                    histo_search_count_single[out_print].gr2.Draw("LP same")
                    
                    if(Make_MM_Cuts):
                        histo_search_count_single[out_print].gr2_Cut_Range_Down.SetLineColor(root_color.Green)
                        histo_search_count_single[out_print].gr2_Cut_Range_Down.SetMarkerColor(root_color.DGreen)
                        histo_search_count_single[out_print].gr2_Cut_Range_Down.SetLineWidth(2)
                        histo_search_count_single[out_print].gr2_Cut_Range_Up.SetLineColor(root_color.Green)
                        histo_search_count_single[out_print].gr2_Cut_Range_Up.SetMarkerColor(root_color.DGreen)
                        histo_search_count_single[out_print].gr2_Cut_Range_Up.SetLineWidth(2)

                        histo_search_count_single[out_print].gr2_Cut_Range_Down.Draw("LP same")
                        histo_search_count_single[out_print].gr2_Cut_Range_Up.Draw("LP same")
                        
                        if("mm0" in str(out_print)):
                            a_upper = 'p1'
                            b_upper = 'p0'
                            
                            a_lower = 'p1'
                            b_lower = 'p0'
                            
                            # a_lower = 'p2'
                            # b_lower = 'p1'
                            # c_lower = 'p0'
                            
                            Cut_Function_Upper = "".join(["(", str(a_upper), ")*x + (", str(b_upper), ")"])
                            if(("p1" in str(Cut_Function_Upper)) or ("p0" in str(Cut_Function_Upper))):
                                Cut_Function_Upper = "pol1(0)"
                            Cut_Function_Lower = "".join(["(", str(a_lower), ")*x + (", str(b_lower), ")"])
                            if(("p1" in str(Cut_Function_Lower)) or ("p0" in str(Cut_Function_Lower))):
                                Cut_Function_Lower = "pol1(0)" # if(Single_EvntType not in ["EO"]) else "pol0(0)"
                                
                            # Cut_Function_Lower = "".join(["(", str(a_lower), ")*x*x + (", str(b_lower), ")*x + (", str(c_lower), ")"])
                            # Cut_Function_Lower = "pol2(0)" # if(Single_EvntType not in ["EO"]) else "pol0(0)"
                                
                            Half_of_dR = 0.5*(Fitting_Lines(Histo_Type=str(out_print), Event_Type=str(Single_EvntType), Bending_Type=str(Selection_of_In_or_Out), Particle=str(Particle_Search), Missing_Mass_Type=str(MM_type), DataSet=str(Single_Data_Run))[0][2])
                            if(Single_EvntType in ["EO"]):
                                Half_of_dR = 0.25
                            
                            Cut_Fit_Line_Upper[out_print] = ROOT.TF1("".join(["myfunc_MM_Cut_Upper_", str(out_print)]), Cut_Function_Upper, histo_search_count_single[out_print].gr2_Cut_Range_Up.GetX()[0] - Half_of_dR, histo_search_count_single[out_print].gr2_Cut_Range_Up.GetX()[histo_search_count_single[out_print].gr2_Cut_Range_Up.GetN() - 1] + Half_of_dR)
                            Cut_Fit_Line_Upper[out_print].SetLineColor(root_color.Pink)
                            Cut_Fit_Line_Upper[out_print].SetLineWidth(3)
                            Cut_Fit_Line_Upper[out_print].SetRange(histo_search_count_single[out_print].gr2_Cut_Range_Up.GetX()[0]     - Half_of_dR,                                                                      histo_search_count_single[out_print].gr2_Cut_Range_Up.GetX()[histo_search_count_single[out_print].gr2_Cut_Range_Up.GetN() - 1] + Half_of_dR)
                            
                            if((Single_EvntType in ["EO"]) and ("Sector 3" in Histo_Title) and (Selection_of_In_or_Out in ["Outbending"]) and (Selection_Data_Set in ["Fall2018_Pass2", "Monte_Carlo_Pass2"])):
                                Cut_Fit_Line_Upper[out_print].SetRange(histo_search_count_single[out_print].gr2_Cut_Range_Up.GetX()[0] + Half_of_dR,                                                                      histo_search_count_single[out_print].gr2_Cut_Range_Up.GetX()[histo_search_count_single[out_print].gr2_Cut_Range_Up.GetN() - 1] + Half_of_dR)
                            
                            if("pol1" in str(Cut_Function_Upper)):
                                Cut_Fit_Line_Upper[out_print].SetParName(0, "B")
                                Cut_Fit_Line_Upper[out_print].SetParName(1, "A")
                                Cut_Fit_Line_Upper[out_print].SetParameter(0, 0)
                                Cut_Fit_Line_Upper[out_print].SetParameter(1, 0)
                                Cut_Fit_Line_Upper[out_print].SetParLimits(0,  0, 2) # if(Single_EvntType not in ["EO"]) else 1.5)
                                Cut_Fit_Line_Upper[out_print].SetParLimits(1, -1, 1)
                                if(Single_EvntType in ["EO"]):
                                    if((Selection_of_In_or_Out in ["Outbending"]) and (Selection_Data_Set in ["Fall2018_Pass2", "Monte_Carlo_Pass2"])):
                                        Cut_Fit_Line_Upper[out_print].SetParameter(1, -0.04)
                                        Cut_Fit_Line_Upper[out_print].SetParLimits(1, -0.06, -0.02)
                                        Cut_Fit_Line_Upper[out_print].SetParameter(0,  1.5)
                                        Cut_Fit_Line_Upper[out_print].SetParLimits(0,  0.75, 1.75)
                                    if(("Sector 3" in Histo_Title) and (Selection_of_In_or_Out in ["Outbending"]) and (Selection_Data_Set in ["Fall2018_Pass2", "Monte_Carlo_Pass2"])):
                                        # Cut_Fit_Line_Upper[out_print].SetParameter(1,  0.05)
                                        # Cut_Fit_Line_Upper[out_print].SetParLimits(1,  0, 0.1)
                                        Cut_Fit_Line_Upper[out_print].SetParameter(1,  0.02)
                                        Cut_Fit_Line_Upper[out_print].SetParLimits(1,  0, 0.03)
                                        Cut_Fit_Line_Upper[out_print].SetParameter(0,  0.6)
                                        Cut_Fit_Line_Upper[out_print].SetParLimits(0,  0.4, 1)
                                elif((Selection_of_In_or_Out in ["Outbending"]) and (Selection_Data_Set in ["Fall2018_Pass2", "Fall2018_Pass2_Forward", "Monte_Carlo_Pass2"])):
                                    Cut_Fit_Line_Upper[out_print].SetParameter(1,  0)
                                    Cut_Fit_Line_Upper[out_print].SetParLimits(1, -0.0024, 0.006)
                                    if(("Sector 1" in Histo_Title) and ("reg1" in out_print)):
                                        Cut_Fit_Line_Upper[out_print].SetParameter(1,  0.0005)
                                        Cut_Fit_Line_Upper[out_print].SetParLimits(1, -0.0024, 0.00085)
                                    if(("Sector 2" in Histo_Title) and ("reg1" in out_print)):
                                        Cut_Fit_Line_Upper[out_print].SetParameter(1,  0.0015)
                                        Cut_Fit_Line_Upper[out_print].SetParLimits(1, -0.0024, 0.0025)
                                        
                            if("pol2" in str(Cut_Function_Upper)):
                                Cut_Fit_Line_Upper[out_print].SetParName(0, "C")
                                Cut_Fit_Line_Upper[out_print].SetParName(1, "B")
                                Cut_Fit_Line_Upper[out_print].SetParName(2, "A")
                                Cut_Fit_Line_Upper[out_print].SetParameter(0, 0)
                                Cut_Fit_Line_Upper[out_print].SetParameter(1, 0)
                                Cut_Fit_Line_Upper[out_print].SetParameter(2, 0)
                                Cut_Fit_Line_Upper[out_print].SetParLimits(0,  0, 2) # if(Single_EvntType not in ["EO"]) else 1.5)
                                Cut_Fit_Line_Upper[out_print].SetParLimits(1, -1, 1)
                                
                            histo_search_count_single[out_print].gr2_Cut_Range_Up.Fit(Cut_Fit_Line_Upper[out_print], "BRQ")
                            Cut_Fit_Line_Upper[out_print].Draw("same")
                            # print("\t", "str(Cut_Fit_Line_Upper)")
                            # print("\t  ", Cut_Fit_Line_Upper[out_print].GetParName(0), "=", str(Cut_Fit_Line_Upper[out_print].GetParameter(0)))
                            # print("\t  ", Cut_Fit_Line_Upper[out_print].GetParName(1), "=", str(Cut_Fit_Line_Upper[out_print].GetParameter(1)))
                            Cut_Fit_Line_Upper["".join(["cut_upper_", str(out_print)])] = "".join(["(", str(round(Cut_Fit_Line_Upper[out_print].GetParameter("A"), 7)), ")*el + (", str(round(Cut_Fit_Line_Upper[out_print].GetParameter("B"), 7)), ")"])
                            # print('\tCut_Fit_Line_Upper["".join(["cut_upper_", str(out_print)])] =', Cut_Fit_Line_Upper["".join(["cut_upper_", str(out_print)])])
                            
                            
                            
                            Cut_Fit_Line_Lower[out_print] = ROOT.TF1("".join(["myfunc_MM_Cut_Lower_", str(out_print)]), Cut_Function_Lower, histo_search_count_single[out_print].gr2_Cut_Range_Down.GetX()[0] - Half_of_dR, histo_search_count_single[out_print].gr2_Cut_Range_Down.GetX()[histo_search_count_single[out_print].gr2_Cut_Range_Down.GetN() - 1] + Half_of_dR)
                            Cut_Fit_Line_Lower[out_print].SetLineColor(root_color.Pink)
                            Cut_Fit_Line_Lower[out_print].SetLineWidth(3)
                            Cut_Fit_Line_Lower[out_print].SetRange(histo_search_count_single[out_print].gr2_Cut_Range_Down.GetX()[0] - Half_of_dR,                                                                          histo_search_count_single[out_print].gr2_Cut_Range_Down.GetX()[histo_search_count_single[out_print].gr2_Cut_Range_Down.GetN() - 1] + Half_of_dR)
                            
                            if("pol" in str(Cut_Function_Lower)):
                                Cut_Fit_Line_Lower[out_print].SetParName(0, "B")
                                # Cut_Fit_Line_Lower[out_print].SetParameter(0, 0    if(Single_EvntType not in ["EO"]) else 0.6)
                                Cut_Fit_Line_Lower[out_print].SetParameter(0, 0.8  if(Single_EvntType not in ["EO"]) else 0.6)
                                Cut_Fit_Line_Lower[out_print].SetParLimits(0, 0, 2 if(Single_EvntType not in ["EO"]) else 1.5)
                                if(Cut_Function_Lower == "pol1(0)"):
                                    Cut_Fit_Line_Lower[out_print].SetParName(1, "A")
                                    if(Single_EvntType not in ["EO"]):
                                        Cut_Fit_Line_Lower[out_print].SetParameter(1, 0)
                                        Cut_Fit_Line_Lower[out_print].SetParLimits(1, -1, 1)
#                                         Cut_Fit_Line_Lower[out_print].SetParameter(1, -0.001)
#                                         Cut_Fit_Line_Lower[out_print].SetParLimits(1, -1, 0.001)
                                        if((Selection_of_In_or_Out in ["Outbending"]) and (Selection_Data_Set in ["Fall2018_Pass2", "Fall2018_Pass2_Forward", "Monte_Carlo_Pass2"])):
                                            Cut_Fit_Line_Lower[out_print].SetParameter(1, 0)
                                            Cut_Fit_Line_Lower[out_print].SetParLimits(1, -0.004, 0.0061)
                                            if(("Sector 1" in Histo_Title) and ("reg1" in out_print)):
                                                # print(f"\n\nHisto_Title = {Histo_Title}\n")
                                                Cut_Fit_Line_Lower[out_print].SetParameter(1,  0.003)
                                                Cut_Fit_Line_Lower[out_print].SetParLimits(1, -0.004, 0.005)
                                            if(("Sector 2" in Histo_Title) and ("reg1" in out_print)):
                                                Cut_Fit_Line_Lower[out_print].SetParameter(1,  0.0025)
                                                Cut_Fit_Line_Lower[out_print].SetParLimits(1, -0.004, 0.005)
                                            if((("Sector 2" in Histo_Title) or ("Sector 3" in Histo_Title)) and ("reg2" in out_print)):
                                                Cut_Fit_Line_Lower[out_print].SetParameter(1,  0.0025)
                                                Cut_Fit_Line_Lower[out_print].SetParLimits(1, -0.004, 0.005)
                                    else:
                                        # Cut_Fit_Line_Lower[out_print].SetParameter(1,  0.005)
                                        # Cut_Fit_Line_Lower[out_print].SetParLimits(1, -0.5, 1)
                                        Cut_Fit_Line_Lower[out_print].SetParameter(1,  -0.005)
                                        Cut_Fit_Line_Lower[out_print].SetParLimits(1, -0.5, 0.02)
                                        if(("Sector 5" in Histo_Title) and (Selection_of_In_or_Out in ["Outbending"]) and (Selection_Data_Set in ["Fall2018_Pass2", "Fall2018_Pass2_Forward", "Monte_Carlo_Pass2"])):
                                            Cut_Fit_Line_Lower[out_print].SetParameter(1,  0)
                                            Cut_Fit_Line_Lower[out_print].SetParLimits(1, -0.05, 0.05)
                                if("pol2" in str(Cut_Function_Lower)):
                                    Cut_Fit_Line_Lower[out_print].SetParName(0, "C")
                                    Cut_Fit_Line_Lower[out_print].SetParName(1, "B")
                                    Cut_Fit_Line_Lower[out_print].SetParName(2, "A")
#                                     Cut_Fit_Line_Lower[out_print].SetParameter(0,  0)
#                                     Cut_Fit_Line_Lower[out_print].SetParameter(1,  0)
                                    Cut_Fit_Line_Lower[out_print].SetParameter(2, -0.001)
#                                     Cut_Fit_Line_Lower[out_print].SetParLimits(0,  0, 2) # if(Single_EvntType not in ["EO"]) else 1.5)
#                                     Cut_Fit_Line_Lower[out_print].SetParLimits(1, -1, 1)
                                    Cut_Fit_Line_Lower[out_print].SetParLimits(2, -0.005, 0)
                                
                            histo_search_count_single[out_print].gr2_Cut_Range_Down.Fit(Cut_Fit_Line_Lower[out_print], "BRQ")
                            Cut_Fit_Line_Lower[out_print].Draw("same")
                            # print("\t", "str(Cut_Fit_Line_Lower[out_print])")
                            # print("\t  ", Cut_Fit_Line_Lower[out_print].GetParName(0), "=", str(Cut_Fit_Line_Lower[out_print].GetParameter(0)))
                            # print("\t  ", Cut_Fit_Line_Lower[out_print].GetParName(1), "=", str(Cut_Fit_Line_Lower[out_print].GetParameter(1)))
                            Cut_Fit_Line_Lower["".join(["cut_lower_", str(out_print)])] = "".join(["(", str(round(Cut_Fit_Line_Lower[out_print].GetParameter("A"), 7)), ")*el + (", str(round(Cut_Fit_Line_Lower[out_print].GetParameter("B"), 7)), ")"])
                            # print('\tCut_Fit_Line_Lower["".join(["cut_lower_", str(out_print)])] =', Cut_Fit_Line_Lower["".join(["cut_lower_", str(out_print)])])
                            
                            
                            Single_Histogram_Canvas[Canvas_Name].Modified()
                            Single_Histogram_Canvas[Canvas_Name].Update()
                            
                            stats1 = histo_search_count_single[out_print].gr2_Cut_Range_Up.GetListOfFunctions().FindObject("stats")
                            stats2 = histo_search_count_single[out_print].gr2_Cut_Range_Down.GetListOfFunctions().FindObject("stats")
                            if(stats1 and stats2):
                                # Move the first stat box to the upper right corner:
                                stats1.SetX1NDC(0.8)    # left edge x-position
                                stats1.SetX2NDC(0.95)   # right edge x-position
                                stats1.SetY1NDC(0.775)  # bottom edge y-position
                                stats1.SetY2NDC(0.925)  # top edge y-position

                                # Move the second stat box to the bottom right corner:
                                stats2.SetX1NDC(0.8)
                                stats2.SetX2NDC(0.95)
                                stats2.SetY1NDC(0.1)
                                stats2.SetY2NDC(0.25)
                            else:
                                print(color.Error, "\n\nERROR\n\n", color.END)
                                print("stats1 =", stats1)
                                print("histo_search_count_single[out_print].gr2_Cut_Range_Up.GetListOfFunctions() =", histo_search_count_single[out_print].gr2_Cut_Range_Up.GetListOfFunctions())
                                print("stats2 =", stats2)

                    Single_Histogram_Canvas_cd_2 = Single_Histogram_Canvas[Canvas_Name].cd(2)

                    num_cols = int(len(histo_search_count_single[out_print].hys2)) if(len(histo_search_count_single[out_print].hys2) < 5) else 3 if((int(len(histo_search_count_single[out_print].hys2)/2)) < 4) else 4
                    num_rows = 1 if(len(histo_search_count_single[out_print].hys2) < 5) else 2

                    if((num_cols*num_rows) < len(histo_search_count_single[out_print].hys2)):
                        # print("Needed 1 extra row")
                        num_rows += 1
                    if((num_cols*num_rows) < len(histo_search_count_single[out_print].hys2)):
                        # print("Needed 2 extra rows")
                        num_rows += 1
                    if((num_cols*num_rows) < len(histo_search_count_single[out_print].hys2)):
                        # print("Needed 1 extra column")
                        num_cols += 1
                    if((num_cols*num_rows) < len(histo_search_count_single[out_print].hys2)):
                        # print("Needed 2 extra rows")
                        num_rows += 1
                    if((num_cols*num_rows) < len(histo_search_count_single[out_print].hys2)):
                        # print("Needed 4 extra rows")
                        num_rows += 1
                    # if((num_cols*num_rows) < len(histo_search_count_single[out_print].hys2)):
                    #     print("Needed 2 extra columns")
                    #     num_cols += 1
                    if((num_cols*num_rows) < len(histo_search_count_single[out_print].hys2)):
                        # print("Needed 5 extra rows")
                        num_rows += 1
                    if((num_cols*num_rows) < len(histo_search_count_single[out_print].hys2)):
                        # print("Needed 6 extra rows")
                        num_rows += 1
                    if((num_cols*num_rows) < len(histo_search_count_single[out_print].hys2)):
                        # print("Needed 7 extra rows")
                        num_rows += 1
                    if((num_cols*num_rows) < len(histo_search_count_single[out_print].hys2)):
                        # print("Needed 8 extra rows")
                        num_rows += 1
                    if((num_cols*num_rows) < len(histo_search_count_single[out_print].hys2)):
                        # print("Needed 9 extra rows")
                        num_rows += 1
                    if((num_cols*num_rows) < len(histo_search_count_single[out_print].hys2)):
                        # print("Needed 10 extra rows")
                        num_rows += 1
                    if((num_cols*num_rows) < len(histo_search_count_single[out_print].hys2)):
                        # print("Needed 11 extra rows")
                        num_rows += 1
                    if((num_cols*num_rows) < len(histo_search_count_single[out_print].hys2)):
                        # print("Needed 12 extra rows")
                        num_rows += 1
                        print("".join(["Pads Needed: ",       str(len(histo_search_count_single[out_print].hys2))]))
                        print("".join(["Current available: ", str((num_cols*num_rows))]))
                        print("".join(["Pads Needed: ",       str(len(histo_search_count_single[out_print].hys2))]))
                        print("".join(["Current available: ", str((num_cols*num_rows))]))
                        
                        
                    Single_Histogram_Canvas_cd_2.Divide(num_cols, num_rows, 0, 0)
                    Drawing_1D_Hist_num = 0
                    for Drawing_1D_Hist in histo_search_count_single[out_print].hys2:
                        Drawing_1D_Hist_num += 1
        #                 Draw_Canvas(Single_Histogram_Canvas_cd_2, Drawing_1D_Hist_num, 0.05, 0, -0.02, 0)
                        Draw_Canvas(Single_Histogram_Canvas_cd_2, Drawing_1D_Hist_num, 0, 0, 0, 0)
#                         ROOT.gStyle.SetOptStat(1)


                        if("hmmCPARTall" in out_print_single):
                            title_MM = Drawing_1D_Hist.GetTitle()

                            if(Single_EvntType != "DP"):
                                if("Sector 1}}" in title_MM or "Sector 2}}" in title_MM or "Sector 3}}" in title_MM or "Sector 4}}" in title_MM or "Sector 5}}" in title_MM or "Sector 6}}" in title_MM):
                                    title_MM = str((((((title_MM.replace("Sector 1}}", "Sector 1")).replace("Sector 2}}", "Sector 2")).replace("Sector 3}}", "Sector 3")).replace("Sector 4}}", "Sector 4")).replace("Sector 5}}", "Sector 5")).replace("Sector 6}}", "Sector 6"))
                                else:
                                    title_MM = (title_MM.replace("#font[22]{", "#font[22]{#splitline{")).replace(" ---- p", "{p")

                            title_MM = title_MM.replace("No El Cor - No Pi+ Cor - No Pi- Cor - No Pro Cor", "No Momentum Corrections")
                            title_MM = (title_MM.replace("Pi+", "#pi^{+}")).replace("Pi-", "#pi^{-}")

                            title_MM = title_MM.replace("Phi", "#phi")

                            if((" Bin" not in title_MM) and any(region_single in out_print_single for region_single in ["reg1", "reg2", "reg3"])):
                            # if("reg1" in out_print_single or "reg2" in out_print_single or "reg3" in out_print_single):
                                title_color, title_bin = [root_color.Black, "Center"] if("reg1" in out_print_single) else [root_color.Red, "Negative"] if("reg2" in out_print_single) else [root_color.Green, "Positive"] if("reg3" in out_print_single) else [root_color.Red, "Error in"]
                                title_MM = "".join(["#splitline{", str(title_MM), "}{#scale[1]{#color[", str(title_color), "]{", str(title_bin), " #phi Bin}}}"])
                                Drawing_1D_Hist.SetTitle(title_MM)

                            # print(title_MM)
    #                         Drawing_1D_Hist.SetTitle(title_MM.replace("#color[2]{Correction", "#color[2]{Correction"))

                            title_MM_X = Drawing_1D_Hist.GetXaxis().GetTitle()
                            title_MM_X = title_MM_X.replace("MM^2", "MM^{2}")
                            if("GeV" not in title_MM_X):
                                title_MM_X = "".join([str(title_MM_X), " (GeV", ")" if("MM^{2}" not in title_MM_X) else "^{2})"])
                            Drawing_1D_Hist.GetXaxis().SetTitle(title_MM_X)
                        if(("Dmom" in out_print_single) and ("GeV" not in Drawing_1D_Hist.GetXaxis().GetTitle())):
                            Drawing_1D_Hist.GetXaxis().SetTitle("".join([str(Drawing_1D_Hist.GetXaxis().GetTitle()), " (GeV)"]))
                
                        Drawing_1D_Hist.SetTitle(str(Drawing_1D_Hist.GetTitle().replace("El Cor (Quad - Quad Phi - With Elastic Cors) - #pi^{+} Cor (Quad - Quad Phi - With Elastic Cors)", "#splitline{El Cor (Quad - Quad Phi - With Elastic Cors)}{#pi^{+} Cor (Quad - Quad Phi - With Elastic Cors)}")))
                        Drawing_1D_Hist.SetTitle(str(Drawing_1D_Hist.GetTitle().replace("{pip}", "{#pi^{+}}")))
                
                        Drawing_1D_Hist.Draw("same")
    #                     Drawing_1D_Hist.SetTitle(str(Drawing_1D_Hist.GetTitle()).replace("#color[2]", ""))

    #                     print(Drawing_1D_Hist.GetTitle())

                        Single_Histogram_Canvas[Canvas_Name].Modified()
                        Single_Histogram_Canvas[Canvas_Name].Update()
                        if("hmmCPARTall" not in out_print_single):
                            statbox_move(Drawing_1D_Hist, Single_Histogram_Canvas_cd_2.cd(Drawing_1D_Hist_num), "", 1, "DP_1D")
#                             statbox_move(Drawing_1D_Hist, Single_Histogram_Canvas_cd_2.cd(Drawing_1D_Hist_num), "", 1, "MM_1D")#, 0.1, 0.45, 0.5, 0.5)
#                             statbox_move(Drawing_1D_Hist, Single_Histogram_Canvas_cd_2.cd(Drawing_1D_Hist_num), "", 1, "off")#, 0.1, 0.45, 0.5, 0.5)
                        else:
                            statbox_move(Drawing_1D_Hist, Single_Histogram_Canvas_cd_2.cd(Drawing_1D_Hist_num), "", 1, "DP_1D")
#                             statbox_move(Drawing_1D_Hist, Single_Histogram_Canvas_cd_2.cd(Drawing_1D_Hist_num), "", 1, "MM_1D")
#                             statbox_move(Drawing_1D_Hist, Single_Histogram_Canvas_cd_2.cd(Drawing_1D_Hist_num), "", 1, "off")

                        Draw_Canvas(Single_Histogram_Canvas_cd_2, Drawing_1D_Hist_num, 0.05, 0, -0.02, 0)

                        Tline_Simple_1D = ROOT.TLine()
                        Tline_Simple_1D.SetLineColor(root_color.Red)
                        Tline_Simple_1D.SetLineWidth(2)

                        Tline_Simple_Ideal_1D = ROOT.TLine()
                        Tline_Simple_Ideal_1D.SetLineColor(root_color.Black)
                        Tline_Simple_Ideal_1D.SetLineWidth(2)

                        Tline_Simple_1D_Peak_X  = histo_search_count_single[out_print].FindPeak_x[Drawing_1D_Hist_num - 1]
                        Tline_Simple_1D_Ideal_X = 0 if("Dmom" in out_print_single) else 0.9383 if("HWC_Histo_All" in out_print_single) else (0.13957*0.13957) if(Single_EvntType == "DP") else (0.1349768*0.1349768) if(Single_EvntType == "P0") else 0.9396 if("SP" in Single_EvntType) else 0

                        # if("Dmom" in out_print_single):
                        #     Tline_Simple_1D_Ideal_X = 0

                        Tline_Simple_1D_Y1, Tline_Simple_Y2 = 0, histo_search_count_single[out_print].FindPeak_y[Drawing_1D_Hist_num - 1]

                        Tline_Simple_Ideal_1D.DrawLine(Tline_Simple_1D_Ideal_X, 0, Tline_Simple_1D_Ideal_X, Tline_Simple_Y2)
                        Tline_Simple_1D.DrawLine(      Tline_Simple_1D_Peak_X,  0, Tline_Simple_1D_Peak_X,  Tline_Simple_Y2)
                        
                        if(Make_MM_Cuts):
                            
                            if("mm0" in str(out_print)):
                                Tline_Function_Cut_Upper_X = round(eval(Cut_Fit_Line_Upper["".join(["cut_upper_", str(out_print)])].replace("el", str(histo_search_count_single[out_print].gr2.GetX()[Drawing_1D_Hist_num - 1]))), 5)
                                # print("\nTline_Function_Cut_Upper_X =", Tline_Function_Cut_Upper_X)
                                if("(nan)*el + " not in str(Cut_Fit_Line_Lower["".join(["cut_lower_", str(out_print)])])):
                                    Tline_Function_Cut_Lower_X = round(eval(Cut_Fit_Line_Lower["".join(["cut_lower_", str(out_print)])].replace("el", str(histo_search_count_single[out_print].gr2.GetX()[Drawing_1D_Hist_num - 1]))), 5)
                                    # print("Tline_Function_Cut_Lower_X =", Tline_Function_Cut_Lower_X)
                                else:
                                    Tline_Function_Cut_Lower_X = round(eval(Cut_Fit_Line_Lower["".join(["cut_lower_", str(out_print)])].replace("(nan)*el + ", "")), 5)
                                
                                Tline_Function_Cut_Upper = ROOT.TLine()
                                Tline_Function_Cut_Upper.SetLineColor(root_color.Pink)
                                Tline_Function_Cut_Upper.SetLineWidth(2)
                                Tline_Function_Cut_Lower = ROOT.TLine()
                                Tline_Function_Cut_Lower.SetLineColor(root_color.Pink)
                                Tline_Function_Cut_Lower.SetLineWidth(2)
                                
                                Tline_Function_Cut_Upper.DrawLine(Tline_Function_Cut_Upper_X, 0, Tline_Function_Cut_Upper_X, Tline_Simple_Y2)
                                Tline_Function_Cut_Lower.DrawLine(Tline_Function_Cut_Lower_X, 0, Tline_Function_Cut_Lower_X, Tline_Simple_Y2)
                            
                            Tline_Simple_1D_Cut_Upper_X, Tline_Simple_1D_Cut_Upper_Y = histo_search_count_single[out_print].FindCut_Upper[Drawing_1D_Hist_num - 1]
                            Tline_Simple_1D_Cut_Lower_X, Tline_Simple_1D_Cut_Lower_Y = histo_search_count_single[out_print].FindCut_Lower[Drawing_1D_Hist_num - 1]
                            Tline_Simple_1D_Cut_Upper = ROOT.TLine()
                            Tline_Simple_1D_Cut_Upper.SetLineColor(root_color.Green)
                            Tline_Simple_1D_Cut_Upper.SetLineWidth(3)
                            Tline_Simple_1D_Cut_Lower = ROOT.TLine()
                            Tline_Simple_1D_Cut_Lower.SetLineColor(root_color.Green)
                            Tline_Simple_1D_Cut_Lower.SetLineWidth(3)
                            
                            Tline_Simple_1D_Cut_Upper.DrawLine(Tline_Simple_1D_Cut_Upper_X, 0, Tline_Simple_1D_Cut_Upper_X, Tline_Simple_1D_Cut_Upper_Y)
                            Tline_Simple_1D_Cut_Lower.DrawLine(Tline_Simple_1D_Cut_Lower_X, 0, Tline_Simple_1D_Cut_Lower_X, Tline_Simple_1D_Cut_Lower_Y)
                        

                        if("hmmCPARTall" in out_print_single):
                            Drawing_1D_Hist.GetYaxis().SetRangeUser(0, 1.5*Tline_Simple_Y2)
                            Drawing_1D_Hist.GetXaxis().SetRangeUser(-0.3, 0.3)

                            # Drawing_1D_Hist.GetXaxis().SetRangeUser(0, 0.025)
                        else:
    #                         Drawing_1D_Hist.GetYaxis().SetRangeUser(0, 1.5*Drawing_1D_Hist.GetMaximum())
                            Drawing_1D_Hist.GetYaxis().SetRangeUser(0, (2.5*Tline_Simple_Y2) if(Single_EvntType in ["SP"] and (Single_Bending_Type in ["Outbending"])) else 1.5*Tline_Simple_Y2)
#                             Drawing_1D_Hist.GetYaxis().SetRangeUser(0, 1.5*Tline_Simple_Y2)

                        if("Dmom_pel_Histo" in out_print_single):
                            # Drawing_1D_Hist.GetXaxis().SetRangeUser(-0.3, 0.3)
                            Drawing_1D_Hist.GetXaxis().SetRangeUser(-0.45, 0.2)

                        if("Dmom_pip_Histo" in out_print_single):
                            # Drawing_1D_Hist.GetXaxis().SetRangeUser(-0.3, 0.3)
                            Drawing_1D_Hist.GetXaxis().SetRangeUser(-0.45, 0.2)

                        if("Dmom_pro_Histo" in out_print_single):
                            # Drawing_1D_Hist.GetXaxis().SetRangeUser(-0.2, 0.2)
                            Drawing_1D_Hist.GetXaxis().SetRangeUser(-0.45, 0.45)

                            Drawing_1D_Hist.GetXaxis().SetRangeUser(-0.2, 0.25)

                        if("HWC_Histo_All" in out_print_single):
#                             Drawing_1D_Hist.GetXaxis().SetRangeUser(0.6, 1.3)
                            Drawing_1D_Hist.GetXaxis().SetRangeUser(0.4, 1.3)
                            
#                             Sigma_Wid = (histo_search_count_single[out_print].Sigma_Widths)[Drawing_1D_Hist_num - 1]
                            
#                             FP_Cut_Up = (histo_search_count_single[out_print].FindPeak_Cut_Up)[Drawing_1D_Hist_num - 1]
                            
#                             Tline_Wid_WC_Upper = ROOT.TLine()
#                             Tline_Wid_WC_Upper.SetLineColor(root_color.Green)
#                             Tline_Wid_WC_Upper.SetLineWidth(2)
                            
#                             Tline_Wid_WC_Lower = ROOT.TLine()
#                             Tline_Wid_WC_Lower.SetLineColor(root_color.Green)
#                             Tline_Wid_WC_Lower.SetLineWidth(2)
                            
#                             # print("Sigma_Wid = ", Sigma_Wid)
#                             # print("Sigma_Wid_Upper = ", Sigma_Wid[1][0])
#                             # print("Sigma_Wid_Lower = ", Sigma_Wid[1][1])
# #                             print("".join(["""    if(eleC.P() > """, str(Sigma_Wid[0][0]), " && eleC.P() < ", str(Sigma_Wid[0][1]), """){ // (""", str(Sigma_Wid[0][2]), """)
# #         Cut_Upper = """, str(round(Sigma_Wid[1][0], 2)), """;
# #         Cut_Lower = """, str(round(Sigma_Wid[1][1], 2)), """;
# #     }"""]))
                            
# #                             print("".join(["\neleC.P() = ", str(Sigma_Wid[0][2]), " --> Cut_Lower = ", str(round(Sigma_Wid[1][1], 4))]))
                            
# #                             print("".join(["""    if(eleC.P() > """, str(Sigma_Wid[0][0]), " && eleC.P() < ", str(Sigma_Wid[0][1]), """){ // (""", str(Sigma_Wid[0][2]), """)
# #         Cut_Upper = """, str(round(FP_Cut_Up,       4)), """;
# #         Cut_Lower = """, str(round(Sigma_Wid[1][1], 4)), """;
# #     }"""]))







# #                             print(str(round(FP_Cut_Up,       4)))
#                             print(str(round(Sigma_Wid[1][1], 4)))



    
#                             Tline_Wid_WC_Upper.DrawLine(FP_Cut_Up, 0, FP_Cut_Up, 1.25*Tline_Simple_Y2)
# #                             Tline_Wid_WC_Upper.DrawLine(round(Sigma_Wid[1][0], 2), 0, round(Sigma_Wid[1][0], 2), 1.25*Tline_Simple_Y2)
#                             Tline_Wid_WC_Lower.DrawLine(round(Sigma_Wid[1][1], 2), 0, round(Sigma_Wid[1][1], 2), 1.25*Tline_Simple_Y2)
                            
#                             Cut_EQ_Upper = eval(Cut_Function_Upper.replace("x", str(Sigma_Wid[0][2])))# (-0.0481)*Sigma_Wid[0][2] + 1.5787
#                             Cut_EQ_Lower = eval(Cut_Function_Lower.replace("x", str(Sigma_Wid[0][1])))# (-0.0381)*Sigma_Wid[0][1] + 1.173
                            

#                             Tline_Wid_WC_Upper_2 = ROOT.TLine()
#                             Tline_Wid_WC_Upper_2.SetLineColor(root_color.Pink)
#                             Tline_Wid_WC_Upper_2.SetLineWidth(2)
                            
#                             Tline_Wid_WC_Lower_2 = ROOT.TLine()
#                             Tline_Wid_WC_Lower_2.SetLineColor(root_color.Pink)
#                             Tline_Wid_WC_Lower_2.SetLineWidth(2)
                            
#                             Tline_Wid_WC_Upper_2.DrawLine(Cut_EQ_Upper, 0, Cut_EQ_Upper, 1.25*Tline_Simple_Y2)
#                             Tline_Wid_WC_Lower_2.DrawLine(Cut_EQ_Lower, 0, Cut_EQ_Lower, 1.25*Tline_Simple_Y2)


                    if(True):
                        Save_Name     = str(str(Canvas_Name.replace("''", "")).replace("(", "")).replace(")", "") + f"_{Single_Bending_Type}.pdf"
                        Save_Name     = str(Save_Name.replace("bending", ""))
                        Save_Name     = str(str(Save_Name.replace(" ", "_")).replace(",", "")).replace("_'3'_", "")
                        Save_Name     = str(str(Save_Name.replace("'el'_'el'", "el")).replace("'pip'_'pip'", "pip")).replace("'", "")
                        Save_Name     = str(Save_Name.replace("__", "_"))
                        Save_Name     = f"Single_Plot_Version_{Save_Name}"
                        Save_Name     = str(Save_Name.replace("Histom", "Histo_m"))
                        Save_Name     = str(Save_Name.replace("1_regall", ""))
                        if(("reg" in Save_Name) and ("_reg" not in Save_Name)):
                            Save_Name = str(Save_Name.replace("reg", "_reg"))
                        Save_Name     = str(Save_Name.replace("__", "_"))
                        if(Make_MM_Cuts):
                            Save_Name = Save_Name.replace("Norm", "MM_Cuts" if(Single_EvntType not in ["EO"]) else "WM_Cuts")
                        Single_Histogram_Canvas[Canvas_Name].SaveAs(Save_Name)
                        print(f"{color.BBLUE}Saved: {color.UNDERLINE}{Save_Name}{color.END}")



                except:
                    print(traceback.format_exc())

#                 print("}")








try:
    Can_Run_This_MM_Cut_Cell = Make_MM_Cuts
except:
    print("Make_MM_Cuts is not defined...")
    Can_Run_This_MM_Cut_Cell = False
    Make_MM_Cuts = False
    
while(Can_Run_This_MM_Cut_Cell):
    Names_of_Histos_Needed = ["hmmCPARTall_('mm0', 1, '', '3', 'reg1', 'el', 'el', '')", "hmmCPARTall_('mm0', 1, '', '3', 'reg2', 'el', 'el', '')", "hmmCPARTall_('mm0', 1, '', '3', 'reg3', 'el', 'el', '')", "hmmCPARTall_('mm0', 2, '', '3', 'reg1', 'el', 'el', '')", "hmmCPARTall_('mm0', 2, '', '3', 'reg2', 'el', 'el', '')", "hmmCPARTall_('mm0', 2, '', '3', 'reg3', 'el', 'el', '')", "hmmCPARTall_('mm0', 3, '', '3', 'reg1', 'el', 'el', '')", "hmmCPARTall_('mm0', 3, '', '3', 'reg2', 'el', 'el', '')", "hmmCPARTall_('mm0', 3, '', '3', 'reg3', 'el', 'el', '')", "hmmCPARTall_('mm0', 4, '', '3', 'reg1', 'el', 'el', '')", "hmmCPARTall_('mm0', 4, '', '3', 'reg2', 'el', 'el', '')", "hmmCPARTall_('mm0', 4, '', '3', 'reg3', 'el', 'el', '')", "hmmCPARTall_('mm0', 5, '', '3', 'reg1', 'el', 'el', '')", "hmmCPARTall_('mm0', 5, '', '3', 'reg2', 'el', 'el', '')", "hmmCPARTall_('mm0', 5, '', '3', 'reg3', 'el', 'el', '')", "hmmCPARTall_('mm0', 6, '', '3', 'reg1', 'el', 'el', '')", "hmmCPARTall_('mm0', 6, '', '3', 'reg2', 'el', 'el', '')", "hmmCPARTall_('mm0', 6, '', '3', 'reg3', 'el', 'el', '')"]
    MM_Cut_Code = '''
                Calculated_Exclusive_Cuts = "".join(["""
                    auto beam = ROOT::Math::PxPyPzMVector(0, 0, """,    str(Beam_Energy),          """, 0);
                    auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, """, str(Particle_Mass_Proton), """);
                    auto ele  = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
                    auto pip0 = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, """, str(Particle_Mass_PiC), """);

                    auto MM_Vector = beam + targ - ele - pip0;

                    auto cut_upper = 1.1;
                    auto cut_lower = 0;
                '''
    if(Single_EvntType in ["EO"]):
        Names_of_Histos_Needed = ["HWC_Histo_All_('mm0', 1, '1', 'regall', 'el', 'el', '')", "HWC_Histo_All_('mm0', 2, '1', 'regall', 'el', 'el', '')", "HWC_Histo_All_('mm0', 3, '1', 'regall', 'el', 'el', '')", "HWC_Histo_All_('mm0', 4, '1', 'regall', 'el', 'el', '')", "HWC_Histo_All_('mm0', 5, '1', 'regall', 'el', 'el', '')", "HWC_Histo_All_('mm0', 6, '1', 'regall', 'el', 'el', '')"]
        # MM_Cut_Code = '''
        # Calculated_Exclusive_Cuts = "".join(["""        
        # // For Invariant Mass Cut (Spring 2019 (Pass 2) - Based on a 1.75*sigma and 2*sigma cuts on the Invarient Mass - Upper Cut is 1.75*sigma - Lower Cut is 2*sigma - Linear Functions of Momentum - No Phi dependence):
        # auto Beam_Energy = """, str(Beam_Energy), """;
        # auto Proton_Mass = """, str(Particle_Mass_Proton), """;
        # auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
        # auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
        # auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
        # auto Cut_Variable = (beam + targ - eleC).M();
        # auto Upper_Cut = 1.3;
        # auto Lower_Cut = 0.7;'''
        MM_Cut_Code = '''
        Calculated_Exclusive_Cuts = "".join(["""        
        // For Invariant Mass Cut (Outbending Fall 2018 (Pass 2) - Based on a 1.75*sigma and 2*sigma cuts on the Invarient Mass - Upper Cut is 1.75*sigma - Lower Cut is 2*sigma - Linear Functions of Momentum - No Phi dependence):
        auto Beam_Energy = """, str(Beam_Energy), """;
        auto Proton_Mass = """, str(Particle_Mass_Proton), """;
        auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
        auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
        auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
        auto Cut_Variable = (beam + targ - eleC).M();
        auto Upper_Cut = 1.3;
        auto Lower_Cut = 0.7;'''
    
    for Name_Needed in Names_of_Histos_Needed:
        if(str(Name_Needed) not in histo_search_count_single):
            print("Missing Histogram Named:", Name_Needed, color.Error, "\nCannot finish running this cell until this histogram is added...", color.END)
            Can_Run_This_MM_Cut_Cell = False
            break
    if(not Can_Run_This_MM_Cut_Cell):
        break
    
    Base_Histo_Name = "hmmCPARTall_('mm0', SECTOR_NUM, '', '3', 'REGION_NAME', 'el', 'el', '')" if(Single_EvntType not in ["EO"]) else "HWC_Histo_All_('mm0', SECTOR_NUM, '1', 'regall', 'el', 'el', '')"
    print("Base_Histo_Name =", Base_Histo_Name)
    for Sector_MM in range(1, 7, 1):
        Current_Sector_Histo_Name = Base_Histo_Name.replace("SECTOR_NUM", str(Sector_MM))
        MM_Cut_Code               = "".join([str(MM_Cut_Code), '''
        if(esec == ''' if(Single_EvntType in ["EO"]) else '''
                    if(esec == ''', str(Sector_MM), '''){'''])
        if(Single_EvntType in ["EO"]):
        #     MM_Cut_Code           = "".join([str(MM_Cut_Code), '''
        #     Upper_Cut = (''', str(round(Cut_Fit_Line_Upper[Current_Sector_Histo_Name].GetParameter("A"), 7)), ''')*el + (''', str(round(Cut_Fit_Line_Upper[Current_Sector_Histo_Name].GetParameter("B"), 7)), ''');
        #     Lower_Cut = (''', str(round(Cut_Fit_Line_Lower[Current_Sector_Histo_Name].GetParameter("B"), 7)), ''');
        # }'''])
            MM_Cut_Code           = "".join([str(MM_Cut_Code), '''
            Upper_Cut = (''',  str(round(Cut_Fit_Line_Upper[Current_Sector_Histo_Name].GetParameter("A"), 7)), ''')*el + (''', str(round(Cut_Fit_Line_Upper[Current_Sector_Histo_Name].GetParameter("B"), 7)), ''');
            Lower_Cut =  (''', str(round(Cut_Fit_Line_Lower[Current_Sector_Histo_Name].GetParameter("A"), 7)), ''')*el + (''', str(round(Cut_Fit_Line_Lower[Current_Sector_Histo_Name].GetParameter("B"), 7)), ''');
        }'''])
        else:
            for Phi_Region in ["reg1", "reg2", "reg3"]:
                Current_Histo_Name    = Current_Sector_Histo_Name.replace("REGION_NAME", str(Phi_Region))
                Phi_Condition         = "localelPhiS > -5 && localelPhiS < 5" if(Phi_Region == "reg1") else "localelPhiS < -5" if(Phi_Region == "reg2") else "localelPhiS > 5" if(Phi_Region == "reg3") else "esec != -3"
                MM_Cut_Code           = "".join([str(MM_Cut_Code), '''
                        if(''', str(Phi_Condition), '''){
                            // Upper Cut
                            cut_upper = (''', str(round(Cut_Fit_Line_Upper[Current_Histo_Name].GetParameter("A"), 7)), ''')*el + (''', str(round(Cut_Fit_Line_Upper[Current_Histo_Name].GetParameter("B"), 7)), ''');
                            // Lower Cut
                            cut_lower = (''', str(round(Cut_Fit_Line_Lower[Current_Histo_Name].GetParameter("A"), 7)), ''')*el + (''', str(round(Cut_Fit_Line_Lower[Current_Histo_Name].GetParameter("B"), 7)), ''');
                        }'''])
            MM_Cut_Code               = "".join([str(MM_Cut_Code), '''
                    }'''])
    Can_Run_This_MM_Cut_Cell = False
    print("MM_Cut_Code:\n", MM_Cut_Code, ''' 

                    return (MM_Vector.M() < cut_upper && MM_Vector.M() > cut_lower);

                """])''' if(Single_EvntType not in ["EO"]) else '''
        return ((Cut_Variable < Upper_Cut) && (Cut_Variable > Lower_Cut));
        """]) if(("Pass 2" in str(pass_version)) and ("Out" not in str(datatype))) else ''')
    print("\n\nDONE WITH MISSING MASS CUTS\n\n")
else:
    if(not Make_MM_Cuts):
        print("Did not run Missing Mass Cuts (make Make_MM_Cuts = True)")




print("Done")
