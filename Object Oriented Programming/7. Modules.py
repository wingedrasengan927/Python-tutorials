
courses = ["History", "Maths", "Science", "Physics", "Biology"]

# Let's say we want to use that 'find_index' function from 'my module' in this script
# Now, both the 'module' and this script are in the same directory
# When we import a module, it runs all of the code from the module we import
# So, that's how it creates all the functions and the variables
# That's why we have put a print statement at the beginning

# let's import the module
# we can directly import it as it's in the same directory

import my_module

# we can see the print statement
# hence, our module has been imported successfully

# we cannot use the functions in the module directly
# instead, we have to type the module name and then access the functions using the dot operator

print(my_module.find_index("Maths", courses))

# if we want to use this function a lot of times in the code
# then it's not good to always access it from the module using the fullname
# it occupies a lot of room
# instead, we can use a short form to our module, such as

import my_module as mm
# and then the function can be accessed as
print(mm.find_index("Maths", courses))

# Now, there is a way to import the function itself directly

from my_module import find_index
print(find_index("Maths", courses))

# the problem with this approach is
# it only gives us access to the find_index function and not to everything else
# like, we cannot have access the test variable stored in the my_module

# we can access both test variable and find index function as
from my_module import find_index, test
print(test)
# using this method of importing, we have to give the specifics and add commas

# there is another way where we can import everything from the module
# but generally, we don't use this way of importing
# reason being, we cannot track down from which module this function or varible is imported

from my_module import *
print(find_index("Maths", courses))
print(test)

# ----------------------------------------------------------------------

# When we import a module, how does it know where to find that module?
# we did'nt pass any file path, it just finds it
# the way it works is, it checks multiple locations
# and the locations it checks are within a list called sys.path

import sys
print(sys.path)

# how directories are added into this list
# order
# first, directory containing the file we are working with
# second, python path environment variable
# third, standard library directories
# lastly, site packages directory

# let's see what it looks like if the module we want to import isn't in the same directory as this file
# let's create a new module in the desktop
# Now, let's try to import 'my_module_1'

# import my_module_1 #error: module not found

# So, one way to avoid this error
# is to add the path to our sys.path list
# so, let's add and try once again

sys.path.append('C:\\Users\\neera\\Desktop')
import my_module_1 # It works, as evident from the print message
print(my_module_1.reverse("Sdsdsd")) # It works

# The other way to do this is to make a change in the python's environment variables

# To set this environment variable on windows
# right click on my computer and select properties
# From properties, go to advanced sysytem settings
# Then click on environment varibles
# Click new
# type 'PYTHONPATH' as variable name
# put the path in the variable value

# To import the module
# Go to the command prompt
# and type 'import module (my_module_1 in this case)'

# If you're using an IDE like pycharm
# the environment variables can be set in an other way
# google 'your IDE name' and PYTHONPATH
# to see how this works for your IDE

# ----------------------------------------------------------------------

# When something is a part of your standard library
# It means we're able to use it without installing anything
# example: Math module, random module
