import folium


def choose_color(award):
    if award == "3 MICHELIN Stars":
        return "blue"
    elif award == "2 MICHELIN Stars":
        return "green"
    elif award == "1 MICHELIN Star":
        return "orange"
    elif award == "Bib Gourmand":
        return "red"
    else:
        return "gray"


london_map = folium.Map(location=[34.57079, 113.45088], zoom_start=6)

f = open("/Users/kasperxiaomingshen/Documents/test111.txt")
lines = f.readlines()
for line in lines:
    line = line.replace("\n", "")
    values = line.split("\t")
    folium.Marker(location=[values[2], values[1]], tooltip=values[0], popup=values[3], icon=folium.Icon(color=choose_color(values[3]))).add_to(london_map)

london_map.save("china_michelin.html")