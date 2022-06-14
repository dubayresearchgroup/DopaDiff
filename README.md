# Data for "Structure and Dynamics of Adsorbed Dopamine on Solvated Carbon Nanotubes and in a CNT Groove"

This compressed folder contains the data presented in [Structure and Dynamics of Adsorbed Dopamine on Solvated Carbon Nanotubes and in a CNT Groove](https://doi.org/10.3390/molecules27123768). DOI: https://doi.org/10.3390/molecules27123768.

## Folder Structure

- `/analysis`: contains the analysis code (mainly in Python) that the authors used.
  - Library dependencies: 

    | Package     | Version | Build           |
    | ----------- | ------- | --------------- |
    | conda       | 4.13.0  | py310hecd8cb5_0 |
    | matplotlib  | 3.5.1   | py310hecd8cb5_1 |
    | moltemplate | 2.20.3  | py310h2ec42d9_1 |
    | numpy       | 1.22.3  | py310hdcd3fac_0 |
    | pandas      | 1.4.2   | py310he9d5cce_0 |
    | pip         | 21.2.4  | py310hecd8cb5_0 |
    | python      | 3.10.4  | hdfd78df_0      |
    | scipy       | 1.7.3   | py310h3dd3380_0 |
    | sqlite      | 3.38.3  | h707629a_0      |
- `/images`: contains the raw images that were generated from the analysis. The corresponding numbered scripts can be found in the `/models` directory.
- `/manuscript`: includes the authors' manuscript in the LaTeX format.
  - Depending on the compilation environment, the compiled pdf may have different layouts than the [published version](https://doi.org/10.3390/molecules27123768).
  - The authors recommend to use [Overleaf](https://www.overleaf.com/) to compile the `/manuscript`, or [MacTeX-2020 Distribution](https://www.tug.org/mactex/) to compile locally.
- `/models`: has the LAMMPS models of adsorbates, partial charge distribution and surfaces.
  - The authors used [22 Aug 2018](https://github.com/lammps/lammps/releases/tag/stable_22Aug2018) LAMMPS stable version in the simulations.
- `/VMD scripts`: contains the VMD scripts for trajectory visualization. 
  - The authors used [VMD 1.9.4a55](https://www.ks.uiuc.edu/Research/vmd/alpha/) to build and run these `.tcl` files.

## More info

If additional clarification notes are necessary, the authors will update this compressed folder at https://github.com/QizhangJia/DopaDiff. Please check this repository for the most up-to-date README.