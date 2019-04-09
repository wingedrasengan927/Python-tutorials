
import json

# load method loads a file into the object
# loads method loads the string

# open the json file
with open('states.json') as f:
    data = json.load(f)

# read the file
for states in data["states"]:
    print(states['name'], states['abbreviation'])

# let's remove the area code and write it into a new json file
for states in data['states']:
    del states['area_codes']

# the dump method is used to write into a new json file
with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)
