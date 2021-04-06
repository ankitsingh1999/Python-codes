"""
@Clever Programmer

Write a function biggest_guy that takes in
three numbers as input and returns the biggest one.

MAKE SURE to use RETURN and not PRINT in your function.
Ex: biggest_guy(10, 30, 20)  # --> 30

BONUS CHALLENGE: Write a 1 line solution (Medium Difficulty)
HINT: Maybe use the bigger_guy function...
"""

# Make sure to un-comment the function line below when you are done.
# Remember to name your function correctly.
# WRITE YOUR CODE HERE...
'''def biggest_guy(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
print(biggest_guy(100,25,50))'''
        

#One more way
#i did not get it because it could take three numbers at a time so how can we compare three numbers at the same time
def bigger_guy(num1, num2):
  if num1 > num2:
    return num1
  else:
    return num2


def biggest_guy(num1, num2, num3):
  # find bigger guy between num1 and num2
  # find biggest guy between bigger guy and num3
  return bigger_guy(bigger_guy(num1, num2), num3)
print(bigger_guy(10,20))

# DO NOT remove lines below here,
# this is designed to test your code.

def test_biggest_guy():
    print("__________Running test________")
    assert biggest_guy(1, 3, 2) == 3
    assert biggest_guy(30, 10, 20) == 30
    assert biggest_guy(20, 10, 30) == 30
    assert biggest_guy(2, 1, 9) == 9
    assert biggest_guy('a', 'a', 'b') == 'b'  # 'b' is greater than 'a'
    print("success!")
    print("your code is correct!")
# test your code by un-commenting the line(s) below
test_biggest_guy()
