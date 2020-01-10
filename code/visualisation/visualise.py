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