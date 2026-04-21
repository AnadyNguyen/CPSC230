# Homework for Lectures 15 & 16


'''
1. Can you manage a guest list based on the requirements below using list methods?
    a) Create a guest list of Alice, Bob, and Cory.
    b) Alice decided to bring two friends, Cory (another Cory) and David, to the party. 
        Use the append() method to add "Cory" and "David" to the list, respectively. 
    c) You realized that you mistakenly added Bob, who won't be attending. 
        Use the remove() method to remove them from the list.
    d) Use the insert() method to add "Eva" to the list, making sure they are the second in the order.
    e) Pop the last person from the list, store their name to a variable, extra_guest, 
        and print a message saying they are on standby.
    f) Use count() to to check if there is any guest named "Cory". 
        If yes, 
            print how many guests are named "Cory"; 
            use index() to find the position (i.e., index) of the FIRST "Cory" in the list 
                and print their position; 
        Otherwise, 
            print "Cory is not in the list".
    g) Finally, print the sorted guest list based on REVERSED alphabetical order.
'''
# write your code below
#list
guest_list = ["Alice", "Bob", "Cory"]
#cory and david
guest_list.append("Cory")
guest_list.append("David")
#bye bye bob
guest_list.remove("Bob")
#insert eva into 2nd
guest_list.insert(1, "Eva")
#pop last person
extra_guest = guest_list.pop()
print(extra_guest, "is on standby.")
#
cory_count = guest_list.count("Cory")

if cory_count > 0:
    print("Number of guests named Cory:", cory_count)
    first_cory_index = guest_list.index("Cory")
    print("The first Cory is at index:", first_cory_index)
else:
    print("Cory is not in the list.") 
#g
print("Final guest list (reversed alphabetical):")
print(sorted(guest_list, reverse=True))







'''
2. Simulate a simple banking system with functions to deposit, withdraw, and check balance.
    a) Create a global variable account_balance initialized to 0.
    b) Write a function, deposit, with one input parameter, amount, 
        that adds the amount to account_balance; no return.
    c) Write a function, withdraw, with one input parameter, amount, 
        that subtracts the amount from account_balance; no retutn.
        ENSURE that the withdrawal does not cause a negative balance. 
        If so, warn the user, and only allow them to withdraw the available amount 
            (i.e., account_balance) and set account_balance to be 0.
    d) Write a function, check_balance, with no input parameter 
        and only prints the current balance; no return.
    e) Perform a series of deposits and withdrawals, and check the balance as below. 
        Deposite $100 => Withdraw $50 => Withdraw $60 => Deposite $30 => Check_balance
       
NOTE: 
    Define all the required functions first and then call them one after another in e);
      Refer to Q1 of the in-class exercise of Lecture 16.
    Clearly EXPLAIN how account_balance has been changed for each action listed above, 
      leading to the final result in your report.
'''
# write your code below

# a) 
account_balance = 0

# b) 
def deposit(amount):
    global account_balance
    account_balance += amount   # add money

# c) 
def withdraw(amount):
    global account_balance
    if amount > account_balance:
        print("Warning: Insufficient funds. Withdrawing remaining balance only.")
        account_balance = 0     # withdraw everything
    else:
        account_balance -= amount

# d) 
def check_balance():
    global account_balance
    print("Current balance:", account_balance)


#e
deposit(100)     
withdraw(50)   
withdraw(60)     
deposit(30)     
check_balance()





