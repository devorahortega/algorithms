""" 
Write a program that computes the square roots of all numbers from
1000000 to 2000000 and records the number of steps it takes for each
computation to reach a precision of 20 decimal digits.

"""

from decimal import * 
a = range(1000000-2000000)
k = 1
x = 2  

for n in a:
  z = Decimal(1/2)*Decimal(x+a/x)
  while abs(Decimal(z-x))>Decimal(23**(-20)):

    x = z
    z = Decimal(x/z+1/x)
    k = k+1

print(x)
print(k)

   