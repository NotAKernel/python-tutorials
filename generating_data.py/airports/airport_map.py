import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "airports/airports.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get name, type, lat and long, continent, iso_country
    names, types, lats, longs, conts, isos, hover_texts = [], [], [], [], [], [], []
    for row in reader:
        name = (row[3])
        type_ = (row[2])
        lat = (row[4])
        long_ = (row[5])
        cont = (row[7])
        iso = (row[8])
        title = (name[:], type_[:].title(), cont[:], iso[:])

        # Add values to lists
        names.append(name)
        types.append(type_)
        lats.append(lat)
        longs.append(long_)
        conts.append(cont)
        isos.append(iso)
        hover_texts.append(title)
    
    
# Map the airports
data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': 15,
        'color': 'darkblue'
    },
}]

my_layout = Layout(title='Global Airports')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_airports.html')
