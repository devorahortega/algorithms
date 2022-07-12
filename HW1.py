""" 
Write a program that computes the square root of 1234556789012345678910
and find how many steps it takes so as to achieve a precision of 20 dec-
imal digits.

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