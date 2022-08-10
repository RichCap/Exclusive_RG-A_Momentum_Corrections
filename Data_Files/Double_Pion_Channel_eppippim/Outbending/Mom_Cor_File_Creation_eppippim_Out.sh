#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=double_pion_out_pro_mom_cor_eppipX_VFinal_SP_V5_DP_6_22_2022
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=6000
#SBATCH --time=24:00:00
#SBATCH --array=0-153




FILES=(/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/outb/epPipPim.outb.qa.nSidis_00*)
# array files (Outbending): 0-153

# FILES=(/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/inb/epPipPim.inb.qa.nSidis_00*)
# # array files (Inbending): 0-173

# FILES=(/lustre19/expphy/volatile/clas12/kenjo/ntuple_epippimp/inb/lvl1_eppimpip.skim4_00*)
# # # array files (Inbending): 0-57

# FILES=(/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/inb/epPipPim.inb.qa.lvl1_eppimpip.skim4_00*)
# # array files (Inbending): 0-173
# # Outbending Files:
# FILES=(/lustre19/expphy/volatile/clas12/trotta/wagon/RhoWagon/PyAnalysis/data/outb/epPipPim.outb.qa.lvl1_eppimpip.skim4_00*)
# # array files (Outbending): 0-185
srun python ../../File_Creation_All_Corrections_Simplified_No_Loop_Finished_SP.py Out DP ${FILES[$SLURM_ARRAY_TASK_ID]}

