#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --job-name=MomC_SP_Out_New_Final_El_Cor_V4_5_21_2023
#SBATCH --mail-type=ALL
#SBATCH --mail-user=richard.capobianco@uconn.edu 
#SBATCH --output=/farm_out/%u/%x-%j-%N.out
#SBATCH --error=/farm_out/%u/%x-%j-%N.err
#SBATCH --partition=production
#SBATCH --account=clas12
#SBATCH --mem-per-cpu=8000
#SBATCH --time=12:00:00
#SBATCH --array=0-185



FILES=(/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Outbending_skim4/ePip.outb.qa.rec_clas_005*)
# (Outbending) array=0-185


# FILES=(/w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Outbending_skim4/ePip.outb.qa.rec_clas_005570.evio.root
# /w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Outbending_skim4/ePip.outb.qa.rec_clas_005571.evio.root
# /w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Outbending_skim4/ePip.outb.qa.rec_clas_005591.evio.root
# /w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Outbending_skim4/ePip.outb.qa.rec_clas_005602.evio.root
# /w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Outbending_skim4/ePip.outb.qa.rec_clas_005606.evio.root
# /w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Outbending_skim4/ePip.outb.qa.rec_clas_005611.evio.root
# /w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Outbending_skim4/ePip.outb.qa.rec_clas_005628.evio.root
# /w/hallb-scshelf2102/clas12/richcap/Momentum_Corrections/Single_Pion_Channel_epipN/Outbending_skim4/ePip.outb.qa.rec_clas_005649.evio.root)
# # (Missed) array=0-7

srun python3 ../../File_Creation_Final_Momentum_Corrections_Github.py Out SP ${FILES[$SLURM_ARRAY_TASK_ID]}
