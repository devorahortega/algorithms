""" 
Write a program that computes all the square roots of all six digit
numbers that are made up of the digits 1,2,3,4,5,6 (in any order).

"""
from decimal import * 

l = 5
permutations = []
permutations.append(['1'])
for n in range(l-1):
  permutations.append([])
for n in range(l-1): 
  digit = str(n+2)
  for item in permutations[n]:
    for k in range(len(item)+1):
      permutations[n+1].append(item[0:k]+digit+item[k:len(item)])
"""
for item in permutations[l-1]:
  print(item)
"""

a = item
k = 1
x = 2  

for item in permutations[5]:
  z = Decimal(1/2)*Decimal(x+a/x)
  while abs(Decimal(z-x))>Decimal(23**(-20)):

    x = z
    z = Decimal(x/z+1/x)
    k = k+1

print(x)
print(k)

   