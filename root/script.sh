#!/bin/bash
#SBATCH --job-name=Games_on_Graphs_4a
#SBATCH --mail-type=ALL
#SBATCH --mail-user=edohearn@crimson.ua.edu
#SBATCH -n 1 #tasks
#SBATCH -N 1 #nodes
#SBATCH -c 1 #number of cores per task
#SBATCH --array 0-8

#SBATCH -o Output/output_GoG_4/%a.txt
#SBATCH -p main
#SBATCH --qos main
#SBATCH --mem=20G

benefit=(2.0 2.5 3.0 3.5 4 4.5 5.0 5.5 6.0)

module load python/python3/3.11.7
cd /home/edohearn/MATH598/
python /home/edohearn/MATH598/root/testing.py ${benefit[${SLURM_ARRAY_TASK_ID}]}