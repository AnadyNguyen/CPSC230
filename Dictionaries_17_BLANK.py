# Class Activities (Lecture 17)

'''
Exercise 1: Inventory Management. Use a dictionary to manage a store's inventory.
NOTE: ONLY Use [] operator (NOT methods)
TODO:
a) Create a dictionary named `inventory` with fruit names as keys and their quantities as values. 
     "apples": 30, "bananas": 45, "oranges": 20.
b) Print the current number of bananas in the inventory.
c) The store received a new batch of 25 bananas. Update the quantity in the inventory and print it.
d) A customer bought 5 oranges. Update the quantity in the inventory and print it.
e) Add a new item to the inventory called "pears" with a quantity of 10 and print the inventory.
f) An item has been discontinued - remove 'apples' from the inventory using the square bracket operator.
    Print the updated inventory dictionary.
'''
print("QUESTION 1")
# write your code below
inventory = {"apples": 30, "bananas": 45, "oranges": 20}

bananas = inventory["bananas"]
print(bananas)

inventory.update({"bananas": bananas + 25})
print(inventory)

inventory.update({"oranges": inventory["oranges"] + 5})
print(inventory)

inventory.update({"pears": 10})
print(inventory)

del inventory["apples"]
print(inventory)



'''
Exercise 2: Inventory Management. Use a dictionary to manage a store's inventory.
NOTE: ONLY Use dictionary methods.
TODO:
a) Create a dictionary named `inventory` with sample items as keys and their quantities as values. 
     "apples": 30, "bananas": 45, "oranges": 20.
b) Print the current number of bananas in the inventory. Use get()
c) The store received a new batch of 25 bananas. Update the quantity in the inventory and print it. Use update()
d) A customer bought 5 oranges. Update the quantity in the inventory and print it. Use update()
e) Add a new item to the inventory called "pears" with a quantity of 10 and print the inventory. Use update()
f) An item has been discontinued - remove 'apples' from the inventory and print the quantity of apple to be removed.
    Print the updated inventory dictionary. Use pop()
'''
print("QUESTION 2")
# write your code below

inventory = {"apples": 30, "bananas": 45, "oranges": 20}

bananas = inventory.get("bananas")

print(bananas)

inventory.update({"bananas" : bananas + 25})
print(inventory)
oranges = inventory["oranges"]
inventory.update({"oranges" : oranges + 25})
print(inventory)
rem_item = inventory.pop("apples")
print(rem_item)
print(inventory)

###
#

#

##



# my_dict = {"a" : 1, "b" : 2, "c" : 3}
# for key, value in my_dict.items():
#     my_dict[key] = value * 2
# print(my_dict)



# my_dict = {"a" : 1, "b" : 2, "c" : 3}
# for key, value in my_dict.items():
#     if value >= 2:
#         print(f"Key: {key} has a value >= 2")


