# a simple generator
def square_numbers(nums):
    for num in nums:
        yield num**2

values = [1, 2, 3, 5, 6]
my_nums = square_numbers(values)

# generator don't hold the entire result in memory
# it yields one result at a time
print(my_nums)

# each time we run the next method, 
# we get the next value that's yielded
print(next(my_nums))

# this is how we iterate through the generator
for my_num in my_nums:
    print(my_num)

# list comprehension with generator
my_nums_2 = (x**3 for x in values)
print(my_nums_2)

# generator to list
my_nums_2 = list(my_nums_2)