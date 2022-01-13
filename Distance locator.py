from opencage.geocoder import OpenCageGeocode
from geopy.distance import geodesic

city1 = input("Your start city")
city2 = input("your end city")

key = "api"  #https://opencagedata.com
geocoder = OpenCageGeocode(key)
query = city1
results = geocoder.geocode(query)
lat1 = results[0]['geometry']['lat']
lng1 = results[0]['geometry']['lng']

query = city2
results = geocoder.geocode(query)
lat2 = results[0]['geometry']['lat']
lng2 = results[0]['geometry']['lng']

city_start = (lat1, lng1)
city_end = (lat2, lng2)

print(geodesic(city_start, city_end).km)
