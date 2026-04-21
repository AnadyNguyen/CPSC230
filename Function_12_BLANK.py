# Class Activities (Lecture 12)
import random

# example: generate a random number between 0 and 9 (inclusive)
x = random.randint(0, 9)
print(x, "is a random number between 0 and 9, inclusive")


'''
0. randint(a, b) is a function from a built-in library named random (see above import random)
that can be used to generate a random integer, N, between two integers (inclusive), a and b, where a <= N <= b.
PART 1: Define a function, named random_sum, that takes two input parameters, a and b (a < b),
    and generates two random numbers between a and b and return their sum.
PART 2: Invoke (use) the function to calculate the sum of two random numbers between 1 and 100 (inclusive)
and print the result.
'''
print("QUESTION 0 ---------------")
# write your code below

def random_sum(a,b):
    num1 = random.randint(a = a, b = b)
    print(f"1st num: . {num1}")
    num2 = random.randint(a = a, b = b)
    print(f"2nd num: . {num2}")
    res = num1 + num2
    return res

result = random_sum(a = 1, b = 100)
print(result)




'''
1. Ask the user for their name, and print a welcome message to the user, e.g., "Welcome, [name]!", using a function:
    PART 1: Define a function with one input parameter, name, that prints a welcome message using that parameter.
    PART 2: Ask the user for their name, invoke (use) the function and input that name to the function as an argument.
Hint: 
- The function has no return statement.
'''
print("QUESTION 1 ---------------")
# write your code below

def user_name(name):
    print("Welcome,", name)

user = input("your name:") 
user_name(name = user)


'''
2. PART 1: Define a function that calculate a rectangle's perimeter based on
   input parameters: length and width. Return the calculated perimeter as output.
        Hint: rectangle's perimeter is 2 * (length + width). 
   PART 2: Invoke (use) the function you just defined to calculate the perimeter 
   of a rectangle of length 5 and width 3 and print the result.
'''
print("QUESTION 2 ---------------")
# write your code below

def rectangle (l, w):
    perimeter = 2 * (l + w)
    return perimeter

l1 = 5
w1 = 3
result = rectangle(l = l1, w = w1)
print(result)

'''
3. PART 1: Define a function that returns True if the input parameter, number, is greater than 10,
    and returns False otherwise.
   PART 2: Use the function's return as part of if/else to check 
    the input argument from the user and print out:
     "[argument] is greater than 10" or "[argument] is not greater than 10"
'''
print("QUESTION 3 ---------------")
# write your code below

def greater_than_10 (number):
    if number > 10:
        return True
    else:
        return False
num = int(input("enter a number: "))
result + greater_than_10(number = num)
if result:
    print(f"{num} is greater than 10")
else:
    print(f"{num} is not greater than 10")

