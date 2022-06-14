#!/bin/bash

for i in {0..9}
do
    cd $i
    rm *.slurm log.lammps slurm-*.out
    cd ..
done
rm 6_*_nvt_*.sh
