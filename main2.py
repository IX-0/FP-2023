from API import *

def print_dict(dict):
    print('='*100)
    for k,v in dict.items(): print("{:^12} : {}".format(k,v))

def dict_all_categs(fileDir):
    '''Creates a dictionary with all the categories in the file as keys and the correspondent sub-categories as values.'''
    with open(fileDir,'r') as f:
        return {k:v for k,v in [(line.strip() ,line.strip().split('.')) for line in f]}

      
def filter_categs(s:str, fileDir):
    '''Removes any categories not existent in file and returns the following pattern: <category>,<categorie>,(...),<categorie>'''
    categ_lst = [categ.strip() for categ in s.strip().split(',')]
    categ_dict = dict_all_categs(fileDir)            
    lst = [categ if categ in categ_dict.keys() else k for categ in categ_lst for k, v in categ_dict.items() if categ in v]
    # OG code is slightly wrong
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
    radius = int(input('Enter radius: ').strip())
    categs = input('Enter categories separated by commas: ').strip()
    new_categs = filter_categs(categs, 'categories.txt')
    if len(new_categs) == 0: 
        print('No valid categories')
        exit()
    params = {
            'apiKey':'d9d7d63a741949f6913b267674ca0f16',
            'categories': filter_categs(new_categs,'categories.txt'),
            'bias': 'proximity:{},{}'.format(lon,lat),
            'limit': 50
        }
    #sort_method = input('Select sorting method(A - Alphabetically | D - by Distance):')
    location_lst = convertRequest(get(baseUrl, params),radius)
    
    location_lst = sorted(location_lst ,reverse=False ,key = lambda location: location['distance'])
    avg_dist = 0
    info_lst = ['name','country','city','distance','lon','lat','categories']
    for location in location_lst:
        avg_dist += location['distance']
        location['distance'] = '{} km'.format(round(location['distance']/1000,2))
        location_dict = {info : location[info] for info in info_lst if location.get(info,False)}
        print_dict(location_dict)
    if len(location_lst) == 0: 
        avg_dist = 0 
    else:
        avg_dist = round(avg_dist/len(location_lst)/1000,2)
    print('='*100)
    print('Average Distance: {} km'.format(avg_dist))
    print('Total Locations: {}'.format(len(location_lst)))
    
main()