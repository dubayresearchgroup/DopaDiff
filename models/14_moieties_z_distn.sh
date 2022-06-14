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
rm functional_groups_*_distn.py

# 2， MSD & VACF computation.
if [[ ${surface_category} == "G" ]]; then
    cp $HOME/Desktop/analysis/moieties_z_distn/functional_groups_z_distn.py .
elif [[ ${surface_category} == "CNT" ]]; then
    cp $HOME/Desktop/analysis/moieties_z_distn/functional_groups_r_distn.py .
elif [[ ${surface_category} == "graphene3" ]]; then
    cp $HOME/Desktop/analysis/moieties_z_distn/functional_groups_graphene3_distn.py .
fi
python functional_groups_*_distn.py

# 3. File cleanup.
rm functional_groups_*_distn.py
if [ ! -d $HOME/Desktop/images ]; then
    mkdir $HOME/Desktop/images
fi
if [ ! -d $HOME/Desktop/images/moieties_z_distn ]; then
    mkdir $HOME/Desktop/images/moieties_z_distn
fi
mv functional_groups_*_distn.png $HOME/Desktop/images/moieties_z_distn/${system}.png
mv functional_groups_*_stats.tex $HOME/Desktop/images/moieties_z_distn/${system}.tex
cd ..
rm 14_moieties_z_distn.sh