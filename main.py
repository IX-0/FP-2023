import tkinter as ttk 
import requests as rqst

#root = ttk.Tk()
#button1 = ttk.Button(root,text="Teste",fg="black",bg="white")

            
def countlen():
    """This function was used purely to study the categories.txt file. Determines the maximum length of a category split by '.' ."""
    with open(r'C:\Users\Utilizador\Desktop\Tiago\GitRepositories\FP-2023\categories.txt') as file:
        print(max([len(line.strip().split('.')) for line in file]))
        
        
def set_all_categs():
    """Creates a set with all the categories in the file separated by '.' ."""
    with open(r'C:\Users\Utilizador\Desktop\Tiago\GitRepositories\FP-2023\categories.txt') as file:
        all_categs={categ for line in file for categ in line.strip().split('.')}
    return all_categs 
   
   
def dict_all_categs():
    """Creates a dictionary with all the categories in the file as keys and the correspondent sub-categories as values."""
    with open(r'C:\Users\Utilizador\Desktop\Tiago\GitRepositories\FP-2023\categories.txt') as file:
        dict = {k:v for k,v in [(line[:-1],line.strip().split('.')) for line in file]}
    return dict

      
def filter_categs(categs):
    categ_set = set_all_categs()
    categ_lst = [categ.strip() for categ in categs.strip().split(',')]
    error_msg = ""
    validated_categs=[]
    for categ in categ_lst:
        if categ in categ_set:
            validated_categs.append(categ)
        else:
            error_msg += "'{}' is not a valid category.\n".format(categ)
    print(error_msg, end="") 
    categ_dict = dict_all_categs()            
    lst=[]
    for categ in validated_categs:
        for k,v in categ_dict.items():
            if categ == k or categ in v:
                lst.append(k)
    return(','.join(lst))

def main():

    x, y = input("Enter coordinates split by coma: ").strip().split(",")
    radius = float(input("Enter radius: "))
    categs = input("Enter categories split by coma: ").lower()

    parameters={
        "filter" : "circle:{},{},{}".format(x,y,radius),
        "apiKey" : "",
        "limit" : "10",
        "categories" : filter_categs(categs),   
    }
    
if __name__ == "__main__":
    main()
    