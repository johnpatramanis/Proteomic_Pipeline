**A Proteomic Pipeline for Phylogenetic Reconstruction by Yiannis P. - Work In Progress**

**What is this?**

Compiled scripts in the form of pipelines to enable easier and reproducable phylo-proteomic analyses.

**Huh interesting, how do they work?**

All of the scripts are based on Snakemake and Conda. This tutorial is designed to help you install and use them for your own projects. I highly recomend reading through if you want to use them as well as trying to run the example files that are included here! The pipelines are split up and the subcomponents are designed to function independently but can also be used one after the other, as they intrinsically synergise. Each pipeline is in its own folder, which contains the Snakemake script, a YAML file to create the conda environment, additional R or python scripts utilised by the pipeline as well as example data and files.

These sub-pipelines are:

1) Dataset Initialization
   Scripts to set up pipeline number 2 but also enable the quick search and download of reference proteomes given a list of proteins.

2) Dataset Construction
   Scripts to download proteomic data, transform DNA datasets to protein ones and properly format them.
   
3) Analysis 
   Scripts to assemble a proteomic dataset, format and prepare it for a phylgenetic analysis- including the actual phylogenetic tree creation
   
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>

   
   
   
   
   
**Instalation of Pipelines and User Guide for _Dataset Initialization_ / _Dataset Preparation_ /  _Dataset Analysis_**

This guide assumes that you are working on a Linux enviroment, preferably a server.
<br />It should work on a Linux personal computer, but this is generally not recomended.
<br />For steps 1-3, you only need to run the once for every personal-computer/server/server-user. Each of the 3 pipelines is semi-autonomus, thus can be run without necesserely running the other 2 pipelines. If for example you just want to run the Dataset Construction pipeline, look bellow for its instalation guide and go through all the steps. If you then also want to run the Dataset Analysis, scroll further down and find its guide.You can skip steps 1,2 and 3 however, if you've gone through them at least once.

<br/><br/>
<br/><br/>
<br/><br/>

**Download and set up of entire Pipeline**

**Step 1)** **Conda**

This pipeline is reliant on conda to deploy all the required dependencies for it to function. First you can check if you have conda installed on your computer by typing 'conda' in the command line. If a bunch of options pop up then move to the next step. If nothing happens, then look here on how to install it: https://conda.io/projects/conda/en/latest/user-guide/install/index.html
It probably involves going to this page: https://www.anaconda.com/products/individual , copying the link of the download page and then using wget.
If you just installed conda, make sure you close your session and re-open it to be able to use it from the command line!




**Step 2) Activation and Git clone**

Now with both conda and mamba installed we will download the package itself into your computer. Before we do that first lets activate the conda base enviroment.

``` conda activate base ```

And now lets download the github repository, the core of the pipeline usig git clone. First move to a directory where you want to have this pipeline installed. Then simply type:

``` git clone https://github.com/johnpatramanis/Proteomic_Pipeline.git ```

and move into the directory that we will work in:

``` cd Proteomic_Pipeline/Dataset_Initialization/ ```

<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>


**Installation of Dataset Initialization and usage**


**Step 3) Enviroment Creation**   

Now we are ready for one of the mos important steps: creating a functionng enviroment within conda that contains all the required dependencies for the pipeline to work!
If you want to use the Dataset Construction pipeline for example, make sure you are in the **'Proteomic_Pipeline/Dataset_Construction/'** fodler and that there is a **'Initiator.yml'** file in there.
If so simply type: ``` conda env create -f Initiator.yml ```
This may take a while to install everything...
Once this is done, remember to activate the enviroment we just created by typing:
``` conda activate Initiator ```


**Step 4) Select the Proteins, Organism and Version (assembly)**

In this step we will set up the process for downloading and creating a 'reference proteome'. There are only 2 things we need for this step:
1) A txt file with the names of the proteins/genes you are interested in, which should bare the name 'Proteins.txt' and 
2) A txt file with the name of the organism(s) and (optional) the version of the assembly you want, which should bare the name 'Organism.txt'

You can find one example file of each of these 2 files in the Dataset_Initialization folder. If you look at the examples you will notice 2 things, the protein folder uses the Gene names as described in Ensembl and is limited to one protein/gene per line. Be careful not to have the same gene twice in the dataset, otherwise snakemake will crash and cry about duplicate output files.

The Organism file is also limited to one organism per line (it will run the whole process for each organism provided) but importantly uses the scientific name of the organism connected by an '\_' (e.g. instead of Human -> Homo\_sapiens ) AND if you want to use a different version of the genome, instead of the latest release which is the default, you can add it next to the organism seperate by a tab. To do that check out Ensembl for the name of the version you want e.g. for the African Elephant you would type Loxafr2 for the previous version. Alternatively if you want to use the latest version, you can just ignore this part and just have the name of the organism by itself.

**REMEMBER** the organsim and version you select, since if you later want to transalte BAM files into proteins, you need these bam files to be aligned to the same organism/version!




**Step 5) Get the data**

Now we just need to activate the conda enviroment, by typing ```conda activate Initiator ```
If the above mentioned files were set up correctly you should be able to just run the pipeline by just typing ``` snakemake -jN ``` , where N is the number of cores you want to use. Remember that this wont work if you have not activated the conda enviroment first, which you would need to do every time you restart a session in your server!


<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>




**Instalation of Dataset Preparation and set up**



**Step 3) Enviroment Creation**   

Now we are ready for one of the mos important steps: creating a functionng enviroment within conda that contains all the required dependencies for the pipeline to work!
If you want to use the Dataset Construction pipeline for example, make sure you are in the **'Proteomic_Pipeline/Dataset_Construction/'** fodler and that there is a **'Translator.yml'** file in there.
If so simply type: ``` conda env create -f Translator.yml ```
This may take a while to install everything...
Once this is done, remember to activate the enviroment we just created by typing:
``` conda activate Translator ```


**Step 4) Prepare your Data for translation**

If everything worked until now, then we are almost set! Now we just need to get some DNA data to translate them over to proteins. If you are using a species that is already aligned to the Human genome (ch37) then all you need to do is place your bam files in the '/Dataset_Construction/Workspace/1_OG_BAM_FILES' folder and then in the '/Dataset_Construction/' folder edit the 'samples.txt' file to contain each sample name per line. If your bam file is named 'SAMPLE.bam' then simply write the name 'SAMPLE' in the sample.txt file. Make sure each bam file is indexed as well (its accompanied by a bam.bai file). If not use samtools index -b command to do so in the 1_OG_BAM_FILES folder.

If you don't have any bam files at hand or simply want to test if the pipeline works, you can type ``` bash 0_Download_Bam_files.sh``` and some bam files will be downloaded and placed in the right folder. The samples.txt file also by default corresponds to these samples. Keep in mind that these files are around 100GB each, so make sure you have space!




If your bam files are aligned to a different species or reference genome, then you need to run the 'Dataset_Initiatialization' pipeline, to create the required files for the translation of your target proteins.


To sum up:
a) Bam files along with their bai index file should be in the Dataset_Construction/Workspace/1_OG_BAM_FILES/ 
b) The 'Samples.txt' file should have the name of each bam file (without the .bam ending), 1 name per line. Also make sure you dont have an empty line, or it will try to find a bam file named ''.bam
c) You are located in the main directory ( ..../Dataset_Construction/ ) at the end of this step


**Step 5) Execute the translation**

With your sample files set up, all you need to do now is initiate the process.
Type ```snakemake -j1 ``` to begin. The command -j1 controls how many cores will be used by the pipeline, e.g. -j8 uses 8 cores, -j16 uses 16 etc
If everything works out, you should get your resulting proteins in the 'Dataset_Construction/Workspace/FINAL_OUTPUT' folder.
   


<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>



**Instalation of Dataset Analysis (Phylogenetic Reconstruction)**



**Step 3) Enviroment Creation**   

Now we are ready for one of the mos important steps: creating a functionng enviroment within conda that contains all the required dependencies for the pipeline to work!
If you want to use the Dataset Analysis pipeline for example, make sure you are in the **'Proteomic_Pipeline/Dataset_Analysis/'** fodler and that there is a **'Analyser.yml'** file in there.
If so simply type: ``` conda env create -f Analyser.yml ```
This may take a while to install everything...
Once this is done, remember to activate the enviroment we just created by typing:
``` conda activate Analyser ```


**Step 4) Set up your Dataset for the Analysis**

Once you have activated the conda enviroment, your computer should now have a couple of more tools installed and available to use: e.g. MUSCLE (aligner for fasta files), PhyML (Phylogenetic tree construction) and a number of R packages. These will be used by the pipeline automatically, but you can also use them on your onw if you want.

There is practicaly only one thing you need to set up for this pipeline: your dataset. Your dataset should be .fasta format file, containing all the sequences you want to use, including the target samples and labeled correctly. Each fasta entry that contains the amino acid sequence of one protein should have a label like this: **Pan_troglodytes_AHSG/1-368** . The "/" seperating the label from the information of the sequence is optional, but the important thing is that the label of each entry is composed of the **name of the sample first** eg Pan_troglodytes and then followed by the name of the gene/protein **AND** connected together using an **\_**. A fasta file example will be later included to better showcase how this looks and to also act as a test file. Once your naming is complete you can place your dataset in the Proteomic_Pipeline/Dataset_Analysis/Workspace/1_OG_Dataset/ folder.

Finally in the Proteomic_Pipeline/Dataset_Analysis/ folder there should be a 'Datasets.txt' file. Open that file to edit it. In the first column you should put the full name of your dataset file (the one we just moved in the Workspace) and in the second one the name of the target sample (the ancient one you want to assign phylogeneticaly). If your dataset contains multiple ancient samples, I highly suggest 'analysing' them at the same time, by writing all of their names in the second column, seperated only by commas. Each row should have 2 items: name of the dataset file and the name of the sample(s). If you want to process multiple datasets, just add more rows!


**Step 5) Run the Phylogenies!**

With your dataset files all set up, all you need to do now is initiate the process.
Type ```snakemake -j1 ``` to begin. The command -j1 controls how many cores will be used by the pipeline, e.g. -j8 uses 8 cores, -j16 uses 16 etc.
If everything works out, you should get your resulting tree files in the appropriate folder in Worksapce.
   
   


<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>

   
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
   



```bash
   Necesary coding
```

**Development To Do list: (Dataset Initialization) - By Yiannis , for Yiannis
   1) Isoforms???
 
   
  **Development To Do list: (Dataset Analysis)** - By Yiannis , for Yiannis
  1) Split up env per step? maybe no
  2) Extend to star-BEAST alternatives that do MSC
  3) replace grep command in Rscript2 -> fix names of dataset as they load and pick correctly the sample
  4) Final touches to masking option, how to input them - concatenation
