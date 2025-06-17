def contar_vogais_consoantes(texto):
    vogais = "aeiouAEIOU"
    total_vogais = 0
    total_consoantes = 0

    for caractere in texto:
        if caractere.isalpha():  # Verifica se é uma letra
            if caractere in vogais:
                total_vogais += 1
            else:
                total_consoantes += 1

    return total_vogais, total_consoantes

resultado1 = contar_vogais_consoantes("Ola Programador!")
print(f"Vogais: {resultado1[0]}, Consoantes: {resultado1[1]}")

resultado2 = contar_vogais_consoantes("Python 3.12 eh Legal :)")
print(f"Vogais: {resultado2[0]}, Consoantes: {resultado2[1]}")