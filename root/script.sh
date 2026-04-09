#!/bin/bash
#SBATCH --job-name=Games_on_Graphs_10
#SBATCH --mail-type=ALL
#SBATCH --mail-user=edohearn@crimson.ua.edu
#SBATCH -n 1 #tasks
#SBATCH -N 1 #nodes
#SBATCH -c 1 #number of cores per task
#SBATCH --array 0-8

#SBATCH -o Output/output_GoG_10/%a.txt
#SBATCH -p main
#SBATCH --qos main
#SBATCH --mem=20G

benefit=(8.0 8.5 9.0 9.5 10 10.5 11 11.5 12)

module load python/python3/3.11.7
cd /home/edohearn/MATH598/
python /home/edohearn/MATH598/root/testing.py ${benefit[${SLURM_ARRAY_TASK_ID}]}