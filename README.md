# bertfordeprel_slurm
### Introduction ####

This is an adaptation of Kirian Guillier's parser, BertForDeprel : https://github.com/kirianguiller/BertForDeprel .
It is meant to be used in the Paris-Saclay University's cluster called Lab-IA : https://www.lab-ia.fr/

Make sure to : 
- recreate the folder structure required by BertForDeprel.
- set the correct parameters in your ~/.bashrc file , as described here : https://www.lab-ia.fr/faq/ , otherwise the access to the internet won't work and you won't be able to install the libraries. 

Also, cuda is already installed, but to use it,  you need to be on a node; no need to install it locally. 


#######

There are 3 scripts in BertForDeprel : one for training a model from scratch -> pretrain.py,
one for finetuning a model -> train.py
and one to make the predictions (to parse on empty conll files) -> predict.py

Each script is executed through a bash file : 

bertfordeprel1.sh executes pretrain.py
bertfordeprel2.sh executes train.py
bertfordeprel3.sh executes predict.py

In these 3 files, change the " cd ...." line to your BertForDeprel directory. 

To run the bash files, use the command sbatch <file.sh>







