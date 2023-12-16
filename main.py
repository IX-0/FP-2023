import os, csv, math
import requests as rqst

def get(baseURL,params={}):
    """Returns the API data in JSON format"""

    newURL = baseURL + "?"
    for k,v in params.items():
        newURL += f"&{k}={v}"
    request = rqst.get(newURL)
    return request.json()


def convertRequest(data):
    """Converts data from the api to a list with locations each being a dictionary with properties as keys"""
    locations = [{k:v for k,v in loc['properties'].items()} for loc in data['features'] if loc['properties'].get('name',False)]
    return locations


def set_all_categs(fileDir):
    """Creates a set with all the possible categories or sub-categories in file"""
    with open(fileDir,'r') as f:
        return {categ for line in f for categ in line.strip().split('.')}
   
   
def dict_all_categs(fileDir):
    """Creates a dictionary with all the categories in the file as keys and the correspondent sub-categories as values."""
    with open(fileDir,'r') as f:
        return {k:v for k,v in [(line.strip() ,line.strip().split('.')) for line in f]}

      
def filter_categs(s:str, fileDir):
    """
    Removes any categories not existent in file and returns found and invalid categories in the following formats: 
    found categories: '<category>,<categorie>,(...),<categorie>'
    invalid categories: '<category>,<categorie>,(...),<categorie>'
    """
    categ_set = set_all_categs(fileDir)
    categ_dict = dict_all_categs(fileDir)
    categ_lst = {categ.strip() for categ in s.strip().split(',')}
     
    validated_categs = {categ for categ in categ_lst if categ in categ_set or categ in categ_dict.keys()}
    unique_categs = {k for k,v in categ_dict.items() for categ in validated_categs if categ in v or categ == k}
    filtered_catgs = categ_lst - validated_categs

    return (','.join(unique_categs) , ','.join(filtered_catgs))


def floatInputLoop(range, prompt):
    """Only returns float values between range[0] and range[1]"""
    min = range[0]
    max = range[1]
    errorMessage = f"Invalid input - Value must be float between {min} and {max}"
    while True:
        try:
            f = float(input(prompt))
            if min <= f <= max:
                return f
            else:
                print(errorMessage)
        except ValueError:
            print(errorMessage)


def haversine(lon1, lat1, lon2, lat2):
    """Returns distance between 2 locations on earth using haversine formula"""
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * 6371 * math.asin(math.sqrt(a))


def prettyPlacePrint(dic):
    print("Name/Adress : {}".format(dic['formatted']))
    print("Categories : {}".format(' , '.join(dic['categories'])))
    print("Coordinates : Lon:{} , Lat:{}".format(dic['lon'],dic['lat']))
    print("Source : {}".format(dic['datasource']['sourcename']))
    print("Place Id : {}".format(dic['place_id']))


def main():
    baseURL = 'https://api.geoapify.com/v2/places'
    
    os.system('cls')
    while True:
        print("="*60)

        #Input loops
        lon = floatInputLoop([-180,180] , 'Longitude (º): ')
        lat = floatInputLoop([-90,90], 'Latitude (º): ')
        radius = floatInputLoop([0,20037250], 'Radius (m): ') #20037250 is about half of the circunference of earth in meters

        #Categories Loop
        while True:
            catgs, filtered_catgs = filter_categs(input('Categories (separated by comma):'),'categories.txt')
            if catgs == '':
                if filtered_catgs != '':
                    print('Invalid categories: ' + filtered_catgs + ' - Please enter some valid ones')
                else:
                    print('Please enter valid categories separated by a comma (,)')
            else:
                if filtered_catgs != '':
                    print('!!! The categories: ' + filtered_catgs + ' where filtered because they where invalid !!!')
                break

        params = {
            'apiKey':'d9d7d63a741949f6913b267674ca0f16',
            'categories': catgs,
            'filter': 'circle:{},{},{}'.format(lon,lat,radius),
            'bias' : 'proximity:{},{}'.format(lon,lat)
        }

        places = convertRequest(get(baseURL, params))
        if len(places) == 0:
            print("="*60)
            print("No places found")
        else:
            totalDistance = 0
            for place in places:
                print("="*60)
                prettyPlacePrint(place)
                distance = round(haversine(place['lon'],place['lat'],lon,lat))
                totalDistance += distance
                print("Distance : {}".format(distance))

            medianDistance = totalDistance/len(places)

            print("="*60)
            print("Distância média : {}".format(medianDistance))
            print("Número de atrações : {}".format(len(places)))
            print("="*60)

            i = input("Export to CSV file? (y/n) ")
            if i.lower() == 'y': 
                filename = input('Enter filename: ')
                with open(filename + '.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['Nome','Country','Lon','Lat','Categories'])
                    for place in places:
                        writer.writerow([place['name'],place['country'],place['lon'],place['lat'],','.join(place['categories'])])

        print("="*60)

        i = input("Go again? (y/n) ")
        if i.lower() == 'y':
            os.system('cls')
            continue
        else:
            print("="*60)
            print("""Thanks for using the places API places getter 3000 mega blaster program, we apreciated ur company""")
            break
        
    
if __name__ == "__main__":
    main()