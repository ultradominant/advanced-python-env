import json
with open("counter.json", "r", encoding = "UTF-8") as file:
    data = json.load(file)
    data["count"] += 1

with open("counter.json", "w", encoding = "UTF-8") as file:
        json.dump(data, file, indent = 4)
        print("Counter updated to:", data["count"])