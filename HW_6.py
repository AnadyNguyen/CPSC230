# Homework for Lecture 10

'''
1. Use a for loop and range() function to iterate all the integers from 1 to 10.
    Check each number if even or odd and print out:
    "[number] is even" or "[number] is odd"
'''
print("QUESTION 1: ")
# write your code below

for a in range(1,11):
    if a % 2 == 0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")

'''
2. Ask the user to type a sentence made of a few words. Using a for loop to count the number of 
a's, e's, i's, o's, and u's in that sentence (counting upper and lower cases as the same letter). 
Print out a message letting the user know the count for each letter. 
For example, if the user typed "Amazing, thank you!", the message could be: 
"Your sentence has 3 a, 0 e, 1 i, 1 o, and 1 u"
Hint: 
- Use a for loop to iterate all the character in the string (user input sentence)
        and compare it with a, e, i, o, u, individually, for both upper and lower cases.
        If the same, increment their counter variables individually,
            you should have 5 counter variables.
- Refer to Lecture 10's in-class exercise: Q4.
'''
print("QUESTION 2:")
# write your code below

g = input("type a sentence of a few words: ")
g = g.lower()
a = 0
e = 0
i = 0
o = 0
u = 0
for h in g:
    if h == "a":
        a += 1
    elif h == "e":
        e += 1
    elif h == "i":
        i += 1
    elif h == "o":
        o += 1
    elif h == "u":
        u += 1
print(f"Your sentence has {a} a's, {e} e's, {i} i's, {o} o's, and {u} u's")