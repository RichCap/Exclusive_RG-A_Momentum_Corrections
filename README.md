# Exclusive RG-A Momentum Corrections
Momentum Corrections developed using exclusive pion reactions.

Main Correction Code Location: Data_Files/File_Creation_Final_Momentum_Corrections_Github.py
Main Notebook Used to Evaluate Files created with the above python code: Momentum_Corrections_Github_Main.ipynb


# Plans:
1) Add more README files for side notes (like this)
2) Steamline Jupyter Notebook Code to be eaiser to run/modify
    * Currently developing under the name: Momentum_Corrections_Github_Main.ipynb
3) Add π0 files (from home directory) to this github (if their size allows)
4) Create Corrections based on Elastic Scattering events
5) Remove MM_type from list of parameters (integrate into event_type)

## Update Notes:
As of 11-10-2022, all files were moved to the work directory mentioned below.
As of 10-7-2022, the data files used (the outputs of the groovy code) were also saved to the work directory.
Saved here to prevent a loss of files while working on the volitile folder.
Backup File location: /w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections



## Updates from 11-10-2022:
General Updates:
* Needed to copy all files into the work directory to avoid a corruption issue encountered with commiting git updates with the files in the volatile folder
* Pi+ Corrections were completed as of GitHub_Pion_Refinement_V4
Update notes from python script:
* Extra_Part_of_Name = "_GitHub_Pion_Refinement_V3"
    * Refined the Pion Corrections from "GitHub_Pion_Refinement_V1" ("GitHub_Pion_Refinement_V2" refinements were accidentally applied to the electron instead of the pion)
    * Set the initial beam energies used throughout the code at the beginning (based on file input) to avoid issues when loading other (i.e., Spring 2019) datasets
    * Fixed the minor note mentioned for "GitHub_Pion_Refinement_V1"
    
* Extra_Part_of_Name = "_GitHub_Pion_Refinement_V4"
    * Refined the Pion Corrections from "GitHub_Pion_Refinement_V3"
    
* Spring 2019 Updates (Pass 1 and Pass 2):
```
    if(pass_version != "NA" and pass_version != ""):
        Extra_Part_of_Name = "".join(["_GitHub_Spring_2019_Pass_", "1" if("Pass 1" in pass_version) else "2", "_V3"])
        # Fixed initial beam energies (was still using energy from Fall 2018 instead of from Spring 2019)
        # File locations take events from MissingNeutron files instead of the nSidis files (want to switch back to nSidis)
```


## Updates from 11-4-2022:
General Updates:
* Made a Multigraph which plots all 3 phi bins together for the ∆P plots
* Switched the way the ∆P (Pi+) plots are fit (now use the same method as the electron plots)
* Pi+ Kinematics are plotted from 0.75-7.25 GeV (the ∆P plots use increments of 0.5 GeV while the Missing Mass plots use increments of 1 GeV)
Update notes from python script:
* Extra_Part_of_Name = "_GitHub_Pion_Refinement_V1"
    * Created new Pion Corrections using the new electron corrections (and fit methods)
    * Minor issue noticed: there seems to be some print funtion which outputs empty lines during the running of this code - this should not effect the histograms, but is an oddity that I would like to fix (this was not noticed ever before)
    
* Extra_Part_of_Name = "_GitHub_Pion_Refinement_V2"
    * Refined the Pion Corrections from "GitHub_Pion_Refinement_V1"
    * Fixed an issue with 'pass_version' being used with Fall2018 data (code check for pass_version != "NS" instead of pass_version != "NA")
    

## Updates from 10-21-2022:
General Updates:
* Added Code to run Pass 1 and Pass 2 Data from Spring 2019 (full tests not yet complete)
* Improving fits of all 2D histograms (sliced histograms)
* Finalizing Extended Electron Corrections (not done as of this update, but nearing completion - may be done by the next github update...)
* Prior python notes older than those in this update were removed from within the python code
    * See older updates below for their details
    * Updates for "_GitHub_Back_to_Back_Test_V9" and "_GitHub_Cut_Tests_V7" were kept to show the last version of each update name (and because V9 makes these names easy to search for when editting the code)
Update notes from python script:
* Extra_Part_of_Name = "_GitHub_Electron_Refinement_V3"
    * Added new (extended) Electron Momentum Corrections (Kinematic Coverage is: 0.95-9.95 GeV)
    * Not running Electron Only Correction (i.e., 'mmF') for the Single Pion Channel (may run it later during the refinement of the pion corrections)

* Extra_Part_of_Name = "_GitHub_Electron_Refinement_V4"
    * Updated Missing Mass histograms so that their momentum ranges are always from p = 0-12 GeV (does not depend on the plotted particle anymore)
    * Refined Electron Corrections based on Extra_Part_of_Name = "_GitHub_Electron_Refinement_V3"
        (*) Kinematic Coverage changed to: 1.45-9.95 GeV
    * Running the pi+ pion corrections again

* Extra_Part_of_Name = "_GitHub_Electron_Refinement_V5"
    * Doubled the number of bins in the ∆P plots (both in x and y binning for the electron corrections, just in the y binning for all others)
        (*) Changed the range of the electron momentum plotted in the ∆P histograms from 0-12 GeV (with 120 bins total) to the new dimensions of 0.5-10.5 GeV with 400 bins total (bin size is 0.025 GeV/bin)
    * Added the Correction options where only the electron is corrected to the SP channel
    * No new corrections since "_GitHub_Electron_Refinement_V4"

* Extra_Part_of_Name = "_GitHub_Electron_Refinement_V6"
    * Refined the Electron Corrections based on the new fits of the uncorrected ∆P plots
    
* Other Names (specific for certain file inputs):
    * Notes:
        1) event_type == "MC" is for simulated data tests
        2) pass_version is used for the Spring 2019 data (to note the difference between pass1 files and pass2 files)
```
if(event_type == "MC"):
    Extra_Part_of_Name = "_GitHub_MC_Test_V1"
    # Testing the momentum corrections using Monte Carlo files (for use in SIDIS analysis)
    # Runs the same as event_type == "SP"

if(pass_version != "NA" and pass_version != ""):
    Extra_Part_of_Name = "".join(["_GitHub_Spring_2019_Pass_", "1" if("Pass 1" in pass_version) else "2", "_V1"])
    # Testing Spring 2019 data with pass 1 and pass 2 files
```


## Updates from 10-14-2022:
General Updates:
* Combined the Electron Only Electron Corrections with new Single Pion Electron Correction (files produced using skim4 which had fewer cuts)
    * New Corrections have much wider coverage (up to p = 9.95 GeV)
    * Code was update such that these corrections can be produced (results of fits have not been added back to the python script)
    * The directory for the skim4 Inbending Files were added to this repository (files created using the same files used to create the Elastic Scattering/Electron Only Files)
* The Universal Jupyter Notebook code has been updated to create phi-dependent corrections again 
    * Another update is still needed to plot each phi bin together for ∆P plots
* More options are available to see plots with and without certain cuts, but the code will skip options which apply a variable cut on a plot/histogram containing information about that variable
* More features added to help provide consistency between different channels and images for the Jupyter Notebook
Update notes given in the python Code:
* Extra_Part_of_Name = "_GitHub_Cut_Tests_V5"
    * Changed the base invariant mass cut to be wider (range extended to W < 1.8 GeV - does not affect existing cuts)
    * Suppressed histograms with cuts that were made with the same variable being plotted
    * Turned off phase space histograms (to run faster)
    * Turned off some cuts - Running the code with the following cuts (only):
        (*) No (Additonal) Cuts
        (*) Calculated Exclusivity Cuts
        (*) Azimuthal Kinematic Cut
        (*) Calculated Polar Kinematic Cut
        (*) Azimuthal and Polar Angle Cuts
        (*) All Additional Cuts)
    * Changed which corrections are being applied to the histograms (without the proton, only electron corrections are needed for ∆P and Invariant Mass)
    * Turned off extra angle calculation types (just V1 and V3 are running - these are the only working versions of ∆Theta and ∆Phi)
    * Only ran for the "ES" channel (not "EO")

* Extra_Part_of_Name = "_GitHub_Cut_Tests_V6"
    * The basic Invariant Mass cut is now not made automatically --> testing new cut which is just a basic cut at W < 0.7 GeV and W > 1.4 GeV (called "Calculated_Exclusive_Cuts_V2")
    * Updated the tighter Invariant Mass cut using the Invariant mass plots from the tagged proton channel (i.e., "ES")
    * Increased the range of the y-axis of the ∆P plots (increased to ±2 GeV with the same sizes of binning)
    * Turned the phase space histograms back on

* Extra_Part_of_Name = "_GitHub_Cut_Tests_V7"
    * Made the basic Invariant Mass cut tighter (i.e., "Calculated_Exclusive_Cuts_V2" --> W < 0.7 GeV and W > 1.2 GeV)
    * Decreased the range of the y-axis of the ∆P plots (decreased to ±1 GeV with the same sizes of binning --> the ideal may be even lower as all desirable events are between ±0.3 Gev but the range has been extended to see more when necessary)

* Extra_Part_of_Name = "_GitHub_Electron_Refinement_V1"
    * Reintroduced the automatic baseline cut on Invariant Mass for elastic channels (W < 0.6 GeV and W > 1.3 GeV --- "Calculated_Exclusive_Cuts_V2" is not effected)
    * Increased the bin sizes along the y-axis of the ∆P plots for the non-elastic channels (same bin ranges as before, but the bin sizes are now consistent with those from the elastic scattering channels)
        (*) Other similar updates were also added so that these channels will produce plots which are consistent with the elastic scattering events
    * Running with electron phi bins
    * Phase space histograms now only create a plot for sector 0 (i.e., all sectors -- Optional condition that can be turned off -- does not affect other options)
    * Only running electron kinematics and corrections (for elastic and single pion channels -- Pi+ corrections are included in the SP channel)
    * Updated the default location of the SP files (compatible with current file names for the SP files made with the groovy script)

* Extra_Part_of_Name = "_GitHub_Electron_Refinement_V2"
    * Minor update to histogram titles (related to the phi binning parts of titles)
    * Updated SP files to take in files using skim4 data (files which did not have the W cuts applied)

## Updates from 10-4-2022:
General Updates:
* Ran the "Electron Only" file options (updated all programs to be compatible with this option)
* Deleted old code from the main jupyter notebook (from how the code used to run - Momentum_Corrections_Github_Main.ipynb now runs the majority of the histograms within one cell)
    * Some old cells have only been commented out and still need to be fully deleted
    * Momentum_Corrections_Github_Missing_Mass_Only.ipynb still contains a recent version of these cell and has not been deleted from the repository yet (has been deleted/renamed in the working directory)
* Improve the fitting procedures for the invariant mass plots (specifically for the elastic events "ES")
Update notes given in the python Code:
* Extra_Part_of_Name = "_GitHub_Cut_Tests_V4"
    1) Added New Invariant Mass Cuts based on the cuts from "_GitHub_Cut_Tests_V3"
        * 3 options of Invariant Mass Cuts have been added based on combinations of the above cuts
    2) Turned back on 'phase space' plots but turned off Missing Mass plots (using Invariant Mass instead)


## Updates from 10-3-2022:
Updates to repository:
* Changed the name of "Momentum_Corrections_Github_Missing_Mass_Only.ipynb" to "Momentum_Corrections_Github_Main.ipynb"
* Added Image Folder to save images to github
* Added new event type "EO" --> Electron Only
    * To be used for elastic scattering corrections
    * Files do not tag the proton, but are otherwise identical to the files created for the "ES" option (elastic scattering)
Update notes given in the python Code:
* Extra_Part_of_Name = "_GitHub_Cut_Tests_V1"
    1) Added a base Invariant Mass Cut that is always applied to the Elastic Events (WM range is set to be between at least 0.6 and 1.3 GeV always)
    2) Removed options to plot versus proton momentum and with any additional cuts (done for time constraints)
* Extra_Part_of_Name = "_GitHub_Cut_Tests_V2"
    1) Added New ∆Phi Cuts with more momentum bins
    2) Only the above cut (and the baseline cut from "_GitHub_Cut_Tests_V1") was run
* Extra_Part_of_Name = "_GitHub_Cut_Tests_V3"
    1) Added New ∆Theta Cuts based on the cuts from "_GitHub_Cut_Tests_V2"
    2) Turned off 'phase space' plots (plots that did not involve ∆P, ∆Theta, ∆Phi, or Invariant/Missing Mass)


### Update from 10-2-2022:
Update notes given in the python Code:
* Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V8"
    1) Had to update the newest ∆Theta_Pro calculation (did not work again)
    2) Updated the way that the default histogram titles were made
    3) Changed the ranges on some histograms
* Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V9"
    1) Increased the number of bins used in the ∆Theta_Pro Histograms
    2) Added an additional exclusivity cut (CutChoice_2) based on ∆Theta Calculation (D_Angle_V1)
    3) Exclusivity Cuts now do not use linear or quadratic equations, but instead use the gaussian widths of the fitted histograms
    4) "Cut_Function" now supports a combination of all of these added cuts (names updated somewhat from V8 to differentiate between all of the cut options)
    5) Removed Phi binning from the Elastic Channel (option was not being used)


### Updates up to 9-29-2022 (commit 2):
1) Added another version of ∆Theta_pro calculation ("D_Angle_V3" gives the proper ∆Phi histograms while "D_Angle_V4" gives the proper ∆Theta_pro calculations)
2) D_Angle plots are now plotted vs the electron momentum (even if calculating proton angle)
3) Multiple exclusivity cuts can now be applied seperately and together
4) Removed the Back-to-Back SECTOR cut (was an automated cut that is covered more directly by other existing cuts)
5) Reduced number of corrections being run
6) Removed old code that was no longer in use including:
    * 1D Missing Mass Histograms
    * Missing Mass vs Particle Angles (theta and phi)
7) Changed how the kinematic momentum/angle plots are named and made (better naming convensions used)
    * hPARTthall -> Histo_P_v_Th
    * hPARTPhiall -> Histo_P_v_Phi
    * hPARTthPhiall -> Histo_Th_v_Phi
    * histoMakerhmmCPARTall -> Missing_Mass_Histo_Maker
8) Name is now: Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V7"


### Updates up to 9-29-2022:
#### General:
1) Momentum_Corrections_Github_Missing_Mass_Only.ipynb is being used as a condensed version of the jupyter code (will eventually simplify all previous code into a single cell/output)
    * Currently missing some old options such as printing ∆P ad function of phi (to be updated later)
2) Focus has been placed on the Elastic Channel
#### Other updates since last note (sorted based on the file name used when running File_Creation_Final_Momentum_Corrections_Github.py - Oldest to Newest)
* Extra_Part_of_Name = "_GitHub_Elastic"
    (*) Created Elastic Scattering Options/Calculations
    (*) Invariant Mass Cut of W < 3 GeV is now an option for any channel
* Extra_Part_of_Name = "_GitHub_Elastic_V2"
    (*) Removed Invariant Mass Cuts (checking statistics with existing PID cuts)
* Extra_Part_of_Name = "_GitHub_Elastic_V3"
    (*) Added new Missing Mass cuts to files that still required the protons be in the forward detector (for cut comparison)
* Extra_Part_of_Name = "_GitHub_Elastic_CD_V1"
    (*) Using elastic groovy files that do not use the forward detector requirement in proton PID cuts (did not add the Invariant Mass Cuts back yet)
* Extra_Part_of_Name = "_GitHub_Elastic_CD_V2"
    (*) Added the Invariant Mass Cuts back to the same files used by "_GitHub_Elastic_CD_V1"
* Extra_Part_of_Name = "_GitHub_Elastic_CD_New_V1"
    (*) Kept the Invariant Mass Cuts and changed the input files (used files without the OkForAsymmetry cuts)
* Extra_Part_of_Name = "_GitHub_Valerii_V1"
    (*) Using same files used by Valerii for the elastic corrections (same cuts as the versions above)
* Extra_Part_of_Name = "_GitHub_Valerii_V2"
    (*) Using same files used by Valerii for the elastic corrections (cuts at the level of the groovy code are unchanged)
    (*) Added new Invariant Mass cuts based on the proton momentum
* Extra_Part_of_Name = "_GitHub_Valerii_V3"
    (*) Using same files used by Valerii for the elastic corrections (cuts at the level of the groovy code are unchanged)
    (*) Removed old (general) Invariant mass cut (this version only uses the calculated cuts)
    (*) Needs to fix an issue with abnormally low event counts for electron momentums (lower than the same plots using the proton momentums)
* Extra_Part_of_Name = "_GitHub_Valerii_V4"
    (*) Using same files used by Valerii for the elastic corrections (cuts at the level of the groovy code are unchanged)
    (*) Reduced the x and y binning (y by a factor of 2, x by a factor of 10) of the ∆P plots (elastic electron only)
    (*) ∆P plots with phi dependence have been turned off - also reduced their momentum range (was set to 20 GeV instead of 12 GeV) <-- Electron only (new changes will only affect the elastic channel - old channels were kept the same for consistency) 
* Extra_Part_of_Name = "_GitHub_Valerii_V5"
    (*) Using same files used by Valerii for the elastic corrections but more files were run (missing files were recovered)
    (*) Modified the Invariant Mass cuts to be based on the electron momentum
    (*) Testing first type of elastic electron correction based on "_GitHub_Valerii_V4"
* Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V1"
    (*) Using same files used by Valerii for the elastic corrections but more files were run (missing files were recovered)
    (*) Added new back-to-back cuts based on the electron's and proton's theta angles (should add up to about 180˚ with the current condition giving a ±5˚ margin of error)
* Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V2"
    (*) Using same files used by Valerii for the elastic corrections but more files were run (missing files were recovered)
    (*) Replaced the last cut with the particle angles with a cut on particle sectors and testing new cuts on the calculated proton angle (∆Theta_Proton < 5˚)
    (*) Also simplified how the histograms are eventually saved (added an option to print/test the histograms to be saved)
    (*) Started to add code to create ∆Theta histograms for more refined exclusive elastic cuts (still being developed)
* Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V3"
    (*) Using same files used by Valerii for the elastic corrections but more files were run (missing files were recovered)
    (*) Last cuts on the calculated proton angle (∆Theta_Proton < 5˚) did not work =====> Changed how ∆Theta_Proton is calculated (now does not use electron info) - Also changed the cut to 10˚ instead of 5˚
    (*) Added ∆Theta histograms for more refined exclusive elastic cuts (still use the prior method of calculating ∆Theta_Proton)
* Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V4"
    (*) Using same files used by Valerii for the elastic corrections but more files were run (missing files were recovered)
    (*) Replaced the calculated proton angle cuts with another back-to-back cut on the absolute difference in the azimuthal angles of each particle =====> CutChoice is that this ∆Phi should be about 180˚ ±5˚
    (*) Changed ∆Theta histograms to being ∆Angle histograms (added ∆Phi to the ∆Theta versions of the caclculation)
* Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V5"
    (*) Using same files used by Valerii for the elastic corrections but more files were run (missing files were recovered)
    (*) Back-to-back cut now features a cut on the absolute difference of the phi angles of the elastic particles (cut is a pol2 function of the proton momentum - unique to each proton sector AND cuts off for |∆Phi - 180| > 5˚)
    (*) Modified the Invariant Mass cut using prior back-to-back cut (|∆Phi - 180| > 5˚)
* Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V6"
    (*) Using same files used by Valerii for the elastic corrections but more files were run (missing files were recovered)
    (*) Back-to-back cut now features a cut on the absolute difference of the phi angles of the elastic particles (cut is a pol2 function of the proton momentum - cut is now tighter than the previous version - unique to each proton sector AND cuts off for |∆Phi - 180| > 3˚)
    (*) Modified the Invariant Mass cut using prior back-to-back cut
All of the above notes (from before "_GitHub_Back_to_Back_Test_V1") were removed on this date



### On 8-25-2022:
1) Updates to python code:
    * SP File location added (files are not located within these repositories on GitHub)
    * Created Elastic Scattering Options/Calculations
    * Invariant Mass Cut of W < 3 GeV is now an option for any channel
    * Created Invariant Mass Histograms options (has tighter cuts on W than the optional cut stated above - i.e., from 0.7 GeV < W < 1.3 GeV)
    * File Name = "_GitHub_Elastic"
2) Added Elastic Scattering Data Folder
    * Files not created yet



### On 8-21-2022:
1) Updates to python code:
    * Added Invariant Mass Cut of W < 3 GeV to Single Pion Channel (to study the effects of Inclusive reactions)
    * File Name = "_GitHub_SP_New_W"
2) Added Single Pion Data Folders
    * Running now (not finished)
    * Python code has not been updated to refer to these files (still refer to old files that may or may not exist on the volitile folder)
    
    

### On 8-15-2022:
1) Updates to python code:
    * Final versions of the momentum corrections have been created
    * Final corrections are included in the new python file called: File_Creation_Final_Momentum_Corrections_Github.py
        * Includes the most simplied version of the corrections (condensed to fewer number of lines)
    * Latest output files include the following name: Extra_Part_of_Name = "_GitHub_F2_Pro"
2) Updates to jupyter notebook:
    * Correction output now prints in scientific notation with a limited number of sig figs
    * Removed more unnecessary parts of the code
    * Preparing to split the Missing Mass Histograms and ∆P histograms into two separate files
    * Current options selected will show all of the most relevant histograms for the proton corrections (using mainly the double pion data)
        * Can switch between Inbending/Outbending and Double Pion/π0 Channels from one cell (See: Choice of File/Data types)
3) Current evaluation of corrections:
    * Electron/π+/Proton Corrections are complete
        * π- Correction may be updated later (work done by Nick)
        * May add boundries of the corrections directly to the code (furthur discussion with group is required)
    * Planned updates will consist of cosmetic updates to images or a reduction to the number of lines required for each correction
        
    

### On 8-11-2022:
1) Updates to python code:
    * Updated both inbending and outbending proton corrections (without phi dependance)
    * Also updated time estimation of code (minor edit)
2) Updates to jupyter notebook:
    * Updated some cells/options and fixed (possible) issues with some parts of the correction generating code
3) Current evaluation of corrections:
    * Outbending Proton corrections work well for double pion channel in terms of Proton AND Electron Bins/Sectors
        * Would have left as it was, however, the π0 channel was not as well off, so an additional correction was added
    * Outbending Proton corrections work well for double pion channel in terms of Proton AND Electron Bins/Sectors

### On 8-10-2022:
#### As of 8:00 pm
* Edited the jupyter notebook file and the python script (cleaned up old/outdated code)
    * python code less effected than the jupyter notebook
* Reran all code (final output files not available due to size)
#### As of 11:00 am:
* Added all (existing) files to this github
    * More may come/change as updates are made
* Some files may not work properly due to changes to file location (work being done to localize the code to work in any directory)





