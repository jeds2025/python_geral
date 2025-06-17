# Programa para calcular o IMC
contador = 0
while True:
    altura = float(input("Informe a altura em metros: "))
    peso = float(input("Informe o peso em Kg: "))

    IMC = peso / (altura**2)
    print()
    print(f"Altura informada: {altura}")
    print(f"Peso informado: {peso}")
    print(f"O IMC calculado foi: {IMC:.2f} kg/m²")

    print()
    print("-" * 38)
    print("            FAIXAS DE IMC")
    print("-" * 38)
    print("Peso baixo |           até 18,49 kg/m²")
    print("Peso normal| entre 18,50 e 24,99 kg/m²")
    print("Sobrepeso  | entre 25,00 e 29,99 kg/m²")
    print("Obesidade  |      acima de 30,00 kg/m²")
    print("-" * 38)

    if IMC <= 18.49:
        print("Você está com Peso baixo")
    elif IMC >= 18.50 and IMC <= 24.99:
        print("Você está com Peso normal")    
    elif IMC >= 25.00 and IMC <= 29.99:
        print("Você está com Sobrepeso") 
    else:
        print("Você está com Obesidade")
    print()

    if IMC > 24.99:
        contador = contador + 1
    
    resposta = input("Deseja calcular outro IMC? (s/n): ")
    if resposta.lower() != "s":
        print()
        print(f"O número de pessoas com Sobrepeso ou Obesidade é: {contador}")
        print()
        break
   