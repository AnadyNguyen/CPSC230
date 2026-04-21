# Homework for Lectures 5 & 6
# Rename the file as HW_3_YOURNAME.py


'''
1. Write code that checks if an integer input by the user is positive, negative, or zero.
Print the result in this format: "-5 is negative." suppose -5 is the user's input.
Hint: convert the user input into an integer before doing conditionals. 
Use if-elif-else statements. 
Hint: Refer to the example "The elif Statement" of Page 6 in Lecture 6.
'''
# write your code below
x = int(input())
if x < 0:
    print(f"{x} is negative")
elif x > 0:
    print(f"{x} is positive")
elif x == 0:
    print(f"{x} is zero")



'''
2. Write code to determine if a person is eligible for a discount based on age 
and membership status. 
There are two scenarios where a person is eligible:
    The person is 60 years or older, 
    or, the person is 50 years or older and having a membership.
    Print out "You are eligible for a discount." 
Otherwise, print out "You are not eligible for a discount."
Use if-else and logical operators for this task.
Hint: Refer to the example in "Combining Multiple Conditions" of Page 15 in Lecture 6.
'''
age = 65
is_member = True
if age >= 60 or is_member == True and age >= 50:
    print("You are eligible for a discount")
else:
    print("You are not eligible for a discount.")


# DONOT DELETE the code above; write your code below





'''
3. Can you write a COMPLETE game of "Rock, Paper, Scissors" between two players, and determine who wins the game?
Ask the user for TWO inputs for the players and store them in variables player1_choice and player2_choice.
Comparing these two variables using if-elif-else statements. 
Print WHO wins the game AND HOW in one print statement.
For example, "Player 1 wins! Scissors cut Paper!" (assume player1 chooses Scissors and player 2 chooses Paper.)
If there is a tie, then print "It's a tie. One more time!"
Note: Now, player 1 can choose any of those three options, not just Rock.
'''
# write your code below

player1_choice = input("Player 1, enter your choice (Rock, Paper, Scissors): ")
player2_choice = input("Player 2, enter your choice (Rock, Paper, Scissors): ")

if player1_choice == player2_choice:
    print("It's a tie. One more time!")
elif player1_choice == "Rock" and player2_choice == "Scissors":
    print("Player 1 wins! Rock crushes Scissors!")
elif player1_choice == "Scissors" and player2_choice == "Paper":
    print("Player 1 wins! Scissors cut Paper!")
elif player1_choice == "Paper" and player2_choice == "Rock":
    print("Player 1 wins! Paper covers Rock!")
elif player2_choice == "Rock" and player1_choice == "Scissors":
    print("Player 2 wins! Rock crushes Scissors!")
elif player2_choice == "Scissors" and player1_choice == "Paper":
    print("Player 2 wins! Scissors cut Paper!")
elif player2_choice == "Paper" and player1_choice == "Rock":
    print("Player 2 wins! Paper covers Rock!")

#I think there is a better way to solve this, but how?