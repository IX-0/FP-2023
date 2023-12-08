from API import *
from main import *

import tkinter as tk

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