from decimal import * 
a = 100000
x = 2  
z = Decimal(1/2)*Decimal(x+a/x)

for i in range(10):
  x = z
  z = Decimal(1/2)*Decimal(x+a/x)

print(x)
print(z)