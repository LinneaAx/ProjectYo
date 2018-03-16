cd ../fastas/predict/
for file in *.fasta
do 
echo $file
psiblast -query $file -evalue 0.001 -db /home/u2365/uniprot_sprot.fasta -num_iterations 3 -out_ascii_pssm /home/u2365/ProjectYo/psiblast/pssms/to_predict/$file -num_threads=8
done
cd ../pssms/to_predict/
for file in *.fasta
python3 pssm_predict.py $file
done



