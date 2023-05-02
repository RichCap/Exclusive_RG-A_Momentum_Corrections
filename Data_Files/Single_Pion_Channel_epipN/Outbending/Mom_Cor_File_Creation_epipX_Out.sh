#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=Out_mom_cor_epipX_GitHub_SP_New_Cut_4_28_2023
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=0-186



FILES=(/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Outbending_skim4/ePip.outb.qa.rec_clas_005*)
# (Outbending) array=0-186


srun python ../../File_Creation_Final_Momentum_Corrections_Github.py Out SP ${FILES[$SLURM_ARRAY_TASK_ID]}
