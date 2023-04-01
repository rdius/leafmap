import folium

# define the center and zoom level of your map
center = [37.7749, -122.4194]
zoom = 13

# define the tile URLs for the two dates you want to display
url_1 = 'https://services.digitalglobe.com/mapservice/wmtsaccess?layer=DigitalGlobe:ImageryTileService&tilematrixset=EPSG:3857&Service=WMTS&Request=GetTile&Version=1.0.0&Format=image/png&TileMatrix={z}&TileCol={x}&TileRow={y}&time=2019-01-01T00:00:00.000Z'
url_2 = 'https://services.digitalglobe.com/mapservice/wmtsaccess?layer=DigitalGlobe:ImageryTileService&tilematrixset=EPSG:3857&Service=WMTS&Request=GetTile&Version=1.0.0&Format=image/png&TileMatrix={z}&TileCol={x}&TileRow={y}&time=2021-01-01T00:00:00.000Z'

# create a map object
my_map = folium.Map(location=center, zoom_start=zoom)

# create a tile layer for each date and add it to the map
folium.TileLayer(tiles=url_1, attr='DigitalGlobe', name='2019 Imagery', overlay=True, control=True).add_to(my_map)
folium.TileLayer(tiles=url_2, attr='DigitalGlobe', name='2021 Imagery', overlay=True, control=True).add_to(my_map)

# add layer control to the map
folium.LayerControl().add_to(my_map)

# display the map
my_map
