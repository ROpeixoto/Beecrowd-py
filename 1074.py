val = int(input())
a = []
def oddeve(n) -> str:
  if n % 2 == 0:
    return "EVEN"
  else:
    return "ODD"

def negpos(b):
  if b>0:
    return "POSITIVE"
  else:
    return "NEGATIVE"

for i in range(val):
  a.append(int(input()))

for i in range(val):
  if a[i] == 0:
    print("NULL")
  else:
    print(f"{oddeve(a[i])} {negpos(a[i])}")
