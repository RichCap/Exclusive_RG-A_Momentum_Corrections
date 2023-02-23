#!/bin/bash
#SBATCH --ntasks=2
#SBATCH --job-name=Mom_Cor_P0_MC_Testing_V11_2_23_2023
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00


srun python ../../../File_Creation_Final_Momentum_Corrections_Github.py In P0_MC /w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Pi0_MC/lvl2_eppi0.inb.mc.eloss.root
# srun python ../../../File_Creation_Final_Momentum_Corrections_Github.py In P0_MC_P /w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Pi0_MC/lvl2_eppi0.inb.mc.eloss.Ppos20.root
# srun python ../../../File_Creation_Final_Momentum_Corrections_Github.py In P0_MC_M /w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Pi0_MC/lvl2_eppi0.inb.mc.eloss.Pneg20.root

