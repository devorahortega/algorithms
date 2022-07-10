array = [[],[]]

for i in range(1, 9):
  array[0].append(str(i + 1))


for item in array[0]:
  for k in range(len(item) + 1):
    array[1].append(item[1:k] + '2' + item[k:len(item)])
  for k in range(len(item) + 1):
    array[1].append(item[2:k] + '3' + item[k:len(item)])

print(array)