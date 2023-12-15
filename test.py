def dict_all_categs(fileDir):
    """Creates a dictionary with all the categories in the file as keys and the correspondent sub-categories as values."""
    with open(fileDir,'r') as f:
        return {k:v for k,v in [(line.strip() ,line.strip().split('.')) for line in f]}

      
def filter_categs(s:str, fileDir):
    """Removes any categories not existent in file and returns the following pattern: <category>,<categorie>,(...),<categorie>"""
    categ_lst = [categ.strip() for categ in s.strip().split(',')]
    categ_dict = dict_all_categs(fileDir)            
    lst = [k for k,v in categ_dict.items() for categ in categ_lst if categ in v or categ == k]

    return ','.join(lst)

print(filter_categs('food_and_drink', 'categories.txt'))