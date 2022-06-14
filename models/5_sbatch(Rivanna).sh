#!/bin/bash

for i in {0..9}
do
    cd $i
    sbatch *.slurm
    cd ..
done
rm 5_sbatch\(Rivanna\).sh