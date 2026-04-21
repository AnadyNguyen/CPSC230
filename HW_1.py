# Homework for Lectures 1 & 2
# Remember to save the file before uploading it. 

'''
1. Write code to print out: Hello, what is your name?
    then ask the user to input their name, 
    assign their name to a variable called user_name
    and print out: Hello [their name]
'''
print("Hello, what is your name?")
user_name = (input("Your name:")) 
print("Hello,", user_name)

'''
2. Given variables x and y, can yo write code to assign 9 to x and x + 1 to y, 
    and print out the values of x and y with one statement? Include comments to EACH line
    to explain the code.
'''

x = 9 #assigns 9 to variable x
y = x+1 #uses + operator on variable x and adds 1, then assigns it to variable y
print(x,",", y) #print x and y, with "," string in the middle to separate both variables

'''
3. Write a statement that assigns total_coins with the sum of nickel_count and 
    dime_count to complete the code. Include comments to EACH line
    to explain the code.
'''

# write your code below

nickel_count = int(input("number of nickels:")) #prompts user to input number of nickels and convert it to an integer and assign it to variable nickel_count
dime_count = int(input("number of dimes:")) #prompts user to input number of dimes and convert it to an integer and assign it to variable nickel_count
total_coins = (nickel_count) + (dime_count) #adds variables nickel_count and dime_count and assigns it to variable total_coins
print("The total amount of coins you have is:", total_coins) #prints out string "The total coins you have is", and prints out variable total_coins with it

# write your code above this line

#print(total_coins)