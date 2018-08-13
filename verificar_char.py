VOGAIS = ('a', 'e', 'i', 'o', 'u')

char = input (': ')[0]
vogal = char.lower() in VOGAIS
print("%s é %s" % (char, "Vogal" if vogal else "Consoante"))
