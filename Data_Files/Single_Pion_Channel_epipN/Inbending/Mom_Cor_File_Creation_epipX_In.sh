#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=In_mom_cor_epipX_VFinal_SP8_6_21_2022
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=0-95





FILES=(/lustre19/expphy/volatile/clas12/shrestha/clas12momcorr/data/inbending/ePipX/epip.skim4_005*)
# (Inbending) array=0-95

# # Outbending Files:
# FILES=(/lustre19/expphy/volatile/clas12/shrestha/clas12momcorr/data/outbending/ePipX/*)
# (Outbending) array=0-169

srun python ../../File_Creation_All_Corrections_Simplified_No_Loop_Finished_SP.py In SP ${FILES[$SLURM_ARRAY_TASK_ID]}
