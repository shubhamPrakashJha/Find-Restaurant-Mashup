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
version = "20180323"


def findRestaurant(mealType, location):
    ''' return restaurant based on meal type and location '''
    # Use getGeocodeLocation to get the latitude and longitude coordinates
    #  of the location string.
    coordinates = get_geocode(location)
    lat = coordinates[0]
    lng = coordinates[1]


    # Use foursquare API to find a nearby restaurant with the
    # latitude, longitude, and mealType strings.
    url = "https://api.foursquare.com/v2/venues/search?" \
          "client_id=%s&client_secret=%s&v=%s&ll=%s,%s&query=%s" % (
              foursquare_client_id, foursquare_client_secret, version, lat,
              lng,
              mealType)
    # create http verb instance
    h = httplib2.Http()
    response = h.request(url, "GET")
    body = json.loads(response[1])
    restaurnats = body['response']['venues']
    print restaurnats


if __name__ == '__main__':
    findRestaurant("Pizza", "Tokyo, Japan")
