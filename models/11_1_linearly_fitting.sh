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
rm linearly_fitting.py 1_1_linearly_fitting.png tex_stats.tex

# 2， MSD & VACF computation.
cp $HOME/Desktop/analysis/fitting/linearly_fitting.py .
python linearly_fitting.py

# 3. File cleanup.
rm linearly_fitting.py
if [ ! -d $HOME/Desktop/images ]; then
    mkdir $HOME/Desktop/images
fi
if [ ! -d $HOME/Desktop/images/individual_linearly_fitting ]; then
    mkdir $HOME/Desktop/images/individual_linearly_fitting
fi
mv 1_1_linearly_fitting.png $HOME/Desktop/images/individual_linearly_fitting/${system}.png
mv tex_stats.tex $HOME/Desktop/images/individual_linearly_fitting/${system}.tex
cd ..
rm 11_1_linearly_fitting.sh

