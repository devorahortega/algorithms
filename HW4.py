"""
Write a program that generates 100 random strings of length 10 con-
sisting of lower case letters and then uses a bubble sort algorithm in
order to sort them alphabetically. Note that in Python the comparison
of strings is done exactly as the comparison of numbers and a sting is
less than another one if it would precede it in the dictionary. You will
need to look up the generation of random string and this may entail
using an extra library.

"""

import string
import random
N = 10

res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))

print("The generated random string : " + str(res))

"""
numbers = []
for i in range(n):
  numbers.append(random.randrange(1,100000))

print(numbers)

for i in range(n):
  done=False
  j = i-1
  while(done==False):
    if j<0:
      done=True
    else:
      if numbers[j+1]>numbers[j]:
        a = numbers[j]
        numbers[j] = numbers[j+1]
        numbers[j+1] = as
        j=j-1
      else:
         done=True

print(numbers)
"""