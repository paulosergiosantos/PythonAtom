import os

DELIMITER = ";"
FILE_HEADER = ("NOME", "CPF", "ENDERECO")

def format_data(args):
    return DELIMITER.join(args)

def write_data(file, data):
    file.write(data)
    file.write(os.linesep)

def write_file(arquivo, nome, cpf, endereco):
    exist = os.path.exists(arquivo)
    file = open(arquivo, "a+")
    if not exist:
        write_data(file, format_data(FILE_HEADER))
    write_data(file, format_data((nome, cpf, endereco)))
    file.close()

def read():
    pessoa = {}
    result = {}
    result["arquivo"] = input("Arquivo: ")
    pessoa["nome"]= input("Nome: ")
    pessoa["cpf"] = input("CPF: ")
    pessoa["endereco"] = input("Endereco: ")
    result["pessoa"] = pessoa

    return result

def init():
    result = read()
    print(result)
    arquivo = result["arquivo"]
    pessoa = result["pessoa"]
    write_file(arquivo, pessoa["nome"], pessoa["cpf"], pessoa["endereco"])

if __name__ == '__main__':
    exit = False
    while not exit:
        value = input("Enter para gravar arquivo ou q para sair:")
        exit = value== "q"
        if (not exit):
            init()
