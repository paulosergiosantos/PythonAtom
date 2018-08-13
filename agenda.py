import os

def write_data(file, data):
    file.write(data)
    file.write(os.linesep)

def write_file(arquivo, agenda):
    exist = os.path.exists(arquivo)
    file = open(arquivo, "a+")
    if not exist:
        write_data(file, "Agenda")
    for nome, pessoa in agenda.items():
        write_data(file, str(pessoa))
    file.close()

def read():
    pessoa = {}
    pessoa["nome"]= input("Nome: ")
    pessoa["endereco"] = input("Endereco: ")
    pessoa["telefone"] = input("Telefone: ")

    return pessoa

if __name__ == '__main__':
    exit = False
    agenda = {};
    while not exit:
        value = input("Enter para para incluir mais um item na agenda ou q para sair:")
        exit = value == "q"
        if (not exit):
            pessoa = read()
            agenda[pessoa["nome"]] = pessoa;

    print(agenda)
    write_file("agenda.dat", agenda)
