from API import *

import tkinter as tk

data = get("https://api.geoapify.com/v2/places",params={'apiKey':'d9d7d63a741949f6913b267674ca0f16','categories':'accommodation','limit':'5','bias':'proximity:-0.07071648508463113,51.50848194136378'})

print(data)

places = convertRequest(data)

print(places)