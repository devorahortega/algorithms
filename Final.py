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
for item in permutations[l-1]:
  print(item)

import random
import string

letters = string.ascii_lowercase 
n = 100
strings = []

for i in range(n):
  strings.append(''.join(random.choice(letters)for i in range(10)))

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
