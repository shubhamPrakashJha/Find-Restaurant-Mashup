from geocode import get_geocode
import httplib2
import json

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

# import foursquare client id & secret to send an API request
foursquare_client_id = "WN0UC4JENWZZSTZROEOEJCZNLKYZO3QIEUBKA5GUDYB1IJ3U"
foursquare_client_secret = "RT34CDWMWRZEL5DQH43P1F3A2HS0VP0OCTKRYZZFFAC2OSB0"

def findRestaurant(mealType, location):
    ''' return restaurant based on meal type and location '''

if __name__ == '__main__':
    findRestaurant("Pizza", "Tokyo, Japan")