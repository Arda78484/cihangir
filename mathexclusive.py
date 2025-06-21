from math import *
d = 180 / pi
r = pi / 180

def haversine(lat1, lon1, lat2, lon2):
    
    # distance between latitudes
    # and longitudes
    dLat = (lat2 - lat1) * pi / 180.0
    dLon = (lon2 - lon1) * pi / 180.0

    # convert to radians
    lat1 = (lat1) * pi / 180.0
    lat2 = (lat2) * pi / 180.0

    # apply formulae
    a = (pow(sin(dLat / 2), 2) + 
         pow(sin(dLon / 2), 2) * 
             cos(lat1) * cos(lat2))
    rad = 6371
    c = 2 * asin(sqrt(a))
    return rad * c