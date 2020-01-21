from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource, LabelSet, GMapOptions, ColumnDataSource
from bokeh.plotting import figure, gmap
from bokeh.sampledata.sample_geojson import geojson
import json
import csv
import random

with open("data/StationsNationaal.json", 'r') as geo_file:
        data = json.load(geo_file)
            
# providing all the stations of the same color
for i in range(10):
    data['features'][i]['properties']['Color'] = ['black', 'black'][i%2]

geo_source = GeoJSONDataSource(geojson=json.dumps(data))

# save all the connections between the stations in a list
x1 = []
y1 = []
count = 0
with open("data/trajectcoordinaten.csv", mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        # count +=1
        # if count < 1:
        #     continue
        
        y1.append([float(row[2]),float(row[4])])
        x1.append([float(row[3]),float(row[5])])
        if count == 10:
            break
        
# figure settings
p = figure(background_fill_color="lightgrey", plot_width=800,plot_height=800, tools="save,tap,pan,lasso_select,box_select,box_zoom,reset", active_drag="lasso_select")

# the lines for all the connections are given the same color, white
p.multi_line(x1,y1,line_width=5,color='white')

x2 = []
y2 = []
# colors = ['blue','red','grey','black','aqua','peru']
for j in range(10):
    # color = colors[j]
    for i in range(j):
        ranges =[0,1,2]
        if i in ranges:
            continue
        x2.append(y1[i])
        y2.append(x1[i])
p.multi_line(y2,x2,line_width=5,color='blue')


# p.circle(x='x', y='y', size=5, color='Color', alpha=0.7, source=geo_source)

# open the map
show(p)
