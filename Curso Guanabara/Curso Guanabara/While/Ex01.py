n_final = int(input("Número Final: "))

n_inicial = 0 

while n_inicial <= n_final:
    n_inicial = n_inicial + 1
    if n_inicial > n_final:
        break
    print(f"número {n_inicial}")

