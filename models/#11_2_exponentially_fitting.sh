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
rm exponential_fitting.py

# 2， MSD & VACF computation.
cp $HOME/Desktop/analysis/fitting/exponential_fitting.py .
python exponential_fitting.py

# 3. File cleanup.
rm exponential_fitting.py
mv 1_exponential_fitting.png $HOME/Desktop/images/individual_exponential_fitting/${system}.png
mv tex_stats.tex $HOME/Desktop/images/tex_exponential_fitting/${system}.tex
cd ..
rm 11_exponential_fitting.sh

