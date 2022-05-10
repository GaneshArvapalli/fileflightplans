# Ganesh Arvapalli
# 5/4/2022

import numpy as np
from shapely.geometry import Point, LineString, Polygon
from fastkml import kml, styles
from pyproj import Proj, Transformer
import pdb
import sys
import argparse

parser = argparse.ArgumentParser(
    usage="%(prog)s [FILE] [MAX_SPEED]",
    description="Calculate green and yellow bounds for flight plan filing, given red bounds in a .kml file."
)
parser.add_argument(
    "-v", "--version", action="version",
    version = f"{parser.prog} version 0.1.0"
)
parser.add_argument('file', help="Name of .kml file")
parser.add_argument('max_speed', type=float, help="Maximum speed of flight in meters per second")
args = parser.parse_args()

# Read in KML file
kml_file = args.file

# The +7.7 comes from accounting for wind
max_speed = float(args.max_speed) # + 7.716667 

with open(kml_file, 'rt', encoding="utf-8") as myfile:
    doc=myfile.read()
    k = kml.KML()
    k.from_string(bytes(doc, encoding='utf8'))

# Get the boundary geometry
# pdb.set_trace()
try:
    features = list(k.features())
    f2 = list(features[0].features())
    red_bounds = f2[0].geometry
except:
    print("Error in parsing file!")
    sys.exit(1)

print("RED")
# Reproject to meter space
transformer = Transformer.from_crs("epsg:4326", "epsg:3857")
meter_points = []
x, y = red_bounds.exterior.coords.xy
for i,j in zip(x,y):
    print(i, j)
    xp,yp = transformer.transform(i,j)
    meter_points.append((xp, yp))

meter_polygon = Polygon([[p[0], p[1]] for p in meter_points])

# Shrink inward proportional to max speed
yellow = meter_polygon.buffer(max_speed * -5, join_style=2)
green = meter_polygon.buffer(max_speed * -7, join_style=2)

# Testing parallel offset method
# yellow_line = meter_polygon.exterior.parallel_offset(distance=-40, side='left')
# yellow = Polygon(yellow_line)
# green_line = meter_polygon.exterior.parallel_offset(distance=-80, side='left')
# green = Polygon(green_line)

print("YELLOW")
transformer = Transformer.from_crs("epsg:3857", "epsg:4326")
x, y = yellow.exterior.coords.xy
yellow_ge_points = []
for i,j in zip(x,y):
    xp,yp = transformer.transform(i,j)
    yellow_ge_points.append((xp, yp))
    print(xp, yp)

yellow_ge_polygon = Polygon([[p[0], p[1]] for p in yellow_ge_points])

print("GREEN")
# inProj = Proj('epsg:3857')
# outProj = Proj('epsg:4326')
transformer = Transformer.from_crs("epsg:3857", "epsg:4326")
x, y = green.exterior.coords.xy
green_ge_points = []
for i,j in zip(x,y):
    xp,yp = transformer.transform(i,j)
    green_ge_points.append((xp, yp))
    print(xp, yp)

green_ge_polygon = Polygon([[p[0], p[1]] for p in green_ge_points])

# Write out to file
outfile = kml_file[:-4] + "_auto.kml"

k = kml.KML()
ns = '{http://www.opengis.net/kml/2.2}'
d = kml.Document(ns, 'RRA_Test_2.kml')
k.append(d)
f = kml.Folder(ns=ns, name='Bounds')
# d.append(f)

ls = styles.LineStyle(ns, color='ff0000ff', width=4)
ps = styles.PolyStyle(ns, fill=0)
s = styles.Style(styles=[ls,ps])
rp = kml.Placemark(ns=ns, name='Red Bounds', styles=[s])
rp.geometry = red_bounds

ls = styles.LineStyle(ns, color='ff00ffff', width=4)
ps = styles.PolyStyle(ns, fill=0)
s = styles.Style(styles=[ls,ps])
yp = kml.Placemark(ns=ns, name='Yellow Bounds', styles=[s])
yp.geometry = yellow_ge_polygon

ls = styles.LineStyle(ns, color='ff00ff00', width=4)
ps = styles.PolyStyle(ns, fill=0)
s = styles.Style(styles=[ls,ps])
gp = kml.Placemark(ns=ns, name='Green Bounds', styles=[s])
gp.geometry = green_ge_polygon

d.append(rp)
d.append(yp)
d.append(gp)

with open(outfile, 'w', encoding="utf-8") as myfile:
    myfile.write(k.to_string(prettyprint=True))


## To get image: https://stackoverflow.com/questions/63708705/python-convert-kml-to-image-file
# import geopandas as gpd
# import matplotlib.pyplot as plt
# gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'


# # Filepath to KML file
# fp = "history.kml"

# polys = gpd.read_file(fp, driver='KML')
# print(polys)
# polys.plot()
# plt.savefig('test.jpg')