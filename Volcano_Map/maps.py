import os, folium, pandas, json
mymap = folium.Map(location=[51.5105,-0.5950], zoom_start = 7, )

data = pandas.read_csv('Volcanoes_USA.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elevation = list(data['ELEV'])
fg = folium.FeatureGroup(name = 'My Map')

def colours(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 < elevation < 3000:
        return 'orange'
    else:
        return 'red'
        


mymap.add_child(fg)  

for lt, ln, el in zip(lat,lon, elevation):
    fg.add_child(folium.Marker(location = [lt,ln], radius = 10, popup = f'Elevation is {el} ', icon = folium.Icon(color = colours(el)), color = 'black', fill_opacity = 0.7 ))

fg.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if x['properties']['POP2005'] > 10000000 and x['properties']['POP2005'] < 100000000 else 'red' }))


mymap.add_child(fg)

    
mymap.save('Map1.html')