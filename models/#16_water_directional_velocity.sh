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
rm water_*_directional_velocity.py

# 2， MSD & VACF computation.
if [[ ${surface_category} == "G" ]]; then
    cp $HOME/Desktop/analysis/water_distn/water_z_directional_velocity.py .
elif [[ ${surface_category} == "CNT" ]]; then
    cp $HOME/Desktop/analysis/water_distn/water_r_directional_velocity.py .
elif [[ ${surface_category} == "graphene3" ]]; then
    cp $HOME/Desktop/analysis/water_distn/water_graphene3_directional_velocity.py .
fi
python water_*_directional_velocity.py

# 3. File cleanup.
rm water_*_directional_velocity.py
if [ ! -d $HOME/Desktop/images ]; then
    mkdir $HOME/Desktop/images
fi
if [ ! -d $HOME/Desktop/images/water_directional_velocity ]; then
    mkdir $HOME/Desktop/images/water_directional_velocity
fi
mv water_directional_velocity.png $HOME/Desktop/images/water_directional_velocity/${system}.png
# mv water_*_stats.tex $HOME/Desktop/images/water_z_distn/${system}.tex
cd ..
rm 16_water_directional_velocity.sh