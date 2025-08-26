import random

def gerar_numero_secreto(minimo: int, maximo: int) -> int:
    return random.randint(minimo, maximo)

def validar_entrada(entrada_usuario: str) -> bool:
    return entrada_usuario.strip().isdigit()

def analisar_palpite(palpite: int, numero_secreto: int) -> str:
    if palpite < numero_secreto:
        return "muito baixo"
    elif palpite > numero_secreto:
        return "muito alto"
    else:
        return "correto"

def atualizar_tentativas(tentativas_restantes: int) -> int:
    return tentativas_restantes - 1

def jogar():
    MIN_NUMERO = 1
    MAX_NUMERO = 100
    TOTAL_TENTATIVAS = 7

    print(f"--- Adivinhe o Número ({MIN_NUMERO}-{MAX_NUMERO}) ---")
    
    numero_secreto = gerar_numero_secreto(MIN_NUMERO, MAX_NUMERO)
    tentativas = TOTAL_TENTATIVAS
    acertou = False

    while tentativas > 0:
        print(f"Você tem {tentativas} tentativas.")
        palpite_str = input("Qual o seu palpite? ")
        
        if not validar_entrada(palpite_str):
            print("Entrada inválida. Por favor, digite um número.")
            print()
            continue
            
        palpite_int = int(palpite_str)
        resultado = analisar_palpite(palpite_int, numero_secreto)
        
        if resultado == 'correto':
            print(f"Parabéns! Você acertou o número {numero_secreto}!")
            acertou = True
            break
        else:
            dica = "Muito baixo!" if resultado == 'muito baixo' else "Muito alto!"
            print(dica)

        tentativas = atualizar_tentativas(tentativas)
        print()

    if not acertou:
        print("\nFim de jogo! Você não conseguiu adivinhar.")
        print(f"O número secreto era: {numero_secreto}")

if __name__ == '__main__':
    jogar()
