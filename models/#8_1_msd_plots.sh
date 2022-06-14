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

if [[ ${surface} == *"CNT"* ]]; then
    surface_category="CNT"
elif [[ ${surface} == "graphene" ]]; then 
    surface_category="G"
elif [[ ${surface} == *"groove"* ]]; then
    surface_category="G"
elif [[ ${surface} == "graphene3" ]]; then
    surface_category="G"
else exit 1
fi

# 1. Initialization.
cd nvt
rm msd_plots.${surface_category}.py

# 2， MSD & VACF computation.
cp $HOME/Desktop/analysis/plotting/msd_plots.${surface_category}.py .
python msd_plots.${surface_category}.py

# 3. File cleanup.
rm msd_plots.${surface_category}.py
if [ ! -d $HOME/Desktop/images ]; then
    mkdir $HOME/Desktop/images
fi
if [ ! -d $HOME/Desktop/images/individual_msd ]; then
    mkdir $HOME/Desktop/images/individual_msd
fi
mv 1_msd_plot.png $HOME/Desktop/images/individual_msd/${system}.png
cd ..
rm 8_1_msd_plots.sh
