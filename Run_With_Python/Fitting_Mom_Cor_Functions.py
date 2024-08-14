import ROOT
import traceback

# from CommonPythonFunctions import *
from File_Search_Script    import *


################################################################################################################
#####==========#####==========####################################################==========#####==========#####
#####==========#####==========#####     Fits for Missing Mass Histograms     #####==========#####==========#####
#####==========#####==========####################################################==========#####==========#####
################################################################################################################

# # Meaning of below: h2 is the 2D histogram to be sliced and fit; minR/maxR is the starting/ending point of the slice range, and dR is the increments of increase between each slice (for p_e, fit range should be minR=2, maxR=8, and dR=1)
# def fit2dall(h2, minR, maxR, dR, Title, BGq, Particle):

#     hx = h2.ProjectionX()
#     hys2, Sigma_Widths = [], []
#     gr2, gr2_Sigma, gr2_Cut_Range_Up, gr2_Cut_Range_Down = ROOT.TGraphErrors(), ROOT.TGraphErrors(), ROOT.TGraphErrors(), ROOT.TGraphErrors()
#     gr2_V2 = ROOT.TGraphAsymmErrors()
#     gr2.SetMarkerStyle(20)
#     gr2_V2.SetMarkerStyle(20)
#     gr2_Sigma.SetMarkerStyle(20)
#     gr2_Cut_Range_Up.SetMarkerStyle(20)
#     gr2_Cut_Range_Down.SetMarkerStyle(20)
    
#     FindPeak_x, FindPeak_y = [], []

#     while minR+dR <= maxR:
        
#         extra_con_pro = False
#         if(Particle == "pro"):
#             extra_con_pro = True
#             if(event_type == "DP" and minR == 2.9):
#                 dR = 0.5
#             if(event_type == "P0" and minR == 1.2):
#                 dR = 0.5
#             if(Particle == "pro"):
#                 if(event_type == "DP" and minR >= 0.85 and dR == 0.05):
#                     dR = 0.1
#                 # if(event_type == "DP" and minR >= 1.1 and dR < 0.25):
#                 #     dR += 0.05
#                 #     dR = round(dR, 3)
#                 if(event_type == "DP" and minR >= 1.25 and dR < 0.25):
#                     dR = 0.25
#                 if(event_type == "P0"):
#                     dR = 0.25
#                 if(event_type == "DP" and minR == 2.9):
#                     dR = 0.5
#                 if(event_type == "P0" and minR == 1.2):
#                     dR = 0.5
                    
#                 if(event_type in ["DP", "P0"]):
#                     dR = 0.25
#                     if(minR >= 2.2):
#                         dR = 0.5
#                         if(minR < 1 and event_type == "DP"):
#                             dR = 0.1

# #                 if(event_type == "P0"):
# #                     dR = 0.1
        
#         ib0, ib1 = hx.FindBin(minR), hx.FindBin(minR+dR)

#         hy2 = h2.ProjectionY(f"hy{ib1}", ib0, ib1)
#         hy2.SetDirectory(0)

#         # if(event_type == "P0"):
#         #     hy2.Rebin(2)
#         #     hy2.Rebin(2)
#         # if(hy2.GetBinContent(hy2.GetMaximumBin()) < 100):
#         #     hy2.Rebin(2)
#         hy2.Rebin(2)
# #         hy2.Rebin(2)
        
#         if(Particle == "pro"):
#             # if(minR < 1):
#             #     hy2.Rebin(2)
#             if(hy2.GetBinContent(hy2.GetMaximumBin()) < 200):
#                 hy2.Rebin(2)
        
#         Slice_Title = "".join(["#splitline{", Title, "}{p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4)), "}"])
#         hy2.SetTitle(Slice_Title)
        
        
#         extra_con_1 = ((Particle == "pip" and ("mmF_PipMMF" in h2.GetName())) and ("Sector 2" in Title and (minR == 3.75 and "reg1" in h2.GetName())))
#         extra_con_2 = ((Particle == "pip" and ("mmF_PipMMF" in h2.GetName())) and (("Sector 2" in Title or "Sector 5" in Title) and (minR == 6.75 and "reg2" in h2.GetName())))
#         extra_con_3 = ((Particle == "pip" and ("mmEF_PipMMEF" in h2.GetName())) and ("Sector 5" in Title and (minR == 6.75)))# and "reg2" in h2.GetName())))
#         extra_con_4 = ((Particle == "pip" and ("'mmEF'" in h2.GetName())) and ((("Sector 5" in Title and minR == 6.75) or ("Sector 6" in Title and minR > 6.15)) and "reg2" in h2.GetName()))
        
#         extra_con_5 = ((Particle == "el" and ("mmEF_PipMMEF" in h2.GetName())) and ("Sector 6" in Title and (minR == 2.5 and "reg3" in h2.GetName())))
        
#         extra_rebin_con = (extra_con_2 or extra_con_3 or extra_con_4 or extra_con_5) and (Particle != "pro")
        
#         if(extra_rebin_con):
#             hy2.Rebin(2)
        

#         hys2.append(hy2)

#         mu = hy2.GetBinCenter(hy2.GetMaximumBin())
#         bin_width_mu = hy2.GetBinWidth(hy2.FindBin(mu))

#         if(MM_type == "epipX" and (mu < 0.5 or mu > 1.15)):
#             mu = 0.9396
#             # print("".join(["\nCheck: ", color.BBLUE, str(Slice_Title), color.END, "\nMax bin centered at: ", str(hy2.GetBinCenter(hy2.GetMaximumBin())), "\n"]))
#             bin_width_mu = 2.5*hy2.GetBinWidth(hy2.FindBin(mu))
                
#         if(MM_type == "eppipX" and (mu < -0.1 or mu > 0.2)):
#             mu = 0
#             print("".join([color.RED, "\nCheck: ", color.BBLUE, str(Slice_Title), color.END, "\nMax bin centered at: ", str(hy2.GetBinCenter(hy2.GetMaximumBin())), "\n"]))
#             bin_width_mu = 2.5*hy2.GetBinWidth(hy2.FindBin(mu))
                
#         if(MM_type == "epX" and (mu < -0.1 or mu > 0.2)):
#             mu = 0        
#             print("".join([color.RED, "\nCheck: ", color.BBLUE, str(Slice_Title), color.END, "\nMax bin centered at: ", str(hy2.GetBinCenter(hy2.GetMaximumBin())), "\n"]))
#             bin_width_mu = 2.5*hy2.GetBinWidth(hy2.FindBin(mu))

        
#         spectrum = ROOT.TSpectrum(5, 2.5)
#         nfound = spectrum.Search(hy2, 2)
        
        
#         if(Particle == "pro"):
#             MM_DP       = 0.13957*0.13957
#             MM_DP_Bin   = hy2.FindBin(MM_DP)
#             MM_MU_Bin   = hy2.FindBin(mu)
#             MM_Spec_Bin = hy2.FindBin((spectrum.GetPositionX())[0])
            
#             MM_Bin_Best = MM_DP
            
#             if(abs(MM_DP_Bin - MM_MU_Bin) < abs(MM_DP_Bin - MM_Spec_Bin)):
#                 MM_Bin_Best = MM_MU_Bin
#                 # print("\nMax")
#                 # print("".join(["minR = ", str(minR)]))
#                 # print("".join(["abs(MM_DP_Bin - MM_MU_Bin) = ", str(abs(MM_DP_Bin - MM_MU_Bin))]))
#                 # print("".join(["abs(MM_DP_Bin - MM_Spec_Bin) = ", str(abs(MM_DP_Bin - MM_Spec_Bin))]))
#                 # if(("Sector 6" in str(Title)) and (minR == 0.45)):
#                 #     print("Max")
#             else:
#                 MM_Bin_Best = MM_Spec_Bin
#                 # print("\nPeak")
#                 # print("".join(["minR = ", str(minR)]))
#                 # print("".join(["abs(MM_DP_Bin - MM_MU_Bin) = ", str(abs(MM_DP_Bin - MM_MU_Bin))]))
#                 # print("".join(["abs(MM_DP_Bin - MM_Spec_Bin) = ", str(abs(MM_DP_Bin - MM_Spec_Bin))]))
#                 # if(("Sector 5" in str(Title)) and (minR == 0.45)):
#                 #     # print("".join(["abs(MM_DP_Bin - MM_MU_Bin) = ", str(abs(MM_DP_Bin - MM_MU_Bin))]))
#                 #     # print("".join(["abs(MM_DP_Bin - MM_Spec_Bin) = ", str(abs(MM_DP_Bin - MM_Spec_Bin))]))
#                 #     # print("Peak")
#                 #     MM_Bin_Best += 1
#                 # if(("Sector 6" in str(Title)) and (minR == 0.45)):
#                 #     print("".join(["minR = ", str(minR)]))
#                 #     print("Peak")
                
#             mu = hy2.GetBinCenter(MM_Bin_Best)
#             bin_width_mu = hy2.GetBinWidth(MM_Bin_Best)
            
            
#             if(MM_DP_Bin == MM_Bin_Best):
#                 bin_width_mu = 0.25*bin_width_mu
#             else:
#                 bin_width_mu = 1.5*bin_width_mu
                
#             if("ProMMpro_LEF" in str(h2.GetName())):
#                 # if("Sector 1" in str(Title)):
#                 # if("Sector 2" in str(Title)):
#                 # if("Sector 3" in str(Title)):
#                 # if("Sector 4" in str(Title)):
#                 if("Sector 5" in str(Title)):
#                     if(minR == 0.45):
#                         bin_width_mu = 0.35*hy2.GetBinWidth(MM_Bin_Best)
#                 #     if(minR == 0.7):
#                 #         bin_width_mu = 2.5*hy2.GetBinWidth(MM_Bin_Best)
#                 if("Sector 6" in str(Title)):
#                     if(minR == 0.45):
#                         bin_width_mu = 0.35*hy2.GetBinWidth(MM_Bin_Best)
            
            

#         if(event_type not in ["DP"]):
#             fit_function = "gaus(0) + pol1(3)"
#         else:
#             fit_function = "gaus(0) + pol2(3)"
        
#         # fy2 = ROOT.TF1("fy2", str(fit_function), mu - 2*0.065, mu + 2*0.065)
#         # fy2 = ROOT.TF1("fy2", str(fit_function), mu - 1*0.065, mu + 1*0.065)
        
#         if(extra_con_1):
#             # print(color.BOLD + "\n" + color.BLUE + str(Slice_Title) + color.END)
#             # print(color.BBLUE + str(h2.GetName()) + color.END + "\n")
#             # fy2 = ROOT.TF1("fy2", str(fit_function), mu - 2*0.065, mu + 2*0.065)
#             fy2 = ROOT.TF1("fy2", str(fit_function), mu - 1*0.065, mu + 1*0.065)
#         elif(extra_con_2 and False):
#             # print(color.BOLD + "\n" + color.BLUE + str(Slice_Title) + color.END)
#             # print(color.BBLUE + str(h2.GetName()) + color.END + "\n")
#             fy2 = ROOT.TF1("fy2", str(fit_function), mu - 3*0.065, mu + 2*0.065)
#         elif(extra_con_pro):
#             fy2 = ROOT.TF1("fy2", str(fit_function), mu - 3*0.065, mu + 4*0.065)
# #             fy2 = ROOT.TF1("fy2", str(fit_function), mu - 3*0.065, mu + 2*0.065)
#         else:
#             fy2 = ROOT.TF1("fy2", str(fit_function), mu - 3*0.065, mu + 3*0.065)

#         fy2.SetParameter(0, 0.85*hy2.GetBinContent(hy2.FindBin(mu)))
#         fy2.SetParLimits(0, 0.65*hy2.GetBinContent(hy2.FindBin(mu)), 1.15*hy2.GetBinContent(hy2.FindBin(mu)))
#         fy2.SetParameter(2, 0.1)
#         fy2.SetParLimits(2, 0.01, 0.3)

#         fy2.SetParName(0, "Constant")
#         fy2.SetParName(1, "Mean")
#         fy2.SetParName(2, "Sigma")
        
        

        
        
# #         if(not (Particle == "pro" and minR < 0.7)):# True):
# #         if(Particle != "pro"):
#         if(True):
#             fy2.SetParameter(1, mu)
#             # if(Particle == "pro" and minR < 0.7):
#             #     fy2.SetParLimits(1, mu - 1.25*bin_width_mu, mu + 1.25*bin_width_mu)
#             # elif(Particle == "pro" and minR < 2.6):
#             #     fy2.SetParLimits(1, mu - 0.75*bin_width_mu, mu + 0.75*bin_width_mu)
#             # elif(Particle == "pro" and minR > 2.6):
#             #     fy2.SetParLimits(1, mu - 1.75*bin_width_mu, mu + 1.75*bin_width_mu)
#             # else:
#             fy2.SetParLimits(1, mu - 1.0*bin_width_mu, mu + 1.0*bin_width_mu)
            
#         else:
#             num_test = 0
#             for peaks in spectrum.GetPositionX():
#                 num_test += 1
#                 current_constant = hy2.GetBinContent(hy2.FindBin(peaks))
#                 fy2.SetParameter((3*num_test) - 3, 0.85*current_constant)
#                 fy2.SetParLimits((3*num_test) - 3, 0.65*current_constant, 1.15*current_constant)
#                 fy2.SetParameter((3*num_test) - 2, peaks)
# #                 fy2.SetParLimits((3*num_test) - 2, peaks - 2*0.0025, peaks + 2*0.0025)
#                 fy2.SetParLimits((3*num_test) - 2, peaks - 0.25*bin_width_mu, peaks + 0.25*bin_width_mu)
#                 fy2.SetParameter((3*num_test) - 1, 0.1)
#                 fy2.SetParLimits((3*num_test) - 1, 0.01, 0.3)
#                 fy2.SetRange(peaks - 2*0.065, peaks + 2*0.065)
#                 break

#         hy2.Fit(fy2, "BRQ")
        

# #         fit_function_BG = "pol1(0)"
# #         fy2_BG = ROOT.TF1("fy2_BG", str(fit_function_BG), mu - 4*0.065, mu + 4*0.065)
# #         fy2_BG.SetParameter(0, fy2.GetParameter(3))
# #         fy2_BG.SetParLimits(0, fy2.GetParameter(3), fy2.GetParameter(3))
# #         fy2_BG.SetParameter(1, fy2.GetParameter(4))
# #         fy2_BG.SetParLimits(1, fy2.GetParameter(4), fy2.GetParameter(4))
# #         fy2_BG.SetLineColor(root_color.Blue)
# #         hy2.Fit(fy2_BG, "BRQ")
        

#         # mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
        
#         # sigma_factor = 1.25
#         sigma_factor = 3
#         sigma_factor_up = 1.75
#         sigma_factor_down = 2
        
        
#         MM_Peak, SIG = fy2.GetParameter(1), abs(fy2.GetParameter(2))

#         gr2.SetPoint(gr2.GetN(), minR+dR/2.0, MM_Peak)
#         gr2_V2.SetPoint(gr2_V2.GetN(), minR+dR/2.0, MM_Peak)
        
#         gr2_Sigma.SetPoint(gr2_Sigma.GetN(), minR+dR/2.0, SIG)
        
#         gr2_Cut_Range_Up.SetPoint(gr2_Sigma.GetN(), minR+dR/2.0, MM_Peak + sigma_factor_up*(SIG))
#         gr2_Cut_Range_Down.SetPoint(gr2_Sigma.GetN(), minR+dR/2.0, MM_Peak - sigma_factor_down*(SIG))
            
            
#         Error_of_MM_Peak = fy2.GetParError(1)
#         Error_of_SIG = fy2.GetParError(2)
        
# #         try:
# #             if(Error_of_MM_Peak < 0.5*(hy2.GetBinWidth(hy2.FindBin(MM_Peak)))):
# #                 Error_of_MM_Peak = 0.5*(hy2.GetBinWidth(hy2.FindBin(MM_Peak)))
# #         except:
# #             print(color.RED + str(traceback.format_exc()) + color.END)
        
#         gr2.SetPointError(gr2.GetN() - 1, dR/2.0, Error_of_MM_Peak)
#         gr2_V2.SetPointError(gr2_V2.GetN() - 1, dR/2.0, Error_of_MM_Peak + sigma_factor_down*(SIG + Error_of_SIG), Error_of_MM_Peak + sigma_factor_up*(SIG + Error_of_SIG))
#         # gr2_V2.SetPointError(gr2_V2.GetN() - 1, 0, 0, Error_of_MM_Peak + sigma_factor_down*(SIG + Error_of_SIG), Error_of_MM_Peak + sigma_factor_up*(SIG + Error_of_SIG))
        
#         gr2_Sigma.SetPointError(gr2_Sigma.GetN() - 1, 0, Error_of_SIG)
        
#         gr2_Cut_Range_Up.SetPointError(gr2_Cut_Range_Up.GetN() - 1, dR/2.0, Error_of_MM_Peak + sigma_factor_up*(Error_of_SIG))
#         gr2_Cut_Range_Down.SetPointError(gr2_Cut_Range_Down.GetN() - 1, dR/2.0, Error_of_MM_Peak + sigma_factor_down*(Error_of_SIG))

        
#         FindPeak_x.append(MM_Peak)
#         FindPeak_y.append(hy2.GetBinContent(hy2.FindBin(MM_Peak)))

#         minR += dR
    
#     setattr(h2, "hys2", hys2)
#     setattr(h2, "gr2", gr2)
#     setattr(h2, "gr2_V2", gr2_V2)
#     setattr(h2, "gr2_Sigma", gr2_Sigma)
#     setattr(h2, "gr2_Cut_Range_Up", gr2_Cut_Range_Up)
#     setattr(h2, "gr2_Cut_Range_Down", gr2_Cut_Range_Down)
#     setattr(h2, "FindPeak_x", FindPeak_x)
#     setattr(h2, "FindPeak_y", FindPeak_y)
    
#     return h2






# ################################################################################################################################################################################################################################################################################################################
# ### New Cell ###################################################################################################################################################################################################################################################################################################
# ################################################################################################################################################################################################################################################################################################################






# Meaning of below: h2 is the 2D histogram to be sliced and fit; minR/maxR is the starting/ending point of the slice range, and dR is the increments of increase between each slice (for p_e, fit range should be minR=2, maxR=8, and dR=1)
def fit2dall(h2, minR, maxR, dR, Title, BGq, Particle, Event_Type_In=event_type):

    hx = h2.ProjectionX()
    hys2, Sigma_Widths = [], []
    gr2, gr2_Sigma, gr2_Cut_Range_Up, gr2_Cut_Range_Down = ROOT.TGraphErrors(), ROOT.TGraphErrors(), ROOT.TGraphErrors(), ROOT.TGraphErrors()
    gr2_V2 = ROOT.TGraphAsymmErrors()
    gr2.SetMarkerStyle(20)
    gr2_V2.SetMarkerStyle(20)
    gr2_Sigma.SetMarkerStyle(20)
    gr2_Cut_Range_Up.SetMarkerStyle(20)
    gr2_Cut_Range_Down.SetMarkerStyle(20)
    
    FindPeak_x, FindPeak_y = [], []

    while minR+dR <= maxR:
        
        extra_con_pro = False
        if(Particle == "pro"):
            extra_con_pro = True
            
            if(Particle == "pro"):
                if(Event_Type_In == "DP" and minR < 0.8):
                    dR = 0.1
                elif(Event_Type_In == "DP"):
                    dR = 0.25
                if(Event_Type_In == "DP" and minR >= 0.85 and dR == 0.05):
                    dR = 0.1
                # if(Event_Type_In == "DP" and minR >= 1.1 and dR < 0.25):
                #     dR += 0.05
                #     dR = round(dR, 3)
                if(Event_Type_In == "DP" and minR >= 1.25 and dR < 0.25):
                    dR = 0.25
                if(Event_Type_In == "P0"):
                    dR = 0.25
                if(Event_Type_In == "DP" and minR == 2.9):
                    dR = 0.5
                if(Event_Type_In == "P0" and minR == 1.2):
                    dR = 0.5

                if(Event_Type_In in ["DP", "P0"]):
                    dR = 0.25
                    if(minR >= 2.2):
                        dR = 0.5
                    if(minR < 1 and Event_Type_In == "DP"):
                        dR = 0.1

            if(Particle == "pro"):
                if(Event_Type_In == "DP" and minR < 0.8):
                    dR = 0.1
                elif(Event_Type_In == "DP"):
                    dR = 0.25
                if(Event_Type_In == "DP" and minR >= 0.85 and dR == 0.05):
                    dR = 0.1
                # if(Event_Type_In == "DP" and minR >= 1.1 and dR < 0.25):
                #     dR += 0.05
                #     dR = round(dR, 3)
                if(Event_Type_In == "DP" and minR >= 1.25 and dR < 0.25):
                    dR = 0.25
                if(Event_Type_In == "P0"):
                    dR = 0.25
                if(Event_Type_In == "DP" and minR == 2.9):
                    dR = 0.5
                if(Event_Type_In == "P0" and minR == 1.2):
                    dR = 0.5

                if(Event_Type_In in ["DP", "P0"]):
                    dR = 0.25
                    if(minR >= 2.2):
                        dR = 0.5
                    if(minR < 1 and Event_Type_In == "DP"):
                        dR = 0.1
                            
#                         dR = 0.05

#                 if(Event_Type_In == "P0"):
#                     dR = 0.1
                if((Event_Type_In == "DP") and (dR < 0.25)):
                    dR = 0.25

            
            
            
#                 if(Particle == "pro" and (Event_Type_In in ["DP", "P0"])):
#                     dR = 0.25
#                     if(minR >= 2.2):
#                         dR = 0.5
#                     if(minR < 1 and Event_Type_In == "DP"):
#                         dR = 0.1

#                         # dR = 0.05





            if(Particle == "pro"):
                if(Event_Type_In == "DP" and minR < 0.8):
                    dR = 0.1
                elif(Event_Type_In == "DP"):
                    dR = 0.25
                if(Event_Type_In == "DP" and minR >= 0.85 and dR == 0.05):
                    dR = 0.1
                # if(Event_Type_In == "DP" and minR >= 1.1 and dR < 0.25):
                #     dR += 0.05
                #     dR = round(dR, 3)
                if(Event_Type_In == "DP" and minR >= 1.25 and dR < 0.25):
                    dR = 0.25
                if(Event_Type_In == "P0"):
                    dR = 0.25
                if(Event_Type_In == "DP" and minR == 2.9):
                    dR = 0.5
                if(Event_Type_In == "P0" and minR == 1.2):
                    dR = 0.5

                if(Event_Type_In in ["DP", "P0"]):
                    dR = 0.25
                    if(minR >= 2.2):
                        dR = 0.5
                    if(minR < 1 and Event_Type_In == "DP"):
                        dR = 0.1


            if(Particle == "pro"):
                if(Event_Type_In == "DP" and minR < 0.8):
                    dR = 0.1
                elif(Event_Type_In == "DP"):
                    dR = 0.25
                if(Event_Type_In == "DP" and minR >= 0.85 and dR == 0.05):
                    dR = 0.1
                # if(Event_Type_In == "DP" and minR >= 1.1 and dR < 0.25):
                #     dR += 0.05
                #     dR = round(dR, 3)
                if(Event_Type_In == "DP" and minR >= 1.25 and dR < 0.25):
                    dR = 0.25
                if(Event_Type_In == "P0"):
                    dR = 0.25
                if(Event_Type_In == "DP" and minR == 2.9):
                    dR = 0.5
                if(Event_Type_In == "P0" and minR == 1.2):
                    dR = 0.5

                if(Event_Type_In in ["DP", "P0"]):
                    dR = 0.25
                    if(minR >= 2.2):
                        dR = 0.5
                    if(minR < 1 and Event_Type_In == "DP"):
                        dR = 0.1

                        dR = 0.05
                        
            if(Particle == "pro"):
                dR = 0.25
                dR = 0.15
#                 dR = 0.3
                        
        
        ib0, ib1 = hx.FindBin(minR), hx.FindBin(minR+dR)

        hy2 = h2.ProjectionY(f"hy{ib1}", ib0, ib1)
        hy2.SetDirectory(0)

        # if(Event_Type_In == "P0"):
        #     hy2.Rebin(2)
        #     hy2.Rebin(2)
        # if(hy2.GetBinContent(hy2.GetMaximumBin()) < 100):
        #     hy2.Rebin(2)
#         hy2.Rebin(2)
        
        
        
        hy2.Rebin(2)
        
        if(Particle == "pro" or Event_Type_In == "DP"):
#             if(minR in [0.45]):
#                 hy2.Rebin(2)
            hy2.Rebin(2)
            hy2.Rebin(2)
#             if(("RE" in str(h2.GetName())) and ("Sector 6" in Title)):
#                 hy2.Rebin(2)
#             if(hy2.GetBinContent(hy2.GetMaximumBin()) < 200):
#                 hy2.Rebin(2)
#             if(hy2.GetBinContent(hy2.GetMaximumBin()) < 200):
#                 hy2.Rebin(2)

        
        Slice_Title = "".join(["#splitline{", Title, "}{p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4)), "}"])
        
#         Slice_Title = str(Slice_Title).replace("{{(Inbending)", "{#color[2]{(Inbending)")
        # print(Title)
#         Slice_Title = "".join(["p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4))])
        hy2.SetTitle(Slice_Title)
#         hy2.SetTitle("".join([Title, "{Test}"]))
        
        
        extra_con_1 = ((Particle == "pip" and ("mmF_PipMMF"   in h2.GetName())) and ("Sector 2"   in Title and (minR == 3.75                                                 and "reg1" in h2.GetName())))
        extra_con_2 = ((Particle == "pip" and ("mmF_PipMMF"   in h2.GetName())) and (("Sector 2"  in Title or "Sector 5" in Title) and (minR == 6.75                         and "reg2" in h2.GetName())))
        extra_con_3 = ((Particle == "pip" and ("mmEF_PipMMEF" in h2.GetName())) and ("Sector 5"   in Title and (minR == 6.75)))# and "reg2" in h2.GetName())))
        extra_con_4 = ((Particle == "pip" and ("'mmEF'"       in h2.GetName())) and ((("Sector 5" in Title and  minR == 6.75)      or ("Sector 6" in Title and minR > 6.15)) and "reg2" in h2.GetName()))
        
        extra_con_5 = ((Particle == "el"  and ("mmEF_PipMMEF" in h2.GetName())) and ("Sector 6"   in Title and (minR == 2.5                                                  and "reg3" in h2.GetName())))
        
        extra_rebin_con = (extra_con_2 or extra_con_3 or extra_con_4 or extra_con_5) and (Particle != "pro")
        
        
        extra_rebin_con = extra_rebin_con
        
        if(extra_rebin_con):
            hy2.Rebin(2)
            

        hys2.append(hy2)

        mu = hy2.GetBinCenter(hy2.GetMaximumBin())
        bin_width_mu = hy2.GetBinWidth(hy2.FindBin(mu))

        if(MM_type == "epipX" and (mu < 0.5 or mu > 1.15)):
            mu = 0.9396
            # print("".join(["\nCheck: ", color.BBLUE, str(Slice_Title), color.END, "\nMax bin centered at: ", str(hy2.GetBinCenter(hy2.GetMaximumBin())), "\n"]))
            bin_width_mu = 2.5*hy2.GetBinWidth(hy2.FindBin(mu))
                
        if(MM_type == "eppipX" and (mu < -0.1 or mu > 0.2)):
            mu = 0
            print("".join([color.RED, "\nCheck: ", color.BBLUE, str(Slice_Title), color.END, "\nMax bin centered at: ", str(hy2.GetBinCenter(hy2.GetMaximumBin())), "\n"]))
            bin_width_mu = 2.5*hy2.GetBinWidth(hy2.FindBin(mu))
                
        if(MM_type == "epX" and (mu < -0.1 or mu > 0.2)):
            mu = 0        
            print("".join([color.RED, "\nCheck: ", color.BBLUE, str(Slice_Title), color.END, "\nMax bin centered at: ", str(hy2.GetBinCenter(hy2.GetMaximumBin())), "\n"]))
            bin_width_mu = 2.5*hy2.GetBinWidth(hy2.FindBin(mu))

        
        spectrum = ROOT.TSpectrum(5, 2.5)
        nfound = spectrum.Search(hy2, 2)
        
        
        if(Particle == "pro"):
            MM_DP       = 0.13957*0.13957
            MM_DP_Bin   = hy2.FindBin(MM_DP)
            MM_MU_Bin   = hy2.FindBin(mu)
            MM_Spec_Bin = hy2.FindBin((spectrum.GetPositionX())[0])
            
            MM_Bin_Best = MM_DP
            
            if(abs(MM_DP_Bin - MM_MU_Bin) < abs(MM_DP_Bin - MM_Spec_Bin)):
                MM_Bin_Best = MM_MU_Bin
                # print("\nMax")
                # print("".join(["minR = ", str(minR)]))
                # print("".join(["abs(MM_DP_Bin - MM_MU_Bin) = ", str(abs(MM_DP_Bin - MM_MU_Bin))]))
                # print("".join(["abs(MM_DP_Bin - MM_Spec_Bin) = ", str(abs(MM_DP_Bin - MM_Spec_Bin))]))
                # if(("Sector 6" in str(Title)) and (minR == 0.45)):
                #     print("Max")
            else:
                MM_Bin_Best = MM_Spec_Bin
                # print("\nPeak")
                # print("".join(["minR = ", str(minR)]))
                # print("".join(["abs(MM_DP_Bin - MM_MU_Bin) = ", str(abs(MM_DP_Bin - MM_MU_Bin))]))
                # print("".join(["abs(MM_DP_Bin - MM_Spec_Bin) = ", str(abs(MM_DP_Bin - MM_Spec_Bin))]))
                # if(("Sector 5" in str(Title)) and (minR == 0.45)):
                #     # print("".join(["abs(MM_DP_Bin - MM_MU_Bin) = ", str(abs(MM_DP_Bin - MM_MU_Bin))]))
                #     # print("".join(["abs(MM_DP_Bin - MM_Spec_Bin) = ", str(abs(MM_DP_Bin - MM_Spec_Bin))]))
                #     # print("Peak")
                #     MM_Bin_Best += 1
                # if(("Sector 6" in str(Title)) and (minR == 0.45)):
                #     print("".join(["minR = ", str(minR)]))
                #     print("Peak")
                
            mu = hy2.GetBinCenter(MM_Bin_Best)
            bin_width_mu = hy2.GetBinWidth(MM_Bin_Best)
            
                
            if("ProMMpro_LEF" in str(h2.GetName())):
                # if("Sector 1" in str(Title)):
                # if("Sector 2" in str(Title)):
                # if("Sector 3" in str(Title)):
                # if("Sector 4" in str(Title)):
                if("Sector 5" in str(Title)):
                    if(minR == 0.45):
                        bin_width_mu = 0.35*hy2.GetBinWidth(MM_Bin_Best)
                #     if(minR == 0.7):
                #         bin_width_mu = 2.5*hy2.GetBinWidth(MM_Bin_Best)
                if("Sector 6" in str(Title)):
                    if(minR == 0.45):
                        bin_width_mu = 0.35*hy2.GetBinWidth(MM_Bin_Best)
                        
            
            if(MM_DP_Bin == MM_Bin_Best):
                # bin_width_mu = 0.25*bin_width_mu
                bin_width_mu = (hy2.GetBinWidth(MM_Bin_Best)) # 0.75*(hy2.GetBinWidth(MM_Bin_Best)) # 0.45*bin_width_mu
                mu = MM_DP
                Fit_Backward, Fit_Forward = 0.25*bin_width_mu, 0.25*bin_width_mu
                Fit_Backward, Fit_Forward =      bin_width_mu,      bin_width_mu
                Fit_Backward, Fit_Forward =  0.5*bin_width_mu,  0.5*bin_width_mu
#                 Fit_Backward, Fit_Forward = 0.75*bin_width_mu, 0.75*bin_width_mu
                
#                 Fit_Backward, Fit_Forward = 0.002, 0.002
                Fit_Backward, Fit_Forward = 0.002, 0.5*bin_width_mu
    
#                 Fit_Backward, Fit_Forward = 0.35*bin_width_mu, 0.5*bin_width_mu
                Fit_Backward, Fit_Forward = 0.004, 0.5*bin_width_mu
    
                Fit_Backward, Fit_Forward = MM_DP, MM_DP
    
                # print("".join([color.BLUE, str(round(0.13957*0.13957, 7)), " is in the correct bin for ", str(round(minR, 3)), "-", str(round(minR+dR, 3)), " (bin_width_mu = ", str(bin_width_mu),")\n\tFitting: ", color.BOLD, str(round(mu - Fit_Backward, 7)), " < ", str(round(mu, 7))," < ", str(round(mu + Fit_Forward, 7)), color.END]))
                
            else:
#                 if(mu < MM_DP):
#                     # Choosen Missing Mass Peak is too small
#                     Fit_Backward = 0.15*(hy2.GetBinWidth(MM_Bin_Best))
#                     Fit_Forward  = (abs(MM_Bin_Best - MM_DP_Bin) + 0.5)*(hy2.GetBinWidth(MM_Bin_Best))
#                     if("Sector 6" in str(Title) and minR in [0.45] and ("ProMMpro_QEF" in str(h2.GetName()))):
#                         mu = hy2.GetBinCenter(MM_Bin_Best + 1)
#                         Fit_Backward = 0.5*(hy2.GetBinWidth(MM_Bin_Best))
#                         Fit_Forward  = (abs((MM_Bin_Best + 1) - MM_DP_Bin) + 0.5)*(hy2.GetBinWidth(MM_Bin_Best))
#                 else:
#                     # Choosen Missing Mass Peak is too large
#                     Fit_Backward = (abs(MM_Bin_Best - MM_DP_Bin) + 0.5)*(hy2.GetBinWidth(MM_Bin_Best))
#                     Fit_Forward  = 0.15*(hy2.GetBinWidth(MM_Bin_Best))
                    
                bin_width_mu = (hy2.GetBinWidth(MM_Bin_Best))
                Fit_Backward, Fit_Forward = bin_width_mu, bin_width_mu
                Fit_Backward, Fit_Forward = MM_DP, MM_DP
                    
                # bin_width_mu = 1.5*bin_width_mu
            

            

        if(Event_Type_In not in ["DP"]):
            fit_function = "gaus(0) + pol1(3)"
        else:
            fit_function = "gaus(0) + pol2(3)"
        
        # fy2 = ROOT.TF1("fy2", str(fit_function), mu - 2*0.065, mu + 2*0.065)
        # fy2 = ROOT.TF1("fy2", str(fit_function), mu - 1*0.065, mu + 1*0.065)
        
        if(Particle != "pro"):
            if(extra_con_1):
                # print(color.BOLD + "\n" + color.BLUE + str(Slice_Title) + color.END)
                # print(color.BBLUE + str(h2.GetName()) + color.END + "\n")
                # fy2 = ROOT.TF1("fy2", str(fit_function), mu - 2*0.065, mu + 2*0.065)
                fy2 = ROOT.TF1("fy2", str(fit_function), mu - 1*0.065, mu + 1*0.065)
            elif(extra_con_2 and False):
                # print(color.BOLD + "\n" + color.BLUE + str(Slice_Title) + color.END)
                # print(color.BBLUE + str(h2.GetName()) + color.END + "\n")
                fy2 = ROOT.TF1("fy2", str(fit_function), mu - 3*0.065, mu + 2*0.065)
            elif(extra_con_pro):
                fy2 = ROOT.TF1("fy2", str(fit_function), mu - 3*0.065, mu + 4*0.065)
                # fy2 = ROOT.TF1("fy2", str(fit_function), mu - 3*0.065, mu + 2*0.065)
            else:
                fy2 = ROOT.TF1("fy2", str(fit_function), mu - 3*0.065, mu + 3*0.065)
                
        else:
            # fy2 = ROOT.TF1("fy2", str(fit_function), mu - 15*bin_width_mu, mu + 10*bin_width_mu)
            
            Full_Backward, Full_Forward = 12, 15 #8
            if("Sector 1" in str(Title)):
                if(minR in [0.45] and ("ProMMpro_LEF" in h2.GetName())):
                    Full_Backward, Full_Forward = 20, 20
                if(minR in [0.45] and ("ProMMpro_QEF" in h2.GetName())):
                    Full_Backward, Full_Forward = 22, 22
                if(minR in [0.55]):
                    Full_Backward, Full_Forward = 13, 20
                if(minR in [0.75, 0.85]):
                    Full_Backward, Full_Forward = 10, 20 # 15, 20
                if(minR in [0.95, 1.05, 1.3]):
                    Full_Backward, Full_Forward = 12, 20
                if(minR in [1.55, 2.05, 2.3]):
                    Full_Backward, Full_Forward = 12, 21
            if("Sector 4" in str(Title)):                    
                if(minR in [0.45]):# and ("ProMM" not in h2.GetName())):
                    Full_Backward, Full_Forward = 15, 20
            if("Sector 5" in str(Title)):
                Full_Forward += 1
                if(minR in [0.75, 0.95, 1.05, 1.55]):
                    Full_Backward, Full_Forward = 12, 20
            if("Sector 6" in str(Title)):
                if(minR in [0.45]):
                    Full_Backward, Full_Forward = 20, 15
#                     Full_Backward, Full_Forward = 12, 9
                if(minR in [0.55, 0.75]):
                    Full_Backward, Full_Forward = 15, 20
            
#             if("ProMMpro_S" in h2.GetName()):
            Full_Backward, Full_Forward = 12, 15
            
            fy2 = ROOT.TF1("fy2", str(fit_function), mu - Full_Backward*hy2.GetBinWidth(MM_Bin_Best), mu + Full_Forward*hy2.GetBinWidth(MM_Bin_Best))

        fy2.SetParameter(0, 0.85*hy2.GetBinContent(hy2.FindBin(mu)))
        fy2.SetParLimits(0, 0.65*hy2.GetBinContent(hy2.FindBin(mu)), 1.15*hy2.GetBinContent(hy2.FindBin(mu)))
        fy2.SetParameter(2, 0.1)
        fy2.SetParLimits(2, 0.001, 0.3)

        fy2.SetParName(0, "Constant")
        fy2.SetParName(1, "Mean")
        fy2.SetParName(2, "Sigma")
        
        

        
        
#         if(not (Particle == "pro" and minR < 0.7)):# True):
#         if(Particle != "pro"):
        if(False):
            num_test = 0
            for peaks in spectrum.GetPositionX():
                num_test += 1
                current_constant = hy2.GetBinContent(hy2.FindBin(peaks))
                fy2.SetParameter((3*num_test) - 3, 0.85*current_constant)
                fy2.SetParLimits((3*num_test) - 3, 0.65*current_constant, 1.15*current_constant)
                fy2.SetParameter((3*num_test) - 2, peaks)
#                 fy2.SetParLimits((3*num_test) - 2, peaks - 2*0.0025, peaks + 2*0.0025)
                fy2.SetParLimits((3*num_test) - 2, peaks - 0.25*bin_width_mu, peaks + 0.25*bin_width_mu)
                fy2.SetParameter((3*num_test) - 1, 0.1)
                fy2.SetParLimits((3*num_test) - 1, 0.01, 0.3)
#                 fy2.SetRange(peaks - 2*0.065, peaks + 2*0.065)
                break
            
        else:
            fy2.SetParameter(1, mu)
            # if(Particle == "pro" and minR < 0.7):
            #     fy2.SetParLimits(1, mu - 1.25*bin_width_mu, mu + 1.25*bin_width_mu)
            # elif(Particle == "pro" and minR < 2.6):
            #     fy2.SetParLimits(1, mu - 0.75*bin_width_mu, mu + 0.75*bin_width_mu)
            # elif(Particle == "pro" and minR > 2.6):
            #     fy2.SetParLimits(1, mu - 1.75*bin_width_mu, mu + 1.75*bin_width_mu)
            # else:
            if(Particle != "pro"):
                fy2.SetParLimits(1, mu - 1.0*bin_width_mu, mu + 1.0*bin_width_mu)
            else:
                fy2.SetParLimits(1, mu - Fit_Backward, mu + Fit_Forward)

            
        if(("mm0_NoELC" in h2.GetName()) or ("'mmEF_PipMMEF'" in h2.GetName()) or ("'mmEF_PipMMEF_NoELC'" in h2.GetName())):
            hy2.Fit(fy2, "NBRQ")
        else:
            hy2.Fit(fy2, "BRQ")
        
        

#         fit_function_BG = "pol1(0)"
#         fy2_BG = ROOT.TF1("fy2_BG", str(fit_function_BG), mu - 4*0.065, mu + 4*0.065)
#         fy2_BG.SetParameter(0, fy2.GetParameter(3))
#         fy2_BG.SetParLimits(0, fy2.GetParameter(3), fy2.GetParameter(3))
#         fy2_BG.SetParameter(1, fy2.GetParameter(4))
#         fy2_BG.SetParLimits(1, fy2.GetParameter(4), fy2.GetParameter(4))
#         fy2_BG.SetLineColor(root_color.Blue)
#         hy2.Fit(fy2_BG, "BRQ")
        

        # mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
        
        # sigma_factor = 1.25
        sigma_factor = 3
        sigma_factor_up = 1.75
        sigma_factor_down = 2
        
        
        MM_Peak, SIG = fy2.GetParameter(1), abs(fy2.GetParameter(2))
        
        
#         print("".join(["\nFor ", str(round(minR, 7)), " < pro < ", str(round(minR + dR, 7)), ": ", color.BOLD, "Peak = ", str(round(MM_Peak, 7)), color.END, " (∆MM = ", str(round(MM_Peak - (0.13957*0.13957), 7)), ")"]))
        
#         if(MM_DP_Bin == MM_Bin_Best):
#             print("".join([color.GREEN, "MM_Peak = ", str(round(MM_Peak, 7)), color.END]))
#         else:
#             print("".join([color.RED, "MM_Peak = ", str(round(MM_Peak, 7)), color.END]))
            
        gr2.SetPoint(gr2.GetN(), minR+dR/2.0, MM_Peak)
        gr2_V2.SetPoint(gr2_V2.GetN(), minR+dR/2.0, MM_Peak)
        
        gr2_Sigma.SetPoint(gr2_Sigma.GetN(), minR+dR/2.0, SIG)
        
        gr2_Cut_Range_Up.SetPoint(gr2_Sigma.GetN(), minR+dR/2.0, MM_Peak + sigma_factor_up*(SIG))
        gr2_Cut_Range_Down.SetPoint(gr2_Sigma.GetN(), minR+dR/2.0, MM_Peak - sigma_factor_down*(SIG))
            
            
        Error_of_MM_Peak = fy2.GetParError(1)
        Error_of_SIG = fy2.GetParError(2)
        
#         try:
#             if(Error_of_MM_Peak < 0.5*(hy2.GetBinWidth(hy2.FindBin(MM_Peak)))):
#                 Error_of_MM_Peak = 0.5*(hy2.GetBinWidth(hy2.FindBin(MM_Peak)))
#         except:
#             print(color.RED + str(traceback.format_exc()) + color.END)
        
        gr2.SetPointError(gr2.GetN() - 1, dR/2.0, Error_of_MM_Peak)
        gr2_V2.SetPointError(gr2_V2.GetN() - 1, dR/2.0, Error_of_MM_Peak + sigma_factor_down*(SIG + Error_of_SIG), Error_of_MM_Peak + sigma_factor_up*(SIG + Error_of_SIG))
        # gr2_V2.SetPointError(gr2_V2.GetN() - 1, 0, 0, Error_of_MM_Peak + sigma_factor_down*(SIG + Error_of_SIG), Error_of_MM_Peak + sigma_factor_up*(SIG + Error_of_SIG))
        
        gr2_Sigma.SetPointError(gr2_Sigma.GetN() - 1, 0, Error_of_SIG)
        
        gr2_Cut_Range_Up.SetPointError(gr2_Cut_Range_Up.GetN() - 1, dR/2.0, Error_of_MM_Peak + sigma_factor_up*(Error_of_SIG))
        gr2_Cut_Range_Down.SetPointError(gr2_Cut_Range_Down.GetN() - 1, dR/2.0, Error_of_MM_Peak + sigma_factor_down*(Error_of_SIG))

        
        FindPeak_x.append(MM_Peak)
        FindPeak_y.append(hy2.GetBinContent(hy2.FindBin(MM_Peak)))

        minR += dR
    
    setattr(h2, "hys2", hys2)
    setattr(h2, "gr2", gr2)
    setattr(h2, "gr2_V2", gr2_V2)
    setattr(h2, "gr2_Sigma", gr2_Sigma)
    setattr(h2, "gr2_Cut_Range_Up", gr2_Cut_Range_Up)
    setattr(h2, "gr2_Cut_Range_Down", gr2_Cut_Range_Down)
    setattr(h2, "FindPeak_x", FindPeak_x)
    setattr(h2, "FindPeak_y", FindPeak_y)
    
    return h2










############################################################################################################################
#####==========#####==========################################################################==========#####==========#####
#####==========#####==========#####     Missing Mass Fits (with In/Out-bending type)     #####==========#####==========#####
#####==========#####==========################################################################==========#####==========#####
############################################################################################################################


def MM_Fits(h2, minR, maxR, dR, Title, BGq, Particle, Bending_Type="In", Event_Type_In=event_type):
    if("In" in Bending_Type and False):
        h2_return = fit2dall(h2, minR, maxR, dR, Title, BGq, Particle, Event_Type_In=Event_Type_In)
        return h2_return
    else:
        hx = h2.ProjectionX()
        hys2, Sigma_Widths = [], []
        gr2, gr2_Sigma, gr2_Cut_Range_Up, gr2_Cut_Range_Down = ROOT.TGraphErrors(), ROOT.TGraphErrors(), ROOT.TGraphErrors(), ROOT.TGraphErrors()
        gr2_V2 = ROOT.TGraphAsymmErrors()
        gr2.SetMarkerStyle(20)
        gr2_V2.SetMarkerStyle(20)
        gr2_Sigma.SetMarkerStyle(20)
        gr2_Cut_Range_Up.SetMarkerStyle(20)
        gr2_Cut_Range_Down.SetMarkerStyle(20)

        FindPeak_x,     FindPeak_y     = [], []
        FindCut_Upper,  FindCut_Lower  = [], []
        ErrorCut_Upper, ErrorCut_Lower = [], []
        
        
        correction_name_print = "mm0" if("mm0" in h2.GetName()) else "mmEF" if("'mmEF'" in h2.GetName()) else "mmExF" if("'mmExF'" in h2.GetName()) else "mmEF_PipMMEF" if("'mmEF_PipMMEF'" in h2.GetName()) else "mmExF_PipMMEF" if("'mmExF_PipMMEF'" in h2.GetName()) else "Error"
        Sector_Name = "Sector 1" if("ector 1" in str(Title)) else "Sector 2" if("ector 2" in str(Title)) else "Sector 3" if("ector 3" in str(Title)) else "Sector 4" if("ector 4" in str(Title)) else "Sector 5" if("ector 5" in str(Title)) else "Sector 6" if("ector 6" in str(Title)) else "All Sectors"
        Region_Name = "reg1" if("reg1" in h2.GetName()) else "reg2" if("reg2" in h2.GetName()) else "reg3" if("reg3" in h2.GetName()) else "regall"
        # print("\nFor", color.BOLD, str(Sector_Name), "--", str(Region_Name), color.END, "the Correction:", color.BOLD, str(correction_name_print), color.END, "the Missing Mass vs", color.BOLD, Particle, color.END, "peaks are:")
        
        Conditions_for_P2_MC = ((Event_Type_In in ["Monte_Carlo_Pass2"]) or all(title_search in Title for title_search in ["(Monte Carlo)", "Pass 2"]))
        
        if(Conditions_for_P2_MC and (Particle in ["pip"])):
            minR, maxR, dR = 1.25, 4.25, 0.5
        #     print(f"{color.BGREEN}\n\nminR, maxR, dR = {minR}, {maxR}, {dR}\n\n{color.END}")
        # else:
        #     print(f"{color.ERROR}\nTitle = {Title}, Event_Type_In = {Event_Type_In}, Particle = {Particle}\nminR, maxR, dR = {minR}, {maxR}, {dR}\n\n{color.END}")
        
        while(minR+dR <= maxR):

            extra_con_pip = (str(Sector_Name) not in ["Sector 1", "Sector 3"]) and (((Region_Name in ["reg2", "reg3"]) and (minR == 6.75)) or ((str(Sector_Name) in ["Sector 4"]) and (Region_Name in ["reg3"]) and (minR > 5.7)))
            extra_con_pip = extra_con_pip and (Particle in ["pip"])
            
            extra_con_el1 =                   (str(Sector_Name) in ["Sector 1"] and (minR in [2])      and (Region_Name in ["reg1"]))
            extra_con_el1 = extra_con_el1  or (str(Sector_Name) in ["Sector 2"] and (minR in [2, 2.5]) and (Region_Name in ["reg2", "reg3"]))
            # extra_con_el1 = extra_con_el1  or (str(Sector_Name) in ["Sector 2"] and (minR in [3])      and (Region_Name in ["reg2"]))
            extra_con_el1 = extra_con_el1  or (str(Sector_Name) in ["Sector 4"] and (minR in [2])      and (Region_Name in ["reg2"]))
            extra_con_el1 = extra_con_el1  or (str(Sector_Name) in ["Sector 5"] and (minR in [2.5])    and (Region_Name in ["reg2"]))
            extra_con_el2 = False
            extra_con_ele = (extra_con_el1 or extra_con_el2) and (Particle in ["el"])
            
            extra_con = (correction_name_print in ["mmEF_PipMMEF"]) and (extra_con_pip or extra_con_ele)
            
            ib0, ib1 = hx.FindBin(minR), hx.FindBin(minR+dR)

            hy2 = h2.ProjectionY(f"hy{ib1}", ib0, ib1)
            hy2.SetDirectory(0)

            hy2.Rebin(2)

            if(hy2.GetBinContent(hy2.GetMaximumBin()) < 200):
                hy2.Rebin(2)
                
            # ((Particle == "el") and ("'mmRP2'" in h2.GetName()) and ("Sector 6" in str(Title)) and ("reg2" in str(h2.GetName())) and (minR in [2.5, 3.0]))
            # print("<<<TESTING>>>")
            if((Particle == "el") and ("'mmRP2'" in h2.GetName()) and ("Sector 6" in str(Title)) and ("reg2" in str(h2.GetName())) and (minR in [2.5, 3.0])):
                # print("<<<REBINNING>>>")
                hy2.Rebin(2)
                
            # print(f"\n\n\nhy2.GetBinContent(hy2.GetMaximumBin()) = {hy2.GetBinContent(hy2.GetMaximumBin())}\n\n\n")
            if(hy2.GetBinContent(hy2.GetMaximumBin()) < 50):
                Slice_Title = "".join(["#splitline{", Title, "}{p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4)), "}"])
                print(f"{color.RED}Warning: Low Bin Content in {color.BOLD}{Slice_Title}{color.END}")
                hy2.Rebin(2)
                
            if(Conditions_for_P2_MC and (Particle in ["pip"])):
                if(hy2.GetBinContent(hy2.GetMaximumBin()) < 100):
                    hy2.Rebin(2)
                if(hy2.GetBinContent(hy2.GetMaximumBin()) < 150):
                    hy2.Rebin(2)
                    
            if((Particle in ["pip"]) and all(title_search in Title for title_search in ["(Outbending)", "Pass 2", "Fall 2018"])):
                if((minR > 7.5) and (Region_Name in ["reg2", "reg3"])):
                    # hy2.Rebin(2)
                    break # Not able to fit thes points anymore (Central Phi Bin is still fine though)
                    
            if((Particle in ["el"]) and all(title_search in Title for title_search in ["(Outbending)", "Pass 2", "Fall 2018"])):
                hy2.Rebin(2)

                
            mu = hy2.GetBinCenter(hy2.GetMaximumBin())
            bin_width_mu = hy2.GetBinWidth(hy2.FindBin(mu))
#             if(hy2.GetBinContent(hy2.GetMaximumBin()) < 200 and Particle in ["el"]):
#                 print("\n\nExtra Rebinning\n\n")
#                 hy2.Rebin(2)
#                 if(hy2.GetBinContent(hy2.GetMaximumBin()) < 200):
#                     hy2.Rebin(2)
#                 if(mu != hy2.GetBinCenter(hy2.GetMaximumBin()) or bin_width_mu != hy2.GetBinWidth(hy2.FindBin(hy2.GetBinCenter(hy2.GetMaximumBin())))):
#                     print("Changing mu or bin_width_mu:")
#                     print("mu (Old) = ", str(mu))
#                     print("bin_width_mu (Old) = ", str(bin_width_mu))
#                     mu = hy2.GetBinCenter(hy2.GetMaximumBin())
#                     bin_width_mu = hy2.GetBinWidth(hy2.FindBin(mu))
#                     print("mu (New) = ", str(mu))
#                     print("bin_width_mu (New) = ", str(bin_width_mu))
#                 else:
#                     print("Not changing mu or bin_width_mu")
                    
            
            Phi_Bin_Title = str(Title)
            if("reg1" in h2.GetName()):
                Phi_Bin_Title = "".join(["#splitline{", str(Title), "}{Central #phi_{",  str(Particle.replace("pip", "#pi^{+}")), "} Bin}"])
            if("reg2" in h2.GetName()):
                Phi_Bin_Title = "".join(["#splitline{", str(Title), "}{Negative #phi_{", str(Particle.replace("pip", "#pi^{+}")), "} Bin}"])
            if("reg3" in h2.GetName()):
                Phi_Bin_Title = "".join(["#splitline{", str(Title), "}{Positive #phi_{", str(Particle.replace("pip", "#pi^{+}")), "} Bin}"])

            Slice_Title = "".join(["#splitline{", Phi_Bin_Title, "}{p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4)), "}"])
            Slice_Title = Slice_Title.replace("Pi+", "#pi^{+}")
            # print(Title)
            hy2.SetTitle(Slice_Title)


            # extra_con_1 = ((Particle == "pip" and ("mmF_PipMMF" in h2.GetName())) and ("Sector 2" in Title and (minR == 3.75 and "reg1" in h2.GetName())))
            # extra_con_2 = ((Particle == "pip" and ("mmF_PipMMF" in h2.GetName())) and (("Sector 2" in Title or "Sector 5" in Title) and (minR == 6.75 and "reg2" in h2.GetName())))
            # extra_con_3 = ((Particle == "pip" and ("mmEF_PipMMEF" in h2.GetName())) and ("Sector 5" in Title and (minR == 6.75)))# and "reg2" in h2.GetName())))
            # extra_con_4 = ((Particle == "pip" and ("'mmEF'" in h2.GetName())) and ((("Sector 5" in Title and minR == 6.75) or ("Sector 6" in Title and minR > 6.15)) and "reg2" in h2.GetName()))
            # extra_con_5 = ((Particle == "el" and ("mmEF_PipMMEF" in h2.GetName())) and ("Sector 6" in Title and (minR == 2.5 and "reg3" in h2.GetName())))
            # extra_rebin_con = (extra_con_2 or extra_con_3 or extra_con_4 or extra_con_5) and (Particle != "pro")
            # if(extra_rebin_con):
            #     hy2.Rebin(2)

            hys2.append(hy2)

            mu = hy2.GetBinCenter(hy2.GetMaximumBin())
#             bin_width_mu = hy2.GetBinWidth(hy2.FindBin(mu))

            if(MM_type == "epipX"  and (mu <  0.5 or mu > 1.15)):
                mu = 0.9396
                # print("".join(["\nCheck: ", color.BBLUE, str(Slice_Title), color.END, "\nMax bin centered at: ", str(hy2.GetBinCenter(hy2.GetMaximumBin())), "\n"]))
                # bin_width_mu = 2.5*hy2.GetBinWidth(hy2.FindBin(mu))

            if(MM_type == "eppipX" and (mu < -0.1 or mu > 0.2)):
                mu = 0
                print("".join([color.RED, "\nCheck: ", color.BBLUE, str(Slice_Title), color.END, "\nMax bin centered at: ", str(hy2.GetBinCenter(hy2.GetMaximumBin())), "\n"]))
                bin_width_mu = 2.5*hy2.GetBinWidth(hy2.FindBin(mu))

            if(MM_type == "epX"    and (mu < -0.1 or mu > 0.2)):
                mu = 0        
                print("".join([color.RED, "\nCheck: ", color.BBLUE, str(Slice_Title), color.END, "\nMax bin centered at: ", str(hy2.GetBinCenter(hy2.GetMaximumBin())), "\n"]))
                bin_width_mu = 2.5*hy2.GetBinWidth(hy2.FindBin(mu))

            try:
                spectrum = ROOT.TSpectrum(5, 2.5)
                nfound = spectrum.Search(hy2, 2)
            except:
                print(f"{color.Error}nfound not found for {color.END_B}'{Slice_Title}'{color.END}")
                nfound = 1

            if(Particle == "pro"):
                MM_DP       = 0.13957*0.13957
                MM_DP_Bin   = hy2.FindBin(MM_DP)
                MM_MU_Bin   = hy2.FindBin(mu)
                MM_Spec_Bin = hy2.FindBin((spectrum.GetPositionX())[0])
                MM_Bin_Best = MM_DP
                if(abs(MM_DP_Bin - MM_MU_Bin) < abs(MM_DP_Bin - MM_Spec_Bin)):
                    MM_Bin_Best = MM_MU_Bin
                else:
                    MM_Bin_Best = MM_Spec_Bin
                mu           = hy2.GetBinCenter(MM_Bin_Best)
                bin_width_mu =  hy2.GetBinWidth(MM_Bin_Best)
                if(MM_DP_Bin == MM_Bin_Best):
                    bin_width_mu = (hy2.GetBinWidth(MM_Bin_Best))
                    mu = MM_DP
                    Fit_Backward, Fit_Forward = MM_DP, MM_DP
                    # print("".join([color.BLUE, str(round(0.13957*0.13957, 7)), " is in the correct bin for ", str(round(minR, 3)), "-", str(round(minR+dR, 3)), " (bin_width_mu = ", str(bin_width_mu),")\n\tFitting: ", color.BOLD, str(round(mu - Fit_Backward, 7)), " < ", str(round(mu, 7))," < ", str(round(mu + Fit_Forward, 7)), color.END]))
                else:
                    bin_width_mu = (hy2.GetBinWidth(MM_Bin_Best))
                    # Fit_Backward, Fit_Forward = bin_width_mu, bin_width_mu
                    Fit_Backward, Fit_Forward = MM_DP, MM_DP
                    # bin_width_mu = 1.5*bin_width_mu


            if(Event_Type_In not in ["DP", "SP"]):
                fit_function = "gaus(0) + pol1(3)"
            else:
                fit_function = "gaus(0) + pol2(3)"

            # fy2 = ROOT.TF1("fy2", str(fit_function), mu - 2*0.065, mu + 2*0.065)
            # fy2 = ROOT.TF1("fy2", str(fit_function), mu - 1*0.065, mu + 1*0.065)

            if(Particle != "pro"):
                # fy2 = ROOT.TF1("fy2", str(fit_function), mu - 3*0.065, mu + 3*0.065)
                fy2 = ROOT.TF1("fy2", str(fit_function), mu - 3.5*bin_width_mu, mu + 3.5*bin_width_mu)
            else:
                Full_Backward, Full_Forward = 12, 15
                fy2 = ROOT.TF1("fy2", str(fit_function), mu - Full_Backward*hy2.GetBinWidth(MM_Bin_Best), mu + Full_Forward*hy2.GetBinWidth(MM_Bin_Best))

            fy2.SetParameter(0, 0.85*hy2.GetBinContent(hy2.FindBin(mu)))
            fy2.SetParLimits(0, 0.65*hy2.GetBinContent(hy2.FindBin(mu)), 1.15*hy2.GetBinContent(hy2.FindBin(mu)))
            fy2.SetParameter(2, 0.1)
            # fy2.SetParLimits(2, 0.001, 0.3)
            fy2.SetParLimits(2, 0.01, 0.3)

            fy2.SetParName(0, "Constant")
            fy2.SetParName(1, "Mean")
            fy2.SetParName(2, "Sigma")
            

            if(extra_con):
                if((Particle in ["pip"]) and (str(Sector_Name) in ["Sector 4"]) and (Region_Name in ["reg3"]) and minR > 6.2):
                    mu           = 0.9418 if(minR == 6.25) else 0.94385
                    bin_width_mu = 0.0065 if(minR == 6.25) else 0.00465
                    # print(color.BOLD, "\n\n\tGoing with mu =", color.BLUE, mu, "+/-", bin_width_mu, color.END, "for p_min =", minR, "\n\n")
                    current_constant = hy2.GetBinContent(hy2.FindBin(mu))
                    fy2.SetParameter(0, 0.85*current_constant)
                    fy2.SetParLimits(0, 0.65*current_constant, 1.15*current_constant)
                    fy2.SetParameter(1, mu)
                    fy2.SetParLimits(1, mu - bin_width_mu, mu + bin_width_mu)
                elif(extra_con_el1):
                    mu           = 0.9409 if(str(Sector_Name) in ["Sector 1"] and (minR in [2]) and (Region_Name in ["reg1"])) else 0.9456 if(str(Sector_Name) in ["Sector 2"] and (minR in [2]) and (Region_Name in ["reg2"])) else 0.9282 if(str(Sector_Name) in ["Sector 2"] and (minR in [2]) and (Region_Name in ["reg3"])) else 0.9277 if(str(Sector_Name) in ["Sector 2"] and (minR in [2.5]) and (Region_Name in ["reg2"])) else 0.9387 if(str(Sector_Name) in ["Sector 2"] and (minR in [2.5]) and (Region_Name in ["reg3"])) else 0.9431 if(str(Sector_Name) in ["Sector 4"] and (minR in [2]) and (Region_Name in ["reg2"])) else 0.9487 if(str(Sector_Name) in ["Sector 5"] and (minR in [2.5]) and (Region_Name in ["reg2"])) else 0.9406
                    # 0.9467 if(str(Sector_Name) in ["Sector 2"] and (minR in [2.5])    and (Region_Name in ["reg3"])) else 
                    bin_width_mu = 0.0102 if(str(Sector_Name) in ["Sector 1"] and (minR in [2]) and (Region_Name in ["reg1"])) else 0.0014 if(str(Sector_Name) in ["Sector 2"] and (minR in [2]) and (Region_Name in ["reg2"])) else 0.0021 if(str(Sector_Name) in ["Sector 2"] and (minR in [2]) and (Region_Name in ["reg3"])) else 0.0016 if(str(Sector_Name) in ["Sector 2"] and (minR in [2.5]) and (Region_Name in ["reg2"])) else 0.0071 if(str(Sector_Name) in ["Sector 2"] and (minR in [2.5]) and (Region_Name in ["reg3"])) else 0.0046 if(str(Sector_Name) in ["Sector 4"] and (minR in [2]) and (Region_Name in ["reg2"])) else 0.0011 if(str(Sector_Name) in ["Sector 5"] and (minR in [2.5]) and (Region_Name in ["reg2"])) else 0.05
                    # 0.0011 if(str(Sector_Name) in ["Sector 2"] and (minR in [2.5])    and (Region_Name in ["reg3"])) else 
                    # print(color.BOLD, "\n\n\tGoing with mu =", color.BLUE, mu, "+/-", bin_width_mu, color.END, "for p_min =", minR, "\n\n")
                    current_constant = hy2.GetBinContent(hy2.FindBin(mu))
                    fy2.SetParameter(0, 0.85*current_constant)
                    fy2.SetParLimits(0, 0.65*current_constant, 1.15*current_constant)
                    fy2.SetParameter(1, mu)
                    fy2.SetParLimits(1, mu - bin_width_mu, mu + bin_width_mu)
                else:
                    fy2.SetParameter(1, mu)
                    fy2.SetParLimits(1, mu - 1.0*bin_width_mu, mu + 1.0*bin_width_mu)
            else:
                num_test = 0
                for peaks in spectrum.GetPositionX():
                    num_test += 1
                    if(peaks > 1.1 or (peaks < 0.5 and Event_Type_In in ["SP"])):
                        if(peaks < 0.5 and Event_Type_In in ["SP"]):
                            current_constant = hy2.GetBinContent(hy2.FindBin(mu))
                            fy2.SetParameter((3*num_test) - 3, 0.85*current_constant)
                            fy2.SetParLimits((3*num_test) - 3, 0.65*current_constant, 1.15*current_constant)
                            fy2.SetParameter((3*num_test) - 2, mu)
                            fy2.SetParLimits((3*num_test) - 2, mu - 0.05, mu + 0.05)
                            fy2.SetParameter((3*num_test) - 1, 0.15)
                            fy2.SetParLimits((3*num_test) - 1, 0.01, 0.4)
                        continue
                    current_constant = hy2.GetBinContent(hy2.FindBin(peaks))
                    fy2.SetParameter((3*num_test) - 3, 0.85*current_constant)
                    fy2.SetParLimits((3*num_test) - 3, 0.65*current_constant, 1.15*current_constant)
                    fy2.SetParameter((3*num_test) - 2, peaks)
                    fy2.SetParLimits((3*num_test) - 2, peaks - 0.005, peaks + 0.005)
                    fy2.SetParameter((3*num_test) - 1, 0.15)
                    fy2.SetParLimits((3*num_test) - 1, 0.01, 0.4)
                    # fy2.SetRange(peaks - 4*0.038, (peaks + 6*0.038) if(minR > 9.9) else (peaks + 8*0.038))
                    break

#             if(("mm0_NoELC" in h2.GetName()) or ("'mmEF_PipMMEF'" in h2.GetName()) or ("'mmEF_PipMMEF_NoELC'" in h2.GetName())):
#                 hy2.Fit(fy2, "NBRQ")
#             else:
#                 hy2.Fit(fy2, "BRQ")
#             fy2.SetParLimits(0, fy2.GetParameter(0) - abs(fy2.GetParError(0)), fy2.GetParameter(0) + abs(fy2.GetParError(0)))
#             fy2.SetParLimits(1, fy2.GetParameter(1) - abs(fy2.GetParError(1)), fy2.GetParameter(1) + abs(fy2.GetParError(1)))
#             fy2.SetParLimits(2, fy2.GetParameter(2) - abs(fy2.GetParError(2)), fy2.GetParameter(2) + abs(fy2.GetParError(2)))
#             fy2.SetParLimits(3, fy2.GetParameter(3) - abs(fy2.GetParError(3)), fy2.GetParameter(3) + abs(fy2.GetParError(3)))
#             fy2.SetParLimits(4, fy2.GetParameter(4) - abs(fy2.GetParError(4)), fy2.GetParameter(4) + abs(fy2.GetParError(4)))
#             if(fit_function != "gaus(0) + pol1(3)"):
#                 fy2.SetParLimits(5, fy2.GetParameter(5) - abs(fy2.GetParError(5)), fy2.GetParameter(5) + abs(fy2.GetParError(5)))
                
            fy2.SetRange(0.8 if(MM_type in ["epipX"]) else -0.1, 1.15 if(MM_type in ["epipX"]) else 0.2)
        
#             if(("mm0_NoELC" in h2.GetName()) or ("'mmEF_PipMMEF'" in h2.GetName()) or ("'mmEF_PipMMEF_NoELC'" in h2.GetName())):
            if(("mm0_NoELC" in h2.GetName()) or ("'mmEF_PipMMEF_NoELC'" in h2.GetName())):
                hy2.Fit(fy2, "NBRQ")
            else:
                hy2.Fit(fy2, "BRQ")

            mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
            
            # sigma_factor = 1.25
            sigma_factor = 3
            sigma_factor_up   = 1.75
            sigma_factor_down = 2
#             if("Pass" in str(Title)):
#                 # print("INCREASING SIG FACTORS...")
#                 sigma_factor_up   = 2.25
#                 sigma_factor_down = 2.25
# #                 if(("reg1" in h2.GetName()) and (Particle in ["el"]) and (Event_Type_In in ["SP"]) and (minR > 7.75)):
#                 if((Particle in ["el"]) and (Event_Type_In in ["SP"]) and ((minR+dR/2.0) > 6)):
#                     sigma_factor_up   = 2
#                     sigma_factor_down = 2


            MM_Peak, SIG = fy2.GetParameter(1), abs(fy2.GetParameter(2))
            
            # print(round(MM_Peak, 5))

            gr2.SetPoint(gr2.GetN(),             minR+dR/2.0, MM_Peak)
            gr2_V2.SetPoint(gr2_V2.GetN(),       minR+dR/2.0, MM_Peak)
            gr2_Sigma.SetPoint(gr2_Sigma.GetN(), minR+dR/2.0, SIG)

            gr2_Cut_Range_Up.SetPoint(gr2_Cut_Range_Up.GetN(),   minR+dR/2.0, MM_Peak + sigma_factor_up*(SIG))
            gr2_Cut_Range_Down.SetPoint(gr2_Cut_Range_Down.GetN(), minR+dR/2.0, MM_Peak - sigma_factor_down*(SIG))

            Error_of_MM_Peak = fy2.GetParError(1)
            Error_of_SIG     = fy2.GetParError(2)

            gr2.SetPointError(gr2.GetN() - 1,        dR/2.0, Error_of_MM_Peak)
            gr2_V2.SetPointError(gr2_V2.GetN() - 1,  dR/2.0, Error_of_MM_Peak + sigma_factor_down*(SIG + Error_of_SIG), Error_of_MM_Peak + sigma_factor_up*(SIG + Error_of_SIG))
            gr2_Sigma.SetPointError(gr2_Sigma.GetN() - 1, 0, Error_of_SIG)

            gr2_Cut_Range_Up.SetPointError(gr2_Cut_Range_Up.GetN() - 1,     dR/2.0, Error_of_MM_Peak + sigma_factor_up*(Error_of_SIG))
            gr2_Cut_Range_Down.SetPointError(gr2_Cut_Range_Down.GetN() - 1, dR/2.0, Error_of_MM_Peak + sigma_factor_down*(Error_of_SIG))

            FindPeak_x.append(MM_Peak)
            FindPeak_y.append(hy2.GetBinContent(hy2.FindBin(MM_Peak)))
            
            FindCut_Upper.append( [MM_Peak          + sigma_factor_up*(SIG),            hy2.GetBinContent(hy2.FindBin(MM_Peak          + sigma_factor_up*(SIG)))])
            FindCut_Lower.append( [MM_Peak          - sigma_factor_down*(SIG),          hy2.GetBinContent(hy2.FindBin(MM_Peak          - sigma_factor_down*(SIG)))])
            ErrorCut_Upper.append([Error_of_MM_Peak + sigma_factor_up*(Error_of_SIG),   hy2.GetBinContent(hy2.FindBin(Error_of_MM_Peak + sigma_factor_up*(Error_of_SIG)))])
            ErrorCut_Lower.append([Error_of_MM_Peak + sigma_factor_down*(Error_of_SIG), hy2.GetBinContent(hy2.FindBin(Error_of_MM_Peak + sigma_factor_down*(Error_of_SIG)))])
            

#             print("\tP =", round(minR+dR/2.0, 5), "---> MM Peak =", round(MM_Peak, 5))# , " error =", round(Error_of_MM_Peak, 5))
            

            minR += dR

        setattr(h2, "hys2",       hys2)
        setattr(h2, "gr2",        gr2)
        setattr(h2, "gr2_V2",     gr2_V2)
        setattr(h2, "gr2_Sigma",  gr2_Sigma)
        setattr(h2, "FindPeak_x", FindPeak_x)
        setattr(h2, "FindPeak_y", FindPeak_y)
        setattr(h2, "gr2_Cut_Range_Up",   gr2_Cut_Range_Up)
        setattr(h2, "gr2_Cut_Range_Down", gr2_Cut_Range_Down)
        setattr(h2, "FindCut_Upper",  FindCut_Upper)
        setattr(h2, "FindCut_Lower",  FindCut_Lower)
        setattr(h2, "ErrorCut_Upper", ErrorCut_Upper)
        setattr(h2, "ErrorCut_Lower", ErrorCut_Lower)
        
        

        return h2










######################################################################################################
#####==========#####==========##########################################==========#####==========#####
#####==========#####==========#####     Fits for ∆P Histograms     #####==========#####==========#####
#####==========#####==========##########################################==========#####==========#####
######################################################################################################    
    
# The function below is used to merge the ∆P fits from the double pion and π0 channel to get the proton corrections from both channels simultaneously
def Merge_Histos(TGE1, TGE2, option="Default", Num_Overlap=2):
    if(option == "Default"):
        Merged_Histo = ROOT.TGraphErrors()
        Merged_Histo.SetMarkerStyle(20)
        Merged_Histo.SetMarkerColor(root_color.Red)
        
        Merged_Histo.SetTitle((TGE1.GetTitle()).replace("Double Pion Channel", "Double Pion (and #pi^{0}) Channels"))
        Merged_Histo.SetTitle((Merged_Histo.GetTitle()).replace("Cut Applied: Calculated Exclusivity Cuts", ""))
        Merged_Histo.GetXaxis().SetTitle(TGE1.GetXaxis().GetTitle())
        Merged_Histo.GetYaxis().SetTitle(TGE1.GetYaxis().GetTitle())

        for TGE1_Entry in range(0, TGE1.GetN() + 1, 1):
            Merged_Histo.SetPoint(Merged_Histo.GetN(), TGE1.GetPointX(TGE1_Entry), TGE1.GetPointY(TGE1_Entry))
            Merged_Histo.SetPointError(Merged_Histo.GetN() - 1, TGE1.GetErrorX(TGE1_Entry), TGE1.GetErrorY(TGE1_Entry))
        for TGE2_Entry in range(0, TGE2.GetN() + 1, 1):
            Merged_Histo.SetPoint(Merged_Histo.GetN(), TGE2.GetPointX(TGE2_Entry), TGE2.GetPointY(TGE2_Entry))
            Merged_Histo.SetPointError(Merged_Histo.GetN() - 1, TGE2.GetErrorX(TGE2_Entry), TGE2.GetErrorY(TGE2_Entry))
    else:
        # Make sure that the Elastic Scattering histogram is inputted second so that TGE2 --> (ES or EO) while TGE1 --> SP
        try:
            Merged_Histo = TGE1.gr2.Clone()
            TGE1_clone   = TGE1.gr2
        except Exception as e:
            print(f"{color.RED}ERROR: {str(e)}{color.END}")
            Merged_Histo = TGE1.Clone()
            TGE1_clone   = TGE1
        Merged_Histo.SetMarkerStyle(20)
        Merged_Histo.SetMarkerColor(root_color.Red)
        Merged_Histo.SetLineColor(root_color.Red)
        
        Merged_Histo.SetTitle((TGE1.GetTitle()).replace("Single Pion Channel", "Single Pion (and Elastic Scattering) Channels"))
        Merged_Histo.SetTitle((Merged_Histo.GetTitle()).replace("Cut Applied: Calculated Exclusivity Cuts", ""))
        Merged_Histo.GetXaxis().SetTitle(TGE1.GetXaxis().GetTitle())
        Merged_Histo.GetYaxis().SetTitle(TGE1.GetYaxis().GetTitle())
        # for TGE1_Entry in range(0, TGE1.GetN() + 1, 1):
        #     Merged_Histo.SetPoint(Merged_Histo.GetN(), TGE1.GetPointX(TGE1_Entry), TGE1.GetPointY(TGE1_Entry))
        #     Merged_Histo.SetPointError(Merged_Histo.GetN() - 1, TGE1.GetErrorX(TGE1_Entry), TGE1.GetErrorY(TGE1_Entry))
        non_overlapped_points = Num_Overlap# + 1
        # print(TGE2.GetPointX(int(TGE2.GetN() - non_overlapped_points)))
        # print(TGE1_clone.GetPointX(TGE1_clone.GetN() - 1))
        # while(TGE2.GetPointX(int(TGE2.GetN() - non_overlapped_points - 1)) < TGE1_clone.GetPointX(TGE1_clone.GetN() - 1)):
        #     # print("Test points overlap...")
        #     non_overlapped_points += -1
        #     if(non_overlapped_points < 0):
        #         print(color.RED + "Error in histogram merge..." + color.END)
        #         break
        # print("Total : " + str(TGE2.GetN() + 1))
        for TGE2_Entry in range(TGE2.GetN() - non_overlapped_points, TGE2.GetN(), 1):
            Merged_Histo.SetPoint(Merged_Histo.GetN(),              TGE2.GetPointX(TGE2_Entry),     TGE2.GetPointY(TGE2_Entry))
            Merged_Histo.SetPointError(Merged_Histo.GetN() - 1, 1.5*TGE2.GetErrorX(TGE2_Entry), 1.5*TGE2.GetErrorY(TGE2_Entry))
        # print("Done with: " + str(Merged_Histo.GetTitle()))
    return Merged_Histo





################################################################################################################################################################################################################################################################################################################
### New Cell ###################################################################################################################################################################################################################################################################################################
################################################################################################################################################################################################################################################################################################################




Dp_Cor_Ideal_FRE = [[0.475, 0.01166, '1'], [0.525, 0.01479, '1'], [0.575, 0.01688, '1'], [0.625, 0.01345, '1'], [0.675, 0.02266, '1'], [0.725, 0.01612, '1'], [0.775, 0.02147, '1'], [0.825, 0.01755, '1'], [0.875, 0.01853, '1'], [0.925, 0.0245, '1'], [0.975, 0.01679, '1'], [1.125, 0.00585, '1'], [1.375, -0.01941, '1'], [1.625, -0.01533, '1'], [1.875, -0.01734, '1'], [2.125, -0.01818, '1'], [2.5, -0.02856, '1'], [0.475, 0.04659, '2'], [0.525, 0.01427, '2'], [0.575, 0.01584, '2'], [0.625, 0.0133, '2'], [0.675, 0.01614, '2'], [0.725, 0.0072, '2'], [0.775, 0.01965, '2'], [0.825, 0.00864, '2'], [0.875, 0.01035, '2'], [0.925, 0.01665, '2'], [0.975, 0.0122, '2'], [1.125, -0.00938, '2'], [1.375, 0.0021, '2'], [1.625, 0.00034, '2'], [1.875, -0.00494, '2'], [2.125, -0.01268, '2'], [2.5, -0.00697, '2'], [0.475, 0.01437, '3'], [0.525, 0.01317, '3'], [0.575, 0.00991, '3'], [0.625, 0.00928, '3'], [0.675, 0.01062, '3'], [0.725, 0.01054, '3'], [0.775, 0.01165, '3'], [0.825, 0.01205, '3'], [0.875, 0.01589, '3'], [0.925, 0.00654, '3'], [0.975, 0.02154, '3'], [1.125, 0.00638, '3'], [1.375, 0.00704, '3'], [1.625, 0.00515, '3'], [1.875, -0.00928, '3'], [2.125, -0.00354, '3'], [2.5, -0.00539, '3'], [0.475, 0.01682, '4'], [0.525, 0.01334, '4'], [0.575, 0.00878, '4'], [0.625, 0.01097, '4'], [0.675, 0.007, '4'], [0.725, 0.00778, '4'], [0.775, 0.01016, '4'], [0.825, 0.01257, '4'], [0.875, 0.01362, '4'], [0.925, 0.01237, '4'], [0.975, 0.01606, '4'], [1.125, 0.01141, '4'], [1.375, 0.00996, '4'], [1.625, 0.01139, '4'], [1.875, -0.00739, '4'], [2.125, 0.00348, '4'], [2.5, -0.00654, '4'], [0.475, 0.00915, '5'], [0.525, 0.01039, '5'], [0.575, 0.0123, '5'], [0.625, 0.01007, '5'], [0.675, 0.0137, '5'], [0.725, 0.00307, '5'], [0.775, 0.00982, '5'], [0.825, 0.01222, '5'], [0.875, 0.0241, '5'], [0.925, 0.01569, '5'], [0.975, 0.00267, '5'], [1.125, 0.01328, '5'], [1.375, 0.00701, '5'], [1.625, -0.01909, '5'], [1.875, -0.015, '5'], [2.125, -0.01, '5'], [2.5, -0.01832, '5'], [0.475, 0.01116, '6'], [0.525, 0.02522, '6'], [0.575, 0.02484, '6'], [0.625, 0.0186, '6'], [0.675, 0.01514, '6'], [0.725, 0.0242, '6'], [0.775, 0.02514, '6'], [0.825, 0.01514, '6'], [0.875, 0.01514, '6'], [0.925, 0.02275, '6'], [0.975, 0.02212, '6'], [1.125, 0.00508, '6'], [1.375, 0.00842, '6'], [1.625, 0.00293, '6'], [1.875, 0.00761, '6'], [2.125, -0.02, '6'], [2.5, -0.0125, '6']]

Dp_Cor_Ideal_FRE_Sec_1, Dp_Cor_Ideal_FRE_Sec_2, Dp_Cor_Ideal_FRE_Sec_3, Dp_Cor_Ideal_FRE_Sec_4, Dp_Cor_Ideal_FRE_Sec_5, Dp_Cor_Ideal_FRE_Sec_6 = [], [], [], [], [], []


for ii in Dp_Cor_Ideal_FRE:
    if('1' in ii):
        Dp_Cor_Ideal_FRE_Sec_1.append(ii)
    if('2' in ii):
        Dp_Cor_Ideal_FRE_Sec_2.append(ii)
    if('3' in ii):
        Dp_Cor_Ideal_FRE_Sec_3.append(ii)
    if('4' in ii):
        Dp_Cor_Ideal_FRE_Sec_4.append(ii)
    if('5' in ii):
        Dp_Cor_Ideal_FRE_Sec_5.append(ii)
    if('6' in ii):
        Dp_Cor_Ideal_FRE_Sec_6.append(ii)
        
        
        
        
        
################################################################################################################################################################################################################################################################################################################
### New Cell ###################################################################################################################################################################################################################################################################################################
################################################################################################################################################################################################################################################################################################################




def fit_Dp_2D(h2, minR, maxR, dR, Title, BGq, Particle, D_Angle=False, Cut_Q=True, Event_Type_In=event_type):
    if("E" not in Event_Type_In):
        
        Short_Q_2 = False
        # if(("El Sector 3" in Title and "(#phi_{El} < -5)" in Title and ("9.0" in Title or "")) or ("El Sector 4" in Title and "(#phi_{El} < -5)" in Title and "9.0" in Title)):
        if((("El Sector 3" in Title or "El Sector 4" in Title) and "(#phi_{El} < -5)" in Title) or ("El Sector 4" in Title and "(-5 < #phi_{El} < 5)" in Title) or ("El Sector 2" in Title and "(#phi_{El} < -5)" in Title  and "(#phi_{El} > 5)" in Title)):
            Short_Q_2 = True
        else:
            Short_Q_2 = False
            
        if("#pi^{+} Sector 5" in Title and "(-10 < #phi_{#pi^{+}} < 10)" in Title):
            Short_Q_2 = True
        if("#pi^{+} Sector " in Title):
            Short_Q_2 = True
            
        if(Particle == "pro"):
            Short_Q_2 = True
            
        Short_Q_2   = True
        Use_Pre_Set = False
            
        if(Short_Q_2):
            hx = h2.ProjectionX()
            hys2, Sigma_Widths = [], []
            gr2, gr2_sigma_up, gr2_sigma_down = ROOT.TGraphErrors(), ROOT.TGraphErrors(), ROOT.TGraphErrors()
            gr2.SetMarkerStyle(20)
            gr2_sigma_up.SetMarkerStyle(20)
            gr2_sigma_down.SetMarkerStyle(20)

            FindPeak_x, FindPeak_y, FindPeak_Cut_Up, FindPeak_Cut_Down = [], [], [], []

            SB_ii = 0
            
            Sector_Title = "1" if("Sector 1" in str(Title)) else "2" if("Sector 2" in str(Title)) else "3" if("Sector 3" in str(Title)) else "4" if("Sector 4" in str(Title)) else "5" if("Sector 5" in str(Title)) else "6" if("Sector 6" in str(Title)) else "All"
            
            Point_by_point_Correction = not True
            
            if(Point_by_point_Correction):
#                 print("".join(["""
# if(sec == """, "1" if("Sector 1" in str(Title)) else "2" if("Sector 2" in str(Title)) else "3" if("Sector 3" in str(Title)) else "4" if("Sector 4" in str(Title)) else "5" if("Sector 5" in str(Title)) else "6" if("Sector 6" in str(Title)) else "Error", """){"""]))
                print("".join(["""
if(sec == """, "1" if("Sector 1" in str(Title)) else "2" if("Sector 2" in str(Title)) else "3" if("Sector 3" in str(Title)) else "4" if("Sector 4" in str(Title)) else "5" if("Sector 5" in str(Title)) else "6" if("Sector 6" in str(Title)) else "Error", """):"""]))
            
            peak_num = 0
            while minR+dR <= maxR:
                
                if(Particle == "pro"):
                    if(Event_Type_In == "DP" and minR < 0.8):
                        dR = 0.1
                    elif(Event_Type_In == "DP"):
                        dR = 0.25
                    if(Event_Type_In == "DP" and minR >= 0.85 and dR == 0.05):
                        dR = 0.1
                    # if(Event_Type_In == "DP" and minR >= 1.1 and dR < 0.25):
                    #     dR += 0.05
                    #     dR = round(dR, 3)
                    if(Event_Type_In == "DP" and minR >= 1.25 and dR < 0.25):
                        dR = 0.25
                    if(Event_Type_In == "P0"):
                        dR = 0.25
                    if(Event_Type_In == "DP" and minR == 2.9):
                        dR = 0.5
                    if(Event_Type_In == "P0" and minR == 1.2):
                        dR = 0.5
                        
                    if(Event_Type_In in ["DP", "P0"]):
                        dR = 0.25
                        if(minR >= 2.2):
                            dR = 0.5
                        if(minR < 1 and Event_Type_In == "DP"):
                            dR = 0.1
                        
#                     if(Event_Type_In == "P0"):
#                         dR = 0.1

                if(Particle == "pro"):
                    if(Event_Type_In == "DP" and minR < 0.8):
                        dR = 0.1
                    elif(Event_Type_In == "DP"):
                        dR = 0.25
                    if(Event_Type_In == "DP" and minR >= 0.85 and dR == 0.05):
                        dR = 0.1
                    # if(Event_Type_In == "DP" and minR >= 1.1 and dR < 0.25):
                    #     dR += 0.05
                    #     dR = round(dR, 3)
                    if(Event_Type_In == "DP" and minR >= 1.25 and dR < 0.25):
                        dR = 0.25
                    if(Event_Type_In == "P0"):
                        dR = 0.25
                    if(Event_Type_In == "DP" and minR == 2.9):
                        dR = 0.5
                    if(Event_Type_In == "P0" and minR == 1.2):
                        dR = 0.5

                    if(Event_Type_In in ["DP", "P0"]):
                        dR = 0.25
                        if(minR >= 2.2):
                            dR = 0.5
                        if(minR < 1 and Event_Type_In == "DP"):
                            dR = 0.1
                            
                            dR = 0.05
                            
                if(Particle == "pro"):
                    dR = 0.25
                    dR = 0.15
                        
                ib0, ib1 = hx.FindBin(minR), hx.FindBin(minR+dR)

                hy2 = h2.ProjectionY(f"hy{ib1}", ib0, ib1)
                hy2.SetDirectory(0)
                
                
                if(Particle != "pro"):
                    hy2.Rebin()
                
                if(Particle == "pip" and minR > 6.2):
                    hy2.Rebin()
                    
                if(Particle == "pip" and minR == 5.75 and "Sector 5" in Title and "< -10" in Title):
                    hy2.Rebin()
                    
                    
                if(Particle == "pro"):
                    hy2.Rebin()
                    if(hy2.GetBinContent(hy2.FindBin(0)) < 100):
                        hy2.Rebin(2)
                    if(hy2.GetBinContent(hy2.FindBin(0)) < 50):
                        hy2.Rebin(2)


                # if(("Fall 2018 - Pass 2" in str(Title)) and ("Fa18" in str(Title)) and ("pip" not in Particle)):
                if(("Fall 2018 - Pass 2" in str(Title)) and ("Fa18" in str(Title))):
                    if(hy2.GetBinContent(hy2.GetMaximumBin()) < 120):
                        hy2.Rebin(2)
                        
                # print(f"\n\n\nhy2.GetBinContent(hy2.GetMaximumBin()) = {hy2.GetBinContent(hy2.GetMaximumBin())}\n\n\n")
                # if(hy2.GetBinContent(hy2.GetMaximumBin()) < 50):
                #     Slice_Title = "".join(["#splitline{", Title, "}{p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4)), "}"])
                #     print(f"{color.RED}Warning: Low Bin Content in {color.BOLD}{Slice_Title}{color.END}")
                #     hy2.Rebin(2)
                        
                hys2.append(hy2)


                mu = hy2.GetBinCenter(hy2.GetMaximumBin())
                if(Event_Type_In in ["DP"] and (mu < -0.2 or mu > 0.2)):
                    # print("RESET")
                    mu = 0

                if("Cut Applied: Calculated Exclusivity Cuts" in str(Title)):
                    Slice_Title = Title.replace("Cut Applied: Calculated Exclusivity Cuts", "".join(["#color[", str(root_color.Black), "]{p_{", Particle, "} Bin: ", str(round(minR, 4)), " < p_{", Particle, "} < ", str(round(minR + dR, 4)), "}"]))
                else:
                    Slice_Title = "".join(["#splitline{", Title, "}{p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4)), "}"])
                hy2.SetTitle(Slice_Title)
                # print(f"\n{hy2.GetTitle()}")

                spectrum = ROOT.TSpectrum(5, 2.5)
                nfound = spectrum.Search(hy2, 2)

                fit_function = "gaus(0) + gaus(3)"
                
                fit_function = "gaus(0) + pol1(3)"
                
#                 if(("'')" in str(h2.GetName())) and (Sector_Title in ["4", "5", "6"]) and not (Sector_Title == "4" and minR > 0.525 and minR < 0.575)):
#                 if((not Use_Pre_Set) and (("'')" in str(h2.GetName())) and (Sector_Title in ["1", "2", "3", "4", "5", "6"]))):
                if((("'')" in str(h2.GetName())) and (Sector_Title in ["1", "2", "3", "4", "5", "6"]))):
                    fit_function = "gaus(0) + pol2(3)"
            
#                 if((("'')" in str(h2.GetName())) and ("FRE" in str(h2.GetName())))):
#                     fit_function = "gaus(0) + gaus(3)"

#                 fit_function = "gaus(0)"

                fy2 = ROOT.TF1("fy2", str(fit_function), mu - 2*0.04, mu + 2*0.04)


                fy2.SetParameter(0, 0.85*hy2.GetBinContent(hy2.FindBin(mu)))
                fy2.SetParLimits(0, 0.65*hy2.GetBinContent(hy2.FindBin(mu)), 1.15*hy2.GetBinContent(hy2.FindBin(mu)))
                fy2.SetParameter(2, 0.15)
                fy2.SetParLimits(2, 0.01, 0.4)
                
                fy2.SetParName(0, "Constant")
                fy2.SetParName(1, "Mean")
                fy2.SetParName(2, "Sigma")
                
                
                conditions_for_peak = [True]
                if("SERC" in str(h2.GetName())):
                    conditions_for_peak = [False]
                    conditions_for_peak.append((Sector_Title == "2") and (minR > 1.7 and minR < 2.2))
                    conditions_for_peak.append((Sector_Title == "3") and (minR > 1.7 and minR < 2.65))
                    conditions_for_peak.append((Sector_Title == "5") and ((minR > 0.69 and minR < 0.74) or (minR > 0.92 and minR < 0.98) or (minR > 1.2 and minR < 1.4) or (minR > 1.7 and minR < 1.9) or (minR+dR == 1.0)))
                    conditions_for_peak.append((Sector_Title == "6") and (minR > 1.2 and minR < 1.45))
                elif("SEC" in str(h2.GetName())):
                    # conditions_for_peak.append(True)
                    conditions_for_peak.append(Sector_Title == "6")
#                     conditions_for_peak.append(not (((Sector_Title == "4") and (minR > 1.45 and minR < 1.7)) or (((Sector_Title == "6") and (minR > 0.84 and minR < 0.89))) or (((Sector_Title == "3") and (minR > 0.94 and minR < 1.1)))))
                    conditions_for_peak.append(not (((Sector_Title == "4") and (minR > 1.45 and minR < 1.7)) or (((Sector_Title == "6") and (minR > 0.84 and minR < 0.89)))))
                elif("SRE" in str(h2.GetName())):
                    conditions_for_peak = [False]
                elif("_RE" in str(h2.GetName())):
                    conditions_for_peak = [False]
                else:
                    conditions_for_peak.append(True)
                    
                if("Corrected (Full) Missing Mass Squared Cut" in str(h2.GetName())):
                    conditions_for_peak = [False]
                    

                if(True not in conditions_for_peak):
                    # print(color.RED + "Running Max" + color.END)
                    fy2.SetParameter(1, mu)
                    fy2.SetParLimits(1, mu - 0.0025, mu + 0.0025)
                    if(("SERC" in str(h2.GetName())) and ((Sector_Title == "4") and (minR > 1.45 and minR < 1.7))):
                        # print(color.RED + "extending range" + color.END)
                        fy2.SetRange(mu - 2*0.055, mu + 2*0.1)
                        
                    fy2.SetRange(-0.15, 0.15)
                        
                else:
                    # print(color.RED + "Running peaks" + color.END)
                    num_test = 0
                    for peaks in spectrum.GetPositionX():
                        num_test += 1
                        current_constant = hy2.GetBinContent(hy2.FindBin(peaks))
                        fy2.SetParameter((3*num_test) - 3, 0.85*current_constant)
                        fy2.SetParLimits((3*num_test) - 3, 0.65*current_constant, 1.15*current_constant)
                        fy2.SetParameter((3*num_test) - 2, peaks)
                        fy2.SetParLimits((3*num_test) - 2, peaks - 2*0.0025, peaks + 2*0.0025)
#                         fy2.SetParLimits((3*num_test) - 2, -0.1, 0.1)
                        fy2.SetParameter((3*num_test) - 1, 0.15)
                        fy2.SetParLimits((3*num_test) - 1, 0.01, 0.4)
                        # fy2.SetRange(peaks - 2*0.04, peaks + 2*0.04)
                        # fy2.SetRange(peaks - 2*0.05, peaks + 2*0.05)
                        fy2.SetRange(peaks - 2*0.085, peaks + 2*0.085)
#                         fy2.SetRange(-0.15, 0.15)
                        break
    
    
    
                ReFit = ("'')" in str(h2.GetName()))
                # Pre-set ∆P correction factors
                if(Use_Pre_Set and ((Event_Type_In in ["DP"]) and ("mmEF_PipMMEF" in str(h2.GetName())) and ("_ProMMpro" not in str(h2.GetName())))):
                    ReFit = False
                    Dp_Cor_Ideal_FRE_Finding = Dp_Cor_Ideal_FRE_Sec_1 if("1" in str(Sector_Title)) else Dp_Cor_Ideal_FRE_Sec_2 if("2" in str(Sector_Title)) else Dp_Cor_Ideal_FRE_Sec_3 if("3" in str(Sector_Title)) else Dp_Cor_Ideal_FRE_Sec_4 if("4" in str(Sector_Title)) else Dp_Cor_Ideal_FRE_Sec_5 if("5" in str(Sector_Title)) else Dp_Cor_Ideal_FRE_Sec_6
                    for Dp_Cor_Final in Dp_Cor_Ideal_FRE_Finding:
                        mom_X, cor_Y, sec = Dp_Cor_Final
                        if(minR < mom_X < minR+dR):
                            fy2.SetParameter(1, cor_Y)
                            fy2.SetParLimits(1, cor_Y - 0.00001, cor_Y + 0.00001)
                            fy2.SetRange(-0.15, 0.15)
                            break
                    
                
                hy2.Fit(fy2, "BRQ")
                
                mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
                
                if(ReFit or True):
                    # print("No cut")
                    peak_num += 1
                    if(Point_by_point_Correction):
                        # print("".join([color.Error, "    // Peak #", str(peak_num), color.END]))
                        print("".join([color.Error, "    # Peak #", str(peak_num), color.END]))
                    if(Sector_Title not in ["1", "2", "3", "4", "5", "6"]):
                        fy2.SetParameter(1, mu)
    #                     fy2.SetParLimits(1, (mu - 0.025) if(Sector_Title not in ["3", "1"]) else (mu - 0.015) if(Sector_Title not in ["1"]) else (mu - 0.005), mu + 0.05)
                        fy2.SetParLimits(1, (mu - 0.025) if(Sector_Title not in ["3", "1"]) else (mu - 0.015) if(Sector_Title not in ["1"]) else 0 if(minR < 0.6) else (mu - 0.005), mu + 0.05)
                        fy2.SetRange(-0.05 if(Sector_Title not in ["1"]) else -0.1, 0.1 if(Sector_Title not in ["3", "1"]) else 0.15)
                        hy2.Fit(fy2, "BRQ")

                        mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))

                        fy2.SetParameter(1, mu)
                        fy2.SetParLimits(1, 0.9*mu, 1.1*mu if(Sector_Title not in ["3", "1"]) else 1.2*mu)
                        fy2.SetRange(-0.2 if(Sector_Title not in ["1"]) else -0.15, 0.2)
                        # fy2.SetRange(-0.2 if(Sector_Title not in ["3"]) else -0.15, 0.2 if(Sector_Title not in ["3"]) else 0.15)
                        hy2.Fit(fy2, "BRQ")

                        mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
                        
                    else:
                        fy2.SetParameter(1, mu)
                        fy2.SetRange(-0.1, 0.1)
                        hy2.Fit(fy2, "BRQ")

                        mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))

                        if(minR < 0.8):
                            fy2.SetRange(-0.06, 0.06)
                        if(minR > 2.0):
                            fy2.SetRange(-0.2, 0.2)
                            
                        fy2.SetParameter(1, mu)
                        fy2.SetParLimits(1, 0.9*mu, 1.1*mu if(mu > 0) else 0.055)
                            
                        hy2.Fit(fy2, "BRQ")

                        mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
                
                # if(("Fall 2018 - Pass 2" in str(Title)) and ("Fa18" in str(Title)) and ("pip" not in Particle)):
                if(("Fall 2018 - Pass 2" in str(Title)) and ("Fa18" in str(Title))):
                    if("pip" not in Particle):
                        if(minR < 7.5):
                            if("Quad - Fa18" in str(Title)):
                                # Using Pion Corrections
                                if(("El Sector 1 -- #phi_{El} Bin:  (-5 < #phi_{El} < 5)" in str(Title)) and ("< 3.95" in str(Slice_Title))):
                                    fy2.SetRange(-0.13, 0.12)
                                elif(("El Sector 1 -- #phi_{El} Bin:  (#phi_{El} > 5)"    in str(Title)) and ("< 4.95" in str(Slice_Title))):
                                    print(f"{color.Error}Slice_Title = {Slice_Title}{color.END}")
                                    fy2.SetRange(-0.13, 0.12)
                                elif(("El Sector 4 -- #phi_{El} Bin:  (#phi_{El} > 5)"    in str(Title)) and ("< 2.45" in str(Slice_Title))):
                                    print(f"{color.Error}Slice_Title = {Slice_Title}{color.END}")
                                    fy2.SetRange(-0.13, 0.12)
                                elif(("El Sector 5 -- #phi_{El} Bin:  (#phi_{El} < -5)"   in str(Title)) and ("< 6.95" in str(Slice_Title))):
                                    print(f"{color.Error}Slice_Title = {Slice_Title}{color.END}")
                                    fy2.SetRange(-0.13, 0.12)
                                elif(("El Sector 6 -- #phi_{El} Bin:  (#phi_{El} < -5)"   in str(Title)) and ("< 2.45" in str(Slice_Title))):
                                    print(f"{color.Error}Slice_Title = {Slice_Title}{color.END}")
                                    fy2.SetRange(-0.12, 0.10)
                                else:
                                    # print(f"Slice_Title = {Slice_Title}")
                                    fy2.SetRange(-0.13, 0.10)
                                # print(f"Title = {Title}")
                            else:
                                fy2.SetRange(-0.13, 0.12)
                        else:
                            fy2.SetRange(-0.145, 0.08)
                    else:
                        fy2.SetRange(-0.16, 0.135)
                    hy2.Fit(fy2, "BRQ")
                    mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
                    

                hy2.SetTitle(Slice_Title)

                if(not D_Angle):
                    Fit_Fixed_Error = 0.01
                else:
                    Fit_Fixed_Error = 0.1

                # Statistical Error Bars
                Error_Bars = fy2.GetParError(1)

                # Pre-Set Error Bars
                hy2.SetTitle(Slice_Title.replace("#DEl", "#Del"))
                if(abs(fy2.GetParError(1)) < Fit_Fixed_Error):
                    Error_Bars = Fit_Fixed_Error
                else:
                    Error_Bars = fy2.GetParError(1)

                par_main_peak = 1
                    
                sigma_factor_upper = 1.25
                sigma_factor_lower = 1.25

                gr2.SetPoint(gr2.GetN(), minR+dR/2.0, fy2.GetParameter(par_main_peak))
                gr2.SetPointError(gr2.GetN()-1, dR/2.0, Error_Bars)

                gr2_sigma_up.SetPoint(gr2_sigma_up.GetN(), minR+dR/2.0, fy2.GetParameter(par_main_peak) + sigma_factor_upper*abs(fy2.GetParameter(par_main_peak + 1)))
                gr2_sigma_up.SetPointError(gr2_sigma_up.GetN()-1, dR/2.0, (Error_Bars**2 + (sigma_factor_upper*fy2.GetParError(par_main_peak + 1))**2)**(0.5))

                gr2_sigma_down.SetPoint(gr2_sigma_down.GetN(), minR+dR/2.0, fy2.GetParameter(par_main_peak) - (sigma_factor_lower*abs(fy2.GetParameter(par_main_peak + 1))))
                gr2_sigma_down.SetPointError(gr2_sigma_down.GetN()-1, dR/2.0, (Error_Bars**2 + (sigma_factor_lower*fy2.GetParError(par_main_peak + 1))**2)**(0.5))


                # Sigma_Widths.append([[Momentum_Min, Momentum_Max, Momentum_Center], [Upper_Width, Lower_Width]])
                Sigma_Widths.append([[minR, minR+dR, minR+dR/2.0], [fy2.GetParameter(par_main_peak) + sigma_factor_upper*abs(fy2.GetParameter(par_main_peak + 1)), fy2.GetParameter(par_main_peak) - (sigma_factor_lower*abs(fy2.GetParameter(par_main_peak + 1)))]])

                FindPeak_x.append(fy2.GetParameter(par_main_peak))
                FindPeak_y.append(hy2.GetBinContent(hy2.FindBin(fy2.GetParameter(par_main_peak))))

                FindPeak_Cut_Up.append(fy2.GetParameter(par_main_peak) + sigma_factor_upper*abs(fy2.GetParameter(par_main_peak + 1)))
                FindPeak_Cut_Down.append(fy2.GetParameter(par_main_peak) - sigma_factor_lower*abs(fy2.GetParameter(par_main_peak + 1)))


                if(Point_by_point_Correction):
#                     print("".join(["""    if(""", str(print_rounded_str(minR, rounding=5)), " < pp && pp < ", str(print_rounded_str(minR + dR, rounding=5)), """){
#         dp = dp + (""", str(print_rounded_str(mu, rounding=5)),""");
#     }"""]))
#                     print("".join(["""    if(""", str(print_rounded_str(minR, rounding=5)), " < pp && pp < ", str(print_rounded_str(minR + dR, rounding=5)), """){
#         dp = dp + (""", str(print_rounded_str(mu, rounding=5)),""");
#     }"""]))
                    print("".join(["""    if(""", str(print_rounded_str(minR, rounding=5)), " < pp and pp < ", str(print_rounded_str(minR + dR, rounding=5)), """):
        dp = dp + (""", str(print_rounded_str(mu, rounding=5)), ")"]))
                
                
                
                minR += dR
                
            if(Point_by_point_Correction):
                print("".join(["""
}
"""]))
                
                     
        else:
            
            # print("Defining ∆P/Theta/Phi fits...")
            hx = h2.ProjectionX()
            hys2, Sigma_Widths = [], []
            gr2, gr2_sigma_up, gr2_sigma_down = ROOT.TGraphErrors(), ROOT.TGraphErrors(), ROOT.TGraphErrors()
            gr2.SetMarkerStyle(20)
            gr2_sigma_up.SetMarkerStyle(20)
            gr2_sigma_down.SetMarkerStyle(20)

            FindPeak_x, FindPeak_y, FindPeak_Cut_Up, FindPeak_Cut_Down = [], [], [], []

            SB_ii = 0

            # print("".join(["\nNumber of x-bins: ", str(hx.GetNbinsX())]))
            # print("".join(["Min x-bin: ", str(round(hx.GetBinCenter(0), 4))]))
            # print("".join(["Max x-bin: ", str(round(hx.GetBinCenter(hx.GetNbinsX()), 4))]))
            # print("".join(["Size of bins = ", str(round((hx.GetBinCenter(hx.GetNbinsX()) - hx.GetBinCenter(0))/hx.GetNbinsX(), 4)), "/bin\n"]))
            
            Sector_Title = "1" if("Sector 1" in str(Title)) else "2" if("Sector 2" in str(Title)) else "3" if("Sector 3" in str(Title)) else "4" if("Sector 4" in str(Title)) else "5" if("Sector 5" in str(Title)) else "6" if("Sector 6" in str(Title)) else "All"
            Point_by_point_Correction = False # True
            if(Point_by_point_Correction):
                print("".join(["""
if(sec == """, "1" if("Sector 1" in str(Title)) else "2" if("Sector 2" in str(Title)) else "3" if("Sector 3" in str(Title)) else "4" if("Sector 4" in str(Title)) else "5" if("Sector 5" in str(Title)) else "6" if("Sector 6" in str(Title)) else "Error", """):"""]))

            while minR+dR <= maxR:
                ib0, ib1 = hx.FindBin(minR), hx.FindBin(minR+dR)

                # print("".join(["\nminR = ", str(round(minR, 4)), " -> bin ", str(ib0)]))
                # print("".join(["minR+dR = ", str(round(minR+dR, 4)), " -> bin ", str(ib1)]))
                # print("".join(["Size of bin = ", str(round(dR/(ib1 - ib0), 4)), "/bin"]))
                # if(minR+dR+dR > maxR):
                #     print("\n")

                # ib0,ib1 = 0, -1
                hy2 = h2.ProjectionY(f"hy{ib1}", ib0, ib1)
                hy2.SetDirectory(0)

                if(BGq == 'yes'):
                    hy2.Add(hy2.ShowBackground(int(30/((SB_ii/2) + 1))), -1)
                    SB_ii += 1
                    for ii in range(0,hy2.GetNbinsX()+1,1):
                        if(hy2.GetBinContent(ii) < 0):
                            hy2.SetBinContent(ii,0)

                if(Event_Type_In == "P0"):
                    hy2.Rebin(4)
                    if(hy2.GetBinContent(hy2.GetMaximumBin()) < 100):
                        hy2.Rebin()
                        
                if(Particle == "pip"):
                    hy2.Rebin()

                hys2.append(hy2)


                # fit_function = "gaus(0) + pol1(3)" if(Event_Type_In != "ES") else "gaus(0)" if(not D_phi) else "gaus(0) + gaus(3)"

                fit_function = "gaus(0) + pol1(3)" if(Event_Type_In != "ES") else "gaus(0) + gaus(3)" if(not Cut_Q) else "gaus(0)"

                fit_function = "gaus(0) + pol1(3)"
                
                # if(Particle == "pip"):
                #     fit_function = "gaus(0)"

                if(not D_Angle or D_Angle == "Theta"):
                    fy2 = ROOT.TF1("fy2", str(fit_function), -1, 1)
                else:
                    fy2 = ROOT.TF1("fy2", str(fit_function), 176, 184)

                # mu = 0
                mu = hy2.GetBinCenter(hy2.GetMaximumBin())


                if(not D_Angle):
                    if(hy2.GetBinContent(hy2.GetMaximumBin()) < 180):
                        hy2.Rebin()

                if("E" not in Event_Type_In):
                    if(hy2.GetBinContent(hy2.GetMaximumBin()) < 180 and Particle == 'el'):
                        hy2.Rebin()
    #                 if(minR > 1.5):
    #                     if(hy2.GetBinContent(hy2.GetMaximumBin()) < 180):
    #                         hy2.Rebin()
    #                     if(hy2.GetBinContent(hy2.GetMaximumBin()) < 180):
    #                         hy2.Rebin()


                # print("\n Max peak value of " + str(Title) + " is " + str(hy2.GetBinCenter(hy2.GetMaximumBin())) +"\n")

                fy2.SetParameters(1, mu, 0.05)
                # if(mu < 0):
                #     fy2.SetParLimits(1, mu - 0.1, 0)
                # else:
                #     fy2.SetParLimits(1, 0, mu + 0.1)
                fy2.SetParLimits(1, mu - 0.1, mu + 0.1)

                fy2.SetParameter(0, hy2.GetBinContent(hy2.GetMaximumBin()))
                fy2.SetParLimits(0, 0.75*(hy2.GetBinContent(hy2.GetMaximumBin())), 1.25*(hy2.GetBinContent(hy2.GetMaximumBin())))

                if("gaus(3)" in fit_function):
                    fy2.SetParameter(3, 0.1*hy2.GetBinContent(hy2.GetMaximumBin()))
                    fy2.SetParLimits(3, 0, 0.25*(hy2.GetBinContent(hy2.GetMaximumBin())))
                    fy2.SetParameter(5, 0.15)
                    fy2.SetParLimits(5, 0.01, 0.3)


                if(not D_Angle):
                    fy2.SetRange(mu - 0.15, mu + 0.15)
                    if(not Cut_Q and D_Angle == "Theta"):
                        fy2.SetParLimits(2, 0.001, 5)
                        fy2.SetParameter(2, 0.5)
                        fy2.SetRange(-5, 5)
                else:
                    fy2.SetParLimits(0, 0.7*(hy2.GetBinContent(hy2.GetMaximumBin())), 1.25*(hy2.GetBinContent(hy2.GetMaximumBin())))
                    fy2.SetParameters(1, mu, 0.05)
                    fy2.SetParLimits(1, mu - 4, mu + 4)
                    fy2.SetParLimits(2, 0.001, 3)
                    if(not Cut_Q and D_Angle == "Theta"):
                        fy2.SetParLimits(2, 0.001, 5)
                        fy2.SetParameter(2, 0.5)
                    if("gaus(3)" in fit_function):
                        fy2.SetParameter(3, 0.1*hy2.GetBinContent(hy2.GetMaximumBin()))
                        fy2.SetParLimits(3, 0, 0.65*(hy2.GetBinContent(hy2.GetMaximumBin())))
                        fy2.SetParLimits(5, 0.1, 40)
                    fy2.SetRange(mu*0.8, mu*1.2)



                if(D_Angle == "Theta"):
                    fy2.SetParLimits(2, 0.001, 5)
                    fy2.SetParameter(2, 0.5)
                    fy2.SetRange(-5, 5)

                hy2.Fit(fy2, "RQ")


                # hy2.SetTitle("".join(["#splitline{", Title, "}{p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4)), "}"]))

                mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))

                if(not D_Angle):
                    if("E" not in Event_Type_In):
                        fy2.SetRange(mu - 3*sig, mu + 3*sig)
                    else:
                        fy2.SetRange(mu - 5*sig, mu + 5*sig)


                if(minR > 1):
                    hy2.Fit(fy2, "RQ")
                    mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))


                # # ERROR BAR OPTIONS:
                # Error_Option = "Stat" # This option uses the default errors given by the fits (i.e., Error_Bars = fy2.GetParError(1))
                Error_Option = "Set" # This option uses a user defined error for error bars (i.e., Error_Bars = Fit_Fixed_Error)
                # # This code will always default to fy2.GetParError(1) if it gives the largest error bars

                Slice_Title = "".join(["#splitline{", Title, "}{p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4)), "}"])
                
                Slice_Title = "".join(["p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4))])

                hy2.SetTitle(Slice_Title)
                hy2.SetTitle(Title)


                if(not D_Angle):
                    Fit_Fixed_Error = 0.01
                else:
                    Fit_Fixed_Error = 0.1

                # Statistical Error Bars
                Error_Bars = fy2.GetParError(1)

                # Pre-Set Error Bars
                if(Error_Option == "Set"):
                    hy2.SetTitle(Slice_Title.replace("#DEl", "#Del"))
                    if(abs(fy2.GetParError(1)) < Fit_Fixed_Error):
                        Error_Bars = Fit_Fixed_Error
                    else:
                        # print("The statistical error is too large for: " + str(hy2.GetTitle()))
                        Error_Bars = fy2.GetParError(1)



                sigma_factor_upper = 1.25
                sigma_factor_lower = 1.25
                if(D_Angle == "Theta"):
                    sigma_factor_upper = 2
                    sigma_factor_lower = 2
                if(D_Angle and D_Angle != "Theta"):
                    sigma_factor_upper = 2
                    sigma_factor_lower = 2

                gr2.SetPoint(gr2.GetN(), minR+dR/2.0, fy2.GetParameter(1))
                gr2.SetPointError(gr2.GetN()-1, dR/2.0, Error_Bars)

                gr2_sigma_up.SetPoint(gr2_sigma_up.GetN(), minR+dR/2.0, fy2.GetParameter(1) + sigma_factor_upper*abs(fy2.GetParameter(2)))
                gr2_sigma_up.SetPointError(gr2_sigma_up.GetN()-1, dR/2.0, (Error_Bars**2 + (sigma_factor_upper*fy2.GetParError(2))**2)**(0.5))
                # gr2_sigma_up.SetPointError(gr2_sigma_up.GetN()-1, 0 if(not D_Angle) else dR/2.0, (Error_Bars**2 + (sigma_factor_upper*fy2.GetParError(2))**2)**(0.5))


                gr2_sigma_down.SetPoint(gr2_sigma_down.GetN(), minR+dR/2.0, fy2.GetParameter(1) - (sigma_factor_lower*abs(fy2.GetParameter(2))))
                gr2_sigma_down.SetPointError(gr2_sigma_down.GetN()-1, dR/2.0, (Error_Bars**2 + (sigma_factor_lower*fy2.GetParError(2))**2)**(0.5))
                # gr2_sigma_down.SetPointError(gr2_sigma_down.GetN()-1, 0 if(not D_Angle) else dR/2.0, (Error_Bars**2 + (sigma_factor_lower*fy2.GetParError(2))**2)**(0.5))



                # Sigma_Widths.append([[Momentum_Min, Momentum_Max, Momentum_Center], [Upper_Width, Lower_Width]])
                Sigma_Widths.append([[minR, minR+dR, minR+dR/2.0], [fy2.GetParameter(1) + sigma_factor_upper*abs(fy2.GetParameter(2)), fy2.GetParameter(1) - (sigma_factor_lower*abs(fy2.GetParameter(2)))]])

                FindPeak_x.append(fy2.GetParameter(1))
                FindPeak_y.append(hy2.GetBinContent(hy2.FindBin(fy2.GetParameter(1))))

                FindPeak_Cut_Up.append(fy2.GetParameter(1) + sigma_factor_upper*abs(fy2.GetParameter(2)))
                FindPeak_Cut_Down.append(fy2.GetParameter(1) - sigma_factor_lower*abs(fy2.GetParameter(2)))
                
                if(Point_by_point_Correction):
                    print("".join(["""    if(""", str(print_rounded_str(minR + 0.0, rounding=5)), " < pp and pp < ", str(print_rounded_str(minR + 0.0 + dR, rounding=5)), """):
        dp = dp + (""", str(print_rounded_str(mu, rounding=5)), ")"]))

                minR += dR
                
            if(Point_by_point_Correction):
                print("".join(["""
                
"""]))

        setattr(h2, "hys2", hys2)
        setattr(h2, "gr2", gr2)
        setattr(h2, "FindPeak_x", FindPeak_x)
        setattr(h2, "FindPeak_y", FindPeak_y)
        setattr(h2, "FindPeak_Cut_Up", FindPeak_Cut_Up)
        setattr(h2, "FindPeak_Cut_Down", FindPeak_Cut_Down)
        setattr(h2, "gr2_sigma_up", gr2_sigma_up)
        setattr(h2, "gr2_sigma_down", gr2_sigma_down)
        setattr(h2, "Sigma_Widths", Sigma_Widths)
        
    else:
        
        
        
        
        Short_Q = False
        if("Electron Only" in Title):
            Short_Q = True
        else:
            Short_Q = False
        
        
        if(Short_Q):
            hx = h2.ProjectionX()
            hys2, Sigma_Widths = [], []
            gr2, gr2_sigma_up, gr2_sigma_down = ROOT.TGraphErrors(), ROOT.TGraphErrors(), ROOT.TGraphErrors()
            gr2.SetMarkerStyle(20)
            gr2_sigma_up.SetMarkerStyle(20)
            gr2_sigma_down.SetMarkerStyle(20)

            FindPeak_x, FindPeak_y, FindPeak_Cut_Up, FindPeak_Cut_Down = [], [], [], []

            SB_ii = 0
            
            if("Pass" not in str(Title)):
                if("El Sector 3" in Title and "(#phi_{El} > 5)" in Title):
                    dR = 2*dR
                    minR = maxR - 2*dR
                    print("\nDoubling size of the bin (manual fix to problematic fit)\n")

            while minR+dR <= maxR:
                ib0, ib1 = hx.FindBin(minR), hx.FindBin(minR+dR)

                hy2 = h2.ProjectionY(f"hy{ib1}", ib0, ib1)
                hy2.SetDirectory(0)

                if(minR < 9.2):
                    hy2.Rebin()
                
                hys2.append(hy2)

                mu = hy2.GetBinCenter(hy2.GetMaximumBin())

                hy2.SetTitle("".join(["#splitline{", Title, "}{p_{", Particle, "} Bin: ", str(round(minR, 4)), " < p_{", Particle, "} < ", str(round(minR + dR, 4)), "}"]))

                spectrum = ROOT.TSpectrum(5, 2.5)
                nfound = spectrum.Search(hy2, 2)


                fit_function = "gaus(0) + gaus(3)"

                fy2 = ROOT.TF1("fy2", str(fit_function), mu - 0.04, mu + 0.04)

                Slice_Title = "".join(["#splitline{", Title, "}{p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4)), "}"])

                fy2.SetParameter(0, 0.85*hy2.GetBinContent(hy2.FindBin(mu)))
                fy2.SetParLimits(0, 0.65*hy2.GetBinContent(hy2.FindBin(mu)), 1.15*hy2.GetBinContent(hy2.FindBin(mu)))
                fy2.SetParameter(2, 0.1)
                fy2.SetParLimits(2, 0.01, 0.3)

                
                Condition_For_NOT_GetPositionX = (("El Sector 3" in Title and str(round(minR + dR, 4)) == "9.7" and ("(#phi_{El} < -5)" in Title or "(#phi_{El} > 5)" in Title)) or ("El Sector 4" in Title and "(#phi_{El} > 5)" in Title))
                # Condition_For_NOT_GetPositionX = ((minR > 9) and ("El Sector 3" in Title and str(round(minR + dR, 4)) == "9.7" and ("(#phi_{El} < -5)" in Title or "(#phi_{El} > 5)" in Title)) or ("El Sector 4" in Title and "(#phi_{El} > 5)" in Title))
                if(Condition_For_NOT_GetPositionX or ("El Sector 1" in Slice_Title and "8.7" in Slice_Title and "8.95" in Slice_Title)):
                    fy2.SetParameter(1, mu)
                    fy2.SetParLimits(1, mu - 0.0025, mu + 0.0025)
                else:
                    num_test = 0
                    for peaks in spectrum.GetPositionX():
                        num_test += 1
                        current_constant = hy2.GetBinContent(hy2.FindBin(peaks))
                        fy2.SetParameter((3*num_test) - 3, 0.85*current_constant)
                        fy2.SetParLimits((3*num_test) - 3, 0.65*current_constant, 1.15*current_constant)
                        fy2.SetParameter((3*num_test) - 2, peaks)
                        fy2.SetParLimits((3*num_test) - 2, peaks - 0.0025, peaks + 0.0025)
                        fy2.SetParameter((3*num_test) - 1, 0.1)
                        fy2.SetParLimits((3*num_test) - 1, 0.01, 0.3)
                        fy2.SetRange(peaks - 0.04, peaks + 0.04)
                        break

                hy2.Fit(fy2, "BRQ")
                
                mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))

                hy2.SetTitle(Slice_Title)

                if(not D_Angle):
                    Fit_Fixed_Error = 0.01
                else:
                    Fit_Fixed_Error = 0.1

                # Statistical Error Bars
                Error_Bars = fy2.GetParError(1)

                # Pre-Set Error Bars
                hy2.SetTitle(Slice_Title.replace("#DEl", "#Del"))
                if(abs(fy2.GetParError(1)) < Fit_Fixed_Error):
                    Error_Bars = Fit_Fixed_Error
                else:
                    Error_Bars = fy2.GetParError(1)

                par_main_peak = 1
                    
                sigma_factor_upper = 1.25
                sigma_factor_lower = 1.25

                gr2.SetPoint(gr2.GetN(), minR+dR/2.0, fy2.GetParameter(par_main_peak))
                gr2.SetPointError(gr2.GetN()-1, dR/2.0, Error_Bars)

                gr2_sigma_up.SetPoint(gr2_sigma_up.GetN(), minR+dR/2.0, fy2.GetParameter(par_main_peak) + sigma_factor_upper*abs(fy2.GetParameter(par_main_peak + 1)))
                gr2_sigma_up.SetPointError(gr2_sigma_up.GetN()-1, dR/2.0, (Error_Bars**2 + (sigma_factor_upper*fy2.GetParError(par_main_peak + 1))**2)**(0.5))

                gr2_sigma_down.SetPoint(gr2_sigma_down.GetN(), minR+dR/2.0, fy2.GetParameter(par_main_peak) - (sigma_factor_lower*abs(fy2.GetParameter(par_main_peak + 1))))
                gr2_sigma_down.SetPointError(gr2_sigma_down.GetN()-1, dR/2.0, (Error_Bars**2 + (sigma_factor_lower*fy2.GetParError(par_main_peak + 1))**2)**(0.5))


                # Sigma_Widths.append([[Momentum_Min, Momentum_Max, Momentum_Center], [Upper_Width, Lower_Width]])
                Sigma_Widths.append([[minR, minR+dR, minR+dR/2.0], [fy2.GetParameter(par_main_peak) + sigma_factor_upper*abs(fy2.GetParameter(par_main_peak + 1)), fy2.GetParameter(par_main_peak) - (sigma_factor_lower*abs(fy2.GetParameter(par_main_peak + 1)))]])

                FindPeak_x.append(fy2.GetParameter(par_main_peak))
                FindPeak_y.append(hy2.GetBinContent(hy2.FindBin(fy2.GetParameter(par_main_peak))))

                FindPeak_Cut_Up.append(fy2.GetParameter(par_main_peak) + sigma_factor_upper*abs(fy2.GetParameter(par_main_peak + 1)))
                FindPeak_Cut_Down.append(fy2.GetParameter(par_main_peak) - sigma_factor_lower*abs(fy2.GetParameter(par_main_peak + 1)))


                minR += dR
                
                
                
                
                
                
        
        elif(not Short_Q):
            hx = h2.ProjectionX()
            hys2, Sigma_Widths = [], []
            gr2, gr2_sigma_up, gr2_sigma_down = ROOT.TGraphErrors(), ROOT.TGraphErrors(), ROOT.TGraphErrors()
            gr2.SetMarkerStyle(20)
            gr2_sigma_up.SetMarkerStyle(20)
            gr2_sigma_down.SetMarkerStyle(20)

            FindPeak_x, FindPeak_y, FindPeak_Cut_Up, FindPeak_Cut_Down = [], [], [], []

            SB_ii = 0

            while minR+dR <= maxR:
                ib0, ib1 = hx.FindBin(minR), hx.FindBin(minR+dR)

                hy2 = h2.ProjectionY(f"hy{ib1}", ib0, ib1)
                hy2.SetDirectory(0)

                if(BGq == 'yes'):
                    hy2.Add(hy2.ShowBackground(int(30/((SB_ii/2) + 1))), -1)
                    SB_ii += 1
                    for ii in range(0,hy2.GetNbinsX()+1,1):
                        if(hy2.GetBinContent(ii) < 0):
                            hy2.SetBinContent(ii,0)

                if(Event_Type_In == "P0"):
                    hy2.Rebin(4)
                    if(hy2.GetBinContent(hy2.GetMaximumBin()) < 100):
                        hy2.Rebin()

                if(hy2.GetBinContent(hy2.GetMaximumBin()) < 40):
                    hy2.Rebin()
                hys2.append(hy2)


                # mu = 0
                mu = hy2.GetBinCenter(hy2.GetMaximumBin())

                hy2.SetTitle("".join(["#splitline{", Title, "}{p_{", Particle, "} Bin: ", str(round(minR, 4)), " < p_{", Particle, "} < ", str(round(minR + dR, 4)), "}"]))

                spectrum = ROOT.TSpectrum(5, 2.5)
                nfound = spectrum.Search(hy2, 2)


                fit_function = "gaus(0)" if(nfound == 1) else "gaus(0) + gaus(3)" if(nfound == 2) else "gaus(0) + gaus(3) + gaus(7)"
                if(minR < 9):
                    fit_function = "gaus(0) + gaus(3)" if(nfound == 1) else "gaus(0) + gaus(3) + gaus(6)" if(nfound == 2) else "gaus(0) + gaus(3) + gaus(6) + gaus(9)"
                else:
                    fit_function = "gaus(0) + gaus(3)"

                fy2 = ROOT.TF1("fy2", str(fit_function), -0.3, 0.3)

                Slice_Title = "".join(["#splitline{", Title, "}{p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4)), "}"])

                if(minR < 9):
                    fy2.SetParameter(0, 0)
                    fy2.SetParLimits(0, 0, 0)
                    fy2.SetParameter(1, 0)
                    fy2.SetParLimits(1, 0, 0)
                    fy2.SetParameter(2, 0)
                    fy2.SetParLimits(2, 0, 0)
                else:
                    fy2.SetParameter(0, 0.85*hy2.GetBinContent(hy2.FindBin(mu)))
                    fy2.SetParLimits(0, 0.45*hy2.GetBinContent(hy2.FindBin(mu)), 1.2*hy2.GetBinContent(hy2.FindBin(mu)))
                    fy2.SetParameter(1, mu)
                    fy2.SetParLimits(1, mu - 0.005, mu +  0.005)
                    fy2.SetParameter(2, 0.1)
                    fy2.SetParLimits(2, 0.01, 0.3)
                if("gaus(3)" in fit_function):
                    fy2.SetParameter(3, 0)
                    fy2.SetParLimits(3, 0, 0)
                    fy2.SetParameter(4, 0)
                    fy2.SetParLimits(4, 0, 0)
                    fy2.SetParameter(5, 0)
                    fy2.SetParLimits(5, 0, 0)
                if("gaus(6)" in fit_function):
                    fy2.SetParameter(6, 0)
                    fy2.SetParLimits(6, 0, 0)
                    fy2.SetParameter(7, 0)
                    fy2.SetParLimits(7, 0, 0)
                    fy2.SetParameter(8, 0)
                    fy2.SetParLimits(8, 0, 0)
                if("gaus(10)" in fit_function):
                    fy2.SetParameter(9, 0)
                    fy2.SetParLimits(9, 0, 0)
                    fy2.SetParameter(10, 0)
                    fy2.SetParLimits(10, 0, 0)
                    fy2.SetParameter(11, 0)
                    fy2.SetParLimits(11, 0, 0)


                if(Slice_Title in ["#splitline{#splitline{Electron Only}{#color[2]{#splitline{#splitline{(Inbending) #Delta p_{El} vs p_{El}}{Correction: #font[22]{No Momentum Corrections}}}{#splitline{El Sector 4 -- #phi_{El} Bin:  (#phi_{El} > 5)}{Cut Applied: Calculated Exclusivity Cuts}}}}}{p_{el} Bin: 9.45 < p_{el} < 9.7}", "#splitline{#splitline{Electron Only}{#color[2]{#splitline{#splitline{(Inbending) #Delta p_{El} vs p_{El}}{Correction: #font[22]{No Momentum Corrections}}}{#splitline{El Sector 3 -- #phi_{El} Bin:  (#phi_{El} > 5)}{Cut Applied: Calculated Exclusivity Cuts}}}}}{p_{el} Bin: 9.45 < p_{el} < 9.7}", "#splitline{#splitline{Electron Only}{#color[2]{#splitline{#splitline{(Inbending) #Delta p_{El} vs p_{El}}{Correction: #font[22]{No Momentum Corrections}}}{#splitline{El Sector 3 -- #phi_{El} Bin:  (#phi_{El} < -5)}{Cut Applied: Calculated Exclusivity Cuts}}}}}{p_{el} Bin: 8.95 < p_{el} < 9.2}", "#splitline{#splitline{Electron Only}{#color[2]{#splitline{#splitline{(Inbending) #Delta p_{El} vs p_{El}}{Correction: #font[22]{No Momentum Corrections}}}{#splitline{El Sector 3}{Cut Applied: Calculated Exclusivity Cuts}}}}}{p_{el} Bin: 8.95 < p_{el} < 9.2}"]):
                    fy2.SetParameter(0, 0.85*hy2.GetBinContent(hy2.FindBin(mu)))
                    fy2.SetParLimits(0, 0.65*hy2.GetBinContent(hy2.FindBin(mu)), 1.15*hy2.GetBinContent(hy2.FindBin(mu)))
                    fy2.SetParameter(1, mu)
                    fy2.SetParLimits(1, mu, mu)
                    fy2.SetParameter(2, 0.1)
                    fy2.SetParLimits(2, 0.01, 0.3)


                # print("".join([color.BLUE, "NO PEAKS (0)", color.END]) if(nfound == 0) else nfound if(nfound < 3) else "".join([color.RED, "More than 2", color.END]))
                if(minR < 9):
                    num_test = 0
                    for peaks in spectrum.GetPositionX():
                        num_test += 1
                        # print("".join(["Peak ", str(num_test), " -> ", str(peaks)]))

                        if(num_test < nfound + 1):

                            current_constant = hy2.GetBinContent(hy2.FindBin(peaks))
                            fy2.SetParameter((3*num_test) - 3, 0.75*current_constant)
                            fy2.SetParLimits((3*num_test) - 3, 0.5*current_constant, 1.1*current_constant)
                            fy2.SetParameter((3*num_test) - 2, peaks)
                            fy2.SetParLimits((3*num_test) - 2, 0.95*peaks, 1.05*peaks)
                            fy2.SetParameter((3*num_test) - 1, 0.15)
                            fy2.SetParLimits((3*num_test) - 1, 0.001, 0.5)

                            if(abs(peaks) < abs(mu)):
                                # print("\nnew mu = " + str(peaks))
                                mu = peaks
                                fy2.SetRange(-0.05, 0.05)
                                hy2.Fit(fy2, "BRQ")
                                mu, sig = fy2.GetParameter((3*num_test) - 2), abs(fy2.GetParameter((3*num_test) - 1))
                                fy2.SetParameter((3*num_test) - 2, mu)
                                fy2.SetParLimits((3*num_test) - 2, 0.995*mu, 1.005*mu)
                                # fy2.SetParameter((3*num_test) - 1, sig)
                                # fy2.SetParLimits((3*num_test) - 1, 0.5*sig, 1.5*sig)
                            else:
                                fy2.SetRange(-0.3, 0.3)
                                hy2.Fit(fy2, "BRQ")
                                fy2.SetParameter((3*num_test) - 2, fy2.GetParameter((3*num_test) - 2))
                                fy2.SetParLimits((3*num_test) - 2, 0.95*fy2.GetParameter((3*num_test) - 2), 1.05*fy2.GetParameter((3*num_test) - 2))
                                # fy2.SetParameter((3*num_test) - 1, sig)
                                # fy2.SetParLimits((3*num_test) - 1, 0.5*sig, 1.5*sig)

                        if(num_test == nfound):
                            # print("break")
                            break

                    # print((spectrum.GetPositionX())[1])

                    fy2.SetRange(-0.3, 0.3)
                    if(nfound == 1):
                        fy2.SetParameter(3, 0.25*hy2.GetBinContent(hy2.GetMaximumBin()))
                        fy2.SetParLimits(3, 0, 0.65*hy2.GetBinContent(hy2.GetMaximumBin()))
                        fy2.SetParameter(4, mu)
                        fy2.SetParLimits(4, -0.3, 0.3)
                        fy2.SetParameter(5, 0.125)
                        fy2.SetParLimits(5, 0.05, 0.2)
                    if(nfound == 2):
                        fy2.SetParameter(6, 0.25*hy2.GetBinContent(hy2.GetMaximumBin()))
                        fy2.SetParLimits(6, 0, 0.65*hy2.GetBinContent(hy2.GetMaximumBin()))
                        fy2.SetParameter(7, mu)
                        fy2.SetParLimits(7, -0.3, 0.3)
                        fy2.SetParameter(8, 0.125)
                        fy2.SetParLimits(8, 0.05, 0.2)
                    if(nfound == 3):
                        fy2.SetParameter(9, 0.25*hy2.GetBinContent(hy2.GetMaximumBin()))
                        fy2.SetParLimits(9, 0, 0.65*hy2.GetBinContent(hy2.GetMaximumBin()))
                        fy2.SetParameter(10, mu)
                        fy2.SetParLimits(10, -0.3, 0.3)
                        fy2.SetParameter(11, 0.125)
                        fy2.SetParLimits(11, 0.05, 0.2)

                else:
                    fy2.SetRange(-0.05, 0.05)
                    hy2.Fit(fy2, "BRQ")
                    mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
                    fy2.SetRange(-0.3, 0.3)
                    fy2.SetParameter(4, mu)
                    fy2.SetParLimits(4, 0.999*mu, 1.001*mu)
                    fy2.SetParameter(5, sig)
                    fy2.SetParLimits(5, 0.999*sig, 1.001*sig)
                    fy2.SetParameter(3, 0.25*hy2.GetBinContent(hy2.GetMaximumBin()))
                    fy2.SetParLimits(3, 0, 0.65*hy2.GetBinContent(hy2.GetMaximumBin()))
                    fy2.SetParameter(4, 0)
                    fy2.SetParLimits(4, -0.3, 0.3)
                    fy2.SetParameter(5, 0.125)
                    fy2.SetParLimits(5, 0.05, 0.2)

                hy2.Fit(fy2, "BRQ")
                # hy2.Fit(fy2, "RQN")


                mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
                par_main_peak = 1
                if(minR < 9):
                    if("gaus(6)" in fit_function):
                        if(abs(mu) > abs(fy2.GetParameter(4))):
                            mu = fy2.GetParameter(4)
                            par_main_peak = 4
                    if("gaus(9)" in fit_function):
                        if(abs(mu) > abs(fy2.GetParameter(7))):
                            mu = fy2.GetParameter(7)
                            par_main_peak = 7


                if(minR > 8.4):
                    mu_max = hy2.GetBinCenter(hy2.GetMaximumBin())
                    mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
                    if("gaus(3)" in fit_function):
                        if(abs(mu_max - mu) > abs(mu_max - fy2.GetParameter(1))):
                            mu = fy2.GetParameter(1)
                            par_main_peak = 1
                    if("gaus(6)" in fit_function):
                        if(abs(mu_max - mu) > abs(mu_max - fy2.GetParameter(4))):
                            mu = fy2.GetParameter(4)
                            par_main_peak = 4
                    if("gaus(9)" in fit_function):
                        if(abs(mu_max - mu) > abs(mu_max - fy2.GetParameter(7))):
                            mu = fy2.GetParameter(7)
                            par_main_peak = 7

                if(Slice_Title in ["#splitline{#splitline{Electron Only}{#color[2]{#splitline{#splitline{(Inbending) #Delta p_{El} vs p_{El}}{Correction: #font[22]{No Momentum Corrections}}}{#splitline{El Sector 3 -- #phi_{El} Bin:  (#phi_{El} < -5)}{Cut Applied: Calculated Exclusivity Cuts}}}}}{p_{el} Bin: 8.95 < p_{el} < 9.2}", "#splitline{#splitline{Electron Only}{#color[2]{#splitline{#splitline{(Inbending) #Delta p_{El} vs p_{El}}{Correction: #font[22]{No Momentum Corrections}}}{#splitline{El Sector 3}{Cut Applied: Calculated Exclusivity Cuts}}}}}{p_{el} Bin: 8.95 < p_{el} < 9.2}"]):
                    # print(color.Error + "\nCHECKING ERRORS")
                    # print("TITLE:")
                    # print(Slice_Title)
                    # print("fit_function = " + str(fit_function))
                    # print("mu1 = " + str(fy2.GetParameter(1)))
                    # print("mu2 = " + str(fy2.GetParameter(4)))
                    # print("mu3 = " + str(fy2.GetParameter(7)))
                    # print("mu_max = " + str(hy2.GetBinCenter(hy2.GetMaximumBin())))
                    # print("par_main_peak = " + str(par_main_peak))
                    # print("\n" + color.END)
                    par_main_peak = 1

    #             mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
    #             par_main_peak = 1
    #             if("gaus(3)" in fit_function):
    #                 if(abs(mu) > abs(fy2.GetParameter(4))):
    #                     mu = fy2.GetParameter(4)
    #                     par_main_peak = 4
    #             if("gaus(7)" in fit_function):
    #                 if(abs(mu) > abs(fy2.GetParameter(7))):
    #                     mu = fy2.GetParameter(7)
    #                     par_main_peak = 7

    #             num_test = 0
    #             for peaks in spectrum.GetPositionX():
    #                 num_test += 1
    #                 if(abs(fy2.GetParameter((3*num_test) - 2)) < abs(mu)):
    #                     mu, sig = fy2.GetParameter((3*num_test) - 2), abs(fy2.GetParameter((3*num_test) - 1))
    #                 if(num_test > nfound):
    #                     break




                # # ERROR BAR OPTIONS:
                # Error_Option = "Stat" # This option uses the default errors given by the fits (i.e., Error_Bars = fy2.GetParError(1))
                Error_Option = "Set" # This option uses a user defined error for error bars (i.e., Error_Bars = Fit_Fixed_Error)
                # # This code will always default to fy2.GetParError(1) if it gives the largest error bars

                Slice_Title = "".join(["#splitline{", Title, "}{p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4)), "}"])

                hy2.SetTitle(Slice_Title)


                if(not D_Angle):
                    Fit_Fixed_Error = 0.01
                else:
                    Fit_Fixed_Error = 0.1

                # Statistical Error Bars
                Error_Bars = fy2.GetParError(par_main_peak)

                # Pre-Set Error Bars
                if(Error_Option == "Set"):
                    hy2.SetTitle(Slice_Title.replace("#DEl", "#Del"))
                    if(abs(fy2.GetParError(par_main_peak)) < Fit_Fixed_Error):
                        Error_Bars = Fit_Fixed_Error
                    else:
                        # print("The statistical error is too large for: " + str(hy2.GetTitle()))
                        Error_Bars = fy2.GetParError(par_main_peak)


                sigma_factor_upper = 1.25
                sigma_factor_lower = 1.25
                if(D_Angle == "Theta"):
                    sigma_factor_upper = 2
                    sigma_factor_lower = 2
                if(D_Angle and D_Angle != "Theta"):
                    sigma_factor_upper = 2
                    sigma_factor_lower = 2

                gr2.SetPoint(gr2.GetN(), minR+dR/2.0, fy2.GetParameter(par_main_peak))
                gr2.SetPointError(gr2.GetN()-1, dR/2.0, Error_Bars)

                gr2_sigma_up.SetPoint(gr2_sigma_up.GetN(), minR+dR/2.0, fy2.GetParameter(par_main_peak) + sigma_factor_upper*abs(fy2.GetParameter(par_main_peak + 1)))
                gr2_sigma_up.SetPointError(gr2_sigma_up.GetN()-1, dR/2.0, (Error_Bars**2 + (sigma_factor_upper*fy2.GetParError(par_main_peak + 1))**2)**(0.5))

                gr2_sigma_down.SetPoint(gr2_sigma_down.GetN(), minR+dR/2.0, fy2.GetParameter(par_main_peak) - (sigma_factor_lower*abs(fy2.GetParameter(par_main_peak + 1))))
                gr2_sigma_down.SetPointError(gr2_sigma_down.GetN()-1, dR/2.0, (Error_Bars**2 + (sigma_factor_lower*fy2.GetParError(par_main_peak + 1))**2)**(0.5))


                # Sigma_Widths.append([[Momentum_Min, Momentum_Max, Momentum_Center], [Upper_Width, Lower_Width]])
                Sigma_Widths.append([[minR, minR+dR, minR+dR/2.0], [fy2.GetParameter(par_main_peak) + sigma_factor_upper*abs(fy2.GetParameter(par_main_peak + 1)), fy2.GetParameter(par_main_peak) - (sigma_factor_lower*abs(fy2.GetParameter(par_main_peak + 1)))]])

                FindPeak_x.append(fy2.GetParameter(par_main_peak))
                FindPeak_y.append(hy2.GetBinContent(hy2.FindBin(fy2.GetParameter(par_main_peak))))

                FindPeak_Cut_Up.append(fy2.GetParameter(par_main_peak) + sigma_factor_upper*abs(fy2.GetParameter(par_main_peak + 1)))
                FindPeak_Cut_Down.append(fy2.GetParameter(par_main_peak) - sigma_factor_lower*abs(fy2.GetParameter(par_main_peak + 1)))


                minR += dR

                
        setattr(h2, "hys2", hys2)
        setattr(h2, "gr2", gr2)
        setattr(h2, "FindPeak_x", FindPeak_x)
        setattr(h2, "FindPeak_y", FindPeak_y)
        setattr(h2, "FindPeak_Cut_Up", FindPeak_Cut_Up)
        setattr(h2, "FindPeak_Cut_Down", FindPeak_Cut_Down)
        setattr(h2, "gr2_sigma_up", gr2_sigma_up)
        setattr(h2, "gr2_sigma_down", gr2_sigma_down)
        setattr(h2, "Sigma_Widths", Sigma_Widths)
        
        
        
        
        
################################################################################################################################################################################################################################################################################################################
### New Cell ###################################################################################################################################################################################################################################################################################################
################################################################################################################################################################################################################################################################################################################




def fit_Dp_2D_Out(h2, minR, maxR, dR, Title, BGq, Particle, Bending_Type="In", D_Angle=False, Cut_Q=True, Event_Type_In=event_type):
    if(("In" in str(Bending_Type)) or (D_Angle != False) or (Cut_Q != True)):
        fit_Dp_2D(h2, minR, maxR, dR, Title, BGq, Particle, D_Angle, Cut_Q, Event_Type_In=Event_Type_In)
    else:
        # print("Using Outbending Correction Fit Functions...\n")
        # fit_Dp_2D(h2, minR, maxR, dR, Title, BGq, Particle, D_Angle, Cut_Q)
        Sector_Title = "1" if("Sector 1" in str(Title)) else "2" if("Sector 2" in str(Title)) else "3" if("Sector 3" in str(Title)) else "4" if("Sector 4" in str(Title)) else "5" if("Sector 5" in str(Title)) else "6" if("Sector 6" in str(Title)) else "All"
        if("E" not in Event_Type_In or True):

            Use_Pre_Set = False # True

            hx = h2.ProjectionX()
            hys2, Sigma_Widths = [], []
            gr2, gr2_sigma_up, gr2_sigma_down = ROOT.TGraphErrors(), ROOT.TGraphErrors(), ROOT.TGraphErrors()
            gr2.SetMarkerStyle(20)
            gr2_sigma_up.SetMarkerStyle(20)
            gr2_sigma_down.SetMarkerStyle(20)

            FindPeak_x, FindPeak_y, FindPeak_Cut_Up, FindPeak_Cut_Down = [], [], [], []

            SB_ii = 0

            Point_by_point_Correction = not True
            
            if(Point_by_point_Correction):
                print("".join(["""
if(sec == """, str(Sector_Title), "):"]))

            peak_num = 0
            while(minR+dR <= maxR):

                ib0, ib1 = hx.FindBin(minR), hx.FindBin(minR+dR)

                hy2 = h2.ProjectionY(f"hy{ib1}", ib0, ib1)
                hy2.SetDirectory(0)

                if(Particle != "pro"):
                    hy2.Rebin()

                if(hy2.GetBinContent(hy2.FindBin(0)) < 100):
                    hy2.Rebin(2)
#                 if(hy2.GetBinContent(hy2.FindBin(0)) < 100):
#                     hy2.Rebin(2)
                # if(hy2.GetBinContent(hy2.FindBin(0)) < 50):
                #     hy2.Rebin(2)

                hys2.append(hy2)

                Slice_Title = "".join(["#splitline{", Title, "}{p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4)), "}"])
                Slice_Title = Slice_Title.replace("#DEl", "#Del")
                hy2.SetTitle(str(Slice_Title))

                spectrum = ROOT.TSpectrum(5, 2.5)
                nfound   = spectrum.Search(hy2, 2)

                # fit_function = "gaus(0) + gaus(3)"
                fit_function = "gaus(0) + pol1(3)"
                # fit_function = "gaus(0) + pol2(3)"
                
                if((Event_Type_In in ["EO"]) and (minR < 9.9)):
                    fit_function = "gaus(0) + pol2(3)"
                
                # min_FitR = -0.2 if(Event_Type_In not in ["SP", "EO"]) else -0.1 if(Event_Type_In not in ["EO"]) else (-0.075 if(minR < 9.9) else -0.09)
                # max_FitR =  0.2 if(Event_Type_In not in ["SP", "EO"]) else  0.1 if(Event_Type_In not in ["EO"]) else ( 0.075 if(minR < 9.9) else  0.09)
                min_FitR = -0.2 if(Event_Type_In not in ["SP", "EO"]) else -0.1 if(Event_Type_In not in ["EO"]) else (-0.12  if(minR < 9.6) else -0.12)
                max_FitR =  0.2 if(Event_Type_In not in ["SP", "EO"]) else  0.1 if(Event_Type_In not in ["EO"]) else ( 0.075 if(minR < 9.6) else  0.12)
                mu       = hy2.GetBinCenter(hy2.GetMaximumBin())
                
                if(mu < min_FitR or mu > max_FitR):
                    print("RESET:", Slice_Title)
                    mu = 0
                
                # if(Event_Type_In in ["DP"] and (mu < -0.2 or mu > 0.2)):
                #     # print("RESET")
                #     mu = 0
                # if(Event_Type_In in ["EO"] and (mu < -0.2 or mu > 0.1)):
                #     # print("RESET")
                #     mu = 0
                    

                # fy2 = ROOT.TF1("fy2", str(fit_function), mu - 0.05, mu + 0.05)
                fy2 = ROOT.TF1("fy2", str(fit_function), min_FitR, max_FitR)

                fy2.SetParameter(0, 0.85*hy2.GetBinContent(hy2.FindBin(mu)))
                fy2.SetParLimits(0, 0.65*hy2.GetBinContent(hy2.FindBin(mu)), 1.15*hy2.GetBinContent(hy2.FindBin(mu)))
                fy2.SetParameter(2, 0.15)
                fy2.SetParLimits(2, 0.01, 0.4)

                fy2.SetParName(0, "Constant")
                fy2.SetParName(1, "Mean")
                fy2.SetParName(2, "Sigma")

                if("gaus(3)" in str(fit_function)):
                    est_bg_peak = 0.09 # Estimated Background Peak (just guessing this value)
                    
                    fy2.SetParameter(3,    0.45*hy2.GetBinContent(hy2.FindBin(est_bg_peak)) if((0.45*hy2.GetBinContent(hy2.FindBin(est_bg_peak))) < (0.35*hy2.GetBinContent(hy2.FindBin(mu)))) else 0.15*hy2.GetBinContent(hy2.FindBin(mu)))
                    fy2.SetParLimits(3, 0, 0.35*hy2.GetBinContent(hy2.FindBin(mu)))
                    fy2.SetParameter(4, est_bg_peak)
                    fy2.SetParLimits(4, 0.005, 0.15)
                    fy2.SetParameter(5, 0.15)
                    fy2.SetParLimits(5, 0.005, 0.5)
                    fy2.SetParName(3, "Constant (BG)")
                    fy2.SetParName(4, "Mean (BG)")
                    fy2.SetParName(5, "Sigma (BG)")
                
                
                conditions_for_peak = [True]
                # conditions_for_peak = [False]

                if(True not in conditions_for_peak):
                    # print(color.RED, "Running Max", color.END)
                    fy2.SetParameter(1, mu)
                    fy2.SetParLimits(1, mu - 0.0025, mu + 0.0025)
                    fy2.SetRange(-0.15, 0.15)

                else:
                    # print(color.RED, "Running peaks", color.END)
                    num_test = 0
                    for peaks in spectrum.GetPositionX():
                        num_test += 1
                        current_constant = hy2.GetBinContent(hy2.FindBin(peaks))
                        fy2.SetParameter((3*num_test) - 3, 0.85*current_constant)
                        fy2.SetParLimits((3*num_test) - 3, 0.65*current_constant, 1.15*current_constant)
                        fy2.SetParameter((3*num_test) - 2, peaks)
                        fy2.SetParLimits((3*num_test) - 2, peaks - 0.005, peaks + 0.005)
                        fy2.SetParameter((3*num_test) - 1, 0.15)
                        fy2.SetParLimits((3*num_test) - 1, 0.01, 0.4)
                        break

                hy2.Fit(fy2, "BRQ")

                mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
                
                if(mu < 0 and (Event_Type_In in ["SP"])): # The following ranges typically work better for the peaks which are shifted in this direction
                    fy2.SetRange(-0.125, 0.075)
                    hy2.Fit(fy2, "BRQ")
                    mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
                # ReFit = ("'')" in str(h2.GetName()))
                if(mu > 0.045   and (Event_Type_In in ["EO"])):
                    fy2.SetRange(-0.05, 0.125)
                    hy2.Fit(fy2, "BRQ")
                    mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
                elif(mu < -0.05 and (Event_Type_In in ["EO"])):
                    fy2.SetRange(-0.15, 0.05)
                    hy2.Fit(fy2, "BRQ")
                    mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
                elif(Event_Type_In in ["EO"]):
                    fy2.SetRange(-0.15, 0.1 if(str(Sector_Title) not in ["5"]) else 0.08)
                    hy2.Fit(fy2, "BRQ")
                    mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
                    
                    
                if(not D_Angle):
                    Fit_Fixed_Error = 0.01
                else:
                    Fit_Fixed_Error = 0.1

                # Statistical Error Bars
                Error_Bars = fy2.GetParError(1)

                # Pre-Set Error Bars
                if(abs(fy2.GetParError(1)) < Fit_Fixed_Error):
                    Error_Bars = Fit_Fixed_Error
                else:
                    Error_Bars = fy2.GetParError(1)

                par_main_peak = 1

                sigma_factor_upper = 1.25
                sigma_factor_lower = 1.25

                gr2.SetPoint(gr2.GetN(),   minR+dR/2.0, fy2.GetParameter(par_main_peak))
                gr2.SetPointError(gr2.GetN()-1, dR/2.0, Error_Bars)

                gr2_sigma_up.SetPoint(gr2_sigma_up.GetN(),   minR+dR/2.0, fy2.GetParameter(par_main_peak) + sigma_factor_upper*abs(fy2.GetParameter(par_main_peak + 1)))
                gr2_sigma_up.SetPointError(gr2_sigma_up.GetN()-1, dR/2.0, (Error_Bars**2 + (sigma_factor_upper*fy2.GetParError(par_main_peak + 1))**2)**(0.5))

                gr2_sigma_down.SetPoint(gr2_sigma_down.GetN(),   minR+dR/2.0, fy2.GetParameter(par_main_peak) - (sigma_factor_lower*abs(fy2.GetParameter(par_main_peak + 1))))
                gr2_sigma_down.SetPointError(gr2_sigma_down.GetN()-1, dR/2.0, (Error_Bars**2 + (sigma_factor_lower*fy2.GetParError(par_main_peak + 1))**2)**(0.5))

                # Sigma_Widths.append([[Momentum_Min, Momentum_Max, Momentum_Center], [Upper_Width, Lower_Width]])
                Sigma_Widths.append([[minR, minR+dR, minR+dR/2.0], [fy2.GetParameter(par_main_peak) + sigma_factor_upper*abs(fy2.GetParameter(par_main_peak + 1)), fy2.GetParameter(par_main_peak) - (sigma_factor_lower*abs(fy2.GetParameter(par_main_peak + 1)))]])

                FindPeak_x.append(fy2.GetParameter(par_main_peak))
                FindPeak_y.append(hy2.GetBinContent(hy2.FindBin(fy2.GetParameter(par_main_peak))))

                FindPeak_Cut_Up.append(fy2.GetParameter(par_main_peak)   + sigma_factor_upper*abs(fy2.GetParameter(par_main_peak + 1)))
                FindPeak_Cut_Down.append(fy2.GetParameter(par_main_peak) - sigma_factor_lower*abs(fy2.GetParameter(par_main_peak + 1)))


                if(Point_by_point_Correction):
#                     print("".join(["""    if(""", str(print_rounded_str(minR, rounding=5)), " < pp && pp < ", str(print_rounded_str(minR + dR, rounding=5)), """){
#         dp = dp + (""", str(print_rounded_str(mu, rounding=5)),""");
#     }"""]))
                    print("".join(["""    if(""", str(print_rounded_str(minR, rounding=5)), " < pp and pp < ", str(print_rounded_str(minR + dR, rounding=5)), """):
        dp = dp + (""", str(print_rounded_str(mu, rounding=5)), ")"]))

                minR += dR

            if(Point_by_point_Correction):
                print("".join(["""
}
"""]))


            setattr(h2, "hys2", hys2)
            setattr(h2, "gr2",  gr2)
            setattr(h2, "FindPeak_x",     FindPeak_x)
            setattr(h2, "FindPeak_y",     FindPeak_y)
            setattr(h2, "FindPeak_Cut_Up",   FindPeak_Cut_Up)
            setattr(h2, "FindPeak_Cut_Down", FindPeak_Cut_Down)
            setattr(h2, "gr2_sigma_up",   gr2_sigma_up)
            setattr(h2, "gr2_sigma_down", gr2_sigma_down)
            setattr(h2, "Sigma_Widths",   Sigma_Widths)

        else:


            hx = h2.ProjectionX()
            hys2, Sigma_Widths = [], []
            gr2, gr2_sigma_up, gr2_sigma_down = ROOT.TGraphErrors(), ROOT.TGraphErrors(), ROOT.TGraphErrors()
            gr2.SetMarkerStyle(20)
            gr2_sigma_up.SetMarkerStyle(20)
            gr2_sigma_down.SetMarkerStyle(20)

            FindPeak_x, FindPeak_y, FindPeak_Cut_Up, FindPeak_Cut_Down = [], [], [], []

            SB_ii = 0

#             if("El Sector 3" in Title and "(#phi_{El} > 5)" in Title):
#                 dR = 2*dR
#                 minR = maxR - 2*dR
#                 print("\nDoubling size of the bin (manual fix to problematic fit)\n")

            while(minR+dR <= maxR):
                ib0, ib1 = hx.FindBin(minR), hx.FindBin(minR+dR)

                hy2 = h2.ProjectionY(f"hy{ib1}", ib0, ib1)
                hy2.SetDirectory(0)

                if(minR < 9.2):
                    hy2.Rebin()

                hys2.append(hy2)

                mu = hy2.GetBinCenter(hy2.GetMaximumBin())

                hy2.SetTitle("".join(["#splitline{", Title, "}{p_{", Particle, "} Bin: ", str(round(minR, 4)), " < p_{", Particle, "} < ", str(round(minR + dR, 4)), "}"]))

                spectrum = ROOT.TSpectrum(5, 2.5)
                nfound = spectrum.Search(hy2, 2)

                fit_function = "gaus(0) + gaus(3)"

                fy2 = ROOT.TF1("fy2", str(fit_function), mu - 0.04, mu + 0.04)

                Slice_Title = "".join(["#splitline{", Title, "}{p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4)), "}"])

                fy2.SetParameter(0, 0.85*hy2.GetBinContent(hy2.FindBin(mu)))
                fy2.SetParLimits(0, 0.65*hy2.GetBinContent(hy2.FindBin(mu)), 1.15*hy2.GetBinContent(hy2.FindBin(mu)))
                fy2.SetParameter(2, 0.1)
                fy2.SetParLimits(2, 0.01, 0.3)


                Condition_For_NOT_GetPositionX = (("El Sector 3" in Title and str(round(minR + dR, 4)) == "9.7" and ("(#phi_{El} < -5)" in Title or "(#phi_{El} > 5)" in Title)) or ("El Sector 4" in Title and "(#phi_{El} > 5)" in Title))
                # Condition_For_NOT_GetPositionX = ((minR > 9) and ("El Sector 3" in Title and str(round(minR + dR, 4)) == "9.7" and ("(#phi_{El} < -5)" in Title or "(#phi_{El} > 5)" in Title)) or ("El Sector 4" in Title and "(#phi_{El} > 5)" in Title))
                if(Condition_For_NOT_GetPositionX or ("El Sector 1" in Slice_Title and "8.7" in Slice_Title and "8.95" in Slice_Title)):
                    fy2.SetParameter(1, mu)
                    fy2.SetParLimits(1, mu - 0.0025, mu + 0.0025)
                else:
                    num_test = 0
                    for peaks in spectrum.GetPositionX():
                        num_test += 1
                        current_constant = hy2.GetBinContent(hy2.FindBin(peaks))
                        fy2.SetParameter((3*num_test) - 3, 0.85*current_constant)
                        fy2.SetParLimits((3*num_test) - 3, 0.65*current_constant, 1.15*current_constant)
                        fy2.SetParameter((3*num_test) - 2, peaks)
                        fy2.SetParLimits((3*num_test) - 2, peaks - 0.0025, peaks + 0.0025)
                        fy2.SetParameter((3*num_test) - 1, 0.1)
                        fy2.SetParLimits((3*num_test) - 1, 0.01, 0.3)
                        fy2.SetRange(peaks - 0.04, peaks + 0.04)
                        break

                hy2.Fit(fy2, "BRQ")

                mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))

                hy2.SetTitle(Slice_Title)

                if(not D_Angle):
                    Fit_Fixed_Error = 0.01
                else:
                    Fit_Fixed_Error = 0.1

                # Statistical Error Bars
                Error_Bars = fy2.GetParError(1)

                # Pre-Set Error Bars
                hy2.SetTitle(Slice_Title.replace("#DEl", "#Del"))
                if(abs(fy2.GetParError(1)) < Fit_Fixed_Error):
                    Error_Bars = Fit_Fixed_Error
                else:
                    Error_Bars = fy2.GetParError(1)

                par_main_peak = 1

                sigma_factor_upper = 1.25
                sigma_factor_lower = 1.25

                gr2.SetPoint(gr2.GetN(), minR+dR/2.0, fy2.GetParameter(par_main_peak))
                gr2.SetPointError(gr2.GetN()-1, dR/2.0, Error_Bars)

                gr2_sigma_up.SetPoint(gr2_sigma_up.GetN(), minR+dR/2.0, fy2.GetParameter(par_main_peak) + sigma_factor_upper*abs(fy2.GetParameter(par_main_peak + 1)))
                gr2_sigma_up.SetPointError(gr2_sigma_up.GetN()-1, dR/2.0, (Error_Bars**2 + (sigma_factor_upper*fy2.GetParError(par_main_peak + 1))**2)**(0.5))

                gr2_sigma_down.SetPoint(gr2_sigma_down.GetN(), minR+dR/2.0, fy2.GetParameter(par_main_peak) - (sigma_factor_lower*abs(fy2.GetParameter(par_main_peak + 1))))
                gr2_sigma_down.SetPointError(gr2_sigma_down.GetN()-1, dR/2.0, (Error_Bars**2 + (sigma_factor_lower*fy2.GetParError(par_main_peak + 1))**2)**(0.5))


                # Sigma_Widths.append([[Momentum_Min, Momentum_Max, Momentum_Center], [Upper_Width, Lower_Width]])
                Sigma_Widths.append([[minR, minR+dR, minR+dR/2.0], [fy2.GetParameter(par_main_peak) + sigma_factor_upper*abs(fy2.GetParameter(par_main_peak + 1)), fy2.GetParameter(par_main_peak) - (sigma_factor_lower*abs(fy2.GetParameter(par_main_peak + 1)))]])

                FindPeak_x.append(fy2.GetParameter(par_main_peak))
                FindPeak_y.append(hy2.GetBinContent(hy2.FindBin(fy2.GetParameter(par_main_peak))))

                FindPeak_Cut_Up.append(fy2.GetParameter(par_main_peak) + sigma_factor_upper*abs(fy2.GetParameter(par_main_peak + 1)))
                FindPeak_Cut_Down.append(fy2.GetParameter(par_main_peak) - sigma_factor_lower*abs(fy2.GetParameter(par_main_peak + 1)))


                minR += dR

            setattr(h2, "hys2", hys2)
            setattr(h2, "gr2",  gr2)
            setattr(h2, "FindPeak_x",     FindPeak_x)
            setattr(h2, "FindPeak_y",     FindPeak_y)
            setattr(h2, "FindPeak_Cut_Up",   FindPeak_Cut_Up)
            setattr(h2, "FindPeak_Cut_Down", FindPeak_Cut_Down)
            setattr(h2, "gr2_sigma_up",   gr2_sigma_up)
            setattr(h2, "gr2_sigma_down", gr2_sigma_down)
            setattr(h2, "Sigma_Widths",   Sigma_Widths)
            
            
            
            
            
            
            
            
            
            
##################################################################################################################
#####==========#####==========######################################################==========#####==========#####
#####==========#####==========#####     Fits for Invariant Mass Histograms     #####==========#####==========#####
#####==========#####==========######################################################==========#####==========#####
##################################################################################################################


# Meaning of below: h2 is the 2D histogram to be sliced and fit; minR/maxR is the starting/ending point of the slice range, and dR is the increments of increase between each slice (for p_e, fit range should be minR=2, maxR=8, and dR=1)
def fit_WM_2D(h2, minR, maxR, dR, Title, BGq, Particle, Cut_Q=False):

    hx = h2.ProjectionX()
    hys2, Sigma_Widths = [], []
    gr2, gr2_Sigma, gr2_Cut_Range_Up, gr2_Cut_Range_Down = ROOT.TGraphErrors(), ROOT.TGraphErrors(), ROOT.TGraphErrors(), ROOT.TGraphErrors()
    gr2_V2 = ROOT.TGraphAsymmErrors()
    gr2.SetMarkerStyle(20)
    gr2_V2.SetMarkerStyle(20)
    gr2_Sigma.SetMarkerStyle(20)
    gr2_Cut_Range_Up.SetMarkerStyle(20)
    gr2_Cut_Range_Down.SetMarkerStyle(20)    
    
    FindPeak_x, FindPeak_y, FindPeak_Cut_Up, FindPeak_Cut_Down = [], [], [], []
    FindCut_Upper, FindCut_Lower = [], []

    while minR+dR <= maxR:
        ib0, ib1 = hx.FindBin(minR), hx.FindBin(minR+dR)

        hy2 = h2.ProjectionY(f"hy{ib1}", ib0, ib1)
        hy2.SetDirectory(0)

#         if(minR < 8.9):
#             hy2.Rebin()
        
        Slice_Title = "".join(["#splitline{", Title, "}{p_{", Particle.replace("pip", "#pi^{+}"), "} Bin: ", str(round(minR, 4)), " < p_{", Particle.replace("pip", "#pi^{+}"), "} < ", str(round(minR + dR, 4)), "}"])
        hy2.SetTitle(Slice_Title)

        hys2.append(hy2)

        mu           = hy2.GetBinCenter(hy2.GetMaximumBin())
        bin_width_mu = hy2.GetBinWidth(hy2.FindBin(mu))
        
        if(mu < 0.8 or mu > 1.0):
            mu = 0.9383
            # print("".join(["\nCheck: ", color.BBLUE, str(Slice_Title), color.END, "\nMax bin centered at: ", str(hy2.GetBinCenter(hy2.GetMaximumBin())), "\n"]))
            bin_width_mu = 1.5*hy2.GetBinWidth(hy2.FindBin(mu))

        
        spectrum = ROOT.TSpectrum(5, 2.5)
        nfound = spectrum.Search(hy2, 2)

        if(minR > 9 and minR > 9.5):
            fit_function = "gaus(0) + gaus(3)"
#             fy2 = ROOT.TF1("fy2", str(fit_function), mu - 2*0.038, mu + 2*0.038)
            fy2 = ROOT.TF1("fy2", str(fit_function), mu - 3.5*bin_width_mu, mu + 3.5*bin_width_mu)
    
            fy2.SetParameter(3, 0.45*hy2.GetBinContent(hy2.FindBin(1.15)))
            fy2.SetParLimits(3, 0.05*hy2.GetBinContent(hy2.FindBin(1.15)), 1.05*hy2.GetBinContent(hy2.FindBin(1.15)))
            fy2.SetParameter(4, 1.15)
            fy2.SetParLimits(4, 1.0, 1.3)
            fy2.SetParameter(5, 0.1)
            fy2.SetParLimits(5, 0.01, 0.3)
            
            fy2.SetParName(3, "Constant (BG)")
            fy2.SetParName(4, "Mean (BG)")
            fy2.SetParName(5, "Sigma (BG)")
    
        else:
            fit_function = "gaus(0) + pol2(3)"
#             fy2 = ROOT.TF1("fy2", str(fit_function), mu - 2.5*bin_width_mu, mu + 2.5*bin_width_mu)
            fy2 = ROOT.TF1("fy2", str(fit_function), mu - 3.5*bin_width_mu, mu + 3.5*bin_width_mu)
            # print(bin_width_mu)


        fy2.SetParameter(0, 0.85*hy2.GetBinContent(hy2.FindBin(mu)))
        fy2.SetParLimits(0, 0.65*hy2.GetBinContent(hy2.FindBin(mu)), 1.15*hy2.GetBinContent(hy2.FindBin(mu)))
        fy2.SetParameter(2, 0.1)
        fy2.SetParLimits(2, 0.01, 0.3)

        fy2.SetParName(0, "Constant")
        fy2.SetParName(1, "Mean")
        fy2.SetParName(2, "Sigma")
        
        # if("Sector 5" in Slice_Title and "9.2" in Slice_Title):
        # if(True):
        # if(minR < 8.9):
        if(False):
            fy2.SetParameter(1, mu)
            fy2.SetParLimits(1, mu - 1.0*bin_width_mu, mu + 1.0*bin_width_mu)
        else:
            num_test = 0
            for peaks in spectrum.GetPositionX():
                # if(minR < 9 and peaks > 1.1):
                if(peaks > 1.1):
                    continue
                    # print(Slice_Title)
                    # print(peaks)
                    # print("\n")
                num_test += 1
                current_constant = hy2.GetBinContent(hy2.FindBin(peaks))
                fy2.SetParameter((3*num_test) - 3, 0.85*current_constant)
                fy2.SetParLimits((3*num_test) - 3, 0.65*current_constant, 1.15*current_constant)
                fy2.SetParameter((3*num_test) - 2, peaks)
                fy2.SetParLimits((3*num_test) - 2, peaks - 2*0.0025, peaks + 2*0.0025)
                fy2.SetParameter((3*num_test) - 1, 0.1)
                fy2.SetParLimits((3*num_test) - 1, 0.01, 0.3)
#                 fy2.SetRange(peaks - 2*0.038, peaks + 2*0.038)
                fy2.SetRange(peaks - 4*0.038, (peaks + 6*0.038) if(minR > 9.9) else (peaks + 8*0.038))
                break

        hy2.Fit(fy2, "BRQ")

        mu, sig = fy2.GetParameter(1), abs(fy2.GetParameter(2))
            
        sigma_factor = 3
        sigma_factor_up = 1.75 if("Cut Applied:" not in Title) else 1.85
        
        sigma_factor_up   = 3
        sigma_factor_down = 2
        
        sigma_factor_up   = 2
        sigma_factor_down = 2
        
        if("Pass" in str(Title)):
            # print("INCREASING SIG FACTORS...")
            sigma_factor_up   = 2
            sigma_factor_up   = 1.75
            sigma_factor_down = 3
            sigma_factor_down = 2
            sigma_factor_down = 3
            # if(minR < 9.5):
            sigma_factor_up   = 1.45
        
        WM_Peak, SIG = fy2.GetParameter(1), abs(fy2.GetParameter(2))

        gr2.SetPoint(gr2.GetN(),             minR+dR/2.0, WM_Peak)
        gr2_V2.SetPoint(gr2_V2.GetN(),       minR+dR/2.0, WM_Peak)
        
        gr2_Sigma.SetPoint(gr2_Sigma.GetN(), minR+dR/2.0, SIG)
        
        gr2_Cut_Range_Up.SetPoint(gr2_Cut_Range_Up.GetN(),     minR+dR/2.0, WM_Peak + sigma_factor_up*(SIG))
        gr2_Cut_Range_Down.SetPoint(gr2_Cut_Range_Down.GetN(), minR+dR/2.0, WM_Peak - sigma_factor_down*(SIG))
            
        Error_of_WM_Peak = fy2.GetParError(1)
        Error_of_SIG     = fy2.GetParError(2)
        
        gr2.SetPointError(gr2.GetN() - 1,             dR/2.0, Error_of_WM_Peak)
        gr2_V2.SetPointError(gr2_V2.GetN() - 1,       dR/2.0, Error_of_WM_Peak + sigma_factor_down*(SIG + Error_of_SIG), Error_of_WM_Peak + sigma_factor_up*(SIG + Error_of_SIG))
        
        gr2_Sigma.SetPointError(gr2_Sigma.GetN() - 1, dR/2.0, Error_of_SIG)
        
        gr2_Cut_Range_Up.SetPointError(gr2_Cut_Range_Up.GetN() - 1,     dR/2.0, ((Error_of_WM_Peak)**2 + (sigma_factor_up*(Error_of_SIG))**2)**0.5)
        gr2_Cut_Range_Down.SetPointError(gr2_Cut_Range_Down.GetN() - 1, dR/2.0, ((Error_of_WM_Peak)**2 + (sigma_factor_down*(Error_of_SIG))**2)**0.5)
        
        FindPeak_x.append(WM_Peak)
        FindPeak_y.append(hy2.GetBinContent(hy2.FindBin(WM_Peak)))
        
        # Sigma_Widths.append([[Momentum_Min, Momentum_Max, Momentum_Center], [Upper_Width, Lower_Width]])
        Sigma_Widths.append([[minR, minR+dR, minR+dR/2.0], [WM_Peak + sigma_factor_up*(SIG), WM_Peak - sigma_factor_down*(SIG)]])
        

        # Find the bin number corresponding to 2 standard deviations from the mean
        bin_range = int((SIG*sigma_factor_up)/(hy2.GetBinWidth(1)))
        # Find the bin number at which to start searching for the minimum
        startbin  = hy2.FindBin(WM_Peak) + 1
        # Find the bin number at which to stop searching for the minimum
        stopbin   = hy2.FindBin(WM_Peak) + bin_range
        # Find the local minima after the peak within the specified range

        # initialize minimum value and corresponding bin index
        min_val = float('inf')
        min_bin = -1
        # loop over bins within the desired range and find the minimum value
        for test_bin in range(startbin, stopbin+1):
            val = hy2.GetBinContent(test_bin)
            if(val < min_val):
                min_val = val
                min_bin = test_bin

        up_cut_min = hy2.GetBinCenter(min_bin)
#         print("Minimum value:", min_val)
#         print("\nLocal minima after the peak (start at peak): ", up_cut_min)
    
        # initialize minimum value and corresponding bin index
        min_val = hy2.GetBinContent(stopbin)
        min_bin = stopbin
        # loop over bins within the desired range and find the minimum value
        for test_bin in range(stopbin, startbin, -1):
            val      = hy2.GetBinContent(test_bin)
            val_next = hy2.GetBinContent(test_bin-1)
            if(val_next < val):
                min_val = val_next
                min_bin = test_bin-1
            else:
                break
        
        up_cut_min = hy2.GetBinCenter(min_bin)
        # print("Local minima after the peak (for p =", (minR+dR/2.0), "): ", up_cut_min)
        
        FindPeak_Cut_Up.append(up_cut_min)
        # FindPeak_Cut_Up.append(WM_Peak   + sigma_factor_up*(SIG))
        FindPeak_Cut_Down.append(WM_Peak - sigma_factor_down*(SIG))
        
        FindCut_Upper.append([WM_Peak    + sigma_factor_up*(SIG),   hy2.GetBinContent(hy2.FindBin(WM_Peak + sigma_factor_up*(SIG)))])
        FindCut_Lower.append([WM_Peak    - sigma_factor_down*(SIG), hy2.GetBinContent(hy2.FindBin(WM_Peak - sigma_factor_down*(SIG)))])
        
        
#         params = fy2.GetParameters()
#         # Create the fit equation string
#         eqn_str = "err"
#         if(fit_function == "gaus(0) + pol2(3)"):
#             eqn_str  =    f"({params[0]:.2f})*exp(-0.5*pow((x - ({params[1]:.2f}))/({params[2]:.2f}), 2))"
#             eqn_str += f" + ({params[3]:.2f}) + ({params[4]:.2f})*x + ({params[5]:.2f})*x*x"
#         elif(fit_function == "gaus(0) + gaus(3)"):
#             eqn_str  =    f"({params[0]:.2f})*exp(-0.5*pow((x - ({params[1]:.2f}))/({params[2]:.2f}), 2))"
#             eqn_str += f" + ({params[3]:.2f})*exp(-0.5*pow((x - ({params[4]:.2f}))/({params[5]:.2f}), 2))"

# #         eqn_str = fit_function.replace("gaus(0)", f"Gaussian({params[1]:.2f}, {params[2]:.2f})", 1)
# #         eqn_str = eqn_str.replace("pol2(3)",    f"Background({params[3]:.2f}, {params[4]:.2f}, {params[5]:.2f})", 1)
#         # Print the fit equation
#         print("Fit equation: ", eqn_str)
        
        minR += dR
 
    setattr(h2, "hys2", hys2)
    setattr(h2, "gr2",  gr2)
    setattr(h2, "gr2_V2",    gr2_V2)
    setattr(h2, "gr2_Sigma", gr2_Sigma)
    setattr(h2, "gr2_Cut_Range_Up",   gr2_Cut_Range_Up)
    setattr(h2, "gr2_Cut_Range_Down", gr2_Cut_Range_Down)
    setattr(h2, "FindPeak_x", FindPeak_x)
    setattr(h2, "FindPeak_y", FindPeak_y)
    setattr(h2, "FindPeak_Cut_Up",   FindPeak_Cut_Up)
    setattr(h2, "FindPeak_Cut_Down", FindPeak_Cut_Down)
    setattr(h2, "Sigma_Widths", Sigma_Widths)
    setattr(h2, "FindCut_Upper",  FindCut_Upper)
    setattr(h2, "FindCut_Lower",  FindCut_Lower)
    
    return h2

            
            
            
            
            
            
            
            
            

            
            
            
            
            
            
            
            
            
            
################################################################################################################################
#####==========#####==========####################################################################==========#####==========#####
#####==========#####==========#####     Parameters for Slices - Fitting_Lines() Function     #####==========#####==========#####
#####==========#####==========####################################################################==========#####==========#####
################################################################################################################################
# Determines the momentum ranges of the plots made by this code

def Fitting_Lines(Histo_Type, Event_Type, Bending_Type, Particle, Missing_Mass_Type="None", DataSet="Fall2018", Sector=1):
    if("hmmCPARTall" in Histo_Type and Missing_Mass_Type == "None"):
        # print("".join([color.RED, "Missing Mass Type not specified... (Defaulting to ", "eppi0X" if(Event_Type == "ES") else "eppipX" if(Event_Type == "DP") else "epipX", ")", color.END]))
        Missing_Mass_Type = "eppi0X" if(Event_Type == "ES") else "eppipX" if(Event_Type == "DP") else "epipX"
        
    MinRange_Fit, MaxRange_Fit, Increment_Fit = 5.95, 9.95, 1
    TLine_X1, TLine_Y1, TLine_X2, TLine_Y2 = (MinRange_Fit - 2*Increment_Fit), 0, (MaxRange_Fit + 2*Increment_Fit), 0
    if(Event_Type == "ES"):
        if(Particle == "el"):
            if(Bending_Type == "Inbending"):
                MinRange_Fit, MaxRange_Fit, Increment_Fit = 5.45, 9.95, 0.5
            else:
                MinRange_Fit, MaxRange_Fit, Increment_Fit = 5.95, 9.95, 1
        if(Particle == "pro"):
            if(Bending_Type == "Inbending"):
                MinRange_Fit, MaxRange_Fit, Increment_Fit = 6.5,  10.4, 0.65
            else:
                MinRange_Fit, MaxRange_Fit, Increment_Fit = 6.5,  10.4, 0.65
    elif(Event_Type == "EO"):
        if(Particle == "el"):
            if(Bending_Type == "Inbending"):
                # MinRange_Fit, MaxRange_Fit, Increment_Fit = 5.45, 9.95, 0.25
                # MinRange_Fit, MaxRange_Fit, Increment_Fit = 8.2, 9.95, 0.25
                # MinRange_Fit, MaxRange_Fit, Increment_Fit = 8.45, 9.7, 0.25
                MinRange_Fit, MaxRange_Fit, Increment_Fit = 9.2, 9.7, 0.25
                if("Fall2018_Pass2" in str(DataSet)):
                    MinRange_Fit, MaxRange_Fit, Increment_Fit = 8.0, 9.8, 0.36
            else:
                MinRange_Fit, MaxRange_Fit, Increment_Fit = 5.95, 9.95, 1
                MinRange_Fit, MaxRange_Fit, Increment_Fit = 9.2,   9.7, 0.25
                MinRange_Fit, MaxRange_Fit, Increment_Fit = 9.2,  10.2, 0.25
                MinRange_Fit, MaxRange_Fit, Increment_Fit = 9.2,  10.2, 0.25#0.125
#                 MinRange_Fit, MaxRange_Fit, Increment_Fit = 6.2,  10.2, 0.5 # 0.25
                MinRange_Fit, MaxRange_Fit, Increment_Fit = 9.2,  10.2, 0.5
                MinRange_Fit, MaxRange_Fit, Increment_Fit = 8.2,  10.2, 0.5
                Increment_Fit = 1
#                 MinRange_Fit += 2*Increment_Fit
                if("Fall2018_Pass2" in str(DataSet)):
                    MinRange_Fit, MaxRange_Fit, Increment_Fit = 8.2,  10.2, 0.5
                    # Increment_Fit = 1.0
                    # MinRange_Fit += Increment_Fit
        if(Particle == "pro"):
            if(Bending_Type == "Inbending"):
                MinRange_Fit, MaxRange_Fit, Increment_Fit = 6.5, 10.4, 0.65
            else:
                MinRange_Fit, MaxRange_Fit, Increment_Fit = 6.5, 10.4, 0.65
    else:
        if(Particle == "el"):
            MinRange_Fit  = 2   if(Event_Type == "SP") else (3 if(Event_Type == "DP") else 4)
            MaxRange_Fit  = 9.5 if(Event_Type == "SP") else 8
            Increment_Fit = 0.5 if(Event_Type == "SP") else 1
            
            if(("Fall2018_Pass2" in str(DataSet)) or ("Monte_Carlo_Pass2" in str(DataSet))):
                MinRange_Fit  = 1.95
                MaxRange_Fit  = 9.45
                Increment_Fit = 0.5
                
                
            if("Fall2018" in DataSet and "Central" in DataSet):
                # print("\n\nCENTRAL\n\n")
                MinRange_Fit  = 8.25
                MaxRange_Fit  = 9.75
                Increment_Fit = 0.25
                
                MinRange_Fit +=  Increment_Fit
                # MaxRange_Fit += -Increment_Fit
            
#             if(("Out" in Bending_Type) and (Event_Type in ["SP"])):
#                 MinRange_Fit  = 2.5
            
        if(Particle == "pro"):
            # MinRange_Fit = 0.45 if(Event_Type == "DP") else 0.35
            # MaxRange_Fit = 2.95 if(Event_Type == "DP") else 2.35
            MinRange_Fit = 0.45 if(Event_Type == "DP") else 0.45
#             MaxRange_Fit = 1.5 if(Event_Type == "DP") else 2.7 # 2.45
            MaxRange_Fit = 3.25 if(Event_Type == "DP") else 2.45 # 2.7 # 2.45
            MaxRange_Fit = 3.25 if(Event_Type == "DP") else 1.25 # 2.45 # 2.7 # 2.45
#             MaxRange_Fit = 3 if(Event_Type == "DP") else 1
#             MaxRange_Fit = 3.4 if(Event_Type == "DP") else 2.7 # 2.45
            MaxRange_Fit = 3.0 if(Event_Type == "DP") else 1.25 # 2.45 # 2.7 # 2.45
            MinRange_Fit = 0.45
            MaxRange_Fit = 3.0
            Increment_Fit = 0.25
            Increment_Fit = 0.05
            Increment_Fit = 0.1
        if(Particle in ["pip", "pim"]):
            MinRange_Fit  = 0.75 if(Event_Type == "SP") else 0.5
            MaxRange_Fit  = 7.25 if(Event_Type == "SP") else 5.5
#             if(DataSet != "Fall2018"):
#                 # MaxRange_Fit  = 4
#                 MinRange_Fit  = 4
            Increment_Fit = 0.5  if(Event_Type == "SP") else 1
            if(("Out" in Bending_Type) and (Event_Type in ["SP"])):
                MinRange_Fit  = 0.75
                # Increment_Fit = 1
                
            if(Sector > 6 or ("Fall2018" in DataSet and "Central" in DataSet)):
                # print("\n\nCENTRAL\n\n")
                MinRange_Fit  = 0.25
                MaxRange_Fit  = 2.25
                Increment_Fit = 0.25
            
            if("Fall2018_Pass2" in str(DataSet)):
                MinRange_Fit  = 0.3
                MaxRange_Fit  = 8.3
                Increment_Fit = 0.5
                
            if("Monte_Carlo_Pass2" in str(DataSet)):
                MinRange_Fit  = 0.3
                MaxRange_Fit  = 4.3
                Increment_Fit = 0.5
                

    if(("Fall2018" not in DataSet) and ("Monte_Carlo" not in DataSet)):
        if(Particle == "el"):
            MinRange_Fit  = 2     # if("SP" in str(Event_Type)) else (3 if(Event_Type == "DP") else 4)
            MinRange_Fit  = 2   if("SP" in str(Event_Type)) else 8    if("EO" in str(Event_Type)) else 3
            # MaxRange_Fit  = 7.7   if("SP" in str(Event_Type)) else 8
            # MaxRange_Fit  = 9.125 if("SP" in str(Event_Type)) else 9.5  if("EO" in str(Event_Type)) else 8
            # Increment_Fit = 0.475 if("SP" in str(Event_Type)) else 0.25 if("EO" in str(Event_Type)) else 1
            MaxRange_Fit  = 9   if("SP" in str(Event_Type)) else 9.5  if("EO" in str(Event_Type)) else 8
            Increment_Fit = 0.5 if("SP" in str(Event_Type)) else 0.5  if("EO" in str(Event_Type)) else 1

            
            
    if("Monte_Carlo_Pass2" in str(DataSet)):
        if(Particle == "el"):
            MinRange_Fit, MaxRange_Fit, Increment_Fit = 5.8, 8.20, 0.4
            MinRange_Fit, MaxRange_Fit, Increment_Fit = 5.9, 8.15, 0.2
    
    TLine_X1, TLine_Y1, TLine_X2, TLine_Y2 = (MinRange_Fit - 2*Increment_Fit), 0, (MaxRange_Fit + 2*Increment_Fit), 0
    
    if("Dmom_p" in Histo_Type):
        TLine_X1, TLine_Y1, TLine_X2, TLine_Y2 = (MinRange_Fit - 2*Increment_Fit), 0, (MaxRange_Fit + 2*Increment_Fit), 0
    if("Dmom_Angle_Histo" in Histo_Type):
        TLine_X1, TLine_Y1, TLine_X2, TLine_Y2 = (MinRange_Fit - 1*Increment_Fit), (180 if("D_Angle_V3" not in Histo_Type) else 0), (MaxRange_Fit + 2.5*Increment_Fit), (180 if("D_Angle_V3" not in Histo_Type) else 0)
    if("hmmCPARTall" in Histo_Type):
        if(Event_Type == "SP" and DataSet in ["Fall2018", "Monte_Carlo"]):
            MinRange_Fit  = 2.5 if(Particle == "el") else 0.75
            MaxRange_Fit  = 9.5 if(Particle == "el") else 7.25
            Increment_Fit = 1   if(Particle == "el") else 0.5
            if("In" not in Bending_Type):
                MinRange_Fit  = 2   if(Particle == "el") else 0.75 # 0.25 # 0.75
                Increment_Fit = 0.5 # if(Particle == "el") else 1
        TLine_X1 = MinRange_Fit - 0.5*Increment_Fit
        TLine_X2 = MaxRange_Fit + 0.5*Increment_Fit
        TLine_Y1, TLine_Y2 = 0, 0
        if(Event_Type == "SP"):
            TLine_Y1, TLine_Y2 = 0.9396, 0.9396                                                
        elif(Event_Type == "DP"):
            TLine_Y1, TLine_Y2 = 0.13957*0.13957, 0.13957*0.13957
        elif(Event_Type == "P0"):
            TLine_Y1, TLine_Y2 = 0.13498*0.13498, 0.13498*0.13498
        # if((Missing_Mass_Type == "epipX") or (Event_Type == "SP")):
        #     TLine_Y1, TLine_Y2 = 0.9396, 0.9396                                                
        # elif((Missing_Mass_Type == "eppipX") or (Event_Type == "DP")):
        #     TLine_Y1, TLine_Y2 = 0.13957*0.13957, 0.13957*0.13957
        # elif((Missing_Mass_Type == "eppi0X") or (Event_Type == "P0")):
        #     TLine_Y1, TLine_Y2 = 0.13498*0.13498, 0.13498*0.13498
    if("HWC_Histo_All" in Histo_Type):
        if("Fall2018_Pass2" not in str(DataSet)):
            if("E" in Event_Type):
                while(MinRange_Fit > 8.2):
                    MinRange_Fit += -Increment_Fit
        TLine_X1 = 3 if(Particle == "el") else 0
        TLine_X2 = (10.5 if(Particle == "el") else 9 if(Particle == "pro") else 12) - 0.5
        TLine_Y1, TLine_Y2 = 0.9383, 0.9383
        
    if(TLine_X1 < 0):
        TLine_X1 = 0
        
    Fit_Parameters  = [MinRange_Fit, MaxRange_Fit, Increment_Fit]
    Line_Parameters = [TLine_X1, TLine_Y1, TLine_X2, TLine_Y2]

    return [Fit_Parameters, Line_Parameters]
