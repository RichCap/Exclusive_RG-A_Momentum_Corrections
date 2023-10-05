#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=SP_P1_In_9_29_2023_R1_Fa18_Pass1_Final_Tests_V1_Mom_Cors
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%A_%a-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%A_%a-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=0-173



FILES=(/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Inbending_skim4/ePip.inb.qa.skim4_005*)
# (Inbending) array=0-173


srun python3 /w/hallb-scshelf2102/clas12/richcap/Exclusive_RG-A_Momentum_Corrections/Data_Files/File_Creation_Final_Momentum_Corrections_Github.py In SP ${FILES[$SLURM_ARRAY_TASK_ID]}
