<<<<<<< HEAD
import math 
import csv

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8

plot = figure(title='Graph Layout Demonstration', x_range=(51,54), y_range=(4,7),
              tools='', toolbar_location=None)

graph = GraphRenderer()
node_indices = list(range(28))
graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(Spectral8, 'color')
graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='color')

graph.edge_renderer.data_source.data = dict(
    start=[0]*28,
    end=node_indices)



x = []
y = []
with open('data/StationsNationaal.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        x.append(float(row[1]))
        y.append(float(row[2]))

graph_layout = dict(zip(node_indices,zip(x, y)))
print(graph_layout)
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)
=======
from bokeh.plotting import figure, show, output_file, gmap
from bokeh.tile_providers import get_provider, Vendors
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions

output_file("tile.html")

tile_provider = get_provider(Vendors.CARTODBPOSITRON)

# range bounds supplied in web mercator coordinates
p = figure(x_range=(-2000000, 6000000), y_range=(-1000000, 7000000),
           x_axis_type="mercator", y_axis_type="mercator")
p.add_tile(tile_provider)

source = ColumnDataSource(
    data=dict(lat=[ 30.29,  30.20,  30.29],
              lon=[-97.70, -97.74, -97.78])
)

p.circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, source=source)
show(p)
>>>>>>> 148b5bace81eebbc723c9825dddea570463b1cd8
