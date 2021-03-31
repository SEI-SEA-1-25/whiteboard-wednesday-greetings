# Functions begin with def keyword 

# variables in Python are snake_case
my_salutation = 'Hello Snakes '

def greeting(greeting_string):
    print(greeting_string)
    print("im in the function scope")

greeting(my_salutation)


# ## ##

None # is afalsey

# Booleans are capitol 
True
False

# boolean operators 
# && || ! in js
# and or not python
print(None and True)
print(True and False)

#  or like js ||
print(True or None)

# !  in js
print(not False)


truth = True
untruth = False
none = None


# Conditionals

if truth:
    print('its true! I dont like you!')
elif untruth:
    print('I am the untruth')
else:
    print('I actually do like you')


# Integers have no decimals

int
my_int= 14

# floats are decimals 
float
my_float = 3.1


# Complex numbers
6+9j

#addition between ints
print(9 + 14)

#addition between floats
print(9 +14.1)

print('subtraction', 20 - 10)

# two types of division

#division
print('division', 20/3 )

# forced integer division
print('forced int division', 20 // 3)

#  Two types of multiplication


# regular
print('reg mult', 3 *3)

#exponential
print('exponents', 3 **3)

# no plus plus X++

my_num = 5

my_num +=1
print(my_num)


############

#STRINGS

my_string = 'Spam and eggs'

#dir will show us the built in methods
print(dir(my_string))
##  __this_dunder_method_is_private__

# built in type methods
print(my_string.upper())


## Formatting Strings

s = 'spam'
# double quotes & single quotes == string
e = "eggs"


# format strings
print('but I dont like {} with my {}'.format(s, e))

# string format template

## string format templates use keyword arguments or kwargs
template = 'My name is {name} and i dont like {food} with my {other_food}'
formatted = template.format(name='Dave', food=s, other_food=e)
print(formatted)


# f strings are like interpolation from javascript

order = f'Ill take the {s} {s} {s} {s} baked beans and {s} and {e}'
print(order)

# String concatenation

s_e = s + ' and ' + e
print(s_e)

# Libraried function to find out length of string
print(len(s_e))

# Spring Splicing 

print(s_e[-2])
print(s_e[3:8])
print(s_e[:8])
print(s_e[3:])
print(s_e[::2])
print(s_e[::-1])


# LISTS  aka arrays

# split chars into list

l = list(s_e)
print(l)

# list use square brackets
breakfast = ['spam', 34, 'baked beans']

# length of lists
print(len(breakfast))

spam_times_5 = ['spam'] * 5
print(breakfast + spam_times_5)

# Make a list from a range of numbers
range_list = list(range(10))
print(range_list)

# Ranges work on lists
#Returns a new list, does not mutate original

print(breakfast[::-1])

## mutate the list with built in methods
range_list.insert(3, 'eggs')
print(range_list)

# Looping 

for thing in range_list:
    print(thing)

# check if something is in a list

if 'spam' in range_list:
    print('spam is in the list')
else:
    print('spam is not in the list')



# iterative looping

for i in range(len(range_list)):
    print(f'index i {i} {range_list[i]}')


for i, item in enumerate(range_list):
    print(f'index {i}, is {item} (this is the other one)')

index = 0

while index < len(range_list):
    print(range_list[index])
    index += 1


## Dictionaries aka objects

## NO DOT NOTATION

# ALL DATATYPES CAN BE KEYS

#STRINGS MUST BE IN QUOTES AS KEYS LIKE IN JSON

meal = {
    'spam': 5,
    'baked beans': 1,
    True: 'waoh',
    10: 'this is nuts'
}

for food in meal:
    print(f'my meal has {meal[food]} {food} in it')

print(dir(meal))

## INPUT from the command line

# input('the user will see this string')


prompt = '>'

print('enter your age, user')
age = input(prompt)
age = int(age)
print(f'wow! You actually look like youre {age - 5} years old')