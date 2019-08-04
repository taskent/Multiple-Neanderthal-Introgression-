# Multiple-Neanderthal-Introgression-

In this project, I investigated whether Neanderthal-introgressed haplotypes in the genomes of present-day Europeans and East Asians were inherited from two different Neanderthal lineages; that is, the late Neanderthals represented by the Vindija Neanderthal genome (Prufer et al 2017) and an early Neanderthal lineage represented by the Altai Neanderthal genome (Prufer et al. 2014). 


1) S*-statistics
To find putatively Neanderthal-introgressed in present-day human genomes, S*-statistics is computed for 200 present-day genomes from each of Europe and East Asia.

S* is performed over 50 kb windows with a step size of 20 kb across all autosomal chromosomes of 20 test Eurasian genomes. 13 Yoruba genomes from sub-Saharan Africa are used as the outgroup population which does not carry Neanderthal ancestry.

Run S* as follows: 

#Western Europe

python Sstar_we.py inputfile1 inputfile2 outputfile1 outputfile2 run

#East Asia

python Sstar_ea.py inputfile1 inputfile2 outputfile1 outputfile2 run

inputfile1: A genotype file for present-day European or East Asian and Yoruba genomes (from sub-Saharan Africa) included in the 1000 Genomes Project, Phase I data set. The derived allele is ascertained against the chimpanzee genome (ie, chimpanzee allele is the ancestral allele)
inputfile2: A .txt file the start and end positions of 50 kb windows over which S* operates
outputfile1: A .bed formatted file (eg, chr start_position end_position genotype_ind1 genotype_ind2 ...) showing the start and end positions of the haplotypes with the highest S*-score for each window. All SNPs that S* used to infer the putatively introgressed haplotype for each window are included in this file. 
outputfile2: A .txt file the total number of segregating sites for all of the 20 Eurasian test genomes and 13 African outgroup genomes across each 50 kb window.
run: 1 to 10

To cover all 200 individuals, this step was performed for 10 runs each time with a different set of 20 European/East Asian and 13 Yoruba genomes.  


2) Haplotypes detected by S* that cannot be explained demographic processes not including Neanderthal introgression.

S*-scores of haplotypes detected for Eurasian genomes are compared with null S*-score distirutions gathered from sequences generated by coalescent simulations not including Neanderthal introgression. Coalescent simulations were performed with ms.  

As recombination and mutation rates vary across the human genome and that S*-statistic is sensitive to variations in recombination and mutation rates, we sampled recombination rate and number of segregating sites parameters of ms from the uniform distributions as shown below:

  ln(recombination rate) from -10.25 to 2.75 cM/Mb (step=0.25) 
  Number of segregating sites from 30 to 350 variants (step=5)

40 haploid sequences of length 50 kb with European/East Asian population history and 26 haploid sequences of length 50 kb wuth African population history were generated for 20,000 replicates with coalescent simulations for each recombination rate and number of segregating sites parameter-pairs. 

Haplotypes with S*-scores falling above 0.99 percentile of the null-distribution matching the recombination rate and the total number of segregating sites for the corresponding window were retained as the S*-significant putatively introgressed haplotypes. 

This filtering step was run as follows:

python SstarScoreFilter.py population run 

population: western Europe or East Asia
run: 1 to 10.


3) Concetanate S*-significant haplotypes for runs 1 to 10

Run as follows:

concat_Sstar_outs_runs1_10_sort.sh


4) Merge overlapping haplotypes

Run as follows:

bedtools merge -i inputfile -c 4,5,6,7,8,9,10,11 -o distinct,collapse,collapse,collapse,collapse,collapse,collapse,collapse -delim ";" >  outputfile

inputfile: A bed file including S*-significant haplotypes gathered from all 10 runs  
outputfile: A bed file including S*-significant haplotypes merged for overlapping regions. 


5) Find phased S*-significant haplotypes

To find phased S*-significant haplotypes, we detected the chromosome for which the derived allele is found in >0.5 times in the individual genome for which the introgressed haplotype is detected. Only SNP positions included in the S*-significant haplotype are used in this analysis.

Run as follows:

python find_phased_haplotypes.py


#Compute average pairwise nucleotide difference (pi) between the S*-significant haplotypes and the two high quality Neanderthal genomes (Altai and Vindija Neanderthal genomes) and count the number of new mutations occurred on S*-significant haplotypes in the modern human lineage (that is, after they entered human genomes) as well as the derived alleles shared between modern human populations and the ancient hominin genomes 

Run as follows:

#East Asia

python compute_pi_new_mut_freqs_on_Sstar_haplotypes_EA.py inputfile inputfile2 outputfile outputfile2

#Western Europe

python compute_pi_new_mut_freqs_on_Sstar_haplotypes_WE.py inputfile inputfile2 outputfile outputfile2

inputfile: A bed file for S*-significant phased haplotypes
inputfile2: A bed file for genotype data for European/East Asian, African as well as ancient hominin genomes (Altai Neanderthal, Vindija Neanderthal, Chagyrskaya Neanderthal and Denisovan genomes)
outputfile1: A bed file for average pairwise nucleotide differences (pi)
outputfile2: A bed file for number of new mutations and allele sharing between human populations and the ancient hominin genomes














