# Homework for Lectures 8 and 9

'''
1. Create a string 'Hello World!' and store it to a variable named str1.
    a. Print out charater 'r' in this string using index.
    b. Slice this string to get 'World' and assign it to another variable named str2 and print it.
'''
str1 = 'Hello World'
print(str1[8])
str2 = str1[6:11]
print(str2)



'''
2. Write some code that asks the user to enter the course code (e.g., CPSC 230)
for one of their classes. Then print out "Great! [Course] sounds like a fun class!",
and ask them if they want to input another course that they're in. You should
stop asking them for course codes once they enter an empty string "" instead of
a course code (you'd do this by not entering anything in the terminal and just
pressing Enter/Return immediately).
Hint:
    Refer to Question 4 of lecture 8's in-class exercise for checking empty strings.
'''


    
while True:
    course_code = input()
    if course_code == "":
        break
    print(f"Great! {course_code} sounds like a fun class!")



    



'''
3. Ask the user to enter a password containing at least two words separated by spaces
    and store it in a variable named my_password. 
    Evaluate the password to see if it meets ALL the four criteria:
        1) At least 10 characters long
        2) NOT start with a number
        3) Start with a capital letter (upper case)
        4) Contains at least two words
    If ANY of those criteria is not met, tell them WHY, e.g., "Your password is shorter than 10 characters."
        and ask for another password. Continue asking them if their password is invalid.
    Otherwise, if their password is good, print "Password accepted!" and exit the loop.
- 
Hint:
    Refer to Question 3 of lecture 9's in-class exercise on how to evaluate a string (password).
    For 4), you may find Pages 15-17 of Lecture 9's slides helpful.
    Use if-elif-else to check all the criteria and print out the messages.
'''


# FOR FULL CREDIT, YOU MUST UNCOMMENT the code below and COMPLETE it.

while True:
    my_password = input("Please enter a password containing at least two words separated by spaces: ")
    my_tokens = my_password.split()
    if len(my_password) < 10:
        print("Your password needs to be 10 characters or more")
    elif my_password[0].isdigit():
        print("Your password cannot start with a number")
    elif my_password[0].isupper() == False:
        print("You need a capital letter in the first letter")
    elif len(my_tokens) < 2:
        print("You need 2 words seperated by a space")
    else:
        print("Password accepted!")
        break





    ###  write your code below ###   
     #TODO: split the password into toke  ns and store the result to my_tokens


    
    # TODO: Use if-elif-else check the criteria and print the messages


