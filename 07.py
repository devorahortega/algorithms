array = [[],[]]

for i in range(999, 9000):
  array[0].append(str(i + 1))
for items in array[0]:
  array[1].append('a' + items) 
print(array)
