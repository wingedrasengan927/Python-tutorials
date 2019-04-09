
# JSON is a data format used to store information
# Can also be used to fetch data from online APIs
''' JavaScript Object Notation '''
# inspired from javascript

import json

# Let's create a string in a valid JSON Format

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

# we can use the loads method to load this data

data=json.loads(people_string)
print(data)

# let's check the type
print(type(data))  # dictionary

# So, we can access the files like a dictionary
# Let's loop through them all and access each of them
for person in data["people"]:
    print(person)