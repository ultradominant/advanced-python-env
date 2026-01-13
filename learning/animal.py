import json

with open("animal.json", "r", encoding = "utf-8") as file:
        data = json.load(file)
        print(data["type"])
        print(data["age"])
        