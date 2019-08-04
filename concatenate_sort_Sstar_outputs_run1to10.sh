#EA - path = /gpfs/scratch/recepozg/sstar/ea
for i in {9..22};
do echo $i;
cat ./run1/inputfile_ea.chr.${i}.bed ./run2/inputfile_ea.chr.${i}.bed ./run3/inputfile_ea.chr.${i}.bed ./run4/inputfile_ea.chr.${i}.bed ./run5/inputfile_ea.chr.${i}.bed ./run6/inputfile_ea.chr.${i}.bed ./run7/inputfile_ea.chr.${i}.bed ./run8/inputfile_ea.chr.${i}.bed ./run9/inputfile_ea.chr.${i}.bed ./run10/inputfile_ea.chr.${i}.bed | sort -k1,1 -k2,2n -k11,11n - > ./runs_merged/inputfile_ea.chr.${i}.run1_10.sorted.bed;
done

for i in {1..8};
do echo $i;
cat ./run1/inputfile_ea.chr.${i}a.bed ./run2/inputfile_ea.chr.${i}a.bed ./run3/inputfile_ea.chr.${i}a.bed ./run4/inputfile_ea.chr.${i}a.bed ./run5/inputfile_ea.chr.${i}a.bed ./run6/inputfile_ea.chr.${i}a.bed ./run7/inputfile_ea.chr.${i}a.bed ./run8/inputfile_ea.chr.${i}a.bed ./run9/inputfile_ea.chr.${i}a.bed ./run10/inputfile_ea.chr.${i}a.bed  | sort -k1,1 -k2,2n -k11,11n - > ./runs_merged/inputfile_ea.chr.${i}a.run1_10.sorted.bed;
cat ./run1/inputfile_ea.chr.${i}b.bed ./run2/inputfile_ea.chr.${i}b.bed ./run3/inputfile_ea.chr.${i}b.bed ./run4/inputfile_ea.chr.${i}b.bed ./run5/inputfile_ea.chr.${i}b.bed ./run6/inputfile_ea.chr.${i}b.bed ./run7/inputfile_ea.chr.${i}b.bed ./run8/inputfile_ea.chr.${i}b.bed ./run9/inputfile_ea.chr.${i}b.bed ./run10/inputfile_ea.chr.${i}b.bed  | sort -k1,1 -k2,2n -k11,11n - > ./runs_merged/inputfile_ea.chr.${i}b.run1_10.sorted.bed;
done


#WE - path = /gpfs/scratch/recepozg/sstar/we
for i in {9..22};
do echo $i;
cat ./run1/inputfile_we.chr.${i}.bed ./run2/inputfile_we.chr.${i}.bed ./run3/inputfile_we.chr.${i}.bed ./run4/inputfile_we.chr.${i}.bed ./run5/inputfile_we.chr.${i}.bed ./run6/inputfile_we.chr.${i}.bed ./run7/inputfile_we.chr.${i}.bed ./run8/inputfile_we.chr.${i}.bed ./run9/inputfile_we.chr.${i}.bed ./run10/inputfile_we.chr.${i}.bed | sort -k1,1 -k2,2n -k11,11n - > ./runs_merged/inputfile_we.chr.${i}.run1_10.sorted.bed;
done

for i in {1..8};
do echo $i;
cat ./run1/inputfile_we.chr.${i}a.bed ./run2/inputfile_we.chr.${i}a.bed ./run3/inputfile_we.chr.${i}a.bed ./run4/inputfile_we.chr.${i}a.bed ./run5/inputfile_we.chr.${i}a.bed ./run6/inputfile_we.chr.${i}a.bed ./run7/inputfile_we.chr.${i}a.bed ./run8/inputfile_we.chr.${i}a.bed ./run9/inputfile_we.chr.${i}a.bed ./run10/inputfile_we.chr.${i}a.bed  | sort -k1,1 -k2,2n -k11,11n - > ./runs_merged/inputfile_we.chr.${i}a.run1_10.sorted.bed;
cat ./run1/inputfile_we.chr.${i}b.bed ./run2/inputfile_we.chr.${i}b.bed ./run3/inputfile_we.chr.${i}b.bed ./run4/inputfile_we.chr.${i}b.bed ./run5/inputfile_we.chr.${i}b.bed ./run6/inputfile_we.chr.${i}b.bed ./run7/inputfile_we.chr.${i}b.bed ./run8/inputfile_we.chr.${i}b.bed ./run9/inputfile_we.chr.${i}b.bed ./run10/inputfile_we.chr.${i}b.bed  | sort -k1,1 -k2,2n -k11,11n - > ./runs_merged/inputfile_we.chr.${i}b.run1_10.sorted.bed;
done
