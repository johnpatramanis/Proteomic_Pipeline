# PaleoProPhyler: A reproducable pipeline for Palaeo-Proteomic Phylogenetic reconstruction.

![alt text](https://github.com/johnpatramanis/Proteomic_Pipeline/blob/main/GitHub_Tutorial/PaleoProPhyler%20Overview%20Fig.svg?raw=true)

## What is this?

Here you will find all the code needed to run the *PaleoProPhyler*.
PaleoProPhyler is a compliation of pipelines to enable easier and more reproducable paleoproteomic phylogenetic analyses.
These pipelinese take the form of Snakemake scripts coupled with Conda enviroments and below you can find a step by step tutorial on how to run them on your local linux machine or your labs server!

**Huh interesting, how do they work?**

All of the scripts are based on Snakemake and Conda. I highly recomend reading through the tutorial if you want to use them. The pipelines are split up and the subcomponents are designed to function semi-independently but can also be used one after the other, as they intrinsically synergise. Each pipelinehas its own folder, which contains the Snakemake script, a YAML (.yml) file to create the conda environment, additional R and/or python scripts utilised by the pipeline as well as some example files.


**The 3 pipelines are:**

**1) Dataset Initialization:**

Easily download reference proteins/proteomes and fetch all resources required for the translation through Dataset Construction.

**2) Dataset Construction:**

  Translate proteins from Whole Genome datasets. Supports BAM,CRAM and VCF files as input. Data needs to be mapped onto an [annotated reference genome from Ensemb](https://www.ensembl.org/info/about/species.html)
   
**3) Dataset Analysis:**

   Align a proteomic dataset, format and prepare it for a phylgenetic analysis- including the actual phylogenetic tree creation
   
<br/><br/>
<br/><br/>
<br/><br/>

## Tutorial
If you want to try to use this, please see the [Tutorial](GitHub_Tutorial/Tutorial.md) on how to install and use the pipelines.

## Dependencies
The pipelines/workflows presented here, multiple, publicly avaialble, software. All of the software and packages used by the pipelines are installed through the conda environments available here (see [Tutorial](GitHub_Tutorial/Tutorial.md) ). For the full list of the software and packages used, check out the last pages of [the supplementary file](GitHub_Tutorial/Supplementary.pdf):

