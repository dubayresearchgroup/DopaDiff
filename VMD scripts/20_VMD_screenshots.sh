#!/bin/bash

###############################
adsorbate=`cut -d'/' -f5 <<< "$(pwd)"`
surface=`cut -d'/' -f6 <<< "$(pwd)"`
system="${adsorbate}_${surface}"
surface=`cut -d'_' -f1 <<< ${surface}`

if [[ ${surface} == *"CNT"* ]]; then
    surface_category="CNT"
elif [[ ${surface} == *"graphene"* ]]; then 
    surface_category="G"
elif [[ ${surface} == *"BNNT"* ]]; then
    surface_category="BNNT"
elif [[ ${surface} == *"boronnitride"* ]]; then 
    surface_category="BN"
else exit 1
fi
###############################

# 1. Initialization.
cd nvt
rm vmd_number_of_frames.${surface_category}.py output.txt

# 2， MSD & VACF computation.
cp $HOME/Desktop/analysis/moieties_z_distn/vmd_number_of_frames.${surface_category}.py .
python vmd_number_of_frames.${surface_category}.py

# 3. File cleanup.
rm vmd_number_of_frames.${surface_category}.py
if [ ! -d $HOME/Desktop/images ]; then
    mkdir $HOME/Desktop/images
fi
if [ ! -d $HOME/Desktop/images/conf_snapshots ]; then
    mkdir $HOME/Desktop/images/conf_snapshots
fi
mv output.txt $HOME/Desktop/images/conf_snapshots/${system}.txt
cd ..
rm 20_VMD_screenshots.sh