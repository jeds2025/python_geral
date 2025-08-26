''' Gravação de números pares e ímpares em arquivos diferentes'
with open("impares.txt", "w") as impares:
    with open("pares.txt", "w") as pares:
        for numero in range(0, 1000):
            if numero % 2 == 0:
                pares.write(f"{numero}\n")
            else:
                impares.write(f"{numero}\n")
'''
# Lê e exibe os conteúdos
import os

# Define a pasta de destino
pasta_destino = "C:/Python_Github/Dados"
os.makedirs(pasta_destino, exist_ok=True)

# Define os caminhos dos arquivos
arquivo_pares = os.path.join(pasta_destino, "pares.txt")
arquivo_impares = os.path.join(pasta_destino, "impares.txt")

# Grava os números
with open(arquivo_impares, "w") as impares, open(arquivo_pares, "w") as pares:
    for numero in range(0, 1000):
        if numero % 2 == 0:
            pares.write(f"{numero}\n")
        else:
            impares.write(f"{numero}\n")

# Lê e exibe os conteúdos
print("📄 Números pares:")
with open(arquivo_pares, "r") as pares:
    print(pares.read())

print("📄 Números ímpares:")
with open(arquivo_impares, "r") as impares:
    print(impares.read())
