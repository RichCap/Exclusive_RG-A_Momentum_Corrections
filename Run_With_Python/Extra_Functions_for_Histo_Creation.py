import ROOT
import traceback
from Functions_for_Printing_Corrections import *


#################################################################################################################
#####==========#####==========#####################################################==========#####==========#####
#####==========#####==========#####     Drawing 1D Histograms with Canvas     #####==========#####==========#####
#####==========#####==========#####################################################==========#####==========#####
#################################################################################################################

def Draw_1D_Histos_with_Canvas(Histo_2D_In, Canvas_Object, Canvas_Name, Sector_Number, Save_Option):

    stats_box_1D_all, Histo_2D_Extra = {}, {}
    
    if(type(Histo_2D_In) is list):
        Histo_2D = (Histo_2D_In[0]).Clone()
        try:
            print(type(Histo_2D.hys2))
        except:
            # print("NEED TO RECREATE...")
            Histo_2D = Find_And_Slice_Histo(RDF=rdf_List[str(("DP", 'Inbending', 'Fall2018'))], NAME=Histo_2D.GetName(), EVENT="DP", PARTICLE="pro", OUT_Q="Histo", Pass_Type='Fall2018')
        
        for ii in range(1, len(Histo_2D_In), 1):
            Histo_2D_Extra[ii] = (Histo_2D_In[ii]).Clone()
            # print("".join(["type(Histo_2D_Extra[", str(ii), "]) == type(Histo_2D) ==> ", color.BLUE, color.BOLD, str(type(Histo_2D_Extra[ii]) == type(Histo_2D)), color.END]))
            try:
                print(type(Histo_2D_Extra[ii].hys2))
            except:
                # print("NEED TO RECREATE...")
                Histo_2D_Extra[ii] = Find_And_Slice_Histo(RDF=rdf_List[str(("DP", 'Inbending', 'Fall2018'))], NAME=Histo_2D_Extra[ii].GetName(), EVENT="DP", PARTICLE="pro", OUT_Q="Histo", Pass_Type='Fall2018')
            
    else:
        Histo_2D = Histo_2D_In.Clone()
        Histo_2D_Extra = "Not Needed"
    
    Divide_1 = 6
    #try:
    Divide_1 = len(Histo_2D.hys2)
    #except:
    #    print("ERROR")
    
    Divide_2 = 6 if(not (Sector_Number in [0, "all"])) else 1
    
    Canvas_Size_1 = 600*Divide_1 if(600*Divide_1 < 3600) else 3600
    Canvas_Size_2 = 900 if(Sector_Number in [0, "all"]) else Canvas_Size_1
    
    Canvas_Size_1 = 4800 if(len(Histo_2D.hys2) > 2) else 1200
    Canvas_Size_2 = 4800
    
    
    try:
        Canvas_Object["".join([Canvas_Name, "_1D_histos"])]
    except:
        Canvas_Object["".join([Canvas_Name, "_1D_histos"])] = ROOT.TCanvas("".join([Canvas_Name, "_1D_histos"]), "".join([Canvas_Name, "_1D_histos"]), Canvas_Size_1, Canvas_Size_2)
        Canvas_Object["".join([Canvas_Name, "_1D_histos"])].Divide(1, Divide_2, 0, 0)
        Canvas_Object["".join([Canvas_Name, "_1D_histos"])].SetGrid()

    cd_sec = Sector_Number if(Sector_Number not in [0, "all"]) else 1
    
    Canvas_1D_Sec_CD = (Canvas_Object["".join([Canvas_Name, "_1D_histos"])].cd(cd_sec))
    
    # Canvas_Object["".join([Canvas_Name, "_1D_histos"])].cd(cd_sec).Divide(Divide_1, 1, 0, 0)
    
    try:
        if(len(Histo_2D.hys2) > 10):
            Divide_1_1 = int(len(Histo_2D.hys2)/2) + 1
            Canvas_1D_Sec_CD.Divide(Divide_1_1, 2, 0, 0)
        else:
            Canvas_1D_Sec_CD.Divide(Divide_1, 1, 0, 0)
        
    except Exception as e:
        print("".join([color.RED, "ERROR IN ADVANCED 1D HISTOGRAM CANVASES: ", str(e), color.END, "\nTraceback: \n", str(traceback.format_exc())]))
        Canvas_Object["".join([Canvas_Name, "_1D_histos"])].cd(cd_sec).Divide(Divide_1, 1, 0, 0)
    
    ROOT.gStyle.SetAxisColor(16,'xy')
    # ROOT.gStyle.SetOptFit(0)
    ROOT.gStyle.SetOptFit(1)
    ROOT.gStyle.SetOptStat("er")
    # ROOT.gStyle.SetOptStat(1)
    ROOT.gStyle.SetTitleY(1)
    ROOT.gStyle.SetTitleX(0.5)
    
    
    Canvas_Object["".join([Canvas_Name, "_1D_histos"])].Draw()
    
    # cd_start = 0 if(Sector_Number == 0 or Sector_Number == "all") else (Sector_Number - 1)*Divide_1
    
    try:
        
        Drawing_1D_Hist_num = 0
        for Drawing_1D_Hist in Histo_2D.hys2:
            Draw_Canvas(Canvas_1D_Sec_CD, Drawing_1D_Hist_num + 1, 0.05, 0, -0.02, 0)
            
            if("hmmCPARTall" in Canvas_Name):
                title_MM = Drawing_1D_Hist.GetTitle()

                if("Double Pion" not in title_MM):
                    title_MM = title_MM.replace("No El Cor - No Pi+ Cor - No Pi- Cor - No Pro Cor", "No Momentum Corrections")
                    title_MM = (title_MM.replace("Pi+", "#pi^{+}")).replace("Pi-", "#pi^{-}")

                    title_MM = title_MM.replace("Phi", "#phi")
                

                    if("Sector 1}}" in title_MM or "Sector 2}}" in title_MM or "Sector 3}}" in title_MM or "Sector 4}}" in title_MM or "Sector 5}}" in title_MM or "Sector 6}}" in title_MM):
                        title_MM = str((((((title_MM.replace("Sector 1}}", "Sector 1")).replace("Sector 2}}", "Sector 2")).replace("Sector 3}}", "Sector 3")).replace("Sector 4}}", "Sector 4")).replace("Sector 5}}", "Sector 5")).replace("Sector 6}}", "Sector 6"))
                    else:
                        title_MM = (title_MM.replace("#font[22]{", "#font[22]{#splitline{")).replace(" ---- p", "{p")

                    if("reg1" in Canvas_Name or "reg2" in Canvas_Name or "reg3" in Canvas_Name):
                        title_color, title_bin = [root_color.Black, "Center"] if("reg1" in Canvas_Name) else [root_color.Red, "Negative"] if("reg2" in Canvas_Name) else [root_color.Green, "Positive"] if("reg3" in Canvas_Name) else [root_color.Red, "Error in"]
                        # title_MM = "".join(["#splitline{", str(title_MM), "}{#scale[2]{#color[", str(root_color.Red), "]{", "Center" if("reg1" in Canvas_Name) else "Negative" if("reg2" in Canvas_Name) else "Positive" if("reg3" in Canvas_Name) else "Error in", " #phi Bin}}}"])
                        title_MM = "".join(["#splitline{", str(title_MM), "}{#scale[2]{#color[", str(title_color), "]{", str(title_bin), " #phi Bin}}}"])

                # print(title_MM)
                Drawing_1D_Hist.SetTitle(title_MM)
                
                title_MM_X = Drawing_1D_Hist.GetXaxis().GetTitle()
                title_MM_X = title_MM_X.replace("MM^2", "MM^{2}")
                Drawing_1D_Hist.GetXaxis().SetTitle(title_MM_X)
            

            
            Draw_Canvas(Canvas_1D_Sec_CD, Drawing_1D_Hist_num + 1, 0.05, 0, -0.02, 0)
            Drawing_1D_Hist.Draw("same")
            # Histo_2D.hys2[Drawing_1D_Hist_num].ShowBackground(2, "same")
            
            if(Histo_2D_Extra != "Not Needed"):
                Drawing_1D_Hist.SetLineWidth(3)
                try:
                    for Extra_Histo in Histo_2D_Extra:
                        # print("".join(["type(Histo_2D_Extra[Extra_Histo]) == type(Histo_2D) ==> ", color.BLUE, color.BOLD, str(type(Histo_2D_Extra[Extra_Histo]) == type(Histo_2D)), color.END]))
                        Histo_2D_Extra[Extra_Histo].hys2[Drawing_1D_Hist_num].SetLineWidth(3)
                        Histo_2D_Extra[Extra_Histo].hys2[Drawing_1D_Hist_num].SetLineStyle(2)
                        Histo_2D_Extra[Extra_Histo].hys2[Drawing_1D_Hist_num].SetLineColor(1 if("mm0" in str(Histo_2D_Extra[Extra_Histo].GetName())) else 46 if("mmEF_PipMMEF" in str(Histo_2D_Extra[Extra_Histo].GetName())) else 3)
                        Draw_Canvas(Canvas_1D_Sec_CD, Drawing_1D_Hist_num + 1, 0.05, 0, -0.02, 0)
                        Histo_2D_Extra[Extra_Histo].hys2[Drawing_1D_Hist_num].Draw("same")
                except Exception as e:
                    print("".join([color.RED, color.BOLD, "ERROR IN EXTRA 1D HISTOGRAM: ", str(e), color.END, color.RED, "\nTraceback: \n", color.END, str(traceback.format_exc())]))
                    
                    
                Draw_Canvas(Canvas_1D_Sec_CD, Drawing_1D_Hist_num + 1, 0.05, 0, -0.02, 0)
                Drawing_1D_Hist.Draw("same")
                # Histo_2D.hys2[Drawing_1D_Hist_num].ShowBackground(2, "same")
            
                
            if("Dmom_pel_Histo" in Canvas_Name and "E" in event_type):
                Histo_2D.hys2[Drawing_1D_Hist_num].ShowPeaks()
            Drawing_1D_Hist_num += 1
            
            Canvas_Object["".join([Canvas_Name, "_1D_histos"])].Modified()
            Canvas_Object["".join([Canvas_Name, "_1D_histos"])].Update()
            stats_box_1D_all["".join([Canvas_Name, "_1D_histos_", str(cd_sec), "_", str(Drawing_1D_Hist_num + 1)])] = ""
            if("hmmCPARTall" not in Canvas_Name):
                # statbox_move(Drawing_1D_Hist, Canvas_1D_Sec_CD, stats_box_1D_all["".join([Canvas_Name, "_1D_histos_", str(cd_sec), "_", str(Drawing_1D_Hist_num + 1)])], 1, "off")#, 0.1, 0.45, 0.5, 0.5)
                statbox_move(Drawing_1D_Hist, Canvas_1D_Sec_CD, stats_box_1D_all["".join([Canvas_Name, "_1D_histos_", str(cd_sec), "_", str(Drawing_1D_Hist_num + 1)])], 1, "MM_1D")#, 0.1, 0.45, 0.5, 0.5)
            else:
                statbox_move(Drawing_1D_Hist, Canvas_Object["".join([Canvas_Name, "_1D_histos"])], stats_box_1D_all["".join([Canvas_Name, "_1D_histos_", str(cd_sec), "_", str(Drawing_1D_Hist_num + 1)])], 1, "MM_1D")
            
            Draw_Canvas(Canvas_1D_Sec_CD, Drawing_1D_Hist_num, 0.05, 0, -0.02, 0)
            
            Tline_Simple_1D = ROOT.TLine()
            Tline_Simple_1D.SetLineColor(root_color.Red)
            Tline_Simple_1D.SetLineWidth(2)
            
            Tline_Simple_Ideal_1D = ROOT.TLine()
            Tline_Simple_Ideal_1D.SetLineColor(root_color.Black)
            Tline_Simple_Ideal_1D.SetLineWidth(2)
            
            Tline_Simple_1D_Peak_X = Histo_2D.FindPeak_x[Drawing_1D_Hist_num - 1]
            Tline_Simple_1D_Ideal_X = 0.9383 if("HWC_Histo_All" in Canvas_Name) else (0.13957*0.13957) if(MM_type == "eppipX") else (0.1349768*0.1349768) if("pi0" in MM_type) else 0.9396 if(MM_type == "epipX") else 0
            
            if("Dmom" in Canvas_Name):
                Tline_Simple_1D_Ideal_X = 0
            
            Tline_Simple_1D_Y1, Tline_Simple_Y2 = 0, Histo_2D.FindPeak_y[(Drawing_1D_Hist_num - 1)]
            
            Tline_Simple_Ideal_1D.DrawLine(Tline_Simple_1D_Ideal_X, 0, Tline_Simple_1D_Ideal_X, Tline_Simple_Y2)
            Tline_Simple_1D.DrawLine(Tline_Simple_1D_Peak_X, 0, Tline_Simple_1D_Peak_X, Tline_Simple_Y2)
            
            if("hmmCPARTall" in Canvas_Name):
                Drawing_1D_Hist.GetYaxis().SetRangeUser(0, 1.5*Tline_Simple_Y2)
            else:
                Drawing_1D_Hist.GetYaxis().SetRangeUser(0, 1.5*Drawing_1D_Hist.GetMaximum())
            
            if("Dmom_pel_Histo" in Canvas_Name):
                Drawing_1D_Hist.GetXaxis().SetRangeUser(-0.3, 0.3)
                
            if("Dmom_pip_Histo" in Canvas_Name):
                Drawing_1D_Hist.GetXaxis().SetRangeUser(-0.3, 0.3)
                
            if("Dmom_pro_Histo" in Canvas_Name):
                Drawing_1D_Hist.GetXaxis().SetRangeUser(-0.3, 0.3)
                
                    
            if("HWC_Histo_All" in Canvas_Name):
                # Drawing_1D_Hist.GetXaxis().SetRangeUser(0.6, 1.75)
                Drawing_1D_Hist.GetXaxis().SetRangeUser(0.6, 1.3)
                
                
            Canvas_Object["".join([Canvas_Name, "_1D_histos"])].Modified()
            Canvas_Object["".join([Canvas_Name, "_1D_histos"])].Update()
                
            
        blank_Canvas = Canvas_Create(Name="test_blank_new", Num_Columns=3, Num_Rows=2, Size_X=1500, Size_Y=1200, cd_Space=0)
        if(Save_Option == "yes"):
            # print(str("".join([Canvas_Name, "_1D_histos.png"])))
            Canvas_Object["".join([Canvas_Name, "_1D_histos"])].SaveAs(("".join([str(Canvas_Name).replace(Correction_Name, corNameTitles(Correction_Name).replace("/", "_")), "_", str(Selection_of_In_or_Out), "_", str(event_type), str(Extra_Saving_Name), "_1D_histos.png"])).replace(" ", "_"))
            
        return Canvas_Object["".join([Canvas_Name, "_1D_histos"])]
        
    except Exception as e:
        print(f"{color.Error}\nFailed to draw canvas...\n{color.END}")
        print("".join([color.RED, "ERROR: ", str(e), color.END, "\nTraceback: \n", str(traceback.format_exc())]))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
############################################################################################################
#####==========#####==========################################################==========#####==========#####
#####==========#####==========#####     Histogram Creation/Retrieval     #####==========#####==========#####
#####==========#####==========################################################==========#####==========#####
############################################################################################################

def Find_And_Slice_Histo(RDF, NAME, EVENT, PARTICLE, BENDING=Selection_of_In_or_Out, OUT_Q="Both", Pass_Type="Fall2018"):
    try:
        
        Histo_Out = (RDF.Get(NAME)).Clone()
        event_title = "".join(["#splitline{", "Single Pion Channel" if(EVENT == "SP") else "Electron Only" if(EVENT == "EO") else "Elastic Scattering" if(EVENT == "ES") else "Double Pion Channel" if(EVENT == "DP") else "#pi^{0} Channel" if(EVENT == "P0") else "Single Pion Channel (Monte Carlo)" if(EVENT in ["MC", "Monte_Carlo"]) else "ERROR", "}{"])
        if("ERROR" in event_title):
            event_title = ""
        Histo_Title_New = "".join([event_title, "#color[", str(root_color.Red), "]{",  Histo_Out.GetTitle(), "}", "}" if(event_title != "") else ""])

        if("localelPhiS" in Histo_Title_New):
            Histo_Title_New = Histo_Title_New.replace("localelPhiS", "#phi_{El}")

        if("localpipPhiS" in Histo_Title_New):
            Histo_Title_New = Histo_Title_New.replace("localpipPhiS", "#phi_{#pi^{+}}")
            
        if(OUT_Q != "Title"):
        
            Histo_Out.SetTitle(Histo_Title_New)

            blank_Canvas = Canvas_Create(Name="".join(["test_blank_func_", str(NAME)]), Num_Columns=3, Num_Rows=2, Size_X=1500, Size_Y=1200, cd_Space=0)
            # Fit_Pars, TLine_Simple_Pars = Fitting_Lines(NAME, EVENT, BENDING, PARTICLE)
            Fit_Pars, TLine_Simple_Pars = Fitting_Lines(Histo_Type=NAME, Event_Type=EVENT, Bending_Type=BENDING, Particle=PARTICLE, DataSet=Pass_Type)
            MinRange_Fit, MaxRange_Fit, Increment_Fit = Fit_Pars
            Tline_Simple_X1, Tline_Simple_Y1, Tline_Simple_X2, Tline_Simple_Y2 = TLine_Simple_Pars


        ###################################################################################################
        ##==================================###########################==================================##
        ##==========##==========##==========##     ∆P Histograms     ##==========##==========##==========##
        ##==================================###########################==================================##
        ###################################################################################################
            dp_bg_option = "no"
            ##############################################################
            ##==========##     ∆P (Electron) Histograms     ##==========##
            ##############################################################
            if("Dmom_pel_Histo" in NAME):
                if(PARTICLE != "el"):
                    print("".join([color.RED, "\n\nERROR: WRONG PARTICLE INPUT FOR ∆P(el)...\n\n", color.END]))
                    blank_Canvas = Canvas_Create(Name="".join(["test_blank_func_", str(NAME)]), Num_Columns=3, Num_Rows=2, Size_X=1500, Size_Y=1200, cd_Space=0)
                fit_Dp_2D_Out(Histo_Out, MinRange_Fit, MaxRange_Fit, Increment_Fit, Histo_Out.GetTitle(), dp_bg_option, "el", Bending_Type=BENDING)
                # blank_Canvas = Canvas_Create(Name="test_blank_func", Num_Columns=3, Num_Rows=2, Size_X=1500, Size_Y=1200, cd_Space=0)
                # Histo_Out.GetYaxis().SetRangeUser(-0.5, 1)
                Histo_Out.GetYaxis().SetRangeUser(-0.3, 0.3)
                Histo_Out.GetXaxis().SetRangeUser(Tline_Simple_X1, Tline_Simple_X2)
            ############################################################
            ##==========##     ∆P (Proton) Histograms     ##==========##
            ############################################################
            if("Dmom_pro_Histo" in NAME):
                if(PARTICLE != "pro"):
                    print("".join([color.RED, "\n\nERROR: WRONG PARTICLE INPUT FOR ∆P(pro)...\n\n", color.END]))
                    blank_Canvas = Canvas_Create(Name="".join(["test_blank_func_", str(NAME)]), Num_Columns=3, Num_Rows=2, Size_X=1500, Size_Y=1200, cd_Space=0)
                fit_Dp_2D_Out(Histo_Out, MinRange_Fit, MaxRange_Fit, Increment_Fit, Histo_Out.GetTitle(), dp_bg_option, "pro", Bending_Type=BENDING)
                # blank_Canvas = Canvas_Create(Name="test_blank_func", Num_Columns=3, Num_Rows=2, Size_X=1500, Size_Y=1200, cd_Space=0)
                Histo_Out.GetYaxis().SetRangeUser(-0.6, 0.6)
                Histo_Out.GetXaxis().SetRangeUser(Tline_Simple_X1, Tline_Simple_X2)
            #############################################################
            ##==========##     ∆P (π+ Pion) Histograms     ##==========##
            #############################################################
            if("Dmom_pip_Histo" in NAME):
                if(PARTICLE != "pip"):
                    print("".join([color.RED, "\n\nERROR: WRONG PARTICLE INPUT FOR ∆P(pip)...\n\n", color.END]))
                    blank_Canvas = Canvas_Create(Name="".join(["test_blank_func_", str(NAME)]), Num_Columns=3, Num_Rows=2, Size_X=1500, Size_Y=1200, cd_Space=0)
                fit_Dp_2D_Out(Histo_Out, MinRange_Fit, MaxRange_Fit, Increment_Fit, Histo_Out.GetTitle(), dp_bg_option, "pip", Bending_Type=BENDING)
                # blank_Canvas = Canvas_Create(Name="test_blank_func", Num_Columns=3, Num_Rows=2, Size_X=1500, Size_Y=1200, cd_Space=0)
                Histo_Out.GetYaxis().SetRangeUser(-0.3, 0.3)
                # Histo_Out.GetXaxis().SetRangeUser(Tline_Simple_X1, Tline_Simple_X2 + 0.5)
            ##############################################################
            ##==========##    ∆Theta (Proton) Histograms    ##==========##
            ##############################################################
            if("Dmom_Angle_Histo" in NAME):
                if(PARTICLE != "el"):
                    print("".join([color.RED, "\n\nERROR: WRONG PARTICLE INPUT FOR ∆P(el)...\n\n", color.END]))
                if("D_Angle_V1" in NAME):
                    Histo_Out.GetYaxis().SetRangeUser(-3, 3)
                if("D_Angle_V3" in NAME):
                    Histo_Out.GetYaxis().SetRangeUser(171, 189)
                title_Dth = Histo_Out.GetTitle()
                title_Dth = title_Dth.replace("No El Cor - No Pi+ Cor - No Pi- Cor - No Pro Cor", "No Momentum Corrections")
                if("D_Angle_V3" not in out_print):
                    title_Dth = title_Dth.replace("#splitline{ vs", "".join(["#splitline{#Delta #theta_{Pro} (Version ", "1" if("D_Angle_V1" in NAME) else "2" if("D_Angle_V2" in NAME) else "3", ") vs"]))
                else:
                    title_Dth = title_Dth.replace("#splitline{ vs", "#splitline{#Delta #phi_{|El-Pro|} vs")
                    if("phi_{|" not in Histo_Out.GetYaxis().GetTitle()):
                        Histo_Out.GetYaxis().SetTitle(Histo_Out.GetYaxis().GetTitle().replace("#Delta#phi", "#Delta #phi_{|El-Pro|}"))
                Histo_Out.SetTitle(title_Dth)
                blank_Canvas = Canvas_Create(Name="".join(["test_blank_func_", str(NAME)]), Num_Columns=3, Num_Rows=2, Size_X=1500, Size_Y=1200, cd_Space=0)
                fit_Dp_2D_Out(Histo_Out, MinRange_Fit, MaxRange_Fit, Increment_Fit, Histo_Out.GetTitle(), dp_bg_option, "el", Bending_Type=BENDING, D_Angle=("Theta" if("D_Angle_V3" not in NAME) else "Phi"), Cut_Q=False)
                # blank_Canvas = Canvas_Create(Name="test_blank_func", Num_Columns=3, Num_Rows=2, Size_X=1500, Size_Y=1200, cd_Space=0)
                Histo_Out.GetXaxis().SetRangeUser(Tline_Simple_X1, Tline_Simple_X2 + 0.5)


        #############################################################################################################
        ##==================================#####################################==================================##
        ##==========##==========##==========##     Missing Mass Histograms     ##==========##==========##==========##
        ##==================================#####################################==================================##
        #############################################################################################################
            MM_bg_option = "no"
            if("hmmCPARTall" in NAME):
                Histo_Out.GetYaxis().SetTitle(Histo_Out.GetYaxis().GetTitle().replace("MM^2", "MM^{2}"))
                blank_Canvas = Canvas_Create(Name="".join(["test_blank_func_", str(NAME)]), Num_Columns=3, Num_Rows=2, Size_X=1500, Size_Y=1200, cd_Space=0)
                # Histo_Out = fit2dall(Histo_Out.Clone(), MinRange_Fit, MaxRange_Fit, Increment_Fit, Histo_Out.GetTitle(), MM_bg_option, PARTICLE)
                Histo_Out = MM_Fits(Histo_Out.Clone(), MinRange_Fit, MaxRange_Fit, Increment_Fit, Histo_Out.GetTitle(), MM_bg_option, PARTICLE, Bending_Type=BENDING)
                # blank_Canvas = Canvas_Create(Name="test_blank_func", Num_Columns=3, Num_Rows=2, Size_X=1500, Size_Y=1200, cd_Space=0)
                # if(EVENT == "SP"):
                #     Histo_Out.GetYaxis().SetRangeUser(0.88, 1)
                # else:
                #     Histo_Out.GetYaxis().SetRangeUser((Tline_Simple_Y1 - 0.1) if(EVENT != "DP") else -0.05, (Tline_Simple_Y1 + 0.1) if(EVENT != "DP") else 0.1)
                Histo_Out.GetXaxis().SetRangeUser(Tline_Simple_X1, Tline_Simple_X2 + 0.5)

        ###############################################################################################################
        ##==================================#######################################==================================##
        ##==========##==========##==========##     Invariant Mass Histograms     ##==========##==========##==========##
        ##==================================#######################################==================================##
        ###############################################################################################################
            WM_bg_option = "no"
            if("HWC_Histo_All" in NAME):
                if(EVENT != "SP"):
                    blank_Canvas = Canvas_Create(Name="".join(["test_blank_func_", str(NAME)]), Num_Columns=3, Num_Rows=2, Size_X=1500, Size_Y=1200, cd_Space=0)
                    fit_WM_2D(Histo_Out, MinRange_Fit, MaxRange_Fit, Increment_Fit, Histo_Title_New, WM_bg_option, PARTICLE)
                    # blank_Canvas = Canvas_Create(Name="test_blank_func", Num_Columns=3, Num_Rows=2, Size_X=1500, Size_Y=1200, cd_Space=0)
                    # Histo_Out.GetYaxis().SetRangeUser(0.5, 1.5)
                    # Histo_Out.GetYaxis().SetRangeUser(0.6, 1.3)
                    Histo_Out.GetYaxis().SetRangeUser(0.8, 1.1)
#                     Histo_Out.GetXaxis().SetRangeUser(8, Tline_Simple_X2 + 0.5)
                else:
                    Histo_Out.GetYaxis().SetRangeUser(0, 4)
                    
                    Histo_Out.GetXaxis().SetRangeUser(Tline_Simple_X1, Tline_Simple_X2 + 0.5)

        # blank_Canvas = Canvas_Create(Name="test_blank_func", Num_Columns=1, Num_Rows=1, Size_X=600, Size_Y=800, cd_Space=0)
        
    except Exception as e:
        print("".join([color.RED, color.BOLD, "\n\nERROR IN HISTOGRAM:\n", color.END, color.RED, str(e), "\n", color.END]))
        print(traceback.format_exc())
        print("\n")
        Histo_Out, Histo_Title_New = "error", "error"
            
    if(OUT_Q == "Both"):
        return [Histo_Out, Histo_Title_New]
    elif(OUT_Q == "Title"):
        return Histo_Title_New
    else:
        return Histo_Out

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#############################################################################################################################
#####==========#####==========#################################################################==========#####==========#####
#####==========#####==========#####     Extra Functions to Help with Histogram Search     #####==========#####==========#####
#####==========#####==========#################################################################==========#####==========#####
#############################################################################################################################

def Condition_Check_Full(Locate_Name_Full_Check, CheckDataFrameQ2_Check, Locate_Name_Sec_Check, out_print_Check):
    condition_Check = False
    if("list" not in str(type(Locate_Name_Full_Check))):
        condition_Check = ('f' in CheckDataFrameQ2_Check or Locate_Name_Sec_Check in out_print_Check)
    elif(len(Locate_Name_Full_Check) > 1):
        condition_Check_2 = 0
        for secondary_check in range(1, len(Locate_Name_Full_Check), 1):
            if(Locate_Name_Full_Check[secondary_check] in out_print_Check):
                condition_Check_2 += 1
                break
        condition_Check = ('f' in CheckDataFrameQ2_Check or (Locate_Name_Sec_Check in out_print_Check and condition_Check_2 != 0))
    return condition_Check



def Full_List_of_Histo_Options(Locate_Name_Full_In, Correction_Name_List_In, Sector_Number_List_In, Binning_Option_List_In, Region_Option_List_In, Particle_Mom_List_In, Particle_Sec_List_In, Extra_Cut_Option_In, D_Angle_Type_In, Get_Dp_Cors_Master_In):
    
    if("list" not in str(type(Locate_Name_Full_In))):
        Locate_name = str(Locate_Name_Full_In)
        print("\nPrinting the full list of histogram names saved in the root file loaded...\n" if('f' in CheckDataFrameQ2) else "".join(["\nSearching for files with: ", color.BOLD, Locate_name, color.END, "\n"]))
    else:
        Locate_name = str(Locate_Name_Full_In[0])
        print("\nPrinting the full list of histogram names saved in the root file loaded...\n" if('f' in CheckDataFrameQ2) else "".join(["\nSearching for files which Include: ", color.BOLD, str(Locate_Name_Full_In).replace('", ', '"\n\t\t\t\t    '), color.END, "\n"]))

    if("Correction_Name_List" in Locate_name):
        print("".join(["\t(*) 'Correction_Name_List' refers to a list of the corrections given by this list: ", color.BOLD, str(Correction_Name_List_In), color.END]))
        Correction_Name_List_2 = Correction_Name_List_In
    else:
        Correction_Name_List_2 = [Correction_Name_List_In[0]]

    if("Sector_Number_List" in Locate_name):
        print("".join(["\t(*) 'Sector_Number_List' refers to a list of the sector numbers given by this list: ", color.BOLD, str(Sector_Number_List_In), color.END]))
        Sector_Number_List_2 = Sector_Number_List_In
    else:
        Sector_Number_List_2 = [Sector_Number_List_In[0]]

    if("Binning_Option_List" in Locate_name):
        print("".join(["\t(*) 'Binning_Option_List' refers to a list of the number of Phi bins given by this list: ", color.BOLD, str(Binning_Option_List_In), color.END]))
        Binning_Option_List_2 = Binning_Option_List_In
    else:
        Binning_Option_List_2 = [Binning_Option_List_In[0]]

    if("Region_Option_List" in Locate_name):
        print("".join(["\t(*) 'Region_Option_List' refers to a list of the different Phi regions given by this list: ", color.BOLD, str(Region_Option_List_In), color.END]))
        Region_Option_List_2 = Region_Option_List_In
    else:
        Region_Option_List_2 = [Region_Option_List_In[0]]

    if("Particle_Mom_List" in Locate_name):
        print("".join(["\t(*) 'Particle_Mom_List' refers to a list of the particle momentums given by this list: ", color.BOLD, str(Particle_Mom_List_In), color.END]))
        Particle_Mom_List_2 = Particle_Mom_List_In
    else:
        Particle_Mom_List_2 = [Particle_Mom_List_In[0]]

    if("Particle_Sec_List" in Locate_name):
        print("".join(["\t(*) 'Particle_Sec_List' refers to a list of the particle sectors/binning given by this list: ", color.BOLD, str(Particle_Sec_List_In), color.END]))
        Particle_Sec_List_2 = Particle_Sec_List_In
    else:
        Particle_Sec_List_2 = [Particle_Sec_List_In[0]]

    if("Extra_Cut_Option" in Locate_name):
        print("".join(["\t(*) 'Extra_Cut_Option' refers to whether any additional cuts will be applied to the histograms: ", color.BOLD, str(Extra_Cut_Option_In), color.END]))
        Extra_Cut_Option_2 = Extra_Cut_Option_In
    else:
        Extra_Cut_Option_2 = [Extra_Cut_Option_In[0]]


    if("D_Angle_Type" in Locate_name):
        print("".join(["\t(*) 'D_Angle_Type' refers to the type of histogram used for giving an anglular cut for elastic exclusive events: ", color.BOLD, str(D_Angle_Type_In), color.END]))
        D_Angle_Type_2 = D_Angle_Type_In
    else:
        D_Angle_Type_2 = [D_Angle_Type_In[0]]


    if("Dmom" not in Locate_Name_Full_In):
        Get_Dp_Cors = "no"
    else:
        Get_Dp_Cors = Get_Dp_Cors_Master_In

    if(Get_Dp_Cors == "no"):
        print("\n")
        
        
    return [Locate_name, Correction_Name_List_2, Sector_Number_List_2, Binning_Option_List_2, Region_Option_List_2, Particle_Mom_List_2, Particle_Sec_List_2, Extra_Cut_Option_2, D_Angle_Type_2, Get_Dp_Cors]


#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################

                            
def Continue_Loops(In_Name, Cut_Name_In="Not_Defined", Correction_Name_In="Not_Defined", Binning_Option_In="Not_Defined", Region_Option_In="Not_Defined", Searching_Q_In="Not_Defined", Region_Option_List_2_In="Not_Defined", EVENTS=event_type):
    Cut_Name_In = str(Cut_Name_In)
    Continue_Conditions = []
    #################################################################################################
    ####==========#####==========####     Skip Conditions: CUTS     ####==========#####==========####
    #################################################################################################
    if(Cut_Name_In != "Not_Defined"):
        Continue_Conditions.append(("Basic"     in Cut_Name_In and "E"      not in EVENTS))
        Continue_Conditions.append(("Azimuthal" in Cut_Name_In and "D_Angle_V3" in In_Name))
        Continue_Conditions.append(("Polar"     in Cut_Name_In and "D_Angle_V1" in In_Name))
        # Continue_Conditions.append(("HWC_Histo_All" in In_Name and ("Calculated Exclusivity" in In_Name or "Invariant" in In_Name or EVENTS == "SP")))
        # # Do not print invariant mass histograms with invariant mass cuts
        # Continue_Conditions.append((("Calculated Exclusivity" not in In_Name) and "Dmom_" in In_Name))
        Continue_Conditions.append(("Dmom_" in In_Name and ("" == Cut_Name_In)))
        Continue_Conditions.append(("MM_3D" in In_Name))

    ########################################################################################################
    ####==========#####==========####     Skip Conditions: CORRECTIONS     ####==========#####==========####
    ########################################################################################################
    # if(Correction_Name_In != "Not_Defined"):
    #     Continue_Conditions.append(("Dmom_" in In_Name and "mmF" == Correction_Name_In and EVENTS == "SP"))
    #     # print("Skip Single Pion ∆P plots with incomplete corrections...")
        
        
        
    ###########################################################################################################
    ####==========#####==========####     Skip Conditions: BINNING/REGION     ####==========#####==========####
    ###########################################################################################################
    if(Region_Option_In != "Not_Defined"):
        Continue_Conditions.append((((Region_Option_In == 'regall' and Binning_Option_In != 1) and (Region_Option_In != "" and Binning_Option_In != "")) and not Searching_Q_In))
        Continue_Conditions.append((((Region_Option_In != 'regall' and Binning_Option_In == 1) and (Region_Option_In != "" and Binning_Option_In != "")) and not Searching_Q_In))
        
        if("P0" not in EVENTS):
            Continue_Conditions.append(("hmmCPARTall" in In_Name and Region_Option_In == 'regall' and "reg1" in Region_Option_List_2_In))
        else:
            Continue_Conditions.append(("P0" in EVENTS and Region_Option_In != 'regall'))
            
    return Continue_Conditions
