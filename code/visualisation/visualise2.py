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

# p = gmap("AIzaSyCnGx0iTuaHmLPA8LdqDnIo7vK15mp5sww", map_options)

# data = json.loads("data/StationsNationaal.json")
with open("data/StationsNationaal2.json", 'r') as geo_file:
        data = json.load(geo_file)


for i in range(len(data['features'])):
    data['features'][i]['properties']['Color'] = ['blue', 'blue'][i%2]

geo_source = GeoJSONDataSource(geojson=json.dumps(data))

TOOLTIPS = [
    ('Station', '@name')
]

p = figure(background_fill_color="lightgrey", tooltips=TOOLTIPS)

# p.line(x='x', y='y',source=geo_source)
p.circle(x='x', y='y', size=5, color='Color', alpha=0.7, source=geo_source)
show(p)


