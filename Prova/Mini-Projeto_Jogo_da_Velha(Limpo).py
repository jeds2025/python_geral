from typing import Optional

def exibir_tabuleiro(tabuleiro: list[str]) -> None:
    print("-------------")
    print(f"| {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} |")
    print("-------------")
    print(f"| {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} |")
    print("-------------")
    print(f"| {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} |")
    print("-------------")

def realizar_jogada(tabuleiro: list[str], posicao: int, jogador: str) -> bool:
    indice = posicao - 1
    if 0 <= indice < 9 and tabuleiro[indice] == ' ':
        tabuleiro[indice] = jogador
        return True
    return False

def verificar_vencedor(tabuleiro: list[str]) -> Optional[str]:
    combinacoes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), 
        (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
    ]
    for combo in combinacoes:
        if tabuleiro[combo[0]] == tabuleiro[combo[1]] == tabuleiro[combo[2]] and tabuleiro[combo[0]] != ' ':
            return tabuleiro[combo[0]]
    return None

def verificar_empate(tabuleiro: list[str]) -> bool:
    return ' ' not in tabuleiro

def trocar_jogador(jogador_atual: str) -> str:
    return 'O' if jogador_atual == 'X' else 'X'

def jogar():
    tabuleiro = [' '] * 9
    jogador_atual = 'X'

    print("--- Bem-vindo ao Jogo da Velha ---")
    exibir_tabuleiro([str(i) for i in range(1, 10)])
    print("O Jogador 'X' começa.\n")

    while True:
        print(f"--- Vez do Jogador: {jogador_atual} ---")
        
        while True:
            entrada = input(f"Escolha sua posição (1-9): ")
            if not entrada.isdigit() or not 1 <= int(entrada) <= 9:
                print("Entrada inválida. Por favor, digite um número de 1 a 9.")
                continue
            
            posicao = int(entrada)
            if realizar_jogada(tabuleiro, posicao, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                break
            else:
                print("Posição já ocupada. Tente outra.")

        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            print(f"\n>> Jogador {vencedor} venceu! <<")
            break

        if verificar_empate(tabuleiro):
            print("\n>> O jogo terminou em empate! <<")
            break
            
        jogador_atual = trocar_jogador(jogador_atual)
        print()

if __name__ == '__main__':
    jogar()
