# Class Activities (Lecture 2)

## Some examples about input("some message"), int(), and int(input())
# input("some message"):
'''
classname = input("What is this class? ")
print("This class is ", classname)

# int()
num_5 = int('5') # convert '5' to 5
num_6 = int('6') # convert '6' to 6
total_num = num_5 + num_6 # calculate the sum
print("The total number is: ", total_num)

# int(input()): convert user input number into an integer number
user_input_number = int(input("Please type in a whole number: "))
print(user_input_number)  
'''

## TODO: Below are in-class exercise for Lecture 2
'''
1: Create a variable called number_of_units and assign 3 to it
    Then in the next line, print out number_of_units
'''

number_of_units = 3
print(number_of_units)

'''
2: What's wrong with the following lines of code? can you fix it?
print out the student's name by using its variable
'''

#uncomment the code to see what's happened?

Second_Student = ("Jane") 
print(Second_Student)



'''
3. The code below calculates the area of a triangle. Add comments to 
each line explaining what it is doing.
'''
base = 10 #assigns value of 10 to variable base
height = 3 #assigns value of 3 to height variable
area = base * height #mutiplies base and height variables and assigns it to area variable
area = area/2 #divides value of area variable by 2 and assign result back to variable area
print("The triangle area is", area) #prints string : "the triangle area is:" and then "area variable"
