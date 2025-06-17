numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo  número: "))

print("-"*20)
print("ENTRADA".center(20))
print("-"*20)
print(f"Primeiro número: {numero1}")
print(f"Segundo número : {numero2}")
print("-"*20)
print("SAÍDA".center(20))
print("-"*20)

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")

if numero2 != 0:
    divisao = numero1 / numero2
    print(f"Divisão: {divisao:.2f}")
else:
    print("Divisão por zero não permitida")

print("-"*20)




