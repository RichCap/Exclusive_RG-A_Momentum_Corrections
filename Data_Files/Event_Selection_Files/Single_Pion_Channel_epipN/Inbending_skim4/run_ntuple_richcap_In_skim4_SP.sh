#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=Mom_Cor_File_Creation_groovy_SP_Inbending_skim4_10_10_2022
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=5500
#SBATCH --time=24:00:00
#SBATCH --array=0-173



FILES=(/cache/clas12/rg-a/production/recon/fall2018/torus-1/pass1/v0/dst/train/skim4/skim4_005*)
# Above is for #SBATCH --array=0-173

# source /work/clas12/kenjo/groovy/env.csh

srun ../ntuple_ePipN_richcap.groovy ${FILES[$SLURM_ARRAY_TASK_ID]}
