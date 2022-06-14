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
rm water_com_distn_plots.${surface_category}.py 3_water_com_distn_plot.png 3_waterO_com_distn_plot.png

# 2， MSD & VACF computation.
cp $HOME/Desktop/analysis/water_distn/water_com_distn_plots.${surface_category}.py .
python water_com_distn_plots.${surface_category}.py

# 3. File cleanup.
rm water_com_distn_plots.${surface_category}.py
if [ ! -d $HOME/Desktop/images ]; then
    mkdir $HOME/Desktop/images
fi
if [ ! -d $HOME/Desktop/images/water_com_distn ]; then
    mkdir $HOME/Desktop/images/water_com_distn
fi
mv 3_water_com_distn_plot.png $HOME/Desktop/images/water_com_distn/water_${system}.png
mv 3_waterO_com_distn_plot.png $HOME/Desktop/images/water_com_distn/waterO_${system}.png
cd ..
rm 18_water_com_distn_plots.sh

