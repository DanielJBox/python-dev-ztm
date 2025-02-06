# is_old = False
# is_licenced = False

# if is_old: 
#     print('you are old enough to drive')
# elif is_licenced:
#     print('you can drive now!')
# else: 
#     print('checkcheck')

# if is_old and is_licenced: 
#     print('you can drive')
# else: 
#     print('sorry you can\'t drive')

# Ternary operator
# is_friend = True
# can_message = "message allowed" if is_friend else "not allowed to message"
# print(can_message)

# Short Circuiting
# Occurs when doing conditionals. If False and True. Here the program won't even look at
# the True because the False has already rendered it meaningless to the program flow.
# Same goes for or.

#Logical Operators
# print('a' > 'A')
# print('a' > 'b')

# is_magician = True
# is_expert = False

# # Check if magician AND expert: "you are a master magician"
# if is_magician and is_expert:
#     print("you are a master")
# # Check if magician but not expert: "at least you're getting there"
# elif is_magician and not is_expert:
#     print("at least you're getting there")
# # if you're not a magician: "You need magic powers"
# elif not is_magician:
#     print("You need magic powers")

# For Loops
# for item in 'Zero to Mastery':
#     print(' - ' + item)

# counter
# myList = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for item in myList:
#     sum += item
# print(sum)

# range
# for num in range(0, 100, 2):
#     print('printing ' + str(num) + ' from 0 to 100 steping over by 2')

# enumerate
# for i,char in enumerate('hello'):
#     print(i,char)

# for i,char in enumerate(list(range(10, 60))):
#     if char == 50:
#         print(f'index of 50 is {i}')

# While loop
# i = 1
# while i <= 50:
#     print(i)
#     i += 1
#     # a 'break' here would break out of the loop completely and skip the else below
# else:
#     print('done with the job')

# counter = 0
# myList = list(range(1,11))
# print(myList)
# while counter < len(myList):
#     print(counter, myList[counter])
#     counter += 1

#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
# picture = [
#   [0,0,0,0,0,0,1,1,0],
#   [0,0,0,0,0,1,0,0,1],
#   [0,0,0,0,1,0,0,0,0],
#   [0,0,0,1,1,1,0,0,0],
#   [0,0,1,1,1,1,1,0,0],
#   [0,1,1,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1,1,1],
#   [0,0,0,0,1,0,0,0,0],
#   [0,0,0,1,1,1,0,0,0],
#   [0,0,0,1,1,1,0,0,0]
# ]
# gui = ''
# for row in picture:
#     for on in row:
#         char = '*' if on else ' '
#         print(char, end='')
#     print('')
# print('My Grinch Christamas tree.')

# What is good code
# - Clean. 
# -- Follows a consistent style supported by the wider community and team. 
# -- No uneccessary code.
# -- Does not repeat itself. 
# -- Each block of code / function does one thing well.
# - Readable. 
# -- variable names that make sense are consistent and follow guidelines.
# -- Use comments where needed.
# -- Don't make me think.
# - Predictability
# -- You can easily predict what a section of code does.
# - DRY
# -- Make code reusable.

# Exercise: Check for duplicates in a list:
# def duplicates_from_list(list):
#     duplicate_list = []
#     for letter in list:
#         if list.count(letter) > 1:
#             if letter not in duplicate_list:
#                 duplicate_list.append(letter)
#     return duplicate_list

# def display_duplicate_list(list):
#     for item in list:
#        print(f'{item} is a duplicate in this list') 

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicate_list = duplicates_from_list(some_list)
# display_duplicate_list(duplicate_list)

# Functions
# def say_hello():
#     print('hello')

# say_hello()

# arguments vs parameters
# When we call a function we can pass it arguments
# A function has parameters that can be used in the function
# The passed arguments become function parameters
# def say_hello(name, emoji):
#     print(f'hello {name} {emoji}')

# say_hello('John', ':)')

# Default Parameters and Keyword Arguments
# Positional arguments and parameters have to be in the order you'd expect
# Keyword arguements allow us to not worry about the position.
# say_hello(emoji = ':0', name = 'Bibibubi') # Bad practice? Keep in order. Keep simple.

# Default Parameters
# def say_hello(name = "Darth", emoji = ">("):
#     print(f'hello {name} {emoji}')

# say_hello()

# Return
# A function should do one thing really well
# A function should return something
# def mySum(num1, num2):
#     return num1 + num2

# print(mySum(4, 5))

# age = input("What is your age?: ")
# def checkDriverAge(age = 0):
#     age = int(age) if isinstance(age, int) else 0
#     if age < 18:
#         return "Sorry, you are too young to drive this car. Powering off"
#     elif age > 18:
#         return "Powering On. Enjoy the ride!"
#     elif age == 18:
#         return "Congratulations on your first year of driving. Enjoy the ride!"
# print(checkDriverAge(age))
#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.


# # Methods vs Functions
# # A function can be called by itself - input()
# # A method belongs to something - 'string'.capitalize()
# # Methods are owned by an object or a data type
# # Function:
# print('something')
# # Method:
# 'string'.capitalize()



# # Docstrings - Gives documentation that is usable by and editor for EG
# def test(a):
#     '''
# Info: Tests and prints param a
#     '''
#     print(a)

# test("234")
# # test()

# print(test.__doc__)



# Clean Code note: Refactor to make clearer and leaner



# # args *args and kwargs (keyword arguments) **kwargs
# def super_func(greeting, *args, **kwargs):
#     total = 0
#     print(greeting)
#     for val in kwargs.values():
#         total += val
#     return sum(args)  + total
    
# print(super_func("hello", 1, 2, 3, 4, 5, num1=5, num2=10))
# print(super_func(30, 1, 2, 3, 4, 5, num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs




# # print highest even number exercise
# # REFACTOR TO TWO SEPARATE FUNCTIONS TO MAKE SURE THEY ONLY DO ONE THING EACH?
# def highest_even(num_list):
#     '''
#     returns the highest even number from a list
#     '''
#     return max(evens_list(num_list))
    

# def evens_list(list):
#     '''
#     Takes a list of numbers and returns a list of only the even numbers from that list
#     '''
#     evens = []
#     for val in list:
#         if is_even(val):
#             evens.append(val)
#     return evens

# def is_even(num):
#     '''
#     Takes a number and returns True if it is even otherwise it returns false.
#     '''
#     return not num % 2

# print(highest_even([12, 3, 6, -8, 14, 6, 2, 17]))

# Scope 
# The only time we create new, non-global, scope is when we define a function.
# Pythons Scope Rules
# 1 - Start with local scope
# 2 - Parent local scope. EG is function that contains this function
# 3 - Global scope
# 4 - Built in python functions
# total = 100 # a part of the global scope

# def some_func():
#     print(total)

# some_func()

# total = 0

# def count():
#     global total # Not best practice. Use dependency injection instead.
#     total += 1
#     return total

# print(count())
# print(count())
# print(count())

# global and nonlocal are there for a reason but avoid if can to make 
# your code predictable and readable.

x = int(5)
print(x)