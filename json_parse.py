import json

with open('info.json','r') as json_file:
    jsonparse = json.load(json_file)

print(jsonparse)
print(jsonparse['name'])