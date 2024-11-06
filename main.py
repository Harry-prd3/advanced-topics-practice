from app import App
from csv import reader
from tech import (Phone, Laptop)

"""
apps = []

with open('app_list.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter=",")
    next(csv_reader)
    for name, description, category in csv_reader:
        apps.append(App(name, description, category))


for app in apps:
    print(app)
"""


lap = Laptop(5, "macbook", 256)
pho = Phone("pixel", 128, "sage")

print(lap)
print(pho)
print(repr(lap))
print(repr(pho))