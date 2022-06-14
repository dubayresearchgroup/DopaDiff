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
rm msd_trajs.py 1_1_msd_trajs.png

# 2， MSD & VACF computation.
cp $HOME/Desktop/analysis/plotting/msd_trajs.py .
python msd_trajs.py

# 3. File cleanup.
rm msd_trajs.py
if [ ! -d $HOME/Desktop/images ]; then
    mkdir $HOME/Desktop/images
fi
if [ ! -d $HOME/Desktop/images/individual_msd_traj ]; then
    mkdir $HOME/Desktop/images/individual_msd_traj
fi
mv 1_1_msd_trajs_x.png $HOME/Desktop/images/individual_msd_traj/${system}_trajs_x.png
mv 1_1_msd_trajs_y.png $HOME/Desktop/images/individual_msd_traj/${system}_trajs_y.png
mv 1_1_msd_trajs_z.png $HOME/Desktop/images/individual_msd_traj/${system}_trajs_z.png
cd ..
rm 8_2_msd_trajs.sh

