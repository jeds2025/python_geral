import random

def mostrar_tabuleiro(tabuleiro):
    print("\n")
    for i, linha in enumerate(tabuleiro):
        print(" | ".join(linha))
        if i < 2:
            print("--+---+--")
    print("\n")

def verificar_vitoria(tabuleiro, marcador):
    # Linhas
    for linha in tabuleiro:
        if all(pos == marcador for pos in linha):
            return True
    # Colunas
    for col in range(3):
        if all(tabuleiro[lin][col] == marcador for lin in range(3)):
            return True
    # Diagonais
    if all(tabuleiro[i][i] == marcador for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == marcador for i in range(3)):
        return True
    return False

def verificar_empate(tabuleiro):
    return all(pos != " " for linha in tabuleiro for pos in linha)

def solicitar_jogada_jogador(tabuleiro):
    while True:
        try:
            pos = input("Sua jogada (linha,coluna) de 1 a 3 (ex: 2,3): ").strip()
            linha, coluna = map(int, pos.split(','))
            if linha < 1 or linha > 3 or coluna < 1 or coluna > 3:
                print("Posição inválida. Use valores entre 1 e 3.")
                continue
            if tabuleiro[linha - 1][coluna - 1] != " ":
                print("Posição já ocupada! Tente outra.")
                continue
            return linha - 1, coluna - 1
        except:
            print("Entrada inválida! Use o formato linha,coluna (ex: 1,3)")

def jogada_computador(tabuleiro):
    # Computador escolhe aleatoriamente uma posição vazia
    vazias = [(i, j) for i in range(3) for j in range(3) if tabuleiro[i][j] == " "]
    return random.choice(vazias) if vazias else None

def jogar():
    print("--- Jogo da Velha: Jogador vs Computador ---")
    tabuleiro = [[" "]*3 for _ in range(3)]
    jogador = "X"
    computador = "O"
    
    while True:
        mostrar_tabuleiro(tabuleiro)
        
        # Jogada do jogador
        linha, coluna = solicitar_jogada_jogador(tabuleiro)
        tabuleiro[linha][coluna] = jogador
        
        if verificar_vitoria(tabuleiro, jogador):
            mostrar_tabuleiro(tabuleiro)
            print("Parabéns! Você venceu!")
            break
        
        if verificar_empate(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("Empate! Ninguém venceu.")
            break
        
        # Jogada do computador
        jog_comp = jogada_computador(tabuleiro)
        if jog_comp is None:
            mostrar_tabuleiro(tabuleiro)
            print("Empate! Ninguém venceu.")
            break
        tabuleiro[jog_comp[0]][jog_comp[1]] = computador
        print(f"Computador jogou na posição: {jog_comp[0]+1},{jog_comp[1]+1}")
        
        if verificar_vitoria(tabuleiro, computador):
            mostrar_tabuleiro(tabuleiro)
            print("Computador venceu! Tente novamente.")
            break
        
        if verificar_empate(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("Empate! Ninguém venceu.")
            break

if __name__ == "__main__":
    jogar()
