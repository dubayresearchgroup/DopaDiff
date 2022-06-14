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
rm msd_dft.py 1_1_msd_dft.png tex_stats.tex

# 2， MSD & VACF computation.
cp $HOME/Desktop/analysis/plotting/msd_dft.py .
python msd_dft.py

# 3. File cleanup.
rm msd_dft.py
if [ ! -d $HOME/Desktop/images ]; then
    mkdir $HOME/Desktop/images
fi
if [ ! -d $HOME/Desktop/images/individual_msd_dft ]; then
    mkdir $HOME/Desktop/images/individual_msd_dft
fi
mv 1_1_msd_dft.png $HOME/Desktop/images/individual_msd_dft/${system}_dft.png
mv tex_stats.tex $HOME/Desktop/images/individual_msd_dft/${system}_dft.tex
cd ..
rm 8_3_msd_dft.sh

