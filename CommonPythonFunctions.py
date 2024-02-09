class color:
    CYAN      = '\033[96m'
    PURPLE    = '\033[95m'
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