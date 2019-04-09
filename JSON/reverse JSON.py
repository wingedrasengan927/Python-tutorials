
# Let's convert a python object into a json string
# we use the json.dumps method

# Let's say in our example we want to remove the phone numbers
# and convert this back into a json string

import json

people_string = '''
{
    "people":[
        {
            "name":"John Smith",
            "phone":"932-232-1344",
            "emails":["Johnny@gmail.com", "Smith961@outlook.com"],
            "has_license":false

        },
        {
            "name":"Jane Doe",
            "phone":"345-235-7855",
            "emails":null,
            "has_license":true            
        }
    ]
}
'''

data = json.loads(people_string)

# Let's loop through them all and delete the phone numbers
for person in data["people"]:
    del person["phone"]

# putting sort_keys=True sorts keys alphabetically
new_string = json.dumps(data, indent=2, sort_keys=True) # for each level, it indents it twice

print(new_string)