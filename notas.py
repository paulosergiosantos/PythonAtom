MIN = 0
MAX = 100
MEDIA = 70

notas = [];
quantidade = int(input("Quantidade de notas: "))
for nota in range(1, quantidade + 1):
    valorNota = int(input("Informe a nota %s:" % nota))
    if (valorNota < MIN or valorNota > MAX):
        print("Nota %s será desconsiderada." % valorNota)
    else:
        notas.append(valorNota)

print("Notas consideradas: %s" % notas)
for valorNota in notas:
    if (valorNota < MEDIA):
        print("Turma de baixa performance")
        break
else:
    print("Turma de alta perforemance")
