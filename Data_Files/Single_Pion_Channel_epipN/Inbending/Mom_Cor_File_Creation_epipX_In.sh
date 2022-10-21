#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=Mom_Cors_epipX_SP_Inbending_GitHub_Electron_Refinement_V6_10_17_2022
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=0-173




FILES=(/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Single_Pion_Channel_epipN/Inbending_skim4/ePip.inb.qa.skim4_00*)
# (Inbending) array=0-173


# FILES=(/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Single_Pion_Channel_epipN/Inbending/ePip.inb.qa.nSidis_005*)
# # (Inbending) array=0-173

# Old Files
# FILES=(/work/clas12/shrestha/clas12momcorr/utsav/dataFiles/inbending/ePipX/epip.skim4_005*)
# # (Inbending) array=0-95

# # Outbending Files:
# FILES=(/work/clas12/shrestha/clas12momcorr/utsav/dataFiles/outbending/ePipX/skim4_005*)
# (Outbending) array=0-176

srun python ../../File_Creation_Final_Momentum_Corrections_Github.py In SP ${FILES[$SLURM_ARRAY_TASK_ID]}
