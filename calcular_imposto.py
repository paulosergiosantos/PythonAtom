def somar_imposto(taxa, custo):
    custo_total = custo * (1.0 + taxa / 100.0)
    return custo_total

if __name__ == '__main__':
    custo = float(input("Custo: "))
    taxa = float(input("Taxa imposto: "))
    print("Custo total: %s" % (somar_imposto(taxa, custo)))
