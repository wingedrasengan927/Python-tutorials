
# Let's say we wrote this and we want to use this in other modules or scripts

print("Imported my module...")

test = "test string"

def find_index(to_search, target):
    for i, value in enumerate(target):
        if value == to_search:
            return i

    print("this value is not contained in the target")

