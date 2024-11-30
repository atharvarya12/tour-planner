import googlemaps
import folium

class MapGenerationAgent:
    @staticmethod
    def generate_map(locations):
        m = folium.Map(location=locations[0], zoom_start=13)
        for loc in locations:
            folium.Marker(loc).add_to(m)
        m.save("data/itinerary_map.html")
