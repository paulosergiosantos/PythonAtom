import sys
import os
import datetime
DATE_FORMAT = "%d/%m/%Y"

def calcular_idade(birthday, today):
    age = today - birthday
    return int(age.days/365)

exit = False
print("Iniciando exemplo para calcular idade a partir de uma data de nascimento...")
while not exit:
    birthdayStr = input("Digite a data de nascimento(dd/MM/yyyy) ou q para sair:")
    try:
        birthday = datetime.datetime.strptime(birthdayStr, DATE_FORMAT).date()
        today = datetime.date.today()
        age = calcular_idade(birthday, today)
        print("Nasci em %s e hoje %s tenho %s anos." % (birthday.strftime(DATE_FORMAT), today.strftime(DATE_FORMAT), age))
    except ValueError:
        print(ValueError)
        exit = True

sys.exit(0)
