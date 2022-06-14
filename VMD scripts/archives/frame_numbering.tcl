proc enabletrace {} { 
  global vmd_frame; 
  trace variable vmd_frame([molinfo top]) w drawcounter 
} 
proc disabletrace {} { 
  global vmd_frame; 
  trace vdelete vmd_frame([molinfo top]) w drawcounter 
} 
proc drawcounter { name element op } { 
  global vmd_frame; 
  draw delete all 
  # puts "callback!" 
  draw color white 
  set psperframe 4 
  set psoffset 0 
  set time [format "%d ps" [expr ($vmd_frame([molinfo top]) * $psperframe) + $psoffset]] 
  draw text {70 40 80 } "$time" 
} 