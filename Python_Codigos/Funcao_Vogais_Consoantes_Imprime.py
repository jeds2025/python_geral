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

    # Imprime os resultados em vez de retornar
    print(f"Vogais: {total_vogais}, Consoantes: {total_consoantes}")

# Exemplo de uso
contar_vogais_consoantes("Ola Programador!")
contar_vogais_consoantes("Python 3.12 eh Legal :)")
