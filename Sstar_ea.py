##Sstats -Sliding Windows of size 50 kb at each 20 kb- EASN-YRI -second half - Reference Chimp
##Author: Recep Ozgur Taskent

import itertools
from itertools import islice
import random
import sys
import os

inputfile1 = sys.argv[1]
inputfile2 = sys.argv[2]
outputfile1 = sys.argv[3]
outputfile2 = sys.argv[4]
RUNX = sys.argv[5]


def get_easn_yri_col_nos(genotypes_start_col, easn_sample_size, yri_sample_size):
	easn_col_no_l = []
	for i in range(genotypes_start_col, genotypes_start_col + easn_sample_size):
		easn_col_no_l.append(i)
	yri_col_no_l = []
	for i in range(genotypes_start_col + easn_sample_size, genotypes_start_col + easn_sample_size + yri_sample_size):
		yri_col_no_l.append(i)
	return easn_col_no_l, yri_col_no_l






def get_window_start_end_line_no_dicts(infile):
	inf_wind = open(infile, 'r')
	wind_start_snp_dict = {}
	wind_end_snp_dict = {}
	count_w = 0
	for line in inf_wind:
		l = line.split()
		wind_start_snp_dict[count_w] = l[0]
		wind_end_snp_dict[count_w] = l[1]
		count_w += 1
	inf_wind.close()
	return wind_start_snp_dict, wind_end_snp_dict



def calculate_Sstar(snp_list, snp_geno_dict, snp_pos_dict):
	score_G_x_dict = {} #empty dictionary for snp scores
	score_x_y_dict = {}	#empty dictionary for snp-pair scores
	score_G_x = 0
	for x in range(len(snp_list)-1):   #for each snp and snp pair, start S*score vectors from zero 
		for y in range(x+1, len(snp_list)):
			score_G_x_dict[snp_list[x]] = 0
			score_G_x_dict[snp_list[y]] = 0
	for x in range(len(snp_list)-1):   #from now on, calculate S*stats
		for y in range(x+1, len(snp_list)):
			total_mis = 0 	#start a mismatch vector for the snp-pair
			e = snp_list[x] 	#first snp position in the file - particular row where the snp is located in the file
			f = snp_list[y] 	#second snp position in the file - particular row where the snp is located in the file
			geno_list_snp1 = snp_geno_dict[e]  #genotypes for all 20 East Asians for the first snp
			geno_list_snp2 = snp_geno_dict[f]  	#genotypes for all 20 East Asians for the second snp
			for v in range(len(geno_list_snp1)): 	#for each individual from nweur get the genotypes  
				w = geno_list_snp1[v] 
				z = geno_list_snp2[v]
				total_mis += abs(int(w) - int(z)) 	#for the snp-pair, calculate the total mismatch between the genotypes of each individual from 20 total individuals from yoruba  
			if total_mis == 0: 		#if there is no mismatch for the genotypes of all 20 individuals for the two snps      
				if score_G_x_dict[e] >= 0: #if S(G, x) is not minus infinity, that is, if the first snp (e) does not have a minus infinity score retained from earlier snp-pair comparisons 
					S_x_y = 5000 + int(snp_pos_dict[f])- int(snp_pos_dict[e]) 	#instantaneous score for the snp-pair is: 5000 + the nucleotide distance between the two snps
					score = S_x_y + score_G_x_dict[e] 	#cumulative S*score for the snp pair is:  instantaneous score for the snp pair + the first snp's retaining individual score
					if score_G_x_dict[f] < score: 	#if the retaining individual score for the second snp is smaller than the cumulative score of the snp pair, equate it to score, that is, if the second snp has a better score for this snp-pair comparison, equate its individual retaining score to the cumulative score of the snp pair   
						score_G_x_dict[f] = score 
					snp_pair = str(e) + "_" + str(f) 
					score_x_y_dict[snp_pair] = score  	#add cumulative score of the snp pair to the snp-pair score dictionary
				elif score_G_x_dict[e] < 0: #if S(G, x) is minus infinity, that is, if the first snp (e) does have a minus infinity score retained from earlier snp pair   
					S_x_y = 5000 + int(snp_pos_dict[f])- int(snp_pos_dict[e])	#instantaneous score for the snp pair is: 5000 + the nucleotide distance between the two snps
					score = S_x_y	#cumulative S*score for the snp-pair is:  instantaneous score for the snp pair 
					if score_G_x_dict[f] < score: 	#if the retaining individual score for the second snp is smaller than the cumulative score of the snp pair, equate it to score, that is, if the second snp has a better score for this snp-pair comparison, equate its individual retaining score to the cumulative score of the snp pair
						score_G_x_dict[f] = score
					snp_pair = str(e) + "_" + str(f)
					score_x_y_dict[snp_pair] = score 	#add cumulative score of the snp pair to the snp-pair score dictionary
			elif total_mis > 0 and total_mis < 6: #if there are 1 to 5 mismatches btw two snps
				if score_G_x_dict[e] >= 0: #if S(G, x) is not -infinity, that is, if the first snp (e) does not have a minus infinity score retained from earlier snp pair comparisons 
					S_x_y = int(-1 * 10000)	#instantaneous score for the snp pair is: -10000 + the nucleotide distance between the two snps
					score = S_x_y + score_G_x_dict[e]	#cumulative S*score for the snp pair is:  instantaneous score for the snp pair + the first snp's individual retaining score
					if score_G_x_dict[f] < score:	#if the retaining individual score for the second snp is smaller than the cumulative score of the snp pair, equate it to score, that is, if the second snp has a better score for this snp-pair comparison, equate its individual retaining score to the cumulative score of the snp pair
						score_G_x_dict[f] = score
					snp_pair = str(e) + "_" + str(f)
					score_x_y_dict[snp_pair] = score	#add cumulative score of the snp pair to the snp-pair score dictionary
				elif score_G_x_dict[e] < 0: #if S(G, x) is -infinity, that is, if the first snp (e) does have a minus infinity score retained from earlier snp-pair comparisons 
					S_x_y = int(-1 * 10000)	#instantaneous score for the snp pair is: -10000 + the nucleotide distance between the two snps
					score = S_x_y	#cumulative S*score for the snp pair is:  instantaneous score for the snp-pair 
					if score > 0:	#if score is positive, equate it to the retaining individual score for the second snp 
						score_G_x_dict[f] = score 
					snp_pair = str(e) + "_" + str(f)
					score_x_y_dict[snp_pair] = score	#add cumulative score of the snp pair to the snp-pair score dictionary
			elif total_mis > 5:  #if there are more than 5 mismatches between the two snps
				score = -1 * float('inf') 	#equate the cumulative score for the snp pair to minus infinity
				snp_pair = str(e) + "_" + str(f)
				score_x_y_dict[snp_pair] = float(score) #add cumulative score of the snp-pair to the snp-pair score dictionary
	return score_G_x_dict, score_x_y_dict



	
	
def get_maximum_SscoreHaplo_SNPs(score_G_x_dict, score_x_y_dict, snp_pos_dict):
	maxi = 0
	maximumScore = 0
	haplo_list = []
	for snp in score_G_x_dict.keys(): 	#get snp with the maximum S*score  
		if score_G_x_dict[snp] > maxi:
			maxi = float(score_G_x_dict[snp])
			maxScore_snp = str(snp)
	#print m, score_G_x_dict, score_x_y_dict
	maxi = 0
	for snp_pair in score_x_y_dict.keys(): 	 #get snp-pair with the maximum S*score
		if score_x_y_dict[snp_pair] > maxi:
			maxi = float(score_x_y_dict[snp_pair])
			maximumScore = float(score_x_y_dict[snp_pair])
			maxScore_snp_pair = str(snp_pair)
	if maxi > 0: 	#if there is a snp-pair with >0 S*score 
		haplo_list = []		##add all snps that contributed to the maximum S*score to the haplotype list, start with the maximum scored snp pair...
		x_snp = maxScore_snp_pair.split('_')[0]		#first snp in the maximum scored snp pair
		y_snp = maxScore_snp_pair.split('_')[1]		#second snp in the maximum scored snp pair
		y_snp_pos = snp_pos_dict[int(y_snp)] 	#get second snp's position
		haplo_list.append(y_snp_pos)  ##add the position for the second snp to the haplotype list 
		while True:  ##add all the snps within the haplotype, continue with the other snps within the haplotype
			maximum = 0
			check = 0
			count5 = 0
			if x_snp == "1":  ##if the first snp in the max scored snp pair is the first snp within the window, add that snp and break...
				x_snp_pos = snp_pos_dict[int(x_snp)]
				haplo_list.append(x_snp_pos)
				break
			for snp_pair in score_x_y_dict.keys(): ##otherwise, for each snp pair for which S*score was calculated, look for the first snp in the maximum scored snp pair...
				first_snp = snp_pair.split("_")[0]		#first snp in the snp pair
				second_snp = snp_pair.split("_")[1]	#second snp in the snp pair
				if second_snp == x_snp: 	#if second snp in the current snp pair is the first snp in the maximum scored snp pair  
					if score_x_y_dict[snp_pair] > maximum:  #and if the S*score of the current snp pair > 0
						maximum = score_x_y_dict[snp_pair] 	#set maximum to S*score of the current snp pair 
						maxScore_snp_pair = str(snp_pair) 	#set maximum-scored snp pair to the current snp pair to get retrospectively all snps that are linked to the first maximum-scored snp pair
						count5 = 1		#set count vector to 1
			if count5 == 1 and maximum > 0: 	#if count is equal to one, that is, if there are more than snp-pair included in the haplotype
				x_snp = maxScore_snp_pair.split('_')[0]		#first snp in the maximum scored snp pair
				y_snp = maxScore_snp_pair.split('_')[1]		#second snp in the maximum scored snp pair
				y_snp_pos = snp_pos_dict[int(y_snp)]		#get second snp's position
				haplo_list.append(y_snp_pos)		##add the position for the second snp to the haplotype list
			if maximum == 0:	#if maximum is equal to zero, that is, if there is no other snp pair in the haplotype than the first maximum-scored snp pair  
				x_snp_pos = snp_pos_dict[int(x_snp)]	#get first snp's position
				haplo_list.append(x_snp_pos)	##add the position for the first snp (from the first maximum scored snp-pair) to the haplotype list and break
				break
		#haplo_dict[j] = haplo_list
	return maximumScore, haplo_list

 
 
 
 
 

outf = open(outputfile1, 'w') #open an output file for the haplotypes detected by S* - in .bed format
outf2 = open(outputfile2, 'w') ##open an output file for the total number of segregating sites used for S* calculations


genotypes_start_col = 5 
easn_sample_size = 20
yri_sample_size = 88

def main():
	
	Wind_start_line_no_dict = get_window_start_end_line_no_dicts(inputfile2)[0]
	Wind_end_line_no_dict = get_window_start_end_line_no_dicts(inputfile2)[1]
	easn = get_easn_yri_col_nos(genotypes_start_col, easn_sample_size, yri_sample_size)[0]
	afr = get_easn_yri_col_nos(genotypes_start_col, easn_sample_size, yri_sample_size)[1]

	snp_geno_dict = {} 	#set an empty snp-genotype dictionary
	snp_pos_dict = {}	#set an empty snp-position dictionary
	snp_list = [] 	#set an empty snp list	
	snp_list_wind_sstats = []	#set an empty list for derived snps where Sstats can be calculated - equivalent of mutation rate in the ms simulations
	haplo_dict = {}		#set an empty dictionary for haplotypes
	snp_count = 0	 #set a counter for the snps where S*stats will be calculated
	count_totalsnp_wind = 0		#set a counter for snps where 20 East Asian individuals have at least one derived allele  
	count_totalsnp_sstats = 0	#set a counter for snps for which S*stats can be calculated - equivalent of mutation rate in ms simulations
	haplo_list = []		#set an empty list for haplotypes

	for j in range(len(Wind_start_line_no_dict)):  ##for each window with the ascending order:
		print 'within window loop: ', j
		yri13 = random.sample(afr, 13)
		for m in easn: 	#for all 20 individuals from East Asia
			#print m
			print 'within individual loop: ', m
			inF = open(inputfile1, 'r') 		#Read the inputfile  
			prev_snp = 0 	#set the position for the previous snp to zero, to change it later
			print 'within inputfile: ', int(Wind_start_line_no_dict[j]) - 1, int(Wind_end_line_no_dict[j])
			for LINE in islice(inF, int(Wind_start_line_no_dict[j]) - 1, int(Wind_end_line_no_dict[j])): 	#for each line in the input file within given window 
				l = LINE.split()	
				CHRX = l[0]
				if int(l[m]) > 0: 	#if there is at least one derived allele at the current snp position for the individual for which S*score is going to be calculated, otherwise, skip the position
					count_totalsnp_wind += 1	#increase the total number of snps for which there is a derived allele for the 20 individuals from Yoruba
					if (l[2] not in snp_list_wind_sstats):
						count_totalsnp_sstats += 1		#increase the total number of derived snp in the window for which S*stats can be calculated - equivalent of mutation rate in ms simulations
						snp_list_wind_sstats.append(l[2])	#add current snp position to the list for derived snps where Sstats can be calculated - equivalent of mutation rate in ms simulations
					if (int(l[2]) - prev_snp >= 10):		#if the corrent snp position is not within 10 bp of the previous snp position and the corrent snp position is not in the list of snps for which S*stats have been calculated for other individuals
						pass
					else:	
						continue
					
					check = 0
					for i in yri13:
						if l[i] != '0':
							check = 1
					if check == 0:
						pass
					else:
						continue
					#afr_der_al_filter(afr, l)
					
					snp_count += 1		#increase snp count by one
					snp_list.append(snp_count)	 #add snp count to the list for the snps for which S*stats will be calculated   
					geno_list = []		#create an empty genotype list for 20 East Asian individuals for the current snp
					for k in easn:
						geno_list.append(l[k])		#add genotypes of 20 East Asian individuals for the current snp to the genotype list
					snp_geno_dict[snp_count] = geno_list	#add genotype list to the snp-genotype dictionary for the current snp 
					snp_pos_dict[snp_count] = int(l[2])		#add current snp position to the snp-position dictionary for the current snp 
					prev_snp = int(l[2])	#reset previous snp position to the current snp position
				elif int(l[m]) == 0:	#if there is no derived snp at the current snp position for the East Asian individual, but if any of the 13 Yoruba has at least one derived allele...
					for k in yri13:	
						if l[k] != "0" and (l[2] not in snp_list_wind_sstats):
							count_totalsnp_sstats += 1		#increase the total number of derived snp in the window for which S*stats can be calculated - equivalent of mutation rate in ms simulations  
							snp_list_wind_sstats.append(l[2])		#add current snp position to the list for derived snps where S*stats can be calculated - equivalent of mutation rate in ms simulations                	
			inF.close()		#close the file
			score_G_x_dict = calculate_Sstar(snp_list, snp_geno_dict, snp_pos_dict)[0]				
			score_x_y_dict = calculate_Sstar(snp_list, snp_geno_dict, snp_pos_dict)[1]
			maxScore = get_maximum_SscoreHaplo_SNPs(score_G_x_dict, score_x_y_dict, snp_pos_dict)[0]
			haplo_list = get_maximum_SscoreHaplo_SNPs(score_G_x_dict, score_x_y_dict, snp_pos_dict)[1]
			print maxScore, haplo_list
			snp_geno_dict = {} #directory for genotypes at each snp. Save as `snp_count` : `genotype_list`.
			snp_list = [] #list for snps (the number of snp where the individual of concern is polymorphic while the reference individual(s) carry the ancestral alleles).
			snp_pos_dict = {} #dictionary for snp positions. save as `snp_count` : `snp_position`.
			snp_count = 0
			if not haplo_list == []:
				highest = haplo_list[0] 	#the end position of the haplotype 
				lowest = haplo_list[-1] #the start position of the haplotype
				length = highest -lowest  #length of the haplotype
				WIND = [ str(j) ]
				IND = [ str(m) ]
				MAXIMUMSCORE = [ str(maxScore) ]
				#HAPLO_LIST = [ str(haplo_list) ]
				haplo_list2 = [str(i) for i in haplo_list]
				HAPLO_LIST = [ ','.join(haplo_list2) ]
				LENGTH = [ str(length) ]
				START = [ str(lowest) ]
				END = [ str(highest) ]
				CHR = [ CHRX ]
				IND2 =  [ ('ind' + str(m)) ]
				POP = [ 'EASN' ]
				RUN = [ RUNX ]
				NO_SNPS = [ str( len(haplo_list) ) ]
				print >>outf, '\t'.join(WIND + IND + MAXIMUMSCORE + HAPLO_LIST + LENGTH)
				print >>outf2, '\t'.join(CHR + START + END + POP + MAXIMUMSCORE + IND2 + LENGTH + RUN +  HAPLO_LIST + NO_SNPS + WIND)
				#outf.write("%s\t%s\t%f\t%s\t%d\n" % (j, m, maximumScore, haplo_list, length)) #write the window number, individual for which the S* was calculated, S* of the haplotype to the output file,  the haplotype, and the length of the haplotype to the outputfile
			haplo_list = []

		WIND = [ str(j) ]
		COUNT_TOTALSNPS = [ str(count_totalsnp_sstats) ]
		print >>outf3, '\t'.join(WIND + COUNT_TOTALSNPS)
		#outf2.write("%s\t%d\n" % (j, count_totalsnp_sstats))  #write the window number and the total number of segregating sites used for S* calculations to the outputfile2
		snp_list_wind_sstats = []
		count_totalsnp_sstats = 0
		count_totalsnp_wind = 0	
	outf.close()
	outf2.close()



if __name__ == '__main__':
	main()





