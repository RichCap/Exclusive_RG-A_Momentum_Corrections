# Exclusive RG-A Momentum Corrections
Momentum Corrections developed using exclusive pion reactions.


# Plans:
1) Add more README files for side notes (like this)
2) Split the final jupyter notebook into two files (one for ∆P histograms and one for the Missing Mass histograms)
3) Add π0 files (from home directory) to this github (if their size allows)
4) Include a "Images" section on github?

## Update Notes:

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





