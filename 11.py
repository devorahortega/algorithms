import random
n = 100
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
        numbers[j+1] = a
        j=j-1
      else:
         done=True

print(numbers)