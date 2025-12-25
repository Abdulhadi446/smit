# Question 1: Write Python code to create a variable that stores an integer value. Then write another line of code to print its data type.
from re import S

a = 1
print(type(a))


# Question 2: Write Python code to create a variable that stores a decimal number. Print the value and its data type.
b = 3.14
print(b)
print(type(b))

# Question 3: Write Python code to store your name in a variable and print its data type.
name = "Abdul hadi"
print(type(name))

# Question 4: Write Python code to store a True or False value in a variable and print its data type.
is_true = True
print(type(is_true))

# Question 5: Write Python code to add two numbers and print the result.
num1 = 5
num2 = 10
ans = num1 + num2
print(ans)

# Question 6: Write Python code to join two strings and print the final output.
str1 = "Abdul "
str2 = "hadi"
name = str1 = str2
print(name)

# Question 7: Write Python code that converts a number stored as text into an integer.
num = "123"
numb = int(num)
print(type(numb))

# Question 8: Write Python code that converts an integer into a string.
num = 11
string = str(num)
print(type(string))

# Question 9: Write Python code to check and print the data type of any variable.


def print_type(variable):
    print(type(variable))


print_type("123")


# Question 10: Write Python code that multiplies a string by a number and prints the result.
def print_line():
    print("--" * 20)


print_line()

# Question 11: Write Python code to create a list that stores at least three different data types.

list_3 = [1, 1.1, "AbdulHadi"]
print(list_3)


# Question 12: Write Python code to access and print the first and second values from a list.
def print_second(l):
    print(l[1])


print_second(list_3)


# Question 13: Write Python code to create a dictionary that stores a person's name and age.
persons = {"hadi": 13, "izan": 10}
print(persons)

# Question 14: Write Python code that compares two numbers and prints True or False.
number1 = 1
number2 = 2

if number1 < number2:
    print("Number 2 is bigger", number1 < number2)

# Question 15: Write Python code that checks the data type of each item inside a list.
list_list = [1, 2, 11.1, "hadi", True]

for list_item in list_list:
    print(type(list_item))
