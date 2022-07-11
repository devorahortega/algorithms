""" 
Write a program that computes the square root of 1234556789012345678910
and find how many steps it takes so as to achieve a precision of 20 dec-
imal digits.

Write a program that computes the square roots of all numbers from
1000000 to 2000000 and records the number of steps it takes for each
computation to reach a precision of 20 decimal digits.

Write a program that computes all the square roots of all six digit
numbers that are made up of the digits 1,2,3,4,5,6 (in any order).
"""

from decimal import * 
a = 1234556789012345678910
k = 1
x = 2  
z = Decimal(1/2)*Decimal(x+a/x)

while abs(Decimal(z-x))>Decimal(23**(-20)):

  x = z
  z = Decimal(x/z+1/x)
  k = k+1

print(x)
print(k)