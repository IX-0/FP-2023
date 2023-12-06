import tkinter as ttk 
import requests as rqst

#root = ttk.Tk()
#button1 = ttk.Button(root,text="Teste",fg="black",bg="white")

            
def countlen():
    with open(r'C:\Users\Utilizador\Desktop\Tiago\GitRepositories\FP-2023\categories.txt') as file:
        print(max([len(line.strip().split('.')) for line in file]))
        
        
def all_categs():
    with open(r'C:\Users\Utilizador\Desktop\Tiago\GitRepositories\FP-2023\categories.txt') as file:
        all_categs={categ for line in file for categ in line.strip().split('.')}
    return all_categs    
    
def make_dict():
    with open(r'C:\Users\Utilizador\Desktop\Tiago\GitRepositories\FP-2023\categories.txt') as file:
        return {k:v for k,v in [(line[:-1],line.strip().split('.')) for line in file]}  
      
def filter_categs(categs):
    categ_set = all_categs()
    categ_lst = categs.strip().split(',')
    error_msg = ""
    validated_categs=[]
    for categ in categ_lst:
        if categ in categ_set:
            validated_categs.append(categ)
        else:
            error_msg += "'{}' is not a valid category.\n".format(categ)
    print(error_msg, end="")
    return ','.join(validated_categs)           

def main():
    countlen()
    categ_set = all_categs() 
    
    """x, y = input("Enter coordinates split by coma: ").strip().split(",")
    coordinates = (float(x), float(y))
    radius = float(input("Enter radius: "))
    categs = input("Enter categories split by coma: ")"""
    
    
    print(make_dict())
    
    
if __name__ == "__main__":
    main()
    