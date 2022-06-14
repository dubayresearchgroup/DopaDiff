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
rm moieties_com_distn.${surface_category}.py

# 2， MSD & VACF computation.
cp $HOME/Desktop/analysis/plotting/moieties_com_distn.${surface_category}.py .
python moieties_com_distn.${surface_category}.py

# 3. File cleanup.
rm moieties_com_distn.${surface_category}.py
if [ ! -d $HOME/Desktop/images ]; then
    mkdir $HOME/Desktop/images
fi
if [ ! -d $HOME/Desktop/images/moieties_com_distn ]; then
    mkdir $HOME/Desktop/images/moieties_com_distn
fi
mv 3_amine_com_distn.png $HOME/Desktop/images/moieties_com_distn/${system}_amine.png
mv 3_ring_com_distn.png $HOME/Desktop/images/moieties_com_distn/${system}_ring.png
mv 3_quinone_com_distn.png $HOME/Desktop/images/moieties_com_distn/${system}_quinone.png
cd ..
rm 14_1_moieties_com_distn.sh