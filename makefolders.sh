#Shell script that opens a "linneas_project_(and some addition name given as an argument)" 
#directory with the subdirectories scripts, bash, input, output, logs

chmod +x makefolders.sh

#mkdir /home/users/u2365/Desktop/projects I already have this folder
mkdir {/home/users/u2365/Desktop/projects/linneas_project_"$@1"}/{scripts, bash, input, output, logs}

