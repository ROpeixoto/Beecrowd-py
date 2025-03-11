a = int(input())
b = int(input())
c = 0
cont = 0
if a > b:
  c = a
  a = b
  b = c
a +=1
while a < b:
  if a % 2 == 1:
    cont += a
  a+=1
  

print(cont)
