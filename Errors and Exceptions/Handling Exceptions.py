
# It is possible to write programs that handle selected exceptions.
# Look at the following example.

while True:
    try:
        x = int(input("Please enter a number: "))
    # An except clause may name multiple exceptions as a parenthesized tuple
    except (ValueError, NameError, RuntimeError):
        print("Only Numbers, Please. Try Again.")
        continue
    else:
        print("The number you've entered is {}".format(x))
        break

print("\n")

# The try statement works as follows.
#
#     First, the try clause (the statement(s) between the try and except keywords) is executed.

#     If no exception occurs, the except clause is skipped and execution of the try statement is finished.

#     If an exception occurs during execution of the try clause, the rest of the clause is skipped.
#     Then if its type matches the exception named after the except keyword, the except clause is executed,
#     and then execution continues after the try statement.

#     If an exception occurs which does not match the exception named in the except clause,
#     it is passed on to outer try statements; if no handler is found, it is an unhandled exception and
#     execution stops with a message as shown above.




# A try statement may have more than one except clause, to specify handlers for different exceptions. At most one handler will be executed.
# Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same try statement.

# The try … except statement has an optional else clause, which, when present, must follow all except clauses.
# It is useful for code that must be executed if the try clause does not raise an exception.

# The use of the else clause is better than adding additional code to the try clause
# because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try … except statement.


#--------------------------------------------------------

# When an exception occurs, it may have an associated value, also known as the exception’s argument.
# The presence and type of the argument depend on the exception type.
# Let's see through an example below
try:
    1/0
except ZeroDivisionError as inst:
    print(type(inst)) # It's class is ZeroDivisionError which is derived from the Exception class
    # Let's see the exceptions argument
    print(inst.args) # returns 'division by zero'

print("\n")

# we can even pass in our own arguments
# pass in a tuple as an argument
try:
    # The raise statement allows the programmer to force a specified exception to occur.
    # more about it in the next file
    raise ZeroDivisionError(("See this returns our own argument"))
except ZeroDivisionError as inst:
    print(inst.args) # returns "See this returns our own argument"


