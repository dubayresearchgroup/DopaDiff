######################################
# structure_dependency.tcl Revision 1.0 [07-10-2020]
#
# Changelog:
# V1.0 [07-10-2020]
# Initial commit. For the thesis Fig. 1.1.
######################################

# logfile console

# 1. Display initialization
color Display Background white
color Labels Bonds black
axes location Off
material change opacity Transparent 0.60
display nearclip set 0.01
display resize 3840 2160

set datafiles {};
set trajfiles {};
foreach i {graphene CNT10a_ext groove} {
	lappend datafiles DA/$i/npt/DA_$i.data;
	lappend trajfiles DA/$i/npt/npt.lammpstrj;
}
set trajfiles [lreplace ${trajfiles} end end DA/groove/nvt/0/nvt.lammpstrj]

foreach file $datafiles traj $trajfiles \
		carbon_top {3702 2482 4942} {
	topo readlammpsdata "$file";
	mol addfile "$traj";
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

}

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

# Fig 1.1(a).
after idle {
	mol top 0
	mol on 0
	mol off 1
	mol off 2
	animate goto 935

	display resetview
	rotate x by -75
	scale by 1.5
	# translate by 0 -1.5 0
	display depthcue on
	display cuedensity 0.32

	render POV3 fig_1a.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT
}

# Fig 1.1(b)
after idle {
	mol top 1
	mol off 0
	mol on 1
	mol off 2
	animate goto 966

	display resetview
	rotate z by -90; rotate x by 10; rotate y by -10;
	scale by 1.5
	# translate by 0 -1.5 0
	display depthcue on
	display cuedensity 0.32

	render POV3 fig_1b.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT
}

# Fig 1.1(c)
after idle {
	mol top 2
	mol off 0
	mol off 1
	mol on 2
	animate goto 917

	display resetview
	rotate z by -180; rotate x by 10; rotate y by -10;
	scale by 1.5
	# translate by 0 -1.5 0
	display depthcue on
	display cuedensity 0.32

	render POV3 fig_1c.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT
}