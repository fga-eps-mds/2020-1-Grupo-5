from geopy.geocoders import Nominatim
import json

locator = Nominatim(user_agent="myGeocoder")

def reverseGeo(location, user_data):
    longitude = location.longitude
    latitude = location.latitude

    coordinates = f'{latitude}, {longitude}'
    
    rev_location = locator.reverse(coordinates)    
    user_location = json.loads(json.dumps(rev_location.raw, indent=4))
    
    user_data['Estado'] = user_location['address']['state']

    try:
        user_data['Cidade'] = user_location['address']['town']
    except:
        try:
            user_data['Cidade'] = user_location['address']['city']
        except:
            user_data['Cidade'] = "Cidade não identificada."

    user_data['País'] = user_location['address']['country']
