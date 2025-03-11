a = float(input())
i = 1
while i != a+1:
  if i % 2 == 0:
    x = i ** 2
    print(f'{i}^2 = {x}')
    i+=1
  else:
    i+=1