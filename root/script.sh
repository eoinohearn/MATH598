#!/bin/bash
#SBATCH --job-name=Games_on_Graphs_ArrayTry
#SBATCH --mail-type=ALL
#SBATCH --mail-user=edohearn@crimson.ua.edu
#SBATCH -n 1 #tasks
#SBATCH -N 1 #nodes
#SBATCH -c 1 #number of cores per task
#SBATCH --array 0-9

#SBATCH -o Output/output_GoG_4_%a.txt
#SBATCH -p main
#SBATCH --qos main
#SBATCH --mem=20G

benefit=(3.6 3.7 3.8 3.9 4 4.1 4.2 4.3 4.4)

module load python/python3/3.11.7
cd /home/edohearn/MATH598/
python /home/edohearn/MATH598/root/testing.py ${benefit[${SLURM_ARRAY_TASK_ID}]}