# Class Activities (Lecture 15)

# Outline
# 1 - 2 Exercise questions list operations
# 3 - 4 Exercise question on list methods
# 5 Exercise questions on list functions
# 5.B Exercise questions on using for-loops on lists
# 6 - 7 More practice questions on list methods and functions

## List operations 
'''
1. List concatenation with +
TODO: Create a new list ['a','b','c','d','e','f'] 
        using the lists below
'''
print("QUESTION 1: ")
list0 = ['a', 'b', 'c']
list1 = ['d', 'e', 'f']

a =list0 + list1
print(a)

'''
2. List repetition with *
TODO: Repeat the list below 3 times
        you should see [1, 2, 3, 1, 2, 3, 1, 2, 3]
'''
print("QUESTION 2: ")
list2 = [1, 2, 3]

b = list2 * 3
print(b)

## List methods
'''
3. Given a list below, tasks, representing a to-do list, 
    a) Use append() to add "Go for a walk" to the end of the list
    b) Use insert() to add "Buy groceries" as the SECOND item in the list
    c) Use pop() to remove AND print the LAST task in the list
    d) Use remove() to remove "Read a book" from the list
    e) Use sort() to sort the list alphabetically AND print the sorted list
'''
print("QUESTION 3: ")
tasks = ["Complete homework", "Read a book", "Write a report"]
# write your code below

tasks.append("Go for a walk")
tasks.insert(1, "Buy groceries")
tasks.pop(-1)
print(tasks)
print(tasks[-1])
tasks.remove("Read a book")
tasks.sort
print(tasks)




'''
4. Given a list of colors below,
    a) Use count() to find and print how many times "red" appears in the list.
    b) Use index() to find and print the position of the FIRST "blue" in the list.
    c) Using a for-loop, find and print the indices of all occurrences of "red" in the list.
    d) Use count() to check if "yellow" in the list. 
        If yes, print its position; if no, print a message saying "Yellow is not in the list".
'''
print("QUESTION 4: ")
colors = ["red", "blue", "green", "red", "blue", "red", "yellow"]
# write your code below
#a
print(colors.count("red"))
#b
print(colors.index("blue"))

#c
length = len(colors)
a = 0
for i in range(length):
    if colors[i] == "red":
        print(i)
#d
count_yellow = colors.count("yellow")
if count_yellow == True:
    print(colors.index("yellow"))
else:
    print("not in list")
## List functions - you MUST USE LIST FUNCTIONS, not methods!
'''
5. Consider a list of temperatures (in Fahrenheit) for a week,
    a) Find and print the length of the temperatures list.
    b) Find and print the maximum and minimum temperatures of the week.
    c) Calculate and print the sum of the temperatures.
    d) Calculate and print the average temperature for the week using sum() and len().
    e) Sort and print the temperatures in ascending order.
    f) Sort and print temperatures in descending order.
'''
print("QUESTION 5: ")
temperatures = [72, 75, 68, 79, 71, 73, 78]
# write your code below

leng = (int(len(temperatures)))
print(leng)
max_temp = max(temperatures)
min_temp = min(temperatures)
print(min_temp, max_temp)
sum_temp = sum(temperatures)
avg_temp = sum_temp / leng
print(sum_temp, avg_temp)
a_list = sorted(temperatures, reverse=True)
print(a_list)




## More practice questions on for-loops on lists
'''
5.B Following Q5 above, 
    a) Instead of using sum(), can you use a for-loop to iterate all the numbers in temperature,
        and calculate the sum of those numbers?
        Compare your result in 5-c)
    b) Create an empty list, my_list, and use another for-loop to iterate all the items in temperature, and add all the items
        that are greater than 74 to my_list. Print my_list at the end.
    c) Use another for-loop and range() to iterate all the items in temperature, 
        and print the indices of all the items in temperatures that are greater than 74. You should see 1, 3, 6.
'''
print("QUESTION 5B: ")
# write your code below

sum = 0
for i in temperatures:  #i is temp
    sum += i
print(sum)

my_list = []
for i in temperatures:  #i is also temp
    if i > 74:
        my_list.appened(i)
print("temps greather than 74: ", my_list)

my_index_list = []
for i in range(len(temperatures)):
    if temperatures[i] > 74:  #i is index because of []
        my_index_list.append(i)
print("temp > 74 index list is ", my_index_list)

for temp in temperatures:
    if temp > 74:
        my_index_list.append(temperatures.index(temp))


# More practice questions on list methods and list functions

'''
6. Start with the following list of numbers:
    1) Use the append() method to add the number 5 to the list.
    2) Use the insert() method to insert 15 at the beginning of the list.
    3) Use the pop() method to remove and print the second number in the list.
    4) Use the remove() method to remove the number 7 from the list.
    5) Use the sort() method to sort the list in descending order and print the result.
'''
print("QUESTION 6: ")
numbers = [10, 3, 7, 2, 8]
# write your code below




'''
7. You work for an online marketplace, and you have collected customer review scores for a popular product:
    1) Calculate the total number of reviews.
    2) Find the highest and lowest review scores.
    3) Calculate the average review score.
    4) Sort and print the review scores in both ascending and descending order.
    5) The product manager decides to filter out the lowest score for a better understanding of the product's performance. 
        Remove the lowest score, recalculate the average, and print it.
'''
print("QUESTION 7: ")
reviews = [4.5, 3.8, 4.2, 4.7, 3.9, 4.0]
# write your code below







