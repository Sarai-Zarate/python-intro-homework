import os 
path = os.path.join("week-7", "data", "students.csv")
print(path)

import csv

with open(path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
       print(f"{row['name']}: {row['score']}")