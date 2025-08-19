# verificar se o numero é primo usando execção
def eh_primo(n):
    if n <= 1:
        raise ValueError("n deve ser maior que 1")
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            raise ValueError("n não é primo")
        return True
    # testar a função
    try:
        print(eh_primo(11))  # deve imprimir True
        print(eh_primo(15))  # deve imprimir ValueError
    except ValueError as e:
        print(e)  # imprime a mensagem de erro
        