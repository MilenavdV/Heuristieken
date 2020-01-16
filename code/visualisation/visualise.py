from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource, LabelSet, GMapOptions, ColumnDataSource
from bokeh.plotting import figure, gmap
from bokeh.sampledata.sample_geojson import geojson
import json
import csv


output_file("geojson.html")
# map_options = GMapOptions(lat=52.5, lng=5, map_type="roadmap", zoom=7)

# p = gmap("AIzaSyCnGx0iTuaHmLPA8LdqDnIo7vK15mp5sww", map_options)

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
        y1.append([float(row[2]),float(row[4])])
        x1.append([float(row[3]),float(row[5])])
        
p = figure(background_fill_color="lightgrey", tooltips=TOOLTIPS, plot_width=800,plot_height=800, tools="tap")
p.multi_line(x1,y1,line_width=2)

x2 = []
y2 = []
i = 0
trajecten_x ={}
trajecten_y = {}
with open("dienstregeling.csv", mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')        
    for row in csv_reader:
        traject = 'Traject ' + str(i + 1)
        if row == []:
            continue
        if 'Total' in row[0]:
            continue
        if row[0] == traject:
            i = i+1
            trajecten_y[i] = []
            trajecten_x[i] = []
            continue
        trajecten_y[i].append(row[2])
        trajecten_y[i].append(row[4])
        trajecten_x[i].append(row[3])
        trajecten_x[i].append(row[5])


# labels = LabelSet(x=y1, y=x1, text='@name', level='glyph', source=geo_source)
color = ['peru','red','purple','yellow','aqua']
for i in range(5):
    p.line(trajecten_x[i+1],trajecten_y[i+1],line_width=2,color=color[i])
    # labels = LabelSet(x='trajecten_y',y='trajecten_x',text=i,level='glyph')
    # p.add_layout(labels)

# p.add_layout(labels)
p.circle(x='x', y='y', size=5, color='Color', alpha=0.7, source=geo_source)
show(p)


