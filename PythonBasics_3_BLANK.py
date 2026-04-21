# Class Activities (Lecture 3)

# Numbers
'''
Create a variable x and assign a random integer (e.g., 5) to it and 
print it and its type in one statement
'''

x = 10
print(x, type(x))

'''
Create a variable y and assign a random float (e.g., 1.3) to it and 
print it and its type in one statement
'''

y = 26.7
print(y, type(y))

# strings
'''
Create a string consisting of all types of characters:
numbers, letters, symbols, and spaces.
Print out the string and its type.
'''

string = "1b$"
print(string, type(string))

# List
'''
Create a list of 1, 2, 3, 4, 5
'''

my_list = [1,2,3,4,5]
print(my_list)
'''
Create a list consisting of a string, an integer, a float
and a list.
Print out the list and its type.
'''

another_list = ['string', 4, 3.2, [1,2,3]]
print(another_list, type(another_list))

# Dictionary
'''
Create a variable of dictionary, named cpsc230
- keys are 'Name', 'School', 'Credits'
- values are 'Computer Science I', 'Engineer', an integer of 3
- Print out the dictionary and its type.
'''

cspc230 = {"Name": "Computer Science I", "School": "Engineer", "Credits": 3}
print(cspc230, type(cspc230))

# Set
'''
Create a set called my_set, consisting of 1, 2, 3, 4, 5, 5, 5, 6 
Print out my_set. Did it change at all? 
Explain why.
'''

my_set = {1,2,3,4,5,5,5,6}
print(my_set)

# Type conversions
'''
Create two variables, a and b, assigned with '1.3' and '5', respectively
Convert the first variable into a float 
Convert the second variable into an integer
Sum them up and assign the result to another variable, c
Print out the value of c, and its type.
Explain why the result is that type.
'''

a = "1.3"
b = "5"
a = float(a)
b = int(b)
c = a + b
print(c, type(c))
