# Create a program with the following:
# A.
# 1. Create a variable name first with value 7.
# 2. Create a variable name second with value 44.3.
# 3. Print result of adding first to second.
# 4. Print result of multiplying first by second
# 5. Print result of dividing second by first

first = 7
second = 44.3
print('first + second is',first + second)
print('first * second is',first * second)
print('Second / first is', second / first)

# B
# What will be the values of a, b, c at the end?
# the values will be
# a = 9
# b = 8
# c = 15

# C.
# Is there a difference between the two lines below? Why?
# name = “john”
# name= ‘john’
name = "john"
name1 = 'john'
print("name = ",name)
print('name1 = ',name1)
# both single quote and double quotes depict string in python
# but it’s sometimes our need to use one type over the other due to the need to print the ' character


# What is the issue with the code below?
my_number = 5+5
#print("Result is: "+my_number)
# The issue the print function can only print strings and the "+" signs in this cases expects a string but gets an integer
# Suggest an edit.
# we could cast the int to string or convert the int to str
print("Result is: " + str(my_number))

# D.
# What will be the output?
x = 5
y = 2.36
print("x + int(y) = ", x+int(y))
# the int() fi=unction will convert the number to integer and round it down to 2 which means the result is 7


# E.
# 1. Create two variables name X and Y.
# 2. Print “BIG” if X is bigger than Y .
# 3. Print “small” if X is smaller than Y.

x1 = int(input('Enter X1:'))
y1 = int(input('Enter Y1:'))
if x1 > y1:
    print("BIG")
if x1 < y1:
    print("Small")

# F.
# 1. Create a variable and initialize it with a
# number 1-4.
# 2. Create 4 conditions (if-elif) which will check
# the variable.
# 3. print the season name accordingly:
# - 1 = summer
# - 2 = winter
# - 3 = fall
# - 4 = spring

season = int(input('Enter season number'))
if season <= 4:
    if season == 1:
        print("Summer")
    elif season == 2:
        print("Winter")
    elif season == 3:
        print("Fall")
    elif season == 4:
        print("Spring")
    else:
        print("issue")

# CHALLENGE:
# Fix the following code, without changing a or b

a = 8
b = "abcd"
# print(a+b)
# we can use the format function to deal with int-> str
print(b+"{} ".format(a))









