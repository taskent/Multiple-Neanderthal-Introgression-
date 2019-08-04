##Author: Recep Ozgur Taskent

## Sscore fine threshold filtering with number of segregating sites and recombination rate

import sys
import os
import math

Path = sys.argv[1] 
inputfile_recom_noSegSites = sys.argv[2]
inputfile_nullSscore_distribution = sys.argv[3]

RUNX = sys.argv[4] #runs 1 to 10
POPX = sys.argv[5] # ea or we


#individual column numbers for 20 European/East Asian genomes included in each S* run in the genotype bed file
eur20_1_10 = [ [147, 106, 109, 46, 250, 88, 39, 79, 261, 41, 56, 155, 201, 258, 8, 185, 86, 62, 126, 105],
 [175, 217, 269, 184, 34, 192, 271, 205, 257, 134, 11, 132, 181, 162, 118, 195, 23, 219, 223, 116],
 [101, 55, 14, 24, 133, 18, 47, 121, 136, 138, 169, 244, 202, 196, 144, 50, 232, 6, 111, 220],
 [128, 57, 153, 225, 207, 64, 182, 44, 210, 204, 5, 140, 95, 35, 102, 67, 218, 74, 97, 186],
 [110, 78, 151, 30, 222, 112, 117, 248, 16, 98, 73, 157, 93, 104, 168, 191, 143, 87, 37, 177],
 [54, 265, 66, 200, 26, 29, 142, 230, 141, 127, 96, 36, 25, 129, 99, 43, 263, 227, 268, 84],
 [159, 131, 15, 130, 114, 49, 212, 149, 17, 178, 260, 171, 45, 163, 199, 247, 197, 166, 90, 61],
 [7, 214, 239, 135, 190, 51, 122, 208, 198, 38, 237, 75, 12, 145, 13, 161, 238, 63, 164, 58],
 [81, 213, 180, 27, 221, 10, 60, 139, 115, 48, 137, 52, 22, 165, 158, 148, 246, 80, 189, 231],
 [42, 85, 70, 242, 119, 173, 123, 69, 266, 77, 103, 107, 92, 241, 94, 160, 215, 259, 270, 76] ]

easn20_1_10 = [ [81, 71, 134, 234, 66, 40, 178, 123, 26, 83, 112, 236, 95, 207, 275, 57, 164, 251, 144, 68], 
[54, 80, 189, 239, 260, 41, 84, 151, 276, 38, 243, 190, 158, 104, 289, 166, 261, 209, 59, 198],
[246, 139, 115, 222, 73, 263, 282, 44, 270, 105, 226, 25, 172, 167, 257, 42, 188, 197, 13, 250],
[259, 28, 223, 219, 213, 133, 159, 232, 136, 93, 283, 119, 228, 48, 10, 18, 196, 76, 60, 34],
[242, 254, 272, 89, 24, 79, 138, 273, 160, 32, 143, 177, 183, 15, 249, 279, 280, 194, 50, 165],
[145, 182, 155, 288, 201, 87, 245, 131, 39, 30, 37, 51, 180, 150, 285, 152, 118, 247, 206, 12],
[218, 7, 19, 92, 181, 162, 64, 258, 171, 215, 191, 268, 116, 11, 174, 52, 203, 88, 192, 55],
[47, 225, 9, 220, 217, 137, 170, 212, 264, 148, 200, 156, 199, 262, 16, 202, 230, 17, 214, 274],
[114, 193, 157, 74, 96, 146, 125, 27, 56, 122, 6, 77, 97, 290, 281, 271, 120, 107, 269, 130],
[229, 121, 103, 35, 108, 126, 90, 252, 187, 31, 124, 33, 70, 45, 231, 53, 82, 135, 43, 98] ]

path = Path

for filename in os.listdir(path):
	if filename != 'SstarScoreFilter':
		inf = open(path + filename, 'r')
		fileName = filename.split('.')
		fileName2 = '.'.join(fileName[:-1]) 
		outf = open(path + 'SstarScoreFilter/' + fileName2 + '.' + 'fineThres' + '.bed', 'w')
		pop = str(fileName[1])
		check = 0
		if fileName[3][-1] == 'a' or fileName[3][-1] == 'b':
			CHR = fileName[3][:-1]
			chr = fileName[3]
			check = 1
		else:
			CHR = fileName[3]
			chr = fileName[3]
		if pop == 'NW_EUR':
			pop2 = 'nweur'
		elif pop == 'E_ASN':
			pop2 = 'easn'
		if pop == 'NW_EUR':
			for line in inf:
				inf_r_s = open(inputfile_recom_noSegSites, 'r')
				inf_null = open(inputfile_nullSscore_distribution, 'r')
				l = line.split()
				start_snp = int(l[1])
				stop_snp = int(l[2])
				ind = l[5]
				ind_col_index = int(ind[3:]) - 5
				new_ind = 'ind' + str(eur20_1_10[int(RUNX) - 1][ind_col_index])
				try: 
					Sscore = l[4].split('.')
					Sscore = int(Sscore[0])
				except ValueError:
					print 'There is a value error with Sscore: %s' % (l[4]),  'run: ', RUNX
					print 'this is the line', line, 'run: ', RUN
					continue
				for line2 in inf_r_s:
					l2 = line2.split()
					w_start_snp = int(l2[2])
					w_stop_snp = int(l2[3])
					if start_snp >= w_start_snp and stop_snp <= w_stop_snp and l2[4] != 'NA':
						recom_rate = float(l2[4])
						try:
							log_recom_rate = math.log(recom_rate)
						except ValueError:
							if recom_rate == 0.0:
								log_recom_rate = -2.75
								pass
							else:
								print 'value error for log-transf of recomb rate: %f' % (recom_rate), 'run: ', RUNX
								print line
								continue
						try:
							segNo = float(l2[5])
						except IndexError:
							print 'there is an index error for inf_r_s: no noSnps for easn', 'run: ', RUNX
							print line2
							continue 
						for line3 in inf_null:
							l3 = line3.split()
							segNo_null = int(l3[0])
							recom_rate_null = (float(l3[1]) * (10**8)) / (4 * 7314.285714)
							try:							
								log_recom_rate_null = math.log(recom_rate_null)
							except ValueError:
								print 'value error for log-transf of null recomb rate: %f' % (recom_rate_null), 'run: ', RUNX
								print line
								continue
							if (segNo > (segNo_null - 5)) and (segNo <= segNo_null ):
								if log_recom_rate > 0.0:
									if log_recom_rate < 2.75:
										if (log_recom_rate >= log_recom_rate_null) and (log_recom_rate < (log_recom_rate_null + 0.25)):
											Sscore_thres = float(l3[4])
											if float(Sscore) > Sscore_thres: 
												if check == 1:
													chromosome =  [ CHR ]
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(chromosome + l[1:5] + new_IND + l[6:])
												elif check == 0: 
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(l[0:5] + new_IND + l[6:])
												break
									elif log_recom_rate >= 2.75:
										if log_recom_rate_null == 2.75:
											Sscore_thres = float(l3[4])
											if float(Sscore) > Sscore_thres: 
												if check == 1:
													chromosome =  [ CHR ]
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(chromosome + l[1:5] + new_IND + l[6:])
												elif check == 0: 
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(l[0:5] + new_IND + l[6:])
												break
										
								else:
									if log_recom_rate > -10.25:
										if (log_recom_rate <= log_recom_rate_null) and (log_recom_rate > (log_recom_rate_null - 0.25)):
											Sscore_thres = float(l3[4])
											if float(Sscore) > Sscore_thres: 
												if check == 1:
													chromosome =  [ CHR ]
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(chromosome + l[1:5] + new_IND + l[6:])
												elif check == 0: 
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(l[0:5] + new_IND + l[6:])
												break									
									if log_recom_rate <= -10.25:
										if log_recom_rate_null == -10.25:
											Sscore_thres = float(l3[4])
											if float(Sscore) > Sscore_thres: 
												if check == 1:
													chromosome =  [ CHR ]
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(chromosome + l[1:5] + new_IND + l[6:])
												elif check == 0: 
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(l[0:5] + new_IND + l[6:])
												break
						inf_null.close()
						break
				inf_r_s.close()
			inf.close()
			outf.close()
		elif pop == 'E_ASN':
			for line in inf:
				inf_r_s = open(inputfile_recom_noSegSites, 'r')
				inf_null = open(inputfile_nullSscore_distribution, 'r')
				l = line.split()
				start_snp = int(l[1])
				stop_snp = int(l[2])
				ind = l[5]
				ind_col_index = int(ind[3:]) - 5
				new_ind = 'ind' + str(easn20_1_10[int(RUNX) - 1][ind_col_index])
				try: 
					Sscore = l[4].split('.')
					Sscore = int(Sscore[0])
				except ValueError:
					print 'There is a value error with Sscore: %s' % (l[4]), 'run: ', RUNX
					print 'this is the line', line
					continue
				for line2 in inf_r_s:
					l2 = line2.split()
					w_start_snp = int(l2[2])
					w_stop_snp = int(l2[3])
					if start_snp >= w_start_snp and stop_snp <= w_stop_snp and l2[4] != 'NA':
						recom_rate = float(l2[4])
						try:
							log_recom_rate = math.log(recom_rate)
						except ValueError:
							if recom_rate == 0.0:
								log_recom_rate = -2.75
								pass
							else:
								print 'value error for log-transf of recomb rate: %f' % (recom_rate), 'run: ', RUNX
								print line
								continue
						try:
							segNo = float(l2[5])
						except IndexError:
							print 'there is an index error for inf_r_s: no noSnps for easn', 'run: ', RUNX
							print line2
							continue 
						for line3 in inf_null:
							l3 = line3.split()
							segNo_null = int(l3[0])
							recom_rate_null = (float(l3[1]) * (10**8)) / (4 * 7314.285714)
							try:							
								log_recom_rate_null = math.log(recom_rate_null)
							except ValueError:
								print 'value error for log-transf of null recomb rate: %f' % (recom_rate_null), 'run: ', RUNX
								print line
								continue
							if (segNo > (segNo_null - 5)) and (segNo <= segNo_null ):
								if log_recom_rate > 0.0:
									if log_recom_rate < 2.75:
										if (log_recom_rate >= log_recom_rate_null) and (log_recom_rate < (log_recom_rate_null + 0.25)):
											Sscore_thres = float(l3[4])
											if float(Sscore) > Sscore_thres: 
												if check == 1:
													chromosome =  [ CHR ]
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(chromosome + l[1:5] + new_IND + l[6:])
												elif check == 0: 
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(l[0:5] + new_IND + l[6:])
												break
									elif log_recom_rate >= 2.75:
										if log_recom_rate_null == 2.75:
											Sscore_thres = float(l3[4])
											if float(Sscore) > Sscore_thres: 
												if check == 1:
													chromosome =  [ CHR ]
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(chromosome + l[1:5] + new_IND + l[6:])
												elif check == 0: 
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(l[0:5] + new_IND + l[6:])
												break
										
								else:
									if log_recom_rate > -10.25:
										if (log_recom_rate <= log_recom_rate_null) and (log_recom_rate > (log_recom_rate_null - 0.25)):
											Sscore_thres = float(l3[4])
											if float(Sscore) > Sscore_thres: 
												if check == 1:
													chromosome =  [ CHR ]
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(chromosome + l[1:5] + new_IND + l[6:])
												elif check == 0: 
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(l[0:5] + new_IND + l[6:])
												break									
									if log_recom_rate <= -10.25:
										if log_recom_rate_null == -10.25:
											Sscore_thres = float(l3[4])
											if float(Sscore) > Sscore_thres: 
												if check == 1:
													chromosome =  [ CHR ]
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(chromosome + l[1:5] + new_IND + l[6:])
												elif check == 0: 
													new_IND = [ new_ind ]
													print >>outf, '\t'.join(l[0:5] + new_IND + l[6:])
												break
						inf_null.close()
						break
				inf_r_s.close()
			inf.close()
			outf.close()
							
							
							
							
		
		
		
		
		
		
		

