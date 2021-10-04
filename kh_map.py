import folium


kh_gps = (22.6273, 120.3014)
m = folium.Map(location=kh_gps, zoom_start=16)
m.save("docs/index.html")
