# Class Activities (Lecture 7)

'''
0. What's wrong with this while loop and how can you fix it?

'''
# Uncomment the code below and fix it
'''
print("question 0:")
x = 11
while x > 10:
     print(x)
     x -= 1
'''

'''
1. Use a while loop, print out all the numbers between 1 and 10 (inclusive).
'''
print("question 1:")
x = 0
while x< 10:
    x += 1
    print(x)

'''
2. Use a while loop, iterate all the numbers from 1 to 10 (inclusive) 
and print all the numbers that are greater than 3 and less than or equal to 6.
Hint: You must use both comparision operators and logical operators.
'''
'''
x = 1
while x<= 10:
    if x >= 3 and x <= 6:
     print(x)
    x += 1
     '''


print("question 2:")
'''
3. Use a while loop, print out all the numbers between 1 and 100 (inclusive) that are
divisible by BOTH 5 and 9.
Hint: When a is divisible by b, the remainder of a/b is 0.
Recall: How to check an even number? (it is a number that is divisible by 2).
'''
print("question 3:")
x = 1
while x<= 100:
    if x % 5 == 0 and x % 9 == 0:
        print(x)
    x += 1
x = 1


    

'''
4. Use a while loop, print out all the numbers between 1 and 100 (inclusive) that are
divisible by both 5 and 9.
Exit the loop when the number is greater than 50.
You must use break for this question.
'''

print("question 4:")
x = 1
while x<= 100:
    if x % 5 == 0 and x % 9 == 0:
        print(x)
    if x > 50:
        break
    x += 1






'''
5. Use a while loop, print out all the numbers between 1 and 10 (inclusive) 
EXCEPT for those which are divisiable by 3.
You must use continue for this question.
'''

print("question 5:")


x = 1
while x <= 10:
    if x % 3 == 0:
        x += 1
    print(x)
    x += 1

x = 1
while x <= 10:
    if x % 3 == 0:
        x += 1 
    print(x)
    x += 1

x = 0
while x < 10:
    x += 1
    if x % 3 == 0:
        continue
    print(x)