#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=Mom_Cor_DP_New_Proton_Refinement_V3_2_14_2023
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=7000
#SBATCH --time=24:00:00
#SBATCH --array=0-173



FILES=(/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Double_Pion_Channel_eppippim/Inbending_skim4/epPipPim.inb.qa.skim4_00*)
# array files (Inbending): 0-173


# FILES=(/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Double_Pion_Channel_eppippim/Inbending/epPipPim.inb.qa.nSidis_005*)
# # array files (Inbending): 0-173

srun python ../../File_Creation_Final_Momentum_Corrections_Github.py In DP ${FILES[$SLURM_ARRAY_TASK_ID]}

