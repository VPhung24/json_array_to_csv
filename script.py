import csv
import json

data = []

with open('data.json') as file:
    data = json.load(file)

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["brand", "itemName", "price"])
    for item in data:
        writer.writerow([item.get("brand", ""), item.get("itemName", ""), item.get("price", "")])
