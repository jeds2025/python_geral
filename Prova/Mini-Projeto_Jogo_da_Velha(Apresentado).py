"""
=============================================================
Mini-Projeto: Jogo da Velha
Autor.....: Prof. Carlos Augusto de S. Almeida
Data......: 26/07/2025
Contato...: carlos.almeida@academico.ifs.edu.br
Licença...: GNU General Public License (GPL)
Requisitos: Python 3.12+

Descrição: Jogo da Velha em Python para dois jogadores. O sistema exibe o tabuleiro,
    valida jogadas, alterna turnos, verifica vitória ou empate e mostra o resultado 
    ao final da partida.
Versão...: 1.0
=============================================================
"""

from typing import Optional

# ==============================================================================================
# DEFINIÇÃO DAS FUNÇÕES AUXILIARES (desenvolvidas nas questões anteriores)
# ==============================================================================================

def exibir_tabuleiro(tabuleiro: list[str]) -> None:
    """Exibe o tabuleiro do Jogo da Velha em um formato de grade 3x3."""
    print("-------------")
    print(f"| {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} |")
    print("-------------")
    print(f"| {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} |")
    print("-------------")
    print(f"| {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} |")
    print("-------------")

def realizar_jogada(tabuleiro: list[str], posicao: int, jogador: str) -> bool:
    """Tenta registrar a jogada de um jogador em uma determinada posição."""
    indice = posicao - 1
    if 0 <= indice < 9 and tabuleiro[indice] == ' ':
        tabuleiro[indice] = jogador
        return True
    return False

def verificar_vencedor(tabuleiro: list[str]) -> Optional[str]:
    """Analisa o tabuleiro para determinar se há um vencedor."""
    combinacoes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), 
        (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
    ]
    for combo in combinacoes:
        if tabuleiro[combo[0]] == tabuleiro[combo[1]] == tabuleiro[combo[2]] and tabuleiro[combo[0]] != ' ':
            return tabuleiro[combo[0]]
    return None

def verificar_empate(tabuleiro: list[str]) -> bool:
    """Verifica se o jogo resultou em empate (tabuleiro cheio)."""
    return ' ' not in tabuleiro

def trocar_jogador(jogador_atual: str) -> str:
    """Alterna o turno entre os jogadores 'X' e 'O'."""
    return 'O' if jogador_atual == 'X' else 'X'

# ==============================================================================================
# FUNÇÃO PRINCIPAL DO JOGO
# ==============================================================================================

def jogar():
    """
    Orquestra o Jogo da Velha, gerenciando o fluxo completo da partida.

    Esta função inicializa o jogo, executa o loop principal e interage com o usuário,
    chamando as funções auxiliares para exibir o tabuleiro, validar jogadas, verificar o
    resultado e alternar jogadores até que o jogo termine.

    Como funciona:
    O jogo começa com um tabuleiro vazio e o jogador 'X'. Um loop `while` infinito mantém o
    jogo em execução. A cada turno, o tabuleiro é exibido, e o jogador atual é solicitado a
    fazer uma jogada. A entrada é validada em um loop aninhado. Após uma jogada válida, o
    sistema verifica se há um vencedor ou um empate. Se uma dessas condições for atendida, o
    jogo termina. Caso contrário, o turno é passado para o próximo jogador.

    Pseudocódigo:
    1.  Inicializar o `tabuleiro` como uma lista de 9 espaços e o `jogador_atual` como 'X'.
    2.  Exibir uma mensagem de boas-vindas e um tabuleiro guia com as posições numeradas.
    3.  Iniciar um loop `while True` que representa o fluxo do jogo.
    4.  Dentro do loop, exibir o tabuleiro atual.
    5.  Iniciar um loop aninhado `while True` para obter e validar a entrada do jogador.
        a. Solicitar ao `jogador_atual` que escolha uma posição (1-9).
        b. Validar se a entrada é um número e se está no intervalo de 1 a 9.
        c. Se a entrada for válida, tentar realizar a jogada usando `realizar_jogada`.
        d. Se a jogada for bem-sucedida, sair do loop de validação.
        e. Se a posição estiver ocupada, informar o jogador e pedir uma nova jogada.
    6.  Após uma jogada válida, chamar `verificar_vencedor`.
        a. Se houver um vencedor, exibir o tabuleiro final, anunciar o vencedor e sair do
           loop principal com `break`.
    7.  Se não houver vencedor, chamar `verificar_empate`.
        a. Se o jogo empatou, exibir o tabuleiro final, anunciar o empate e sair do loop
           principal com `break`.
    8.  Se o jogo continuar, trocar o jogador usando `trocar_jogador`.
    """
    # (passo 1) Inicializa as variáveis do jogo.
    tabuleiro = [' '] * 9
    jogador_atual = 'X'

    # (passo 2) Exibe o cabeçalho e o guia de posições.
    print("--- Bem-vindo ao Jogo da Velha ---")
    exibir_tabuleiro([str(i) for i in range(1, 10)])
    print("O Jogador 'X' começa.\n")

    # (passo 3) Loop principal do jogo.
    while True:
        # (passo 4) Exibe o estado atual do tabuleiro.
        print(f"--- Vez do Jogador: {jogador_atual} ---")
        
        # (passo 5) Loop para obter uma jogada válida.
        while True:
            # (passo 5a) Solicita a jogada.
            entrada = input(f"Escolha sua posição (1-9): ")
            
            # (passo 5b) Validação da entrada.
            if not entrada.isdigit() or not 1 <= int(entrada) <= 9:
                print("Entrada inválida. Por favor, digite um número de 1 a 9.")
                continue
            
            posicao = int(entrada)
            
            # (passo 5c, 5d, 5e) Tenta realizar a jogada.
            if realizar_jogada(tabuleiro, posicao, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                break  # Sai do loop de entrada se a jogada foi válida.
            else:
                print("Posição já ocupada. Tente outra.")

        # (passo 6) Verifica se há um vencedor.
        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            # (passo 6a) Anuncia o vencedor e termina o jogo.
            print(f"\n>> Jogador {vencedor} venceu! <<")
            break

        # (passo 7) Verifica se há empate.
        if verificar_empate(tabuleiro):
            # (passo 7a) Anuncia o empate e termina o jogo.
            print("\n>> O jogo terminou em empate! <<")
            break
            
        # (passo 8) Troca o jogador para o próximo turno.
        jogador_atual = trocar_jogador(jogador_atual)
        print() # Adiciona linha em branco para legibilidade

# Inicia o jogo quando o script é executado.
if __name__ == '__main__':
    jogar()
