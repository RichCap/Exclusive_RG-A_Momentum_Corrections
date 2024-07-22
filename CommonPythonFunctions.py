import ROOT

class color:
    CYAN      = '\033[96m'
    PURPLE    = '\033[95m'
    PINK      = '\033[35m'
    BLUE      = '\033[94m'
    YELLOW    = '\033[93m'
    GREEN     = '\033[92m'
    RED       = '\033[91m'
    DARKCYAN  = '\033[36m'
    BOLD      = '\033[1m'
    LIGHT     = '\033[2m'
    ITALIC    = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK     = '\033[5m'
    DELTA     = '\u0394' # symbol
    END       = '\033[0m'
    ERROR     = '\033[91m\033[1m' # Combines RED and BOLD
    Error     = '\033[91m\033[1m' # Same as ERROR
    BBLUE     = '\033[1m\033[94m' # Combines BLUE and BOLD
    BGREEN    = '\033[1m\033[92m' # Combines GREEN and BOLD
    END_B     = '\033[0m\033[1m'  # Combines END and BOLD
    END_R     = '\033[0m\033[91m' # Combines END and RED
    
class color_bg:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'
    END     = '\033[0m'
    
    
class root_color:
    # Colors
    White   = 0
    Black   = 1
    Red     = 2
    Green   = 3
    Blue    = 4
    Yellow  = 5
    Pink    = 6
    Cyan    = 7
    DGreen  = 8 # Dark Green
    Purple  = 9
    DGrey   = 13
    Grey    = 15
    LGrey   = 17
    Brown   = 28
    Teal    = 30
    Gold    = 41
    Rust    = 46
    
    # Fonts
    Bold    = '#font[22]'
    Italic  = '#font[12]'
    
    # Symbols
    Delta   = '#Delta'
    Phi     = '#phi'
    π       = '#pi'
    Degrees = '#circ'
    
    Line    = '#splitline'
    
    
    
##==============================================================================================##
##==========##==========##     Function for Correction Title Names      ##==========##==========##
##==============================================================================================##

def corNameTitles(CorrectionNameIn, Form="Default", EVENT_TYPE="SP", BENDING_TYPE="In"):
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
        CorrectionName1 = 'El Cor (Quad - Linear Phi - Refined 1)'.replace('Linear', 'Linear' if("In" in BENDING_TYPE) else 'Quad')
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
    if('mmfaP2'   in CorrectionNameIn):
        CorrectionName1 = 'El Cor (Quad - Quad Phi - Fa18 - Pass 2)'

    if(EVENT_TYPE in ["EO"]):
        if(CorrectionNameIn == "mm0"):
            CorrectionName = "No Momentum Corrections"
        else:
            CorrectionName = CorrectionName1
        return CorrectionName

    if('Pip' not in CorrectionNameIn):
        CorrectionName2 = 'No Pi+ Cor' if(EVENT_TYPE not in ["P0"]) else ""
    if('Pip' in CorrectionNameIn):
        if('MM0'       in CorrectionNameIn):
            CorrectionName2 = 'No Pi+ Cor'
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
        if('MMsP2'     in CorrectionNameIn):
            CorrectionName2 = 'Pi+ Cor (Quad - Pass 2 - Split)'
        if('MMfaP2'    in CorrectionNameIn):
            CorrectionName2 = 'Pi+ Cor (Quad - Fa18 - Pass 2)'
        if("ELPipMM"   in CorrectionNameIn):
            CorrectionName2 = "".join(["Pi+ Energy Loss Cor - ", str(str(CorrectionName2).replace("Pi+ Cor", "Pi+ Mom Cor"))])

    if('Pim' not in CorrectionNameIn):
        CorrectionName3 = 'No Pi- Cor' if(EVENT_TYPE in ["DP"]) else ""
    if('Pim' in CorrectionNameIn):
        if('MMpimPhi'   in CorrectionNameIn):
            CorrectionName3 = 'Pi- Cor (Linear - Linear Phi)'
        if('MMpim_qPhi' in CorrectionNameIn):
            CorrectionName3 = 'Pi- Cor (Quad - Quad Phi)'
        if('MMpim_F'    in CorrectionNameIn):
            CorrectionName3 = 'Pi- Cor (Quad - Quad Phi - Rounded)'

    if('Pro' not in CorrectionNameIn):
        CorrectionName4 = 'No Pro Cor' if(EVENT_TYPE not in ["SP", "MC"]) else ""
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

    if(CorrectionName2 == 'Error' and EVENT_TYPE not in ["P0", "ES"]):
        print("".join(["Error with the Pi+ Pion Correction in CorrectionNameInput = ", str(CorrectionNameIn)]))
        CorrectionName2 = "Pi+ Cor (ERROR)"

    if(CorrectionName3 == 'Error' and EVENT_TYPE not in ["SP", "MC", "P0", "ES"]):
        print("".join(["Error with the Pi- Pion Correction in CorrectionNameInput = ", str(CorrectionNameIn)]))
        CorrectionName3 = "Pi- Cor (ERROR)"

    if(CorrectionName4 == 'Error' and EVENT_TYPE not in ["SP", "MC"]):
        print("".join(["Error with the Proton Correction in CorrectionNameInput = ", str(CorrectionNameIn)]))
        CorrectionName4 = "Pro Cor (ERROR)"

    CorrectionName = "".join([CorrectionName1, " - " if(CorrectionName2 != "") else "", CorrectionName2, " - " if(CorrectionName3 != "") else "", CorrectionName3, " - " if(CorrectionName4 != "") else "", CorrectionName4])

    if(EVENT_TYPE in ["SP", "MC"]):
        CorrectionName = "".join([CorrectionName1, " - " if(CorrectionName2 != "") else "", CorrectionName2])
    elif(EVENT_TYPE != "ES"):
        CorrectionName = "".join([CorrectionName1, " - " if(CorrectionName2 != "") else "", CorrectionName2, " - " if(CorrectionName3 != "") else "", CorrectionName3, " - " if(CorrectionName4 != "") else "", CorrectionName4])
    else:
        CorrectionName = "".join([CorrectionName1, " - " if(CorrectionName4 != "") else "", CorrectionName4])


    if(CorrectionName1 == 'El Cor (Quad - Quad Phi)' and CorrectionName2 == 'Pi+ Cor (Quad - Quad Phi)'):
        if(EVENT_TYPE in ["SP", "MC"]):
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

    if(EVENT_TYPE not in ["SP", "MC"]):
        if("Energy Loss Cor" not in CorrectionName and '_NoELC' not in CorrectionNameIn):
            CorrectionName = CorrectionName.replace('Pro Cor (Quad - Quad Phi)', 'Pro Cor (Quad - Quad Phi - Energy Loss Cor)')

    CorrectionName = CorrectionName.replace('- No Pi- Cor ', "")

    if(CorrectionNameIn in ["mm0", "mm0_NoELC"]):
        CorrectionName = "".join(["No Momentum Corrections", " (Energy Loss Cor)" if(EVENT_TYPE not in ["SP", "MC"] and (("NoELC" not in CorrectionNameIn) or ("MC" in event_Name))) else ""])

    if(("ELPipMM" in CorrectionNameIn) and ("Pi+ Energy Loss Cor" not in CorrectionName)):
        CorrectionName = "".join([CorrectionName, " - Pi+ Energy Loss Cor"])

    if(Form != "Default"):
        if("No Momentum Corrections" not in CorrectionName and CorrectionName != 'El/Pi+ Cor (Quad - Quad Phi)'):
            if(EVENT_TYPE in ["SP", "MC"]):
                CorrectionName = "".join(["#splitline{", str(CorrectionName1), "}{", str(CorrectionName2), "}"])
            if("E" in EVENT_TYPE or EVENT_TYPE == "P0"):
                CorrectionName = "".join(["#splitline{", str(CorrectionName1), "}{", str(CorrectionName4), "}"])
            if(EVENT_TYPE == "DP"):
                CorrectionName = "".join(["#splitline{#splitline{", str(CorrectionName1), "}{", str(CorrectionName2), "}}{", "".join(["#splitline{", str(CorrectionName3), "}{", str(CorrectionName4), "}"]) if(str(CorrectionName3) not in ["No Pi- Cor", "", "Error"]) else str(CorrectionName4), "}"])
                if(CorrectionName1 == 'El Cor (Quad - Quad Phi)' and CorrectionName2 == 'Pi+ Cor (Quad - Quad Phi)'):
                    CorrectionName = "".join(["#splitline{El/Pi+ Cor (Quad - Quad Phi)}{", "".join(["#splitline{", str(CorrectionName3), "}{", str(CorrectionName4), "}"]) if(str(CorrectionName3) not in ["No Pi- Cor", "", "Error"]) else str(CorrectionName4), "}"])
                if(CorrectionName1 == 'El Cor (Quad - Quad Phi - Energy Loss Cor)' and CorrectionName2 == 'Pi+ Cor (Quad - Quad Phi - Energy Loss Cor)'):
                    CorrectionName = "".join(["#splitline{El/Pi+ Cor (Quad - Quad Phi - Energy Loss Cor)}{", "".join(["#splitline{", str(CorrectionName3), "}{", str(CorrectionName4), "}"]) if(str(CorrectionName3) not in ["No Pi- Cor", "", "Error"]) else str(CorrectionName4), "}"])

    if("Test" in CorrectionNameIn):
        CorrectionName = "".join(["" if("mm0" in CorrectionNameIn) else "".join(["(", str(str(CorrectionNameIn).replace("_Test_M", "")).replace("_Test_P", ""), ") "]), "Test Proton Correction (", "Adding 20 MeV" if("Test_P" in CorrectionNameIn) else "Subtracting 20 MeV" if("Test_M" in CorrectionNameIn) else "Error", " - Energy Loss Cor)" if(EVENT_TYPE not in ["SP", "MC"] and "NoELC" not in CorrectionNameIn) else ")"])

    return CorrectionName



    ##===================================================================================================##
    ##==========##==========##     Function for Correction Title Names (End)     ##==========##==========##
    ##===================================================================================================##
    
    
    
    
    
##########################################################################################################
##==========##==========##     From: Momentum_Corrections_Github_Main.ipynb     ##==========##==========##
##########################################################################################################
    
    ##==========================================================================================##
    ##==========##==========##        General Use Functions/Code        ##==========##==========##
    ##==========================================================================================##
    
def Canvas_Create(Name="test", Num_Columns=3, Num_Rows=2, Size_X=600, Size_Y=800, cd_Space=0):
    canvas_test = ROOT.TCanvas(str(Name), str(Name), Size_X, Size_Y)
    canvas_test.Divide(Num_Columns, Num_Rows, cd_Space, cd_Space)
    canvas_test.SetGrid()
    ROOT.gStyle.SetAxisColor(16, 'xy')
    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetOptFit(1)
    return canvas_test


def plot_colors(Region, Correction="Corrected", OutPut_Q="All"):
    reg_color    = root_color.Black    if(Region in ["regall", "reg1", "Center"]) else root_color.Red  if(Region in ["reg2", "Negative"]) else root_color.Green if(Region in ["reg3", "Positive"]) else "error"
    line_style   = 1
    marker_style = 8
    if(Correction in ["mm0", "No Correction", "Uncorrected"]):
        reg_color    = root_color.Grey if(Region in ["regall", "reg1", "Center"]) else root_color.Rust if(Region in ["reg2", "Negative"]) else root_color.DGreen if(Region in ["reg3", "Positive"]) else "error"
        line_style   = 9
        marker_style = 1
    if(reg_color == "error"):
        print(f"{color.RED}\nColor Error\n{color.END}")
        reg_color = root_color.Black
    if(OutPut_Q == "All"):
        return [reg_color, line_style, marker_style]
    elif("color"  in OutPut_Q or "Color"  in OutPut_Q):
        return reg_color
    elif("line"   in OutPut_Q or "Line"   in OutPut_Q):
        return line_style
    elif("marker" in OutPut_Q or "Marker" in OutPut_Q):
        return marker_style
    else:
        print(f"{color.RED}\nOutput Error?\n{str(OutPut_Q)}\n{color.END}")
        return [reg_color, line_style, marker_style]
        
    
def palette_move(canvas, histo, x_left, x_right, y_up, y_down):
        palette_test = 0
        canvas.Modified()
        canvas.Update()
        while(palette_test < 4 and palette_test != -1):
            try:
                palette_histo = histo.GetListOfFunctions().FindObject("palette")
                palette_histo.SetX1NDC(0.905 + x_left)
                palette_histo.SetX2NDC(0.925 + x_right)
                palette_histo.SetY1NDC(0.1 + y_down)
                palette_histo.SetY2NDC(0.9 + y_up)
                canvas.Modified()
                canvas.Update()
                palette_test = -1
            except:
                palette_test += 1
        if(palette_test > 0):
            print("\nFailed to move palette...")
              
    
def Draw_Canvas(canvas, cd_num=1, left_add=0, right_add=0, up_add=0, down_add=0):
    canvas.cd(cd_num)
    canvas.cd(cd_num).SetLeftMargin(0.05 + left_add)
    canvas.cd(cd_num).SetRightMargin(0.05 + right_add)
    canvas.cd(cd_num).SetTopMargin(0.1 + up_add)
    canvas.cd(cd_num).SetBottomMargin(0.1 + down_add)
    
    
def statbox_move(Histogram, Canvas, Default_Stat_Obj, Sector=1, Print_Method="norm", Y1_add=0, Y2_add=0, X1_add=0, X2_add=0):
    finding, search = 0, 0
    Canvas.Modified()
    Canvas.Update()
    while(finding == 0 and search < 5):
        if(Default_Stat_Obj == ""):
            Default_Stat_Obj = Histogram.GetListOfFunctions().FindObject("stats")
        if("TPaveStats" not in str(type(Default_Stat_Obj))):
            try:
                Default_Stat_Obj = Histogram.GetListOfFunctions().FindObject("stats")# Default_Stat_Obj.FindObject("stats")
            except Exception as e:
                print(color.RED + str(e) + color.END)
        try:
            if(Print_Method == "DP_1D"):                
                Default_Stat_Obj.SetY1NDC(0.12)
                Default_Stat_Obj.SetY2NDC(0.45)
                Default_Stat_Obj.SetX1NDC(0.12)
                Default_Stat_Obj.SetX2NDC(0.43)
            if(Print_Method == "MM_1D"):
                Default_Stat_Obj.SetY1NDC(0.12)
                Default_Stat_Obj.SetY2NDC(0.45)
                Default_Stat_Obj.SetX1NDC(0.12)
                Default_Stat_Obj.SetX2NDC(0.43)
            if(Print_Method == "off"):
                Default_Stat_Obj.SetY1NDC(0)
                Default_Stat_Obj.SetY2NDC(0)
                Default_Stat_Obj.SetX1NDC(0)
                Default_Stat_Obj.SetX2NDC(0)
            if(Print_Method == "norm"):
                Default_Stat_Obj.SetY1NDC(0.05 + Y1_add)
                Default_Stat_Obj.SetY2NDC(0.25 + Y2_add)
                Default_Stat_Obj.SetX1NDC(0.15 + X1_add)
                Default_Stat_Obj.SetX2NDC(0.45 + X2_add)
            if(Print_Method == "ver"):
                Default_Stat_Obj.SetY1NDC(0.05 + Y1_add)
                Default_Stat_Obj.SetY2NDC(0.25 + Y2_add)
                if(Sector != -1):
                    if(Sector > 4):
                        Default_Stat_Obj.SetY1NDC(0.15 + Y1_add)
                        Default_Stat_Obj.SetY2NDC(0.25 + Y2_add)
                    if(Sector%2 == 0):
                        Default_Stat_Obj.SetX1NDC(0.05 + X1_add)
                        Default_Stat_Obj.SetX2NDC(0.35 + X2_add)
                    else:
                        Default_Stat_Obj.SetX1NDC(0.15 + X1_add)
                        Default_Stat_Obj.SetX2NDC(0.45 + X2_add)
            if(Print_Method == "hor"):
                Default_Stat_Obj.SetY1NDC(0.05 + Y1_add)
                Default_Stat_Obj.SetY2NDC(0.25 + Y2_add)
                if(Sector != -1):
                    if(Sector > 3):
                        Default_Stat_Obj.SetY1NDC(0.15 + Y1_add)
                        Default_Stat_Obj.SetY2NDC(0.35 + Y2_add)
                    if(Sector != 1 and Sector != 4):
                        Default_Stat_Obj.SetX1NDC(0.05 + X1_add)
                        Default_Stat_Obj.SetX2NDC(0.35 + X2_add)
                    else:
                        Default_Stat_Obj.SetX1NDC(0.15 + X1_add)
                        Default_Stat_Obj.SetX2NDC(0.45 + X2_add)
            Default_Stat_Obj.Draw("same")
            Canvas.Modified()
            Canvas.Update()
            finding += 1
        except Exception as e:
            Canvas.Modified()
            Canvas.Update()
            if(search > 2):
                print(f"{color.RED}Search is Failing... ({str(search)}){color.END}\nError: {str(e)}")
                fail
            finding = 0
            search += 1
    if(search > 4):
        print("Failed search")
        

def print_rounded_str(number=0, rounding=0):
    try:
        if(rounding != 0 and abs(number) >= 0.001):
            output = round(number, rounding)
            output = "".join(["{:.", str(rounding), "}"]).format(float(number))
            # print("round")
        elif(rounding != 0):
            output = "".join(["{:.", str(rounding-1), "e}"]).format(float(number))
            # print("science")
        else:
            # print("other")
            output = number
            
        return output
    
    except Exception as e:
        print("".join([color.Error, "Error: number = ", str(output), " is not accepted", " --> failed to round input..." if(rounding != 0) else "", "\nERROR Output Is: \n", str(e), "\nTraceback: ", str(traceback.format_exc()), color.END]))
        return number
    
    ##==========================================================================================##
    ##==========##==========##     General Use Functions/Code (End)     ##==========##==========##
    ##==========================================================================================##
    
    