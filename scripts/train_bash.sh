cd ../splitoutput/

for file in *.txt_split_output.txt.npz
do 
echo $file
python3 ../scripts/train_my_model.py $file

done 
