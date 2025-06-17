def eh_primo(numero):
    if numero <= 1:
        return False  # 1 e números negativos não são primos
    
    # Verifica se o número é divisível por qualquer número de 2 até o número - 1
    for i in range(2, numero):
        if numero % i == 0:
            return False  # O número é divisível por i, portanto não é primo
    
    return True  # O número é primo

numero_usuario = int(input("Digite um número inteiro positivo: "))

if eh_primo(numero_usuario):
    print(f"{numero_usuario} é primo.")
else:
    print(f"{numero_usuario} não é primo.")
