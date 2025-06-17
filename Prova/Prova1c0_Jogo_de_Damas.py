import random

def criar_tabuleiro():
    # 'b' para peça preta, 'p' para peça branca, '.' para casa vazia, ' ' para casa clara (inválida)
    tab = []
    for linha in range(8):
        row = []
        for col in range(8):
            if (linha + col) % 2 == 1:
                if linha < 3:
                    row.append('b')  # peças pretas (computador)
                elif linha > 4:
                    row.append('p')  # peças brancas (jogador)
                else:
                    row.append('.')
            else:
                row.append(' ')
        tab.append(row)
    return tab

def mostrar_tabuleiro(tab):
    print("\n    0 1 2 3 4 5 6 7")
    print("   -----------------")
    for i, row in enumerate(tab):
        print(f"{i} | {' '.join(row)}")
    print()

def posicoes_possiveis(tab, jogador):
    # Retorna lista de movimentos possíveis (origem, destino) para jogador 'p' ou 'b'
    direcao = -1 if jogador == 'p' else 1
    capturas = []
    simples = []

    for r in range(8):
        for c in range(8):
            if tab[r][c].lower() == jogador:
                # movimentos simples
                for dc in [-1, 1]:
                    nr = r + direcao
                    nc = c + dc
                    if 0 <= nr < 8 and 0 <= nc < 8 and tab[nr][nc] == '.':
                        simples.append(((r,c),(nr,nc)))
                # capturas
                for dc in [-1, 1]:
                    nr = r + direcao
                    nc = c + dc
                    nr2 = r + 2*direcao
                    nc2 = c + 2*dc
                    if 0 <= nr2 < 8 and 0 <= nc2 < 8:
                        if tab[nr][nc].lower() != jogador and tab[nr][nc] != '.' and tab[nr][nc] != ' ' and tab[nr2][nc2] == '.':
                            capturas.append(((r,c),(nr2,nc2)))
    return capturas if capturas else simples

def aplicar_movimento(tab, origem, destino):
    r0,c0 = origem
    r1,c1 = destino
    tab[r1][c1] = tab[r0][c0]
    tab[r0][c0] = '.'

    # verifica captura
    if abs(r1 - r0) == 2:
        rm = (r0 + r1)//2
        cm = (c0 + c1)//2
        tab[rm][cm] = '.'

    # promoção a dama - não implementada para simplificar

def jogo_terminado(tab):
    pecas_p = sum(row.count('p') + row.count('P') for row in tab)
    pecas_b = sum(row.count('b') + row.count('B') for row in tab)
    return pecas_p == 0 or pecas_b == 0

def jogador_move(tab):
    movimentos = posicoes_possiveis(tab, 'p')
    if not movimentos:
        return False
    while True:
        try:
            mostrar_tabuleiro(tab)
            print("Suas peças: p")
            origem = input("Digite posição da peça para mover (ex: 5 0): ")
            destino = input("Digite posição destino (ex: 4 1): ")
            r0,c0 = map(int, origem.strip().split())
            r1,c1 = map(int, destino.strip().split())
            if ((r0,c0),(r1,c1)) in movimentos:
                aplicar_movimento(tab, (r0,c0), (r1,c1))
                return True
            else:
                print("Movimento inválido. Tente novamente.")
        except Exception:
            print("Entrada inválida. Use formato linha coluna, ex: 5 0")

def computador_move(tab):
    movimentos = posicoes_possiveis(tab, 'b')
    if not movimentos:
        return False
    movimento = random.choice(movimentos)
    aplicar_movimento(tab, movimento[0], movimento[1])
    print(f"Computador moveu de {movimento[0]} para {movimento[1]}")
    return True

def jogar_damas():
    print("--- Jogo de Damas simplificado contra computador ---")
    tab = criar_tabuleiro()
    jogador_turno = True  # True = jogador, False = computador

    while True:
        if jogo_terminado(tab):
            mostrar_tabuleiro(tab)
            if jogador_turno:
                print("Fim de jogo! Computador venceu.")
            else:
                print("Fim de jogo! Você venceu!")
            break

        if jogador_turno:
            if not jogador_move(tab):
                mostrar_tabuleiro(tab)
                print("Você não tem movimentos válidos. Computador venceu!")
                break
        else:
            if not computador_move(tab):
                mostrar_tabuleiro(tab)
                print("Computador não tem movimentos válidos. Você venceu!")
                break
        jogador_turno = not jogador_turno

if __name__ == "__main__":
    jogar_damas()
