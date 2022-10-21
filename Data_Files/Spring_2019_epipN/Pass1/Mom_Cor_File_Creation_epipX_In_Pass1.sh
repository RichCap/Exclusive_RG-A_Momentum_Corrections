#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=Mom_Cors_epipX_SP_Inbending_GitHub_Spring_2019_Pass1_V1_10_20_2022
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=0-120



FILES=(/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Spring2019/Pass1/Inbending/ePip.pass1.inb.qa.nSidis_00*)
# (Inbending - Pass 1) array=0-120

# FILES=(/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Spring2019/Pass2/Inbending/ePip.pass2.inb.qa.nSidis_00*)
# # (Inbending - Pass 2) array=0-29

srun python ../../File_Creation_Final_Momentum_Corrections_Github.py In P1SP ${FILES[$SLURM_ARRAY_TASK_ID]}
