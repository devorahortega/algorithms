from decimal import * 
a = 2
x = 2  
z = Decimal(1/2)*Decimal(x+a/x)

for i in range(100):
  x = z
  z = Decimal(1/2)*Decimal(x+a/x)

print(x)
print(z)