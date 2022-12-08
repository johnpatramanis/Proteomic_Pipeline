---
title: "PaleoProPhyler: a reproducible pipeline for phylogenetic inference using ancient proteins"
tags:
  - Palaeoproteomics
  - Phylogeny
  - Python
  - R
  - Phyloproteomics
authors:
  - name: Ioannis Patramanis
    affiliation: 1
  - name: Jazmin Ramos Madrigal
    affiliation: 2
  - name: Enrico Cappellini
    affiliation: 3
  - name: Fernando Racimo
    affiliation: 1 , 4

affiliations:
  - name: Section for Molecular Ecology and Evolution, Globe Institute, University of Copenhagen
    index: 1
  - name: Center for Evolutionary Hologenomics, Globe Institute, University of Copenhagen
    index: 2
  - name: Centre for GeoGenetics , Globe Institute, University of Copenhagen
    index: 3
  - name: Lundbeck GeoGenetics Centre, Globe Institute, University of Copenhagen
    index: 4
date: 2022-12-06
bibliography: references.bib 
---
# Summary

Ancient proteins from fossilized or semi-fossilized remains can yield
phylogenetic information at broad temporal horizons, in some cases even
millions of years into the past. In recent years, peptides extracted
from archaic hominins and long-extinct mega-fauna have enabled
unprecedented insights into their evolutionary
history[@welker2017middle; @cappellini2019early; @chen2019late; @welker2019enamel; @buckley2019collagen; @welker2020dental].
In contrast to the field of ancient DNA - where several computational
methods exist to process and analyze sequencing data - few tools exist
for handling ancient protein sequence data. Instead, most studies rely
on loosely combined custom scripts, which makes it difficult to
reproduce results or share methodologies across research groups. Here,
we present PaleoProPhyler: a new fully reproducible pipeline for
aligning ancient peptide data and subsequently performing phylogenetic
analyses. The pipeline can not only process various forms of proteomic
data, but also easily harness genetic data in different formats (CRAM,
BAM, VCF) and translate it, allowing the user to create reference panels
for phyloproteomic analyses. We describe the various steps of the
pipeline and its many functionalities, and provide some examples of how
to use it. PaleoProPhyler allows researchers with little bioinformatics
experience to efficiently analyze palaeoproteomic sequences, so as to
derive insights from this valuable source of evolutionary data.

# Statement of Need

Recent advances in protein extraction and mass spectrometry
[@ruther2022spin; @lanigan2020multi; @porto2011new] have made it
possible to isolate ancient peptides from organisms that lived thousands
or even millions of years ago. Certain ancient proteins have a lower
degradation rate and can be preserved for longer than ancient DNA
[@cappellini2014unlocking; @demarchi2016protein; @hendy2021ancient; @warinner2022_paleoproteomics].
The sequences of these proteins contain evolutionary information and
thus have the potential to resolve important scientific questions about
the deep past, which are not approachable via other methods. Tooth
enamel proteins in particular have been successfully extracted from
multiple extinct species, in order to resolve their relationships to
other species
[@welker2017middle; @cappellini2019early; @welker2019enamel; @welker2020dental; @buckley2015ancient; @buckley2019collagen].

Ancient proteomic studies typically use combinations of custom scripts
and repurposed software, which require extensive in-house knowledge and
phylogenetic expertise, and are not easily reproducible. Barriers to
newcomers in the field include difficulties in properly aligning the
fractured peptides with present-day sequences, translating available
genomic data for comparison, and porting proteomic data into standard
phylogenetic packages. The creation of automated pipelines like PALEOMIX
[@schubert2014characterization] and EAGER [@peltzer2016eager] have
facilitated the streamlining and reproducibility of ancient DNA
analyses, which has been particularly helpful for emerging research
groups around the world. This has undoubtedly contributed to the growth
of the field [@lan2018technical]. Yet, the field of palaeoproteomics
still lacks a "democratizing" tool that is approachable to researchers
of different backgrounds and expertises.

Another important issue in phyloproteomics is the relative scarcity of
proteomic datasets [@muller2020proteome; @brandt2022palaeoproteomics].
There are currently tens of thousands of publicly available whole genome
sequences, covering hundreds of species
[@lewin2018earth; @byrskahigh; @prado2013great; @zhang2014comparative; @koepfli2015genome].
The amount of publicly available proteome sequences is much smaller in
comparison. For most vertebrate species, lab-generated protein data does
not even exist and phyloproteomic research is reliant on sequences
translated *in silico* from genomic data. These, more often than not,
are not sufficiently validated or curated [@bagheri2020detecting]. As a
result, assembling a proper reference dataset for phyloproteomics can be
challenging. Given how important rigorous taxon sampling is in
performing proper phylogenetic reconstruction
[@rosenberg2003taxon; @heath2008taxon], having a complete and reliable
reference dataset is crucial. In the case of proteins, the typically
short sequence length and the low amounts of sequence diversity - due to
the strong influence of purifying selection - means that absence of
knowledge about even a single amino acid polymorphism (SAP) can strongly
affect downstream inferences
[@chen2019late; @opperdoes2003phylogenetic; @presslee2019data; @demarchi2022ancient].

To address all of the above issues, we present "PaleoProPhyler": a fully
reproducible and easily deployable pipeline for assisting researchers in
phyloproteomic analyses of ancient peptides. "PaleoProPhyler" is based
on the workflows developed in earlier ancient protein studies
[@cappellini2019early; @welker2019enamel; @welker2020dental], with some
additional functionalities. It allows for the search and access of
available reference proteomes, bulk translation of CRAM, BAM or VCF
files into amino acid seuqences in FASTA format, and various forms of
phylogenetic tree reconstruction.


![Overview of the pipeline\label{fig:Overview}](graphics/PaleoProPhyler_Overview_Fig.png)

# Description of the Pipeline

To maximize reproducibility, accessibility and scalability, we have
built our pipeline using Snakemake [@molder2021sustainable] and Conda
[@anaconda]. The Snakemake format provides the workflow with tools for
automation and computational optimization, while Conda enables the
pipeline to operate on different platforms, granting it ease of access
and portability. The pipeline is divided into three distinct but
interacting modules (Modules 1,2 and 3), each of which is composed of a
Snakemake script and a Conda environment
\autoref{fig:Overview}. The modules are intended to synergize with
each other, but can also be used independently. An in-depth explanation
of each step of each module, as well as the code being run in the
background, is provided on the software's Github page as well as in the
supplementary material.

# Application

As proof of principle, we deploy this pipeline in the reconstruction of
ancient hominid history using the publicly available enamel proteomes of
*Homo antecessor* and *Gigantopithecus blacki*, in combination with
translated genomes from hundreds of present-day and ancient hominid
samples. In the process, we have generated the most complete and up to
date, molecular hominid phyloproteomic tree
\autoref{fig:PhyloTree}. The
process of generating the reference dataset and its phyloproteomic tree
using PaleoProPhyler is covered in detail in the step-by-step [Github
Tutorial](https://github.com/johnpatramanis/Proteomic_Pipeline/blob/main/GitHub_Tutorial/Tutorial.md).
The dataset used as input for the creation of the phylogenetic tree is
available at [Zenodo'](https://zenodo.org/record/7404802#.Y48vOHbMKbg)

![Phyloproteomic tree generated using PaleoProPhyler's Module 3. The
tree was constructed using 9 protein sequences obtained from enamel and
includes more than 100 hominid individuals translated from genomic data,
two individuals from published palaeoproteomic datasets as well as
sequence data from a *Macaca* and a *Hylobates* individual, which are
used to root the tree.\label{fig:PhyloTree}](graphics/tree-plot.png){ width=45% }

# Protein Reference Dataset

In order to facilitate future analyses of ancient protein data, we also
generated a publicly-available palaeoproteomic hominid reference
dataset, using Modules 1 and 2. We translated 204 publicly available
whole genomes from all 4 extant Hominid genera
[@byrskahigh; @prado2013great; @nater2017morphometric]. Details on the
preparation of the translated samples can be found in the supplementary
materials. We also translated multiple ancient genomes from VCF files,
including those of several Neanderthals and one Denisovan
[@prufer2017high; @mafessoni2020high]. Since the dataset is tailored for
palaeoproteomic tree sequence reconstruction, we chose to translate
proteins that have previously been reported as present in either teeth
or bone tissue. We compiled a list of 1696 proteins from previous
studies
[@castiblanco2015identification; @alves2011unraveling; @acil2005detection; @salmon2016global; @jagr2012comprehensive; @park2009proteomics]
and successfully translated 1,543 of them. For each protein, we
translated the canonical isoform as well as all alternative isoforms,
leading to a total of 10,058 protein sequences for each individual in
the dataset. Details on the creation of the protein list can be found in
the supplementary materials. The palaeoproteomic hominid reference
dataset is publicly available online at [Zenodo, under the name 'Hominid
Palaeoproteomic Reference
Dataset'](https://zenodo.org/record/7404802#.Y48vOHbMKbg)

# Availability and Community Guidelines

PaleoProPhyler is publicly available on
[github](https://github.com/johnpatramanis/Proteomic_Pipeline): The
software requires the prior installation of Conda. The github repository
contains a tutorial for using the workflow presented here, with the
proteins recovered from the *Homo antecessor* and *Gigantopithecus
blacki* as examples. We welcome code contributions, feature requests,
and bug reports via Github. The software is released under a CC-BY
license.

# Author Contributions

-   **Ioannis Patramanis**: Conceptualization, manuscript writing, code
    writing for the Snakemake scripts, compilation of the Conda
    environments and application of the pipelines to produce the results
    described in the 'Application' and 'Protein Reference Dataset'
    section.

-   **Jazmin Ramos Madrigal**: Manuscript review, conceptualization and
    code for multiple R and bash scripts utilised by the Snakemake
    script as steps of the pipeline.

-   **Enrico Cappellini** : Manuscript review and editing

-   **Fernando Racimo** : Conceptualization, manuscript writing, review
    and editing

# Acknowledgements

We thank Ryan Sinclair Paterson, Graham Gower, Alberto Taurozzi, Martin
Petr, Evan Irving-Pease and other members of the Racimo and Cappellini
groups, who provided valuable help and feedback throughout the project.

#### 

#### 

#### 

# Funding

The project was funded by the European Union's EU Framework Programme
for Research and Innovation Horizon 2020, under Grant Agreement No.
861389 - PUSHH. FR was additionally supported by a Villum Young
Investigator Grant (project no. 00025300), a COREX ERC Synergy grant (ID
951385) and a Novo Nordisk Fonden Data Science Ascending Investigator
Award (NNF22OC0076816). E.C. was additionally supported by the European
Research Council (ERC) through the ERC Advanced Grant "BACKWARD", under
the Eu- ropean Union's Horizon 2020 research and innovation program
(grant agreement No. 101021361).
