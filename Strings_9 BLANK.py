# Class Activities (Lecture 9)

'''
1. Ask the user to input a random word, assign it to my_string.
First, check if my_string is all uppercased. 
If yes, print out "Good, all're uppercased!".
Otherwise, convert my_string to all uppercase and print out the result.
'''
my_string = input("Choose a word:")
if my_string.isupper():
    print("Good, all're uppercased!")
else:
    new_string = my_string.upper()
    print(new_string)




'''
2. Replace all occurrences of "coffee" with "hot chocolate" and "programmer" 
with "coder". Print out the result.
'''
paragraph = """In the town of Coderville, every programmer loved to drink coffee; 
coffee gave them the energy to code late into the night. 
However, some programmers preferred tea over coffee.""" 
# NOTE: In Python, a pair of triple double quotes like the ones above,
#   creates a multi-line string.
'''
new_paragraph1 = paragraph.replace("coffee," "hot chocolate")
new_paragraph2 = new_paragraph1.replace("programmer," "coder")
print(new_paragraph2)
'''
new_paragraph = paragraph.replace("coffee", "hot chocolate").replace("programmer", "coder")
print(new_paragraph)


'''
3. Ask the user to type AT LEAST two words separated by spaces, 
    store the input to a variable named my_string.
    a. Check if the first character is capitalized (upper case), 
        if yes, print out "[user input]'s first character is capitalized";
        otherwise, print out "[user input]'s first character is NOT capitalized".
        Hint: Access the first character using indexing.
    b. Check if the first character is a number: 0 - 9,
        if yes, print out "[user input]'s first character is a number";
        otherwise, print out "[user input]'s first character is NOT a number".
    c. Print how many words in my_string
        Hint: Split my_strings by space and print the length of the list of tokens.
'''

my_string = input("Choose a few words, separated by spaces:")
if my_string[0].isupper():
    print(f"{my_string}'s first character is capitalized")
else:
    print(f"{my_string}'s first character is NOT capitalized")

if my_string[0].isdigit():
    print(f"{my_string}'s first character is a number")
else:
    print(f"{my_string}'s first character is NOT a number")

my_token = my_string.split(" ")
word_count = len(my_token)
print(f"this string has {word_count} words")