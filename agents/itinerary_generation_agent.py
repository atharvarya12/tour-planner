import googlemaps
from config import GOOGLE_MAPS_API_KEY

gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

def get_tourist_spots(destination, interests):
    # Get tourist spots based on destination and interests
    places = gmaps.places(query=f"{destination} {interests}")
    return [place['name'] for place in places.get("results", [])]

def generate_itinerary(user_details):
    # Generate an itinerary with places based on user interests
    tourist_spots = get_tourist_spots(user_details['destination'], user_details['interests'])
    
    # Example: Providing a basic itinerary (could be more sophisticated)
    itinerary = {
        "destination": user_details["destination"],
        "tourist_spots": tourist_spots
    }
    
    return itinerary
