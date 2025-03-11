h1,m1,h2,m2 = map(int,input().split())

h1 = h1*60
h2 = h2*60
tt = (h2 + m2) - (h1+m1)
minuts = tt % 60
hours = tt / 60
hours = int(hours)
if (h1 + m1) == (h2+m2):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

elif (h1 + m1) < (h2+m2):
  print(f'O JOGO DUROU {hours} HORA(S) E {minuts} MINUTO(S)')
else:
  hours = 24 - (hours * -1)
  if minuts > 0:
    hours -= 1
#  if minuts > 0:
 #   minuts = minuts
  else:
    minuts = 0
  print(f'O JOGO DUROU {hours} HORA(S) E {minuts} MINUTO(S)')