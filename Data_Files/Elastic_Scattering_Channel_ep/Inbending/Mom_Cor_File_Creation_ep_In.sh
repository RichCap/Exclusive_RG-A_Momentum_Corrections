#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=Mom_Cors_ep_elastic_Inbending_GitHub_Electron_Refinement_V1_10_7_2022
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=0-173




FILES=(/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Elastic_Scattering_ep/Inbending/eP_Elastic_with_CDpro.inb.qa.skim4_005*)
# array files (Inbending): 0-173


srun python ../../File_Creation_Final_Momentum_Corrections_Github.py In ES ${FILES[$SLURM_ARRAY_TASK_ID]}
