import math

exit = False
print("Iniciando exemplo para elevar um número ao cubo...")
while not exit:
    value = input("Digite um número ou outro caracter para sair:")
    try:
        value = int(value)
        print(math.pow(value, 3))
    except ValueError:
        print(ValueError)
        exit = True
