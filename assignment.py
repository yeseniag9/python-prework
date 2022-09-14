# Question 1 -
# Write a function to print "hello_USERNAME!" USERNAME is the input of the 
# function. The first line of the code has been defined below.

def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")

hello_name("yesenia")

# Second way to do Question 1

def hello_name(user_name):
    all_caps_user_name = user_name.upper()
    print(f"hello_{all_caps_user_name}!") 

hello_name('yesenia')

# Question 2 -
# Write a python function, first_odds that prints the odd numbers from 1-100 
# and returns nothing.

def first_odds():
    for x in range(1, 100, 2):
        print(x)
    
first_odds()

# Second way to do Question 2

def first_odss():
    i = 1
    while i <= 100:
        if i % 2 == 1:
            print(i)
        i = i + 1

first_odss()

# Question 3 -
# Please write a Python function, max_num_in_list to return the max number of 
# a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    return max(a_list)

print(max_num_in_list([17, 3, 11, 8, 0, 15]))

# Second way to do Question 3

def max_num_in_list_2(a_list):
    current_max = a_list[0]
    for num in a_list:
        if num > current_max:
            current_max = num
    return current_max

print(max_num_in_list_2([4, 9, 12, 1, 7, 0]))

# Question 4 -
# Write a function to return if the given year is a leap year. A leap year is 
# divisble by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (True/False).

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    elif a_year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(2100))
print(is_leap_year(2020))

# Question 5 -
# Write a function to check to see if all numbers in list are consecutive 
# numbers. For example, [2, 3, 4, 5, 6, 7] are consecutive numbers, but 
# [1, 2, 4, 5] are not consecutive numbers. The return should be Boolean type.

def is_consecutive(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i] + 1 != a_list[i+1]: 
            return False
    return True

print(is_consecutive([4, 5, 6, 7, 8, 9]))

print(is_consecutive([4, 5, 7, 8]))