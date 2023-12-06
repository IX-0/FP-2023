import requests as rqst
import math

def get(baseURL,params={}):
    newURL = baseURL + "?"
    for k,v in params.items():
        newURL += f"&{k}={v}"

    request = rqst.get(newURL)
    return request.json()

def calc_dist(lon1,lat1,lon2,lat2):
    """fiz uma função inútil pq não sabia que havia a API també dava a distância"""
    RADIUS = 6371
    φ1 = lat1 * math.pi/180
    φ2 = lat2 * math.pi/180
    Δφ = (lat2-lat1) * math.pi/180
    Δλ = (lon2-lon1) * math.pi/180
    a = math.sin(Δφ/2) * math.sin(Δφ/2) + math.cos(φ1) * math.cos(φ2) * math.sin(Δλ/2) * math.sin(Δλ/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    dist = RADIUS * c
    return dist
    
    
lon = -0.07071648508463113
lat = 51.50848194136378    
request = {
"apiKey":"d9d7d63a741949f6913b267674ca0f16",
"categories":"accommodation,activity",
"limit":"10",
"bias":"proximity:-0.07071648508463113,51.50848194136378"
}

data = get("https://api.geoapify.com/v2/places",request)
#print(data)
for i in data['features']:
    this_data = i ['properties']
    if this_data.get('name',None) == None: continue
    else:
        this_dict = {
            'name':this_data['name'],
            'country': this_data['country'],
            'state': this_data['state'],
            'city': this_data['city'],
            'coordinates': (this_data['lon'],this_data['lat']),
            'distance': this_data['distance'],
            'categories': this_data['categories']
        }
        print("=============================")
        for k,v in this_dict.items():
            print("{:15} : {}".format(k,v))
    
#print(data['features'][8]['properties'])

#round(calc_dist(this_data['lon'],this_data['lat'],lon,lat),3)  
    