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
    #lst = [categ if categ in categ_dict.keys() else k for categ in categ_lst for k, v in categ_dict.items() if categ in v]
    # OG code is slightly wrong
    '''for categ in categ_lst:
        if categ in categ_dict.keys():
            lst.append(categ)
        else:
            for k,v in categ_dict.items():
                if categ in v:
                    lst.append(k)'''
    # ChatGPT lst comprehension
    lst = list({categ if categ in categ_dict.keys() else next((k for k, v in categ_dict.items() if categ in v), 'default_value') for categ in categ_lst})
    if 'default_value' in lst: 
        for i in range(lst.count('default_value')): lst.remove('default_value')
    return ','.join(lst)

print(filter_categs('poop, hut, beach, poop, commercial','categories.txt'))