import googlemaps
from config import GOOGLE_MAPS_API_KEY

gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

def optimize_travel_path(itinerary, budget, time_limit):
    
    max_time = time_limit // 1  # Assume 1 hour per attraction
    
    
    optimized_itinerary = itinerary[:max_time]
    
    # Further optimize by considering travel distance (e.g., taxi or walking)
    travel_options = []
    for i in range(len(optimized_itinerary) - 1):
        travel_info = gmaps.directions(optimized_itinerary[i], optimized_itinerary[i + 1])
        travel_options.append(travel_info)
    
    return optimized_itinerary, travel_options
