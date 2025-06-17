soma = 0

for numero in range(1, 50+1):
    if numero % 2 == 0: # Verifica se o número é par
        soma += numero  # Adiciona o número par à soma

print(f"A soma dos números pares entre 1 e 50 é: {soma}")
