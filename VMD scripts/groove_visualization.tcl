######################################
# groove_visualization.tcl
#
# Changelog:
######################################

# logfile console

# 1. Display initialization
color Display Background white
color Labels Bonds black
axes location Off
material change opacity Transparent 0.50
display nearclip set 0.01
display resize 3840 2160

set carbon_top 4942
topo readlammpsdata DA/groove/npt/DA_groove.data

unset -nocomplain trajfiles
for { set i 0}  {$i < 10} {incr i} {
	puts ${i}
	lappend trajfiles /Volumes/Backup/DopaDiff/DA/groove/nvt/${i}/nvt.lammpstrj;
}
foreach traj $trajfiles {
	mol addfile "$traj";
}

set id [molinfo top];
mol delrep 0 $id

mol color Name
mol representation CPK 1.0 0.6 100 100
mol selection index 0 to 21
mol material Opaque
mol addrep $id

mol color Name
mol representation CPK 1.6 0.6 100 100
mol selection index 0 to 7
mol material Opaque
mol addrep $id

mol color Name
mol representation CPK 1.5 0.6 100 100
mol selection index 8
mol material Opaque
mol addrep $id

mol color Name
mol representation CPK 1.4 0.6 100 100
mol selection index 9 10
mol material Opaque
mol addrep $id

mol color ColorID 2
mol representation DynamicBonds 1.6 0.3 100
mol selection index 22 to $carbon_top
mol material Transparent
mol addrep $id

# mol color Name
# mol representation Lines 2.0
# mol selection index [expr $carbon_top + 1] to 9999
# mol material Opaque
# mol addrep $id

color Name C gray
color Name O red
color Name N blue
color Name H white

######################################
# 2. Wrap the molecules according to PBC.

after idle {
	set id_list [molinfo list]
	foreach id $id_list {
		mol top $id
		pbc wrap -compound res -all;
	}
}

######################################
# 3. examine the vacuum data

# 1. Display initialization
color Display Background white
color Labels Bonds black
axes location Off
material change opacity Transparent 0.50
display nearclip set 0.01
display resize 3840 2160

set carbon_top 4942
topo readlammpsdata DA/no-water/groove/npt/DA_groove.data

unset -nocomplain trajfiles
for { set i 0}  {$i < 10} {incr i} {
	puts ${i}
	lappend trajfiles /Volumes/Backup/DopaDiff/DA/no-water/groove/nve/${i}/nvt.lammpstrj;
}
foreach traj $trajfiles {
	mol addfile "$traj";
}

set id [molinfo top];
mol delrep 0 $id

mol color Name
mol representation CPK 1.0 0.6 100 100
mol selection index 0 to 21
mol material Opaque
mol addrep $id

mol color Name
mol representation CPK 1.6 0.6 100 100
mol selection index 0 to 7
mol material Opaque
mol addrep $id

mol color Name
mol representation CPK 1.5 0.6 100 100
mol selection index 8
mol material Opaque
mol addrep $id

mol color Name
mol representation CPK 1.4 0.6 100 100
mol selection index 9 10
mol material Opaque
mol addrep $id

mol color ColorID 2
mol representation DynamicBonds 1.6 0.3 100
mol selection index 22 to $carbon_top
mol material Transparent
mol addrep $id

# mol color Name
# mol representation Lines 2.0
# mol selection index [expr $carbon_top + 1] to 9999
# mol material Opaque
# mol addrep $id

color Name C gray
color Name O red
color Name N blue
color Name H white

######################################
# 2. Wrap the molecules according to PBC.

after idle {
	set id_list [molinfo list]
	foreach id $id_list {
		mol top $id
		pbc wrap -compound res -all;
	}
}