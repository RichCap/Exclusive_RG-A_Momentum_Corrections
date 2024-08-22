#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=fa2SPF_MomC_In_Forward_Fall2018_P2_In_Refine_V3_8_22_2024_Run1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%A_%a-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%A_%a-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=8000
#SBATCH --time=3:00:00
#SBATCH --array=0-170



FILES=(/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Central_Tracking/Fall2018/Inbending/Single_Pion_Channel_epipN/ePip.wCentral.pass2.inb.qa.Fa18.rec_clas_005*)
# (Outbending) array=0-170

srun python3 /w/hallb-scshelf2102/clas12/richcap/Exclusive_RG-A_Momentum_Corrections/Data_Files/Momentum_Correction_File_Creation_wPass2.py In fa2SPF ${FILES[$SLURM_ARRAY_TASK_ID]}
