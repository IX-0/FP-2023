import requests as rqst

def get(baseURL,params={}):
    """Returns the API data in JSON format"""

    newURL = baseURL + "?"
    for k,v in params.items():
        newURL += f"&{k}={v}"
    print(newURL)
    request = rqst.get(newURL)
    return request.json()

def convertRequest(data,radius):
    """Converts data from the api to a list with locations"""
    locations = [{k:v for k,v in loc['properties'].items() } for loc in data['features'] if loc['properties'].get('name',False) and loc['properties']['distance'] <= radius*1000]
    return locations