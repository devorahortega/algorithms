array = [[],[]]

for i in range(999, 1010):
  array[0].append(str(i + 1))


for item in array[0]:
  for k in range(len(item) + 1):
    array[1].append(item[0:k] + 'a' + item[k:len(item)])

print(array)