   
# Tutorial
<br/><br/>
## How to use PaleoProPhyler's modules.
A step by step guid on how to use the 3 modules of PaleoProPhyler.
Create a Reference Dataset, enhance it with translated data and use it to reconstruct the phylogeny of two palaeoproteomic samples: *H. antecessor* and *G.blacki*.


<br/><br/>
<br/><br/> 

## INTRODUCTION

This tutorial aims to introduce the functionality of the pipelines by easily recreating the enamel paleoproteomic-based phylogeny of Homo antecessor from Welker et al.2020 & Gigantopithecus blacki from  [Welker et al.2020](https://www.nature.com/articles/s41586-020-2153-8) & *Gigantopithecus blacki* from [Welker 2019 et. al.](https://www.nature.com/articles/s41586-019-1728-8). The goal here is not to support the specific phylogenetic placement of these species, but rather to showcase how running the different modules of PaleoProPhyler in conjunction with the published paleo-proteomes can easily reproduce the results presented in those publications. The tutorial is written with a non-bioinformatics-background audience in mind and proceeds in a step by step manner, trying to explain as much as possible in each step. A glossary can be found at the very end of the document explaining a lot of the terms used in the tutorial which, although common in bioinformatics, might be new to someone else.
 

<br/><br/>
<br/><br/>
## REQUIREMENTS
A computer running on Linux OS and has ['Conda'](https://docs.conda.io/en/latest/) installed. If you don't have Conda installed, look below for info.
The tutorial should be a ble to run in a personal computer, but I would suggest running it on a server machine. If your server is using a queing system like ["Slurm"](https://slurm.schedmd.com/documentation.html), I would suggest running the tutorial in an 'interactive session', instead of submitting job queues. In those cases I would also suggest using 32+ GB of RAM for your session, along with a lengthy time limit of 2+ hours. Furthermore, regardless of server or presonal machine, I would suggest having at least a disc space of 20GB or more. Using module number 2 can also require much greater disc space (100+ GB), but that depends on the size of the genomic data you want to translate, so thats optional.

Example of 'Interactive session': srun --nodes=1 --ntasks-per-node=4 --time=48:00:00 --clusters=NAME_OF_CLSUTER --partition=NAME_OF_PARTITION --mem=32GB  --pty bash

<br/><br/>
<br/><br/>

## STEP 0 - Installation and Data preparation

<br/><br/>

### Install Conda
The first step is the installation of the pipeline. The pipeline requires a Linux operating system with ['Conda'](https://docs.conda.io/en/latest/) installed. If you have that, then the installation is quite straightforward. If you don't have Conda , you can find a quick guide on how to do that here: https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html. I suggest installing 'miniconda' instead of 'anaconda', since it has fewer tools preinstalled and thus a lighter 'base environment', upon which we will build the environments of the pipeline (or any other environment you may want to set up in the future).

You can check if conda is installed and properly set up on your Linux machine by simply typing:
```conda```
in your command line.



I would also suggest installing libmamba-solver for conda. Its optional, but in my experience it can radically reduce the time it takes conda to jointly install multiple tools. You can easily install libmamba-solver in your base conda like this:

```bash
conda install -n base conda-libmamba-solver
conda config --set solver libmamba
```

<br/><br/>

### Download the workflows
If conda is installed and ready to go, we can start the tutorial!
First navigate to a location on your computer where you want to install the pipeline and where you have sufficient space. Then, download the pipeline from github using the simple command:

```bash
git clone https://github.com/johnpatramanis/Proteomic_Pipeline.git
```

If your computer does not have git installed then the above command will fail. You can instead use:

```bash
wget https://github.com/johnpatramanis/Proteomic_Pipeline/archive/refs/heads/main.zip
unzip main.zip
mv Proteomic_Pipeline-main Proteomic_Pipeline
```

<br/><br/>

### Install the Conda environments (30 minutes to 2 hours, depending on machine)

To install all 3 sub-Modules of the pipeline enter the `‘Proteomic Pipeline’` folder using

```bash
cd Proteomic_Pipeline
``` 

and then one by one, type the commands below:

```bash
conda env create -f ./Dataset_Initialization/Initiator.yml
```
There could be some messages popping up, simply types 'y' if asked to confirm the installation.
If there is an error instead, look below for an alternative way to install the environment.

<br/><br/>

Then repeat the same process for the other 2 environments:

```bash
conda env create -f ./Dataset_Construction/Translator.yml
```
```bash
conda env create -f ./Dataset_Analysis/Analyser.yml
```
<br/><br/>
If there were no errors until this point, then you have successfully installed all 3 modules!
You can always check which conda environments are installed on your machine by typing:

```bash
conda env list
```
<br/><br/>
<br/><br/> 
<br/><br/> 

#### Installation Errors / Alternative Installations

There are some cases where the conda environments provided here cannot be installed. This tends to happen when base conda already has some packages installed. In these cases you will probably get an error in one of the above steps and the environment will not be (properly) installed. Below you will find alternative commands to install each conda environment by manually installing each the necessary tools into a new environment. If the installation seems to be taking too long (e.g. more than 2 hours) I would suggest terminating it using Control+Z and moving to the next method of installation.

Now, for the first module you can manually install it copying the text below:
```bash
conda create -n Initiator -c conda-forge -c bioconda snakemake
```

<br/><br/>

For the second module:
```bash
conda create -n Translator -c conda-forge -c bioconda  openssl=1.1 bioconductor-shortread angsd blast samtools bcftools biopython snakemake
```

<br/><br/>

For the third module:
```bash
conda create -n Analyser  -c bioconda -c conda-forge snakemake phyml mafft mrbayes revbayes trimal bioconductor-shortread r-stringr r-data.table r-phyclust seqmagick
```

<br/><br/>
<br/><br/>


#### If this still doesn't get the installation to work or the installation seems to be taking **too** long, you can try installing it using Conda & Mamba:
This installation method ustilises [Mamba](https://github.com/mamba-org/mamba) instead of the base conda to 'solve' which software have incompatibilities.

For the first module:
```bash
conda create -n Initiator -c conda-forge mamba
conda activate Intiator
mamba install -c conda-forge -c bioconda snakemake
conda deactivate
```

<br/><br/>

For the second module:
```bash
conda create -n Translator -c conda-forge mamba
conda activate Translator
mamba install -c conda-forge -c bioconda  openssl=1.1 bioconductor-shortread angsd blast samtools bcftools biopython snakemake
conda deactivate
```

<br/><br/>

For the third module:
```bash
conda create -n Analyser -c conda-forge mamba
conda activate Analyser
mamba install -c bioconda -c conda-forge snakemake phyml mafft mrbayes revbayes trimal bioconductor-shortread r-stringr r-data.table r-phyclust seqmagick
conda deactivate
```

<br/><br/>
<br/><br/>
<br/><br/>

### Download and format the published palaeoproteomic data

Finally, since our goal here is to reconstruct the enamel phylogeny of *H.antecessor* and *G.blacki* as they were presented in their original publications, we will download the protein sequences from the publications themselves. We will then apply some shell magic to prepare the files, remove the *H.erectus* sample that is also included the dataset and modify the labels to suit the pipeline.

First Download the published Fasta sequences from the *H.antecessor* repository.

```bash
wget https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-020-2153-8/MediaObjects/41586_2020_2153_MOESM4_ESM.txt -O PaleoProteome.fa
```

Then some shell magic to prepare the file ....

```bash
END_LINE=$(grep -o -i -n -m 1 Dmanisi_H_ere  PaleoProteome.fa | cut -d ':' -f 1)
END_LINE=$(expr $END_LINE - 1)
head -n $END_LINE PaleoProteome.fa > H_antecessor.fa
sed -i 's/\(>Atapuerca_H_antecessor_.\+\)GN.\+/\1/' H_antecessor.fa
```
And the Antecessor is ready to go! You can check the content of the file we just created using 
```bash
less H_antecessor.fa
```

Press 'q' to exit the file.
Similarly we can also download and prepare the Gigantopethicus data.

```bash
wget https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-019-1728-8/MediaObjects/41586_2019_1728_MOESM3_ESM.txt -O Gigantopethicus_Raw.fa
cat Gigantopethicus_Raw.fa | sed  's/.\+\(Gigantopithecus\).\+GN=\(.\+\)/\1_\2/' | cut -d ' ' -f 1 > Gigantopethicus.fa
```


<br/><br/>

You should now have both ancient protein samples downloaded and properly formatted in 2 files: "H_antecessor.fa" & "Gigantopethicus.fa" .
If all 3 pipelines were installed without an error and the data was successfully downloaded, then congratulations , we can now start our phylogenetic reconstruction!



<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>






## STEP 1 - Reference Dataset Initialisation (30 minutes - 1 hour for the example provided)

<br/><br/>
### Activate the first module

The only sequences we have on our hands right now are the proteins of *H.antecessor* and *G.blacki*. In order to explore their phylogeny, we first need to set up a reference dataset with which we can compare their sequences to. We can use the reference proteomes of different species that we expect to be somewhat related to both *H.antecessor* and *G.blacki*. We will use Module 1 of the pipeline, to create the ‘scaffold’ of a reference dataset.  Reference proteomes, like reference genomes, serve as the 'default' representatives of a species. They can be utilised to easily compare organisms with each other and in our case with a new sample of relatively unknown phylogenetic placement. Although practically very useful, reference proteomes cannot represent a species true protein diversity however, which 
 in the worse case scenario will lead to wrong evolutionary inferences. On the other hand, comparing a single ancient sample with hundreds of (translated) modern proteomes can potentially diminish your phylogenetic signal of a only few amino acids. For now let's focus on creating the representative dataset:

```bash
cd ./Dataset_Initialization/
conda activate Initiator
```

With the above commands we are now inside the folder of Module 1 and have ‘activated’ the Conda environment of this 1st module of the pipeline. This environment has now unlocked new software on our command line, which the pipeline will make use of. An example of this is [snakemake](https://snakemake.readthedocs.io/en/stable/), a tool which all of the pipelines are based upon. You can test if snakemake is available to you by typing:

```bash
snakemake --help
```

This will just print out the full command list of snakemake, which means snakemake is ready to go.
You can read more about conda environments [here](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) if you are interested.
For now, all you need to know is that activating the right environment is needed to use each of the modules of the pipeline. Most linux machines display which conda environment is activated at any time point in a bracket next to the command line e.g. (Initiator)


<br/><br/> 
### Prepare input of the first module

To use this module of the pipeline we just need two input files:

a) 1 txt file, named ```Proteins.txt``` with the gene names of the proteins we are interested in. For example if we were interested in Enamelin, we would add ```ENAM``` into that file. Only one gene name per line should be provided. If you are interested in a specific [isoform](https://en.wikipedia.org/wiki/Protein_isoform) of a protein, you can select that by adding '::' after the gene name followed by the name of the isoform in Ensembl e.g. ```ENAM::ENAM-202```. If you want to get all possible isoforms follow the same strategy but add the word "ALL" e.g. ```ENAM:ALL```.

b) 1 txt file, named ```Organism.txt``` with the scientific names of the species we are interested in. For this version of the pipeline you can only select from species present in the [Ensembl database](https://www.ensembl.org/info/about/species.html). The species name should be without capital letters and with underscores instead of spaces e.g. ```homo_sapiens```. Once again only one species per line should be provided. Additionally if you want to use a specific reference version/assembly of a species, you can do that. Simply add a tab or a space after the species name and then write the assembly version e.g. ```homo_sapiens GRCh37```. If no specific assembly is provided the latest version of Ensembl will be used. Be aware of the proper name of each assembly as it needs to match perfectly with what Ensembl has in its database (e.g. "GRch37" would not work). You can look some of the assembly names [here](https://www.ensembl.org/info/website/archives/assembly.html). The safest way to find an valid name of an assembly is to look for it in the webpage of a gene: 

![alt text](https://github.com/johnpatramanis/Proteomic_Pipeline/blob/main/GitHub_Tutorial/Images/Assembly_Loc.PNG?raw=true)

<br/><br/> 

For this tutorial both of the above files are already prepared and ready to use. You can copy them over from their folder using:

```bash
cp ../GitHub_Tutorial/Organism_Refs.txt ./Organism.txt
cp ../GitHub_Tutorial/Proteins.txt ./Proteins.txt
```

You can also take a look at them using:


```bash
less Proteins.txt
less Organism.txt
```

As you can see the proteins we will be using are all enamel-related and the organisms are hominids or closely related primates. This is of course on purpose since we are analyzing the enamel proteins of extinct hominids. You may want to edit these 2 files and add some proteins or some species using [nano](https://help.ubuntu.com/community/Nano), or any other linux text editor:
If you have never used nano you can [click here for some help with the commands for it](https://www.nano-editor.org/dist/latest/cheatsheet.html)

```bash
nano Proteins.txt
nano Organism.txt
```

This is of course optional and you can also just leave these files as they are and move one.

<br/><br/> 

### Run the first module

If everything looks fine, it's now time to execute the pipeline by simply typing:

```bash
snakemake -j4 --resources FTP=7
```

Depending on the computing power of your computer, you can increase the number of cores being used, by typing -j8 or  -j16 if you want to utilize 8 or 16 cores instead of 4. 
FTP is a unique 'resource' for this module that makes sure you are not making too many requests-per-second from Ensembl. If you do, Ensembl might shut you out for a few moments, leading to the script crashing. I highly suggest not using anything more than FTP=7 (you can use less , it might make things slightly slower)

<br/><br/> 

### Check the output the first module and deactivate environment

Once the pipeline finishes running you can check the results by diving into the ```Workspace``` folder. There are many output files that we will use later on, but the most important ones for now are located in:
```Workspace/3_FASTA_Seqs/All_Sequences.fa```
where all your proteins for all your species are stored.
Different subsets of this fasta file can be found here: 

```/Dataset_Initialization/Workspace/3_FASTA_Seqs/Combined_Per_Species/```
```/Dataset_Initialization/Workspace/3_FASTA_Seqs/Combined_Per_Protein/```

Feel free to navigate into those folders and look at the files that have been created inside ```/Dataset_Initialization/Workspace/```
Come back to the main folder directory ```/Dataset_Initialization/``` once you are finished.
<br/><br/> 

Now save this simple reference dataset we have created, using the shell commands:

```bash
cp ./Workspace/3_FASTA_Seqs/All_Sequences.fa Reference_Proteomes.fa
```  
We can now also deactivate Module's 1 environment, since we are done here and moving on to Module 2 and leave the folder.

```bash
conda deactivate
cd ..
```

<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>





















## STEP 2 - Reference Dataset Enrichment / Protein translation (3+ hours, depending on the speed of the connection. This is due to the size of the genetic data used in the examples.)

<br/><br/> 

### Activate the second module

We now have the ‘scaffold’ of our reference dataset ready and if we wanted to, we could move straight on to STEP 3 and generate a tree from it. However the purpose of this tutorial is to also go through STEP 2 and ‘enhance’ our scaffold dataset with protein data translated from available genomic data. To do this we can use the PaleoProPhyler's 2nd Module. Unfortunately this requires downloading some large genomic-data files. First the modern human BAM files are around 15 Gb each. You can try downloading between 1-4 of them. Then, both the Neanderthal and the Denisovan genome (VVCF files) we will download to use, are high coverage (>30x) and thus multiple Gigabits in size. These 2 also require a few edits before they are usable. Finally there are some other modern human VCF files which we can also use in this tutorial. The tutorial will guide you through this process for all of these files but you can choose to only download some of them. If you are _not_ interested in the translation part of the pipelines, please move to module number 3. If translating genomes is your main interest, please follow the steps below to understand the process for each data format.

First, activate the module by typing:

```bash
conda activate Translator
```

and move into the right folder:

```bash
cd ./Dataset_Construction/
```


<br/><br/> 

Now we need to download some data to translate. For this example we will build a subset of the reference dataset presented in the [publication of PaleoProPhyler](https://www.biorxiv.org/content/10.1101/2022.12.12.519721v1). We can use any of the following datasets:

https://pubmed.ncbi.nlm.nih.gov/36055201/

https://pubmed.ncbi.nlm.nih.gov/28982794/

https://www.sciencedirect.com/science/article/pii/S0960982217312459?via%3Dihub 


WARNING: The following few steps download a couple of large files. The minimum disk space that will be required is 200+ GB
If you have the disk space, proceed as below. If not, you can download only **some** of the files or simply move straight to Module 3.

<br/><br/> 

### Download modern genetic data to translate (1000 Genomes Dataset - BAM/CRAM files)

For this simple example, we will download 4 modern human individuals from the 1000 genomes project. The links for the samples are located in ```GitHub_Tutorial\1KG_Samples.txt ```
and you can download them using this loop:

```bash
FILE="../GitHub_Tutorial/1KG_Samples.txt";
LINES=$(cat $FILE);
for SAMPLE in $LINES
do
       wget --continue --progress=dot:mega --tries=0 "$SAMPLE";
done
mv *.cram Workspace/1_OG_BAM_FILES/
```
If you don't want to download all of them, you can remove some of the links from the ```GitHub_Tutorial/1KG_Samples.txt ``` file and then run the above command block. Each line of the '/GitHub_Tutorial/1KG_Samples.txt' file should correspond to one sample. I would suggest trying this tutorial with at least one sample, so removing every line from that file besides the first one. 

Note: Some servers block access to users downloading files using ftp. This will manifest in the above loop attempting to connect but without success. In these cases you should contact the person responsible for your server. Remember that you need to download genetic data in order to do the translations, but you can always instead move to module 3.

<br/><br/> 

### Bonus Step
### Download and preprocess ancient genetic data to translate (VCF files) 

<br/><br/> 

If you want to explore the ability to translate VCF files or are interested in using archaic humans in you dataset, we can additionally download some of the available high coverage archaic human samples. By default I would always suggest using VCF files for ancient DNA samples. Ancient DNA samples tend to contain multiple sequencing errors, but their VCF files have been more carefully curated and called by the researchers who published then, who specialize in this kind of work. The process of downloading and preparing the following VCF files will take some time so feel free to find an alternative VCF file to use (e.g. scroll down a bit to find modern VCF files). Always make sure your VCF file is in a format that is readable with bcftools (```bcftools head VCF_FILE ```), otherwise the pipeline won't be able to precess it!

We can download and format the VCF files for 1 Neanderthal and 1 Denisovan as an example, using the commands that follow.

<br/><br/> 
<br/><br/> 
## Download and preprocess Neanderthal Genetic Data (high quality VCF files - multiple hours to download and preprocess the first time) 

<br/><br/> 

Download the data:
```bash
cd Workspace/0_VCF_FILES/
### Download step
wget -r -np -nH --cut-dirs=3 -R index.html http://cdna.eva.mpg.de/neandertal/altai/AltaiNeandertal/VCF/;    ###( 70 Gigabytes )

```

Check that the files are are in there and go back to the main repository

```bash
ls VCF/
cd ../..
```


In addition to that, translating from a VCF file requires a reference genome which the VCF was created from. VCF files only contain 'variant' positions, so for any non variant position we have no idea what base was there. This is where the reference genomes (fasta file) comes in and fills in the gaps. This file MUST be a file ending with '.fa' and placed inside the appropriate folder named '/Reference/'. You can download the GrCh37 (also known as hg19) reference using:

```bash
wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.fa.gz -P ./Reference/
gunzip ./Reference/hg19.fa.gz
```

<br/><br/> 

The pipeline requires 1 VCF file per sample, where the VCF file should contain genome-wide variation or at least the information for all the locations where the genes of interest are. Unfortunately the VCF files from the Leipzig repository are a bit difficult to work with and need some preprocessing. We will have to index them and then merge them together ourselves. Finally these 2 genomes (Neanderthal and Denisovan) were mapped onto GrCh37, which is an older version of the human reference genome. However if you followed the steps of module 1, you should have also downloaded the files for that reference and don't need to do anything else.

The files are large, so this process will take a while. You can increase the number of threads wherever possible to make the process faster, if your computer has that capability of course. Alternatively you can use a different modern VCF file that is 'ready to go'. (Scroll down)

```bash
#### For Neanderthal

cd Workspace/0_VCF_FILES/VCF/
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y MT nonchrom; do bcftools index -f AltaiNea.hg19_1000g.$i.mod.vcf.gz --threads 4; done
ls AltaiNea.hg19_1000g.*.mod.vcf.gz > Altai.txt
bcftools concat -f Altai.txt -Oz -o Altai.vcf.gz --threads 4
cd ..
mv VCF/Altai.vcf.gz ./
```



Now lets check that the sample works:

```bash
#### Check that it worked
bcftools head  Altai.vcf.gz

#### If the above prints something, it worked, remove original vcf files
rm -rf VCF

#### Go back to main directory
clear
cd ../..
```












<br/><br/>
<br/><br/> 

## Download and preprocess Denisovan Genetic Data (high quality VCF files - multiple hours to download and preprocess the first time)

<br/><br/> 

Download the data:
```bash
cd Workspace/0_VCF_FILES/
### Download step
wget -r -np -nH --cut-dirs=3 -R index.html http://cdna.eva.mpg.de/denisova/VCF/hg19_1000g/;  ####(54 Gigabytes )

```

Check that the files are are in there and go back to the main repository

```bash

ls T_hg19_1000g.*.mod.vcf.gz
cd ../..

```


In addition to that, translating from a VCF file requires a reference genome which the VCF was created from. VCF files only contain 'variant' positions, so for any non variant position we have no idea what base was there. This is where the reference genomes (fasta file) comes in and fills in the gaps. This file MUST be a file ending with '.fa' and placed inside the appropriate folder named '/Reference/'. If you have already done this for the Neanderthal sample you can ignore this step. You can download the GrCh37 (also known as hg19) reference using:

```bash
wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.fa.gz -P ./Reference/
gunzip ./Reference/hg19.fa.gz
```

<br/><br/> 
<br/><br/> 

The pipeline requires 1 VCF file per sample, where the VCF file should contain genome-wide variation or at least the information for all the locations where the genes of interest are. Unfortunately the VCF files from the Leipzig repository are a bit difficult to work with and need some preprocessing. We will have to index them and then merge them together ourselves. Finally these 2 genomes were mapped onto GrCh37, which is an older version of the human reference genome. However if you followed the steps of module 1, you should have also downloaded the files for that reference.

The files are large, so this process will take a while. You can increase the number of threads wherever possible to make the process faster, if your computer has that capability of course. Alternatively you can use a different modern VCF file that is 'ready to go'. (Scroll down)

```bash
##### For Denisovan
cd Workspace/0_VCF_FILES/
ls T_hg19_1000g.*.mod.vcf.gz > Denisovan.txt
bcftools concat -f Denisovan.txt -Oz -o Denisovan.vcf.gz --threads 4

```



Now lets check that the sample works:

```bash
#### Check that it worked
bcftools head  Denisovan.vcf.gz

#### If the above prints something, it worked, remove original vcf files
rm -rf T_hg19_1000g.*.mod.vcf.gz*


#### Go back to main directory
clear
cd ../..
```


<br/><br/> 

### Bonus Step
### Download and preprocess modern humans (SGDP dataset - VCF files with a large number of individuals) 

<br/><br/> 

Instead of (or in addition to) downloading and processing the Neanderthal & Denisovan VCF files we can use some modern data instead.
Below we will download the SGDP data, mapped onto GrCh37. All they need is to be merged into one VCF file. The size of the total VCFs is still quite large (~ 67 GB) so this will still take some time. The benefit however is that there are hundreds of samples in this VCF. In the interest of time however we will only use a handful of them  this tutorial.

```bash
cd Workspace/0_VCF_FILES/

wget -r -np -nH --cut-dirs=3 -R index.html https://sharehost.hms.harvard.edu/genetics/reich_lab/sgdp/phased_data2021/;
cd phased_data2021/
ls chr.sgdp.pub.*.bcf > SGDP.txt
bcftools concat -f SGDP.txt -o SGDP.vcf.gz -Oz
cd ..
mv phased_data2021/SGDP.vcf.gz ./
rm -rf phased_data2021

cd ../../
```

This is an alternative example on how to translate from a VCF file. The data here is from modern humans and require less preprocessing than the Leipzig VCF files.
The data are mapped on to GrCh37, so we still need to download that reference:
(If you run this step for the Neanderthal/Denisovan example, you don't need to repeat it)
```bash
wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.fa.gz -P ./Reference/
gunzip ./Reference/hg19.fa.gz
```






<br/><br/>
#### Prepare input for BAM/CRAM file translation

Now that we have downloaded our datasets we are ready to set up the translation. The translation of a genome requires a number of resources specific to the reference assembly that the genome was mapped on to. Considering the data we downloaded correspond to different reference genomes (1000 genomes of modern humans are mapped onto GrCh38 and the SGDP and archaic humans are mapped onto GrCh37), we have to run the pipeline at least 2 times separately for each reference.

As we just mentioned, translation requires a couple of resources. First we need the location (chromosome/scaffold, position & strand) of the gene that produces the protein. Most genes require splicing, so we also need the exon and intron information. Finally, a reference amino acid sequence of the protein is also necessary. This sounds like a lot, but given that we have run Pipeline 1 for the proteins of interest and the organisms and reference versions of interest (Homo sapiens GRCh37 & GRCh38), all of this data has already been downloaded and is available to us!

In this first example we will deal with the BAM files of the 1000 genomes of modern humans, which are mapped onto the  GrCh38 reference.
First we need a txt file named ```Organism.txt```, where the organism and reference version for the translation are given. For GRCh38 one is already in place and we can take a look at it with

```bash
less Organism.txt
```

Then we need a list of the samples we want to translate, in the form of a txt file named ‘Samples.txt’. Since all of them are CRAM files inside the folder ```Dataset_Construction/Workspace/1_OG_BAM_FILES/``` we can use:

```bash
ls Dataset_Construction/Workspace/1_OG_BAM_FILES/*.cram | cut -d '.'  -f 1 > Samples.txt
```
Note: if you never downloaded the 1000 genomes cram files, the above command will not work.


Notice that for the list the file extension should not be mentioned, just the name of the bam file.
We can take a look at how the file looks with:

```bash
less Samples.txt
```


<br/><br/> 

### Run the second module (Translation)

With these two files set up, we don’t need anything else. Which proteins are being translated though? If we have successfully run Pipeline 1 for the proteins of interest, then Pipeline 2 will translate those proteins. You can test-run the pipeline to see if everything is set up with:

```bash
snakemake -n -r -j4
```

You can also take a look at which proteins are being translated by looking into the file 'Gene_locs.txt'. This file also contains the information on the location of the gene that codes the proteins. Take a look into the file by typing:

```bash
less Gene_locs.txt
```



All we need to do now, is execute the pipeline:

```bash
snakemake -j4
```

This will take some time! Again, in the example above we use 4 cores, but if your computer is more powerful, you can try increasing the number of cores (e.g. -j32 ) to increase efficiency and decrease waiting time. Once this dataset finishes, we can take a look at the results by:



```bash
less Workspace/9_FINAL_OUTPUT/ALL_PROT_REFERENCE.fa
```

and we can store the result somewhere as

```bash
cp Workspace/9_FINAL_OUTPUT/ALL_PROT_REFERENCE.fa Modern_Humans_from_BAM.fa
```

<br/><br/> 
<br/><br/> 
<br/><br/> 
### Bonus step
### Alternative datasets translation

Alternatively if you downloaded the archaic genomes or the SGDP modern humans, you would want to use the GRCh37 reference genome, since all this data were generated using that reference. In order to translate them, first we need to switch our reference genome by editing the ```Organism.txt``` file

```bash
echo homo_sapiens    GRCh37 > Organism.txt
```
Then, let's empty the Samples.txt from the samples that are already finished:

```bash
rm Samples.txt
```

Finally, since our data are now VCF files instead of CRAM or BAM files, we need a slightly different method of translating them. 
Earlier we have downloaded the VCF files and placed them into ```Workspace/0_VCF_FILES/```
Now we need to specify which samples we want to translate, which VCF file contains those samples and which reference fasta to use for their translation.
For our example the input file is pre-made. You can copy it over using:

```bash
cp ../GitHub_Tutorial/VCF_Samples.txt VCF_Samples.txt
```

The samples that you want to translate must be in a file named 'VCF_Samples.txt'. If we take a look at this new VCF_Samples.txt file, we can see the format required for the samples: A file with 3 separated columns, one with the name of the sample inside the vcf, one with the name of the vcf file and one with the reference fasta file that corresponds to the sample:

Sample_Name VCF_File_Name Reference_File_Name

The columns are separated by a tab and all the files must be in their proper folder, VCF inside 'Workspace/0_VCF_FILES/' and the reference fasta inside 'Reference'

Take a look at the file to see:
```bash
less VCF_Samples.txt 
```
In the case that you only downloaded and set up some of these samples (either Neanderthal, Denisovan or modern humans) simply keep the samples you want to translate and remove all others.

We are now set for the new translation and we can execute it again, by typing:

```bash
snakemake -j4
```
Again remember you can increase the number of cores (-j4) to make it faster.

Finally when this is done you can check for the results in Workspace/9_FINAL_OUTPUT. If everything looks alright, copy over the resulting fasta files using:

```bash
cat Workspace/9_FINAL_OUTPUT/ALL_PROT_REFERENCE.fa >> Translated.fa
```

<br/><br/> 
### Prepare input for (modern) VCF file translation and run translation

Finally let's translate the SGDP-modern humans dataset. This dataset consists of multiple modern individuals (~300 individuals) mapped onto GRCh37. In order to translate them, first we need to switch our reference genome by editing the ```Organism.txt``` file.
(If you just did this step for the Neaderthal/Denisovan samples you don't need to do it again, go stragiht to the copying VCF_Samples.txt step.)

```bash
echo ‘Homo_sapiens	GRCh37’ > Organism.txt
```
Then, let's empty the Samples.txt from the samples that are already finished:

```bash
rm Samples.txt
```

Finally, since our data are now VCF files, we need a slightly different method of translating them. 
Earlier we have downloaded the VCF files and placed them into ```Workspace/0_VCF_FILES/```
Now we need to specify which samples we want to translate, which VCF file contains those samples and which reference fasta to use for their translation.
For our example the input file is pre-made. You can copy it over using:

```bash
cp GitHub_Tutorial/VCF_Samples_Modern.txt VCF_Samples.txt
```

The samples that you want to translate must be in a file named 'VCF_Samples.txt'.If we take a look at this new VCF_Samples.txt file, we can see the format required for the samples: A file with 3 separated columns, one with the name of the sample inside the vcf, one with the name of the vcf file and one with the reference fasta file that corresponds to the sample:

Sample_Name VCF_File_Name Reference_File_Name

The columns are seperated by a tab and all the files must be in their proper folder, VCF inside 'Workspace/0_VCF_FILES/' and the reference fasta inside 'Reference'

Take a look at the file to see:
```bash
less VCF_Samples.txt 
```


We are now set for the new translation and we can execute it again, by typing:

```bash
snakemake -j4
```
Again remember you can increase the number of cores (-j4) to make it faster.

<br/><br/>
### Merge Ancient proteins, 'scaffold' produced by module 1 and translated data produced by module 2


And once this is also finished, we can combine the resulting translations into one dataset, along with the *H.antecessor* and exit the pipeline folder and environment.

```bash
cat Workspace/9_FINAL_OUTPUT/ALL_PROT_REFERENCE.fa >> Translated.fa
cat Modern_Humans_from_BAM.fa >> Translated.fa
conda deactivate
cd ..
```   
   
   
   
   
   
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>


























## STEP 3 - Phylogenetic Analysis

We now have the paleo-proteomic data ( ```H_antecessor.fa``` & ```Gigantopethicus.fa```) , the reference proteomes from STEP 1 (```Reference_Proteomes.fa```) and the translated sequences from STEP 2( ```Translated.fa``` ), which we can all merge together into the dataset which we want to run a phylogenetic analysis on. If you didn't complete one of the relevant steps, just ignore the command that adds that dataset (e.g. if you didn't run STEP 2, don't run cat Dataset_Construction/Translated.fa >> Reference_Data.fa).

```bash
cat H_antecessor.fa >>  Reference_Data.fa
cat Gigantopethicus.fa >>  Reference_Data.fa
cat Dataset_Initialization/Reference_Proteomes.fa  >> Reference_Data.fa
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
echo Dataset   Ancient_Samples > Datasets.txt
echo Reference_Data.fa   Atapuerca_H_antecessor >> Datasets.txt
``

Now all we have to do is run the pipeline and wait.

```bash
snakemake -j4
```
Once this finishes running you will have a generated tree for each of your proteins individually, as well as one Maximum Likelihood and one Bayesian species from the concatenation of these proteins. The full output of the analysis is located within Dataset_Analysis/Workspace/1_OG_Dataset/2_DATASETS/ in a folder with the name of the name of the original fasta dataset, which in our case is 'Reference_Data'.

Inside this folder are located multiple subfolders. Most of these subfolders will have the name and correspond to a single protein used in your analysis (e.g. 'ENAM', 'AMELX'). Inside each one of those folders are a couple of fasta alignment files and the resulting files from a maximum likelihood tree generation. The most important files here are: 

a) 'Protein-Name'_aln_e.fa which contains the final alignment of you data for this protein.

b) 'Protein-Name'_aln_e.phy_phyml_tree.txt which is the phylogenetic tree of this protein in newick format.

Both fasta alignment files and newick trees can be transported and vissualised on your personal computer using some external tools. For fasta files I like to use [Jalview](https://www.jalview.org/) and for newick trees [Figtree](http://tree.bio.ed.ac.uk/software/figtree/). Any viewing tool will do however and there are indeed multiple to choose from!

Most importantly, there is also a single folder named 'CONCATINATED'. This folder contains the results of the concatenation of all the available proteins and the trees generated using that concatenation. All files starting with the name 'CONCATINATED_aln_e.phy' are a result of the maximum likelihood analysis and all files starting with 'CONCATINATED_o.nex' are a result of the Bayesian analysis. Again **the most important files** in the folder are:

a) CONCATINATED_o.fa , which contains the final alignment of you data for all the concatenated proteins.

b) CONCATINATED_o.nex.con.tre and CONCATINATED_aln_e.phy_phyml_tree.txt , which contain the resulting newick tree from the Bayesian and maximum likelihood anaysis accordingly.

And once again, you can transport those files to your personal computer and vissualise them using the tool of your choice. For the phylogenetic trees, make sure you also plot the bootstraps or posterior probabilities so you can understand how much support your phylogeny has. Finally, keep in mind that given the low number of genetic loci (proteins) we are using in palaeoproteomics, all trees we create may not accurately depict the full genetic history of a species.

<br/><br/>
<br/><br/>

### OPTIONAL - MASKING MODERN SAMPLES AS ANCIENT
The user has the further optional ability to 'mask' some of the modern samples with the missingness of one of the ancient samples. Modern sample that has been masked with the missingness of an ancient sample will either still be placed in its original clade or be shifted somewhere else, because of the missing data. This may help the user determine the amount of phylogenetic information their ancient samples contain and the effect of the missingness on their phylogenetic palcement. To use the masking option add a simple txt file named 'MASKED' inside the main /Dataset_Analysis/ folder. This file should contain 2 columns seperated by a tab, one with the name of the modern sample you want to mask and one with the name of the ancient sample which you want to copy its missingness.



<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>

## Glossary

| Term  | Description |
| ------------- | ------------- |
| [BAM](https://en.wikipedia.org/wiki/Binary_Alignment_Map) | File format. Contains DNA reads that have been aligned onto a reference genome. As the name suggests, its content are in a binary language and thus cannot be read by a human. You can use tools such as bcftools to read, extract or edit its content. |
| [Conda](https://docs.conda.io/en/latest/)  | "Package, dependency and environment management for any language". Conda is a tool that can install other tools. It's most prominent feature is the ability to detect 'conflicts' between the tools you want to install and other existing software in the computer. |
| [CRAM](https://en.wikipedia.org/wiki/CRAM_(file_format))  | File format. Its a more compressed version of a BAM file. Works almost the same way.  |
| [FASTA](https://en.wikipedia.org/wiki/FASTA_format)  | File format that describe one or more sequences of proteins or DNA (or eny other data that uses a sequence of letters). Easy to read and edit, can be opened with any txt editing tool such as the humble Windows notepad but also with some specific tools like [Jalview](https://www.jalview.org/) which can provide you with a much nicer way to vissualise the sequences. |
| [Mamba](https://github.com/mamba-org/mamba) | An upgrade to Conda (requires Conda). More capable and faster at detecting system conflicts. |
| [Nano](https://en.wikipedia.org/wiki/GNU_nano) | A basic Linux tool to edit text files. It's a bit tricky to use at first but suitable for small edits into the text of files in Linux. |
| [Reference Genome](https://en.wikipedia.org/wiki/Reference_genome)  | The whole genome of a specific organism. Reference genomes are usefull as a model everyone can point to to describe the genome of an organism. They usually don't have any biological meaning behind them (e.g. it's not the most ancestral genome of a species) and usually correspond to the first individual that was sequenced in high coverage from a species (Human genomes are an exception to this). When genetic variation is described, it's usually against a certain reference genome.|
| [Reference Proteome](https://en.wikipedia.org/wiki/Proteome) | Similarly to the Reference Genome above, a reference proteome are the sequences of the proteins of an organism that serve as a model for said organism. This term is not used so much, but it describes this section of [Uniprot's Reference Proteomes](https://www.uniprot.org/proteomes/?query=*)|
| [Shell](https://en.wikipedia.org/wiki/Shell_(computing))  | The 'black box' informatics people have open all the time in front of them. Its a tool that uses a basic language to comunicate with your computer. Can do basic things such as moving between directories to more advanced things like searching for patterns inside a document.|
| [TXT](https://en.wikipedia.org/wiki/Text_file) | One of the most commonly used filetypes. It contains information in the format of letters of text. Can be opened by multiple software including Notepad or Word. |
|[VCF](https://en.wikipedia.org/wiki/Variant_Call_Format) | File format that contains genetic data. VCFs are produced (usually from BAM files) by comparing a genome to a _reference genome_ to identify locations on the genome where the two differ. These sites are known as _variant_ sites. The VCF files usually only contain information on variant sites (any site that is the same as the reference genome is omitted). They can contain information from one to hundreds of individuals. VCF files can be opened by txt reading software but are more easily handeld by specialised tools such as 'vcftools'. |
|[VCF.GZ](https://www.biostars.org/p/59492/) | Exactly the same as a VCF file but more compact packaging. Can only be opened by specific tools like 'vcftools'. |


<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>

## Reporting Issues
Errors, issues and suggestions can be reported either directly to my current work email : ioannis.patramanis@sund.ku.dk , or more preferably through this github repository's issue page [here](https://github.com/johnpatramanis/Proteomic_Pipeline/issues).

When reporting errors, please include the following information:

a) On which module does the error occur?

b) Was the installation of the module successful?

c) Are there any output file generated?

d) Can you please provide a screenshot or a copy of the error message, if there is any.

<br/><br/>
<br/><br/>

## Keeping up to date

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
This should take care of the code itself. If you need to update the conda environments ( e.g. the software used by the pipeline) as well, you can enter the main directory with the 3 subfolders and update each of the environments:

```bash
conda env update --name Analyser --file Dataset_Analysis/Analyser.yml --prune
conda env update --name Initiator --file Dataset_Initialization/Initiator.yml --prune
conda env update --name Translator --file Dataset_Construction/Translator.yml --prune
```

