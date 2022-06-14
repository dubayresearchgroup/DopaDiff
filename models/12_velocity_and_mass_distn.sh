#!/bin/bash

###############################
adsorbate=`cut -d'/' -f5 <<< "$(pwd)"`
surface=`cut -d'/' -f6 <<< "$(pwd)"`
system="${adsorbate}_${surface}"
surface=`cut -d'_' -f1 <<< ${surface}`

if [[ ${surface} == *"CNT"* ]]; then
    surface_category="CNT"
elif [[ ${surface} == "graphene" ]]; then 
    surface_category="G"
elif [[ ${surface} == *"BNNT"* ]]; then
    surface_category="BNNT"
elif [[ ${surface} == *"boronnitride"* ]]; then 
    surface_category="BN"
elif [[ ${surface} == *"groove"* ]]; then
    surface_category="groove"
elif [[ ${surface} == "graphene3" ]]; then
    surface_category="graphene3"
else exit 1
fi
###############################

# 1. Initialization.
cd nvt
rm velocity_and_mass_distn.${surface_category}.py velocity_and_mass_distn.png

# 2， MSD & VACF computation.
cp $HOME/Desktop/analysis/plotting/velocity_and_mass_distn.${surface_category}.py .
python velocity_and_mass_distn.${surface_category}.py

# 3. File cleanup.
rm velocity_and_mass_distn.${surface_category}.py
if [ ! -d $HOME/Desktop/images ]; then
    mkdir $HOME/Desktop/images
fi
if [ ! -d $HOME/Desktop/images/individual_rms_mass_distn ]; then
    mkdir $HOME/Desktop/images/individual_rms_mass_distn
fi
mv velocity_and_mass_distn.png $HOME/Desktop/images/individual_rms_mass_distn/${system}.png
#mv tex_stats.tex $HOME/Desktop/images/tex_exponential_fitting/${system}.tex
cd ..
rm 12_velocity_and_mass_distn.sh

