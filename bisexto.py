import math

def anoBisexto(ano):
    divBy400 = ano % 400 == 0
    divBy4 = ano % 4 == 0
    divBy100 = ano % 100 == 0
    bisexto = (divBy400) or (divBy4 and not divBy100)
    print("%s: %s, %s, %s" % (ano, divBy4, divBy100, divBy400))
    return bisexto

exit = False
while not exit:
    value = input("Digite o ano ou outro caracter caracter para sair:")
    try:
        value = int(value)
        bisexto = anoBisexto(value)
        print("Bisexto: %s" % (bisexto))
    except ValueError:
        print(ValueError)
        exit = True
