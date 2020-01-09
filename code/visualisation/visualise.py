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