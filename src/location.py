import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import matplotlib.pyplot as plt
import plotly_express as px
import tqdm
import json
from tqdm._tqdm_notebook import tqdm_notebook

locator = Nominatim(user_agent="myGeocoder")

def reverseGeo(location, context):

    print("reverseGeo Init: ", context.user_data)

    longitude = location.longitude

    latitude = location.latitude
    
    coordinates = f'{latitude}, {longitude}'
    
    rev_location = locator.reverse(coordinates)
    
    user_location = json.loads(json.dumps(rev_location.raw, indent=4))
    
    context.user_data['Estado'] = user_location['address']['state']

    try:
        context.user_data['Cidade'] = user_location['address']['town']
    
    except:
        try:
            context.user_data['Cidade'] = user_location['address']['city']

        except:
            context.user_data['Cidade'] = "Cidade não identificada."

    context.user_data['País'] = user_location['address']['country']

    print("reverseGeo End: ", context.user_data)
