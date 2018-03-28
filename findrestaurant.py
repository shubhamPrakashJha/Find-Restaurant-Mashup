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


    # Grab the first restaurant
    if body['response']['venues'] is not None:
        restaurants = body['response']['venues']
        restaurant = restaurants[0]
        rname = restaurant['name']
        rid = restaurant['id']
        raddress = restaurant['location']['formattedAddress']
        address = ""
        for i in raddress:
            address += i + " "
        raddress = address


        #  Get a  300x300 picture of the restaurant using the venue_id
        # (you can change this by altering the 300x300 value in the URL or
        # replacing it with 'orginal' to get the original picture
        images_url = "https://api.foursquare.com/v2/venues/%s/photos?" \
                     "client_id=%s&client_secret=%s&v=%s" % (
                         rid, foursquare_client_id, foursquare_client_secret,
                         version)
        response = h.request(images_url, "GET")
        body = json.loads(response[1])
        if body['response']['photos']['count'] != 0:
            # Grab the first image
            image = body['response']['photos']["items"][0]
            prefix = image['prefix']
            suffix = image['suffix']
            image_url = prefix + "300x300" + suffix
        else:
                # If no image is available, insert default a image url
            image_url = "https://cdn.pixabay.com/photo/2018/03/27/09/46/wine-32" \
                        "65462_960_720.jpg"

        restaurant_info = {'name': rname, 'address': raddress,
                           'image_url': image_url}
        print "\nRestaurant Name: %s" % restaurant_info['name']
        print "Restaurant Address: %s" % restaurant_info['address']
        print "Image: %s" % restaurant_info['image_url']
        return restaurant_info
    else:
        print " No Restaurant Found in %s " % location
        return "No Restaurant found"
if __name__ == '__main__':
    findRestaurant("Pizza", "Tokyo, Japan")
    findRestaurant("Tacos", "Jakarta, Indonesia")
    findRestaurant("Tapas", "Maputo, Mozambique")
    findRestaurant("Falafel", "Cairo, Egypt")
    findRestaurant("Spaghetti", "New Delhi, India")
    findRestaurant("Cappuccino", "Geneva, Switzerland")
    findRestaurant("Sushi", "Los Angeles, California")
    findRestaurant("Steak", "La Paz, Bolivia")
    findRestaurant("Gyros", "Sydney Australia")
