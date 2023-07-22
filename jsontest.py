import json 
with open('stuffs.json', 'r') as f:
    data = json.load(f)

print(data)