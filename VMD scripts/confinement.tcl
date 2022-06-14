######################################
# confinement.tcl Revision 1.0 [07-10-2020]
#
# Changelog:
# V1.0 [07-10-2020]
# Initial commit. For the thesis Fig. 1.2.
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
foreach i {CNT10a_ext} {
    lappend datafiles DA/$i/npt/DA_$i.data;
    lappend trajfiles DA/$i/npt/npt.lammpstrj;
}

foreach file $datafiles traj $trajfiles \
        carbon_top {2482} {
    topo readlammpsdata "$file";
    mol addfile "$traj";
    set id [molinfo top];
    mol delrep 0 $id

    mol color ColorID 2
    mol representation DynamicBonds 1.6 0.3 100
    mol selection index 22 to 1641
    mol material Transparent
    mol addrep $id

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

# Fig 1.2(a).
after idle {
    animate goto 1050

    mol color Name
    mol representation CPK 1.0 0.4 100 100
    mol selection same residue as (within 5 of index 22 to 1950) and (index 2483 to 4605)
    mol material Opaque
    mol addrep $id

    mol color Name
    mol representation CPK 1.0 0.4 100 100
    mol selection same residue as (not within 5 of index 22 to 2482) and (index 2483 to 4605)
    mol material Opaque
    mol addrep $id
    
    graphics $id delete all
    graphics $id materials on
    graphics $id material Transparent
    graphics $id color 0
    graphics $id cylinder {25 25 0} {25 25 82} radius 7 resolution 100 filled yes
    graphics $id color 21
    graphics $id cylinder {25 25 0} {25 25 100} radius 5 resolution 100 filled yes

    display resetview
    rotate y by 40; rotate x by 5; 
    translate by -0.75 0 -0.5
    scale by 2.25
    display depthcue on
    display cuedensity 0.12

    #render POV3 fig_2a.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT
    render snapshot fig_2a.tga /usr/bin/open %s
}

# Fig 1.2(b).
after idle {
    animate goto 1050
    
    graphics $id delete all
    graphics $id materials on
    graphics $id material Transparent
    graphics $id color 0
    graphics $id cylinder {25 25 5} {25 25 82} radius 7 resolution 100 filled yes
    graphics $id color 21
    graphics $id cylinder {25 25 4.99} {25 25 100} radius 5 resolution 100 filled yes

    display resetview
    rotate x by 180;
    scale by 2.5
    display depthcue on
    display cuedensity 0.12

    #render POV3 fig_2b.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT
    render snapshot fig_2b.tga /usr/bin/open %s
}