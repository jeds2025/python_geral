def boas_vindas():
    print("Bem vindo!!!")

def soma(a, b):
    resultado = a + b
    return resultado

boas_vindas()
print(soma(4, 2))

nome = "José Enaldo Dantas dos Santos"
contador = 0

print(nome.replace(" ", "")[::2])

for letra in nome.replace(" ", ""):
    contador += 1
    print(letra)

print(contador)
