color Display Background white
color Labels Bonds black
axes location Off
material change opacity Transparent 0.75
display nearclip set 0.01

set carbon_top 2482
topo readlammpsdata DA/CNT10a_ext/npt/DA_CNT10a_ext.data

unset -nocomplain trajfiles
for { set i 0}  {$i < 10} {incr i} {
	puts ${i}
	lappend trajfiles DA/CNT10a_ext/nvt/${i}/nvt.lammpstrj;
}
foreach traj $trajfiles {
	mol addfile "$traj";
}

######################################
set id [molinfo top]
animate delete  beg 0 end 0 skip 0 $id
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

color Name C gray
color Name O red
color Name N blue
color Name H white

pbc wrap -compound res -all
display resize 3840 2160
display resetview
display projection Orthographic
######################################

# Fig 7(a).
animate goto 9643

#mol showperiodic 0 4
#mol numperiodic 0 4 1

mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 5 of index 8 20 21) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id


display resetview
rotate z by 50; rotate z by 90;
scale by 9
translate by 0 0 1

display depthcue on
display cuedensity 0.12


render POV3 fig_7a.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

######################################
mol delrep 5 $id

# Fig 7(b).
animate goto 8028

#mol showperiodic 0 4
#mol numperiodic 0 4 1

mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 5 of index 8 20 21) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id


display resetview
rotate z by -180;  rotate z by 90;
scale by 9
translate by 0 -0 3

display depthcue on
display cuedensity 0.12

render POV3 fig_7b.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

######################################
mol delrep 5 $id

# Fig 7(c).

animate goto 8886

#mol showperiodic 0 4
#mol numperiodic 0 4 1

mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 5 of index 8 20 21) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id


display resetview
rotate z by 150;  rotate z by 90;
scale by 9
translate by 0 0 -5

display depthcue on
display cuedensity 0.12


render POV3 fig_7c.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

# after idle {mol delrep 5 $id}

























#display resetview
display depthcue on
display cuedensity 0.12
set id [molinfo top]

# Fig 7(a) series.
mol delrep 5 $id
animate goto 3497
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7a1.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 4746
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7a2.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 433
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7a3.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 3115
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7a4.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 4938
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7a5.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 3377
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7a6.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 1598
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7a7.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 4973
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7a8.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

# Fig 7(b) series.
mol delrep 5 $id
animate goto 603
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7b1.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 2539
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7b2.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 2188
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7b3.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 1318
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7b4.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 1905
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7b5.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 1815
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7b6.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 1369
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7b7.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 1940
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7b8.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

# Fig 7(c) series.
mol delrep 5 $id
animate goto 484
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7c1.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 3900
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7c2.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 4656
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7c3.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 792
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7c4.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 726
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7c5.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 2273
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7c6.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 187
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7c7.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT

mol delrep 5 $id
animate goto 101
mol color Name
mol representation CPK 1.0 0.4 100 100
mol selection same residue as (within 4 of index 8) and (index [expr $carbon_top + 1] to 9999)
mol material Opaque
mol addrep $id
render POV3 fig_7c8.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT