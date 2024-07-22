import ROOT
import array
import traceback

from Fitting_Mom_Cor_Functions import *


#########################################################################################################################
#####==========#####==========#############################################################==========#####==========#####
#####==========#####==========#####     Routine for Printing Correction Functions     #####==========#####==========#####
#####==========#####==========#############################################################==========#####==========#####
#########################################################################################################################

def fit_quadratic_equation(points):
    # Extract x and y values from the given points
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    # Fit a quadratic equation to the points
    parameters = np.polyfit(x, y, 2)
    return parameters





def Print_Correction_Function(h2D, h2DName, CorrectionNameIn, Sector, Particle, PFname, LineOrQuad, Input="Default", Extra_Fit_Name="Do_not_name_a_fit_with_this_name"):
    
    if(Input != "Extended"):
        if(Particle == "pro"):
            try:
                hist_in_use = h2D[str((h2DName, "both"))]
            except:
                print(color.RED + "\n\n\nFAILED TO GET THE RIGHT ∆P (PROTON) HISTOGRAM...\n\n" + color.END)
                hist_in_use = h2D[h2DName].gr2
        else:
            try:
                hist_in_use = h2D[h2DName].gr2
            except:
                print(color.RED + "\n\n\nERROR IN GETTING THE CORRECT ∆P HISTOGRAM...\n\n" + color.END)
                hist_in_use = h2D
    else:
        hist_in_use = h2D
        

    if(Input != "Extended"):
        # CorrectionName = corNameTitles(CorrectionNameIn)
        CorrectionName = corNameTitles(CorrectionNameIn, Form="Default", EVENT_TYPE="SP", BENDING_TYPE=Selection_of_In_or_Out)
    else:
        CorrectionName = CorrectionNameIn
        
        
    outputListforTXT = [""]
    

    PhiFilterName = "".join(["[", str(PFname), "]"]) if(PFname != "") else ""
    
    
    line1_end = "".join(["function predicted for ", color.DELTA, "p_{", str(Particle), "} for [", str(Selection_of_In_or_Out), "][Cor = ", str(CorrectionName), "][All Sectors]" if(Sector == 'all' or Sector == 0) else "".join(["][Sector ", str(Sector), "]"]), str(PhiFilterName), " is:"])

    GetFunction_name = "pol1"
    
    if(LineOrQuad in ['linear', 'both']):
        
        GetFunction_name = "pol1" if(Extra_Fit_Name == "Do_not_name_a_fit_with_this_name") else Extra_Fit_Name

        line1 = "".join(["\n\n// The LINEAR ", str(line1_end)])
        
        outputListforTXT.append(line1)
        print("".join(["\n", line1]))

        parA = round(hist_in_use.GetFunction(GetFunction_name).GetParameter(1), 8)
        if(abs(parA) < 0.01):
            parA = "{:.4e}".format(parA)
        else:
            parA = round(parA, 5)
            
        parB = round(hist_in_use.GetFunction(GetFunction_name).GetParameter(0), 8)
        if(abs(parB) < 0.01):
            parB = "{:.4e}".format(parB)
        else:
            parB = round(parB, 5)
        
        correction = "".join(["((", str(parA), ")*pp + (", str(parB), "));"])
        
        
        line2 = "".join(["dp = ", correction])

        if(Particle == "el"):
            line2 = "".join(["dp = ", "dp + " if('mm0'  not in CorrectionNameIn) else                                       "", correction])        
        if(Particle == "pip"):
            line2 = "".join(["dp = ", "dp + " if(('Pip'     in CorrectionNameIn) and  ('MM0' not in CorrectionNameIn)) else "", correction])
        if(Particle == "pro"):
            line2 = "".join(["dp = ", "dp + " if('Pro'      in CorrectionNameIn) else                                       "", correction])
        
        outputListforTXT.append(line2)
        print(line2)
        
    
    if(LineOrQuad in ['quadratic', 'both']):

        GetFunction_name = "pol2" if(Extra_Fit_Name == "Do_not_name_a_fit_with_this_name") else Extra_Fit_Name
        
        line1 = "".join(["\n\n// The QUADRATIC ", str(line1_end)])
        
        outputListforTXT.append(line1)
        print("".join(["\n", line1]))
        
        parA = round(hist_in_use.GetFunction(GetFunction_name).GetParameter(2), 8)
        if(abs(parA) < 0.01):
            parA = "{:.4e}".format(parA)
        else:
            parA = round(parA, 5)
            
        parB = round(hist_in_use.GetFunction(GetFunction_name).GetParameter(1), 8)
        if(abs(parB) < 0.01):
            parB = "{:.4e}".format(parB)
        else:
            parB = round(parB, 5)
            
        parC = round(hist_in_use.GetFunction(GetFunction_name).GetParameter(0), 8)
        if(abs(parC) < 0.01):
            parC = "{:.4e}".format(parC)
        else:
            parC = round(parC, 5)
        
        
        correction = "".join(["((", str(parA), ")*pp*pp + (", str(parB), ")*pp + (", str(parC), "));"])
        
        
        line2 = "".join(["dp = ", correction])
        
        if(Particle == "el"):
            # line2 = "".join(["dp = ", "dp + " if('mm0' not in CorrectionNameIn) else "", correction])
            line2 = "".join(["dp = ", "dp + " if('mm0'  not in CorrectionNameIn) else                                       "", correction])
        if(Particle == "pip"):
            # line2 = "".join(["dp = ", "dp + " if('Pip'     in CorrectionNameIn) else "", correction])
            line2 = "".join(["dp = ", "dp + " if(('Pip'     in CorrectionNameIn) and  ('MM0' not in CorrectionNameIn)) else "", correction])
        if(Particle == "pro"):
            # line2 = "".join(["dp = ", "dp + " if('Pro'     in CorrectionNameIn) else "", correction])
            line2 = "".join(["dp = ", "dp + " if('Pro'      in CorrectionNameIn) else                                       "", correction])
        
        line2 = "".join(["dp = ",     "dp + " if('Pro'     in CorrectionNameIn) else "", correction])
        
        outputListforTXT.append(line2)
        print(line2)
               
    return outputListforTXT












    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    












    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#####################################################################################################################
#####==========#####==========#########################################################==========#####==========#####
#####==========#####==========#####     Function for Printing PHI Corrections     #####==========#####==========#####
#####==========#####==========#########################################################==========#####==========#####
#####################################################################################################################

def PhiCor_Function(canvas_name, HistoBinC, HistoBinN, HistoBinP, Sector, Particle="el", LineOrQuad_Phi="pol2", LineOrQuad="pol2", cCor_Phi={}, gCor_Par={}, Extra_Fit_Name="Do_not_name_a_fit_with_this_name", Correction="mm0"):
    # HistoBinC -> Histogram for the Central Phi Bin
    # HistoBinN -> Histogram for the Negative/Lower Phi Bin
    # HistoBinP -> Histogram for the Positive/Upper Phi Bin
    
    # SecName = "".join([(((str(Particle).replace("el", "El")).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}")).replace("pim", "#pi^{+}"), " Sector ", str(Sector)])
    list_of_pars = []
    if(LineOrQuad == 'pol2'):
        list_of_pars.append("par2")
    list_of_pars.append("par1")
    list_of_pars.append("par0")

    points_test = {}
###########################################################################
##==========##==========##    Making Canvases    ##==========##==========##
###########################################################################
    name_1 = "".join(["(", "_".join([str(canvas_name), str(LineOrQuad), str(LineOrQuad_Phi)]), ")"])
    
    First_Line_Print = "".join(["\t// The CONTINUOUS ", "QUADRATIC" if(LineOrQuad_Phi == "pol2") else "LINEAR", " function predicted for ∆p_{", (((str(Particle).replace("el", "El")).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}")).replace("pim", "#pi^{+}"), "} for [Cor = ", str(Correction) if(("mm0" not in canvas_name) or ("mm0_EL" in canvas_name)) else "No Correction", "][Sector ", str(Sector), "] is:"])
    
    Correction_Line_Full     = "\tdp = " if(("mm0" in Correction) or ("Uncorrected" in Correction) or ("mm0" in canvas_name)) else "\tdp = dp + "
    if((Particle in ["pip"]) and ('MM0'  in Correction)):
        Correction_Line_Full = "\tdp = "
                    
    for par in list_of_pars:
        
        name_2 = "_".join([name_1, str(par)])
        try:
            cCor_Phi[name_2]
        except:
            # print("".join([color.BOLD, str(name_2), color.END, " Was not made before..."]))
            cCor_Phi[name_2] = Canvas_Create(name_2, Num_Columns=3, Num_Rows=2, Size_X=1200, Size_Y=1100)
        
        # cCor_Phi[name_2].Draw()
        
        try:
            gCor_Par["_".join([name_2, str(Sector)])]
        except:
            gCor_Par["_".join([name_2, str(Sector)])] = ROOT.TGraphErrors()
            gCor_Par["_".join([name_2, str(Sector)])].SetMarkerStyle(20)

    ###########################################################################
    ##==========##==========## Correction Parameters ##==========##==========##
    ###########################################################################
        try:
            NLower_momY_Par       = round(HistoBinN.GetFunction(LineOrQuad if(Extra_Fit_Name == "Do_not_name_a_fit_with_this_name") else Extra_Fit_Name).GetParameter(0 if("0" in par) else 1 if("1" in par) else 2 if("2" in par) else 0), 8)
            NLower_momY_Par_Error = round(HistoBinN.GetFunction(LineOrQuad if(Extra_Fit_Name == "Do_not_name_a_fit_with_this_name") else Extra_Fit_Name).GetParError(0  if("0" in par) else 1 if("1" in par) else 2 if("2" in par) else 0), 8)

            Center_momY_Par       = round(HistoBinC.GetFunction(LineOrQuad if(Extra_Fit_Name == "Do_not_name_a_fit_with_this_name") else Extra_Fit_Name).GetParameter(0 if("0" in par) else 1 if("1" in par) else 2 if("2" in par) else 0), 8)
            Center_momY_Par_Error = round(HistoBinC.GetFunction(LineOrQuad if(Extra_Fit_Name == "Do_not_name_a_fit_with_this_name") else Extra_Fit_Name).GetParError(0  if("0" in par) else 1 if("1" in par) else 2 if("2" in par) else 0), 8)

            PUpper_momY_Par       = round(HistoBinP.GetFunction(LineOrQuad if(Extra_Fit_Name == "Do_not_name_a_fit_with_this_name") else Extra_Fit_Name).GetParameter(0 if("0" in par) else 1 if("1" in par) else 2 if("2" in par) else 0), 8)
            PUpper_momY_Par_Error = round(HistoBinP.GetFunction(LineOrQuad if(Extra_Fit_Name == "Do_not_name_a_fit_with_this_name") else Extra_Fit_Name).GetParError(0  if("0" in par) else 1 if("1" in par) else 2 if("2" in par) else 0), 8)


            points_test[par] = [(-12 if("el" in Particle) else -18, NLower_momY_Par), (0, Center_momY_Par), (12 if("el" in Particle) else 18, PUpper_momY_Par)]

        ###########################################################################
        ##==========##==========##  Setting Plot Points  ##==========##==========##
        ###########################################################################
            gCor_Par["_".join([name_2, str(Sector)])].SetPoint(gCor_Par["_".join([name_2, str(Sector)])].GetN(),          -12 if("el" in Particle) else -18, NLower_momY_Par)
            gCor_Par["_".join([name_2, str(Sector)])].SetPointError(gCor_Par["_".join([name_2, str(Sector)])].GetN() - 1, 2.5 if("el" in Particle) else   5, NLower_momY_Par_Error)

            gCor_Par["_".join([name_2, str(Sector)])].SetPoint(gCor_Par["_".join([name_2, str(Sector)])].GetN(),                                          0, Center_momY_Par)
            gCor_Par["_".join([name_2, str(Sector)])].SetPointError(gCor_Par["_".join([name_2, str(Sector)])].GetN() - 1, 2.5 if("el" in Particle) else   5, Center_momY_Par_Error)

            gCor_Par["_".join([name_2, str(Sector)])].SetPoint(gCor_Par["_".join([name_2, str(Sector)])].GetN(),           12 if("el" in Particle) else  18, PUpper_momY_Par)
            gCor_Par["_".join([name_2, str(Sector)])].SetPointError(gCor_Par["_".join([name_2, str(Sector)])].GetN() - 1, 2.5 if("el" in Particle) else   5, PUpper_momY_Par_Error)
        ###########################################################################
        ##==========##==========##  Setting Plot Points  ##==========##==========##
        ###########################################################################



        ###########################################################################
        ##==========##==========##  Setting Plot Titles  ##==========##==========##
        ###########################################################################
            Parameter = "UNKNOWN - ERROR"
            if("par2" not in list_of_pars):
                Parameter = "B" if("0" in par) else "A" if("1" in par) else "UNKNOWN - ERROR"
                # Parameter = "".join([Parameter, " (From: A*p + B)"])
                Parameter = "".join([Parameter, " (From: Linear Eq.)"])
            else:
                Parameter = "C" if("0" in par) else "B" if("1" in par) else "A" if("2" in par) else "UNKNOWN - ERROR"
                # Parameter = "".join([Parameter, " (From: A*p^{2} + B*p + C)"])
                Parameter = "".join([Parameter, " (From: Quad. Eq.)"])
                
                
            Title_New = "".join(["#splitline{", HistoBinC.GetTitle(), "}{Momentum Correction Parameter: ", root_color.Bold, "{", str(Parameter), "}}; #phi_{", (((str(Particle).replace("el", "El")).replace("pip", "#pi^{+}")).replace("pi0", "#pi^{0}")).replace("pim", "#pi^{+}"), "} [#circ]"])
            Title_New = Title_New.replace("El:  (-5 < #phi_{El} < 5)", "Continuous #phi_{El} Correction")
            Title_New = Title_New.replace("#phi_{El} Bin:  (-5 < #phi_{El} < 5)", "Continuous #phi_{El} Correction")
            Title_New = Title_New.replace("#phi_{#pi^{+} } Bin:  (-10 < #phi_{#pi^{+}} < 10)", "Continuous #phi_{#pi^{+}} Correction")
            # print(Title_New)
            gCor_Par["_".join([name_2, str(Sector)])].SetTitle(Title_New)
            
            # print(gCor_Par["_".join([name_2, str(Sector)])].GetTitle())
        ###########################################################################
        ##==========##==========##  Setting Plot Titles  ##==========##==========##
        ###########################################################################



        ###########################################################################
        ##==========##==========##     Drawing Plots     ##==========##==========##
        ###########################################################################
            ############ Opening Canvas ############
            Draw_Canvas(cCor_Phi[name_2], cd_num=Sector if(Sector != 0 and type(Sector) is not str) else 1, left_add=0.05, right_add=-0.025, up_add=0, down_add=0)
            # print("".join(["\nDraw_Canvas(cCor_Phi[", str(name_2), "], cd_num=", str(Sector) if(Sector != 0 and type(Sector) is not str) else "1", ", left_add=0, right_add=0, up_add=0, down_add=0)"]))

            ############ Drawing Histogram ############
            gCor_Par["_".join([name_2, str(Sector)])].Draw("AP")
            # print("".join(["\ngCor_Par[", "_".join([name_2, str(Sector)]), '].Draw("AP")']))

            gCor_Par["_".join([name_2, str(Sector)])].GetXaxis().SetRangeUser(-18 if(Particle == "el") else -28, 18 if(Particle == "el") else 28)
            gCor_Par["_".join([name_2, str(Sector)])].GetYaxis().SetRangeUser(-0.01 if("par2" == par) else -0.1 if("par1" == par) else -0.15, 0.01 if("par2" == par) else 0.1 if("par1" == par) else 0.15)

            if((("Inbending" in str(canvas_name)) and ("el" in canvas_name))):
                # y_range_max = (0.001 if(str(Sector) not in ["1", "4"]) else 0.0005) 
                y_range_max = 0.003 if("par2" == par) else 0.1 if("par1" == par) else 0.15
                # y_range_min = (0.001 if(str(Sector) not in ["1", "4"]) else 0.0015) 
                y_range_min = 0.003 if("par2" == par) else 0.1 if("par1" == par) else 0.15
                gCor_Par["_".join([name_2, str(Sector)])].GetYaxis().SetRangeUser(-y_range_min, y_range_max)
            
            if((("Outbending" in str(canvas_name)) and ("pip" in canvas_name))):
                gCor_Par["_".join([name_2, str(Sector)])].GetYaxis().SetRangeUser(-0.004 if("par2" == par) else -0.04 if("par1" == par) else -0.045, 0.004 if("par2" == par) else 0.04 if("par1" == par) else 0.045)
        ###########################################################################
        ##==========##==========##     Drawing Plots     ##==========##==========##
        ###########################################################################


##=====>############################################################################
##=====>##==========##==========##   New Phi Correction   ##==========##==========##
##=====>############################################################################
            if(LineOrQuad_Phi == "pol2"):
                Phi_Fit_Equation = "[p2]*x*x + [p1]*x + [p0]"
            else:
                Phi_Fit_Equation = "[p1]*x + [p0]"

            Phi_Fit_Function = ROOT.TF1(Phi_Fit_Equation, Phi_Fit_Equation, -15 if(Particle == "el") else -25, 15 if(Particle == "el") else 25)
            
            # if("par2" == par and LineOrQuad_Phi == "pol2"):
            if(LineOrQuad_Phi == "pol2"):
                
                Phi_Fit_Function.SetParLimits(1, -0.05, 0.05)
                
                if((("Outbending" in str(canvas_name)) and ("mm0" in canvas_name)) and (((str(Sector) in ["1"]) and ("2" in par)) or ((str(Sector) in ["5"]) and ("0" in par)))):
                    Phi_Fit_Function.SetParLimits(1, -0.075, 0.075)
                    
                    Phi_Fit_Function.SetParameter(2, 0.00016135165 if(str(Sector) in ["5"]) else 0.00000504105)
                    Phi_Fit_Function.SetParLimits(2, 0.000,  0.05)
                    
                if((("Outbending" in str(canvas_name)) and ("'mmEF'" in canvas_name) and ("pip" in canvas_name)) and (((str(Sector) in ["2", "5", "6"]) and ("2" in par)))):
                    # print("\n\nTESTING\n\n")
                    Phi_Fit_Function.SetParLimits(1, -0.075, 0.075)
                    
                    Phi_Fit_Function.SetParameter(2, 0.00000504105)
                    Phi_Fit_Function.SetParLimits(2, -0.05,   0.05)
                    
                    # print("Unique Correction conditions for ", canvas_name, "(Sector", Sector, " - Parameter", par, " - ", Parameter, ")")
                    # print("Fitting:\nNLower_momY_Par =", NLower_momY_Par, "+/-", NLower_momY_Par_Error, "\nCenter_momY_Par =", Center_momY_Par, "+/-", Center_momY_Par_Error, "\nPUpper_momY_Par =", PUpper_momY_Par, "+/-", PUpper_momY_Par_Error, "\n\n")

                if((("Outbending" in str(canvas_name)) and ("'mmEF'" in canvas_name) and ("pip" in canvas_name)) and (((str(Sector) in ["6"]) and ("0" in par)))):
                    # print("\n\nTESTING\n\n")
                    Phi_Fit_Function.SetParLimits(1, -0.075, 0.075)
                    
                    Phi_Fit_Function.SetParameter(2, 0.00000504105)
                    Phi_Fit_Function.SetParLimits(2, -0.05,   0.05)
                    
                if((("Outbending" in str(canvas_name)) and ("'mmEF_" in canvas_name) and ("el" in canvas_name)) and (((str(Sector) in ["4"]) and (True)))):
                    Phi_Fit_Function.SetParLimits(0, 0.5*fit_quadratic_equation(points_test[par])[2], 1.5*fit_quadratic_equation(points_test[par])[2])
                    Phi_Fit_Function.SetParameter(0, fit_quadratic_equation(points_test[par])[2])
                    Phi_Fit_Function.SetParLimits(1, 0.5*fit_quadratic_equation(points_test[par])[1], 1.5*fit_quadratic_equation(points_test[par])[1])
                    Phi_Fit_Function.SetParameter(1, fit_quadratic_equation(points_test[par])[1])
                    Phi_Fit_Function.SetParLimits(2, 0.5*fit_quadratic_equation(points_test[par])[0], 1.5*fit_quadratic_equation(points_test[par])[0])
                    Phi_Fit_Function.SetParameter(2, fit_quadratic_equation(points_test[par])[0])
                    
                    
                if("Outbending" in str(canvas_name)):
                    Phi_Fit_Function.SetParLimits(0, 0.5*fit_quadratic_equation(points_test[par])[2], 1.5*fit_quadratic_equation(points_test[par])[2])
                    Phi_Fit_Function.SetParameter(0, fit_quadratic_equation(points_test[par])[2])
                    Phi_Fit_Function.SetParLimits(1, 0.5*fit_quadratic_equation(points_test[par])[1], 1.5*fit_quadratic_equation(points_test[par])[1])
                    Phi_Fit_Function.SetParameter(1, fit_quadratic_equation(points_test[par])[1])
                    Phi_Fit_Function.SetParLimits(2, 0.5*fit_quadratic_equation(points_test[par])[0], 1.5*fit_quadratic_equation(points_test[par])[0])
                    Phi_Fit_Function.SetParameter(2, fit_quadratic_equation(points_test[par])[0])
                    
                    
                    
#                 if(("Inbending" in str(canvas_name)) and ("mm0" in canvas_name) and ("el" in canvas_name)):
#                     if(LineOrQuad_Phi == "pol2"):
#                         if(str(Sector) in ["1"]):
#                             Phi_Fit_Function.SetParameter(2, -4.3303e-06)
#                             Phi_Fit_Function.SetParLimits(2, -4.33031e-06, -4.33029e-06)
#                             Phi_Fit_Function.SetParameter(1,  1.1006e-04)
#                             Phi_Fit_Function.SetParLimits(1,  1.10059e-04,  1.10061e-04)
#                             Phi_Fit_Function.SetParameter(0, -5.7235e-04)
#                             Phi_Fit_Function.SetParLimits(0, -5.72351e-04, -5.72349e-04)
#                         if(str(Sector) in ["2"]):
#                             Phi_Fit_Function.SetParameter(2, -9.8045e-07)
#                             Phi_Fit_Function.SetParLimits(2, -9.80451e-07, -9.80449e-07)
#                             Phi_Fit_Function.SetParameter(1,  6.7395e-05)
#                             Phi_Fit_Function.SetParLimits(1,  6.73949e-05,  6.73951e-05)
#                             Phi_Fit_Function.SetParameter(0, -4.6757e-05)
#                             Phi_Fit_Function.SetParLimits(0, -4.67571e-05, -4.67569e-05)
#                         if(str(Sector) in ["3"]):
#                             Phi_Fit_Function.SetParameter(2, -5.9459e-07)
#                             Phi_Fit_Function.SetParLimits(2, -5.94591e-07, -5.94589e-07)
#                             Phi_Fit_Function.SetParameter(1, -2.8289e-05)
#                             Phi_Fit_Function.SetParLimits(1, -2.82891e-05, -2.82889e-05)
#                             Phi_Fit_Function.SetParameter(0, -4.3541e-04)
#                             Phi_Fit_Function.SetParLimits(0, -4.35411e-04, -4.35409e-04)
#                         if(str(Sector) in ["4"]):
#                             Phi_Fit_Function.SetParameter(2, -2.2714e-06)
#                             Phi_Fit_Function.SetParLimits(2, -2.27141e-06, -2.27139e-06)
#                             Phi_Fit_Function.SetParameter(1, -3.0360e-05)
#                             Phi_Fit_Function.SetParLimits(1, -3.03601e-05, -3.03599e-05)
#                             Phi_Fit_Function.SetParameter(0, -8.9322e-04)
#                             Phi_Fit_Function.SetParLimits(0, -8.93221e-04, -8.93219e-04)
#                         if(str(Sector) in ["5"]):
#                             Phi_Fit_Function.SetParameter(2, -1.1490e-06)
#                             Phi_Fit_Function.SetParLimits(2, -1.14901e-06, -1.14899e-06)
#                             Phi_Fit_Function.SetParameter(1, -6.2147e-06)
#                             Phi_Fit_Function.SetParLimits(1, -6.21471e-06, -6.21469e-06)
#                             Phi_Fit_Function.SetParameter(0, -4.7235e-04)
#                             Phi_Fit_Function.SetParLimits(0, -4.72351e-04, -4.72349e-04)
#                         if(str(Sector) in ["6"]):
#                             Phi_Fit_Function.SetParameter(2,  1.1076e-06)
#                             Phi_Fit_Function.SetParLimits(2,  1.10759e-06,  1.10761e-06)
#                             Phi_Fit_Function.SetParameter(1,  4.0156e-05)
#                             Phi_Fit_Function.SetParLimits(1,  4.01559e-05,  4.01561e-05)
#                             Phi_Fit_Function.SetParameter(0, -1.6341e-04)
#                             Phi_Fit_Function.SetParLimits(0, -1.63411e-04, -1.63409e-04)
                        
#                 # For Fall 2018 Pass 1
#                 if(("Inbending" in str(canvas_name)) and ("mm0" in canvas_name) and ("el" in canvas_name)):
#                     if("0" in par):
#                         if(str(Sector) in ["3"]):
#                             Phi_Fit_Function.SetParameter(2,  7.3348e-05)
# #                             Phi_Fit_Function.SetParLimits(2,  7.33481e-05,  7.33479e-05)
#                             Phi_Fit_Function.SetParameter(1, -0.001102)
# #                             Phi_Fit_Function.SetParLimits(1, -0.0011021,   -0.0011019)
#                             Phi_Fit_Function.SetParameter(0,  0.057052)
# #                             Phi_Fit_Function.SetParLimits(0,  0.0570521,    0.0570519)





                # # For Spring 2019 Pass 2 Correcions
                # if(("Inbending" in str(canvas_name)) and ("mmRP2" in canvas_name) and ("pip" in canvas_name)):
                #     if("2" in par):
                #         if(str(Sector) in ["2"]):
                #             Phi_Fit_Function.SetParameter(2,  2.865e-06)
                #             Phi_Fit_Function.SetParLimits(2,  2.865e-07, 2.865e-05)
                #             # Phi_Fit_Function.SetParameter(1, ###)
                #             # Phi_Fit_Function.SetParLimits(1, ###,   ###)
                #             Phi_Fit_Function.SetParameter(0,  9.21e-04)
                #             Phi_Fit_Function.SetParLimits(0,  0,         9.21e-02)
                #             # print(str(gCor_Par["_".join([name_2, str(Sector)])].GetTitle()))
                #             gCor_Par["_".join([name_2, str(Sector)])].SetTitle("".join(["#splitline{", str(gCor_Par["_".join([name_2, str(Sector)])].GetTitle()), "}{MODIFIED FIT}"]))
                
                
                
                # For Fall 2018 Pass 2 Corrections
                if("Fall2018_Pass2_Forward" in str(canvas_name)):
                    # print(f"canvas_name = {canvas_name}")
                    # Define your points
                    x1, y1 = -12 if("el" in Particle) else -18, NLower_momY_Par
                    x2, y2 =                                 0, Center_momY_Par
                    x3, y3 =  12 if("el" in Particle) else  18, PUpper_momY_Par

                    # Create the matrices
                    A = np.array([[x1**2, x1, 1], [x2**2, x2, 1], [x3**2, x3, 1]])
                    B = np.array([y1, y2, y3])

                    # Solve for the coefficients
                    coefficients = np.linalg.solve(A, B)
                    # print("A (quadratic coefficient):", coefficients[0])
                    # print("B (linear coefficient):",    coefficients[1])
                    # print("C (constant term):",         coefficients[2])
                    
                    Phi_Fit_Function.SetParameter(2,  coefficients[0])
                    Phi_Fit_Function.SetParLimits(2,  0.2*coefficients[0], 1.8*coefficients[0])
                    Phi_Fit_Function.SetParameter(1,  coefficients[1])
                    Phi_Fit_Function.SetParLimits(1,  0.2*coefficients[1], 1.8*coefficients[1])
                    Phi_Fit_Function.SetParameter(0,  coefficients[2])
                    Phi_Fit_Function.SetParLimits(0,  0.2*coefficients[2], 1.8*coefficients[2])

                    

            gCor_Par["_".join([name_2, str(Sector)])].Fit(Phi_Fit_Function)

            cCor_Phi[name_2].Update()
            
            statbox_move(gCor_Par["_".join([name_2, str(Sector)])], cCor_Phi[name_2], Default_Stat_Obj={}, Sector=Sector, Print_Method="norm", Y1_add=0.075, Y2_add=0.075, X1_add=0, X2_add=0)

            if(LineOrQuad_Phi == "pol2"):
                parA = gCor_Par["_".join([name_2, str(Sector)])].GetFunction(Phi_Fit_Equation).GetParameter(2)
                parA = print_rounded_str(parA, rounding=5)
            parB = gCor_Par[    "_".join([name_2, str(Sector)])].GetFunction(Phi_Fit_Equation).GetParameter(1)
            parB = print_rounded_str(parB, rounding=5)
            parC = gCor_Par[    "_".join([name_2, str(Sector)])].GetFunction(Phi_Fit_Equation).GetParameter(0)
            parC = print_rounded_str(parC, rounding=5)

            if(LineOrQuad_Phi == "pol2"):
                correction = "".join(["(", str(parA), ")*phi*phi + (", str(parB), ")*phi + (", str(parC), ")"])
            else:
                correction = "".join(["(", str(parB), ")*phi + (", str(parC), ")"])

            Correction_Line_Full = "".join([Correction_Line_Full, "(", str(correction), ")", "*pp*pp + " if("par2" == par) else "*pp + " if("par1" == par) else ";"])

            
        except Exception as e:
            print("".join([color.Error,  "\nERROR in Phi Corrections: \n", str(e), "\n", color.END]))
            return "".join([color.Error, "\nERROR in Phi Corrections: \n", str(e), "\n", color.END])
    ###########################################################################
    ##==========##==========## Correction Parameters ##==========##==========##
    ###########################################################################

    print("\n".join([First_Line_Print, Correction_Line_Full]))
    
    return [cCor_Phi, gCor_Par]












    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    












    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

#############################################################################################################################
#####==========#####==========#################################################################==========#####==========#####
#####==========#####==========#####     Functions to Help with Getting Exclusive Cuts     #####==========#####==========#####
#####==========#####==========#################################################################==========#####==========#####
#############################################################################################################################

def Print_Cut_Func(Histogram_Up, Histogram_Down, Sector):
    par_UP_1 = round(Histogram_Up.GetFunction("Upper_Cut_Func").GetParameter(1), 6)
    par_UP_0 = round(Histogram_Up.GetFunction("Upper_Cut_Func").GetParameter(0), 6)
    par_DOWN_1 = round(Histogram_Down.GetFunction("Lower_Cut_Func").GetParameter(1), 6)
    par_DOWN_0 = round(Histogram_Down.GetFunction("Lower_Cut_Func").GetParameter(0), 6)
    print("".join(["\n\t\tif(esec == ", str(Sector), "){\n\n\t\t\t// Upper Cut\n\t\t\tcut_up = (", str(par_UP_1), ")*el + (", str(par_UP_0), ");\n\n\t\t\t// Lower Cut\n\t\t\tcut_down = (", str(par_DOWN_1), ")*el + (", str(par_DOWN_0), ");\n\n\t\t}"]))
    
    
    
def Print_WM_Cut_Func(Histogram_Up, Histogram_Down, Sector):
    par_UP_1 = round(Histogram_Up.GetFunction("Upper_Cut_Func").GetParameter(1), 6)
    par_UP_0 = round(Histogram_Up.GetFunction("Upper_Cut_Func").GetParameter(0), 6)
    par_DOWN_1 = round(Histogram_Down.GetFunction("Lower_Cut_Func").GetParameter(1), 6)
    par_DOWN_0 = round(Histogram_Down.GetFunction("Lower_Cut_Func").GetParameter(0), 6)
    print("".join(["\n\t\tif(prosec == ", str(Sector), "){\n\n\t\t\t// Upper Cut\n\t\t\tcut_up = (", str(par_UP_1), ")*pro + (", str(par_UP_0), ");\n\n\t\t\t// Lower Cut\n\t\t\tcut_down = (", str(par_DOWN_1), ")*pro + (", str(par_DOWN_0), ");\n\n\t\t}"]))
    
    
    
def Print_Cut_Func_Phi(Histogram_Up, Histogram_Down, Phi_Bin):
    par_UP_1 = round(Histogram_Up.GetFunction("Upper_Cut_Func").GetParameter(1), 6)
    par_UP_0 = round(Histogram_Up.GetFunction("Upper_Cut_Func").GetParameter(0), 6)
    par_DOWN_1 = round(Histogram_Down.GetFunction("Lower_Cut_Func").GetParameter(1), 6)
    par_DOWN_0 = round(Histogram_Down.GetFunction("Lower_Cut_Func").GetParameter(0), 6)
    binName = "localelPhiS"
    PhiFilter = "localelPhiS > -100000" # Integrated phi (this statement will always be true by the definitions of phi)
    if(Phi_Bin == 'reg1'):
        PhiFilter = "".join([binName, ' > -5 && ', binName, ' < 5'])
    if(Phi_Bin == 'reg2'):
        PhiFilter = "".join([binName, ' < -5'])
    if(Phi_Bin == 'reg3'):
        PhiFilter = "".join([binName, ' > 5'])
    output = "".join(["\n\t\t\tif(", str(PhiFilter), "){\n\n\t\t\t\t// Upper Cut\n\t\t\t\tcut_up = (", str(par_UP_1), ")*el + (", str(par_UP_0), ");\n\n\t\t\t\t// Lower Cut\n\t\t\t\tcut_down = (", str(par_DOWN_1), ")*el + (", str(par_DOWN_0), ");\n\n\t\t\t}"])
    return output






################################################################################################################################################################################################################################################################################################################
### New Cell ###################################################################################################################################################################################################################################################################################################
################################################################################################################################################################################################################################################################################################################






def Print_Cut_Func(Histogram_Up, Histogram_Down, Particle, Sector):
    par_UP_1 = round(Histogram_Up.GetFunction("Upper_Cut_Func").GetParameter(1), 6)
    par_UP_0 = round(Histogram_Up.GetFunction("Upper_Cut_Func").GetParameter(0), 6)
    par_DOWN_1 = round(Histogram_Down.GetFunction("Lower_Cut_Func").GetParameter(1), 6)
    par_DOWN_0 = round(Histogram_Down.GetFunction("Lower_Cut_Func").GetParameter(0), 6)
    if(Particle == "el"):
        print("".join(["\n\t\tif(esec == ", str(Sector), "){\n\t\t\t// Upper Cut\n\t\t\tcut_up = (", str(par_UP_1), ")*el + (", str(par_UP_0), ");\n\t\t\t// Lower Cut\n\t\t\tcut_down = (", str(par_DOWN_1), ")*el + (", str(par_DOWN_0), ");\n\t\t}"]))
    if(Particle == "pro"):
        print("".join(["\n\t\tif(prosec == ", str(Sector), "){\n\t\t\t// Upper Cut\n\t\t\tcut_up = (", str(par_UP_1), ")*pro + (", str(par_UP_0), ");\n\t\t\t// Lower Cut\n\t\t\tcut_down = (", str(par_DOWN_1), ")*pro + (", str(par_DOWN_0), ");\n\t\t}"]))
        
        
        
def Print_Cut_Func_Phi(Histogram_Up, Histogram_Down, Phi_Bin):
    par_UP_1 = round(Histogram_Up.GetFunction("Upper_Cut_Func").GetParameter(1), 6)
    par_UP_0 = round(Histogram_Up.GetFunction("Upper_Cut_Func").GetParameter(0), 6)
    par_DOWN_1 = round(Histogram_Down.GetFunction("Lower_Cut_Func").GetParameter(1), 6)
    par_DOWN_0 = round(Histogram_Down.GetFunction("Lower_Cut_Func").GetParameter(0), 6)
    binName = "localelPhiS"
    PhiFilter = "localelPhiS > -100000" # Integrated phi (this statement will always be true by the definitions of phi)
    if(Phi_Bin == 'reg1'):
        PhiFilter = "".join([binName, ' > -5 && ', binName, ' < 5'])
    if(Phi_Bin == 'reg2'):
        PhiFilter = "".join([binName, ' < -5'])
    if(Phi_Bin == 'reg3'):
        PhiFilter = "".join([binName, ' > 5'])
    output = "".join(["\n\t\t\tif(", str(PhiFilter), "){\n\n\t\t\t\t// Upper Cut\n\t\t\t\tcut_up = (", str(par_UP_1), ")*el + (", str(par_UP_0), ");\n\n\t\t\t\t// Lower Cut\n\t\t\t\tcut_down = (", str(par_DOWN_1), ")*el + (", str(par_DOWN_0), ");\n\n\t\t\t}"])
    return output
    
    
    
def Print_Cut_By_Points(Histogram, Sector, Particle, Type, Current_Cut=""):
    List_of_Widths = Histogram
    try:
        List_of_Widths = Histogram.Sigma_Widths
    except Exception as e1:
        try:
            if(Histogram is list):
                List_of_Widths = Histogram
            else:
                print("".join([color.BOLD, color.RED, "ERROR: ", color.END, str(e1)]))
        except Exception as e2:
            print("".join([color.BOLD, color.RED, "ERROR IN INPUT: ", color.END, str(e2)]))
    Particle_Sector = "esec" if(Particle == "el") else "pipsec" if(Particle == "pip") else "prosec" if(Particle == "pro") else "pimsec" if(Particle == "pim") else "esec"
    Particle_Vector = "eleC" if(Particle == "el") else "".join([Particle, "C"])
    if(Current_Cut == ""):
        Cut_Code = """
    auto Beam_Energy = 10.6041;
    auto Proton_Mass = 0.938;
    auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
    auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, Proton_Mass);
    auto eleC = ROOT::Math::PxPyPzMVector(ex, ey, ez, 0);
    """
        if("pro" in Particle or "Theta" in Type):
            Cut_Code = "".join([Cut_Code, "auto proC = ROOT::Math::PxPyPzMVector(prox, proy, proz, Proton_Mass);"])
        if("pip" in Particle or "MM" in Type):
            Cut_Code = "".join([Cut_Code, "auto pipC = ROOT::Math::PxPyPzMVector(pipx, pipy, pipz, 0.13957);"])
        if("pim" in Particle):
            Cut_Code = "".join([Cut_Code, "auto pimC = ROOT::Math::PxPyPzMVector(pimx, pimy, pimz, 0.13957);"])
        if("MM" in Type):    
            Cut_Code = "".join([Cut_Code, """
    auto Cut_Variable = (beam + targ - eleC - pipC).M();
    double Cut_Upper = 1.1;
    double Cut_Lower = 0;
    """])
        if("WM" in Type):    
            Cut_Code = "".join([Cut_Code, """
    auto Cut_Variable = (beam + targ - eleC).M();
    double Cut_Upper = 1.3;
    double Cut_Lower = 0.7;
    """])
        if("Phi" in Type):
            Cut_Code = "".join([Cut_Code, """
    auto el_Phi = (180/3.1415926)*atan2(ey, ex);
    auto pro_Phi = (180/3.1415926)*atan2(proy, prox);
    if(el_Phi < 0){el_Phi += 360;}
    if(pro_Phi < 0){pro_Phi += 360;}
    double Cut_Upper = 183;
    double Cut_Lower = 177;
    double Cut_Variable = abs(el_Phi - pro_Phi);
    """])
        if("Theta" in Type):
            Cut_Code = "".join([Cut_Code, """
    auto Pro_Th_Calc = atan(Proton_Mass/((Beam_Energy + Proton_Mass)*tan(eleC.Theta()/2)))*(180/3.1415926);
    auto Cut_Variable = ((proC.Theta())*(180/3.1415926)) - Pro_Th_Calc;
    double Cut_Upper = 5;
    double Cut_Lower = -5;
    """])
        Cut_Code = "".join([Cut_Code, """
    if(""", str(Particle_Sector), """ == 1){CUT_SECTOR_1
    }
    if(""", str(Particle_Sector), """ == 2){CUT_SECTOR_2
    }
    if(""", str(Particle_Sector), """ == 3){CUT_SECTOR_3
    }
    if(""", str(Particle_Sector), """ == 4){CUT_SECTOR_4
    }
    if(""", str(Particle_Sector), """ == 5){CUT_SECTOR_5
    }
    if(""", str(Particle_Sector), """ == 6){CUT_SECTOR_6
    }
    return ((Cut_Variable < Cut_Upper) && (Cut_Variable > Cut_Lower));
    
    """])
    else:
        Cut_Code = Current_Cut
    # Cut_Sector = "        "
    Cut_Sector = ""
    try:
        for List_For_Cuts in List_of_Widths:
            min_Mom, max_Mom, cen_Mon = List_For_Cuts[0]
            sigma_upper,  sigma_lower = List_For_Cuts[1]
            Cut_Sector = "".join([Cut_Sector, """
        if(""", Particle_Vector, ".P() > ", str(min_Mom), " && ", Particle_Vector, ".P() < ", str(max_Mom), """){
            Cut_Upper = """, str(print_rounded_str(sigma_upper, 2)), """;
            Cut_Lower = """, str(print_rounded_str(sigma_lower, 2)), """;
        }"""])
    except Exception as e:
        print(f"{color.Error}ERROR: {color.END}{str(e)}")
    Cut_Code = Cut_Code.replace("".join(["CUT_SECTOR_", str(Sector)]), Cut_Sector)
    # print(Cut_Sector)
    return Cut_Code
    
    