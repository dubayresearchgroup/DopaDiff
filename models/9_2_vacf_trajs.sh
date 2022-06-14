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
rm vacf_trajs.py 1_1_vacf_trajs.png

# 2， MSD & VACF computation.
cp $HOME/Desktop/analysis/plotting/vacf_trajs.py .
python vacf_trajs.py

# 3. File cleanup.
rm vacf_trajs.py
if [ ! -d $HOME/Desktop/images ]; then
    mkdir $HOME/Desktop/images
fi
if [ ! -d $HOME/Desktop/images/individual_vacf_traj ]; then
    mkdir $HOME/Desktop/images/individual_vacf_traj
    mkdir $HOME/Desktop/images/individual_vacf_traj/raw
    mkdir $HOME/Desktop/images/individual_vacf_traj/transformed
fi

for k in x y z; do
mv 1_1_vacf_trajs_raw_${k}.png $HOME/Desktop/images/individual_vacf_traj/raw/${system}_trajs_${k}.png
mv 1_1_vacf_trajs_transformed_${k}.png $HOME/Desktop/images/individual_vacf_traj/transformed/${system}_trajs_${k}.png
done

cd ..
rm 9_2_vacf_trajs.sh

