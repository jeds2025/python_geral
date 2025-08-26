# Programa para calcular a sequencia fibonaci com entrada de valor digitado por usuario
def fibonacci(n):
    if n <= 0:
        return "Entrada invalida"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
            return b

n = int(input("Digite o valor de n: "))
print(fibonacci(n))
          
        

                    


