# 1. Display initialization
color Display Background white
axes location Off
material change opacity Transparent 0.75
display nearclip set 0.01
display resize 3840 2160

set datafiles {};
set trajfiles {};
foreach i {graphene CNT10a_int CNT10a_ext CNT15a_int CNT15a_ext CNT20a_int CNT20a_ext} {
	lappend datafiles DA/$i/npt/DA_$i.data;
	lappend trajfiles DA/$i/nvt/0/nvt.lammpstrj;
}

#{621 621 901 1181 1181 901 621}
#{3702 2482 2482 3630 3630 4778 4778}

foreach file $datafiles traj $trajfiles \
		carbon_top {3702 2482 2482 3630 3630 4778 4778} {
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


##########################################
set id_list [molinfo list]
foreach id $id_list {
	mol top $id
	animate delete  beg 0 end 0 skip 0 $id
	pbc wrap -compound res -all;
	
	#pbc box;
	#mol showperiodic $id 1 Z
	#mol numperiodic $id 1 1
}

foreach id $id_list {
	mol off $id
}

# Fig 2.2(a).
after idle {
	mol top 0
	mol on 0
	animate goto 796

	display resetview
	rotate x by -75
	scale by 1.5
	# translate by 0 -1.5 0
	display depthcue on
	display cuedensity 0.32

	render POV3 fig_2a.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

	foreach id $id_list {
	mol off $id
	}
}

# Fig 2.2(b).
after idle {
	mol top 1
	mol on 1
	animate goto 683

	display resetview
	rotate z by 135; rotate x by 5; rotate y by -5;
	scale by 1.5
	# translate by 0 0 -0.5
	display depthcue on
	display cuedensity 0.32

	render POV3 fig_2b.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

	display resetview
	foreach id $id_list {
	mol off $id
	}
}

# Fig 2.2(c).
after idle {
	mol top 2
	mol on 2
	animate goto 115

	#display resetview
	rotate z by 120; rotate x by 5; rotate y by -5;
	scale by 1.5
	# translate by 0 0 -0.5
	display depthcue on
	display cuedensity 0.32

	render POV3 fig_2c.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

	foreach id $id_list {
	mol off $id
	}
}


# Fig 2.2(d).
after idle {
	mol top 3
	mol on 3
	animate goto 29

	display resetview
	rotate z by -105; rotate x by 7; rotate y by -7;
	scale by 1.5
	# translate by 0 0 -0.5
	display depthcue on
	display cuedensity 0.32

	render POV3 fig_2d.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

	display resetview
	foreach id $id_list {
	mol off $id
	}
}

# Fig 2.2(e).
after idle {
	mol top 4
	mol on 4
	animate goto 710

	#display resetview
	rotate z by 45; rotate x by 7; rotate y by -7;
	scale by 1.5
	# translate by 0 0 -0.5
	display depthcue on
	display cuedensity 0.32

	render POV3 fig_2e.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

	foreach id $id_list {
	mol off $id
	}
}

# Fig 2.2(f).
after idle {
	mol top 5
	mol on 5
	animate goto 29

	display resetview
	rotate z by 75; rotate x by 9; rotate y by -9;
	scale by 1.5
	# translate by 0 0 -0.5
	display depthcue on
	display cuedensity 0.32

	render POV3 fig_2f.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

	display resetview
	foreach id $id_list {
	mol off $id
	}
}

# Fig 2.2(g).
after idle {
	mol top 6
	mol on 6
	animate goto 209

	#display resetview
	rotate y by 180;
	rotate z by -75; rotate x by 9; rotate y by -9;
	scale by 1.5
	# translate by 0 0 -0.5
	display depthcue on
	display cuedensity 0.32

	render POV3 fig_2g.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

	foreach id $id_list {
	mol off $id
	}
}