from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource, LabelSet, GMapOptions, ColumnDataSource
from bokeh.plotting import figure, gmap
from bokeh.sampledata.sample_geojson import geojson
import json
import csv
import random

def visualise(train_used):
    # the file where we save the map
    output_file("geojson.html")
    style_options = json.dumps([
    {
        "featureType": "landscape",
        "elementType": "all",
        "stylers": [
            {
                "hue": "#FFBB00"
            },
            {
                "saturation": 43.400000000000006
            },
            {
                "lightness": 37.599999999999994
            },
            {
                "gamma": 1
            }
        ]
    },
    {
        "featureType": "poi",
        "elementType": "all",
        "stylers": [
            {
                "hue": "#00FF6A"
            },
            {
                "saturation": -1.0989010989011234
            },
            {
                "lightness": 11.200000000000017
            },
            {
                "gamma": 1
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "all",
        "stylers": [
            {
                "hue": "#ffc200"
            },
            {
                "saturation": -61.8
            },
            {
                "lightness": 45.599999999999994
            },
            {
                "gamma": 1
            },
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "road.arterial",
        "elementType": "all",
        "stylers": [
            {
                "hue": "#FF0300"
            },
            {
                "saturation": -100
            },
            {
                "lightness": 51.19999999999999
            },
            {
                "gamma": 1
            }
        ]
    },
    {
        "featureType": "road.local",
        "elementType": "all",
        "stylers": [
            {
                "hue": "#FF0300"
            },
            {
                "saturation": -100
            },
            {
                "lightness": 52
            },
            {
                "gamma": 1
            }
        ]
    },
    {
        "featureType": "water",
        "elementType": "all",
        "stylers": [
            {
                "hue": "#0078FF"
            },
            {
                "saturation": -13.200000000000003
            },
            {
                "lightness": 2.4000000000000057
            },
            {
                "gamma": 1
            }
        ]
    }
])
    # googlemaps settings
    map_options = GMapOptions(lat=52.5, lng=5, map_type="roadmap", zoom=7,styles = style_options)
    p = gmap("AIzaSyB9pKdfe3bVfkZR_sseLIf6y-9bs2x2aLo", map_options, tools="save,tap,pan,wheel_zoom,box_select,box_zoom,reset")
    
    # loading the geodata 
    with open("data/StationsNationaal.json", 'r') as geo_file:
            data = json.load(geo_file)
            
    # providing all the stations of the same color
    for i in range(len(data['features'])):
        data['features'][i]['properties']['Color'] = ['black', 'black'][i%2]

    geo_source = GeoJSONDataSource(geojson=json.dumps(data))

    # save all the connections between the stations in a list
    x1 = []
    y1 = []
    with open("data/trajectcoordinaten.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            y1.append([float(row[2]),float(row[4])])
            x1.append([float(row[3]),float(row[5])])
            
    # figure settings
    # p = figure(background_fill_color="lightgrey", plot_width=800,plot_height=800, tools="save,tap,pan,lasso_select,box_select,box_zoom,reset", active_drag="lasso_select")
    
    # the lines for all the connections are given the same color, white
    p.multi_line(x1,y1,line_width=5,color='white')
    
    # all the x and y coordinates of the tracks are saved in the same dictionary,
    # with the key being the number of a traject
    i = 0
    trajecten_x ={}
    trajecten_y = {}
    with open("dienstregeling-1.csv", mode='r') as csv_file:
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

    # for each traject a random rgb color is generated and with this color a line is made on the same figure as above
    for i in range(train_used):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        p.line(trajecten_x[i+1],trajecten_y[i+1],line_width=2.5,color=(r,g,b))

    # the stations are added at the the end to make sure the black dotes are in front of the lines
    p.circle(x='x', y='y', size=5, color='Color', alpha=0.7, source=geo_source)
    
    # open the map
    show(p)


