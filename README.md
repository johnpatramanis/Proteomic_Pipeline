# A Proteomic Pipeline for Phylogenetic Reconstruction by Yiannis P. -  /// Work In Progress!! /// 

## What is this?

Here you will find all the code needed to run the *Paleo-Phylo-Proteomic Pipelines* to enable easier and more reproducable paleoproteomic analyses.
They take the form of Snakemake scripts coupled with Conda enviroments and below you can find a step by step tutorial on how to run them on your linux machine!

**Huh interesting, how do they work?**

All of the scripts are based on Snakemake and Conda. I highly recomend reading through the tutorial if you want to use them. The pipelines are split up and the subcomponents are designed to function semi-independently but can also be used one after the other, as they intrinsically synergise. Each pipelinehas its own folder, which contains the Snakemake script, a YAML (.yml) file to create the conda environment, additional R and/or python scripts utilised by the pipeline as well as some example files.


**The 3 pipelines are:**

**1) Dataset Initialization:**

Easily download reference proteins/proteomes and fetch all resources required for the translation through Dataset Construction.

**2) Dataset Construction:**

  Translate proteins from Whole Genome datasets. Supports BAM,CRAM and VCF files as input.
   
**3) Dataset Analysis:**

   Align a proteomic dataset, format and prepare it for a phylgenetic analysis- including the actual phylogenetic tree creation
   
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>

   
# Tutorial
## How to build the 'Paleo Proteomic Hominid Reference Dataset' and how to use it to reconstruct the phylogeny of H. antecessor:

<br/><br/> 

## INTRODUCTION

This tutorial aims to introduce the functionality of the pipelines by easily recreating the paleoproteomic-based phylogeny of Homo antecessor from Frido et al.2020 & Gigantopithecus blacki from Welker 2019 et. al . It is written with a non-bioinformatics background audience in mind and tries to go step by step, explaining as much as possible for each step. 

<br/><br/>
<br/><br/>

## STEP 0 - Installation

The first step is the installation of the pipelines. The pipelines require a Linux operating system with Conda installed. If you have that, then the installation is quite straightforward. If you don't have  Conda installed, you can find a quick guide on how to do that here: https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html.

If conda is installed and ready to go, we can start the tutorial! First navigate to a location on your computer where you want to install them and have sufficient space. Then, download the pipelines from github using the simple command:

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
???conda??? on your command line, 
Screenshot of typing that

If the result matches the above screenshot, Conda is set and we can move on.

To install all 3 pipelines enter the `???Proteomic Pipeline???` folder using

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
Finally since our goal here is to reconstruct the phylogeny of H.antecessor , we will download the protein sequences from the publication itself and then apply some shell magic to remove the Erectus sample that is also included and modify the labels to suit the pipeline.

```bash
wget https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-020-2153-8/MediaObjects/41586_2020_2153_MOESM4_ESM.txt -O PaleoProteome.fa
```

Some shell magic....

```bash
END_LINE=$(grep -o -i -n -m 1 Dmanisi_H_ere  PaleoProteome.fa | cut -d ':' -f 1)
END_LINE=$(expr $END_LINE - 1)
head -n $END_LINE PaleoProteome.fa > H_antecessor.fa
sed -i 's/\(>Atapuerca_H_antecessor_.\+\)GN.\+/\1/' H_antecessor.fa
```
And the Antecessor is ready to go!

Similarly we can also download and prepare the Gigantopethicus data.

```bash
wget https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-019-1728-8/MediaObjects/41586_2019_1728_MOESM3_ESM.txt -O Gigantopethicus_Raw.fa
cat Gigantopethicus_Raw.fa | sed  's/.\+\(Gigantopithecus\).\+GN=\(.\+\)/\1_\2/' | cut -d ' ' -f 1 > Gigantopethicus.fa
```


<br/><br/>

You should now have both the 2 ancient protein samples downloaded and properly formatted.
If all 3 pipelines were installed without an error and the data was successfully downloaded, then congratulations , we can now start our phylogenetic reconstruction!



<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>







## STEP 1 ( Reference Dataset Initialisation )

The only sequences we have on our hands right now are the proteins of H.antecessor. To recreate its phylogeny, we first need to set up a reference dataset with which we can compare our sample. To do that, we can use Pipeline 1, and create the ???skeleton??? of the reference dataset, using the reference proteomes of different species that we expect to be somewhat related to H.antecessor. So let???s get ready to do that.

```bash
cd ./Dataset_Initialization
conda activate Initiator
```

With the above commands we are now inside the folder of Pipeline 1 and have ???activated??? the pipeline???s environment. This environment has now also unlocked new software on our command line, which the pipeline will use. You can test this out by typing:
```bash
snakemake
```

You can read more about conda environments here if you are interested: LINK
For now, all you need to know is, activating the right environment is needed to use each of the pipelines.

To use this pipeline we just need two things:
1 txt file, named ```Proteins.txt``` with the proteins we are interested in and
1 txt file, named ```Organism.txt``` with the scientific names of the species we are interested in.
For this tutorial these files are already prepared and ready to use.
You can take a look at them using

(OPTIONAL COMMANDS)
```bash
less Proteins.txt
less Organism.txt
```

and you may want to edit them and add some proteins or species using:

```bash
nano Proteins.txt
nano Organism.txt
```

For this example the proteins we are interested in are the ones recovered for the *H.antecessor* and the species we are interested in are thought to be at least somewhat related to H.antecessor. Now, to execute the pipeline simply type:

```bash
snakemake -j4 --resources FTP=7
```

Depending on the computing power of your computer, you can increase the number of cores being used, by typing -j8 or  -j16 if you want to utilize 8 or 16 cores instead of 4. 
Once the pipeline finishes running you can check the results by diving into the ```Workspace``` folder. There are many output files that we will use later on, but the most important ones for now are located in:
```Workspace/3_FASTA_Seqs/All_Sequences.fa```

where all your proteins for all your species are stored.
Different subsets of this fasta file can be found here: 

```/Dataset_Initialization/Workspace/3_FASTA_Seqs/Combined_Per_Species/```
```/Dataset_Initialization/Workspace/3_FASTA_Seqs/Combined_Per_Protein/```

We can save this simple reference dataset we have created using shell commands:

```bash
cp ./Workspace/3_FASTA_Seqs/All_Sequences.fa >> Reference_Proteomes.fa
```  

<br/><br/>
<br/><br/>   
<br/><br/>
<br/><br/>

## STEP 2 ( Dataset Enhancement)

We now have the ???skeleton??? of our reference dataset ready and if we wanted we could move straight on to STEP 3 and generate a tree from it. However for the purpose of this tutorial we will also go through STEP 2 and ???enhance??? our dataset with protein data from the translation of available genomic data. To do this we can use the 2nd pipeline. First we need to download some data to translate. For this example we will build the same reference genome presented in the publication of this workflow ??? INSERT NAME OF PUBLICATION HERE ??? . We will use the following datasets:

https://www.biorxiv.org/content/10.1101/2021.02.06.430068v2.full 

https://www.nature.com/articles/nature12228 

https://pubmed.ncbi.nlm.nih.gov/28982794/

WARNING ABOUT DATA SIZE!!

```bash
COMMANDS TO WGET DATASETS in the right folder
COMMAND TO WGET GRCH37 or HG18
```

ALTERNATIVE LIGHTER VERSION OF DWONLOAD

```bash
COMMANDS TO WGET DATASETS in the right folder
COMMAND TO WGET GRCH37 or HG18
```




```bash
cd ./Dataset_Construction/
```


Now that we have downloaded our datasets we are ready to set up the translation. The translation of a genome requires a number of resources specific to the reference assembly, the data are mapped on to. Considering the data we downloaded correspond to different reference genomes ( All of them are mapped onto the human reference genome, but different versions of it) we have to run the pipeline multiple times separately for each reference (2 times). 

As we just mentioned, translation requires a couple of resources. First we need the location (chromosome/scaffold,position & strand) of the gene that produces the protein. Most genes require splicing, so we also need the exon and intron information . Finally, a reference amino acid sequence of the protein is also necessary. Given that we have run Pipeline 1 for the proteins of interest and the organisms and reference versions of interest (Homo sapiens GRCh37 & GRCh38), all of this data has been downloaded and is available to us.

We???ll start with the 2 first datasets, which are both mapped on to GRCh38. First we need a txt file named ```Organism.txt```, where the organism and reference version for the translation are given. For GRCh38 one is already in place and we can take a look at it with

```bash
less Organism.txt
(Screenshot of file)
```

Then we need a list of the samples we want to translate from, in the form of a txt file named ???Samples.txt???. Since all of them are BAM files inside the folder ```Dataset_Construction/Workspace/1_OG_BAM_FILES/```we can use:

```bash
ls Dataset_Construction/Workspace/1_OG_BAM_FILES/*.bam | cut -d ???.???  -f 1 > Samples.txt
```

Notice that for the list the file extension should not be mentioned, just the name of the bam file.
We can take a look at how the file looks with:

```bash
less Samples.txt
```

# (SCREENSHOT HERE)

With these two files set up, we don???t need anything else. If we have successfully run Pipeline 1 for the proteins of interest, then Pipeline 2 will translate those.
All we need to do now, is switch to the appropriate conda environment and execute the pipeline:

```bash
conda deactivate
conda activate Translator
snakemake -j4
```

This will take some time! Again, in the example above we use 4 cores, but if your computer is more powerful, you can try increasing the number of cores (e.g. -j32 ) to increase efficiency and decrease waiting time. Once this dataset finishes, we can take a look at the results by:

If disk space is an issue for you, we can use one of Snakemake's features to reduce the amount of output the pipeline generates. Specifically we can use the parameter 
``` --all-temp ``` which will make sure that any outputs between the input and the final output are deleted once used by the pipeline. To use it simply run

```bash
snakemake -j4 --all-temp 
```

```bash
less Workspace/9_FINAL_OUTPUT/ALL_PROT_REFERENCE.fa
```

and we can store the result somewhere as

```bash
cp Workspace/9_FINAL_OUTPUT/ALL_PROT_REFERENCE.fa Great_Apes_and_Modern_Humans.fa
```

Next we want to translate a different dataset, namely Prufer et al 2017. This dataset consists of multiple ancient individuals mapped onto GRCh37 and carefully had their genotypes called. In order to translate them, first we need to switch our reference genome by editing the ```Organism.txt``` file

```bash
echo ???Homo_sapiens	GRCh37??? > Organism.txt

```
Then, since our data are now VCF files, we need a slightly different method of translating them. 
WE have downloaded earlier the VCF files and placed them into ```Workspace/0_VCF_FILES/```
In order to prepare them for the translation, we can use a custom python script.

```bash
python3 Workspace/0_VCF_FILES/VCF_sample_list_generator.py -V (comma sep list of VCF) -R GRCh37.fa
mv Workspace/0_VCF_FILES/VCF_Samples.txt ./
```

If we take a look at this new VCF_Samples.txt file, we can see the format required for the samples: A file with 3 space separated columns, one with the name of the sample inside the vcf, one with the name of the vcf file and one with the reference fasta file that corresponds to the sample.

```bash
less VCF_Samples.txt 
```
We also need to delete the previous Samples.txt file, otherwise the pipeline will attempt to retranslate those as well

```bash
rm Samples.txt
```
We are now set for the new translation and we can execute it again, by typing

```bash
snakemake -j4
```

And once this is also finished, we can combine the resulting translations into one dataset, along with the *H.antecessor* and exit the pipeline folder and environment.

```bash
cat Workspace/9_FINAL_OUTPUT/ALL_PROT_REFERENCE.fa >> Translated.fa
cat Great_Apes_and_Modern_Humans.fa >> Translated.fa
conda deactivate
cd ..
```   
   
   
   
   
   
   
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>






## STEP 3 ( Phylogenetic Reconstruction )

We now have the paleo-proteomic data ( ```H_antecessor.fa```) , the reference proteomes ( ```Reference_Proteomes.fa```) and the translated sequences ( ```Translated.fa``` ), which we can all merge together into the dataset we want to run a phylogenetic analysis.

```bash
cat H_antecessor.fa >>  Reference_Data.fa
cat Dataset_Initialization/Reference_Proteomes.fa  >>  Reference_Data.fa
cat Dataset_Construction/Translated.fa >> Reference_Data.fa
```


This ```Reference_Data.fa``` is the fasta file we will use for the phylogenetic reconstruction. We can take a look at how our fasta file looks like, by using


```bash
less Reference_Data.fa
```

Notice that each sequence follows the same pattern of Sample-name_Protein-name . This is very important as this will allow the next pipeline to understand which sequences correspond to which sample and which protein. All of the sequences we have generated and collected follow this pattern. If any additional sequences should be added, they must also follow this format if they are to be utilized properly. 

Now let's move onto the final pipeline and run the phylogeny.

```bash
cp Reference_Data.fa Dataset_Analysis/Workspace/1_OG_Dataset/
cd Dataset_Analysis
conda activate Analyser
```

All we need to do now is let the pipeline know which datasets we want to run and which samples in those datasets are paleo proteomic data, in order to handle them accordingly.


```bash
echo ???Reference_Data.fa	H_antecessor??? > Datasets.txt
```


(OPTIONAL - MASKING MODERN SAMPLES AS ANCIENT)

Now all we have to do is run the pipeline and wait.

```bash
snakemake -j4
```
Once this finishes running you will have a generated tree for each of your porteins individually, as well as one Maximum Likelihood and one Bayesian species from the concatenation of these proteins.

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

## UPDATING  --  NEEDS SOME MORE WRITING

If you have installed this workflow on your computer and a newer version of it has been released, you can simply update it!
To do that go to where the Workflow Folder is located and simply repeat the download step:


```bash
git clone https://github.com/johnpatramanis/Proteomic_Pipeline.git
```

OR

```bash
wget https://github.com/johnpatramanis/Proteomic_Pipeline/archive/refs/heads/main.zip
unzip main.zip
```
This should take care of the code itself. If you need to update the conda enviroments ( e.g. the software used by the pipeline) as well you can find the yaml files in each of the 3 subfolders and do :

```bash
conda env update --name ENV_NAME --file YML_FILE.yml --prune
```

