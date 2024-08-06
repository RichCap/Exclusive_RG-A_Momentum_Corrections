#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=MC_P2_MomC_Inbending_Fa18_P2_MC_V4_8_6_2024_R2
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%A_%a-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%A_%a-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=1:00:00
#SBATCH --array=0-63


FILES=(/w/hallb-scshelf2102/clas12/richcap/SIDIS/Matched_REC_MC/With_BeamCharge/Pass2/More_Cut_Info/MC_Matching_sidis_epip_richcap.inb.qa.new5.inb-clasdis*)
# Above is for (mdf_NewP2) #SBATCH --array=0-63


srun python3 /w/hallb-scshelf2102/clas12/richcap/Exclusive_RG-A_Momentum_Corrections/Data_Files/Momentum_Correction_File_Creation_wPass2.py In fa2MC ${FILES[$SLURM_ARRAY_TASK_ID]}

