import tkinter as tk 
from API import *

def printPlaces(places):
    print()
    print("="*60)
    for place in places:
        for k,v in place.items():
            print("{} : {}".format(k,v))
        print()
        print("="*60)


def addPlaces(frame:tk.Frame):

    """Function that adds location objects to a frame"""

    #DEBUG
    data = get("https://api.geoapify.com/v2/places",params={'apiKey':'d9d7d63a741949f6913b267674ca0f16','categories':'accommodation','limit':'20','bias':'proximity:-0.07071648508463113,51.50848194136378'})

    places = convertRequest(data)
    #DEBUG END

    for place in places:
        placeFrame = tk.LabelFrame(frame, text=place['name'])

        tk.Label(placeFrame, text='Distance: {}'.format(place['distance']))
        tk.Label(placeFrame, text='Categories: {}'.format(place['categories']))

        for element in placeFrame.winfo_children():
            element.pack()

        placeFrame.pack()


def clearPlaces(frame:tk.Frame):
    for place in frame.winfo_children():
        place.destroy()
        

def set_all_categs():
    """Creates a set with all the categories in the file separated by '.' ."""
    with open(r'C:\Users\Utilizador\Desktop\Tiago\GitRepositories\FP-2023\categories.txt') as file:
        all_categs={categ for line in file for categ in line.strip().split('.')}
    return all_categs 
   
   
def dict_all_categs():
    """Creates a dictionary with all the categories in the file as keys and the correspondent sub-categories as values."""
    with open(r'C:\Users\Utilizador\Desktop\Tiago\GitRepositories\FP-2023\categories.txt') as file:
        dict = {k:v for k,v in [(line,line.strip().split('.')) for line in file]}
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
    #GUI

    #Window
    root = tk.Tk()
    root.title('Places API')

    
    #Widgets
    searchButton = tk.Button(
        root,
        text='Search'
    )
    clearButton = tk.Button(
        root,
        text='Clear Results'
    )


    categoryEntry = tk.Entry(
        root,
        width=25,
    )
    categoryLabel = tk.Label(
        root,
        text='Category:',
        font=('Open Sans', 10),
    )


    latEntry = tk.Entry(
        root,
        width=25
    )
    latLabel = tk.Label(
        root,
        text='Latitude (º)',
        font=('Open Sans', 10),
    )


    lonEntry = tk.Entry(
        root,
        width=25
    )
    lonLabel = tk.Label(
        root,
        text='Longitude (º)',
        font=('Open Sans', 10),
    )

    placesFrame = tk.Frame(
        root,
        width= 50
    )

    searchButton.configure(command= lambda: addPlaces(frame=placesFrame))
    clearButton.configure(command= lambda: clearPlaces(frame=placesFrame))
    #Placement
    searchButton.grid(column=2,row=0,rowspan=2)
    clearButton.grid(column=2,row=2)

    categoryLabel.grid(column=0,row=0)
    categoryEntry.grid(column=1,row=0)

    latLabel.grid(column=0,row=1)
    latEntry.grid(column=1,row=1)

    lonLabel.grid(column=0,row=2)
    lonEntry.grid(column=1,row=2)

    placesFrame.grid(column=0,row=3,columnspan=3)

    root.mainloop()

    # x, y = input("Enter coordinates split by coma: ").strip().split(",")
    # radius = float(input("Enter radius: "))
    # categs = input("Enter categories split by coma: ").lower()
    
    # parameters={
    #     "filter" : "circle:{},{},{}".format(x,y,radius),
    #     "apiKey" : "",
    #     "categories" : filter_categs(categs),   
    # }


if __name__ == "__main__":
    main()