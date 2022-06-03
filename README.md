# A Proteomic Pipeline for Phylogenetic Reconstruction by Yiannis P. - Work In Progress!!

## What is this?

Here you will find all the code needed to run the Paleo-Phylo-Proteomic *Pipelines* to enable easier and more reproducable paleoproteomic analyses.
They take the form of Snakemake scripts coupled with Conda enviroments and below you can find a step by step tutorial on how to run them on your linux machine!

**Huh interesting, how do they work?**

All of the scripts are based on Snakemake and Conda. I highly recomend reading through the tutorial if you want to use them. The pipelines are split up and the subcomponents are designed to function semi-independently but can also be used one after the other, as they intrinsically synergise. Each pipelinehas its own folder, which contains the Snakemake script, a YAML (.yml) file to create the conda environment, additional R and/or python scripts utilised by the pipeline as well as some example files.


**The 3 pipelines are:**

**1) Dataset Initialization:**

Scripts to set up a reference protein dataset using reference proteomes. The pipeline also sets up pipeline number 2 with the resources necesary to use it.

**2) Dataset Construction:**

   Scripts to translate DNA datasets into protein ones and properly format them.
   
**3) Dataset Analysis:**

   Scripts to assemble a proteomic dataset, format and prepare it for a phylgenetic analysis- including the actual phylogenetic tree creation
   
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>

   
# Tutorial on how to build the 'Paleo Proteomic Hominid Reference Dataset' and how to use it to reconstruct the phylogeny of H. antecessor:
   
## INTRODUCTION

This tutorial aims to introduce the functionality of the pipelines by easily recreating the paleoproteomic-based phylogeny of H.antecessor from Frido et al. It is written with a non-bioinformatics background audience in mind and tries to go step by step, explaining as much as possible for each step. 

## STEP 0 - Installation

The first step is the installation of the pipelines. The pipelines require a Linux operating system with Conda installed. If you have that, then the installation is quite straightforward. First navigate to a location on your computer where you want to install them and have sufficient space. Then, download the pipelines from github using the simple command:

```bash
git clone https://github.com/johnpatramanis/Proteomic_Pipeline.git
```

If your computer does not have git installed then the above command will fail. You can instead use:

```bash
wget https://github.com/johnpatramanis/Proteomic_Pipeline/archive/refs/heads/main.zip
unzip main.zip
```

If your computer does not already have conda installed, you can get it from here:

You can check if conda is installed and properly set up on your computer by simply typing 
‘conda’ on your command line, 
Screenshot of typing that

If the result matches the above screenshot, Conda is set and we can move on.

To install all 3 pipelines enter the `‘Proteomic Pipeline’` folder using

```cd Proteomic_Pieline``` 

and then one by one, type the commands below:

```bash
conda env create -f ./Dataset_Initialization/Initiator.yml
```
```bash
conda env create -f ./Dataset_Construction/Translator.yml
```
```bash
conda env create -f ./Dataset_Analysis/Analyser.yml
```
Finally since our goal here is to reconstruct the phylogeny of H.antecessor , we will download the protein sequences from the publication itself

```bash
wget H.antecessor_Data_Location
Some shell commands to isolate and format the sequences in a fasta file labeled H_antecessor.fa
```

If all 3 pipelines were installed without an error and the data was successfully downloaded, then congratulations , we can now start our phylogenetic reconstruction!

   
   
   
   
   
<br/><br/>
<br/><br/>
<br/><br/>


<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>

   
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
   



```bash
   ls |cut -d '.' -f 1 
```

**Development To Do list: (Dataset Initialization) - By Yiannis , for Yiannis
   1) Isoforms???
 
   
  **Development To Do list: (Dataset Analysis)** - By Yiannis , for Yiannis
  1) Split up env per step? maybe no
  2) Extend to star-BEAST alternatives that do MSC
  3) replace grep command in Rscript2 -> fix names of dataset as they load and pick correctly the sample
  4) Final touches to masking option, how to input them - concatenation
