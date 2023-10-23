#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=SP_P2_In_10_18_2023_Run2_Sp19_rec_clas_V6_Mom_Cors
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%A_%a-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%A_%a-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=3,4,19-21,24,25,27,30,34,38-40,42-44,51,57-59,61,62,66,68,70,78,80,82,105,108-110,113,115-117


FILES=(/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/Inbending_recon/Single_Pion_Channel_epipN/ePip.pass2.inb.qa.rec_clas_00*)
# (Inbending - Pass 2) array=0-119


srun python3 /w/hallb-scshelf2102/clas12/richcap/Exclusive_RG-A_Momentum_Corrections/Data_Files/File_Creation_Final_Momentum_Corrections_Github.py In P2SP ${FILES[$SLURM_ARRAY_TASK_ID]}
