#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=double_pion_out_pro_mom_cor_eppipX_GitHub_2_DP_8_11_2022
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=0-185



FILES=(/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Double_Pion_Channel_eppippim/Outbending/epPipPim.outb.qa.nSidis_005*)
# array files (Outbending): 0-185

srun python ../../File_Creation_Momentum_Corrections_Github.py Out DP ${FILES[$SLURM_ARRAY_TASK_ID]}

