array = []

for i in range(9000):
  array.append(str(i + 1))
for i in range(9000):
  array[i] = 'a' + array[i]

print(array)
