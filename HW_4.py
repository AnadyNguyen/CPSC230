# Homework for Lecture 7

'''
1. Write a while loop that repeats as long as user_input >= 1. 
In each loop iteration, frist floor-divide user_input by 2 
(remember to assign the updated value back to user_input),
then print user_input.
'''

user_input = int(input("Input a number"))
# write your code below

while user_input >=1:
    user_input //= 2
    print(user_input)



'''
2. Write a while loop that only prints out integers that are odd numbers
from 1 to 11 (inclusive), i.e., you should see, 1, 3, 5, 7, 9, 11.
Note: You must use arithmatic operators to explicitly check if a number is odd (not even).
'''
# write your code below
x = 1
while x <= 11:
    if x % 2 != 0:
        print(x)
    x += 1



'''
3. Use a while loop that repeatly asks the user to guess your age. If they
guess too high, print out "wow I am younger than that!". If they guess
too low, print out "hahaha I am older than that!". Once they
guess correctly, print out a message telling them they are right and exit the loop.
Basically, if they guess  it wrong, keep asking them until they get it right! 
Use if-elif-else statements.
Use break to exit the loop.
Hint: Check the example of "break" in Page 16 of Lecture 7 for your reference.
'''
# You must UNCOMMENT the code below and COMPLETE it.

my_age = 18 # you may modify this to whatever age you'd like to check upon
while True:
    user_input = int(input("Guess my age!"))
    if user_input > my_age:
        print("wow I am younger than that!")
    elif user_input < my_age:
        print("hahaha I am older than that!")
    else:
        print("You are right!")
        break

 