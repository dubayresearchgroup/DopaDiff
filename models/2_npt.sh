#!/bin/bash

# Place this shell file in the system folder.

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

rm -rf npt
mkdir npt
cd npt

# 1. Initialization.
rm -rf restarts
mkdir restarts

# 2. File copy.
cp ../moltemplate_files/*.in* ../moltemplate_files/*.data .
cp $HOME/Desktop/standard.slurm .

# 3. File editing.
export MODEL_DIR="$HOME/Desktop/models"
cat $MODEL_DIR/scripts/adsorbates/script_${adsorbate}.in >> *.in
cat $MODEL_DIR/scripts/surfaces/${surface_category}.npt >> *.in
cat $MODEL_DIR/charges/${adsorbate}.charges >> *.in.charges

# 4. File cleanup.
cd ..
rm 2_npt.sh
