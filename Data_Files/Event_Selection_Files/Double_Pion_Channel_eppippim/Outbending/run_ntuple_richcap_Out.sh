#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=Mom_Cor_File_Creation_groovy_Outbending
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=5500
#SBATCH --time=24:00:00
#SBATCH --array=0-185


source /work/clas12/kenjo/groovy/env.csh


FILES=(/cache/clas12/rg-a/production/recon/fall2018/torus+1/pass1/v1/dst/train/nSidis/nSidis_005*)
# Above is for #SBATCH --array=0-185

srun ../ntuple_ePipPimP.groovy ${FILES[$SLURM_ARRAY_TASK_ID]}