**Proteomic_Pipeline - Under Construction!**

**What is it?**

Compiled scripts to enable phyloproteomic analysis suing Snakemake.

1) Dataset Construction (Working check bellow for instalation)
   Scripts to download proteomic data, transform DNA datasets to protein ones and properly format them.
2) Analysis (Under development)
   Scripts to assemble a proteomic dataset, format and prepare it for a phylgenetic analysis- including the actual phylogenetic tree creation
   
   
   
   
   
   
   
   
   
**Instalation - User Guide**

This guide assumes that you are working on a Linux enviroment, preferably a server. It should potentially work on a personal computer and even a Macintosh enviroment but I would suggest not to do that.

**Step 1)** **Conda**

This pipeline is based on conda to deploy all the required dependencies for it to function. First check if you have conda installed on your computer by typing 'conda' in the command line. If a bunch of options pop up then move to the next step. If nothing happens, then look here on how to install it: https://conda.io/projects/conda/en/latest/user-guide/install/index.html




**Step 2) Mamba**

This pipeline also requires snakemake to work. Snakemake suggest that you have Mamba installed with conda so we will also do that. With conda installed succesfully, you can simply type : 'conda install -n base -c conda-forge mamba'
and conda will take care of the rest.


**Step 3) Activation and Git clone**

Now with both conda and mamba installed we will download the package itself into your computer. Before we do that first lets activate the conda base enviroment.

'conda activate base'



   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
**Development To Do list: (Dataset Construction)**
   1) Rename folders?
   2) Dependencies and software: Get slim list of conda env - > split it up to sub env? - Rscript and R?
   3) angsd asks if you want to overwrite-> always do?
   4) Alternative path to FASTA files for pre split bam files
   5) Make 'FRMT' files temporary?
   6) Pre bam file input?
   7) Different use for ancient / modern samples
