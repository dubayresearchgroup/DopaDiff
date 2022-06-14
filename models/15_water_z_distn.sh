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
rm water_*_distn.py water_*_plot.py

# 2， MSD & VACF computation.
if [[ ${surface_category} == "G" ]]; then
    cp $HOME/Desktop/analysis/moieties_z_distn/water_z_distn.py .
    cp $HOME/Desktop/analysis/moieties_z_distn/water_z_plot.py .
elif [[ ${surface_category} == "CNT" ]]; then
    cp $HOME/Desktop/analysis/moieties_z_distn/water_r_distn.py .
    cp $HOME/Desktop/analysis/moieties_z_distn/water_r_plot.py .
elif [[ ${surface_category} == "graphene3" ]]; then
    cp $HOME/Desktop/analysis/moieties_z_distn/water_graphene3_distn.py .
    cp $HOME/Desktop/analysis/moieties_z_distn/water_graphene3_plot.py .
fi
python water_*_distn.py 
python water_*_plot.py

# 3. File cleanup.
rm water_*_distn.py water_*_plot.py
if [ ! -d $HOME/Desktop/images ]; then
    mkdir $HOME/Desktop/images
fi
if [ ! -d $HOME/Desktop/images/water_z_distn ]; then
    mkdir $HOME/Desktop/images/water_z_distn
fi
mv water_*_distn.png $HOME/Desktop/images/water_z_distn/${system}.png
# mv water_*_stats.tex $HOME/Desktop/images/water_z_distn/${system}.tex
cd ..
rm 15_water_z_distn.sh