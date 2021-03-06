"""
visualise.py

Visualisation of the solution to the train planning problem

Author: 0505 + Wouter

"""

from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource, LabelSet, GMapOptions, ColumnDataSource
from bokeh.plotting import figure, gmap
from bokeh.sampledata.sample_geojson import geojson
import json
import csv
import random


class Visualise:
    """Visualisation of a train planning solution"""

    def __init__(self,train_used):
        self.train_used = train_used

    def map(self):
        """Returns a map"""

        # the file where we save the map
        output_file("geojson.html")
       
        # loading the geodata 
        with open("data/StationsNationaal.json", 'r') as geo_file:
                data = json.load(geo_file)
                
        # providing all the stations of the same color
        for i in range(len(data['features'])):
            data['features'][i]['properties']['Color'] = ['black', 'black'][i%2]

        geo_source = GeoJSONDataSource(geojson=json.dumps(data))

        # save all the connections coordinates between the stations in a list
        x1 = []
        y1 = []
        with open("data/trajectcoordinaten.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                y1.append([float(row[2]),float(row[4])])
                x1.append([float(row[3]),float(row[5])])
                
        # figure settings
        p = figure(background_fill_color="lightgrey", plot_width=800,plot_height=800, 
                tools="save,tap,pan,lasso_select,box_select,box_zoom,reset", active_drag="lasso_select")
        
        # the lines for all the connections are given the same color, white
        p.multi_line(x1,y1,line_width=5,color='white')
        
        # all the x and y coordinates of the tracks are saved in the same dictionary,
        # with the key being the number of a traject
        i = 0
        trajecten_x ={}
        trajecten_y = {}
        with open("results/dienstregeling.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')        
            for row in csv_reader:
                traject = 'Traject ' + str(i + 1)
                if row == []:
                    continue
                if 'Total' in row[0]:
                    continue
                if row[0] == traject:
                    i = i + 1
                    trajecten_y[i] = []
                    trajecten_x[i] = []
                    continue
                trajecten_y[i].append(row[2])
                trajecten_y[i].append(row[4])
                trajecten_x[i].append(row[3])
                trajecten_x[i].append(row[5])

        # all the lines for the tracks that are actually made get different colors
        color = ['blue','red', 'cyan','peru', 'olive', 'black', 'lime', 'pink','orchid','goldenrod','grey', 'lightcoral', 'yellow', 
                    'darkviolet', 'darkgreen', 'mediumblue', 'magenta', 'silver','cadetblue', 'purple']

        for i in range(self.train_used):
            p.line(trajecten_x[i+1],trajecten_y[i+1],line_width=2.5,color= color[i])

        # the stations are added at the the end to make sure the black dotes are in front of the lines
        p.circle(x='x', y='y', size=5, color='Color', alpha=0.7, source=geo_source)
        
        # open the map
        show(p)

