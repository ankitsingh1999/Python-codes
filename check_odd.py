"""
@Clever Programmer

Write a function is_odd that takes 
in a number and returns True if it is odd,
otherwise false.

HINT:
Question: What does it mean for a number 
to be divisible by another number?

Answer: number % another_number == 0 
# Gives you true

Ex: 12 % 3 == 0  --> True  
--> This means 12 is divisble by 3.

BONUS CHALLENGE:
Write the function solution in 1 line 
of code without using if statements.

*** SOLUTION ***
"""

# Make sure to un-comment the function line below when you are done.
# Remember to name your function is_even
# Write your code here...
def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False

#bonus challenge
def is_odd(number):
    return number % 2 != 0
       


# Do not remove lines below here,
# this is designed to test your code.

def test_is_odd():
    assert is_odd(2) == False
    assert is_odd(3) == True
    assert is_odd(8) == False
    assert is_odd(100) == False
    assert is_odd(101) == True
    print("YOUR CODE IS CORRECT!")
  
# test your code by un-commenting the line(s) below
test_is_odd()
