# for complex mathematical functions import the Math module

import math



# Print is a Python function to print in the console (akin to console.log in JS)
print("Hello World")

# The code below will print stars in the console 10 times.

print("*" * 10)

# Linting exercise
# 2 + 3

# x = 1

# unit_price = 3

# variables can just be named and be set to a string, boolean, float, 
# multiple lines of strings in between tripple quotes. Booleans have to start
# with a capital letter

# students_cnt = 1000
# print(students_cnt)

# rating = 5.99
# print(type(rating))

# is_published  = False
# print(type(is_published))

# c_name = """
# Many 
# Lines
# """
# the type function will let you know the type of value the variable is 
# assigned to eg for the variable below you should see on console
# <class "str">

# print(type(c_name))

# x, y = 1, 3

# print(x, y)

# x = y = 1

# print(x, y)

# examples of type annotation to differentiate the values named as the same 
# variable, when the first variable is set to an initial type, one cannot set it again as a different type of value.
# name: str  = "Python"

# name: int = 3 

# print(name)

y = [3, 2, 4]

# this gives you the address of the memory location where we have stored
# the variable shown on the console, this original location stays the same
# even if a variable with the same name gets reassigned.

# print(id(y))

# y.append(6)

# print(id(y))
# print(y)

# number of items in an object, eg a list use method len(variable_name_here)
kare = "Nicholas Cage"

# will print the number of letters in the string 13, includes space
print(len(kare))

# will print the first letter of the string based on index number "N"

print(kare[0])

# a negative index will print the last letter of the string "e", this is unique to Python

print(kare[-1]) 

# print(kare[-13]) = print(kare[0])

# another method used to splice or extract letters from an object is used in the format below,
# this will only print the first two letters of a string, the last number after the colon indicates where
# to stop splicing. we should return "Nic", but not the character at index 3 which would be "h"

print(kare[0:3])

# print(kare[0:3]) = print(kare[:3])
# print(kare[0:])  = print(kare) = print(kare[:])

# escape characters \"
# \'
# \\
# \n
# or just use tripple quotes, it acts like a literal on strings
mess = "Pit \"Prog"
# mess = "Pit \"Prog" = mess = """ Pit
                        # Prog
                        # """

print(mess)



# Formatted Strings  - 

fir = "Karen"
las = "Beltran"

# expression evaluated at run time f, can be upper case
full = f"{len(fir)} {las}"
print(full)

# String Methods 

les = " Pi Prog"

# all letters upper case
print(les.upper())
# all letters lower case
print(les.lower())
# first letter in each word upper case
print(les.title())
# trim white space
print(les.strip())
# index of character
print(les.find("pro"))
# replaces a letter on a list with character of choice
print(les.replace("P", "?"))
# to see if something exists in a variable, this should return True or False
print("Prog" in les)
# to see if something does not exist in a variable, this should return True or False
print("Prog" not in les)

# Numbers 
# to print binary form
k = 10
k = 0b10
print(k)

# binary representation
print(bin(k))

# hexadecimal representation
k = 0x12c
print(k)

# hexadecimal format
# print(hex(k))

# complex numbers a + bi, j is an imaginary number

# x = 1 + 2j
# print(x)


# Arithmetic Operations

# x = 10 + 3

# x = 10 - 3

# x = 10 * 3

# float
# x = 10 / 3

# integer division 
# x = 10 // 3

# modulus, remainder
# x = 10 % 3

# exponiential component

# x = 10 ** 3

# print(x)

# augmented assignment operator
# x += 1 = x = x + 1


# Working with numbers, upper case variables tells developers that it is a constant
# and it shouldn't be modified.

PI = 3.14

# round function to round number
print(round(PI))

# absolute function to return absolute value of a number

# print(abs(PI))
# print(math.floor(PI))


# TYPE CONVERSIONS 
# built in function input()
# x = input("x: ")

# print(int(x))
# print(float(x))
# print(bool(x))

# CONDITIONAL STATEMENTS 

age = 25

# no braces in python
if age >= 18:
    print("adult")
    # else if
elif age>= 13:
    print("teenager")
else: 
    print("child")

print("All done!")

# LOGICAL OPERATORS 

# not
first = "May"
last= "June"

# name = f"{first} {last}"
name = ""

if not name:
    print("Please enter name")
else:
    print("Welcome", name)




















