import json
with open("user.json", "r", encoding = "UTF-8") as file:
    data = json.load(file)

data["active"] = True

with open("user.json", "w", encoding = "UTF-8") as file:
    json.dump(
        data,
        file, 
        indent = 4,
        ensure_ascii = False)
    print("User data updated:", data)
    