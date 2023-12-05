import requests as rqst

def get(baseURL,params={}):
    newURL = baseURL + "?"
    for k,v in params.items():
        newURL += f"&{k}={v}"

    request = rqst.get(newURL)
    return request.json()

request = {
"apiKey":"d9d7d63a741949f6913b267674ca0f16",
"categories":"accommodation,activity",
"limit":"10",
"bias":"proximity:-0.07071648508463113,51.50848194136378"
}

print(get("https://api.geoapify.com/v2/places",request))