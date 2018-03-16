#Changed in an attempt to make a bash script that predicts by taking in seq id, blasting etc. Not finished. 

echo Dear user, to predict, please input a 2 line fasta with sequence that you want to predict the topology. The code requires you to have the swissprot database on your computer.

read fastafile

python3 make_separate_fasta.py $fastafile
echo fastafiles  

cd ../fastas/$fastafile/to_predict/
for file in *.fasta
do 
echo $file
psiblast -query $file -evalue 0.001 -db ../../uniprot_sprot.fasta -num_iterations 3 -out_ascii_pssm ../../../pssms/to_predict/$file -num_threads=8
done
cd ../pssms/to_predict/
for file in *.fasta
python3 pssm_predict.py $file
done






