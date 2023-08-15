data <- readDiscreteCharacterData("CONCATINATED_o_Rev.nex") #load nexus data

## Helpful integers
num_taxa <- data[1].ntaxa()
num_branches <- 2 * num_taxa - 3
taxa <- data[1].taxa()
n_data_subsets <- data.size()


## Create Empty lists
moves    = VectorMoves()
monitors = VectorMonitors()


for (i in 1:n_data_subsets){
## subst matrix
Q[i] <- fnDayhoff()

## Gamma rate variation
alpha[i]~ dnUniform(0,1E8)
alpha[i].setValue(1)
gamma_rates[i]:=fnDiscretizeGamma(alpha[i],alpha[i],4,false)
moves.append(mvScale(alpha[i],lambda=0.1,tune=true,weight=1.0))


### Prblity of a site in partition being invariable
pinvar[i]~dnBeta(1.0,1.0)
moves.append(mvBetaProbability(pinvar[i],delta=2,tune=true,weight=1.0))

}



## Set topology
topology ~ dnUniformTopology(taxa)


####
## mixing moves for MCMC, scalled with number of taxa
moves.append( mvNNI(topology, weight=num_taxa) )
moves.append( mvSPR(topology, weight=num_taxa/10.0) )


#####
## Create random branch length branches
for (i in 1:num_branches){
br_lens[i] ~ dnExponential(10.0)
moves.append( mvScale(br_lens[i]) )
}


##########
### Tree Length
TL := sum(br_lens)

########
### Set up Phylogram
psi := treeAssembly(topology, br_lens)

##########
### Set up rate multipliers for each partition
for (i in 1:n_data_subsets){
if (i == 1) {
part_rate_mult[i] <- 1.0
} else {
part_rate_mult[i] ~ dnLognormal (0.0, 0.587405)  #sd=0.587405 corresponds to one-order-of-magnitude sd for a lognormal distribution
moves.append( mvScaleBactrian(part_rate_mult[i], lambda=0.1, weight=1.0))
}
}


###########
### Combine everything
for (i in 1:n_data_subsets){
seq[i] ~ dnPhyloCTMC(tree=psi, Q=Q[i], branchRates=part_rate_mult[i], siteRates=gamma_rates[i], pInv=pinvar[i], type="AA")
seq[i].clamp(data[i])
}

###########
## Create model
mymodel = model(psi)

##########
#Monitor run
monitors.append( mnModel(filename="output_RevBayes/CONCATINATED_rev.log", printgen=10) )
monitors.append( mnFile(filename="output_RevBayes/CONCATINATED_rev.trees", printgen=10, psi) )
monitors.append( mnScreen(printgen=10, TL) )

## Run MCMC
mymcmc = mcmc(mymodel, monitors, moves, nruns=2, combine="mixed")
mymcmc.run(generations=20000, tuningInterval=100, checkpointInterval=100, checkpointFile="output_RevBayes/CONCATINATED_rev.state")

#### Restart from checkpoint
#### mymcmc.initializeFromCheckpoint("output/primates_cytb_JC.state")


treetrace = readAncestralStateTreeTrace("output_RevBayes/CONCATINATED_rev.trees", treetype="non-clock")
map_tree = mapTree(treetrace,"output_RevBayes/CONCATINATED_MAP_rev.trees")






### Query probability of clade
# Lemuroidea <- clade("Cheirogaleus_major",
                    # "Daubentonia_madagascariensis",
                    # "Lemur_catta",
                    # "Lepilemur_hubbardorum",
                    # "Microcebus_murinus",
                    # "Propithecus_coquereli",
                    # "Varecia_variegata_variegata")

# treetrace.cladeProbability( Lemuroidea )

q()
