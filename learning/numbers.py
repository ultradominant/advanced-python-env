import json
with open("numbers.json", "r", encoding = "utf-8") as file:
    data = json.load(file)

    min_number = min(data["numbers"])
    max_number = max(data["numbers"])

    print("Minimum number:", min_number)
    print("Maximum number:", max_number)
    print("All numbers:", data["numbers"])

