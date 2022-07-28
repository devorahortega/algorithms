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
