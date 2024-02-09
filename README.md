# Exclusive RG-A Momentum Corrections
Momentum Corrections developed using exclusive pion reactions.

Main Correction Code Location: Data_Files/File_Creation_Final_Momentum_Corrections_Github.py

Main Notebook Used to Evaluate Files created with the above python code: Momentum_Corrections_Github_Main.ipynb


# Plans:
1) Work on Pass2 Corrections for the Spring 2019 Data
    * Also comparing with Pass1 Spring 2019 Data
    * Planning to test data which includes the central detector events
2) Start Pass2 Corrections for the Fall 2018 Data once available

## Update Notes:
As of 10-27-2023:
    * Updated the Exclusivity Cuts in the Spring 2019 datasets and made a new default Missing Mass Cut for all Single Pion Files
        * The default cut filters all events with an uncorrected missing mass of more than 1.8 GeV
        * Reason for new default cut: The phase space histograms were showing many events (particularly at low electron momentum) which were clearly not appearing in any other relevant histograms
            * Made this cut to help better represent the actual events being included while not cutting too tightly as to have any significant chances of effecting the other plots accidentally

As of 10-23-2023:
    * Correction Progress:
        * Fall 2018   - Pass 1 corrections are COMPLETED
        * Fall 2018   - Pass 2 corrections not yet made (not begun)
        * Spring 2019 - Pass 1 corrections not yet made (not begun)
        * Spring 2019 - Pass 2 corrections are IN-DEVELOPMENT now
    * Deleted Some older images from this repository (were not really needed here)

As of 9-19-2023, the all Fall 2018 Pass1 corrections are complete (this README.md file has not been kept regularly updated for a few months)

As of 11-10-2022, all files were moved to the work directory mentioned below. 

As of 10-7-2022, the data files used (the outputs of the groovy code) were also saved to the work directory.

Saved here to prevent a loss of files while working on the volitile folder.

Backup File location: /w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections



## Updates from 10-23-2023
* The following file names/info detail (most) changes since the last update to this README.md file (all still appear in the python code as of this update):
```
    # New Names as of 9-19-2023 (After Fall 2018 - Pass 1 corrections were finished)
    if("Pass" in str(pass_version)):
        Pass_File_Name     = (...)
        
        Extra_Version_Name = "_V1"
        # Ran on 9/19/2023-9/20/2023 with Spring 2019 data (Pass 2)
            # Ran 3 versions of files for SP and EO events (6 files total)
                # Included normal code (no changes since the last time it was run) and 2 versions where cuts to check the central/forward detector separately (via theta cuts) were added
                # Note: Later change was made to the Central detector cuts to remove the condition that the electron be detected there (no events were suriving the cut)
                    # This change was updated for only the SP events (Central EO would be the same as the other files if the cut was removed)
                    # Didn't matter since the central detector was cut in the groovy script already (did not remove the cut beforehand)
                    
                    
        Extra_Version_Name = "_V2"
        # Ran on 9/21/2023 with Spring 2019 data (Pass 2)
        # Added Refinements to the earlier Pass 2 Corrections (added phi-dependence)
            # Correction name is 'mmRP2' for 'Refined'-'Pass 2'
        # Extended the plot range of the theta particle in relavent plots (will help see the central detector particles later)
        
        
        Extra_Version_Name = "_V3"
        # Ran on 9/22/2023 with Spring 2019 data (Pass 2)
        # Refined the phi-dependent Pass 2 Correction again
            # Correction is still called 'mmRP2'
            
            
        Extra_Version_Name = "_V4"
        # Ran on 9/29/2023 with Spring 2019 data (Pass 2)
        # Added a pi+ phi-dependent Correction based on 'mmRP2'
        # Needed to test a potential issue in the Inbending pi+ corrections
            # Testing to see what the differences are between 'PipMMF', 'PipMMExF', and 'PipMMEF' in case the Inbending corrections for 'PipMMF' and 'PipMMEF' are the same (possible naming error in Inbending Pass 1)
                # RESULT OF TEST: The issue did NOT exist when finalizing the Pass 1 Corrections. It does, however, exist now such that the 'PipMMEF' correction no longer works the same as it did when finalizing the results
                    # The issue must have been created while working on the Outbending corrections with the Inbending code never having been readdressed and fixed before this point
                    # The issue has been resolved (for the next file version) and since the pion correction has not been used to develop new corrections yet, this presents no concerns for the status of the Pass 2 corrections
                    
                    
        Extra_Version_Name = "_V5"
        # Ran on 10/5/2023 with Spring 2019 data (Pass 2 AND Pass 1)
        # Refined the pi+ phi-dependent Correction based on 'mmRP2_PipMMP2'
            # Name has not been changed
        # Fixed the issue noted in the 'RESULT OF TEST' section of the 'Extra_Version_Name = "_V4"' notes
            # No longer using the extra corrections ('ExF') now that the test is complete
        # Finished creating the Pass 1 version of the required files
            # Ran with Pass 2 versions
            # Included the Pass 2 versions of the corrections to test how compatile they are (no existing Pass 1 corrections to compare otherwise)
            
            
        Extra_Version_Name = "_V6"
        # Ran on 10/16/2023 with Spring 2019 data (Pass 2 and Pass 1)
        # Made a new refinement correction for the pi+ pion based on 'mmRP2_PipMMP2'
            # Called 'mmRP2_PipMMsP2'
            # This correction splits the data to create separate corrections based on whether the pion momentum is above or below 4 GeV
            # As of this file, the refinement only is applied if pip >= 4
        # No new Pass 1 corrections were made
            # Now not running Pass 2 corrections for any pass 1 data set
        # Now running sector-by-sector phase space plots to try to find the issue with the pipPhi angle favoring larger values
        
        
        Extra_Version_Name = "_V7"
        # Running on 10/23/2023 with Spring 2019 data (Pass 2 and Pass 1)
        # Did not update the new refinement correction for the pi+ pion from the last version
            # Correction 'mmRP2_PipMMsP2' is still the same as it was in Extra_Version_Name = "_V6"
        # No new corrections/refinements were made (for either Pass version)
            # Still using all the same corrections and histograms as was used in Extra_Version_Name = "_V6"
        # Modified the Missing/Invariant Mass Exclusivity Cuts for the Spring 2019 data
            # Was still using the same cuts as the Pass 1 Fall 2018 data
            # Cuts are now unique between datasets and pass versions
                # Will still have the same name (must keep track of file version to track difference in the exclusivity cuts)
            # Single Pion Channels have cuts which are functions of electron sector, local phi angle, and momentum
                # phi-dependence is not continuous
                # Linear dependence on momentum
                # Cuts are from fits of the widths of the peak distributions (boundaries are taken from 3-sigma widths in both directions)
            # Electron Only/Elastic Scattering Channels have cuts which are functions of electron sector and momentum
                # No phi-dependence
                # Linear dependence on momentum for the upper cut, cut is constant in momentum for the lower cut
                # Cuts are from fits of the widths of the peak distributions (boundaries are taken from a 2-sigma width for the upper cut and a 3-sigma width for the lower cut)
        # Updated the time-estimates for running the code
            # Does not impact how the code runs
            # Just helps predict the amount of time that will be required to run when running the code as a test
        
        
        Extra_Part_of_Name = "".join(["_", str(Pass_File_Name), "_rec_clas", str(Extra_Version_Name)])
        # 'rec_clas' refers to the DST files used to create the root files in this code
            # The DST files are what was used instead of the skim4 or nSidis files since there was not any current versions of the skim files without the cuts I wanted removed
        # Refer to Extra_Version_Name above for version notes
    else:
        Extra_Part_of_Name = "_Pass1_Final_Tests_V1"
        # Ran with Extra_Version_Name = "_V4" above (with Pass 1 Fall 2018 data)
            # RESULT OF TEST: The issue did NOT exist when finalizing the Pass 1 Corrections. It does, however, exist now such that the 'PipMMEF' correction no longer works the same as it did when finalizing the results
                # The issue must have been created while working on the Outbending corrections with the Inbending code never having been readdressed and fixed before this point
                # The issue has been resolved (for the next file version) and since the pion correction has not been used to develop new corrections yet, this presents no concerns for the status of the Pass 2 corrections
```

## Updates from 9-19-2023
* The following file names/info has been removed from the main python file (cleaning up unnecessary clutter):
```
    Extra_Part_of_Name = "_GitHub_Back_to_Back_Test_V9"
    # Increased the number of bins used in the ∆Theta_Pro Histograms
    # Added an additional exclusivity cut (CutChoice_2) based on ∆Theta Calculation (D_Angle_V1)
    # Exclusivity Cuts now do not use linear or quadratic equations, but instead use the gaussian widths of the fitted histograms
    # "Cut_Function" now supports a combination of all of these added cuts (names updated somewhat from V8 to differentiate between all of the cut options)
    # Removed Phi binning from the Elastic Channel (option was not being used)
    
    Extra_Part_of_Name = "_GitHub_Cut_Tests_V7"
    # Made the basic Invariant Mass cut tighter (i.e., "Calculated_Exclusive_Cuts_v2" --> W < 0.7 GeV and W > 1.2 GeV)
    # Decreased the range of the y-axis of the ∆P plots (decreased to ±1 GeV with the same sizes of binning --> the ideal may be even lower as all desirable events are between ±0.3 Gev but the range has been extended to see more when necessary)
    
    Extra_Part_of_Name = "_GitHub_Electron_Refinement_V1"
    # Reintroduced the automatic baseline cut on Invariant Mass for elastic channels (W < 0.6 GeV and W > 1.3 GeV --- "Calculated_Exclusive_Cuts_v2" is not effected)
    # Increased the bin sizes along the y-axis of the ∆P plots for the non-elastic channels (same bin ranges as before, but the bin sizes are now consistent with those from the elastic scattering channels)
        # Other similar updates were also added so that these channels will produce plots which are consistent with the elastic scattering events
    # Running with electron phi bins
    # Phase space histograms now only create a plot for sector 0 (i.e., all sectors -- Optional condition that can be turned off -- does not affect other options)
    # Only running electron kinematics and corrections (for elastic and single pion channels -- Pi+ corrections are included in the SP channel)
    # Updated the default location of the SP files (compatible with current file names for the SP files made with the groovy script)
    
    Extra_Part_of_Name = "_GitHub_Electron_Refinement_V2"
    # Minor update to histogram titles (related to the phi binning parts of titles)
    # Updated SP files to take in files using skim4 data (files which did not have the W cuts applied)
    
    Extra_Part_of_Name = "_GitHub_Electron_Refinement_V3"
    # Added new (extended) Electron Momentum Corrections (Kinematic Coverage is: 0.95-9.95 GeV)
    # Not running Electron Only Correction (i.e., 'mmF') for the Single Pion Channel (may run it later during the refinement of the pion corrections)
    
    Extra_Part_of_Name = "_GitHub_Electron_Refinement_V4"
    # Updated Missing Mass histograms so that their momentum ranges are always from p = 0-12 GeV (does not depend on the plotted particle anymore)
    # Refined Electron Corrections based on Extra_Part_of_Name = "_GitHub_Electron_Refinement_V3"
        # (Kinematic Coverage changed to: 1.45-9.95 GeV)
    # Running the pi+ pion corrections again
    
    Extra_Part_of_Name = "_GitHub_Electron_Refinement_V5"
    # Doubled the number of bins in the ∆P plots (both in x and y binning for the electron corrections, just in the y binning for all others)
        # Changed the range of the electron momentum plotted in the ∆P histograms from 0-12 GeV (with 120 bins total) to the new dimensions of 0.5-10.5 GeV with 400 bins total (bin size is 0.025 GeV/bin)
    # Added the Correction options where only the electron is corrected to the SP channel
    # No new corrections since "_GitHub_Electron_Refinement_V4"
    
    Extra_Part_of_Name = "_GitHub_Electron_Refinement_V6"
    # Refined the Electron Corrections based on the new fits of the uncorrected ∆P plots
    
    Extra_Part_of_Name = "_GitHub_Pion_Refinement_V1"
    # Created new Pion Corrections using the new electron corrections (and fit methods)
    # Minor issue noticed: there seems to be some print funtion which outputs empty lines during the running of this code - this should not effect the histograms, but is an oddity that I would like to fix (this was not noticed ever before)
    
    Extra_Part_of_Name = "_GitHub_Pion_Refinement_V2"
    # Refined the Pion Corrections from "GitHub_Pion_Refinement_V1"
    # Fixed an issue with 'pass_version' being used with Fall2018 data (code check for pass_version != "NS" instead of pass_version != "NA")
    
    Extra_Part_of_Name = "_GitHub_Pion_Refinement_V3"
    # Refined the Pion Corrections from "GitHub_Pion_Refinement_V1" ("GitHub_Pion_Refinement_V2" refinements were accidentally applied to the electron instead of the pion)
    # Set the initial beam energies used throughout the code at the beginning (based on file input) to avoid issues when loading other (i.e., Spring 2019) datasets
    # Fixed the minor note mentioned for "GitHub_Pion_Refinement_V1"
    
    Extra_Part_of_Name = "_GitHub_Pion_Refinement_V4"
    # Refined the Pion Corrections from "GitHub_Pion_Refinement_V3"
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V1"
    # Starting the proton corrections
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V2"
    # New proton corrections (compatible with Elastic Corrections) - Quadratic but not phi dependent 
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V3"
    # New proton corrections added
        # More complex correction uses 2 quadratic equation
    # Ran more versions of the corrections which turned off the Energy Loss Corrections
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V4"
    # New proton corrections added
        # More complex correction uses a combination of a quadratic and then a linear equation
            # The correction added used the Energy Loss corrections when being created
            # These are the only proton (momentum) corrections that are applied in this file
    # The (new) corrections from "_GitHub_Proton_Refinement_V3" were not run again (did not work well)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V5"
    # New proton corrections added
        # Modified/replaced existing corrections to check how the number/size of momentum bins effects the corrections (updated the 'complex' corrections as well as the 'regular' quadratic corrections)
        
        
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V6"
    # Refined the Proton Corrections by limiting the contributions of the Pi0 channel
    # No longer plotting Pi- histograms (only electron, proton, and Pi+)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V7"
    # Refined the Proton Corrections (again)
    
    Extra_Part_of_Name = "_GitHub_Cut_Check_V1"
    # Running Missing Mass histograms WITH exclusivities cuts (investigating why the corrections are not working)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V8"
    # Refined the Proton Corrections (again)
    # Reset the exclusivity cuts to only run for the proper histograms
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V9"
    # Refined the Proton Corrections (again)
        # No Pi0 Contributions to the proton corrections
        
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V10"
    # Refined the Proton Corrections (Just the Quad+Linear and 'refined' Quad)
        # No Pi0 Contributions to the proton corrections
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V11"
    # Refined the Proton Corrections (All versions with 'REF' now including another double quadratic refinement)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V12"
    # Refined the Proton Corrections (New/Refined corrections to replace/improve those from V11)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V13"
    # Refined the Proton Corrections ("LEF" Corrections refined with normal quadratic OR linear corrections - depending on sector)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V14"
    # New the Proton Corrections (New versions of "LEF" and "QEF" that use 0.05 GeV Momentum slices of ∆P below p = 1 GeV)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V15"
    # Removed some corrections (all proton corrections that are not the quad+linear ones) but adds two new ones
        # New proton corrections are:
            # 1) A refinement of the quad+linear correction where the refinement uses the mean of each gaussian slice is used in their defined range instead of using a continuous function
            # 2) A new proton correction entirely pased on the method described in the above refinement
            
            
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V16"
    # Refined the sliced corrections
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V17"
    # Needed to fix the refinements from the last version
    # Changed the binning of the Missing Mass Squared plots (from 160 to 200 in the range of -0.5 to 0.5)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V18"
    # Changed the binning of the Missing Mass Squared plots (from 200 to 310 in the range of -0.3175 to 0.3025)
    # Removed plots which use different particle momentums and sectors
    # Checking Missing Mass Plots with exclusivity cuts
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V19"
    # Changed the binning of the Missing Mass Squared plots (from 310 to 320 in the range of -0.3275 to 0.3125 - Same size but the range is increased to make the bins easier to change while fitting)
    # Added alternative calculation of ∆P histograms
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V20"
    # Removed the alternative calculation of ∆P histograms but added the ∆P vs uncorrected proton momentum (i.e., without the energy loss correction - will be incompatible with current order that the proton corrections are applied)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V21"
    # New Proton Correction Refinement (Sliced)
    # Added Integrated Sector ∆P histograms
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V22"
    # New Proton Correction that uses slices WITHOUT the Energy Loss corrections
    # Updated the corNameTitles function so that histograms are made with the corrections already in multiple lines for each particle
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V23"
    # Added new type of exclusivity cut (simple cut on the MM2 < 0.2 and MM2 > -0.2)
        # Past cuts were too tight/baised higher missing mass at low momentum
    # No longer running invariant mass histograms (was not using them)
    # Removed the Proton Correction that used slices WITHOUT the Energy Loss corrections (i.e., the one added in the previous version)
        # Was not necessary (the problem with the corrections was not the order of the Energy Loss/Momentum corrections were applied)
        
        
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V24"
    # Added another new type of exclusivity cut (cut on the MM2 < 0.15 and MM2 > -0.2)
    # Rewrote the Proton Correction that used slices WITHOUT the Energy Loss corrections (Now is a unique slice correction using the new exclusivity cut from 'Extra_Part_of_Name = "_GitHub_Proton_Refinement_V23"')
    # Refined the Sliced Proton correction from prior files using the new cut (seperated the refinement from the original versions)
    # Removed the phi binning histograms (was not using)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V25"
    # The tighter MM2 cut from the last file was not needed
    # Refined the 'SERC' proton correction 
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V26"
    # Refined the sliced proton corrections and added a new one (using the original, calculated, cuts)
    # Removed a few unused corrections
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V27"
    # Combined a refined version of the sliced proton corrections and added a new one (using the original, calculated, cuts)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V28"
    # Refined the new sliced proton correction (from V27, i.e., corPro == 10) using ∆P fits without exclusivity cuts
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V29"
    # Added new exclusivity cut which includes the energy loss corrections before cutting on the Missing Mass Squared (cut still on |MM2| < 0.2)
    # Created a new correction from a refinement of the sliced proton correction from V28 (i.e., corPro == 10 refined into the new correction corPro == 11)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V30"
    # Slightly refined corPro == 11 and created a double quadratic (continuous) correction using those parameters
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V31"
    # Needed to fix corPro == 12 (used the wrong parameter at the end of the equation and refined the switch point a bit)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V32"
    # Removed Sliced Corrections and created a new refined corPro == 13 (similar to corPro == 12 but with a few adjustments)
    # Renamed corPro == 12 (gave name to corPro == 13)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V33"
    # Created a new refined corPro == 14 (similar to corPro == 12-13 but with a few adjustments)
    # Renamed corPro == 12-14 (switched similar names)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V34"
    # Refined corPro == 14 (sector 5 and 6 using ∆P peaks with corrected (Eloss) Missing Mass Cuts)
    # Added new cut which corrects all particles except the proton and pi- pion (i.e., full electron/pi+ momentum corrections + Eloss)
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V35"
    # Refined corPro == 14 (sector 5 and 6 refined arbitrarily for testing - last version performed very poorly)
    # Added new 3D histogram to plot ∆P, Missing Mass, and proton momentum in the same histogram
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V36"
    # Refined corPro == 15 (sector 5 and 6 refined arbitrarily for testing)
    # Fixed the 3D histogram to plot ∆P, Missing Mass, and proton momentum in the same histogram (was not running due to constant crashes)
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V37"
    # Testing Theta (3D ∆P plots) and Phi bins to see if they can help with the corrections
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V38"
    # Removed 3D and Phi plots
    # Refined Sec 5 as a test (corPro == 15)
        # Sec 6 will still need correcting
        
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V39"
    # Refined Sec 5 as another test (corPro == 15)
        # V38 was an improvement
        # Sec 6 will still need correcting
    
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V40"
    # Using 3D tests with new conditions for getting ∆P
    # Removed some unnecessary options/cuts
    
    Extra_Part_of_Name = "_GitHub_Proton_Refinement_V41"
    # Flipped the condition for D_p_S_pro
    
    Extra_Part_of_Name = "_Proton_Testing_V1"
    # Added testing corrections (proton only - not sector dependent)
    
    Extra_Part_of_Name = "_Proton_Testing_V2"
    # Added additional testing corrections from the last version (now also include the other particle corrections)
    
    Extra_Part_of_Name = "_New_Proton_Refinement_V1"
    # Added manual sliced refinement (corPro == 18 -- 'Sliced - Manual Refined New')
        # Refined from 'mmEF_PipMMEF_ProMMpro_NRE' but completely independent when running
        
    Extra_Part_of_Name = "_New_Proton_Refinement_V2"
    # Modified corPro == 18 (saved only improved points with a few additional minor tests)
    # Added another 3D histogram to show both ∆P calculated options
    
    if(event_type in ["SP", "P0"]):
        Extra_Part_of_Name = "_GitHub_3D_Dp_Test_V1"
        # Testing 3D ∆P vs Missing Mass vs Momentum for the Pi+ Corrections (reduced other options to avoid running unnecessary plots for this test)
        # No Phi Bins and only Pi+ (∆P) Plots
        
        if("MC" in event_Name):
            Extra_Part_of_Name = "_MC_Testing_Normal_V1"
            # Testing Correction Code with Simulated data
            
            Extra_Part_of_Name = "_MC_Testing_Normal_V2"
            # Same update as "_New_Proton_Refinement_V2"
            
            Extra_Part_of_Name = "_MC_Testing_Normal_V3"
            # Removed all non-testing corrections
            # ∆P histograms now do not plot sector-by-sector
            # Testing ∆P = P_calculated - P_generated (instead of measured)
            # Plotting the larger ∆P instead of the flipped choices
            
            Version_MC = "_V4"
            # Made plot for Missing Mass vs both ∆P values
            
            Version_MC = "_V5"
            # Fixed some issues in the last version and added the ∆P(Gen) plots
            
            Version_MC = "_V6"
            # Completely switched to generated kinematics
            
            Version_MC = "_V7"
            # Improved formatting for generated events
            
            Version_MC = "_V8"
            # Delta P cuts only

            Version_MC = "_VTesting_Delete"
            
            Version_MC = "_V9"
            # Fixed beam energy
            
            Version_MC = "_V10"
            # Cutting events from ∆P with imaginary components
            
            Version_MC = "_V11"
            # Plotting ∆P vs Theta
            
            Version_MC = "_VTesting_Delete"
            
            Version_MC = "_VTesting_Delete_New"
            # Updating the mass sig figs
            
            Version_MC = "_V12"
            # Plotting all terms in ∆P calculation
            # Turning off exclusivity cuts
            
            Version_MC = "_V13"
            # Using full sig figs all particles except electron
    
            Extra_Part_of_Name = "".join(["_MC_Testing_Normal", str(Version_MC)])
            
            if("+20 MeV" in event_Name):
                Extra_Part_of_Name = "_MC_Testing_Plus_V1"
                # Testing Correction Code with Simulated data (added 20 MeV to Proton Momentum)
                
                Extra_Part_of_Name = "_MC_Testing_Plus_V2"
                # Same update as "_New_Proton_Refinement_V2"
                
                Extra_Part_of_Name = "_MC_Testing_Plus_V3"
                # Removed all non-testing corrections
                # ∆P histograms now do not plot sector-by-sector
                # Testing ∆P = P_calculated - P_generated (instead of measured)
                # Plotting the larger ∆P instead of the flipped choices
                
                Extra_Part_of_Name = "".join(["_MC_Testing_Plus", str(Version_MC)])
                
            if("-20 MeV" in event_Name):
                Extra_Part_of_Name = "_MC_Testing_Minus_V1"
                # Testing Correction Code with Simulated data (subtracted 20 MeV from Proton Momentum)
                
                Extra_Part_of_Name = "_MC_Testing_Minus_V2"
                # Same update as "_New_Proton_Refinement_V2"
                
                Extra_Part_of_Name = "_MC_Testing_Minus_V3"
                # Removed all non-testing corrections
                # ∆P histograms now do not plot sector-by-sector
                # Testing ∆P = P_calculated - P_generated (instead of measured)
                # Plotting the larger ∆P instead of the flipped choices
                
                Extra_Part_of_Name = "".join(["_MC_Testing_Minus", str(Version_MC)])
                
            if("(GEN)" in event_Name):
                Version_MC = "_V1"
                # First version to give the option to switch back-and-forth between the generated and reconstructed simulated events
                # Made after "_V12"/"_V13" from above notes (ran just before "_V14")
                # Last reconstructed version was "_V6" so all notes after that correspond to this group going forward
                # Changed binning for the square root term histograms
                
                Version_MC = "_V2"
                # Added cut on the square root term (instead of ∆P - cut is for less than 0.05)
                # Ran with "_V14" for REC
                
                Extra_Part_of_Name = "".join(["_MC_GEN_Test", str(Version_MC)])
    
    if(pass_version not in ["NA", ""]):
        Extra_Part_of_Name = "".join(["_GitHub_Spring_2019_Pass_", "1" if("Pass 1" in pass_version) else "2", "_V1"])
        # Testing Spring 2019 data with pass 1 and pass 2 files
        
        Extra_Part_of_Name = "".join(["_GitHub_Spring_2019_Pass_", "1" if("Pass 1" in pass_version) else "2", "_V2"])
        # Update file locations to take in events from different file skims (MissingNeutron files instead of the nSidis files)
        # Removed "Extended" Electron Corrections (i.e., the refinements of the original corrections from the last collaboration meeting)
        
        Extra_Part_of_Name = "".join(["_GitHub_Spring_2019_Pass_", "1" if("Pass 1" in pass_version) else "2", "_V3"])
        # Fixed initial beam energies (was still using energy from Fall 2018 instead of from Spring 2019)
        # File locations take events from MissingNeutron files instead of the nSidis files (want to switch back to nSidis)
        
        Extra_Part_of_Name = "".join(["_GitHub_Spring_2019_Pass_", "1" if("Pass 1" in pass_version) else "2", "_V4"])
        # Starting new Pass 2 electron corrections
        
        Extra_Part_of_Name = "".join(["_GitHub_Spring_2019_Pass_", "1" if("Pass 1" in pass_version) else "2", "_V5"])
        # Made new electron correction for pass 2
        # Starting Pi+ Corrections
    
    if("Out" in datatype):
        Extra_Part_of_Name = "_New_Extended_Out_V1"
        # New Extended Outbending Corrections
        
        Extra_Part_of_Name = "_New_Extended_Out_V2"
        # New Extended Outbending Corrections (ran with more files)
        
        Extra_Part_of_Name = "_New_Extended_Out_V3"
        # Modified the Exclusive Cuts to the Electron Only (EO) Files
            # Used the simplest version of the cuts to begin their development 
        # Added the Invariant Mass Histograms to the list of histograms being produced (needed to refine the Electron Only Files)
        
        Extra_Part_of_Name = "_New_Extended_Out_V4"
        # New Outbending Exclusivity Cut (Linear equations - NOT sector dependant - replaced "Calculated_Exclusive_Cuts")
        
        Extra_Part_of_Name = "_New_Extended_Out_V5"
        # New Outbending Exclusivity Cut (Linear equations - functions of MOMENTUM and PHI - sector dependant - replaced "Calculated_Exclusive_Cuts")
            # Cuts use a new method of finding the region where the background is overtaking the signal (should offer better cuts to avoid large background peaks in the ∆P distributions)
        # Invariant Mass Histograms can now be made with the cuts being applied
        
        
        Extra_Part_of_Name = "_New_Extended_El_Cor_V1"
        # New Electron correction for the outbending data
        
        Extra_Part_of_Name = "_New_Extended_El_Cor_V2"
        # Refined the new Electron correction from '_New_Extended_El_Cor_V1'
            # Correction from '_New_Extended_El_Cor_V1' was renamed from 'mmEF' to 'mmExF' (refined correction is now called 'mmEF')
            
        Extra_Part_of_Name = "_New_Extended_El_Cor_V3"
        # Refined the Electron correction from '_New_Extended_El_Cor_V2'
            # Correction 'mmEF' now has an additional refinement made to it ('mmExF' has not changed)
            
        Extra_Part_of_Name = "_New_Extended_El_Cor_V4"
        # Refined the Electron correction from '_New_Extended_El_Cor_V3'
            # Correction 'mmEF' now has an additional refinement made to it ('mmExF' has not changed)
            
        Extra_Part_of_Name = "_New_Extended_El_Cor_V5"
        # Refined the Electron correction from '_New_Extended_El_Cor_V4'
            # Correction 'mmEF' now has an additional refinement made to it while 'mmExF' has been changed to include all prior refinements since "_New_Extended_El_Cor_V1"
            
            
        Extra_Part_of_Name = "_New_Extended_El_Cor_V6"
        # Refined the Electron correction from '_New_Extended_El_Cor_V5'
            # Correction 'mmEF' now has an additional refinement made to it while 'mmExF' is the same correction as 'mmEF' was in "_New_Extended_El_Cor_V5"
            # The newest refinement uses data that starts from 2.5 GeV instead of 2 GeV (too few statistics to keep using for refinements)
            
        Extra_Part_of_Name = "_New_Extended_El_Cor_V7"
        # Refined the Electron correction from '_New_Extended_El_Cor_V6'
            # Correction 'mmEF' now has an additional refinement made to it while 'mmExF' is the same correction as 'mmEF' was in "_New_Extended_El_Cor_V6"
            # The newest refinement uses data that starts from 2.5 GeV instead of 2 GeV
            
        Extra_Part_of_Name = "_New_Extended_El_Cor_V8"
        # Refined the Electron correction from '_New_Extended_El_Cor_V7'
            # Correction 'mmEF' now has some additional refinements but some sectors are either left unchanged from what they were in "_New_Extended_El_Cor_V7" (sectors 4 and 6) or have been reverted to be the same as 'mmExF' (which was left unchanged this time as well)
            
        Extra_Part_of_Name = "_New_Extended_El_Cor_V9"
        # Refined the Electron correction from '_New_Extended_El_Cor_V8'
            # Correction 'mmEF' now has one additional refinement to sector 1 (refinement uses the old range starting at 2 GeV instead of 2.5 GeV)
            # All other sectors are left unchanged from what they were in "_New_Extended_El_Cor_V8"
            
        Extra_Part_of_Name = "_New_Pip_Cor_V1"
        # Condensed the Electron correction from '_New_Extended_El_Cor_V9' into one line
            # Correction 'mmEF' may be slightly rounded but otherwise the same
            # Correction 'mmExF' is the same (unrounded) correction that was 'mmEF' in '_New_Extended_El_Cor_V9' (the older 'mmExF' was replaced)
        # Added new Pi+ Momentum correction as an initial test (iterations may be needed as 'mmEF' was changed slightly)
        # Now running "SP" events with the corrections 'mmEF_PipMMEF' and 'mmExF_PipMMEF'
        
        Extra_Part_of_Name = "_New_Pip_Cor_V2"
        # The condensed the Electron correction from '_New_Pip_Cor_V1' was successfully tested
            # All corrections using 'mmExF' were removed as the correction is now identical to 'mmEF'
        # Refined the new Pi+ Momentum correction
        
        Extra_Part_of_Name = "_New_Pip_Cor_V3"
        # Refined the new Pi+ Momentum correction from '_New_Pip_Cor_V2'
            # Refinement was done using the same momentum range but the size of each slice was increased from 0.5 GeV per point to 1 GeV per point
            
        Extra_Part_of_Name = "_New_Final_El_Cor_V1"
        # Refined the new Electron Momentum correction from '_New_Pip_Cor_V3'
            # Refinement was done using the shorter electron momentum range which started at 2.5 GeV
            # File 5578 had some issues when being processed that were not addressed (could be fixed by rerunning the code but this was not done before moving on the next version)
            
        Extra_Part_of_Name = "_New_Final_El_Cor_V2"
        # Refined the Electron Momentum correction from '_New_Final_El_Cor_V1'
            # Refinement was done with a slightly different method using the missing mass values as a direct means of calculating ∆P for the final levels of refinement
            
        Extra_Part_of_Name = "_New_Final_Pip_Cor_V1"
        # Refined the Pi+ Momentum correction from '_New_Final_El_Cor_V2'
            # Normal method
        # Removed all "mmExF" corrections
    
        Extra_Part_of_Name = "_New_Final_Pip_Cor_V2"
        # Refined the Pi+ Momentum correction from '_New_Final_El_Cor_V1' (removed all sectors refinements from '_New_Final_El_Cor_V2' and '_New_Final_Pip_Cor_V1' and only refined sector 4)
        # Removed a variety of histograms not being used currently including a 3D histogram and the phase space and Invariant mass histograms. Also only running the final corrections
        
        Extra_Part_of_Name = "_New_Final_El_Cor_V3"
        # Refined the El Momentum correction from '_New_Final_Pip_Cor_V2' (just refined El sector 1 and 2)
        
        Extra_Part_of_Name = "_New_Final_El_Cor_V4"
        # Refined the El Momentum correction from '_New_Final_El_Cor_V3' (just refined El)
```






## Updates from 5-9-2023
* Updated the Inbending Corrections (Done)
* Updating the Outbending Corrections (In-progress)
* Switched to running files with python3 (original command stopped working on 5-9-2023)


## Updates from 11-14-2022:
General Updates:
* Moved back to the work directory (issue was fixed but code may not all be updated yet...)


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





