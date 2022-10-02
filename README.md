# Exclusive RG-A Momentum Corrections
Momentum Corrections developed using exclusive pion reactions.


# Plans:
1) Add more README files for side notes (like this)
2) Split the final jupyter notebook into two files (one for ∆P histograms and one for the Missing Mass histograms)
3) Add π0 files (from home directory) to this github (if their size allows)
4) Include a "Images" section on github?
5) Create Corrections based on Elastic Scattering events

## Update Notes:


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





