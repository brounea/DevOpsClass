# # A.
# # 1. Create two numeric variables named X and Y.
# # 2. Print the word “BIG” if the value of X is bigger than Y .
# # 3. Print the word “small” if the value of X is smaller than Y.
# #
# x = 5
# y = 8
# if x > y:
#     print("BIG")
# if x < y:
#     print("Small")
#
# # B.
# # 1. Run a “for” loop 5 times.
# # 2. Print the iteration number every time.
# #
# for i in range(5):
#     print(i)
#
# # C.
# # 1. Create a variable and initialize it with a number 1-4.
# # 2. Create 4 conditions (if-elif) which will check the variable
# # value.
# # 3. print a different season name for each number:
# # For example:
# # - 1 = summer
# # - 2 = winter
# # - 3 = fall
# # - 4 = spring
# #
# season = int(input('Enter season number'))
# if season <= 4:
#     if season == 1:
#         print("Summer")
#     elif season == 2:
#         print("Winter")
#     elif season == 3:
#         print("Fall")
#     elif season == 4:
#         print("Spring")
#     else:
#         print("issue")
#
# # D.
# # 1. how many times will the following loop run?
# # 2. what will be printed last?
# #
# count = 1
# while count<11:
#     print(count)
#     count =+1
#The code will run indefinitely b/c the count increment will not happen inside the while loop
# # E.
# # Write a program with variables holding the following:
# # 1. Your age.
# # 2. First letter of your last name.
# # 3. Current shekels-dollar currency.
# # 4. Did you flew abroad (true/false)
# # 5. Your apartment number.
# #
# # ● Print all variables.
# # ● Add the currency(3) to your age(1), and check the result.
# #
# my_age = 55
# first_letter_fn = 'B'
# current_conversion = 3.2
# did_i_fly = True
# aprt = 0
# print(my_age)
# print(first_letter_fn)
# print(current_conversion)
# print(did_i_fly)
# print(aprt)
# print(my_age + current_conversion)

# # F.
# # Create a program which uses input with the following:
# # 1. Ask user for his phone number
# # 2. Print the words “phone number” and the phone number
# # the user entered.

#
# F.
# Create a program which uses input with the following:
# 1. Ask user for his phone number
# 2. Print the words “phone number” and the phone number
# the user entered.
#
# phone = int(input('Enter phone number'))
# print('Phone number :' + phone)

# G.
#
# Write a program with the following:
# 1. Function named printHello() that prints the word “hello”.
# 2. Function named calculate() which adds 5+3.2 and prints the
# result.
#
# def printHello():
#     print('Hello')
#
# def calculate()
#     print(5 + 3.2)
# H.
# Write a program with the following:
# 1. Function that receive a name as an argument and prints it.
# 2. Function that receive a number, divide it by 2, and prints the
# result.
#
# def myprint(myname):
#     print(myname)
#
# def mydivide(mynumber):
#     print(mynumber / 2)


# I.
# Write a program with the following:
# 1. Function that receive two numbers, add them, and return the
# sum.
# def myadd(num1, mun2):
#     return num1 + mun2

# 2. Function that receive two Strings, add space between them,
# and return one spaced string.
#
# def myconct(str1, str2):
#     return str1 + ' ' + str2
# J.
# Create a program with the following:
# 1. Create an array with 3 numbers
# 2. Iterate through the array to print all elements.
#
# myarry = [1,2,3]
# for i in myarry:
#     print(i)

# K.
# Create a program which will get a list of numbers and prints the
# sum of all items.
# lst = [1,2,3,4,5,6]
# sm = 0
# for i in lst:
#     sm = sm + i
# print(sm)
#
# L.
# Write a Python program to iterate over dictionaries and prints all keys
# using for loop
#
#my_dictionary = {'a': 1,'B': 2, 'C': 3}
# for i in my_dictionary:
#     print(my_dictionary[i],i)

#
# Challenges:
# M.
# Create a nested for loop (loop inside another loop) to create
# a pyramid shape:
#rows = int(input('Enter row number'))
# rows= 5
# for i in range(0, rows):
#     for j in range(0, i+1):
#         print('* ',end="")
#     print("\r")

# N.
# Create a nested for loop to create X shape (width is 7,
# length is 7):
len = 7
for i in range(0,len):
    for j in range(0,len):
        #print(i,j)
        if (i==j or j==len-1-i):
            #print(i, j,len-1-i)
            print("*",end="")
        else:
            print(" ",end=" ")
    print()




# O.
# Write a program with the following:
# 1. Function that gets a number from the user (using input).
# 2. Function that receive the number from the first method, and
# computes the sum of the digits the integer (e.g. 25 = 7,
# 2+5=7)
#
#
# def digit_sum(num):
#     dstr = str(num)
#     sm=0
#     for elm in dstr:
#         sm = sm + int(elm)
#     print(sm)
#
# num = int(input('Enter number'))
# digit_sum(num)




# P.
# Write a Python program to convert a tuple to a string.
#
# x_tuple = 1,2,3,4,5,'seventeen'
# newstr = ""
# for elm in x_tuple:
#     newstr += str(elm)
# print(newstr)

# Q.
# Write a Python program to get the smallest number from a list.

# lst = [1,2,3,4,5,6]
# min= lst[0]
# print(min)
# for elm in lst:
#     if elm < min:
#         min = elm
# print(min)

