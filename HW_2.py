# Homework for Lectures 3 & 4
# Remember to save the file before uploading it.

'''
1. Write some code that asks the user for 5 different numbers, and stores
them in the variables x1, x2, x3, x4, and x5. Use a set to create a
unique set of numbers entered (e.g. if they enter 5 twice, only count it once.)
Print out the set.
'''

print("Choose 5 numbers:")
x1 = input("1st number:")
x2 = input("2nd number:")
x3 = input("3rd number:")
x4 = input("4th number:")
x5 = input("5th number:")
print({x1, x2, x3, x4, x5})

#Is there a way we can order the set?





'''
2. Create a dictionary variable named student_1 to store the name, age, and major, of a random Chapman Student.
'''
# write your code below
x = input("What is your name?")
y = int(input("how old are you?"))
z = input("What is your Major?")
random_student_1 = {"name" : x , "age": y , "major": z } 
print(random_student_1)
'''
3 Without using Python, figure out the answer to this statement.
    Explain the order of operations IN YOUR WRITTEN REPORT.
    You DO NOT NEED to rewrite the expression using paratheses. 

    2 * 4 + 2 ** 3 // 2 + 6 - 7 * 9 + (16 + 4)

Check your answer using Python by putting the above expression into print() 
NOTE: YOU DON'T NEED TO WRITE ANY CODE FOR THIS QUESTION.
'''

print(2 * 4 + 2 ** 3 // 2 + 6 - 7 * 9 + (16 + 4))


'''
4. Using these operators (%,/,//,*), write some code to convert an amount of
time in minutes (e.g. 257 minuts) into hours and minutes (e.g. 4 hours and 17 minutes).

Instructions: 
    1) Get input minutes from the user using the following statement
        e.g., mins_input = int(input("Please input some minutes: ")). 
    2) Write code to convert mins_input into two variables, X and Y, 
        reprsenting hours and minutes respectively, using operators %, /, //, *.
    3) Print out the numbers of hours and minutes in one statement,
        in the format of "X hours, Y minutes" 

Verify your code using the following values:
- 12938 (answer: 215 hours, 38 minutes)
- 55 (answer: 0 hours, 55 minutes)
- 525,600 (answer: 8760 hours, 0 minutes )
- 432 (answer: 7 hours, 12 minutes)

If you input 12938, and your code prints '215 hours, 38 minutes'
CONGRATS!
'''
# write your code below

mins_input = int(input("Please input some minutes:"))
X = mins_input // 60
Y = mins_input % 60

print(X, "hours,", Y, "minutes")