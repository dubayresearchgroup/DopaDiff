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
# MacOS BSD sed.

# 1. Initialization.
rm -rf nvt
mkdir nvt

# 2. Find closest frames.
cd npt
rm box_sizes.txt
cp $HOME/Desktop/analysis/during_simulation/${surface_category}.npt.py .
python ${surface_category}.npt.py
rm ${surface_category}.npt.py

# 3. File copy.
export MODEL_DIR="$HOME/Desktop/models"
cd ../nvt

cp ../npt/*.in* .
rm *.in
cp ../moltemplate_files/*.in .
sed -i '' 's/read_data.*data"/read_restart restart.*.dopa/g' *.in
cat $MODEL_DIR/scripts/adsorbates/script_${adsorbate}.in >> *.in
cat $MODEL_DIR/scripts/surfaces/${surface_category}.nvt >> *.in


# 4. File separation.
i=0
for restartfile in restart.*.dopa; do
    mkdir $i
    mv ${restartfile} $i
    cp *.in* $HOME/Desktop/standard.slurm $i
    i=$((i+1))
done

rm *.in*
#cp $MODEL_DIR/5_sbatch\(Rivann\).sh .
cd ..
rm 4_nvt.sh