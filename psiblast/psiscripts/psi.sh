cd ../fastas/
for file in *.fasta
do 
echo $file
psiblast -query $file -evalue 0.001 -db /home/u2365/uniprot_sprot.fasta -num_iterations 3 -out_ascii_pssm /home/u2365/ProjectYo/psiblast/pssms/$file -num_threads=8
done
