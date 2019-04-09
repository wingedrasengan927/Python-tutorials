# ask the user 2 numbers

num1, num2 = input('Enter any 2 numbers ').split()  # split separates two or more variables with respect to space

# Convert the strings to int

num1 = int(num1)
num2 = int(num2)

# divide num1 and num2 and print the result

divide = num1/num2
print("{} / {} = {}".format(num1, num2, divide))  # the variables go into the curly braces in their respective order

# Problem : recieve miles and convert them to kilometers
# kilometers = miles * 1.60934

miles = input('enter the number of miles ')
factor = 1.60934
miles = int(miles)
kilometers = miles * factor
print("{} miles is equal to {} kilometers".format(miles, kilometers))

#  Calculator : User Inputs 5 * 6 ; outputs 5 * 6 = 30

num1, operator, num2 = input('Enter the Calculation : ').split()

num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print("{} + {} = {} ".format(num1, num2, num1 + num2))
elif operator == "*":
    print("{} * {} = {} ".format(num1, num2, num1 * num2))
elif operator == "-":
    print("{} - {} = {} ".format(num1, num2, num1 - num2))
elif operator == "/":
    print("{} / {} = {} ".format(num1, num2, num1 / num2))
elif operator == "%":
    print("{} % {} = {} ".format(num1, num2, num1 % num2))
else:
    print("use either +, -, /, * or % next time")

#  Age program

age = eval(input('enter your age: '))

if age < 5:
    print('too young for school')
elif age == 5:
    print('go to kindergarten')
elif age >= 6 and age <= 17:
    print("go to class {} ".format(age-5))
elif age > 17 and age < 21:
    print('go to college')
else:
    print('you are an adult')
