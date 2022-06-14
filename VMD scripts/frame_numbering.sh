rm -rf foo.jpg

find . -name "*.ppm" | while read line 
do ts=$(echo $line | awk -F . '{print $3}') 
#rt=$(echo "scale=1;$ts/100" | bc)
rt=$(awk "BEGIN {printf \"%.2f\n\", $ts/100}")
rt="${rt} ns" 
echo $rt 
convert -font CourierNew -fill black -pointsize 20 -draw "text 450,810 '$rt'" $line foo.$ts.jpg 
done 

ffmpeg -an -i foo.%05d.jpg -vcodec mpeg2video -r 24 -vframes 1200 -qscale 0 output.mpg
rm -rf foo.*.jpg