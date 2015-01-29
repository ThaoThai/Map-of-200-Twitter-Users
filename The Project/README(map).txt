Thao Thai
Linux Project
Flappy Bird and Frozen "HeatMap"

#twitter keyword "Frozen" and "flappy bird"

# Combine All Collect Files Into One
cat file1.txt file2.txt > flappybird.txt

# Clean up the file
cat flappybird.txt | egrep -o '"coordinates":[^"]*,'| sed '/"coordinates":null/d' | tr -d '"coordinates:"'| tr -d '\}'| sed 's/\[\[//'|sed 's/\]\]//'|sed 's/\(,\[..\).*//'|sed 's/,$//'|sed 's/$/,/'

# Modified into GeoJSon format
cat flappybird.txt| sed -i '1s/^/{"type": "MultiPoint","coordinates": [\n/' flappybird.txt|sed -e '$s/,$/\]\}/' flappybird.txt

Then use geojson.io, get the map.geojson file
Edit the map using TileMill
