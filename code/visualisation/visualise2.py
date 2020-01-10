from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure
from bokeh.sampledata.sample_geojson import geojson
import json
import csv
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap
from bokeh.models import HoverTool

output_file("geojson.html")
map_options = GMapOptions(lat=52, lng=5, map_type="roadmap", zoom=7)

p = gmap("AIzaSyCnGx0iTuaHmLPA8LdqDnIo7vK15mp5sww", map_options)

# data = json.loads("data/StationsNationaal.json")
with open("data/StationsNationaal2.json", 'r') as geo_file:
        data = json.load(geo_file)


for i in range(len(data['features'])):
    data['features'][i]['properties']['Color'] = ['blue', 'blue'][i%2]

geo_source = GeoJSONDataSource(geojson=json.dumps(data))

TOOLTIPS = [
    ('Station', '@name')
]

x1 = []
y1 = []
with open("data/trajectcoordinaten2.csv", mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        x1.append([float(row[2]),float(row[4])])
        # x1.append(float(row[4]))
        y1.append([float(row[3]),float(row[5])])
        

# print(y1,x1)
# print(y1)
# p = figure(background_fill_color="lightgrey", tooltips=TOOLTIPS)

p.multi_line(y1,x1,line_width=2)
p.circle(x='x', y='y', size=5, color='Color', alpha=0.7, source=geo_source)
show(p)


