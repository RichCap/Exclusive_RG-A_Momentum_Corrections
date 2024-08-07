#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=Mom_Cors_MC_Inbending_Fa18_P1_MC_V2_6_4_2024
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%A_%a-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%A_%a-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=0-219
#SBATCH --constraint=el7




FILES=(/w/hallb-scshelf2102/clas12/richcap/SIDIS/Matched_REC_MC/MC_Matching_sidis_epip_richcap.inb.qa.45nA_job_*)
# Above is for (mdf) #SBATCH --array=0-219


srun python3 /w/hallb-scshelf2102/clas12/richcap/Exclusive_RG-A_Momentum_Corrections/Data_Files/Momentum_Correction_File_Creation_wPass2.py In MC ${FILES[$SLURM_ARRAY_TASK_ID]}

