#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=Mom_Cors_ep_elastic_Inbending_GitHub_Valerii_V1_9_1_2022
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=0-53



FILES=(/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/Valerii_Files/eP_Elastic_with_CDpro_New.inb.qa.skim4_005*)
# array files (Inbending): 0-53

# # Old Inbending files (do not use for elastic ep->e'p' events)
# FILES=(/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/Inbending/eP_Elastic_with_CDpro_New.inb.qa.nSidis_00*)
# # array files (Inbending): 0-173

srun python ../../File_Creation_Final_Momentum_Corrections_Github.py In ES ${FILES[$SLURM_ARRAY_TASK_ID]}

