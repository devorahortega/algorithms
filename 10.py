from decimal import * 
a = 100000000000000000000000000000000000000000000000000000000000000000000000000000000
k = 1
x = 2  
z = Decimal(1/2)*Decimal(x+a/x)

while abs(Decimal(z-x))>Decimal(10**(-20)):

  x = z
  z = Decimal(x/z+1/x)
  k = k+1

print(x)
print(k)