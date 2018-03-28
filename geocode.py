import httplib2
import json


def get_geocode(location):
    google_api_key = 'AIzaSyAZuiMVwYKU__4AnQ43L1B0Bgm33NSC_mw'
    locationString = location.replace(" ", "+")
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (
        locationString, google_api_key)

    # create instance of http verb
    h = httplib2.Http()
    response = h.request(url,'GET')
    body = response[1]

    # find latitude and longitude from response
    result = json.loads(body)
    latitide = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitide, longitude)

