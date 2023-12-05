import tkinter as ttk 
import requests as rqst

root = ttk.Tk()

button1 = ttk.Button(root,text="Teste",fg="black",bg="white")



        

def main():
    with open("categories.txt","r") as file:
        categ_dict={}
        for line in file:
            categories = line.strip().split(".")
            if len(categories)!=1:
                categ_dict[categories[0]] = categ_dict.get(categories[0],[])
                categ_dict[categories[0]].append(categories[1])
            else:
                continue    
    root.mainloop()
    print(categ_dict)
if __name__ == "__main__":
    main()
    