# Class Activities (Lecture 4)

'''
Without using Python, figure out the answer to this statement.

    10 + 2 ** 3 - (4+5) + 49/7 * 2

1. What's the Answer? BONUS: will this be a float or int? 
2. What Order should we go in? 
3. Rewrite this expression using more parenthese to make it
    clearer on what order things are run in.
4. Check your answers using Python.
'''
# your answers here

 #1. float, because division returns a float
 #2. parentheses, exponent, divide and multiply, and addition and subratction, left to right for same precedence of operators
 #3. (10-(4+5)) + 2 ** 3 + 49/7 * 2 
print(10 + 2 ** 3 - (4+5) + 49/7 * 2)
print((10-(4+5)) + 2 ** 3 + 49/7 * 2 )

'''
Using Comparison operators and arithmetic operators, make a complicated 
expression (use at least 5 operators, repeats allowed) that evaluates to False.
Check your answer by printing out the result of the expression (should be a False).
'''
# your answer here

a = 42/7 + 8 ** 2 - (9+6) - 5 <= 0
print(a)