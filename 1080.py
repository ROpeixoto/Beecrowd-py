a = []
for i in range(100):
  a.append(input())
m = 0
pos = 0
x=0
for x in range(len(a)):
  if int(a[x]) > m:
    pos = x + 1
    m = int(a[x])

print(m)
print(pos)