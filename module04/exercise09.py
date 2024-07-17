import csv

with open("countries.csv", "rt") as file:
    reader = csv.reader(file)
    for code, name, continent, population in reader:
        print(f"{code},{name},{continent},{population}")
