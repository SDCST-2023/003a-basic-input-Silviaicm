#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

import math
a= input("Please input the value you wanna give to a")
b= input("Please input the value you wanna give to b")
c= input("Please input the value you wanna give to c")

a=int(a)
b=int(b)
c=int(c)

X=(c-b)/a

print(f"The value of x is {X}")
