import os

for v in range(1, 10):
    print(v, "Par" if v % 2 == 0 else "Impar")
else:
    print("Ultimo valor", v)

SEMANA = ('DOM','SEG','TER','QUA','QUI','SEX','SAB');

for s in SEMANA:
    print (s, end=" ")
else:
    print()

for d in range(1,31):
    print("%4s" % d, end = " " if d % 7 != 0 else os.linesep)
