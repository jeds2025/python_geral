def calcular_area_retangulo(base, altura):
    return base * altura

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

# Chama a função com os valores informados
area = calcular_area_retangulo(base, altura)

print(f"A área do retângulo com base {base} e altura {altura} é: {area}") 
