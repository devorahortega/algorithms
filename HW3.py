""" 
Write a program that computes all the square roots of all six digit
numbers that are made up of the digits 1,2,3,4,5,6 (in any order).

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

   