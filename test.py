from API import *

import tkinter as tk

<<<<<<< HEAD
# Create the main window
window = tk.Tk()
window.title("PythonExamples.org")
window.geometry("300x200")

# Function to read and print the value in Entry widget
def print_entered_value():
    value = entry.get()
    label1.configure(text="Hello {}!".format(value))

label = tk.Label(window, text="Enter you name")
label.pack()
 
# Create an Entry field
entry = tk.Entry(window)
entry.pack()

# Create a button
button = tk.Button(window, text="Submit", command=print_entered_value)
button.pack()

label1 = tk.Label(window, text="")
label1.pack(padx=10,pady=10)

# Run the application
window.mainloop()
=======
data = get("https://api.geoapify.com/v2/places",params={'apiKey':'d9d7d63a741949f6913b267674ca0f16','categories':'accommodation','limit':'5','bias':'proximity:-0.07071648508463113,51.50848194136378'})

print(data)

places = convertRequest(data)

print(places)
>>>>>>> 2143fc24e480e35134f7ad06398122a40c3c4fb6
