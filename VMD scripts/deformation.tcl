color Display Background white
color Labels Bonds black
axes location Off
material change opacity Transparent 0.75
display nearclip set 0.01

set carbon_top 286

topo readlammpsdata /Users/jiaqz/Desktop/deformation/graphene/fix_none/0/after_nvt.data
mol addfile /Users/jiaqz/Desktop/deformation/graphene/fix_none/0/nvt.lammpstrj

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
rotate x by -90
scale by 2
render POV3 deformation_graphene.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT
######################################
mol delete $id

color Display Background white
color Labels Bonds black
axes location Off
material change opacity Transparent 0.75
display nearclip set 0.01
set carbon_top 622

topo readlammpsdata /Users/jiaqz/Desktop/deformation/CNT/fix_none/0/after_nvt.data
mol addfile /Users/jiaqz/Desktop/deformation/CNT/fix_none/0/nvt.lammpstrj

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
rotate z by 160
render POV3 deformation_CNT.pov povray +W%w +H%h -I%s -O%s.tga +D +X +A +FT