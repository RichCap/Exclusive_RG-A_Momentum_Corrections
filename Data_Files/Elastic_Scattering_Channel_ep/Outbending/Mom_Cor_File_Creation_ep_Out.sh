#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=Mom_Cors_ep_elastic_Outbending_New_Extended_Cut_V1_3_12_2022
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=0-215



FILES=(/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Elastic_Scattering_ep/Outbending/eP_Elastic_with_CDpro.outb.qa.rec_clas_005449.evio.0*)
# (Outbending) array=0-215

# FILES=(/lustre19/expphy/volatile/clas12/richcap/Momentum_Cors/Exclusive_RG-A_Momentum_Corrections/Data_Files/Event_Selection_Files/Elastic_Scattering_ep/Outbending/eP_Elastic_with_CDpro_New.outb.qa.nSidis_00*)
# # array files (Outbending): 0-185

srun python ../../File_Creation_Final_Momentum_Corrections_Github.py Out ES ${FILES[$SLURM_ARRAY_TASK_ID]}

