import random
from typing import Tuple

def obter_palavra_secreta() -> str:
    palavras = ["python", "programacao", "desenvolvimento", "algoritmo", "computador", "interface"]
    return random.choice(palavras).lower()

def exibir_palavra_mascarada(palavra_secreta: str, letras_corretas: set[str]) -> str:
    return " ".join([letra if letra in letras_corretas else "_" for letra in palavra_secreta])

def validar_letra(letra: str, letras_corretas: set[str], letras_erradas: set[str]) -> Tuple[bool, str]:
    letra = letra.lower()
    if len(letra) != 1 or not letra.isalpha():
        return (False, 'Entrada inválida. Por favor, digite uma única letra.')
    if letra in letras_corretas or letra in letras_erradas:
        return (False, 'Você já tentou essa letra.')
    return (True, 'Letra válida.')

def processar_jogada(letra: str, palavra_secreta: str, corretas: set[str], erradas: set[str], tentativas: int) -> int:
    if letra in palavra_secreta:
        corretas.add(letra)
        print("Correto!")
    else:
        erradas.add(letra)
        tentativas -= 1
        print("Errado!")
    return tentativas

def checar_fim_de_jogo(palavra_secreta: str, letras_corretas: set[str], tentativas: int) -> str:
    if set(palavra_secreta).issubset(letras_corretas):
        return 'vitoria'
    if tentativas == 0:
        return 'derrota'
    return 'continua'

def jogar():
    palavra_secreta = obter_palavra_secreta()
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 6

    while True:
        print("\n--- Jogo da Forca ---")
        display = exibir_palavra_mascarada(palavra_secreta, letras_corretas)
        print(f"Palavra: {display.upper()}")
        print(f"Letras erradas: {sorted(list(letras_erradas))}")
        print(f"Tentativas restantes: {tentativas}")

        letra_digitada = input("Digite uma letra: ")
        valida, mensagem = validar_letra(letra_digitada, letras_corretas, letras_erradas)
        if not valida:
            print(mensagem)
            continue
        
        letra_normalizada = letra_digitada.lower()
        tentativas = processar_jogada(letra_normalizada, palavra_secreta, letras_corretas, letras_erradas, tentativas)
        estado_jogo = checar_fim_de_jogo(palavra_secreta, letras_corretas, tentativas)

        if estado_jogo == 'vitoria':
            print(f"\nParabéns, você venceu! A palavra era: '{palavra_secreta.upper()}'.")
            break
        elif estado_jogo == 'derrota':
            print(f"\nVocê perdeu! A palavra era: '{palavra_secreta.upper()}'.")
            break

if __name__ == '__main__':
    jogar()
