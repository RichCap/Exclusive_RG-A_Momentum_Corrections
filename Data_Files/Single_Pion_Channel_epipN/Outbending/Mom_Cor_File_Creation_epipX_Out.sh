#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=Out_mom_cor_epipX_GitHub_SP_New_W_8_22_2022
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=0-176






FILES=(/work/clas12/shrestha/clas12momcorr/utsav/dataFiles/outbending/ePipX/skim4_005*)
# (Outbending) array=0-176

# # Inbending Files:
# FILES=(/work/clas12/shrestha/clas12momcorr/utsav/dataFiles/inbending/ePipX/epip.skim4_005*)
# # (Inbending) array=0-95


srun python ../../File_Creation_Final_Momentum_Corrections_Github.py Out SP ${FILES[$SLURM_ARRAY_TASK_ID]}
