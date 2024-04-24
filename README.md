# GR-Placefile-Maker
Turn a CSV of points and data into a Gibson Ridge 2 Analyst 3 (GR2AAnalyst 3) PlaceFile 


Example usage: 
The [USWTDB](https://eerscmap.usgs.gov/uswtdb/) dataset shows information about wind turbines. In the CSV, 'ylat' is the latitude, 'xlong' is the longitude, 'p_name' is the priject name, and 't_hh' is the turbine height. 
The following shows the command so far, with the CSV and output names filled in.

`.\program.py -f "uswtdbCSV\uswtdb_v6_1_20231128.csv" -o "uswtdbCSV\Turbines.txt" -lat ylat -lon xlong -ln PROJ -n p_name -ld height -d t_hh `

Additionally, we need to give information about the Icon. You can find an example icon at http://saratoga-weather.org/USA-blitzortung/lightningiconsnob.png. Using this icon, you might do:

`-i "http://saratoga-weather.org/USA-blitzortung/lightningiconsnob.png" -iw 30 -ih 30 -ix 15 -ix 15 -in 120`
to get a blue dot. 

You also might want a title, so you can add '-t "Wind Turbines"` for the title. 

the full command is then 
`.\program.py -f "uswtdbCSV\uswtdb_v6_1_20231128.csv" -o "uswtdbCSV\Turbines.txt" -lat ylat -lon xlong -ln PROJ -n p_name -ld height -d t_hh -i "http://saratoga-weather.org/USA-blitzortung/lightningiconsnob.png" -iw 30 -ih 30 -ix 15 -ix 15 -in 120 -t "wind turbines"`
