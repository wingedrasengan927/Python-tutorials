

# The raise statement allows the programmer to force a specified exception to occur.
# The sole argument to raise indicates the exception to be raised.
# This must be either an exception instance or an exception class (a class that derives from Exception).

try:
    # Example of an Exception instance :
    raise Exception("x should not exceed 10")
except Exception as inst:
    print(type(inst)) # See, This is an Instance of Exception Class

# Let's create our own Error derived from the Exception Class
# Most exceptions are defined with names that end in “Error”, similar to the naming of the standard exceptions.

class ExampleError(Exception):
    "This is just to illustrate"
    pass

print("\n")

try:
    # Example of an exception class (a class that derives from Exception)
    # If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments.
    # Meaning, we don't need to put braces like ExampleError()
    # The Constructor will take care of this
    raise ExampleError # shortcut for ExampleError()
except ExampleError:
    print("This is just to Illustrate")

print("\n")

# Many standard modules define their own exceptions to report errors that may occur in functions they define.

# User-Defined Exceptions should typically be derived from the Exception class, either directly or indirectly.

# Exception classes can be defined which do anything any other class can do, but are usually kept simple,
# often only offering a number of attributes that allow information about the error to be extracted by handlers for the exception.

# When creating a module that can raise several distinct errors,
# a common practice is to create a base class for exceptions defined by that module,
# and subclass that to create specific exception classes for different error conditions

# Let's see this with an example

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class NothingError(Error):
    """Exception raised if the variable contains nothing.

    Attributes:
        datatype -- the datatype of the variable in which the error occurs
        message -- explanation of the error
    """

    def __init__(self, datatype, message):
        self.datatype = type(datatype)
        self.message = message

print("\n")

try:
    data=[]
    if not data:
        raise NothingError(data, "This {} contains no data. Hence the error".format(type(data)))
except NothingError as inst:
    print(inst.datatype)
    print(inst.message)