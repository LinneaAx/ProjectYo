# ProjectYo
Development of a SVM predictor of membrane proteins, classifying globular, helical, inside and outside loop residues.

#TO RUN THE LinearSVC PREDICTOR
 - In scripts, run predict.py as main. Will take multiple input sequences. Provided with test example if run as main.
 - If you prefer pickle for loading the model use picklepredict.py. Will take multiple input sequences. Provided with test example if run as main. 

#TO RUN THE PSSM PREDICTOR
 - In psiblast, run pssm_predict.py. Provided with test example if run as main. 

#TO TRAIN A MODEL
 - Extraction of feature and recoding is done by parse_code.py for single windowsize or with humble_python.py for extracting and training for multiple window sizes.  
 - Training of multiple models from existing np.savez files is done by bash script train.sh which runs train_my_model.py for multiple files, saving the models.

/scripts - various scripts used to parse input, train and save models, predict using models

/data - various data files.
 - the main data set used is data/alpha_beta_globular_sp_4state.txt_split
 - The set of 50 extra proteins 

/outputfiles - various output files from optimizing and plotting 

/generated models - models using different windowsizes, default setting for LinearSVC. 


TO DO:
  - Make sure only relevant scripts are in the scripts folder.
  - Add documentation as to how to use the predictor in my Diary
  - Add shebangs in relevant scripts
  - Make sure there are path directories for outputting files, parse_code, humble_python, humble_python_predict 
  - Add argv arguments for file input for training and predicting scripts, default model for fridays deadline 
