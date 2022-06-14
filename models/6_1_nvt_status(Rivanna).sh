#!/bin/bash

# Place this shell file in the system folder.

###############################

###############################

for dir in {0..9}; do 
tail -1 ${dir}/slurm*.out
done