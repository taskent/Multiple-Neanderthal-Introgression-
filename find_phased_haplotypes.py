##Author: Recep Ozgur Taskent

import sys
import os
import string

inputfile1 = sys.argv[1]
inputfile2 = sys.argv[2]
outputfile = sys.argv[3]
popx = sys.argv[4]

inf = open(inputfile1,'r')
outf = open(output_name,'w')

if popx == 'ea':
	pop_d = {'ind251': 'NA18999', 'ind154': 'HG00580', 'ind163': 'HG00596', 'ind48': 'NA18579', 'ind49': 'NA18582', 'ind42': 'NA18571', 'ind43': 'NA18572', 'ind40': 'NA18567', 'ind41': 'NA18570', 'ind46': 'NA18576', 'ind47': 'NA18577', 'ind44': 'NA18573', 'ind45': 'NA18574', 'ind241': 'NA18985', 'ind240': 'NA18984', 'ind243': 'NA18987', 'ind242': 'NA18986', 'ind245': 'NA18989', 'ind139': 'HG00531', 'ind247': 'NA18992', 'ind246': 'NA18990', 'ind249': 'NA18995', 'ind248': 'NA18994', 'ind138': 'HG00530', 'ind164': 'HG00607', 'ind137': 'HG00525', 'ind166': 'HG00610', 'ind167': 'HG00611', 'ind160': 'HG00592', 'ind161': 'HG00593', 'ind162': 'HG00595', 'ind136': 'HG00524', 'ind168': 'HG00613', 'ind135': 'HG00513', 'ind77': 'NA18626', 'ind76': 'NA18624', 'ind75': 'NA18623', 'ind74': 'NA18622', 'ind73': 'NA18621', 'ind72': 'NA18620', 'ind71': 'NA18619', 'ind70': 'NA18618', 'ind133': 'HG00501', 'ind189': 'HG00684', 'ind79': 'NA18628', 'ind78': 'NA18627', 'ind290': 'NA19088', 'ind281': 'NA19078', 'ind131': 'HG00479', 'ind287': 'NA19084', 'ind114': 'HG00442', 'ind130': 'HG00478', 'ind285': 'NA19082', 'ind278': 'NA19075', 'ind279': 'NA19076', 'ind274': 'NA19068', 'ind275': 'NA19070', 'ind109': 'HG00422', 'ind277': 'NA19074', 'ind270': 'NA19064', 'ind271': 'NA19065', 'ind272': 'NA19066', 'ind273': 'NA19067', 'ind173': 'HG00626', 'ind172': 'HG00625', 'ind171': 'HG00620', 'ind170': 'HG00619', 'ind177': 'HG00635', 'ind176': 'HG00634', 'ind117': 'HG00446', 'ind174': 'HG00628', 'ind179': 'HG00651', 'ind178': 'HG00650', 'ind276': 'NA19072', 'ind60': 'NA18608', 'ind61': 'NA18609', 'ind62': 'NA18610', 'ind63': 'NA18611', 'ind64': 'NA18612', 'ind65': 'NA18613', 'ind66': 'NA18614', 'ind67': 'NA18615', 'ind68': 'NA18616', 'ind69': 'NA18617', 'ind119': 'HG00449', 'ind118': 'HG00448', 'ind282': 'NA19079', 'ind286': 'NA19083', 'ind124': 'HG00463', 'ind125': 'HG00464', 'ind158': 'HG00589', 'ind269': 'NA19063', 'ind268': 'NA19062', 'ind283': 'NA19080', 'ind134': 'HG00512', 'ind262': 'NA19055', 'ind261': 'NA19054', 'ind260': 'NA19012', 'ind267': 'NA19060', 'ind266': 'NA19059', 'ind265': 'NA19058', 'ind264': 'NA19057', 'ind128': 'HG00475', 'ind188': 'HG00683', 'ind129': 'HG00476', 'ind186': 'HG00671', 'ind187': 'HG00672', 'ind184': 'HG00662', 'ind185': 'HG00663', 'ind182': 'HG00656', 'ind183': 'HG00657', 'ind180': 'HG00653', 'ind181': 'HG00654', 'ind120': 'HG00451', 'ind121': 'HG00452', 'ind122': 'HG00457', 'ind123': 'HG00458', 'ind99': 'NA18748', 'ind98': 'NA18747', 'ind126': 'HG00472', 'ind127': 'HG00473', 'ind95': 'NA18647', 'ind94': 'NA18645', 'ind97': 'NA18745', 'ind96': 'NA18740', 'ind91': 'NA18641', 'ind90': 'NA18640', 'ind93': 'NA18643', 'ind92': 'NA18642', 'ind15': 'NA18538', 'ind14': 'NA18537', 'ind17': 'NA18541', 'ind16': 'NA18539', 'ind11': 'NA18534', 'ind10': 'NA18532', 'ind13': 'NA18536', 'ind12': 'NA18535', 'ind19': 'NA18543', 'ind18': 'NA18542', 'ind244': 'NA18988', 'ind132': 'HG00500', 'ind216': 'NA18953', 'ind235': 'NA18978', 'ind199': 'HG00705', 'ind198': 'HG00704', 'ind218': 'NA18956', 'ind219': 'NA18957', 'ind195': 'HG00699', 'ind194': 'HG00698', 'ind197': 'HG00702', 'ind196': 'HG00701', 'ind191': 'HG00690', 'ind190': 'HG00689', 'ind193': 'HG00693', 'ind192': 'HG00692', 'ind115': 'HG00443', 'ind88': 'NA18638', 'ind89': 'NA18639', 'ind86': 'NA18636', 'ind87': 'NA18637', 'ind84': 'NA18634', 'ind85': 'NA18635', 'ind82': 'NA18632', 'ind83': 'NA18633', 'ind80': 'NA18630', 'ind81': 'NA18631', 'ind116': 'HG00445', 'ind111': 'HG00428', 'ind110': 'HG00427', 'ind102': 'HG00403', 'ind113': 'HG00437', 'ind165': 'HG00608', 'ind214': 'NA18951', 'ind112': 'HG00436', 'ind209': 'NA18946', 'ind208': 'NA18945', 'ind205': 'NA18942', 'ind204': 'NA18941', 'ind207': 'NA18944', 'ind206': 'NA18943', 'ind201': 'HG00708', 'ind200': 'HG00707', 'ind103': 'HG00404', 'ind202': 'NA18939', 'ind148': 'HG00559', 'ind149': 'HG00560', 'ind289': 'NA19087', 'ind142': 'HG00536', 'ind143': 'HG00537', 'ind140': 'HG00533', 'ind141': 'HG00534', 'ind146': 'HG00556', 'ind147': 'HG00557', 'ind144': 'HG00542', 'ind145': 'HG00543', 'ind33': 'NA18560', 'ind32': 'NA18559', 'ind31': 'NA18558', 'ind30': 'NA18557', 'ind37': 'NA18564', 'ind36': 'NA18563', 'ind35': 'NA18562', 'ind34': 'NA18561', 'ind39': 'NA18566', 'ind38': 'NA18565', 'ind288': 'NA19085', 'ind280': 'NA19077', 'ind222': 'NA18961', 'ind169': 'HG00614', 'ind238': 'NA18982', 'ind239': 'NA18983', 'ind203': 'NA18940', 'ind230': 'NA18973', 'ind231': 'NA18974', 'ind232': 'NA18975', 'ind233': 'NA18976', 'ind234': 'NA18977', 'ind175': 'HG00629', 'ind236': 'NA18980', 'ind237': 'NA18981', 'ind159': 'HG00590', 'ind106': 'HG00418', 'ind107': 'HG00419', 'ind151': 'HG00566', 'ind150': 'HG00565', 'ind153': 'HG00578', 'ind152': 'HG00577', 'ind155': 'HG00581', 'ind104': 'HG00406', 'ind157': 'HG00584', 'ind156': 'HG00583', 'ind105': 'HG00407', 'ind28': 'NA18553', 'ind29': 'NA18555', 'ind24': 'NA18548', 'ind25': 'NA18549', 'ind26': 'NA18550', 'ind27': 'NA18552', 'ind20': 'NA18544', 'ind21': 'NA18545', 'ind22': 'NA18546', 'ind23': 'NA18547', 'ind5': 'NA18525', 'ind226': 'NA18965', 'ind7': 'NA18527', 'ind6': 'NA18526', 'ind223': 'NA18962', 'ind100': 'NA18749', 'ind221': 'NA18960', 'ind220': 'NA18959', 'ind101': 'NA18757', 'ind9': 'NA18530', 'ind8': 'NA18528', 'ind229': 'NA18971', 'ind228': 'NA18968', 'ind227': 'NA18966', 'ind225': 'NA18964', 'ind59': 'NA18606', 'ind58': 'NA18605', 'ind224': 'NA18963', 'ind108': 'HG00421', 'ind217': 'NA18954', 'ind51': 'NA18593', 'ind50': 'NA18592', 'ind53': 'NA18596', 'ind52': 'NA18595', 'ind55': 'NA18599', 'ind54': 'NA18597', 'ind57': 'NA18603', 'ind56': 'NA18602', 'ind252': 'NA19000', 'ind253': 'NA19002', 'ind250': 'NA18998', 'ind215': 'NA18952', 'ind256': 'NA19005', 'ind257': 'NA19007', 'ind254': 'NA19003', 'ind255': 'NA19004', 'ind212': 'NA18949', 'ind258': 'NA19009', 'ind259': 'NA19010', 'ind213': 'NA18950', 'ind263': 'NA19056', 'ind210': 'NA18947', 'ind284': 'NA19081', 'ind211': 'NA18948'}
	population = 'EASN' 
elif popx == 'we':
	pop_d =  {'ind251': 'NA12749', 'ind154': 'HG00339', 'ind163': 'HG00351', 'ind48': 'HG00146', 'ind49': 'HG00148', 'ind42': 'HG00138', 'ind43': 'HG00139', 'ind40': 'HG00136', 'ind41': 'HG00137', 'ind46': 'HG00142', 'ind47': 'HG00143', 'ind44': 'HG00140', 'ind45': 'HG00141', 'ind241': 'NA12383', 'ind240': 'NA12348', 'ind243': 'NA12400', 'ind242': 'NA12399', 'ind245': 'NA12489', 'ind139': 'HG00323', 'ind247': 'NA12716', 'ind246': 'NA12546', 'ind249': 'NA12718', 'ind248': 'NA12717', 'ind138': 'HG00321', 'ind164': 'HG00353', 'ind137': 'HG00320', 'ind166': 'HG00356', 'ind167': 'HG00357', 'ind160': 'HG00346', 'ind161': 'HG00349', 'ind162': 'HG00350', 'ind136': 'HG00319', 'ind168': 'HG00358', 'ind135': 'HG00318', 'ind77': 'HG00250', 'ind76': 'HG00249', 'ind75': 'HG00247', 'ind74': 'HG00246', 'ind73': 'HG00245', 'ind72': 'HG00244', 'ind71': 'HG00243', 'ind70': 'HG00242', 'ind133': 'HG00313', 'ind189': 'NA06989', 'ind79': 'HG00252', 'ind78': 'HG00251', 'ind131': 'HG00311', 'ind114': 'HG00270', 'ind130': 'HG00310', 'ind109': 'HG00190', 'ind270': 'NA12889', 'ind271': 'NA12890', 'ind173': 'HG00364', 'ind172': 'HG00362', 'ind171': 'HG00361', 'ind170': 'HG00360', 'ind177': 'HG00372', 'ind176': 'HG00369', 'ind117': 'HG00273', 'ind174': 'HG00366', 'ind179': 'HG00375', 'ind178': 'HG00373', 'ind60': 'HG00231', 'ind61': 'HG00232', 'ind62': 'HG00233', 'ind63': 'HG00234', 'ind64': 'HG00235', 'ind65': 'HG00236', 'ind66': 'HG00237', 'ind67': 'HG00238', 'ind68': 'HG00239', 'ind69': 'HG00240', 'ind119': 'HG00275', 'ind118': 'HG00274', 'ind124': 'HG00281', 'ind125': 'HG00282', 'ind158': 'HG00344', 'ind269': 'NA12874', 'ind268': 'NA12873', 'ind134': 'HG00315', 'ind262': 'NA12827', 'ind261': 'NA12815', 'ind260': 'NA12814', 'ind267': 'NA12872', 'ind266': 'NA12843', 'ind265': 'NA12842', 'ind264': 'NA12830', 'ind128': 'HG00306', 'ind188': 'NA06986', 'ind129': 'HG00309', 'ind186': 'HG00384', 'ind187': 'NA06984', 'ind184': 'HG00382', 'ind185': 'HG00383', 'ind182': 'HG00378', 'ind183': 'HG00381', 'ind180': 'HG00376', 'ind181': 'HG00377', 'ind120': 'HG00276', 'ind121': 'HG00277', 'ind122': 'HG00278', 'ind123': 'HG00280', 'ind99': 'HG00178', 'ind98': 'HG00177', 'ind126': 'HG00284', 'ind127': 'HG00285', 'ind95': 'HG00173', 'ind94': 'HG00171', 'ind97': 'HG00176', 'ind96': 'HG00174', 'ind91': 'HG00264', 'ind90': 'HG00263', 'ind93': 'HG01334', 'ind92': 'HG00265', 'ind15': 'HG00109', 'ind14': 'HG00108', 'ind17': 'HG00111', 'ind16': 'HG00110', 'ind11': 'HG00103', 'ind10': 'HG00102', 'ind13': 'HG00106', 'ind12': 'HG00104', 'ind19': 'HG00113', 'ind18': 'HG00112', 'ind244': 'NA12413', 'ind132': 'HG00312', 'ind216': 'NA11995', 'ind235': 'NA12287', 'ind199': 'NA10851', 'ind198': 'NA10847', 'ind218': 'NA12004', 'ind219': 'NA12006', 'ind195': 'NA07056', 'ind194': 'NA07051', 'ind197': 'NA07357', 'ind196': 'NA07347', 'ind191': 'NA07000', 'ind190': 'NA06994', 'ind193': 'NA07048', 'ind192': 'NA07037', 'ind115': 'HG00271', 'ind88': 'HG00261', 'ind89': 'HG00262', 'ind86': 'HG00259', 'ind87': 'HG00260', 'ind84': 'HG00257', 'ind85': 'HG00258', 'ind82': 'HG00255', 'ind83': 'HG00256', 'ind80': 'HG00253', 'ind81': 'HG00254', 'ind116': 'HG00272', 'ind111': 'HG00267', 'ind110': 'HG00266', 'ind102': 'HG00182', 'ind113': 'HG00269', 'ind165': 'HG00355', 'ind214': 'NA11993', 'ind112': 'HG00268', 'ind209': 'NA11930', 'ind208': 'NA11920', 'ind205': 'NA11893', 'ind204': 'NA11892', 'ind207': 'NA11919', 'ind206': 'NA11894', 'ind201': 'NA11830', 'ind200': 'NA11829', 'ind103': 'HG00183', 'ind202': 'NA11831', 'ind148': 'HG00332', 'ind149': 'HG00334', 'ind142': 'HG00326', 'ind143': 'HG00327', 'ind140': 'HG00324', 'ind141': 'HG00325', 'ind146': 'HG00330', 'ind147': 'HG00331', 'ind144': 'HG00328', 'ind145': 'HG00329', 'ind33': 'HG00128', 'ind32': 'HG00127', 'ind31': 'HG00126', 'ind30': 'HG00125', 'ind37': 'HG00133', 'ind36': 'HG00131', 'ind35': 'HG00130', 'ind34': 'HG00129', 'ind39': 'HG00135', 'ind38': 'HG00134', 'ind222': 'NA12045', 'ind169': 'HG00359', 'ind238': 'NA12342', 'ind239': 'NA12347', 'ind203': 'NA11843', 'ind230': 'NA12273', 'ind231': 'NA12275', 'ind232': 'NA12282', 'ind233': 'NA12283', 'ind234': 'NA12286', 'ind175': 'HG00367', 'ind236': 'NA12340', 'ind237': 'NA12341', 'ind159': 'HG00345', 'ind106': 'HG00187', 'ind107': 'HG00188', 'ind151': 'HG00336', 'ind150': 'HG00335', 'ind153': 'HG00338', 'ind152': 'HG00337', 'ind155': 'HG00341', 'ind104': 'HG00185', 'ind157': 'HG00343', 'ind156': 'HG00342', 'ind105': 'HG00186', 'ind28': 'HG00123', 'ind29': 'HG00124', 'ind24': 'HG00119', 'ind25': 'HG00120', 'ind26': 'HG00121', 'ind27': 'HG00122', 'ind20': 'HG00114', 'ind21': 'HG00116', 'ind22': 'HG00117', 'ind23': 'HG00118', 'ind5': 'HG00096', 'ind226': 'NA12154', 'ind7': 'HG00099', 'ind6': 'HG00097', 'ind223': 'NA12046', 'ind100': 'HG00179', 'ind221': 'NA12044', 'ind220': 'NA12043', 'ind101': 'HG00180', 'ind9': 'HG00101', 'ind8': 'HG00100', 'ind229': 'NA12272', 'ind228': 'NA12249', 'ind227': 'NA12155', 'ind225': 'NA12144', 'ind59': 'HG00160', 'ind58': 'HG00159', 'ind224': 'NA12058', 'ind108': 'HG00189', 'ind217': 'NA12003', 'ind51': 'HG00150', 'ind50': 'HG00149', 'ind53': 'HG00152', 'ind52': 'HG00151', 'ind55': 'HG00155', 'ind54': 'HG00154', 'ind57': 'HG00158', 'ind56': 'HG00156', 'ind252': 'NA12750', 'ind253': 'NA12751', 'ind250': 'NA12748', 'ind215': 'NA11994', 'ind256': 'NA12775', 'ind257': 'NA12777', 'ind254': 'NA12761', 'ind255': 'NA12763', 'ind212': 'NA11933', 'ind258': 'NA12778', 'ind259': 'NA12812', 'ind213': 'NA11992', 'ind263': 'NA12829', 'ind210': 'NA11931', 'ind211': 'NA11932'}
	population = 'NWEUR'




count_error = 0
count_no_haplos_found = 0
for line in inf:
	#l = line.split()
	l = line.split()
	chr = input_name.split('.')[3]
	if (chr[-1] == 'a' or chr[-1] == 'b'):
		chr_no = chr[:-1]
	else:
		chr_no = chr
	start = l[1]
	end = l[2]
	#wind = l[-1]

	Sscore_l = l[5].split(';')
	length_l = l[8].split(';')
	run_l = l[9].split(';')
	no_snp_l = l[11].split(';')
	wind_l = l[-1].split(';')
	
	sample_size = l[7]
	
	ind_l = l[6].split(';')
	real_ind_l = []
	for ind in ind_l:
		real_ind = pop_d[ind]
		real_ind_l.append(real_ind)
	
	#print ind_l, len(ind_l), real_ind_l, len(real_ind_l) 
	
	SNPs = l[10].split(';')
	SNPs_l = []
	SNPs_l_no_dupl = []
	for i,snps in enumerate(SNPs):
		ind_snps_l = snps.split(',')
		SNPs_l.append(ind_snps_l[::-1])
		for snp in ind_snps_l:
			if int(snp) not in SNPs_l_no_dupl:
				SNPs_l_no_dupl.append(int(snp)) 
	SNPs_l_no_dupl.sort()
	#print  'SNPs_l: ', SNPs_l, len(SNPs_l)
	#print 'snps no duplicate list and total number of snps detected ', SNPs_l_no_dupl, 'total number of snps: ', len(SNPs_l_no_dupl), 'in these windows: ', wind_l 
	
	haplo1_l_list = []
	haplo2_l_list = []
	for ind in real_ind_l:
		haplo1_l_list.append([])
		haplo2_l_list.append([])

	count_snp_match = 0

	inf2 = open(inputfile2, 'r')
	for line2 in inf2:
		l2 = line2.split()
		if l2[0] == '#CHROM':
			col_id_l = []
			#print real_ind_l, len(real_ind_l) 
			for REAL_IND in real_ind_l:
				col_id_l.append(l2.index(REAL_IND))				
			#print col_id_l, len(col_id_l)
		if not l2[0].startswith('#'):
			snp2 = l2[1]
			ref2 = l2[3]
			alt2 = l2[4]
			pass_nopass = l2[6]
			if (int(snp2) in SNPs_l_no_dupl) and (len(ref2) == 1) and (len(alt2) == 1) and (pass_nopass == 'PASS'):
				count_snp_match += 1
				for i,ind_snp_list in enumerate(SNPs_l):
					if snp2 in ind_snp_list:
						#print 'match in snps at this pos: ', chr, snp2,  'total match: ', count_snp_match, 'in these windows: ', wind_l, 'for this individual: ', real_ind_l[i] 
						col_id =  col_id_l[i]
						geno = l2[col_id].split('|')
						haplo1 = geno[0]
						haplo2 = geno[1]
						haplo1_l_list[i].append(haplo1)
						haplo2_l_list[i].append(haplo2)								
			elif int(snp2) > int(SNPs_l_no_dupl[-1]):
				break
	inf2.close()

	#print 'haplotype 1 list: ', haplo1_l_list, 'in these windows: ', wind_l, 'for these individuals: ', real_ind_l
	#print 'haplotype 2 list: ', haplo2_l_list, 'in these windows: ', wind_l, 'for these individuals: ', real_ind_l

	ratio_derived_l_haplos1 = []
	for haplo1_list in haplo1_l_list:
		try:
			ratio_derived = float(haplo1_list.count('1'))/len(haplo1_list)
			ratio_derived_l_haplos1.append(ratio_derived)
			#print 'ratio of derived alleles in haplotype 1: ', ratio_derived, chr, start, end, haplo1_list
		except ZeroDivisionError:
			print 'ZeroDivisionError in haplotype 1: ', haplo1_list, 'line: ', line
			ratio_derived_l_haplos1.append('NA')
			pass 

	ratio_derived_l_haplos2 = []
	for haplo2_list in haplo2_l_list:
		try:
			ratio_derived = float(haplo2_list.count('1'))/len(haplo2_list)
			ratio_derived_l_haplos2.append(ratio_derived)
			#print 'ratio of derived alleles in haplotype 2: ', ratio_derived, chr, start, end, haplo2_list
		except ZeroDivisionError:
			print 'ZeroDivisionError in haplotype 2: ', haplo2_list, 'line: ', line
			ratio_derived_l_haplos2.append('NA')
			pass 

	new_ind_l = []
	ratio_derived_list = []
	for i,e in enumerate(ratio_derived_l_haplos1):
		if str(e) != 'NA':
			if e >= 0.5:
				ind_hapl1 = real_ind_l[i] + '_' + 'haplo1'
			else:
				ind_hapl1 = 'None'
		else: 
			ind_hapl1 = 'None'
		if str(ratio_derived_l_haplos2[i]) != 'NA':
			if ratio_derived_l_haplos2[i] >= 0.5:
				ind_hapl2 = real_ind_l[i] + '_' + 'haplo2'
			else:
				ind_hapl2 = 'None'
		else: 
			ind_hapl2 = 'None'
		
		new_ind = ind_hapl1 + ',' + ind_hapl2
		new_ind_l.append(new_ind)
		ratio_derived_ind = str(e) + ',' + str(ratio_derived_l_haplos2[i]) 
		ratio_derived_list.append(ratio_derived_ind)
	


	new_ind_l2 = []
	indices_to_remove = []
	for i,new_ind in enumerate(new_ind_l): 
		if new_ind == 'None,None':
			print 'no derived allele!!!',ratio_derived_list[i]
			for j in ratio_derived_list[i].split(','):
				try:
					if float(j) >= 0.5:
						count_error += 1
						print ratio_derived_list[i], new_ind, start, end					
				except ValueError:
					pass
			indices_to_remove.append(i)
		else:
			new_ind2 = new_ind.split(',')
			for IND in new_ind2:
				if IND != 'None':  
					new_ind_l2.append(IND)
	

	Sscore_l2 = []
	length_l2 = []
	run_l2 = []
	no_snp_l2 = []
	wind_l2 = []
	SNPs_l2 = []
	ratio_derived_list2 = []	
	for i in range(len(Sscore_l)):
		if i not in indices_to_remove:
			Sscore_l2.append(Sscore_l[i])
			length_l2.append(length_l[i])
			run_l2.append(run_l[i])
			no_snp_l2.append(no_snp_l[i])
			wind_l2.append(wind_l[i])
			SNPs_l2.append(SNPs_l[i])
			ratio_derived_list2.append(ratio_derived_list[i])
			
		
	new_inds = ';'.join(new_ind_l2)
	ratio_derived_snps_per_haplo = ';'.join(ratio_derived_list2)
	
	indices_to_remove_snps = []
	for i,SNP in enumerate(SNPs_l_no_dupl):
		check = 0
		for ind_snp_l in SNPs_l2:
			if str(SNP) in ind_snp_l:
				check = 1
		if check == 0:
			indices_to_remove_snps.append(i)

	SNPs_l_no_dupl2 = []
	for i in range(len(SNPs_l_no_dupl)):
		if i not in indices_to_remove_snps:
			SNPs_l_no_dupl2.append(SNPs_l_no_dupl[i])
	
	try:
		no_snps = len(SNPs_l_no_dupl2)
	
		new_start_snp = SNPs_l_no_dupl2[0]
		new_end_snp = SNPs_l_no_dupl2[-1]	
		new_length = str(new_end_snp - new_start_snp)

		SNPs_l_no_dupl_str = [str(x) for x in SNPs_l_no_dupl2 ]	
	
		new_sample_size = len(set(new_ind_l2))
	except IndexError:
		print 'no snp left in SNPs_l_no_dupl2: ', SNPs_l_no_dupl2, 'new_inds: ', new_inds, 'ratio_derived_snps_per_haplo: ', ratio_derived_snps_per_haplo, 'Sscore_l2: ', Sscore_l2, 'length_l2: ', length_l2, 'run_l2: ', run_l2, 'no_snp_l2: ', no_snp_l2, 'wind_l2: ', wind_l2, 'SNPs_l2: ', SNPs_l2, 'line: ', line
		#outf2.write(line)
		count_no_haplos_found += 1	
		continue
		
	new_single_nucl_poly_list = []
	for ind_snp_l in SNPs_l2:
		IND_SNPs = ','.join(ind_snp_l)
		new_single_nucl_poly_list.append(IND_SNPs)
			
	new_single_nucl_polys = ';'.join(new_single_nucl_poly_list)
	
	
	if 'haplo' in new_inds:
		CHR_no = [ 'chr' + chr_no ]
		NEW_start_snp = [ str(new_start_snp) ]
		NEW_end_snp = [ str(new_end_snp) ]
		POP = [ population ]
		NEW_length = [ new_length ]
		SSCORE_l = [ ';'.join(Sscore_l2) ]
		NEW_inds = [ new_inds ]
		RATIO_derived_snps_per_haplo = [ ratio_derived_snps_per_haplo ]
		NEW_sample_size = [ str(new_sample_size) ]
		LENGTH_l = [ ';'.join(length_l2) ]
		RUN_l = [ ';'.join(run_l2) ]
		NEW_single_nucl_polys = [ new_single_nucl_polys ] 
		Snps = [ ','.join(SNPs_l_no_dupl_str) ]
		NO_snp_l = [ ';'.join(no_snp_l2) ]
		NO_snps = [ str(no_snps) ]
		WIND_l = [ ';'.join(wind_l2) ]
	 	print >>outf, '\t'.join(CHR_no + NEW_start_snp + NEW_end_snp + POP + NEW_length + SSCORE_l + NEW_inds + RATIO_derived_snps_per_haplo + NEW_sample_size + LENGTH_l + RUN_l + NEW_single_nucl_polys + Snps + NO_snp_l + NO_snps + WIND_l)


		
		
		
		
		

inf.close()
outf.close()	
print count_error	
print count_no_haplos_found
