a = []
for x in range(10):
  a.append(int(input()))

for i in range(len(a)):
    if a[i] <= 0:
     a[i] = 1
    print(f"X[{i}] = {a[i]}")