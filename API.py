import requests as rqst

def get(baseURL,params={}):
    """Returns the API data in JSON format"""

    newURL = baseURL + "?"
    for k,v in params.items():
        newURL += f"&{k}={v}"

    request = rqst.get(newURL)
    return request.json()

def convertRequest(data):
    """Converts data from the api to a list with locations"""
    locations = [{k:v for k,v in loc['properties'].items()} for loc in data['features']]

    return locations