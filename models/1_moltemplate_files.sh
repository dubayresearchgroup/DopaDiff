#!/bin/bash

# Place this Bash script in the system folder.

###############################
adsorbate=`cut -d'/' -f5 <<< "$(pwd)"`
surface=`cut -d'/' -f6 <<< "$(pwd)"`
system="${adsorbate}_${surface}"
surface=`cut -d'_' -f1 <<< ${surface}`
###############################

rm -rf moltemplate_files
mkdir moltemplate_files
cd moltemplate_files

# 1. Initialization.
rm -rf output_ttree
rm -rf oplsaa_lt_generator
rm *.data *.in*

# 2. File copy.
export MODEL_DIR="$HOME/Desktop/models"
if [ ! -d ${MODEL_DIR} ] 
then
    echo "Error: Directory MODEL_DIR does not exist."
    cd ..
    return
fi

cp $MODEL_DIR/oplsaa_lt_generator/oplsaa.lt .
cp $MODEL_DIR/adsorbates/${adsorbate}.lt .
cp $MODEL_DIR/templates/TIP3P.lt .
cp $MODEL_DIR/surfaces/${surface}.lt .

# 3. Moltemplate generate.
cp $MODEL_DIR/templates/adsorbates/template_${adsorbate}.lt ${system}.lt 
if [[ ${surface} == *"CNT"* ]]; then
    side=`cut -d'_' -f3 <<< ${system}`
    cat $MODEL_DIR/templates/sides/${surface}_${side}.lt >> ${system}.lt 
fi
cat $MODEL_DIR/templates/surfaces/template_${surface}.lt >> ${system}.lt
export MOLTEMPLATE_PATH="/Users/jiaqz/miniconda3/pkgs/moltemplate-2.20.3-py310h2ec42d9_1/bin/"
bash ${MOLTEMPLATE_PATH}/moltemplate.sh ${system}.lt

# 4. File cleanup.
rm -rf output_ttree 
rm -rf oplsaa_lt_generator
rm oplsaa.lt ${adsorbate}.lt TIP3P.lt ${surface}.lt ${system}.lt

cd ..
rm 1_moltemplate_files.sh
