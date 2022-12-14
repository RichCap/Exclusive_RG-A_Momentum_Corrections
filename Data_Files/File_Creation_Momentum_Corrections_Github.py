import ROOT, numpy
import array
from datetime import datetime

from sys import argv
# Let there be 4 arguements in argv when running this code

# Arguement 1: Name of this code (File_Creation_Momentum_Corrections_Github.py)

# Arguement 2: data-type (In/Out)
    # Options: 
    # 1) In -> Inbending
    # 2) Out -> Outbending

# Arguement 3: event-type (type of exclusive events)
    # Options: 
    # 1) SP -> Single Pion (i.e., ep->eπ+N)
    # 2) DP -> Double Pion (i.e., ep->epπ+π-)
    # 3) P0 -> Pi0 Channel (i.e., ep->epπ0)

# Arguement 4: file number (Full file name)
    # If the file number is given as 'All', then all files will be run instead of a select number of them
    # If the file number is given as 'test', then the code will run without saving any of the histograms

# EXAMPLES: 
    # python File_Creation_Momentum_Corrections_Github.py In SP All
        # The line above would run ALL INBENDING files together for the ep->eπ+N channel
    # python File_Creation_Momentum_Corrections_Github.py Out DP test
        # The line above would test-run the OUTBENDING files for the ep->epπ+π- channel (no results would be saved)

code_name, datatype, event_type, file_location = argv

datatype, file_location, event_type = ''.join([str(datatype), "bending"]), str(file_location), str(event_type)

file_name = str(file_location)

if(datatype == "Outbending"):
    file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/shrestha/clas12momcorr/data/outbending/ePipX/", ""))
    file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/kenjo/ntuple_epippimp/inb/lvl1_eppimpip.skim4_00", ""))
    file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/outb/epPipPim.outb.qa.nSidis_00", ""))
    file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/kenjo/", ""))
    file_name = str(file_name.replace(".hipo.epip.root", ""))
    file_name = str(file_name.replace(".hipo.root", ""))
    file_name = str(file_name.replace("/u/home/richcap/", ""))
    file_name = str(file_name.replace("qa.", ""))
    file_name = str(file_name.replace("exclusiveselection.root", "Ex_Select"))

    
if(datatype == "Inbending"):
    file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/shrestha/clas12momcorr/data/inbending/ePipX/epip.", ""))
    file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/kenjo/ntuple_epippimp/inb/lvl1_eppimpip.skim4_00", ""))
    file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/inb/epPipPim.inb.qa.nSidis_00", ""))
    file_name = str(file_name.replace(".epippimp", ""))
    file_name = str(file_name.replace("/lustre19/expphy/volatile/clas12/kenjo/", ""))
    file_name = str(file_name.replace(".hipo.root", ""))
    file_name = str(file_name.replace(".root", ""))
    file_name = str(file_name.replace("/u/home/richcap/", ""))
    file_name = str(file_name.replace("qa.", ""))
    file_name = str(file_name.replace("exclusiveselection.root", "Ex_Select"))
    
    
    
file_name = str(file_name.replace("".join(["/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Double_Pion_Channel_eppippim/", str(datatype), "/"]), ""))
    

    
    
ROOT.gStyle.SetTitleOffset(1.3,'y')
ROOT.gStyle.SetGridColor(17)
ROOT.gStyle.SetPadGridX(1)
ROOT.gStyle.SetPadGridY(1)


event_Name = "error"

if(event_type == "SP"):
    event_Name = "Single Pion Channel"
    MM_type = "epipX"
if(event_type == "DP"):
    event_Name = "Double Pion Channel"
    # # Missing Mass Choice:
    # MM_type = "eppippim"
    MM_type = "eppipX"
    # MM_type = "eppimX"
    # MM_type = "epippimX"
    
if(event_type == "P0"):
    event_Name = "Pi0 Channel"
    MM_type = "eppi0X"

    
if(MM_type == "epippimX"):
    Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max = 160, 0, 1
elif(MM_type == "epipX"):
    Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max = 200, 0.5, 1.2
else:
    Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max = 160, -0.5, 0.5

if(event_Name != "error"):
    
    print("".join(["\n\033[1mStarting ", str(event_Name), " ", str(datatype), " ", str(MM_type), "...\033[0m"]))

    # These lines are left over from older versions of the code. Do not change or remove them without editing all other parts of code that reference them.
    CutChoice = 'none'


    ##################################################################################
    ##=====##=====##=====##     Choices for Initial Set-Up     ##=====##=====##=====##
    ##################################################################################

    # See_Num_of_Events_Q = 'y'
    See_Num_of_Events_Q = 'n'


    # Run (any) Delta P Histograms? (Use Delta_P_histo_Q to set answer)
#     Delta_P_histo_Q = 'n'
    Delta_P_histo_Q = 'y'

    Delta_Pel_histo_Q, Delta_Pip_histo_Q, Delta_Pim_histo_Q, Delta_Pro_histo_Q = 'n', 'n', 'n', 'n'

    if(Delta_P_histo_Q == 'y'):
        # Run ∆P (Electron) Histograms? (Use Delta_Pel_histo_Q to set answer)
        Delta_Pel_histo_Q = 'y'
        
        # Run ∆P (Pi+ Pion) Histograms? (Use Delta_Pip_histo_Q to set answer)
        Delta_Pip_histo_Q = 'y'
        
        # Run ∆P (Pi- Pion) Histograms? (Use Delta_Pim_histo_Q to set answer)
#         Delta_Pim_histo_Q = 'y'
        
        # Run ∆P (Proton) Histograms? (Use Delta_Pro_histo_Q to set answer)
        Delta_Pro_histo_Q = 'y'

    else:
        Delta_Pel_histo_Q, Delta_Pip_histo_Q, Delta_Pim_histo_Q, Delta_Pro_histo_Q = 'n', 'n', 'n', 'n'
        
        
    if(event_type == "SP"):
        Delta_Pim_histo_Q, Delta_Pro_histo_Q = 'n', 'n'
    if(event_type == "DP"):
        Delta_Pel_histo_Q, Delta_Pip_histo_Q = 'n', 'n'
    if(event_type == "P0"):
        Delta_Pel_histo_Q, Delta_Pim_histo_Q, Delta_Pip_histo_Q = 'n', 'n', 'n'

        
    if(Delta_P_histo_Q != 'n'):
        if(Delta_Pel_histo_Q != 'n'):
            print("Running with ∆P (el) histograms.")
        if(Delta_Pip_histo_Q != 'n'):
            print("Running with ∆P (π+) histograms.")
        if(Delta_Pim_histo_Q != 'n'):
            print("Running with ∆P (π-) histograms.")
        if(Delta_Pro_histo_Q != 'n'):
            print("Running with ∆P (pro) histograms.")
    else:
        print("\033[1mNOT running ∆P histograms.\033[0m")


    # Print rdf information? (Letting CheckDataFrameQ = 'y' will print out every variable name available for plotting within the dataframe)
    # Option does not affect the histograms that can/will be made. Purely provides user with more information while coding
    # CheckDataFrameQ = 'y'
    CheckDataFrameQ = 'n'




    ########################################################################################
    ##=====##=====##=====##     Choices for Initial Set-Up (End)     ##=====##=====##=====##
    ########################################################################################








    ##########################################################################
    ##=====##=====##=====##     Choices for Saving     ##=====##=====##=====##
    ##########################################################################
    SaveResultsQ = 'yes'
    # SaveResultsQ = 'no'

    if(file_location == "Test" or file_location == "test"):
        SaveResultsQ = 'no'

    if(SaveResultsQ == 'no'):
        print("\033[1mNot saving results...\033[0m")


# # #     Extra_Part_of_Name = ''
# #     Extra_Part_of_Name = '_V2'
# #     # V2 -> Updated electron corrections based on mmF_PipMMF
    
#     Extra_Part_of_Name = '_V3'
#     # V3 -> Updated electron corrections based on mmF_PipMMF (from V2)

    Extra_Part_of_Name = '_VF'
    # VF -> Fixed version (with the actual corrections - undid above versions)
    
    Extra_Part_of_Name = '_VF2'
    # VF2 -> Fixed version (refined with the actual corrections - i.e., VF)
    
    Extra_Part_of_Name = '_VF3'
    # VF3 -> Refined with VF2
    
    Extra_Part_of_Name = '_VF4'
    # VF4 -> Refinements VF2-VF3 did not work for any sector except for esec = 3
    
    Extra_Part_of_Name = ''
    # Starting over naming (for pi0 channel)
    
    Extra_Part_of_Name = '_V1'
    # Starting over naming from V1 (for DP channel)
    
    Extra_Part_of_Name = '_V2'
    # DP refined proton from V1 (also fixed angular shift)
    
    
    Extra_Part_of_Name = '_V1'
    # DP No proton corrections (yet) for outbending data
    
    Extra_Part_of_Name = '_VF3'
    # VF3 -> Turned off extra electron corrections in outbending files
    
    Extra_Part_of_Name = '_VF4'
    # VF4 -> Turned off extra π+ corrections in outbending files and added 2 new corrections to El sec 4 and 5 based on the pre-rounding final corrections (SP)
    
    
    Extra_Part_of_Name = '_V2'
    # DP New proton corrections for outbending data (made with different electron corrections)

    
    Extra_Part_of_Name = '_VFinal'
    # Turned off the last of the old inbending mmF refinements. Also changed exclusive cuts in SP to include phi bins. Also turned these cuts on for the phase space histograms
    
    Extra_Part_of_Name = '_VFinal2'
    # refined from VFinal
    
    
    Extra_Part_of_Name = '_VFinal_SP'
    
    Extra_Part_of_Name = '_VFinal_SP2'
    # Pi+ refinements needed for the inbending channel
    
    Extra_Part_of_Name = '_VFinal_SP3'
    # Another Pi+ refinements needed for the inbending channel
    
    Extra_Part_of_Name = '_VFinal_SP4'
    # Another Pi+ refinements needed for the inbending channel
    
    Extra_Part_of_Name = '_VFinal_SP5'
    # Yet another Pi+ refinements needed for the inbending channel
    
    
    Extra_Part_of_Name = '_VFinal_SP6'
    # No change to the corrections, just testing to see if there are changes
    # Updated how the code runs (Might fix bugs if present)
    
    
    Extra_Part_of_Name = '_VFinal_SP7'
    # Refined Pi+ (MMF) Corrections using the uncombined (PipMMqPhi_R5) correction and removed prior corrections from VFinal_SP
    # Updated how the code runs (Might fix bugs if present)
    
    
    

    
    
    
    if("Out" in datatype):
        Extra_Part_of_Name = '_VFinal_SP2'
        # New electron corrections for the outbending files
        
        Extra_Part_of_Name = '_VFinal_SP3'
        # Removed the last (New) electron corrections for the outbending files --> Did not work as well on π+ side
        # Also updated how the code runs (Might fix bugs if present)
        
        Extra_Part_of_Name = '_VFinal_SP4'
        # Refined electron based on VFinal_SP3

        Extra_Part_of_Name = '_VFinal_SP5'
        # Refined π+ pion based on VFinal_SP4
        
        Extra_Part_of_Name = '_VFinal_SP6'
        # Refined electron based on VFinal_SP5
        # Also updated the exclusivity cuts (may have changed slightly due to either a change to the fitting procedure or due to the dataframe fixes made in the version '_VFinal_SP3' above)
        # Also removed the MM option to see only the electron correction (i.e., removed 'mmF' from correctionList due to it not being used in analysis)
        
        Extra_Part_of_Name = '_VFinal_SP7'
        # Refined π+ pion based on VFinal_SP6
        
        
        
        
        
    if(event_type == "SP"):
        Extra_Part_of_Name = '_VFinal_SP8'
        # Final Versions of the Single Pion Histograms
        # Corrections are all applied in their final forms (for the collaboration meeting)
        # True for both Inbending AND Outbending files
        
        
    
    if(event_type != "SP"):
        Extra_Part_of_Name = '_VFinal_SP_DP1'
        # Proton Corrections (ready for outbending)
        # For the Inbending channel, there are already proton corrections but the π+/electron corrections have been updated (but not fully tested as of VFinal_SP5)
        
        Extra_Part_of_Name = '_VFinal_SP_DP2'
        # Refined Proton corrections from _VFinal_SP_DP1 (Inbending)
        
        Extra_Part_of_Name = '_VFinal_SP_DP3'
        # Another refinement of the Proton corrections from _VFinal_SP_DP2 (Inbending)
        
        Extra_Part_of_Name = '_VFinal_SP_V1_Pro'
        # Uses the final version of the Electron AND π+ Pion Corrections and existing Proton corrections (not updated with the new electron/π+ corrections)
        # Proton corrections can now be combined from both the double pion and π0 channels
        # (Error in running the double pion channel caused old proton corrections to be used - did not run the correct version of this code for the double pion channel)
        
        
        Extra_Part_of_Name = '_VFinal_SP_V2_Pro'
        # Updated the proton corrections using both the double pion and the π0 channel
        # Using a non-phi dependent correction/refinement
        
        Extra_Part_of_Name = '_VFinal_SP_V3_Pro'
        # Updated the proton corrections using both the double pion and the π0 channel
        # Using a non-phi dependent correction/refinement
        # Corrections are based on most recent inbending corrections
        # Updated the exclusivity cuts
        
        Extra_Part_of_Name = '_VFinal_SP_V4_Pro'
        # Updated proton correction based on last version
        # Added option to turn the energy loss corrections on and off
        
        
        Extra_Part_of_Name = '_VFinal_SP_V5_Pro'
        # Relized an issue with ∆P histograms for Double Pion channel: ∆P is plotted as a function of uncorrected momentum, but for the proton, energy correcions are applied after data is complied
        # Corrections needed to be restarted due to issue (no updates to corrections beyond rerunning options)
        
        
        Extra_Part_of_Name = '_VFinal_SP_V6_Pro'
        # Added linear refinements to existing corrections and created a new category of proton corrections for linear momentum corrections without phi dependance
        # Updated Exclusivity cuts for both Inbending and Outbending Proton Channels
        
        
        Extra_Part_of_Name = '_VFinal_SP_V7_Pro'
        # Added linear refinements and fixed Pi0 channel to add and remove energy loss corrections
        # Edits to several aspects of the code (namely related to how the DP and P0 files differed)
        # Added Inbending/Outbending file type to the names of the histograms
        
        Extra_Part_of_Name = '_VFinal_SP_V8_Pro'
        # Error in previous ∆P histograms (only used uncorrected proton momentum when the energy loss corrections were applied) - Now Fixed
        # Images will have the Pi0 ∆P points plotted in red after this update (change made in other code - this is a not to help identify the currently saved images)
        
        
        if("Out" in datatype):
            Extra_Part_of_Name = '_VFinal_SP_V1_Pro'
            # Running Outbending files with all options added to the Inbending files
            
            Extra_Part_of_Name = '_VFinal_SP_V2_Pro'
            # Relized an issue with ∆P histograms for Double Pion channel: ∆P is plotted as a function of uncorrected momentum, but for the proton, energy correcions are applied after data is complied
            # Corrections needed to be restarted due to issue (updates to corrections are minor - 'No Phi' has a correction now, though its meaning will be replaced soon)
            
            Extra_Part_of_Name = '_VFinal_SP_V3_Pro'
            # Added linear refinements to existing corrections and created a new category of proton corrections for linear momentum corrections without phi dependance
            # Updated Exclusivity cuts for both Inbending and Outbending Proton Channels (Outbending Exclusivity cuts are new - Did not previously exist for these channels)
            
            
            Extra_Part_of_Name = '_VFinal_SP_V4_Pro'
            # Fixed the energy loss corrections (was using the inbending energy loss corrections)
            # Same updates as "_VFinal_SP_V7_Pro" for the inbending corrections, but no refinements were added yet
            
            Extra_Part_of_Name = '_VFinal_SP_V5_Pro'
            # Error in previous ∆P histograms (only used uncorrected proton momentum when the energy loss corrections were applied) - Now Fixed
            # Images will have the Pi0 ∆P points plotted in red after this update (change made in other code - this is a not to help identify the currently saved images)

        
        
    if(event_type == "P0"):
        Extra_Part_of_Name = '_V1_SP_DP'
        
        Extra_Part_of_Name = '_VFinal_SP_V1_Pro'
        # Uses the final version of the Electron AND π+ Pion Corrections and existing Proton corrections (not updated with the new electron/π+ corrections)
        # Proton corrections can now be combined from both the double pion and π0 channels
        # (Error in running the double pion channel caused old proton corrections to be used - did not run the correct version of this code for the double pion channel)
        
        Extra_Part_of_Name = '_VFinal_SP_V2_Pro'
        # Updated the proton corrections using both the double pion and the π0 channel
        # Using a non-phi dependent correction/refinement
        
        Extra_Part_of_Name = '_VFinal_SP_V3_Pro'
        # Updated the proton corrections using both the double pion and the π0 channel
        # Using a non-phi dependent correction/refinement
        # Corrections are based on most recent inbending corrections
        
        Extra_Part_of_Name = '_VFinal_SP_V4_Pro'
        # Updated proton correction based on last version
        
        
        Extra_Part_of_Name = '_VFinal_SP_V5_Pro'
        # Relized an issue with ∆P histograms for Double Pion channel: ∆P is plotted as a function of uncorrected momentum, but for the proton, energy correcions are applied after data is complied
        # Corrections needed to be restarted due to issue (no updates to corrections beyond rerunning options)
        
        
        Extra_Part_of_Name = '_VFinal_SP_V6_Pro'
        # Added linear refinements to existing corrections and created a new category of proton corrections for linear momentum corrections without phi dependance
        # Updated Exclusivity cuts for both Inbending and Outbending Proton Channels
        
        
        Extra_Part_of_Name = '_VFinal_SP_V7_Pro'
        # Added linear refinements and fixed Pi0 channel to add and remove energy loss corrections
        # Edits to several aspects of the code (namely related to how the DP and P0 files differed)
        # Added Inbending/Outbending file type to the names of the histograms
        
        Extra_Part_of_Name = '_VFinal_SP_V8_Pro'
        # Error in previous ∆P histograms (only used uncorrected proton momentum when the energy loss corrections were applied) - Now Fixed
        # Images will have the Pi0 ∆P points plotted in red after this update (change made in other code - this is a not to help identify the currently saved images)
        
        
        if("Out" in datatype):
            Extra_Part_of_Name = '_VFinal_SP_V1_Pro'
            # Running Outbending files with all options added to the Inbending files
            
            Extra_Part_of_Name = '_VFinal_SP_V2_Pro'
            # Relized an issue with ∆P histograms for Double Pion channel: ∆P is plotted as a function of uncorrected momentum, but for the proton, energy correcions are applied after data is complied
            # Corrections needed to be restarted due to issue (updates to corrections are minor - 'No Phi' has a correction now, though its meaning will be replaced soon)
            
            Extra_Part_of_Name = '_VFinal_SP_V3_Pro'
            # Added linear refinements to existing corrections and created a new category of proton corrections for linear momentum corrections without phi dependance
            # Updated Exclusivity cuts for both Inbending and Outbending Proton Channels (Outbending Exclusivity cuts are new - Did not previously exist for these channels)
            
            
            Extra_Part_of_Name = '_VFinal_SP_V4_Pro'
            # Fixed the energy loss corrections (was using the inbending energy loss corrections)
            # Same updates as "_VFinal_SP_V7_Pro" for the inbending corrections, but no refinements were added yet
            
            Extra_Part_of_Name = '_VFinal_SP_V5_Pro'
            # Error in previous ∆P histograms (only used uncorrected proton momentum when the energy loss corrections were applied) - Now Fixed
            # Images will have the Pi0 ∆P points plotted in red after this update (change made in other code - this is a not to help identify the currently saved images)

    
    
    
#     Extra_Part_of_Name = '_Final_SP_VDP'
#     # Electron and π+ corrections are done, proton corrections in development



    Extra_Part_of_Name = "_GitHub_1_Pro"
    # Uploaded code to github (this is the first file name after uploading to github)
    
    Extra_Part_of_Name = "_GitHub_2_Pro"
    # Updated both inbending and outbending proton corrections (without phi dependance)
    # Also updated time estimation of code (minor edit)
    

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
    running_code_with_these_files = "/lustre19/expphy/volatile/clas12/shrestha/clas12momcorr/data/outbending/ePipX/skim4_00*"

    if(file_location == "All" or file_location == "Test" or file_location == "test"):
        if(event_type == "SP"):
            if(datatype == "Inbending"):
                running_code_with_these_files = "/lustre19/expphy/volatile/clas12/shrestha/clas12momcorr/data/inbending/ePipX/epip.skim4_00*"
            else:
                running_code_with_these_files = "/lustre19/expphy/volatile/clas12/shrestha/clas12momcorr/outbending/ePipX/skim4_00*"

        if(event_type == "DP"):
            if(datatype == "Inbending"):
                # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/kenjo/ntuple_epippimp/inb/lvl1_eppimpip.skim4_005*"
                running_code_with_these_files = "/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/inb/epPipPim.inb.qa.nSidis_005*"
            else:
                # running_code_with_these_files = "/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/outb/epPipPim.outb.qa.lvl1_eppimpip.skim4_00*"
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

    else:
        if(datatype == "Inbending"):
            running_code_with_these_files = file_location
        else:
            running_code_with_these_files = file_location

    rdf = ROOT.RDataFrame("h22", str(running_code_with_these_files))

    #############################################################################
    ##=====##=====##=====##=====##   Loading RDF   ##=====##=====##=====##=====##
    #############################################################################

    if(See_Num_of_Events_Q != 'n'):
        print("".join(["Number of events = ", str(rdf.Count().GetValue())]))
    print("".join(["Running code with files located here: ", str(running_code_with_these_files), "\n"]))




    if(event_type != "SP"):
        if("prox" not in rdf.GetColumnNames() and "px" in rdf.GetColumnNames()):
            rdf = rdf.Define("prox", "px")
            # print("Redefining px")
        if("proy" not in rdf.GetColumnNames() and "py" in rdf.GetColumnNames()):
            rdf = rdf.Define("proy", "py")
            # print("Redefining py")
        if("proz" not in rdf.GetColumnNames() and "pz" in rdf.GetColumnNames()):
            rdf = rdf.Define("proz", "pz")
            # print("Redefining pz")
        if("prosec" not in rdf.GetColumnNames() and "psec" in rdf.GetColumnNames()):
            rdf = rdf.Define("prosec", "psec")
            # print("Redefining psec")
    
    






    ############################################################################################################################################################
    ##========================================================================================================================================================##
    ##==============##============##============##============##         Calculations for RDF         ##============##============##============##============##
    ##========================================================================================================================================================##
    ############################################################################################################################################################



    ## Proton Energy Loss Corrections ##
    if(event_type != "SP"):
        
        Proton_Energy_Loss_Cor = ''.join(["""
        
        // // Proton Energy Corrections //
        // double ppro_mag = sqrt(prox*prox + proy*proy + proz*proz);
        // double pro_t = sqrt(prox*prox + proy*proy);
        // auto ppro = ROOT::Math::PxPyPzMVector(prox, proy, proz, 0.938);
        // bool lowband = (ppro.Theta()*(180/3.1415926)) < 27;
        // double dploss = exp(-2.739 - 3.932*ppro_mag) + 0.002907;
        // if(!lowband) dploss = exp(-1.2 - 4.228*ppro_mag) + 0.007502;
        // double feloss = (ppro_mag + dploss)/ppro_mag;
        // // double prox1 = feloss*prox;
        // // double proy1 = feloss*proy;
        // // double proz1 = feloss*proz;
        
        
        
        double dE_loss = 0;
        
        //=====// My Version of Andrey's Proton Energy Loss Correction (Corrections should be identical to the ones above, but the code is written slightly differently) //=====//
        
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
        rdf = rdf.Define("el","sqrt(ex*ex+ey*ey+ez*ez)")
        ##=====##       Polar Angles       ##=====##
        rdf = rdf.Define("elth","atan2(sqrt(ex*ex+ey*ey), ez)*(180/3.1415926)")
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
    except:
        print("Failure to process Electron Kinematics")

    #------------------------------------------#
    #---------------# Pi+ Pion #---------------#
    #------------------------------------------#
    if(event_type != "P0"):
        try:
            ##=====##    Momentum Magnitude    ##=====##
            rdf = rdf.Define("pip","sqrt(pipx*pipx+pipy*pipy+pipz*pipz)")
            ##=====##       Polar Angles       ##=====##
            rdf = rdf.Define("pipth","atan2(sqrt(pipx*pipx+pipy*pipy), pipz)*(180/3.1415926)")
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
        except:
            print("Failure to process Pi+ Pion Kinematics")
        
    #------------------------------------------#
    #---------------# Pi- Pion #---------------#
    #------------------------------------------#
    if(event_type == "DP"):
        try:
            ##=====##    Momentum Magnitude    ##=====##
            rdf = rdf.Define("pim","sqrt(pimx*pimx+pimy*pimy+pimz*pimz)")
            ##=====##       Polar Angles       ##=====##
            rdf = rdf.Define("pimth","atan2(sqrt(pimx*pimx+pimy*pimy), pimz)*(180/3.1415926)")
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
        except:
            print("Failure to process Pi- Pion Kinematics")
        
    #----------------------------------------#
    #---------------# Proton #---------------#
    #----------------------------------------#
    if(event_type != "SP"):
        try:
            ##=====##    Momentum Magnitude    ##=====##
            rdf = rdf.Define("pro","sqrt(prox*prox + proy*proy + proz*proz)")
            ##=====##       Polar Angles       ##=====##
            rdf = rdf.Define("proth","atan2(sqrt(prox*prox + proy*proy), proz)*(180/3.1415926)")
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
        except:
            print("Failure to process Proton Kinematics")
            
    #-----------------------------------------------------------#
    #---------------# Proton (Energy Corrected) #---------------#
    #-----------------------------------------------------------#
    if(event_type != "SP"):
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
        except:
            print("Failure to process Proton Kinematics")


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
    #----------#     Last updated on: 6-11-2022     #----------#
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

            }


            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //====================================================================================================================================//
            //======================//======================//     Electron Corrections (End)     //======================//======================//
            //====================================================================================================================================//
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





            /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //=========================================================================================================================================================//
            //==============================//==============================//     Pi+ Corrections     //==============================//==============================//
            //=========================================================================================================================================================//
            /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


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


            ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //===============================================================================================================================================================//
            //==============================//==============================//     Pi+ Corrections (End)     //==============================//==============================//
            //===============================================================================================================================================================//
            ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





            /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //=========================================================================================================================================================//
            //==============================//==============================//     Pi- Corrections     //==============================//==============================//
            //=========================================================================================================================================================//
            /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


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


            ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //===============================================================================================================================================================//
            //==============================//==============================//     Pi- Corrections (End)     //==============================//==============================//
            //===============================================================================================================================================================//
            ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //================================================================================================================================================================//
            //==============================//==============================//     All Proton Corrections     //==============================//==============================//
            //================================================================================================================================================================//
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

            if(corPro != 0 && ivec == 3){
            
                if(corPro == 1){ // Quadratic Momentum - Quadratic Phi

                    if(sec == 1){

                        // The following lines should be added up in the order given for the full correction
                        // Applying this code as given will give the exact corrections of this analysis
                        // These parameters will be combined into a single line at a later point

                        dp = ((3.54e-06)*phi*phi + (0.00012741)*phi + (-0.00169485))*pp*pp + ((-6.8e-06)*phi*phi + (-0.00018409)*phi + (0.00756841))*pp + ((3.49e-06)*phi*phi + (6.297e-05)*phi + (-0.00334762));
                        dp = dp + ((-1.857e-05)*phi*phi + (-1.14e-04)*phi + (4.346e-03))*pp*pp + ((5.978e-05)*phi*phi + (3.776e-04)*phi + (-0.0192))*pp + ((-3.864e-05)*phi*phi + (-2.651e-04)*phi + (0.0163));
                        dp = dp + ((9.05e-06)*phi*phi + (-0.00011072)*phi + (-0.0019497))*pp*pp + ((-2.473e-05)*phi*phi + (0.00025581)*phi + (0.006382))*pp + ((1.288e-05)*phi*phi + (-0.00012678)*phi + (-0.0034358));
                        dp = dp + ((-4.88e-06)*phi*phi + (0.00015119)*phi + (0.00157759))*pp*pp + ((1.467e-05)*phi*phi + (-0.00032185)*phi + (-0.00770597))*pp + ((-1.062e-05)*phi*phi + (0.00016935)*phi + (0.00680068));
                        dp = dp + ((-6.48e-06)*phi*phi + (9.682e-05)*phi + (0.00122778))*pp*pp + ((2.14e-05)*phi*phi + (-0.00026216)*phi + (-0.00452799))*pp + ((-1.54e-05)*phi*phi + (0.00013753)*phi + (0.00366475));
                        
                        // No phi dependence refinements
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 1][All Pro Phi Bins] is:
                        dp = dp + (0.00169173)*pp*pp + (-0.00575224)*pp + (-0.00014507);
                        
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 1][All Pro Phi Bins] is:
                        dp = dp + (-0.00168968)*pp*pp + (0.00419236)*pp + (-0.0049719);
                        
                        
                        // From VFinal_SP_V3_Pro for VFinal_SP_V4_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 1][All Pro Phi Bins] is:
                        dp = dp + (0.00072651)*pp*pp + (-0.00130255)*pp + (0.00061113);
                        
                        
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
                        dp = dp + (-0.00285548)*pp + (0.00229098);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
                        dp = dp + (-0.00663606)*pp + (0.0093758);
                        
                        

                    }

                    if(sec == 2){

                        // The following lines should be added up in the order given for the full correction
                        // Applying this code as given will give the exact corrections of this analysis
                        // These parameters will be combined into a single line at a later point

                        dp = ((-7.51e-06)*phi*phi + (7.449e-05)*phi + (-0.00193523))*pp*pp + ((1.372e-05)*phi*phi + (-0.00033226)*phi + (0.01605589))*pp + ((-2.27e-06)*phi*phi + (0.00017048)*phi + (-0.01159601));
                        dp = dp + ((-2e-07)*phi*phi + (1.393e-04)*phi + (-9.325e-04))*pp*pp + ((3.51e-06)*phi*phi + (-4.582e-04)*phi + (-2.414e-03))*pp + ((1.13e-06)*phi*phi + (3.343e-04)*phi + (4.76e-03));
                        dp = dp + ((3.84e-06)*phi*phi + (-1.841e-05)*phi + (0.00085236))*pp*pp + ((-1.049e-05)*phi*phi + (3.949e-05)*phi + (-0.0024575))*pp + ((7.08e-06)*phi*phi + (-2.962e-05)*phi + (0.00084752));
                        dp = dp + ((1.51e-06)*phi*phi + (-8.957e-05)*phi + (-0.0029601))*pp*pp + ((-1.07e-05)*phi*phi + (0.00022399)*phi + (0.0077783))*pp + ((1.042e-05)*phi*phi + (-0.00015105)*phi + (-0.00291493));
                        dp = dp + ((2.57e-06)*phi*phi + (-1.635e-05)*phi + (-0.00105274))*pp*pp + ((-8.65e-06)*phi*phi + (4.65e-05)*phi + (0.00267734))*pp + ((5.91e-06)*phi*phi + (-2.431e-05)*phi + (-0.00144716));
                        
                        // No phi dependence refinements
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 2][All Pro Phi Bins] is:
                        dp = dp + (0.00395058)*pp*pp + (-0.01560805)*pp + (0.00876263);
                        
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 2][All Pro Phi Bins] is:
                        dp = dp + (-3.649e-05)*pp*pp + (0.00149925)*pp + (-0.00417216);
                        
                        
                        // From VFinal_SP_V3_Pro for VFinal_SP_V4_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 2][All Pro Phi Bins] is:
                        dp = dp + (-0.00021132)*pp*pp + (0.00102468)*pp + (-0.00067411);
                        
                        
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
                        dp = dp + (-0.00160472)*pp + (0.00228755);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
                        dp = dp + (-0.00449475)*pp + (0.00631827);
                        
                        

                    }

                    if(sec == 3){

                        // The following lines should be added up in the order given for the full correction
                        // Applying this code as given will give the exact corrections of this analysis
                        // These parameters will be combined into a single line at a later point

                        dp = ((-1.192e-05)*phi*phi + (5.745e-05)*phi + (0.00184011))*pp*pp + ((3.226e-05)*phi*phi + (-0.00017688)*phi + (0.00281795))*pp + ((-1.339e-05)*phi*phi + (0.00010705)*phi + (-0.00584473));
                        dp = dp + ((1.153e-05)*phi*phi + (-4.931e-05)*phi + (-5.09e-03))*pp*pp + ((-3.071e-05)*phi*phi + (7.061e-05)*phi + (6.413e-03))*pp + ((1.525e-05)*phi*phi + (3.982e-05)*phi + (2.289e-03));
                        dp = dp + ((2.49e-06)*phi*phi + (-2.58e-05)*phi + (-0.00047769))*pp*pp + ((-6.8e-06)*phi*phi + (7.153e-05)*phi + (0.0012909))*pp + ((3.31e-06)*phi*phi + (-5.431e-05)*phi + (-0.00023919));
                        dp = dp + ((4.49e-06)*phi*phi + (-0.00019179)*phi + (0.00160744))*pp*pp + ((-8.79e-06)*phi*phi + (0.00055794)*phi + (-0.0092487))*pp + ((1.43e-06)*phi*phi + (-0.00031925)*phi + (0.00929164));
                        dp = dp + ((7.71e-06)*phi*phi + (-2.683e-05)*phi + (-0.00231227))*pp*pp + ((-2.053e-05)*phi*phi + (3.837e-05)*phi + (0.00664668))*pp + ((1.225e-05)*phi*phi + (-7.91e-06)*phi + (-0.00462877));
                        
                        // No phi dependence refinements
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 3][All Pro Phi Bins] is:
                        dp = dp + (0.00203021)*pp*pp + (-0.00608307)*pp + (-0.00010907);
                        
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 3][All Pro Phi Bins] is:
                        dp = dp + (0.00168811)*pp*pp + (-0.00460045)*pp + (-0.00045637);
                        
                        
                        // From VFinal_SP_V3_Pro for VFinal_SP_V4_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 3][All Pro Phi Bins] is:
                        dp = dp + (-0.00418762)*pp*pp + (0.01056876)*pp + (-0.00554405);
                        
                        
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
                        dp = dp + (-0.00092964)*pp + (-0.00109126);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
                        dp = dp + (-0.00717693)*pp + (0.01030637);
                        
                        

                    }

                    if(sec == 4){

                        // The following lines should be added up in the order given for the full correction
                        // Applying this code as given will give the exact corrections of this analysis
                        // These parameters will be combined into a single line at a later point

                        dp = ((1.02e-06)*phi*phi + (-5.753e-05)*phi + (-0.00116896))*pp*pp + ((6.6e-07)*phi*phi + (0.00027025)*phi + (0.01147826))*pp + ((5.7e-07)*phi*phi + (-0.00018222)*phi + (-0.01011935));
                        dp = dp + ((-1.496e-05)*phi*phi + (5.225e-05)*phi + (1.183e-03))*pp*pp + ((4.374e-05)*phi*phi + (-1.675e-04)*phi + (-8.0593e-03))*pp + ((-3.157e-05)*phi*phi + (1.325e-04)*phi + (9.979e-03));
                        dp = dp + ((5e-07)*phi*phi + (-1.454e-05)*phi + (-0.0007149))*pp*pp + ((5.47e-06)*phi*phi + (7.743e-05)*phi + (0.00068488))*pp + ((-7.88e-06)*phi*phi + (-8.695e-05)*phi + (7.4e-05));
                        dp = dp + ((7.8e-07)*phi*phi + (0.00011795)*phi + (0.00165541))*pp*pp + ((-3.13e-06)*phi*phi + (-0.00042059)*phi + (-0.00798432))*pp + ((6.23e-06)*phi*phi + (0.00033604)*phi + (0.00680092));
                        dp = dp + ((-3.98e-06)*phi*phi + (-2.054e-05)*phi + (0.00014266))*pp*pp + ((1.058e-05)*phi*phi + (6.702e-05)*phi + (-0.00055213))*pp + ((-8.63e-06)*phi*phi + (-8.036e-05)*phi + (0.00105203));
                        
                        // No phi dependence refinements
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 4][All Pro Phi Bins] is:
                        dp = dp + (-0.00162264)*pp*pp + (0.00271055)*pp + (-0.00383378);
                        
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 4][All Pro Phi Bins] is:
                        dp = dp + (-0.00181956)*pp*pp + (0.00507679)*pp + (-0.00558739);
                        
                        
                        // From VFinal_SP_V3_Pro for VFinal_SP_V4_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 4][All Pro Phi Bins] is:
                        dp = dp + (-0.00127361)*pp*pp + (0.00317634)*pp + (-0.00102369);
                        
                        
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
                        dp = dp + (-0.00220956)*pp + (0.00169869);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
                        dp = dp + (-0.00440748)*pp + (0.00582998);
                        
                        

                    }

                    if(sec == 5){

                        // The following lines should be added up in the order given for the full correction
                        // Applying this code as given will give the exact corrections of this analysis
                        // These parameters will be combined into a single line at a later point

                        dp = ((8.52e-06)*phi*phi + (-0.00019083)*phi + (-0.00545608))*pp*pp + ((-2.943e-05)*phi*phi + (0.00051946)*phi + (0.01909462))*pp + ((2.152e-05)*phi*phi + (-0.00028127)*phi + (-0.01224992));
                        dp = dp + ((-7.62e-06)*phi*phi + (4.846e-05)*phi + (1.713e-03))*pp*pp + ((1.092e-05)*phi*phi + (-4.886e-05)*phi + (-8.412e-03))*pp + ((5.17e-06)*phi*phi + (-2.448e-05)*phi + (5.572e-03));
                        dp = dp + ((4.63e-06)*phi*phi + (8.79e-06)*phi + (-0.0016709))*pp*pp + ((-1.308e-05)*phi*phi + (-3.022e-05)*phi + (0.0046265))*pp + ((7.58e-06)*phi*phi + (1.813e-05)*phi + (-0.0026691));
                        dp = dp + ((-1.6e-07)*phi*phi + (-3.7e-06)*phi + (0.00249659))*pp*pp + ((9e-06)*phi*phi + (-2.182e-05)*phi + (-0.012996))*pp + ((-1.66e-05)*phi*phi + (-1.649e-05)*phi + (0.01366649));
                        dp = dp + ((-3.89e-06)*phi*phi + (-8.14e-06)*phi + (0.00086004))*pp*pp + ((1.439e-05)*phi*phi + (4.012e-05)*phi + (-0.00281493))*pp + ((-1.111e-05)*phi*phi + (-3.062e-05)*phi + (0.00129624));
                        
                        // No phi dependence refinements
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 5][All Pro Phi Bins] is:
                        dp = dp + (0.00242698)*pp*pp + (-0.00809566)*pp + (0.00226371);
                        
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 5][All Pro Phi Bins] is:
                        dp = dp + (-0.00101855)*pp*pp + (0.00321118)*pp + (-0.00487795);
                        
                        
                        // From VFinal_SP_V3_Pro for VFinal_SP_V4_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 5][All Pro Phi Bins] is:
                        dp = dp + (-0.00046125)*pp*pp + (0.00058938)*pp + (-0.00023735);
                        
                        
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
                        dp = dp + (-0.00437863)*pp + (0.00306682);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
                        dp = dp + (-0.00641025)*pp + (0.00742032);
                        
                        

                    }

                    if(sec == 6){

                        // The following lines should be added up in the order given for the full correction
                        // Applying this code as given will give the exact corrections of this analysis
                        // These parameters will be combined into a single line at a later point

                        dp = ((-6.8e-06)*phi*phi + (-9.966e-05)*phi + (0.00217971))*pp*pp + ((1.846e-05)*phi*phi + (0.000334)*phi + (-0.00358955))*pp + ((-7.83e-06)*phi*phi + (-0.00022134)*phi + (0.00280734));
                        dp = dp + ((-3.43e-06)*phi*phi + (3.171e-04)*phi + (-1.572e-03))*pp*pp + ((1.799e-05)*phi*phi + (-8.219e-04)*phi + (-2.945e-03))*pp + ((-9.34e-06)*phi*phi + (3.74e-04)*phi + (5.1794e-03));
                        dp = dp + ((-3.64e-06)*phi*phi + (1.113e-05)*phi + (0.0014469))*pp*pp + ((1.031e-05)*phi*phi + (-2.765e-05)*phi + (-0.0041404))*pp + ((-5.83e-06)*phi*phi + (-3.08e-06)*phi + (0.0024571));
                        dp = dp + ((1.969e-05)*phi*phi + (-6.395e-05)*phi + (-0.00457687))*pp*pp + ((-5.808e-05)*phi*phi + (0.00018976)*phi + (0.01091338))*pp + ((3.344e-05)*phi*phi + (-0.00015701)*phi + (-0.00426004));
                        dp = dp + ((2.39e-06)*phi*phi + (3.47e-06)*phi + (0.00087654))*pp*pp + ((-7.18e-06)*phi*phi + (4.082e-05)*phi + (-0.00295533))*pp + ((2.94e-06)*phi*phi + (-4.526e-05)*phi + (0.00265678));
                        
                        // No phi dependence refinements
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 6][All Pro Phi Bins] is:
                        dp = dp + (-0.0049111)*pp*pp + (0.01095641)*pp + (-0.00659583);
                        
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 6][All Pro Phi Bins] is:
                        dp = dp + (0.00305608)*pp*pp + (-0.00825601)*pp + (0.00172904);
                        
                        
                        // From VFinal_SP_V3_Pro for VFinal_SP_V4_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 6][All Pro Phi Bins] is:
                        dp = dp + (0.00177597)*pp*pp + (-0.00329542)*pp + (0.00131247);
                        
                        
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
                        dp = dp + (-0.00381041)*pp + (0.00380846);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
                        dp = dp + (-0.00976345)*pp + (0.01137852);
                        
                        

                    }
                }
                
                
                
                if(corPro == 2){ // Quadratic Momentum - No Phi Dependence

                    if(sec == 1){
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 1][All Pro Phi Bins] is:
                        // dp = dp + (8.9731e-04)*pp*pp + (2.46733e-03)*pp + (-8.50352e-03);
                        
                        
                        // // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi)][Sector 1][All Pro Phi Bins] is:
                        // dp = dp + (0.00047616)*pp*pp + (-0.01123335)*pp + (0.01506785);
                        
                        
                        // // From VFinal_SP_V3_Pro for VFinal_SP_V4_Pro
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi)][Sector 1][All Pro Phi Bins] is:
                        // dp = dp + (-0.00077651)*pp*pp + (0.00274527)*pp + (-0.00186343);
                        
                        
                        // Above corrections were flawed when initially created
                        // Below: From VFinal_SP_V4_Pro for VFinal_SP_V5_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
                        dp = (0.00095864)*pp*pp + (-0.00763615)*pp + (0.00577594);
                        
                        
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
                        dp = dp + (-0.00449132)*pp + (0.00445928);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
                        dp = dp + (-0.0049576)*pp + (0.00709573);
                        
                        
                        // From GitHub_1 for GitHub_2
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
                        dp = dp + ((-4.1714e-04)*pp*pp + (6.8231e-03)*pp + (-9.5502e-03));
                        
                        
                    }

                    if(sec == 2){
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 2][All Pro Phi Bins] is:
                        // dp = dp + (-1.31559e-03)*pp*pp + (4.09356e-03)*pp + (-4.80802e-03);
                        
                        
                        // // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi)][Sector 2][All Pro Phi Bins] is:
                        // dp = dp + (-0.00120067)*pp*pp + (0.00146865)*pp + (0.00380791);
                        
                        
                        // // From VFinal_SP_V3_Pro for VFinal_SP_V4_Pro
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi)][Sector 2][All Pro Phi Bins] is:
                        // dp = dp + (0.00027291)*pp*pp + (-0.00066265)*pp + (0.00052011);
                        
                        
                        // Above corrections were flawed when initially created
                        // Below: From VFinal_SP_V4_Pro for VFinal_SP_V5_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
                        dp = (-0.00129479)*pp*pp + (0.00159079)*pp + (0.00110165);
                        
                        
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
                        dp = dp + (-0.00182564)*pp + (0.00289993);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
                        dp = dp + (-0.00559668)*pp + (0.00781151);
                        
                        
                        // From GitHub_1 for GitHub_2
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
                        dp = dp + ((3.4040e-04)*pp*pp + (2.9688e-03)*pp + (-8.4316e-03));
                        
                        
                    }

                    if(sec == 3){
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 3][All Pro Phi Bins] is:
                        // dp = dp + (2.06335e-03)*pp*pp + (-3.03677e-03)*pp + (-4.89312e-03);
                        
                        
                        // // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi)][Sector 3][All Pro Phi Bins] is:
                        // dp = dp + (-0.00192469)*pp*pp + (-0.00047181)*pp + (0.00573251);
                        
                        
                        // // From VFinal_SP_V3_Pro for VFinal_SP_V4_Pro
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi)][Sector 3][All Pro Phi Bins] is:
                        // dp = dp + (-0.0039923)*pp*pp + (0.00960735)*pp + (-0.00520611);
                        
                        
                        // Above corrections were flawed when initially created
                        // Below: From VFinal_SP_V4_Pro for VFinal_SP_V5_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
                        dp = (-0.00291321)*pp*pp + (0.00359669)*pp + (-0.00315983);
                        
                        
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
                        dp = dp + (-0.00349174)*pp + (0.0022677);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
                        dp = dp + (-0.00598024)*pp + (0.00867433);
                        
                        
                        // From GitHub_1 for GitHub_2
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
                        dp = dp + ((2.3578e-03)*pp*pp + (-1.8221e-03)*pp + (-2.0130e-03));
                        
                        
                    }

                    if(sec == 4){
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 4][All Pro Phi Bins] is:
                        // dp = dp + (-3.673e-03)*pp*pp + (0.01286885)*pp + (-0.01358279);
                        
                        
                        // // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi)][Sector 4][All Pro Phi Bins] is:
                        // dp = dp + (-0.00164851)*pp*pp + (0.00110237)*pp + (0.00462848);
                        
                        
                        // // From VFinal_SP_V3_Pro for VFinal_SP_V4_Pro
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi)][Sector 4][All Pro Phi Bins] is:
                        // dp = dp + (-0.00091463)*pp*pp + (0.00181641)*pp + (-0.00059543);
                        
                        
                        // Above corrections were flawed when initially created
                        // Below: From VFinal_SP_V4_Pro for VFinal_SP_V5_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
                        dp = (-0.0044169)*pp*pp + (0.01163524)*pp + (-0.0074502);
                        
                        
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
                        dp = dp + (-0.0033675)*pp + (0.00321459);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
                        dp = dp + (-0.00528728)*pp + (0.0063143);
                        
                        
                        // From GitHub_1 for GitHub_2
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
                        dp = dp + ((4.2225e-03)*pp*pp + (-8.7515e-03)*pp + (1.3453e-03));
                        
                        
                    }

                    if(sec == 5){
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 5][All Pro Phi Bins] is:
                        // dp = dp + (9.88e-04)*pp*pp + (-2.9184e-04)*pp + (-6.18385e-03);
                        
                        
                        // // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi)][Sector 5][All Pro Phi Bins] is:
                        // dp = dp + (-0.00235825)*pp*pp + (-0.00275384)*pp + (0.00779621);
                        
                        
                        // // From VFinal_SP_V3_Pro for VFinal_SP_V4_Pro
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi)][Sector 5][All Pro Phi Bins] is:
                        // dp = dp + (0.00120317)*pp*pp + (-0.00540241)*pp + (0.00395903);
                        
                        
                        // Above corrections were flawed when initially created
                        // Below: From VFinal_SP_V4_Pro for VFinal_SP_V5_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
                        dp = (-0.00019781)*pp*pp + (-0.00714057)*pp + (0.0043824);
                        
                        
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
                        dp = dp + (-0.00448086)*pp + (0.00277793);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
                        dp = dp + (-0.00703286)*pp + (0.00816163);
                        
                        
                        // From GitHub_1 for GitHub_2
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
                        dp = dp + ((1.7379e-03)*pp*pp + (1.7106e-03)*pp + (-4.8564e-03));
                        
                        
                    }

                    if(sec == 6){
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi)][Sector 6][All Pro Phi Bins] is:
                        // dp = dp + (-1.63203e-03)*pp*pp + (9.23426e-03)*pp + (-0.01045406);
                        
                        
                        // // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi)][Sector 6][All Pro Phi Bins] is:
                        // dp = dp + (-0.00123307)*pp*pp + (-0.00767686)*pp + (0.01289128);
                        
                        
                        // // From VFinal_SP_V3_Pro for VFinal_SP_V4_Pro
                        // // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi)][Sector 6][All Pro Phi Bins] is:
                        // dp = dp + (0.00013966)*pp*pp + (-0.00160231)*pp + (0.00144506);
                        
                        
                        // Above corrections were flawed when initially created
                        // Below: From VFinal_SP_V4_Pro for VFinal_SP_V5_Pro
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
                        dp = (0.00021002)*pp*pp + (-0.00663462)*pp + (0.00686447);
                        
                        
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
                        dp = dp + (-0.00396208)*pp + (0.00403928);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
                        dp = dp + (-0.00975372)*pp + (0.01145557);
                        
                        
                        // From GitHub_1 for GitHub_2
                        // The QUADRATIC function predicted for Δp_{pro} for [Inbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
                        dp = dp + ((2.1718e-03)*pp*pp + (-3.7965e-04)*pp + (-5.1268e-03));
                        
                        
                    }
                }
                
                
                
                
                if(corPro == 3){ // Linear Momentum - No Phi Dependence
                
                    if(sec == 1){
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
                        dp = (-0.004303)*pp + (0.00333901);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Linear - No Phi)][Sector 1][All Pro Phi Bins] is:
                        dp = dp + (-0.00829709)*pp + (0.01068574);
                        
                        
                    }
                    
                    if(sec == 2){
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
                        dp = (-0.00252231)*pp + (0.00368321);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Linear - No Phi)][Sector 2][All Pro Phi Bins] is:
                        dp = dp + (-0.00657007)*pp + (0.00982608);
                        
                        
                    }
                    
                    if(sec == 3){
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
                        dp = (-0.00591728)*pp + (0.00326054);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Linear - No Phi)][Sector 3][All Pro Phi Bins] is:
                        dp = dp + (-0.00800403)*pp + (0.01009171);
                        
                        
                    }
                    
                    if(sec == 4){
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
                        dp = (-0.0028457)*pp + (0.0021428);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Linear - No Phi)][Sector 4][All Pro Phi Bins] is:
                        dp = dp + (-0.00522008)*pp + (0.00629009);
                        
                        
                    }
                    
                    if(sec == 5){
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
                        dp = (-0.00753056)*pp + (0.00439248);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Linear - No Phi)][Sector 5][All Pro Phi Bins] is:
                        dp = dp + (-0.00852263)*pp + (0.00862785);
                        
                        
                    }
                    
                    if(sec == 6){
                        // From VFinal_SP_V5_Pro for VFinal_SP_V6_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
                        dp = (-0.00588786)*pp + (0.00618525);
                        
                        
                        // From VFinal_SP_V6_Pro for VFinal_SP_V7_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Linear - No Phi)][Sector 6][All Pro Phi Bins] is:
                        dp = dp + (-0.01185891)*pp + (0.01375949);
                        
                        
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
    #----------#     Last updated on: 8-11-2022     #----------#
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

            // For Pi+ Pion/Proton Shift
            if(ivec == 1 || ivec == 3){
                phi = PhiLocal + (32/(pp-0.05));
            }

            // For Pi- Pion Shift
            if(ivec == 2){
                phi = PhiLocal - (32/(pp-0.05));
            }



            ////////////////////////////////////////////////////////////////////////////////////////////////
            //===============//===============//     No Corrections     //===============//===============//
            ////////////////////////////////////////////////////////////////////////////////////////////////

            if(corEl == 0 && ivec == 0){ // No Electron Correction
                dp = 0;
            }
            if(corPip == 0 && ivec == 1){ // No Pi+ Correction
                dp = 0;
            }
            if(corPim == 0 && ivec == 2){ // No Pi- Correction
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





            /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //=====================================================================================================================================//
            //=========================//=========================//     Pi+ Corrections     //=========================//=========================//
            //=====================================================================================================================================//
            /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

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

            /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //=====================================================================================================================================//
            //=======================//=======================//      Pi+ Corrections (End)      //=======================//=======================//
            //=====================================================================================================================================//
            /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            
            
            
            
            /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //=====================================================================================================================================//
            //=========================//=========================//     Pi- Corrections     //=========================//=========================//
            //=====================================================================================================================================//
            /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

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


            /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //=====================================================================================================================================//
            //=======================//=======================//      Pi+ Corrections (End)      //=======================//=======================//
            //=====================================================================================================================================//
            /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////









            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            //====================================================================================================================================//
            //========================//========================//     Proton Corrections     //========================//========================//
            //====================================================================================================================================//
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

            if(ivec == 3 && corPro != 0){

                if(corPro == 1){ // Quadratic Momentum - Quadratic Phi

                    // STILL IN DEVELOPMENT (As of 6-5-2022)

                    if(sec == 1){
                        dp = ((3.64e-06)*phi*phi + (1.1921e-04)*phi + (-0.01125))*pp*pp + ((-1.178e-05)*phi*phi + (-4.5955e-04)*phi + (0.03691))*pp + ((4.61e-06)*phi*phi + (3.6478e-04)*phi + (-0.01722));
                        dp = dp + ((4.03e-06)*phi*phi + (-1.1415e-04)*phi + (1.1251e-03))*pp*pp + ((-1.245e-05)*phi*phi + (2.5131e-04)*phi + (-3.8259e-03))*pp + ((8.92e-06)*phi*phi + (-1.0316e-04)*phi + (2.2956e-03));
                        dp = dp + ((2.29e-06)*phi*phi + (-3.7782e-04)*phi + (6.6792e-03))*pp*pp + ((4.7e-06)*phi*phi + (1.1717e-03)*phi + (-0.02151))*pp + ((-1.858e-05)*phi*phi + (-7.5414e-04)*phi + (0.01789));
                        
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
                        dp = dp + (0.00073098)*pp + (-0.00597196);

                    }

                    if(sec == 2){
                        dp = ((4.88e-06)*phi*phi + (2.7371e-04)*phi + (-9.3059e-03))*pp*pp + ((-1.639e-05)*phi*phi + (-9.4587e-04)*phi + (0.03113))*pp + ((9.88e-06)*phi*phi + (5.4051e-04)*phi + (-0.01697));
                        dp = dp + ((-1.57e-06)*phi*phi + (-7.892e-05)*phi + (-1.3376e-03))*pp*pp + ((4.98e-06)*phi*phi + (2.0238e-04)*phi + (2.9417e-03))*pp + ((-1.42e-06)*phi*phi + (-9.277e-05)*phi + (-1.536e-03));
                        dp = dp + ((-1.109e-05)*phi*phi + (5.63e-05)*phi + (1.6522e-03))*pp*pp + ((3.364e-05)*phi*phi + (-1.9326e-04)*phi + (-3.1746e-03))*pp + ((-2.293e-05)*phi*phi + (1.5602e-04)*phi + (-1.2221e-03));
                        
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
                        dp = dp + (-0.00377298)*pp + (-0.00093475);

                    }

                    if(sec == 3){
                        dp = ((-3.8e-07)*phi*phi + (-2.3252e-04)*phi + (-6.9323e-03))*pp*pp + ((-8.05e-06)*phi*phi + (7.6794e-04)*phi + (0.02568))*pp + ((1.771e-05)*phi*phi + (-4.2146e-04)*phi + (-0.01939));
                        dp = dp + ((1.89e-06)*phi*phi + (-5.226e-05)*phi + (-3.1965e-04))*pp*pp + ((-6.1e-06)*phi*phi + (2.1759e-04)*phi + (7.4608e-04))*pp + ((6.54e-06)*phi*phi + (-2.3328e-04)*phi + (-9.3044e-04));
                        dp = dp + ((8.39e-06)*phi*phi + (4.036e-05)*phi + (-5.4168e-03))*pp*pp + ((-3.316e-05)*phi*phi + (-3.941e-05)*phi + (0.01842))*pp + ((2.57e-05)*phi*phi + (-9.111e-05)*phi + (-0.01268));
                        
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
                        dp = dp + (-0.00270011)*pp + (-0.00380264);

                    }

                    if(sec == 4){
                        dp = ((5.18e-06)*phi*phi + (9.651e-05)*phi + (-3.2349e-03))*pp*pp + ((-5.53e-06)*phi*phi + (-3.2406e-04)*phi + (8.7308e-03))*pp + ((-4.85e-06)*phi*phi + (3.4975e-04)*phi + (-2.2932e-03));
                        dp = dp + ((-5.83e-06)*phi*phi + (-9.317e-05)*phi + (1.5804e-04))*pp*pp + ((1.776e-05)*phi*phi + (2.5267e-04)*phi + (2.7523e-04))*pp + ((-7.28e-06)*phi*phi + (-6.666e-05)*phi + (-9.4837e-04));
                        dp = dp + ((3.28e-06)*phi*phi + (-2.424e-05)*phi + (-2.892e-03))*pp*pp + ((-7.55e-06)*phi*phi + (9.2e-07)*phi + (8.5874e-03))*pp + ((4.61e-06)*phi*phi + (3.191e-05)*phi + (-2.6045e-03));
                        
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
                        dp = dp + (8.924e-05)*pp + (-0.00839515);

                    }

                    if(sec == 5){
                        dp = ((2.02e-06)*phi*phi + (-6.398e-05)*phi + (-2.936e-03))*pp*pp + ((-1.362e-05)*phi*phi + (1.6553e-04)*phi + (0.01371))*pp + ((1.477e-05)*phi*phi + (-1.7292e-04)*phi + (-9.3934e-03));
                        dp = dp + ((-3.34e-06)*phi*phi + (-6.845e-05)*phi + (3.9336e-04))*pp*pp + ((6.54e-06)*phi*phi + (2.6982e-04)*phi + (-1.0648e-03))*pp + ((3.7e-07)*phi*phi + (-2.4201e-04)*phi + (6.1124e-04));
                        dp = dp + ((-9.95e-06)*phi*phi + (-5.962e-05)*phi + (3.2408e-03))*pp*pp + ((2.779e-05)*phi*phi + (2.0489e-04)*phi + (-7.7477e-03))*pp + ((-1.437e-05)*phi*phi + (-1.8023e-04)*phi + (4.0063e-03));
                        
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
                        dp = dp + (-0.00031025)*pp + (-0.00564687);

                    }

                    if(sec == 6){
                        dp = ((-6.09e-06)*phi*phi + (3.723e-05)*phi + (-3.8812e-03))*pp*pp + ((1.358e-05)*phi*phi + (-2.3503e-04)*phi + (0.01602))*pp + ((9.2e-07)*phi*phi + (1.6677e-04)*phi + (-0.01057));
                        dp = dp + ((1.47e-06)*phi*phi + (9.36e-05)*phi + (-3.0238e-04))*pp*pp + ((4.01e-06)*phi*phi + (-3.3589e-04)*phi + (-2.6796e-03))*pp + ((-2.356e-05)*phi*phi + (2.188e-04)*phi + (9.0301e-03));
                        dp = dp + ((-1.322e-05)*phi*phi + (-1.502e-05)*phi + (1.8311e-03))*pp*pp + ((4.069e-05)*phi*phi + (8.516e-05)*phi + (-3.9543e-03))*pp + ((-2.426e-05)*phi*phi + (-4.229e-05)*phi + (1.912e-03));
                        
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi-/Pro Cor (Quad - Quad Phi - Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
                        dp = dp + (0.00058117)*pp + (-0.00297983);

                    }

                }
                
                
                if(corPro == 2){ // Quadratic Momentum - No Phi Dependence

                    // STILL IN DEVELOPMENT (As of 8-11-2022)

                    if(sec == 1){
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
                        dp = (-0.00130144)*pp*pp + (0.00637438)*pp + (-0.00699777);
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
                        dp = dp + (0.00080717)*pp + (-0.00110934);
                        
                        
                        // From GitHub_1 for GitHub_2
                        // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
                        dp = dp + ((-3.0072e-03)*pp*pp + (8.1872e-03)*pp + (-8.5605e-03));
                        
                        
                    }

                    if(sec == 2){
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
                        dp = (-0.01021316)*pp*pp + (0.03057096)*pp + (-0.02332303);
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
                        dp = dp + (-0.00219862)*pp + (-0.00013674);
                        
                        
                        // From GitHub_1 for GitHub_2
                        // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
                        dp = dp + ((-2.7312e-03)*pp*pp + (0.01281)*pp + (-0.01061));
                        
                        
                    }

                    if(sec == 3){
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
                        dp = (-0.00893696)*pp*pp + (0.02823431)*pp + (-0.02539962);
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
                        dp = dp + (-0.00132046)*pp + (-0.00173872);
                        
                        
                        // From GitHub_1 for GitHub_2
                        // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
                        dp = dp + ((-4.2909e-04)*pp*pp + (5.6398e-03)*pp + (-7.0443e-03));
                        
                        
                    }

                    if(sec == 4){
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
                        dp = (-0.01029772)*pp*pp + (0.03414159)*pp + (-0.02817884);
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
                        dp = dp + (0.00024025)*pp + (-0.00287093);
                        
                        
                        // From GitHub_1 for GitHub_2
                        // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
                        dp = dp + ((-4.2337e-03)*pp*pp + (0.01534)*pp + (-0.01327));
                        
                        
                    }

                    if(sec == 5){
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
                        dp = (-0.00843996)*pp*pp + (0.02813552)*pp + (-0.02389639);
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
                        dp = dp + (7.24e-05)*pp + (-0.00224052);
                        
                        
                        // From GitHub_1 for GitHub_2
                        // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
                        dp = dp + ((-2.4041e-03)*pp*pp + (0.0107)*pp + (-0.01073));
                        
                        
                    }

                    if(sec == 6){
                        // The QUADRATIC function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
                        dp = (-0.00332273)*pp*pp + (0.01146096)*pp + (-0.00790601);
                        
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
                        dp = dp + (0.00100324)*pp + (-0.00102267);
                        
                        
                        // From GitHub_1 for GitHub_2
                        // The QUADRATIC function predicted for Δp_{pro} for [Outbending][Cor = El/Pi+ Cor - Pro Cor (Quad - No Phi - Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
                        dp = dp + ((-1.2336e-03)*pp*pp + (5.0923e-03)*pp + (-8.5287e-03));
                        
                        
                    }

                }
            

                if(corPro == 3){ // Linear Momentum - No Phi Dependence

                    if(sec == 1){
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 1][All Pro Phi Bins] is:
                        dp = (0.00211577)*pp + (-0.00407329);
                    }

                    if(sec == 2){
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 2][All Pro Phi Bins] is:
                        dp = (-0.00304336)*pp + (-0.00083124);
                    }

                    if(sec == 3){
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 3][All Pro Phi Bins] is:
                        dp = (-0.00109669)*pp + (-0.0058555);
                    }

                    if(sec == 4){
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 4][All Pro Phi Bins] is:
                        dp = (0.00012601)*pp + (-0.00523176);
                    }

                    if(sec == 5){
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 5][All Pro Phi Bins] is:
                        dp = (0.00022382)*pp + (-0.00509549);
                    }

                    if(sec == 6){
                        // From VFinal_SP_V2_Pro for VFinal_SP_V3_Pro
                        // The LINEAR function predicted for Δp_{pro} for [Cor = El/Pi+/Pi- Cor (Quad - Quad Phi) - No Pro Cor (Energy Loss Cor)][Sector 6][All Pro Phi Bins] is:
                        dp = (0.00052844)*pp + (-0.0005943);
                    }

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
    #     // corEl == 1 --> No Phi Bins (From Utsav - REMOVED)
    #     // corEl == 3 --> Utsav's Continous Correction (REMOVED)
    #     // corEl == 2 --> Quad Momentum - Quad Phi (Final Version)
    def NameElCor(corEl, datatype):
        coutN = 0
        if('mm0' in corEl):
            coutN = 0
        if('mm1' in corEl):
            coutN = 1
        if('mmPhi' in corEl):
            coutN = 3
        if('mmF' in corEl):
            coutN = 2

        return coutN


    # // corPip ==> Gives the 'generation' of the Pi+ Pion correction
    #     // corPip == 0 --> No Correction
    #     // corPip == 1 --> No Phi Bins (Andrey's Baseline Correction)
    #     // corPip == 2 --> Quad Momentum, Quad Phi (Final Version)
    def NamePipCor(corPip, datatype):
        coutN = 0
        if("Pip" not in corPip):
            coutN = 0
        if('PipMMQ' in corPip):
            coutN = 1
        if('PipMMF' in corPip):
            coutN = 2

        return coutN


    # // corPim ==> Gives the 'generation' of the Pi- Pion correction
    #     // corPim == 0 --> No Correction
    #     // corPim == 1 --> Nick's Quad Momentum, Quad Phi
    #     // corPim == 2 --> Rounded version of corPim == 1 (Not developed yet)
    def NamePimCor(corPim, datatype):
        coutN = 0
        if("Pim" not in corPim):
            coutN = 0
        if('PimMMpim_qPhi' in corPim):
            coutN = 1
        if('PimMMpim_F' in corPim):
            coutN = 2

        return coutN


    # // corPro ==> Gives the 'generation' of the Proton correction
    #     // corPro == 0 --> No Correction
    #     // corPro == 1 --> Quad Momentum, Quad Phi
    #     // corPro == 2 --> Quad Momentum, No Phi
    #     // corPro == 3 --> Linear Momentum, No Phi
    def NameProCor(corPro, datatype):
        coutN = 0
        if("Pro" not in corPro):
            coutN = 0
        if('ProMMpro_qPhi' in corPro):
            coutN = 1
        if('ProMMpro_qNoPhi' in corPro):
            coutN = 2 # Quad - No Phi
        if('ProMMpro_NoPhi' in corPro):
            coutN = 3 # Linear - No Phi

        return coutN


    def CorDpp(Data_Frame, Correction, Out_Type, Channel_Type, MM_Type, Data_Type, Extra_Cut):
        # Correction --> Name of Correction (string)
        # Out_Type --> Desired output of this function
            # Examples:
                # (*) 'MM' --> Missing Mass Calculation (changes with MM_Type)
                # (*) 'D_p' --> ∆P Calculation 
                    # Options are:
                        # 'D_pel' (Default of SP Channel)
                        # 'D_pip' 
                        # 'D_pro' (Default of DP and P0 Channels)
                        # 'D_pim' (NOT AVAILABLE - must use Nick's Code)
                # (*) 'Mom' -> Corrected Momentum (same options as ∆P regarding particle choice - will default to the electron)
                # (*) "WM" --> Invariant Mass      
        # Channel_Type --> Name of channel (i.e., event_type)
        # Data_Type --> Whether the correction is for the 'Inbending' or 'Outbending' data

        Full_Correction_Output = ""

        # Correction Numbers (for code - translating the input string into integers for C++):
        corEl_Num = str(NameElCor(Correction, Data_Type))
        corPip_Num = str(NamePipCor(Correction, Data_Type))
        corPim_Num = str(NamePimCor(Correction, Data_Type))
        corPro_Num = str(NameProCor(Correction, Data_Type))

        # print("Correction by particle is:")
        # print("".join(["El = ", corEl_Num]))
        # print("".join(["Pip = ", corPip_Num]))
        # print("".join(["Pim = ", corPim_Num]))
        # print("".join(["Pro = ", corPro_Num]))


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

        if("P0" not in Channel_Type and ("Mom_el" not in Out_Type and "Mom_pim" not in Out_Type and "Mom_pro" not in Out_Type)):
            Particles_for_Correction = "".join([Particles_for_Correction, """
    auto fpip = dppC(pipx, pipy, pipz, pipsec, 1, """, str(corEl_Num), """, """, str(corPip_Num), """, """, str(corPim_Num), """, """, str(corPro_Num), """) + 1;
    auto pipC = ROOT::Math::PxPyPzMVector(pipx*fpip, pipy*fpip, pipz*fpip, 0.13957);
        """])

        if("DP" in Channel_Type and ("Mom_el" not in Out_Type and "Mom_pip" not in Out_Type and "Mom_pro" not in Out_Type)):
            Particles_for_Correction = "".join([Particles_for_Correction, """
    auto fpim = dppC(pimx, pimy, pimz, pimsec, 2, """, str(corEl_Num), """, """, str(corPip_Num), """, """, str(corPim_Num), """, """, str(corPro_Num), """) + 1;
    auto pimC = ROOT::Math::PxPyPzMVector(pimx*fpim, pimy*fpim, pimz*fpim, 0.13957);
        """])


        if("SP" not in Channel_Type and ("Mom_el" not in Out_Type and "Mom_pip" not in Out_Type and "Mom_pim" not in Out_Type)):
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


        # print("".join(["Corrections in use: \n", Particles_for_Correction]))




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
            if(Channel_Type == "SP"):
                Calculation_Code_Choice = """
    double neutronM2 = 0.9396*0.9396;
                """
                if("D_pip" in Out_Type):
                    ##================================================================================================##
                    ##=====================##         ∆P (Single Pion - π+) Calculations         ##===================##
                    ##================================================================================================##
                    Calculation_Code_Choice = "".join([Calculation_Code_Choice, """

    // Below are the kinematic calculations of the π+ momentum (from el+pro->el+Pip+N) based on the assumption that the π+ angle and electron reconstruction were measured by the detector correctly for elastic events in the epipX channel
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

    // Below are the kinematic calculations of the electron momentum (from el+pro->el+Pip+N) based on the assumption that the electron angle and π+ reconstruction were measured by the detector correctly for elastic events in the epipX channel
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



    // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pip+pim) based on the assumption that the proton angle and electron/π+ reconstruction were measured by the detector correctly for elastic events in the ep->epπ+π- channel 
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


    // Below are the kinematic calculations of the proton momentum (from el+pro->el+pro+pi0) based on the assumption that the proton angle and electron reconstruction were measured by the detector correctly for elastic events in the ep->epπ0 channel
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

    // Below are the kinematic calculations of the electron momentum (from el+pro->el+pro+pi0) based on the assumption that the electron angle and proton reconstruction were measured by the detector correctly for elastic events in the epπ0 channel
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



        ##########################################################################################################
        ##======================================================================================================##
        ##==============##============##         Delta P Calculations (End)         ##============##============##
        ##======================================================================================================##
        ##########################################################################################################


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

    """, "// " if "MM" not in Out_Type else "", """auto beam = ROOT::Math::PxPyPzMVector(0, 0, Beam_Energy, 0);
    """, "// " if "MM" not in Out_Type else "", """auto targ = ROOT::Math::PxPyPzMVector(0, 0, 0, 0.938);
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


        Output = Data_Frame.Define(str(Output_Title), str(Full_Correction_Output))
        if(Extra_Cut != "None" and Extra_Cut != ""):
            Output = Output.Filter(Extra_Cut)

        # # Below is for printing out the code for testing...
        # Output = "".join(["Data_Frame.Define(", str(Output_Title), ", ", str(Full_Correction_Output),")"])

        return Output

    print("Done with Calculations.")
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
        print("".join(["Number of events = ", str(rdf.Count().GetValue())]))
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
            CorrectionName4 = 'No Pro Cor' if event_type != "SP" else ""
            if(('_NoELC' not in CorrectionNameIn and event_type == "DP") or (event_type == "P0")):
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
            if('MMpro_qNoPhi' in CorrectionNameIn):
                CorrectionName4 = 'Pro Cor (Quad - No Phi)'
            if('_NoELC' not in CorrectionNameIn):
                CorrectionName4 = CorrectionName4.replace(")", " - Energy Loss Cor)")

        if(CorrectionName1 == 'Error'):
            print("".join(["Error with the Electron Correction in CorrectionNameInput = ", str(CorrectionNameIn)]))
            CorrectionName1 = "El Cor (ERROR)"

        if(CorrectionName2 == 'Error' and event_type != "P0"):
            print("".join(["Error with the Pi+ Pion Correction in CorrectionNameInput = ", str(CorrectionNameIn)]))
            CorrectionName2 = "Pi+ Cor (ERROR)"

        if(CorrectionName3 == 'Error' and event_type != "P0" and event_type != "SP"):
            print("".join(["Error with the Pi- Pion Correction in CorrectionNameInput = ", str(CorrectionNameIn)]))
            CorrectionName3 = "Pi- Cor (ERROR)"

        if(CorrectionName4 == 'Error' and event_type != "SP"):
            print("".join(["Error with the Proton Correction in CorrectionNameInput = ", str(CorrectionNameIn)]))
            CorrectionName4 = "Pro Cor (ERROR)"

        CorrectionName = "".join([CorrectionName1, " - " if CorrectionName2 != "" else "", CorrectionName2, " - " if CorrectionName3 != "" else "", CorrectionName3, " - " if CorrectionName4 != "" else "", CorrectionName4])
        
        if(event_type == "SP"):
            CorrectionName = "".join([CorrectionName1, " - " if CorrectionName2 != "" else "", CorrectionName2])
        else:
            CorrectionName = "".join([CorrectionName1, " - " if CorrectionName2 != "" else "", CorrectionName2, " - " if CorrectionName3 != "" else "", CorrectionName3, " - " if CorrectionName4 != "" else "", CorrectionName4])


        if(CorrectionName1 == 'El Cor (Quad - Quad Phi)' and CorrectionName2 == 'Pi+ Cor (Quad - Quad Phi)'):
            if(event_type == "SP"):
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

        if(event_type != "SP"):
            if("Energy Loss Cor" not in CorrectionName and '_NoELC' not in CorrectionNameIn):
                CorrectionName = CorrectionName.replace('Pro Cor (Quad - Quad Phi)', 'Pro Cor (Quad - Quad Phi - Energy Loss Cor)')

        

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

    # Other Kinematic Cuts can be made with the variable KFit. 
    # If KFit = 'nf', then only the regular binning cuts will be made by this function.

    
    def regFilter(Bank, Binning, Sector, Region, Shift, KFit, Particle):
        if(KFit == 'nf'):
            Bank1 = Bank
        else:
            Bank1 = Bank.Filter(str(KFit))

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


    ##==========================================================================##
    ##==========##     For 1D Missing Mass Histograms - hmmCall     ##==========##
    ##==========================================================================##


    def histoMakerhmmCall(Bank,Correction,Sector,Region,Shift,Binning,KFit,Particle):

        regionName = ''

        # No Phi Bin Region
        if(Binning == '1'):
            regionName = ''

        # 3 Phi Bin Region
        if(Binning == '3'):

            if(Particle == 'el'):
                if(Region == 'reg1'):
                    regionName = ''.join([' for -5 < #phi_{', str(Particle), '} < 5'])
                if(Region == 'reg2'):
                    regionName = ''.join([' for #phi_{', str(Particle), '} < -5'])
                if(Region == 'reg3'):
                    regionName = ''.join([' for #phi_{', str(Particle), '} > 5'])
            else:
                if(Region == 'reg1'):
                    regionName = ''.join([' for -10 < #phi_{', str(Particle), '} < 10'])
                if(Region == 'reg2'):
                    regionName = ''.join([' for #phi_{', str(Particle), '} < -10'])
                if(Region == 'reg3'):
                    regionName = ''.join([' for #phi_{', str(Particle), '} > 10'])

        # 5 Phi Bin Region
        if(Binning == '5'):
            if(Region == 'reg1'):
                regionName = ''.join([' for -5 < #phi_{', str(Particle), '} < 5'])
            if(Region == 'reg2'):
                regionName = ''.join([' for -15 < #phi_{', str(Particle), '} < -5'])
            if(Region == 'reg3'):
                regionName = ''.join([' for #phi_{', str(Particle), '} < -15'])
            if(Region == 'reg4'):
                regionName = ''.join([' for 5 < #phi_{', str(Particle), '} < 15'])
            if(Region == 'reg5'):
                regionName = ''.join([' for #phi_{', str(Particle), '} > 15'])

        if(Sector == 0):
            SecName = 'All Sectors'
        else:
            SecName = ''.join(['Sector ', str(Sector)])

        CorrrectionName = corNameTitles(Correction)

        name = (Correction, Sector, '', Binning, Region, Particle, '')
        output_title = "".join([datatype, " MM", "^2" if MM_type != "epipX" else "", "_{", str(MM_type), "} ", str(CorrrectionName), " ", str(SecName), str(regionName), ";MM", "^2" if MM_type != "epipX" else "", "_{", str(MM_type), "}"])

        output = Bank.Histo1D(("".join(["hmmCall_", str(name)]), str(output_title), Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max), Correction)


        return output



    ##================================================================================##
    ##==========##     For 1D Missing Mass Histograms - hmmCall (End)     ##==========##
    ##================================================================================##





    ##==========================================================================================##
    ##==========##     For 2D Missing Mass vs Momentum Histograms - hmmCPARTall     ##==========##
    ##==========================================================================================##

    def histoMakerhmmCPARTall(Bank, Correction, Sector, Region, Shift, Binning, Particle_Plot, Particle, KFit):

        # Difference between Particle and Particle_Plot ==> Particle defines which particle is referenced for sectors and phi bins while Particle_Plot refers to which particle momentum will be plotted against

        regionName = ''

        # No Phi Bin Region
        if(Binning == '1'):
            regionName = ''

        # 3 Phi Bin Region
        if(Binning == '3'):

            if(Particle == 'el'):
                if(Region == 'reg1'):
                    regionName = ''.join([' for ', str(Particle) , ' Bin: -5 < #phi_{', str(Particle), '} < 5'])
                if(Region == 'reg2'):
                    regionName = ''.join([' for ', str(Particle) , ' Bin: #phi_{', str(Particle), '} < -5'])
                if(Region == 'reg3'):
                    regionName = ''.join([' for ', str(Particle) , ' Bin: #phi_{', str(Particle), '} > 5'])
            else:
                if(Region == 'reg1'):
                    regionName = ''.join([' for ', str(Particle) , ' Bin: -10 < #phi_{', str(Particle), '} < 10'])
                if(Region == 'reg2'):
                    regionName = ''.join([' for ', str(Particle) , ' Bin: #phi_{', str(Particle), '} < -10'])
                if(Region == 'reg3'):
                    regionName = ''.join([' for ', str(Particle) , ' Bin: #phi_{', str(Particle), '} > 10'])

        # 5 Phi Bin Region
        if(Binning == '5'):

            if(Region == 'reg1'):
                regionName = ''.join([' for ', str(Particle) , ' Bin: -5 < #phi_{', str(Particle), '} < 5'])
            if(Region == 'reg2'):
                regionName = ''.join([' for ', str(Particle) , ' Bin: -15 < #phi_{', str(Particle), '} < -5'])
            if(Region == 'reg3'):
                regionName = ''.join([' for ', str(Particle) , ' Bin: #phi_{', str(Particle), '} < -15'])
            if(Region == 'reg4'):
                regionName = ''.join([' for ', str(Particle) , ' Bin: 5 < #phi_{', str(Particle), '} < 15'])
            if(Region == 'reg5'):
                regionName = ''.join([' for ', str(Particle) , ' Bin: #phi_{', str(Particle), '} > 15'])


        if(Sector == 0):
            SecName = 'All Sectors'
        else:
            SecName = ''.join([str(Particle) , ' Sector ', str(Sector)])


        CorrrectionName = corNameTitles(Correction)


        name = (Correction, Sector, '', Binning, Region, Particle_Plot, Particle, '')
        output_title = "".join([datatype, " MM", "^2" if MM_type != "epipX" else "", "_{", str(MM_type), "} ", str(CorrrectionName), " ", SecName, regionName, ";p_{", Particle_Plot, "} [GeV];MM", "^2" if MM_type != "epipX" else "", "_{", str(MM_type), "}"])

        output = Bank.Histo2D(("".join(["hmmCPARTall_", str(name)]), str(output_title), 200, 2 if 'el' in Particle_Plot else 0, 12 if 'el' in Particle_Plot else 10, Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max), Particle_Plot, Correction)

        return output

    

    ##================================================================================================##
    ##==========##     For 2D Missing Mass vs Momentum Histograms - hmmCPARTall (End)     ##==========##
    ##================================================================================================##





    ##===============================================================================================##
    ##==========##     For 2D Missing Mass vs Theta Angle Histograms - hmmCPARTthall     ##==========##
    ##===============================================================================================##

    def histoMakerhmmCPARTthall(Bank,Correction,Sector,Region,Shift,Binning,Particle,KFit):
        regionName = ''

        # No Phi Bin Region
        if(Binning == '1'):
            regionName = ''

        # 3 Phi Bin Region
        if(Binning == '3'):

            if(Particle == 'el'):
                if(Region == 'reg1'):
                    regionName = ''.join([' for -5 < #phi_{', str(Particle), '} < 5'])
                if(Region == 'reg2'):
                    regionName = ''.join([' for #phi_{', str(Particle), '} < -5'])
                if(Region == 'reg3'):
                    regionName = ''.join([' for #phi_{', str(Particle), '} > 5'])
            else:
                if(Region == 'reg1'):
                    regionName = ''.join([' for -10 < #phi_{', str(Particle), '} < 10'])
                if(Region == 'reg2'):
                    regionName = ''.join([' for #phi_{', str(Particle), '} < -10'])
                if(Region == 'reg3'):
                    regionName = ''.join([' for #phi_{', str(Particle), '} > 10'])

        # 5 Phi Bin Region
        if(Binning == '5'):
            if(Region == 'reg1'):
                regionName = ''.join([' for -5 < #phi_{', str(Particle), '} < 5'])
            if(Region == 'reg2'):
                regionName = ''.join([' for -15 < #phi_{', str(Particle), '} < -5'])
            if(Region == 'reg3'):
                regionName = ''.join([' for #phi_{', str(Particle), '} < -15'])
            if(Region == 'reg4'):
                regionName = ''.join([' for 5 < #phi_{', str(Particle), '} < 15'])
            if(Region == 'reg5'):
                regionName = ''.join([' for #phi_{', str(Particle), '} > 15'])


        if(Sector == 0):
            SecName = 'All Sectors'
        else:
            SecName = ''.join(['Sector ', str(Sector)])

        CorrrectionName = corNameTitles(Correction)


        name = (Correction, Sector, '', Binning, Region, Particle, '')
        output_title = "".join([datatype, " MM", "^2" if MM_type != "epipX" else "", "_{", str(MM_type), "} vs #theta_{", Particle, "} ", str(CorrrectionName), " ", SecName, regionName, ";#theta_{", Particle, "} [#circ];MM", "^2" if MM_type != "epipX" else "", "_{", str(MM_type), "}"])


        output = Bank.Histo2D(("".join(["hmmCPARTthall_", str(name)]), str(output_title), 200, 0, 50, Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max), "".join([Particle, "th"]), mmValue)

        return output

                               

    ##=====================================================================================================##
    ##==========##     For 2D Missing Mass vs Theta Angle Histograms - hmmCPARTthall (End)     ##==========##
    ##=====================================================================================================##





    ##==============================================================================================##
    ##==========##     For 2D Missing Mass vs Phi Angle Histograms - hmmCPARTPhiall     ##==========##
    ##==============================================================================================##

    def histoMakerhmmCPARTPhiall(Bank,Correction,Sector,Region,Shift,Binning,Particle,KFit):

        regionName = ''

        # No Phi Bin Region
        if(Binning == '1'):
            regionName = ''

        # 3 Phi Bin Region
        if(Binning == '3'):
            if(Particle == 'el'):
                if(Region == 'reg1'):
                    regionName = ''.join([' for -5 < #phi_{', str(Particle), '} < 5'])
                if(Region == 'reg2'):
                    regionName = ''.join([' for #phi_{', str(Particle), '} < -5'])
                if(Region == 'reg3'):
                    regionName = ''.join([' for #phi_{', str(Particle), '} > 5'])
            else:
                if(Region == 'reg1'):
                    regionName = ''.join([' for -10 < #phi_{', str(Particle), '} < 10'])
                if(Region == 'reg2'):
                    regionName = ''.join([' for #phi_{', str(Particle), '} < -10'])
                if(Region == 'reg3'):
                    regionName = ''.join([' for #phi_{', str(Particle), '} > 10'])

        # 5 Phi Bin Region
        if(Binning == '5'):
            if(Region == 'reg1'):
                regionName = ''.join([' for -5 < #phi_{', str(Particle), '} < 5'])
            if(Region == 'reg2'):
                regionName = ''.join([' for -15 < #phi_{', str(Particle), '} < -5'])
            if(Region == 'reg3'):
                regionName = ''.join([' for #phi_{', str(Particle), '} < -15'])
            if(Region == 'reg4'):
                regionName = ''.join([' for 5 < #phi_{', str(Particle), '} < 15'])
            if(Region == 'reg5'):
                regionName = ''.join([' for #phi_{', str(Particle), '} > 15'])


        if(Sector == 0):
            SecName = 'All Sectors'
        else:
            SecName = ''.join(['Sector ', str(Sector)])


        CorrrectionName = corNameTitles(Correction)

        name = (Correction, Sector, '', Binning, Region, Particle, '')
        output_title = "".join([datatype, " MM", "^2" if MM_type != "epipX" else "", "_{", str(MM_type), "} vs #phi_{", Particle, "} ", str(CorrrectionName), " ", SecName, regionName, ";#phi_{", Particle, "} [#circ];MM", "^2" if MM_type != "epipX" else "", "_{", str(MM_type), "}"])


        output = Bank.Histo2D(("".join(["hmmCPARTPhiall_", str(name)]), str(output_title), 200, -20, 60, Missing_Mass_bins, Missing_Mass_min, Missing_Mass_max), "".join(["local" if shift != "NS" else "", Particle, "Phi"]), Correction)

        return output



    ##====================================================================================================##
    ##==========##     For 2D Missing Mass vs Phi Angle Histograms - hmmCPARTPhiall (End)     ##==========##
    ##====================================================================================================##





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



    #########################################################################################################################
    ##=====================================================================================================================##
    ##===============##=============##         Exclusivity Cuts (Using MM from eπ+(N))         ##=============##=============##
    ##=====================================================================================================================##
    #########################################################################################################################
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

    
    
    
    
    

    ############################################################################################################################################
    ##=================================================######################################=================================================##
    ##=================================================##                                  ##=================================================##
    ##===============##===============##===============##      Exclusivity Cuts (End)      ##===============##===============##===============##
    ##=================================================##                                  ##=================================================##
    ##=================================================######################################=================================================##
    ############################################################################################################################################


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


    # Delta_Pip_histo_SecList = [1, 2, 3, 4, 5, 6]
    # Delta_Pip_histo_SecList = ['all']



    # # Extra Sector Filter that filters based on Electron Sectors (instead of just Pi+ Sectors). ExtraElectronSecListFilterOn = 'no' turns this option off
    # ExtraElectronSecListFilterOn = 'no'
    ExtraElectronSecListFilterOn = 'yes'
    
    
    if(event_type != "SP"):
        Delta_Pip_histo_SecList = [1, 2, 3, 4, 5, 6] # Only the proton correction is available for the double pion channel (Turned off pi0 channel as well)
        ExtraElectronSecListFilterOn = 'no'
    

    if(ExtraElectronSecListFilterOn == 'yes'):
        ExtraElectronSecListFilter = ['all', 1, 2, 3, 4, 5, 6]
        # ExtraElectronSecListFilter = [1, 2, 3, 4, 5, 6]
    else:
        ExtraElectronSecListFilter = ['all']


    # # Combine Electron and Pi+ Filters? 
    # Combine_el_pip_filters_Q = "yes"
    Combine_el_pip_filters_Q = "no"


    Delta_P_histo_CorList = ['mm0']

    
    
    if(event_type == "SP"):
        if(datatype == "Inbending"):
            # Delta_P_histo_CorList = ['mm0', 'mmPhi_R5_PipMMqPhi_R5', 'mmF', 'mmF_PipMMF']
            Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_PipMMF']


        if(datatype == "Outbending"):
            Delta_P_histo_CorList = ['mm0', 'mmPhi_R2_PipMMqPhi_R2', 'mmF', 'mmF_PipMMF']
            Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_PipMMF']
            
        # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        Delta_P_histo_CompareList = ['pi+', 'el']
        # Delta_P_histo_CompareList = ['el']
        # Delta_P_histo_CompareList = ['pi+']
            
            
    if(event_type == "DP"):
        if(datatype == "Inbending"):
               
#             Delta_P_histo_CorList = ['mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_qPhi', 'mmF_PipMMF_ProMMpro_pi0Phi', 'mmF_PipMMF_ProMMpro_pi2Phi', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_pi0Phi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_pi2Phi']
#             Delta_P_histo_CorList = ['mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi']
            
#             Delta_P_histo_CorList = ['mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_qPhi', 'mmF_PipMMF_ProMMpro_NoPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi']
            
#             Delta_P_histo_CorList = ['mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_qPhi', 'mmF_PipMMF_ProMMpro_NoPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi']
               
#             Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi_NoELC', 'mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi']
            
            
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qNoPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi_NoELC', 'mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qNoPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi']


        if(datatype == "Outbending"):
#             Delta_P_histo_CorList = ['mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi']
#             Delta_P_histo_CorList = ['mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi']
            
#             Delta_P_histo_CorList = ['mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_qPhi', 'mmF_PipMMF_ProMMpro_NoPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi']
            
#             Delta_P_histo_CorList = ['mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_qPhi', 'mmF_PipMMF_ProMMpro_NoPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi']
               
#             Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi_NoELC', 'mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi']
            
            
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qNoPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi_NoELC', 'mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qNoPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi']
            
        # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        Delta_P_histo_CompareList = ['pro']
            
    if(event_type == "P0"):
        if(datatype == "Inbending"):
#             Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_pi0Phi', 'mmF_ProMMpro_pi2Phi']
#             Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi']
            
#             Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_NoPhi']
            
            
            Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_qNoPhi', 'mmF_ProMMpro_NoPhi']
            
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_qPhi_NoELC', 'mmF_ProMMpro_qNoPhi_NoELC', 'mmF_ProMMpro_NoPhi_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_qNoPhi', 'mmF_ProMMpro_NoPhi']

        if(datatype == "Outbending"):
#             Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_pi0Phi', 'mmF_ProMMpro_pi2Phi']
#             Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi']
            
#             Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_NoPhi']
            
            
            Delta_P_histo_CorList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_qNoPhi', 'mmF_ProMMpro_NoPhi']
            
            Delta_P_histo_CorList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_qPhi_NoELC', 'mmF_ProMMpro_qNoPhi_NoELC', 'mmF_ProMMpro_NoPhi_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_qNoPhi', 'mmF_ProMMpro_NoPhi']
            
        # Select which comparisons you would like to see (i.e. which variables would you like to compare to the theoretical calculations)
        # Delta_P_histo_CompareList = ['pro', 'el']
        Delta_P_histo_CompareList = ['pro']












    # Extend range of the 2D histograms? (The 2D histograms are the ∆P values versus the particle's momentum measurements) 
    # For the y-axis to have a user-determined range, let Extend2D_histo = 'y'
    # For the y-axis to have a range of -0.4 to 0.4, let Extend2D_histo = 'n'
        # Note: binning set for the default of 200 bins for a range of -1 to 1
    Extend2D_histo = 'y'

    # Set the extended range:
    extendx_min, extendx_max = -3, 3
    # extendx_min, extendx_max = -1, 1
    # extendx_min, extendx_max = -0.4, 0.4

    NumOfExtendedBins = round((extendx_max - extendx_min)/0.005)


    # For using ShowBackground() with the slices of the extra 2D histograms
    # SBehQ = 'yes'
    SBehQ = 'no'



    # Number of (pi+/pro) phi bins
    NumPhiBins = ['1', '3']
    # NumPhiBins = ['3']
    # NumPhiBins = ['1']


    # # Number of (electron) phi bins
    # To run code normally (without electron phi bins in delta p histograms), let NumPhiBinsEL = ['1'] (anything else will cut histograms based on electron phi angles)
    NumPhiBinsEL = ['1', '3']
    # NumPhiBinsEL = ['3']
    # NumPhiBinsEL = ['1']
    
    if(ExtraElectronSecListFilterOn == 'no'):
        NumPhiBinsEL = ['1']



    ##-----------------------------------------------------------------##
    ##-----##-----## Printing Choices for Delta P Histos ##-----##-----##
    ##-----------------------------------------------------------------##
    if(Delta_P_histo_Q == 'y'):
        print("\n\033[1mFor the ∆P histograms...\033[0m")
        print("".join(["The momentums being calculated are: ", str(Delta_P_histo_CompareList)]))

        print("".join(["The corrections that will run are: ", str(Delta_P_histo_CorList)]))
        print("These Corrections correspond to the following:")
        cor_num = 1
        for cor_names in Delta_P_histo_CorList:
            print("".join(["\t", str(cor_num), ") ", str(cor_names), " -> '", corNameTitles(cor_names), "'"]))
            cor_num += 1
        print("".join(["The ", "Pi+" if event_type == "SP" else "proton", " sectors being run are: ", str(Delta_Pip_histo_SecList)]))
        print("".join(["The electron sectors being run are: ", str(ExtraElectronSecListFilter)]))

        print("".join(["The list of (", "Pi+" if event_type == "SP" else "Proton", ") phi bins that will be run is: ", str(NumPhiBins)]))
        print("".join(["The list of (Electron) phi bins that will be run is: ", str(NumPhiBinsEL)]))

        if(str(SBehQ) != 'no'):
            print("".join(["Running fits with ShowBackground()?: ", str(SBehQ)]))

        if(Extend2D_histo == 'y'):
            print("".join(["\nThe 2D histograms will be have a range of ", str(extendx_min), " < \u0394p < ", str(extendx_max)]))

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

        for correction in Delta_P_histo_CorList:
            for sec in Delta_Pip_histo_SecList:
                for secEL in ExtraElectronSecListFilter:
                    for binning in NumPhiBins:
                        reglist = regList_Call(binning, 'pip' if event_type == "SP" else "pro", 1)
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

                                    if(CutChoice != 'none'):

                                        if('pi+' in Delta_P_histo_CompareList and Delta_Pip_histo_Q == 'y'):
                                            Delta_P_histo_Count += 1
                                            
                                        if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                                            Delta_P_histo_Count += 1

                                        if('el' in Delta_P_histo_CompareList and Delta_Pel_histo_Q == 'y'):
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
    
    if(event_type == "SP"):
        particleList = ['el', 'pip']
        # particleList = ['el']
        # particleList = ['pip']
        # particleList = []
        
        particle_plot_List = ['el', 'pip']
        # particle_plot_List = ['el']
        # particle_plot_List = ['pip']
        # particle_plot_List = []
        
        
    if(event_type == "DP"):
        particleList = ['el', 'pip', 'pro', 'pim']
        # particleList = ['el']
        # particleList = ['pip']
        # particleList = ['pim']
        # particleList = ['pro']
        # particleList = []
        
        particle_plot_List = ['el', 'pip', 'pro', 'pim']
        # particle_plot_List = ['el']
        # particle_plot_List = ['pip']
        # particle_plot_List = ['pim']
        # particle_plot_List = ['pro']
        # particle_plot_List = []
        
        
    if(event_type == "P0"):
        particleList = ['el', 'pro']
        # particleList = ['el']
        # particleList = ['pro']
        # particleList = []
        
        particle_plot_List = ['el', 'pro']
        # particle_plot_List = ['el']
        # particle_plot_List = ['pro']
        # particle_plot_List = []



    correctionList = ['mm0']
    
    
    if(event_type == "SP"):
        if(datatype == "Inbending"):
            # correctionList = ['mm0', 'mmPhi_R5_PipMMqPhi_R5', 'mmF', 'mmF_PipMMF']
            # correctionList = ['mm0', 'mmPhi_R5_PipMMqPhi_R5', 'mmF_PipMMF']
            correctionList = ['mm0', 'mmF', 'mmF_PipMMF']
        if(datatype == "Outbending"):
            # correctionList = ['mm0', 'mmPhi_R2_PipMMqPhi_R2', 'mmF', 'mmF_PipMMF']
            correctionList = ['mm0', 'mmF', 'mmF_PipMMF']
            
    if(event_type == "DP"):
        if(datatype == "Inbending"):
            # correctionList = ['mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_qPhi', 'mmF_PipMMF_ProMMpro_pi0Phi', 'mmF_PipMMF_ProMMpro_pi2Phi', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_pi0Phi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_pi2Phi']
#             correctionList = ['mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi']
#             correctionList = ['mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi', 'mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi_NoELC']
            
            correctionList = ['mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qNoPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi', 'mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qNoPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi_NoELC']
            
        if(datatype == "Outbending"):
#             correctionList = ['mm0', 'mmF_PipMMF', 'mmF_PipMMF_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi']
#             correctionList = ['mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi', 'mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi_NoELC']
            
            correctionList = ['mm0', 'mmF_PipMMF_PimMMpim_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qNoPhi', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi', 'mm0_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_qNoPhi_NoELC', 'mmF_PipMMF_PimMMpim_qPhi_ProMMpro_NoPhi_NoELC']
            
            
    if(event_type == "P0"):
        if(datatype == "Inbending"):
            # correctionList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_pi0Phi', 'mmF_ProMMpro_pi2Phi']
#             correctionList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi']
#             correctionList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_NoPhi']
            
            correctionList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_qNoPhi', 'mmF_ProMMpro_NoPhi']
        
        
            correctionList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_qPhi_NoELC', 'mmF_ProMMpro_qNoPhi_NoELC', 'mmF_ProMMpro_NoPhi_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_qNoPhi', 'mmF_ProMMpro_NoPhi']
            
            
        if(datatype == "Outbending"):
            # correctionList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_pi0Phi', 'mmF_ProMMpro_pi2Phi']
#             correctionList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi']
#             correctionList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_NoPhi']
            
            correctionList = ['mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_qNoPhi', 'mmF_ProMMpro_NoPhi']
        
        
            correctionList = ['mm0_NoELC', 'mmF_NoELC', 'mmF_ProMMpro_qPhi_NoELC', 'mmF_ProMMpro_qNoPhi_NoELC', 'mmF_ProMMpro_NoPhi_NoELC', 'mm0', 'mmF', 'mmF_ProMMpro_qPhi', 'mmF_ProMMpro_qNoPhi', 'mmF_ProMMpro_NoPhi']
            
            
            




    # binningList = ['1','3','5']
    binningList = ['1', '3']
    # binningList = ['3']


    # SecRangeMin = 0 refers to all sectors so the code will start by making histograms that do not filter by sector
    # Any number 1-6 will correspond to the sector of that same number (do not go above 6 or have SecRangeMin>SecRangeMax)
    # If SecRangeMin = SecRangeMax, then only 1 sector (the one specified) will be shown
    # The range of sectors will always be continuous

    SecRangeMin, SecRangeMax = 0, 6





    ##-----------------------------------------------------------------##
    ##=====##=====##     Non-vital Histogram Options     ##=====##=====##
    ##-----------------------------------------------------------------##

    # Letting Run_Phase_Space = 'yes' allows for the histograms without the missing mass values to be run
    Run_Phase_Space = 'yes'
#     Run_Phase_Space = 'no'

#     if(event_type == "P0"):
#         Run_Phase_Space = 'no'

    # This list is for the extra phase space histograms which can be run with or without shifts      
    shiftList = ['', 'S', 'NS']


    # Run with the extra histograms?
    # Letting RunExtra = 'yes' causes the code to also create histograms for missing mass versus the particle angles
    # RunExtra = 'yes'
    RunExtra = 'no'


    ##-----------------------------------------------------------------------##
    ##=====##=====##     Non-vital Histogram Options (End)     ##=====##=====##
    ##-----------------------------------------------------------------------##



    # Use the function ShowBackground? ('yes' or 'no')
    ShowBGq = 'no'
    # ShowBGq = 'yes'


    if(CutChoice == 'none'):
        kinematicFit = ['nf']
    else:
        kinematicFit = ['nf', CutChoice]



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

    SecRangeAll = []
    SecRangeAll.extend(range(SecRangeMin, SecRangeMax + 1))


    if(SecRangeMin == 0 and SecRangeMax > 0):
        SecRangeAll = []
        SecRangeAll.extend(range(SecRangeMin, SecRangeMax + 1))
        StartOfSRR = 0
    if(SecRangeMin > 0):
        SecRangeAll = []
        SecRangeAll.extend(range(SecRangeMin, SecRangeMax + 1))
        StartOfSRR = SecRangeMin - 1
    if(SecRangeMin == 0 and SecRangeMax == 0):
        SecRangeReduce = 'N/A'
        StartOfSRR = SecRangeMin - 1



    if(particleList != []):
        print("\n\033[1mFor the Missing Mass Histograms...\033[0m")
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

        if(Run_Phase_Space == 'yes'):
            print("Will be running the phase space histograms (without missing mass).")

        if(str(ShowBGq) != 'no'):
            print("".join(["Using ShowBackground()?: ", ShowBGq]))

    else:
        print("\n\033[1mNot running Missing Mass Histograms...\033[0m")

    countHisto = 0


    for errorCut in kinematicFit:
        for particle in particle_plot_List:
            for sector in SecRangeAll:
                for correction in correctionList:
                    shift = '' # Corrections are always made using shifted phi
                    for binning in binningList:
                        for particle_filter in particleList:

                            regionList = regList_Call(binning, particle_filter, 1)


                            for region in regionList:

                                if(Print_Names_Of_Histos_To_Be_Made_Q == 'yes'):
                                    print(str((correction, sector, shift, binning, region, particle, particle_filter, errorCut)))

                                if(RunExtra == 'yes'):
                                    countHisto += 3
                                else:
                                    countHisto += 1
                                if(ShowBGq == 'yes' and particle == 'el'):
                                    countHisto += 1


    if(Run_Phase_Space == 'yes'):
        for correction in correctionList:
            for particle in particleList:
                for shift in shiftList:
                    for sector in SecRangeAll:
                        if(sector == 0):
                            if(correction == 'mm0'):
                                countHisto += 3
                            else:
                                countHisto += 2
                        else:
                            if(correction == 'mm0'):
                                countHisto += 3
                            else:
                                countHisto += 2


    print("".join(["\n\033[1mTotal Missing Mass Histograms that will be made: \033[0m", str(countHisto)]))

    print("".join(["\033[1mWith the first half of the code, the total will be: \033[0m", str(Total_Extra + countHisto)]))

    count_Total = Total_Extra + countHisto


    if(datatype == "Inbending"):
        # This number should be set to the number of histograms expected to be made per minute while running this code (VERY rough estimate - often changes between runs)
        TimeToProcess = 720 if("DP" in event_type and file_location != "All") else 747 if("P0" in event_type) else 9.77035490605428
    if(datatype == "Outbending"):
        # This is a VERY rough estimate of the runtime/histogram for when each file is loaded individually (times will vary bases on number of histograms/corrections and the file used)
        TimeToProcess = 1080 if("DP" in event_type and file_location != "All") else 747 if("P0" in event_type) else 17 





    if((count_Total/TimeToProcess) > 1):
        if((count_Total/TimeToProcess) > 60):
            print("".join(["\nEstimated time to run: ", str((round((count_Total/TimeToProcess)/60)) - (round((count_Total/TimeToProcess)/60))%1), " hour(s) and ", str(round(count_Total/TimeToProcess)%60), " mins at a rate of ", str(TimeToProcess), " histograms per minute"]))
        else:
            print("".join(["\nEstimated time to run: ", str(round(count_Total/TimeToProcess)), " mins at a rate of ", str(TimeToProcess), " histograms per minute"]))
    else:
        print("".join(["\nEstimated time to run: ", str(round((count_Total/TimeToProcess)*60)), " seconds at a rate of ", str(TimeToProcess), " histograms per minute"]))


    print("Note: Estimates are based on observations made over time while running this code. Exact times will vary greatly based on choices and file size. (Estimates may also need to be updated after significant changes occur)")



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

    print("\n\033[1mMaking Histograms now...\033[0m")


    #############################################################################################################
    ##=====##=====##=====##=====##=====##     Making Delta P Histograms     ##=====##=====##=====##=====##=====##
    #############################################################################################################

    if(Delta_P_histo_Q == 'y'):

        # Dmom_pip_Histo, Dmom_pip_Histoth, Dmom_pip_HistoPhi = {}, {}, {}
        Dmom_pip_Histo, Dmom_pel_Histo, Dmom_pro_Histo = {}, {}, {}


        print("Making the ∆P Histograms...")
        for correction in Delta_P_histo_CorList:

            correctionNAME = corNameTitles(correction)

            # With this line, the data frame used by the Dp histograms gains an extra cut on the missing mass for mm0 > 1.1
            # Erdf = Dp_Bank_Def(rdf.Filter('epipXC[0].M() < 1.1'), correction, '', Delta_P_histo_CompareList)
            # Erdf = Dp_Bank_Def(rdf.Filter(Calculated_Exclusive_Cuts), correction, '', Delta_P_histo_CompareList)
            
            Erdf = rdf
            if('pi+' in Delta_P_histo_CompareList and Delta_Pip_histo_Q == 'y'):
                Erdf = CorDpp(Erdf, correction, "D_pip", event_type, MM_type, datatype, Calculated_Exclusive_Cuts)
            if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                Erdf = CorDpp(Erdf, correction, "D_pro", event_type, MM_type, datatype, Calculated_Exclusive_Cuts)
            if('el' in Delta_P_histo_CompareList and Delta_Pel_histo_Q == 'y'):
                Erdf = CorDpp(Erdf, correction, "D_pel", event_type, MM_type, datatype, Calculated_Exclusive_Cuts)


            for sec in Delta_Pip_histo_SecList:

                if(sec != "all" and sec != 0):
                    SecName = ''.join(["Pi+" if event_type == "SP" else "Pro", " Sector ", str(sec)])
                else:
                    SecName = ''

                for secEL in ExtraElectronSecListFilter:

                    if(secEL != "all" and secEL != 0):
                        if(sec != "all" and sec != 0):
                            SecName = ''.join(["Pi+" if event_type == "SP" else "Pro", " Sector ", str(sec), " and El Sector ", str(secEL)])
                        else:
                            SecName = ''.join(['El Sector ', str(secEL)])


                    for binning in NumPhiBins:

                        reglist = regList_Call(binning, 'pip' if event_type == "SP" else 'pro', 2)

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
                                        sdf = regFilter(Erdf.Filter("".join(["pip" if event_type == "SP" else "pro", "sec == ", str(sec)])), binning, sec, region, 'S', 'nf', 'pip' if event_type == "SP" else 'pro')
                                    else:
                                        sdf = regFilter(Erdf, binning, sec, region, 'S', 'nf', 'pip' if event_type == "SP" else 'pro')


                                    if(secEL != "all" and secEL != 0):
                                        sdf = sdf.Filter("".join(["esec == ", str(secEL)]))


                                    if(binningEL != '1'):
                                        sdf = regFilter(sdf, binningEL, secEL, regionEL, 'S', 'nf', 'el')
                                        histoName = (correction, '', SecName, binning, region, binningEL, regionEL)
                                    else:
                                        histoName = (correction, '', SecName, binning, region)



                                    if('pi+' in Delta_P_histo_CompareList and Delta_Pip_histo_Q == 'y'):

                                        if(Extend2D_histo == 'y'):
                                            if(binningEL == '1'):
                                                Dmom_pip_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pip_Histo", str(histoName)]), "".join(["(", datatype, ") #Delta p_{pip} vs p_{pip} ", str(SecName), " ", str(correctionNAME), " " ,str(regionName), "; p_{pip}; #Delta p_{pip}"]), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pip', ''.join(['D_pip_', str(correction)]))
                                            else:
                                                Dmom_pip_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pip_Histo", str(histoName)]), "".join(["#splitline{#splitline{(", datatype,") #Delta p_{pip} vs p_{pip} -- ", str(SecName), "}{Correction: ", str(correctionNAME), "}}{Pi+: ", str(regionName) + " -- El: ", str(regionNameEL), "}; p_{pip}; #Delta p_{pip}"]), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pip', ''.join(['D_pip_', str(correction)]))
                                        else:
                                            if(binningEL == '1'):
                                                Dmom_pip_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pip_Histo", str(histoName)]), "".join(["(", datatype, ") #Delta p_{pip} vs p_{pip} ", str(SecName), " ", str(correctionNAME), " ", str(regionName), "; p_{pip}; #Delta p_{pip}"]), 200, 0, 10, 80, -0.4, 0.4), 'pip', ''.join(['D_pip_', str(correction)]))
                                            else:
                                                Dmom_pip_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pip_Histo", str(histoName)]), "".join(["#splitline{#splitline{(", datatype,") #Delta p_{pip} vs p_{pip} -- ", str(SecName), "}{Correction: ", str(correctionNAME), "}}{Pi+: ", str(regionName), " -- El: ", str(regionNameEL), "}; p_{pip}; #Delta p_{pip}"]), 200, 0, 10, 80, -0.4, 0.4), 'pip', ''.join(['D_pip_', str(correction)]))


                                        Delta_P_histo_Count += 1


                                    if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):

                                        if(Extend2D_histo == 'y'):
                                            if(binningEL == '1'):
                                                # Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), "".join(["(", datatype, ") #Delta p_{pro} vs p_{pro} ", str(SecName), " ", str(correctionNAME), " " ,str(regionName), "; ", "p_{pro}" if("_NoELC" in correction) else "Corrected p_{pro}", "; #Delta p_{pro}"]), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pro' if("_NoELC" in correction or event_type == "P0") else "pro_cor", ''.join(['D_pro_', str(correction)]))
                                                Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), "".join(["(", datatype, ") #Delta p_{pro} vs p_{pro} ", str(SecName), " ", str(correctionNAME), " " ,str(regionName), "; ", "p_{pro}" if("_NoELC" in correction) else "Corrected p_{pro}", "; #Delta p_{pro}"]), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pro' if("_NoELC" in correction) else "pro_cor", ''.join(['D_pro_', str(correction)]))
                                            else:
                                                # Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), "".join(["#splitline{#splitline{#Delta p_{pro} vs p_{pro} -- ", str(SecName), "}{Correction: ", str(correctionNAME), "}}{Pro: ", str(regionName) + " -- El: ", str(regionNameEL), "}; ", "p_{pro}" if("_NoELC" in correction) else "Corrected p_{pro}", "; #Delta p_{pro}"]), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pro' if("_NoELC" in correction or event_type == "P0") else "pro_cor", ''.join(['D_pro_', str(correction)]))
                                                Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), "".join(["#splitline{#splitline{#Delta p_{pro} vs p_{pro} -- ", str(SecName), "}{Correction: ", str(correctionNAME), "}}{Pro: ", str(regionName) + " -- El: ", str(regionNameEL), "}; ", "p_{pro}" if("_NoELC" in correction) else "Corrected p_{pro}", "; #Delta p_{pro}"]), 200, 0, 10, NumOfExtendedBins, extendx_min, extendx_max), 'pro' if("_NoELC" in correction) else "pro_cor", ''.join(['D_pro_', str(correction)]))
                                        else:
                                            if(binningEL == '1'):
                                                # Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), "".join(["(", datatype, ") #Delta p_{pro} vs p_{pro} ", str(SecName), " ", str(correctionNAME), " ", str(regionName), "; ", "p_{pro}" if("_NoELC" in correction) else "Corrected p_{pro}", "; #Delta p_{pro}"]), 200, 0, 10, 80, -0.4, 0.4), 'pro' if("_NoELC" in correction or event_type == "P0") else "pro_cor", ''.join(['D_pro_', str(correction)]))
                                                Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), "".join(["(", datatype, ") #Delta p_{pro} vs p_{pro} ", str(SecName), " ", str(correctionNAME), " ", str(regionName), "; ", "p_{pro}" if("_NoELC" in correction) else "Corrected p_{pro}", "; #Delta p_{pro}"]), 200, 0, 10, 80, -0.4, 0.4), 'pro' if("_NoELC" in correction) else "pro_cor", ''.join(['D_pro_', str(correction)]))
                                            else:
                                                # Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), "".join(["#splitline{#splitline{(", datatype,") #Delta p_{pro} vs p_{pro} -- ", str(SecName), "}{Correction: ", str(correctionNAME), "}}{Pro: ", str(regionName), " -- El: ", str(regionNameEL), "}; ", "p_{pro}" if("_NoELC" in correction) else "Corrected p_{pro}", "; #Delta p_{pro}"]), 200, 0, 10, 80, -0.4, 0.4), 'pro' if("_NoELC" in correction or event_type == "P0") else "pro_cor", ''.join(['D_pro_', str(correction)]))
                                                Dmom_pro_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pro_Histo", str(histoName)]), "".join(["#splitline{#splitline{(", datatype,") #Delta p_{pro} vs p_{pro} -- ", str(SecName), "}{Correction: ", str(correctionNAME), "}}{Pro: ", str(regionName), " -- El: ", str(regionNameEL), "}; ", "p_{pro}" if("_NoELC" in correction) else "Corrected p_{pro}", "; #Delta p_{pro}"]), 200, 0, 10, 80, -0.4, 0.4), 'pro' if("_NoELC" in correction) else "pro_cor", ''.join(['D_pro_', str(correction)]))


                                        Delta_P_histo_Count += 1


                                    if('el' in Delta_P_histo_CompareList and Delta_Pel_histo_Q == 'y'):

                                        if(Extend2D_histo == 'y'):
                                            if(binningEL == '1'):
                                                Dmom_pel_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pel_Histo", str(histoName)]), "".join(["(", datatype, ") #Delta p_{el} vs p_{el} ", str(SecName), " ", str(correctionNAME), " ", str(regionName), "; p_{el}; #Delta p_{el}"]), 240, 0, 12, NumOfExtendedBins, extendx_min, extendx_max), 'el', ''.join(['D_pel_', str(correction)]))
                                            else:
                                                Dmom_pel_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pel_Histo", str(histoName)]), "".join(["#splitline{#splitline{(", datatype,") #Delta p_{el} vs p_{el} -- ", str(SecName), "}{Correction: ", str(correctionNAME), "}}{Pi+: ", str(regionName), " -- El: ", str(regionNameEL), "}; p_{el}; #Delta p_{el}"]), 240, 0, 20, NumOfExtendedBins, extendx_min, extendx_max), 'el', ''.join(['D_pel_', str(correction)]))
                                        else:
                                            if(binningEL == '1'):
                                                Dmom_pel_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pel_Histo", str(histoName)]), "".join(["(", datatype, ") #Delta p_{el} vs p_{el} ", str(SecName), " ", str(correctionNAME), " ", str(regionName), "; p_{el}; #Delta p_{el}"]), 240, 0, 12, 80, -0.4, 0.4), 'el', ''.join(['D_pel_', str(correction)]))
                                            else:
                                                Dmom_pel_Histo[histoName] = sdf.Histo2D(("".join(["Dmom_pel_Histo", str(histoName)]), "".join(["#splitline{#splitline{(", datatype,") #Delta p_{el} vs p_{el} -- ", str(SecName), "}{Correction: ", str(correctionNAME), "}}{Pi+: ", str(regionName), " -- El: ", str(regionNameEL), "}; p_{el}; #Delta p_{el}"]), 240, 0, 20, 80, -0.4, 0.4), 'el', ''.join(['D_pel_', str(correction)]))


                                        Delta_P_histo_Count += 1






        print("".join(["Number of ∆P Histograms made: ", str(Delta_P_histo_Count)]))


    ###########################################################################################################
    ##=====##=====##=====##=====##=====##     Made Delta P Histograms     ##=====##=====##=====##=====##=====##
    ###########################################################################################################





    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#





    ##################################################################################################################
    ##=====##=====##=====##=====##=====##     Making Missing Mass Histograms     ##=====##=====##=====##=====##=====##
    ##################################################################################################################


    # hmmCall, hmmCallbg, hmmCPARTall, hmmCPARTthall, hmmCPARTPhiall = {}, {}, {}, {}, {}
    # hmmCPARTall, hmmCPARTthall, hmmCPARTPhiall = {}, {}, {}
    hmmCPARTall = {}
    count = 0


    for errorCut in kinematicFit:
        for particle in particle_plot_List:
            for sector in SecRangeAll:
                if(particle == 'el'):
                    # Rmin, Rmax, dr, secfilter = 2, 9, 1, 'esec'
                    Rmin, Rmax, dr = 2, 9, 1
                if(particle == 'pip'):
                    # Rmin, Rmax, dr, secfilter = 1, 8, 1, 'pipsec'
                    Rmin, Rmax, dr = 1, 8, 1
                if(particle == 'pim'):
                    # Rmin, Rmax, dr, secfilter = 1, 8, 1, 'pimsec'
                    Rmin, Rmax, dr = 1, 8, 1
                if(particle == 'pro'):
                    # Rmin, Rmax, dr, secfilter = 1, 8, 1, 'prosec'
                    Rmin, Rmax, dr = 0, 4.2, 0.6

                for correction in correctionList:
                    shift = '' # Corrections are always made using shifted phi
                    # sdf1 = MM_Bank_Def(rdf, correction, shift)
                    sdf1 = CorDpp(rdf, correction, "MM", event_type, MM_type, datatype, "")

                    for binning in binningList:
                        for particle_filter in particleList:
                            if(particle_filter == 'el'):
                                secfilter = 'esec'
                            if(particle_filter == 'pip'):
                                secfilter = 'pipsec'
                            if(particle_filter == 'pim'):
                                secfilter = 'pimsec'
                            if(particle_filter == 'pro'):
                                secfilter = 'prosec'

                            if(sector == 0):
                                sdf = sdf1
                            if(sector != 0):
                                sdf = sdf1.Filter("".join([secfilter, ' == ', str(sector)]))

                            regionList = regList_Call(binning, particle_filter, 1)

                            for region in regionList:

                                name = (correction, sector, shift, binning, region, particle, particle_filter, errorCut)

                                # if(particle == 'el'):
                                hmmCPARTall[name] = histoMakerhmmCPARTall(regFilter(sdf,binning,sector,region,shift,errorCut,particle_filter),correction,sector,region,shift,binning,particle,particle_filter,errorCut)
                                if(RunExtra == 'yes'):
                                    hmmCPARTthall[name] = histoMakerhmmCPARTthall(regFilter(sdf,binning,sector,region,shift,errorCut,particle),correction,sector,region,shift,binning,particle,errorCut)
                                    hmmCPARTPhiall[name] = histoMakerhmmCPARTPhiall(regFilter(sdf,binning,sector,region,shift,errorCut,particle),correction,sector,region,shift,binning,particle,errorCut)
                                    count += 3
                                else:
                                    count += 1



    # print("Done Making the Missing Mass Histograms.")
    print("".join(["Total Missing Mass Histograms made: ", str(count)]))

    ################################################################################################################
    ##=====##=====##=====##=====##=====##     Made Missing Mass Histograms     ##=====##=====##=====##=====##=====##
    ################################################################################################################





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

        hPARTthall, hPARTPhiall, hPARTthPhiall = {}, {}, {}

        for correction in correctionList:
            for particle in particleList:
                for shift in shiftList:
                    for local_Q in ["", "local "]:
                        if(shift == "NS" and "local" in local_Q):
                            continue

                        for sector in SecRangeAll:
                            if("local" not in local_Q):
                                if(correction == "mm0"):
                                    ref = (sector, particle, shift)
                                else:
                                    ref = (correction, sector, particle, shift)
                            else:
                                if(correction == "mm0"):
                                    ref = (sector, particle, shift, "local")
                                else:
                                    ref = (correction, sector, particle, shift, "local")


                            particle_title = (((particle.replace("el", "El")).replace("pip", "#pi+")).replace("pim", "#pi-")).replace("pro", "Pro")


                            title_theta = "".join(["#splitline{(", datatype, ") ", "#theta_{", particle_title, "} vs p_{", particle_title, "} ", "(All Sectors)" if (sector == 0 or sector == 'all') else "".join(["(Sector ", str(sector),")"]), shiftTitle(shift), "}{Cor: ", corNameTitles(correction), "}; p_{", particle_title, "}; #theta_{", particle_title, "} [#circ]"])
                            title_phi = "".join(["#splitline{(", datatype, ") ", local_Q, "#phi_{", particle_title, "} vs p_{", particle_title, "} ", "(All Sectors)" if (sector == 0 or sector == 'all') else "".join(["(Sector ", str(sector),")"]), shiftTitle(shift), "}{Cor: ", corNameTitles(correction), "}; p_{", particle_title, "}; ", local_Q, "#phi_{", particle_title, "} [#circ]"])
                            title_theta_phi = "".join(["(", datatype, ") ", "#theta_{", particle_title, "} vs ", local_Q, "#phi_{", particle_title, "} ", "(All Sectors)" if (sector == 0 or sector == 'all') else "".join(["(Sector ", str(sector),")"]), shiftTitle(shift), "; ", local_Q, "#phi_{", particle_title, "} [#circ]; #theta_{", particle_title, "} [#circ]"])


                            hPARTthall_ref_title = "".join(["hPARTthall_", particle, "thallSec", str(sector), shift, "" if correction == "mm0" else "".join(["_", correction]), local_Q])
                            hPARTPhiall_ref_title = "".join(["hPARTPhiall_", particle, "PhiSec", str(sector), shift, "" if correction == "mm0" else "".join(["_", correction]), local_Q])
                            hPARTthPhiall_ref_title = "".join(["hPARTthPhiall_", particle, "thPhiSec", str(sector), shift, local_Q])

                            if(sector == 0):
                                sdf = CorDpp(rdf, correction, "".join(["Mom_", particle]), event_type, MM_type, datatype, Calculated_Exclusive_Cuts)
                                # sdf = Extra_Mom_Bank_Def(rdf.Filter(str(Calculated_Exclusive_Cuts)), correction, particle)
                            else:
                                secfilter = "".join([particle.replace("l", ""), "sec"])
                                sdf = CorDpp(rdf.Filter("".join([secfilter, " == ", str(sector)])), correction, "".join(["Mom_", particle]), event_type, MM_type, datatype, Calculated_Exclusive_Cuts)
                                # sdf = Extra_Mom_Bank_Def(rdf.Filter("".join([secfilter, " == ", str(sector)])), correction, particle)


                            hPARTthall[ref] = sdf.Histo2D((hPARTthall_ref_title, title_theta, 110, 0, 11, 100, 0, 40), "".join([particle, "_", correction]), "".join([particle, "th"]))
                            hPARTPhiall[ref] = sdf.Histo2D((hPARTPhiall_ref_title, title_phi, 110, 0, 11, 720, -260, 460), "".join([particle, "_", correction]), "".join([local_Q.replace(" ", ""), particle, "Phi", shift]))
                            count += 2
                            if(correction == 'mm0'):
                                hPARTthPhiall[ref] = sdf.Histo2D((hPARTthPhiall_ref_title, title_theta_phi, 720, -260, 460, 100, 0, 40), "".join([local_Q.replace(" ", ""), particle, "Phi", shift]), "".join([particle, "th"]))
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

        # print("Number of events = " + str(rdf.Count().GetValue()))









    #=======================================================================================================================================================================================================================================================#
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #=======================================================================================================================================================================================================================================================#









    ################################################################################################################################################################
    ##============================================================================================================================================================##
    ##==========##==========##==========##==========##==========##         Saving  Histograms         ##==========##==========##==========##==========##==========##
    ##============================================================================================================================================================##
    ################################################################################################################################################################        
    if(SaveResultsQ == 'yes'):


        print("\n\033[1mSaving Results Now...\033[0m")

        RoutputFile = ROOT.TFile(str(OutputFileName),'recreate')

        countSaved = 0


        # # # # # # # # # # # # # # # # # # # #    For the Delta_p Histograms    # # # # # # # # # # # # # # # # # # # # 

        if(Delta_P_histo_Q == 'y'):  

            for correction in Delta_P_histo_CorList:

                correctionNAME = corNameTitles(correction)

                for sec in Delta_Pip_histo_SecList:

                    if(sec != "all" and sec != 0):
                        SecName = ''.join(["Pi+" if event_type == "SP" else "Pro", ' Sector ', str(sec)])
                    else:
                        SecName = ''

                    for secEL in ExtraElectronSecListFilter:

                        if(secEL != "all" and secEL != 0):
                            if(sec != "all" and sec != 0):
                                SecName = ''.join(["Pi+" if event_type == "SP" else "Pro", ' Sector ', str(sec), ' and El Sector ', str(secEL)])
                            else:
                                SecName = ''.join(['El Sector ', str(secEL)])


                        for binning in NumPhiBins:

                            reglist = regList_Call(binning, "pip" if event_type == "SP" else "pro", 2)


                            # Pi+ Regions
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


                                        if(binningEL != '1'):
                                            histoName = (correction, '', SecName, binning, region, binningEL, regionEL)
                                        else:
                                            histoName = (correction, '', SecName, binning, region)



                                        if('pi+' in Delta_P_histo_CompareList and Delta_Pip_histo_Q == 'y'):
                                            # try:
                                            Dmom_pip_Histo[histoName].Write()
                                            countSaved += 1
                                            # except:
                                            #     print("".join(["Failed to save: Dmom_pip_Histo[", str(histoName), "]"]))

                                        if('pro' in Delta_P_histo_CompareList and Delta_Pro_histo_Q == 'y'):
                                            # try:
                                            Dmom_pro_Histo[histoName].Write()
                                            countSaved += 1
                                            # except:
                                            #     print("".join(["Failed to save: Dmom_pro_Histo[", str(histoName), "]"]))

                                        if('el' in Delta_P_histo_CompareList and Delta_Pel_histo_Q == 'y'):
                                            # try:
                                            Dmom_pel_Histo[histoName].Write()
                                            countSaved += 1
                                            # except:
                                            #     print("".join(["Failed to save: Dmom_pel_Histo[", str(histoName), "]"]))




        # # # # # # # # # # # # # # # # # # Second half of code (Missing Mass Histograms) # # # # # # # # # # # # # # # # # #


        for errorCut in kinematicFit:
            for particle in particle_plot_List:
                for sector in SecRangeAll:

                    for correction in correctionList:
                        shift = '' # Corrections are always made using shifted phi

                        for binning in binningList:
                            for particle_filter in particleList:

                                regionList = regList_Call(binning, particle_filter, 1)

                                for region in regionList:

                                    name = (correction, sector, shift, binning, region, particle, particle_filter, errorCut)

                                    hmmCPARTall[name].Write();
                                    if(RunExtra == 'yes'):
                                        hmmCPARTthall[name].Write();
                                        hmmCPARTPhiall[name].Write();
                                        countSaved += 3
                                    else:
                                        countSaved += 1


        # # # # # # # # # # # # # # #   Other Phase Space Histograms (without Missing Mass)   # # # # # # # # # # # # # # #

        if(Run_Phase_Space == 'yes'):
            for correction in correctionList:
                for particle in particleList:
                    for shift in shiftList:
                        for local_Q in ["", "local "]:
                            if(shift == "NS" and "local" in local_Q):
                                continue
                            for sector in SecRangeAll:
                                if("local" not in local_Q):
                                    if(correction == "mm0"):
                                        ref = (sector, particle, shift)
                                    else:
                                        ref = (correction, sector, particle, shift)
                                else:
                                    if(correction == "mm0"):
                                        ref = (sector, particle, shift, "local")
                                    else:
                                        ref = (correction, sector, particle, shift, "local")
                                hPARTthall[ref].Write()
                                hPARTPhiall[ref].Write()
                                countSaved += 2
                                if(correction == 'mm0'):
                                    hPARTthPhiall[ref].Write()
                                    countSaved += 1

        RoutputFile.Close()

        print("".join(["\033[1mTotal Histograms Saved = \033[0m", str(countSaved)]))

#         else:
#             print("\n\033[1mNo results saved.\033[0m")



    ###############################################################################################################################################################
    ##===========================================================================================================================================================##
    ##==========##==========##==========##==========##==========##         Saved  Histograms         ##==========##==========##==========##==========##==========##
    ##===========================================================================================================================================================##
    ###############################################################################################################################################################
    else:
        print("\n\n\033[1mCode not set to make the histograms at this time.\033[0m")




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
    
Ending Code...
    """]))

