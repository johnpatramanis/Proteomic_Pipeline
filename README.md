**Proteomic_Pipeline - Under Construction!**

**What is it?**

Compiled scripts to enable phyloproteomic analysis suing Snakemake.

1) Dataset Construction (Working check bellow for instalation)
   Scripts to download proteomic data, transform DNA datasets to protein ones and properly format them.
2) Analysis (Under development)
   Scripts to assemble a proteomic dataset, format and prepare it for a phylgenetic analysis- including the actual phylogenetic tree creation
   
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
   
   
   
   
   
**Instalation - User Guide**

This guide assumes that you are working on a Linux enviroment, preferably a server. It should potentially work on a personal computer and even a Macintosh enviroment but I would suggest not to do that.

**Step 1)** **Conda**

This pipeline is based on conda to deploy all the required dependencies for it to function. First check if you have conda installed on your computer by typing 'conda' in the command line. If a bunch of options pop up then move to the next step. If nothing happens, then look here on how to install it: https://conda.io/projects/conda/en/latest/user-guide/install/index.html




**Step 2) Mamba**

This pipeline also requires snakemake to work. Snakemake suggest that you have Mamba installed with conda so we will also do that. With conda installed succesfully, you can simply type : ``` conda install -n base -c conda-forge mamba ```
and conda will take care of the rest.


**Step 3) Activation and Git clone**

Now with both conda and mamba installed we will download the package itself into your computer. Before we do that first lets activate the conda base enviroment.

``` conda activate base ```

And now lets download the github repository, the core of the pipeline usig git clone. First move to a directory where you want to have this pipeline installed. Then simply type:

``` git clone https://github.com/johnpatramanis/Proteomic_Pipeline.git ```

and move into the directory that we will work in:

``` cd Proteomic_Pipeline/Dataset_Construction/ ```
   
   
   
**Step 4) Enviroment Creation**   

Now we are ready for one of the mos important steps: creating a functionng enviroment within conda that contains all the required dependencies for the pipeline to work!
Make sure you are in the **'Proteomic_Pipeline/Dataset_Construction/'** fodler and that there is a **'Translator.yml'** file in there.
If so simply type: ``` conda env create -f Translator.yml ```
This may take a while to install everything...
Once this is done, remember to activate the enviroment we just created by typing:
``` conda activate Translator ```

   
   
   
   
   
   
   
   
   
   
   
   
**Development To Do list: (Dataset Construction)**
   1) Rename folders?
   2) Dependencies and software: Get slim list of conda env - > split it up to sub env? - Rscript and R?
   3) angsd asks if you want to overwrite-> always do?
   4) Alternative path to FASTA files for pre split bam files
   5) Make 'FRMT' files temporary?
   6) Pre bam file input?
   7) Different use for ancient / modern samples
