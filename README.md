# PaleoProPhyler: A reproducible pipeline for Palaeo-Proteomic Phylogenetic reconstruction.

![alt text](https://github.com/johnpatramanis/Proteomic_Pipeline/blob/main/GitHub_Tutorial/PaleoProPhyler%20Overview%20Fig.svg?raw=true)

## What is this?

Here you will find all the code needed to run the *PaleoProPhyler*.
PaleoProPhyler is a compliation of pipelines to enable easier and more reproducable paleoproteomic phylogenetic analyses.
These pipelinese take the form of Snakemake scripts coupled with Conda enviroments and below you can find a step by step tutorial on how to run them on your local linux machine or your labs server!

**Huh interesting, how do they work?**

All of the scripts are based on Snakemake and Conda. I highly recomend reading through the tutorial if you want to use them. The pipelines are split up and the subcomponents are designed to function semi-independently but can also be used one after the other, as they intrinsically synergise. Each pipelinehas its own folder, which contains the Snakemake script, a YAML (.yml) file to create the conda environment, additional R and/or python scripts utilised by the pipeline as well as some example files.


**The 3 pipelines are:**

**1) Dataset Initialization:**

Easily download reference proteins/proteomes and fetch all resources required for the translation through the 'Dataset Construction' module.

**2) Dataset Construction:**

  Translate proteins from Whole Genome datasets. Supports BAM,CRAM and VCF files as input. Data needs to be mapped onto an [annotated reference genome from Ensemb](https://www.ensembl.org/info/about/species.html)
   
**3) Dataset Analysis:**

   Align a proteomic dataset, format and prepare it for a phylgenetic analysis. Run phylogenetic trees including for each individual protein of the dataset and for a concatenation of all of the available proteins.
   
<br/><br/>
<br/><br/>
<br/><br/>

## Tutorial
If you want to try to use PalaeoProPhyler, please see the [Tutorial](GitHub_Tutorial/Tutorial.md) on how to install and use each of its pipelines.

## Code Overview - Under the Hood
If you want to have a detailed explanation of what is happening "under the hood" in each of the modules of PalaeoProPhyler, you can read about it in [the supplementary file](GitHub_Tutorial/Supplementary.pdf). This should provide you with a text explanation as well as commands and links* to scripts. 
Note *:The links only work if you download the pdf file, unfortunately Github's PDF viewer has some limits. 


## Dependencies
The pipelines/workflows presented here use, multiple publicly available software. All of the software and packages used by the pipelines are installed through the conda environments available here ( see [Tutorial](GitHub_Tutorial/Tutorial.md) ). For the full list of the software and packages used, check out the last pages of [the supplementary file](GitHub_Tutorial/Supplementary.pdf):


## User Extentions
Users with experience in conding/bioinformatics are free to alter, add or remove steps of the pipelines if they see fit. If you do that however and use the altered version of the pipeline in a publication, make sure you record and mention every alteration! I would suggest updating the conda environments with any new software that you add and uploading on Github the entire folder of the altered workflows.

## License
PalaeoProPhyler is released under the [MIT License](LICENSE.md)
