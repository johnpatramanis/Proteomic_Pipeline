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

   
   
**Step 5) Prepare your Data for translation**

If everything worked until now, then we are almost set! Now we just need to get some DNA data to translate them over to proteins. If you are using a species that is already aligned to the Human genome (ch37) then all you need to do is place your bam files in the '/Dataset_Construction/Workspace/OG_BAM_FILES' folder and then in the '/Dataset_Construction/' folder edit the 'samples.txt' file to contain each sample name per line. If your bam file is named SAMPLE.bam then simply write the name SAMPLE in the sample.txt file. 

If you don't have any bam files at hand or simply want to test if the pipeline works, you can type ``` bash 0_Download_Bam_files.sh``` and some bam files will be downloaded and placed in the right folder. The samples.txt file also by default corresponds to these samples.




If your bam files are aligned to a different species or reference genome, then things will get more complicated as other files need to be re-adjusted. if you want to target different proteins than the enamel presets, then you also need to make some adjustments. These are described in step number **.


**Step 6) Execute the translation**

With your sample files set up, all you need to do now is initiate the process.
Type ```snakemake -j1 ``` to begin.
If everything works out, you should get your resulting proteins in the 'Dataset_Construction/Workspace/FINAL_OUTPUT' folder.
   
   
**Step 7) Adjusting for different target proteins**

**Step 8) Adjusting for different reference genome**
   
   
   
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
   
**Development To Do list: (Dataset Construction)** - By Yiannis , for Yiannis
   1) Dependencies and software: Get slim list of conda env - > split it up to sub env? - Rscript and R?
   3) Alternative path to FASTA files for pre split bam files
   4) Make 'FRMT' files temporary?
   5) Pre bam file input?
   6) Different use for ancient / modern samples
