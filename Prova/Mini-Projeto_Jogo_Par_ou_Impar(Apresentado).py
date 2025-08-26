"""
=============================================================
Mini-Projeto: Jogo Par ou Ímpar
Autor.....: Prof. Carlos Augusto de S. Almeida
Data......: 03/08/2025
Contato...: carlos.almeida@academico.ifs.edu.br
Licença...: GNU General Public License (GPL)
Requisitos: Python 3.x

Descrição: Jogo de Par ou Ímpar em Python, onde o usuário joga contra o computador.
    O sistema valida entradas, calcula resultados, mantém o placar e exibe o resumo
    de cada rodada até o jogador decidir encerrar.
Versão...: 1.0
=============================================================

import random
import sys

# ==============================================================================================
# DEFINIÇÃO DAS FUNÇÕES AUXILIARES
# ==============================================================================================
"""
def verificar_paridade(numero: int) -> str:
    """Verifica se um número inteiro é par ou ímpar."""
    return 'par' if numero % 2 == 0 else 'impar'

def obter_numero_computador(maximo: int) -> int:
    """Gera um número inteiro aleatório para a jogada do computador."""
    return random.randint(0, maximo)

def determinar_vencedor_rodada(soma: int, escolha_jogador: str) -> str:
    """Determina o vencedor da rodada com base na soma e na escolha do jogador."""
    resultado_real = verificar_paridade(soma)
    return 'jogador' if resultado_real == escolha_jogador else 'computador'

def atualizar_placar(placar: dict[str, int], vencedor: str) -> dict[str, int]:
    """Incrementa a pontuação do vencedor no dicionário do placar."""
    placar[vencedor] += 1
    return placar

def exibir_resultado_rodada(
    num_jogador: int, num_computador: int, escolha_jogador: str, vencedor: str
) -> None:
    """Imprime um resumo detalhado do resultado de uma única rodada."""
    soma = num_jogador + num_computador
    paridade_soma = verificar_paridade(soma)
    print()
    print(f"Você jogou {num_jogador} e escolheu {escolha_jogador.upper()}.")
    print(f"O computador jogou {num_computador}.")
    print(f"A soma é {soma} ({paridade_soma.upper()}).")
    if vencedor == 'jogador':
        print(">> Você venceu! <<")
    else:
        print(">> Você perdeu! <<")

# ==============================================================================================
# FUNÇÃO PRINCIPAL DO JOGO
# ==============================================================================================

def jogar():
    """
    Executa o jogo de Par ou Ímpar contra o computador.

    Esta função gerencia o ciclo de vida completo do jogo, desde a inicialização do placar
    até o loop de rodadas e a finalização, interagindo com o usuário para obter suas
    jogadas e a decisão de continuar jogando.

    Como funciona:
    O jogo opera dentro de um loop infinito (`while True`) que representa as rodadas. A cada
    rodada, o sistema solicita e valida a escolha de paridade e o número do jogador. Em
    seguida, o computador faz sua jogada. Os resultados são calculados, o vencedor é
    determinado e o placar é atualizado e exibido. Ao final da rodada, o jogador é
    questionado se deseja continuar. A resposta 'n' ou 'não' encerra o loop e o jogo.

    Pseudocódigo:
    1.  Definir constantes do jogo, como o número máximo para a escolha.
    2.  Inicializar o placar para o jogador e o computador com 0 vitórias.
    3.  Iniciar um loop infinito (`while True`) para as rodadas do jogo.
    4.  Imprimir o cabeçalho da rodada.
    5.  Em um loop de validação, solicitar ao jogador 'par' ou 'impar' até que uma
        entrada válida seja fornecida.
    6.  Em um loop de validação, solicitar um número (entre 0 e o máximo) até que uma
        entrada numérica válida no intervalo seja fornecida.
    7.  Obter o número aleatório do computador usando `obter_numero_computador`.
    8.  Calcular a soma dos dois números.
    9.  Determinar o vencedor da rodada com `determinar_vencedor_rodada`.
    10. Atualizar o placar com `atualizar_placar`.
    11. Exibir o resumo completo da rodada com `exibir_resultado_rodada`.
    12. Mostrar o placar atualizado.
    13. Em um loop de validação, perguntar se o jogador quer jogar novamente, aceitando 's'/'n'.
    14. Se a resposta for não, imprimir mensagem de despedida e sair do loop com `break`.

    """
    # (passo 1) Constantes do jogo.
    NUMERO_MAXIMO = 5

    # (passo 2) Inicializa o placar.
    placar = {"jogador": 0, "computador": 0}

    # (passo 3) Loop principal do jogo.
    while True:
        # (passo 4) Cabeçalho da rodada.
        print("\n--- Jogo Par ou Ímpar ---")

        # (passo 5) Loop para obter e validar a escolha de paridade.
        escolha_paridade = ""
        while escolha_paridade not in ["par", "impar"]:
            prompt = "Você escolhe PAR ou IMPAR? "
            escolha_paridade = input(prompt).lower().strip()
            if escolha_paridade == "ímpar":  # Acomoda acentuação
                escolha_paridade = "impar"

        # (passo 6) Loop para obter e validar o número do jogador.
        num_jogador = -1
        while num_jogador == -1:
            prompt = f"Digite um número (0-{NUMERO_MAXIMO}): "
            num_jogador_str = input(prompt).strip()
            if num_jogador_str.isdigit() and 0 <= int(num_jogador_str) <= NUMERO_MAXIMO:
                num_jogador = int(num_jogador_str)
            else:
                print(f"Entrada inválida. Digite um número entre 0 e {NUMERO_MAXIMO}.")


        # (passo 7) Computador faz sua jogada.
        num_computador = obter_numero_computador(NUMERO_MAXIMO)
        
        # (passo 8) Soma dos números.
        soma_total = num_jogador + num_computador
        
        # (passo 9) Determina o vencedor.
        vencedor = determinar_vencedor_rodada(soma_total, escolha_paridade)
        
        # (passo 10) Atualiza o placar.
        placar = atualizar_placar(placar, vencedor)
        
        # (passo 11) Exibe o resultado detalhado da rodada.
        exibir_resultado_rodada(num_jogador, num_computador, escolha_paridade, vencedor)
        
        # (passo 12) Mostra o placar geral.
        print(f"PLACAR: Jogador {placar['jogador']} X {placar['computador']} Computador")
        
        # (passo 13) Pergunta se o jogador quer continuar.
        continuar = ""
        while continuar not in ['s', 'n']:
            continuar = input("\nJogar novamente? (s/n): ").lower().strip()
            
        # (passo 14) Encerra o jogo se a resposta for não.
        if continuar == 'n':
            print("Obrigado por jogar!")
            break

# Inicia o jogo
if __name__ == '__main__':
    try:
        jogar()
    except (KeyboardInterrupt, EOFError):
        # Trata a interrupção pelo usuário (Ctrl+C) de forma graciosa.
        print("\n\nJogo interrompido. Obrigado por jogar!")
        sys.exit(0)
