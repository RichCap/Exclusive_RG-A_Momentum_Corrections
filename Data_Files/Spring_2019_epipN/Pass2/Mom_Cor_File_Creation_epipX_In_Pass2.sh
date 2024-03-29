#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=Mom_Cors_epipX_SP_Inbending_GitHub_Spring_2019_Pass_2_NEW_V1_8_18_2023_V2
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=0-119



FILES=(/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/Inbending_nSidis/Complete/ePip.pass2.inb.qa.nSidis_00*)
# (Inbending - Pass 2 - New) array=0-119

# FILES=(/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/Inbending_nSidis/ePip.pass2.inb.qa.nSidis_00*)
# # (Inbending - Pass 2) array=0-29

# FILES=(/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass1/Inbending_nSidis/ePip.pass1.inb.qa.nSidis_00*)
# # (Inbending - Pass 1) array=0-120


srun python3 /w/hallb-scshelf2102/clas12/richcap/Exclusive_RG-A_Momentum_Corrections/Data_Files/File_Creation_Final_Momentum_Corrections_Github.py In P2SP ${FILES[$SLURM_ARRAY_TASK_ID]}
