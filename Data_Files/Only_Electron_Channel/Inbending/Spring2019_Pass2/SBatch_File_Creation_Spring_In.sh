#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=EO_P2_F_In_8_27_2024_Run1_Sp19_P2_Refine_V2_Mom_Cors
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%A_%a-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%A_%a-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=0-119


FILES=(/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Spring2019/Pass2/Inbending_recon/Only_Electron_Channel/electron_only.pass2.inb.qa.rec_clas_00*)
# (Inbending - Pass 2) array=0-119


srun python3 /w/hallb-scshelf2102/clas12/richcap/Exclusive_RG-A_Momentum_Corrections/Data_Files/Momentum_Correction_File_Creation_wPass2.py In P2EOF ${FILES[$SLURM_ARRAY_TASK_ID]}

