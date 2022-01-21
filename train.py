#!/usr/bin/python3
# Adapted from Kirian Guiller's Google Collab BertForDeprel parser: https://colab.research.google.com/drive/1UngKLyqRZk7vXawWnYzJtrjrNisPnhgK?usp=sharing
# make sure to have the same folder architecture as required in the tutorial : https://github.com/kirianguiller/BertForDeprel
import os
os.system("git clone https://github.com/kirianguiller/BertForDeprel")
os.system("cd BertForDeprel && git pull origin master")
os.system("python3 -m pip install --user --proxy=http://webproxy.lab-ia.fr:8080 --upgrade pip wheel")
os.system("python3 -m pip install --proxy=http://webproxy.lab-ia.fr:8080 -r BertForDeprel/requirements.txt")

import torch

if torch.cuda.is_available():
    print("Good, everything is working fine (so far) :).")
else:
    print("GPU is not available, you can activate the gpu on the colab session (Edit -> Notebook Settings -> Hardware accelerator = GPU) ")

# Be careful to choose a path that exists
os.system("ls")

# Create the annotation schema

#os.system("python3 BertForDeprel/BertForDeprel/preprocessing/1_compute_annotation_schema.py \
   # --input_folder \"conllus\" \
   # --output_path \"annotation_schema.json\"")

# finetuning starts here
    
os.system("python3 BertForDeprel/BertForDeprel/run.py train \
    --folder \"./\" \
    --ftrain \"conllus/train_normalized_random2.conllu\" \
    --fpretrain \"models/Written_from_scratch_testPS_30e.pt\" \
    --epochs 30 \
    --model Spoken_from_Written_testPS_30e.pt \
    --batch 16 \
    --gpu_ids 0 \
    --punct \
    --bert_type \"camembert-base\"")
   

