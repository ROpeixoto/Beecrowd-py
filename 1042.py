ab = [3]
abc = [3]
abc = list(map(int, input().split()))
ab = abc.copy()
c = 0
for j in range(3):
  for i in range(2):
    if ab[i] > ab[i+1]:
      c = ab[i]
      ab[i] = ab[i+1]
      ab[i+1] = c

print(f"{ab[0]}\n{ab[1]}\n{ab[2]}\n")

print(f"{abc[0]}\n{abc[1]}\n{abc[2]}")