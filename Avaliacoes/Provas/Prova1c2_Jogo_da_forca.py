import random

def escolher_palavra(lista_palavras):
    """Escolhe uma palavra aleatória da lista fornecida."""
    return random.choice(lista_palavras)

def mostrar_palavra_oculta(palavra_secreta, letras_corretas):
    """Retorna a representação atual da palavra, mostrando as letras corretas e ocultando as demais."""
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra_secreta])

def jogar():
    """Função principal que orquestra o jogo da forca."""
    lista_palavras = ['abacaxi', 'python', 'programacao', 'desenvolvimento', 'jogo']
    numero_maximo_erros = 6
    palavra_secreta = escolher_palavra(lista_palavras).upper()
    letras_corretas = []
    letras_tentadas = []
    erros = 0

    print("--- Jogo da Forca ---")
    print("Adivinhe a palavra!")

    while erros < numero_maximo_erros:
        print(f"\nPalavra: {mostrar_palavra_oculta(palavra_secreta, letras_corretas)}")
        print(f"Letras tentadas: {letras_tentadas}")
        print(f"Erros restantes: {numero_maximo_erros - erros}")

        letra = input("Digite uma letra: ").upper()

        if letra in letras_tentadas:
            print(f"Você já tentou a letra '{letra}'. Tente outra.")
            continue

        letras_tentadas.append(letra)

        if letra in palavra_secreta:
            letras_corretas.append(letra)
            print(f"'{letra}' está na palavra!")
        else:
            erros += 1
            print(f"'{letra}' não está na palavra.")

        # Verifica se o jogador ganhou
        if all(letra in letras_corretas for letra in palavra_secreta):
            print(f"\n--- Fim de Jogo ---")
            print(f"Parabéns, você ganhou! A palavra era '{palavra_secreta}'.")
            return

    # Se o número máximo de erros for atingido
    print(f"\n--- Fim de Jogo ---")
    print(f"Você perdeu! A palavra era '{palavra_secreta}'.")

# Executa o jogo
if __name__ == "__main__":
    jogar()
