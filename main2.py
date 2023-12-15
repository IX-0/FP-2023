from API import *


def dict_all_categs(fileDir):
    '''Creates a dictionary with all the categories in the file as keys and the correspondent sub-categories as values.'''
    with open(fileDir,'r') as f:
        return {k:v for k,v in [(line.strip() ,line.strip().split('.')) for line in f]}

      
def filter_categs(s:str, fileDir):
    '''Removes any categories not existent in file and returns the following pattern: <category>,<categorie>,(...),<categorie>'''
    categ_lst = [categ.strip() for categ in s.strip().split(',')]
    categ_dict = dict_all_categs(fileDir)            
    #lst = [k for k,v in categ_dict.items() for categ in categ_lst if categ in v or categ == k]
    lst = [categ if categ in categ_dict.keys() else k for categ in categ_lst for k, v in categ_dict.items() if categ in v]
    # OG code
    '''for categ in categ_lst:
        if categ in categ_dict.keys():
            lst.append(categ)
        else:
            for k,v in categ_dict.items():
                if categ in v:
                    lst.append(k)'''
    # ChatGPT lst comprehension
    lst = [categ if categ in categ_dict else next(k for k, v in categ_dict.items() if categ in v) for categ in categ_lst]
    

    return ','.join(lst)

def main():
    
    baseUrl = 'https://api.geoapify.com/v2/places'
    lon = input('Enter Longitude: ').strip()
    lat = input('Enter Latitude: ').strip()
    #radius = input('Enter radius: ').strip()
    categs = input('Enter categories separated by commas: ').strip()
    new_categs = filter_categs(categs, 'categories.txt')
    params = {
            'apiKey':'d9d7d63a741949f6913b267674ca0f16',
            'categories': filter_categs(new_categs,'categories.txt'),
            'bias': 'proximity:{},{}'.format(lon,lat),
            'limit': 50
        }
    #sort_method = input('Select sorting method(A - Alphabetically | D - by Distance):')
    location_lst = convertRequest(get(baseUrl, params))
    
    location_lst = sorted(location_lst ,reverse=True , key = lambda location: location['name'])
    avg_dist = 0
    for location in location_lst:
        print('Name: {}\nCountry: {}\nLocation: (Lon = {}, Lat = {})\nDistance: {} km\nCategories: {}\n======================='.format(location['name'],location['name'],location['lon'],location['lat'],location['distance']/1000,location['categories']))
        avg_dist += location['distance']
    if len(location_lst) == 0: 
        avg_dist = 0 
    else:
        
        avg_dist = round(avg_dist/len(location_lst)/1000,2)
    print('Average Distance: {} km'.format(avg_dist))
    print('Total Locations: {}'.format(len(location_lst)))
    
main()