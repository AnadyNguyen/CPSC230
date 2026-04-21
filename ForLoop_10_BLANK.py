# Class Activities (Lecture 10)

'''
1. Use a for loop and range() to create integers from 0 to 5 (inclusive) and print them out.
'''
print("QUESTION 1:")
# write your code below
i = 0
for i in range(6):
    print(i)


'''
2. Use a for loop and range() to create integers from 0 to 5 and print them out.
Use a counter variable to count iteration number and print it out after the for loop.
'''
print("QUESTION 2:")
# write your code below
counter = 0
for a in range(6):
    print(a)
    counter += 1
print("# of iterations:", counter)

'''
3. Use a for loop to iterate a list of numbers, use counter variable num_neg 
    to count the number of negative numbers (< 0), and print the result.
'''
print("QUESTION 3:")
numbers = [30, 20, 2, -5, -15, -8, -1, 0, 5, 35]

# write your code below
num_neg = 0
for b in numbers:
    if b < 0: 
        num_neg += 1
print(f"total number of neg numbers is: {num_neg}" )
    



'''
4. Ask the user to input two words of the SAME LENGTH. If they give words of the same length,
use a for loop, count how many corresponding letters are the same in the two strings. 
For example in 'spam' and 'span', 3 of the letters (s,p,a) are the same. 
In the words 'bitter' and 'better',5 of the letters are the same. 
Print out a message telling the user how many letters are the same.
Hint: 
 1. Get both words' lengths and compare.
 2. Access the corresponding charaters of the same index in both words and compare them.
'''
print("QUESTION 4: ")
# write your code below

x = input("choose a word of the same length: ")
o = input("Choose another word of the same length: ")
counter = 0
len1 = len(x)
len2 = len(o)
if len1 == len2:
    for i in range(len1):
        if x[i] == o[i]:
            counter += 1
else:
    print("two words must be same length")
print(f"your words have {counter} letters of the same")