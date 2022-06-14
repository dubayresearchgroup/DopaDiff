#!/bin/bash

# Place this shell file in the system folder.

###############################

###############################

rm log.lammps *.slurm
mv slurm*.out log.lammps
rm 3_*_npt_*.sh