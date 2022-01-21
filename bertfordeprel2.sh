#!/bin/sh
#BATCH --job-name=bertfordeprel          # name of the job
#SBATCH --partition=all        # request for allocation on the CPU partition
#SBATCH --ntasks=1                  # number of tasks (a single process here)
#SBATCH --cpus-per-task=20          # number of OpenMP threads
# /!\ Caution, "multithread" in Slurm vocabulary refers to hyperthreading.
#SBATCH --time=47:59:05             # maximum execution time requested (HH:MM:SS)
#SBATCH --output=omp%j_test.out          # name of output file
#SBATCH --error=omp%j_test.out           # name of error file (here, in common with outp
#SBATCH --gres=gpu:1
###SBATCH --nodes=55
###SBATCH --mem = 32
###SBATCH --requeue
###SBATCH --qos=preempt$
#SBATCH --exclude=n1,n2,n3,n4,n5
srun hostname
srun echo --------------------------------------
srun pwd
srun echo --------------------------------------
source ~/.bashrc
source activate base
cd ~/bertfordeprel/Paris_Stories_Parser_normalized2
NCCL_SOCKET_IFNAME=eno1
python3 train.py
