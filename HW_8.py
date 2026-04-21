# Homework for Lectures 13 & 14

'''
1. 
a) Function definition: Write a function, euclidean(), that takes in 4 parameters, x1, y1, x2, and y2,
    and calculate the euclidean distance between two points whose (x,y) coordinates are (x1, y1) and (x2, y2), respectively.
    Return the euclidean distance as a number.
    Make the default arguments 1 for all four parameters.
b) Function calling: Calcuate and print the euclidean distance between two points whose (x,y)
    coordinates are (1, 1) and (2, 2), respectively by invoking the function.
    (your function should return 1.4142..., which is the square root of 2)
NOTE: FULL CREDIT: Use exponent operator ** and other necessary arithmetic operators for this question.

Hint:
    Euclidean distance = square root of (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)
    Refer to the power function in Q3 in the in-class exercise for lecture 13 on
    how to calculate square root.
'''
print("QUESTION 1: ")
# write your code below

#a) 
def euclidean(x1 = 1, y1 = 1, x2 = 1, y2 = 1):
    euclidean_distance = ((x2 - x1) ** 2 + (y2- y1) ** 2) ** 0.5
    return euclidean_distance

x1 = 1
y1 = 1
x2 = 2
y2 = 2
distance = euclidean(x1, y1, x2, y2)
print(distance)

'''
2. There is a triangle of three vertices (i.e., points), whose (x,y) coordinates are (0,0), (2,2), (4,0). 
    a) Create a list of tuples, named coordinates, to store those three vertices. 
    b) Use a FOR-LOOP to iteratue the list of tuples and print all the vertex coordinates 
        in the format of "X: 2, Y: 2".
    c) Calculate the euclidean distances by using the function you defined in Q1(a) 
        between the first two vertices (tuples) in the list, coordinates, 
        Print out the result in this format: 
            "The euclidean distance between (0,0) and (2,2) is [result]"
NOTE: FULL CREDIT: When calling the function and input arguments, 
        use indices to access the first two tupes in the list, coordinates; 
        DO NOT directly use those numbers in the tuples.
Hint: 
    Refer to Page 9 in Lecture 14 on how to access an item in a tuple in a list.  
'''
print("QUESTION 2: ")
# write your code below
coordinates = ((0,0), (2,2), (4,0))
for vertex in coordinates:
    print(f"X: {vertex[0]}, Y: {vertex[1]}")

euclidean(coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1])
result = euclidean(coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1])
print("The euclidean distance between (0,0) and (2,2) is", result)











