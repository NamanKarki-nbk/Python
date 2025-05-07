import json

data = {"name": "Alice", "age": 25}

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    loaded = json.load(f)

print(loaded)
