# Class Activities (Lecture 14)

## lists
'''
0. Access a list of lists.
'''
recipe_ingredients = [["cheese", "chicken", "tomato sauce", "basil", "breadcrumbs"],
["chickpeas", "cucumber", "tzatziki", "tomatoes", "onion"],
["hamburger", "bun", "ketchup", "lettuce", "pickles", "mayo"],
["white beans", "celery", "diced tomatoes", "shallots", "broth"]]

print("QUESTION 0: ")
# TODO: Get 'tzatziki' from recipe_ingredients using indexing 
#          and store it to variable, ingredient. 
#           print the variable to check the result -> you should see 'tzatziki'

print(recipe_ingredients[1][2])

# Count the number of ingredients in the recipe in total. 
#   Print the total number to check your answer. (The total number is 21)
# Hint: Use len() to get the number of items in a list
#       Use for loop to iterate each sub-list to get the number of items and sum them up
# TODO: write your code below

b = len(recipe_ingredients)
print(b)
counter = 0
counter1 = 0
for i in recipe_ingredients:
    for a in i:
        counter1 += 1
print(counter1)

# If one's allergic to gluten, how to replace "bun" with "gluten-free bun" in recipe_ingredients?
#   print recipe_ingredients to check your answer.
# TODO: write your code below

recipe_ingredients[2][1] = "gluten-free bun"
print(recipe_ingredients)

'''
1. Read and run the code below. Turn this while loop into a for loop.
    To check your answer, use ''' ''' to comment out the while loop (DO NOT comment my_list)
'''
print("QUESTION 1: ")
my_list = ["music", "lego", "netflix", "tech", "tennis", "pets", "coding"]

# While loop version
# i = 0
# while i < len(my_list):
#     print("I like " + my_list[i])
#     i += 1

# TODO: write your code below
# For loop version

counter = 0
for i in my_list:
    print("I like " + my_list[i])



'''
2. Change the first item of my_list (from Q1) to be 'sun'
'''
print("QUESTION 2: ")
# TODO: write your code below
my_list[0] = "sun"



'''
3. Create a tuple, my_tuple, using the same items in my_list in Q1.
Then, change the first item to be 'ocean'. 
Does it work? Why?
'''
print("QUESTION 3: ")
# TODO: write your code below
my_tuple = ("music", "lego", "netflix", "tech", "tennis", "pets", "coding")



'''
4. Create a shopping list: apple (count: 1), banana (count: 2), cherry (count: 3), dragonfruit (count 4)
    a. Construct a list of tuples, shopping_list, with each tuple containing a fruit above and its amount, say ("apple", 1).
    b. Print the fruit name whose amount is 2. (You should see "banana")
Hint: 
    Use a for loop to iterate shopping_list and only print the first item of a tuple, whose second item is 2.
'''
print("QUESTION 4: ")
# TODO: write your code below





