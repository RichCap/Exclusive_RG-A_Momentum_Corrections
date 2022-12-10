#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=Mom_Cors_electron_only_Inbending_GitHub_Electron_Refinement_V6_10_17_2022
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=0-173




FILES=(/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Only_Electron_Channel/Inbending/electron_only.inb.qa.skim4_00*)
# array files (Inbending): 0-173


srun python ../../File_Creation_Final_Momentum_Corrections_Github.py In EO ${FILES[$SLURM_ARRAY_TASK_ID]}

