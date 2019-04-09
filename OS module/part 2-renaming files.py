
import os

os.chdir(r'C:\Users\neera\Desktop')
print(os.getcwd())

# Let's rename the text file present in the directory
os.rename("demo.txt", "test.txt") # first argument is the original name, second is the name we want to change it to

print(os.listdir())