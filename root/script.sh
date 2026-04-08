#!/bin/bash
#SBATCH --job-name=Games_on_Graphs
#SBATCH --mail-type=ALL
#SBATCH --mail-user=edohearn@crimson.ua.edu
#SBATCH -n 1 #tasks
#SBATCH -N 1 #nodes
#SBATCH -c 1 #number of cores per task

#SBATCH -o Output/output_GoG.txt
#SBATCH -p main
#SBATCH --qos main
#SBATCH --mem=20G


module load python/python3/3.11.7
cd /home/edohearn/MATH598/
.venv/Scripts/activate
python /home/edohearn/MATH598/root/main.py