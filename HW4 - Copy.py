"""
Write a program that generates 100 random strings of length 10 con-
sisting of lower case letters and then uses a bubble sort algorithm in
order to sort them alphabetically. Note that in Python the comparison
of strings is done exactly as the comparison of numbers and a sting is
less than another one if it would precede it in the dictionary. You will
need to look up the generation of random string and this may entail
using an extra library.

"""

import random
import string
letters = string.ascii_lowercase 
n = 100
strings = []

for i in range(n):
  strings.append(''.join(random.choice(letters)for i in range(10))

print(strings)

for i in range(n):
  done=False
  j = i-1
  while(done==False):
    if j<0:
      done=True
    else:
      if strings[j+1]>strings[j]:
        a = strings[j]
        strings[j] = strings[j+1]
        strings[j+1] = a
        j=j-1
      else:
         done=True

print(strings)