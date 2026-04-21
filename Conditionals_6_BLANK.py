# Class Activities (Lecture 6)

'''
** Update your previous code to use if-elif-else statements instead. **
Let's implement a simpler version of the game "Rock, Paper, Scissors" using conditionals.
* Rock crushes Scissors
* Scissors cuts Paper
* Paper covers Rock
1. Get two inputs from the user and stored them in variables player1_choice and player2_choice
2. Compare their choices:
    Assume player 1 always chooses 'Rock'
        i.e., assign 'Rock' to player1_choice
    When players 1 and 2 choose the same: print "It's a tie!"
    If player 2 chooses Scissors, print "Player 1 wins! Rock crushes Scissors!"
    If player 2 chooses Paper, print "Player 2 wins! Paper covers Rock!"
'''
# write your code below
'''
player1_choice = "Rock"
player2_choice = input("Player 2, Choose Rock, Paper, or Scissors:")

if player2_choice == player1_choice:
    print("It's a tie!")
elif player2_choice == ("Scissors"):
    print("Player 1 wins! Rock crushes Scissors!")
elif player2_choice == ("Paper"):
    print("Player 2 wins! Paper covers Rock!")
else:
    print("Please only type Rock, Paper, or Scissors")
'''



'''
Ask the user to input an integer and store it in the variable x.
Convert the value of x into an integer. 
Check whether the number is even and greater than 17.
If yes, print "Yes!"; otherwise, print "No."
Use if-else statement and a logical operator.
Hint: an even number can be exactly divided by 2, leaving a remainder of 0. 
'''
# write your code below
'''
x = int(input("Pick an integer:"))
if x % 2 == 0 and x > 17:
    print("Yes!")
else:
    print("No")
'''

'''
You are designing a system for a park to determine whether a visitor 
is allowed to enter based on their age and height.

Write a program that:
* Asks the user for their age (integer input)
* Asks the user for their height (in centimeters, float input)
* The visitor can only enter the park if they are AT LEAST 10 years old
    AND AT LEAST 120.0 cm tall.
* If they don't meet either condition, deny their entry with a message
    letting them know the reason (e.g., "You must be at least 10 years old").
* Otherwise, print a message to welcome them!

Use if-else and logical operators (and/or) for this question.
'''

# write your code below

user_age = int(input("What is your age?"))
user_height = float(input("What is your height in centimeters?"))
if user_age >= 10 and user_height >= 120.0:
    print("Welcome!")
elif user_age < 10 and user_height < 120.0:
    print("You meet neither requirement")
else:
    if user_height < 120.0:
        print("you dont meet the height requirements")
    if user_age < 10:
        print("You dont meet the age requirement")

'''
elif user_age<10:
    print("Sorry, we cannot let you enter, you don't meet the age requirements")
if user_height < 120.0:
    print("You are not tall enough")
elif user_age < 10 and user_height < 120.0:
    print("You are neither tall enough or old enough")
    '''