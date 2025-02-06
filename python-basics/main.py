
# Set - Unordered collections of unique objects
# my_set = {1, 2, 5, 3, 4, 2, 5}
# print(my_set)
# print(1 in my_set)
# print(len(my_set))
# set_one = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# set_two = {3, 6, 9, 12, 15, 18}
set_one = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_two = {1, 2, 3}
# print(set_one.difference(set_two))
# set_one.discard(10)
# print(set_one)
# set_one.difference_update(set_two)
# print(set_one)
# print(set_one.intersection(set_two))
print(set_two.issubset(set_one))


# Tuple - immutable list
# Less flexible because they can't change. EG no sort, reverse
# More reliable or readable for coder becuase they can't change
# Better performance
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[2])
# print(2 in my_tuple)
# print('two' in my_tuple)
# print(0 in my_tuple)
# new_tuple = my_tuple[1:4]
# print(new_tuple)

# # Dictionary - unordered key:value pair
# dictionary = {
#     'key': 'value',
#     'b': 2,
#     'c': [1, 2, 3]
# }
# print(dictionary.get('key'))
# print(dictionary.get('c')[2])
# print(dictionary.get('d', 'value not found.'))
# # None
# weapons = None
# win_fight = True
# if weapons is None:
#     win_fight = False
# print(win_fight)
# # List unpacking

# a, b, c, *the_rest, d = [1, 2, 3, 4, 5, 6]
# print(the_rest)
# print(d)
# from typing import List

# # List methods
# basket: List[object] = [1,2,3,4,5]
# print(basket)

# # Adding
# basket.append(6)
# print(basket)
# basket.insert(3, 3.5)
# print(basket)
# basket.extend([7, 8, 9])
# print(basket)

# # Removing
# print(basket.pop())
# print(basket)
# basket.pop(3)
# print(basket)
# new_list = basket[:]
# print(new_list)
# new_list.insert(3, "fish")
# print(new_list)
# new_list.remove("fish")
# print(new_list)
# new_list.clear()
# print(new_list)

# more list methods
# basket = [1, 2, 3, 4, 11, 6, 7, 11, 9]
# print(basket.index(11))
# basket2 = ["a", "b", "c", "d", "e", "f", "g", "h"]
# if 'c' in basket2[0:3]:
#     message = "'c' is at index position " + str(basket2.index('c'))
# else:
#     message = "'c' not found."

# print(message)

# # print(basket2.index('c', 0, 2))

# print(basket.count(11))

# basket = ['a', 'x', 'b', 'd', 'c', 'e']
# print(basket)
# print(sorted(basket))  # Prints a new sorted copy of the basket.
# print(basket)
# basket.sort()  # Changes the basket to a new sorted version.
# print(basket)
# basket.reverse()
# print(basket)
# print(basket[::-1])  # Reverses the order of the list.

# print(list(range(1, 100)))
# sentence = '-'
# print(sentence.join(['hi', 'my', 'name', 'is', 'Bob']))
# print(' '.join(['hi', 'my', 'name', 'is', 'Bob']))
# print(sentence)

# Matrix
# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# print(matrix[0][2])

# lists are a form of arrays
# # there are differences between lists and arrays
# li = [1,2,3,4,5]
# li2 = ['a', 'b', 'c']
# li3 = [1,2,'a', True]

# # Data Structure
# # amazon_cart = ['notebooks', 'sunglasses']
# # print(amazon_cart[0])

# # List Slicing
# amazon_cart = [
#   'notebooks',
#   'sunglasses',
#   'toys',
#   'apples'
# ]
# # print(amazon_cart[1:2])
# # print(amazon_cart[1::2])

# # amazon_cart[0] = 'car'
# # print(amazon_cart)

# amazon_cart[0] = 'laptop'
# new_cart = amazon_cart[:]
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart)

# username = input("What is your username? ")
# password = input("What is your password? ")

# password_length = len(password)
# hidden_password = "*" * password_length

# longString = ("Here is a really long string. Here is a really long string. "
#               "Here is a really long string. Here is a really long string. "
#               "Here is a really long string. Here is a really long string. "
#               "Here is a really long string. Here is a really long string. "
#               "Here is a really long string. Here is a really long string. "
#               "Here is a really long string.")
# print(longString)

# print(f"{username}, your password {hidden_password} is {password_length}
#       letters long")
# print(longString)

# from datetime import datetime

# def calculate_age(date_born):
#   today = datetime.today()

#   age = today.year - date_born.year - ((today.month, today.day)
# < (date_born.month, date_born.day))

#   return age

# birth_year = datetime(int(input('What year were you born? (YYYY)')))
# birth_month = int(input('What month were you born? (1-12)'))
# birth_date = int(input('What date were you born? (1-31)'))

# age = calculate_age(birth_year, birth_month, birth_date)

# print(f'Your age is {age}')

# # booleans
# is_cool = False
# is_cool = True
# print(bool(''))


# #Built in functions and methods
# quote = 'to be or not to be'
# print(quote.capitalize())
# print(quote.upper())
# print(quote.find('be'))
# print(quote.replace('be', 'me'))
# print(quote)

# Strings are immutable - cannnot be changed

# # String Indexes
# selfish = 'me-me-me-me'
#           #012345678910
# # [start:stop:stepover], String slicing
# get the string value at index position 6
# print(selfish[6])
# get the string value from index position 0 up until but not including
# index position 8, stepping over every 2nd character
# print(selfish[0:8:2])
# get the string value starting from and including index position 3
# print(selfish[3:])
# get the string value up until but NOT including index position 4?
# print(selfish[:4])
# get the whole string value but step over by 2
# print(selfish[::2])
# get the string value starting at one position from the end of the string
# print(selfish[-1])
# get the whole string stepping over backwards by 1 - reverse order
# print(selfish[::-1])

# formatted strings

# name = 'Johnny'
# age = 55
# print(f'hi {name}. You are {age} years old')


# string concactenation
# print("hello " + "world")
# print(str(100))
# print(type(str(100)))
# #Type conversion
# a = str(100)

# #Escapec Sequence
# weather = "It\'s \"kind of\" sunny"


# 'hi hello there'
# print(type("hi hello there"))
# username = input("what is your username?")
# print("hello " + username)
# long_string = '''
# WOW
# 0 0
# ---
# '''
# print(long_string)


# iq = 190
# user_age = iq/4
# print(iq)
# print(user_age)
# # variables are snake_case and case sensitive.
# # must start with either letter or underscore. Can contain numbers after that
# # variables starting with an underscore are a private variable.
# # variables starting with two underscores are dunder variables.

# # constants
# PI = 3.4 # you can change this value but it is not a good practice.
# # dunder variables __dunder_variable__. Should be left alone.

# # rapidly assign variables values
# a,b,c = 1,2,3
# print(b)

# # expressions vs statements
# # expression is a piece of code that produces a value
# # a statement is an entire line of code that performs an action
# # in the below code iq/5 is an expression because it produces a value
# # and the entire line is a statement because it performs an action.
# iq = 100
# user_age = iq/5

# augmented assignment operator
# some_value = 5
# some_value += 2
# print(some_value)
# some_value -= 3
# print(some_value)

# # Data Types
# # print(type(2 + 4))
# # print(type(2 / 4))
# # print(type(None))
# # print(2 ** 3) # 2 to the power of 3
# # print(6 // 4) # returns integer rounded down
# # print(6 % 4) # returns remainder

# # Math Functions
# print(round(3.6))
# print(abs(-20))

# # Operator Precedence
# print(20 - 3 * 4)
# # ()
# # **
# # * /
# # + -


# #float
# # bool
# # str
# # list
# # tuple
# # set
# # dict

# # Classes -> custom types

# # Specialized Data Types: Not built in python, but are special packages
# and modules that
# # we can use from libraries.

# None # means nothing, absence of value.

# complex # complex numbers. rarely used.

# # bin() returns the binary representation of a number.
# bin(5)
# print(bin(5))
# print(int('0b101', 2)
