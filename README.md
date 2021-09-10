**Proteomic_Pipeline - Under Construction!**

**What is it?**

Compiled scripts to enable phyloproteomic analysis suing Snakemake.

1) Dataset Construction
   Scripts to download proteomic data, transform DNA datasets to protein ones and properly format them.
2) Analysis 
   Scripts to assemble a proteomic dataset, format and prepare it for a phylgenetic analysis- including the actual phylogenetic tree creation
   
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>

   
   
   
   
   
**Instalation of Pipelines and User Guide for _Dataset Preparation_ /  _Dataset Analysis_**

This guide assumes that you are working on a Linux enviroment, preferably a server. It should potentially work on a personal computer and even a Macintosh enviroment but I would suggest not to do that. Steps 1-3 need only be done once for every computer. If for example you just want to run the Dataset Preparation pipeline, look bellow for its instalation guide and go through all the steps. If you then also want to run the Dataset Analysis,scroll further down and find its guide, you can skip steps 1,2 and 3 however, if you've gone through them once.

**Instalation of Dataset Preparation and set up**

**Step 1)** **Conda**

This pipeline is reliant on conda to deploy all the required dependencies for it to function. First check if you have conda installed on your computer by typing 'conda' in the command line. If a bunch of options pop up then move to the next step. If nothing happens, then look here on how to install it: https://conda.io/projects/conda/en/latest/user-guide/install/index.html
If you just installed conda, make sure you close your session and re-open it to be able to use it from the command line!




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
If you want to use the Dataset Construction pipeline for example, make sure you are in the **'Proteomic_Pipeline/Dataset_Construction/'** fodler and that there is a **'Translator.yml'** file in there.
If so simply type: ``` conda env create -f Translator.yml ```
This may take a while to install everything...
Once this is done, remember to activate the enviroment we just created by typing:
``` conda activate Translator ```


**Step 5) Prepare your Data for translation**

If everything worked until now, then we are almost set! Now we just need to get some DNA data to translate them over to proteins. If you are using a species that is already aligned to the Human genome (ch37) then all you need to do is place your bam files in the '/Dataset_Construction/Workspace/1_OG_BAM_FILES' folder and then in the '/Dataset_Construction/' folder edit the 'samples.txt' file to contain each sample name per line. If your bam file is named 'SAMPLE.bam' then simply write the name 'SAMPLE' in the sample.txt file. Make sure each bam file is indexed as well (its accompanied by a bam.bai file). If not use samtools index -b command to do so in the 1_OG_BAM_FILES folder.

If you don't have any bam files at hand or simply want to test if the pipeline works, you can type ``` bash 0_Download_Bam_files.sh``` and some bam files will be downloaded and placed in the right folder. The samples.txt file also by default corresponds to these samples. Keep in mind that these files are around 100GB each, so make sure you have space!




If your bam files are aligned to a different species or reference genome, then things will get more complicated as other files need to be re-adjusted. if you want to target different proteins than the enamel presets, then you also need to make some adjustments. These are described in step number 7 & 8.

To sum up:
a) Bam files along with their bai index file should be in the Dataset_Construction/Workspace/1_OG_BAM_FILES/ 
b) The 'Samples.txt' file should have the name of each bam file (without the .bam ending), 1 name per line. Also make sure you dont have an empty line, or it will try to find a bam file named ''.bam
c) You are located in the main directory ( ..../Dataset_Construction/ ) at the end of this step

**Step 6) Execute the translation**

With your sample files set up, all you need to do now is initiate the process.
Type ```snakemake -j1 ``` to begin. The command -j1 controls how many cores will be used by the pipeline, e.g. -j8 uses 8 cores, -j16 uses 16 etc
If everything works out, you should get your resulting proteins in the 'Dataset_Construction/Workspace/FINAL_OUTPUT' folder.
   


<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>



**Instalation of Dataset Analysis (Phylogenetic Reconstruction)**

If you have already gone through the previous pipeline (Dataset Analysis) you can skip steps 1-3 and go straight to step 4!

**Step 1)** **Conda**

This pipeline is reliant on conda to deploy all the required dependencies for it to function. First check if you have conda installed on your computer by typing 'conda' in the command line. If a bunch of options pop up then move to the next step. If nothing happens, then look here on how to install it: https://conda.io/projects/conda/en/latest/user-guide/install/index.html
If you just installed conda, make sure you close your session and re-open it to be able to use it from the command line!




**Step 2) Mamba**

This pipeline also requires snakemake to work. Snakemake suggest that you have Mamba installed with conda so we will also do that. With conda installed succesfully, you can simply type : ``` conda install -n base -c conda-forge mamba ```
and conda will take care of the rest.


**Step 3) Activation and Git clone**

Now with both conda and mamba installed we will download the package itself into your computer. Before we do that first lets activate the conda base enviroment.

``` conda activate base ```

And now lets download the github repository, the core of the pipeline usig git clone. First move to a directory where you want to have this pipeline installed. Then simply type:

``` git clone https://github.com/johnpatramanis/Proteomic_Pipeline.git ```

and move into the directory that we will work in:

``` cd Proteomic_Pipeline/Dataset_Analysis/ ```


**Step 4) Enviroment Creation**   

Now we are ready for one of the mos important steps: creating a functionng enviroment within conda that contains all the required dependencies for the pipeline to work!
If you want to use the Dataset Analysis pipeline for example, make sure you are in the **'Proteomic_Pipeline/Dataset_Analysis/'** fodler and that there is a **'Analyser.yml'** file in there.
If so simply type: ``` conda env create -f Analyser.yml ```
This may take a while to install everything...
Once this is done, remember to activate the enviroment we just created by typing:
``` conda activate Analyser ```


**Step 5) Set up your Dataset for the Analysis**

Once you have activated the conda enviroment, your computer should now have a couple of more tools installed and available to use: e.g. MUSCLE (aligner for fasta files), PhyML (Phylogenetic tree construction) and a number of R packages. These will be used by the pipeline automatically, but you can also use them on your onw if you want.

There is practicaly only one thing you need to set up for this pipeline: your dataset. Your dataset should be .fasta format file, containing all the sequences you want to use, including the target samples and labeled correctly. Each fasta entry that contains the amino acid sequence of one protein should have a label like this: **Pan_troglodytes_AHSG/1-368** . The "/" seperating the label from the information of the sequence is optional, but the important thing is that the label of each entry is composed of the **name of the sample first** eg Pan_troglodytes and then followed by the name of the gene/protein **AND** connected together using an **\_**. A fasta file example will be later included to better showcase how this looks and to also act as a test file. Once your naming is complete you can place your dataset in the Proteomic_Pipeline/Dataset_Analysis/Workspace/1_OG_Dataset/ folder.

Finally in the Proteomic_Pipeline/Dataset_Analysis/ folder there should be a 'Datasets.txt' file. Open that file to edit it. In the first column you should put the full name of your dataset file (the one we just moved in the Workspace) and in the second one the name of the target sample (the ancient one you want to assign phylogeneticaly). If your dataset contains multiple ancient samples, I highly suggest 'analysing' them at the same time, by writing all of their names in the second column, seperated only by commas. Each row should have 2 items: name of the dataset file and the name of the sample(s). If you want to process multiple datasets, just add more rows!


**Step 6) Run the Phylogenies! **

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
   
   
   
**Development To Do list: (Dataset Initialization) - By Yiannis , for Yiannis
   0) How to contact datbases help: https://www.ebi.ac.uk/proteins/api/doc/#proteins_search_anchor / http://rest.ensembl.org/
   1) Get Protein - Gene name
   2) Get Coordinates on genome (start and end) + strand
   3) Get Fasta file of protein
   4) Get at least one exons - introns table
   5) Isoforms???
 
**Development To Do list: (Dataset Construction)** 
   1) IMPORTANT FIX reading of template fasta files-> organism name and Protein name should be switched in time!
   2) IMPORTANT Try the --no-build method for creating a yml file from conda env
   4) Make 'FRMT' files temporary?
   5) Pre bam file input?
   6) Different use for ancient / modern samples
   
  **Development To Do list: (Dataset Analysis)** - By Yiannis , for Yiannis
  1) Split up env per step? maybe no
  2) Extend to BEAST software or BEAST alternatives that do MSC
  3) Phylogenetic Network construction
