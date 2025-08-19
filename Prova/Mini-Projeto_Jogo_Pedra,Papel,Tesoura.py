"""
=============================================================
Mini-Projeto: Jogo Pedra, Papel e Tesoura
Autor.....: Prof. Carlos Augusto de S. Almeida
Data......: 29/07/2025
Contato...: carlos.almeida@academico.ifs.edu.br
Licença...: GNU General Public License (GPL)
Requisitos: Python 3.12+

Descrição: Jogo simples de Pedra, Papel e Tesoura em Python. O usuário joga contra o
    computador, podendo escolher entre pedra, papel ou tesoura. O sistema determina 
    o vencedor de cada rodada, atualiza o placar e exibe o resultado de forma clara.
Versão...: 1.0
=============================================================
"""

import random

#---------------------------------------------------------------------------------------------------

# Quest-1 de 6: As Regras do Jogo
def obter_regras() -> dict[str, str]:
    """
    Retorna um dicionário que representa as regras do jogo Pedra, Papel e Tesoura.

    Args:
        Nenhum argumento é necessário.

    Returns:
        dict[str, str]: Dicionário onde cada chave é uma jogada e o valor é a jogada que ela vence.

    Como funciona:
    - O dicionário é criado associando cada jogada à jogada que ela vence.
    - Por exemplo, 'pedra' vence 'tesoura', 'tesoura' vence 'papel', e 'papel' vence 'pedra'.

    Pseudocódigo:
    1. Cria um dicionário com as regras do jogo.
    2. Retorna o dicionário.

    Examples:
    >>> obter_regras()
    {'pedra': 'tesoura', 'tesoura': 'papel', 'papel': 'pedra'}

    """
    # (passo 1) Cria o dicionário de regras
    result = {
        'pedra'   : 'tesoura',
        'tesoura' : 'papel',
        'papel'   : 'pedra'
    }
    # (passo 2) Retorna o dicionário
    return result

#---------------------------------------------------------------------------------------------------

# Quest-2 de 6: A Escolha do Computador
def obter_jogada_computador() -> str:
    """
    Gera e retorna uma jogada aleatória válida para o computador.

    Returns:
        str: Uma das strings 'pedra', 'papel' ou 'tesoura'.

    Como funciona:
    - A função define uma lista de jogadas válidas e utiliza a função random.choice
        para selecionar uma delas aleatoriamente.

    Pseudocódigo:
    1. Define a lista de jogadas válidas.
    2. Seleciona aleatoriamente uma jogada da lista.
    3. Retorna a jogada escolhida.

    Examples:
    >>> obter_jogada_computador()  # Saída pode variar
    'pedra'

    """
    # (passo 1) Define as jogadas válidas
    jogadas_validas = ['pedra', 'papel', 'tesoura']
    # (passo 2) Seleciona aleatoriamente
    jogada = random.choice(jogadas_validas)
    # (passo 3) Retorna a jogada
    return jogada

#---------------------------------------------------------------------------------------------------

# Quest-3 de 6: Determinar Vencedor da Rodada
def determinar_vencedor(jogada_jogador: str, jogada_computador: str, regras: dict[str, str]) -> str:
    """
    Determina o vencedor da rodada com base nas jogadas do jogador e do computador.

    Args:
        jogada_jogador (str): Jogada escolhida pelo usuário ('pedra', 'papel' ou 'tesoura').
        jogada_computador (str): Jogada escolhida pelo computador.
        regras (dict[str, str]): Dicionário de regras do jogo.

    Returns:
        str: 'jogador' se o usuário vencer, 'computador' se o computador vencer, ou 'empate'.

    Como funciona:
    - Compara as jogadas. Se forem iguais, é empate.
    - Se a jogada do jogador vence a do computador segundo as regras, retorna 'jogador'.
    - Caso contrário, retorna 'computador'.

    Pseudocódigo:
    1. Se as jogadas forem iguais, retorna 'empate'.
    2. Se a jogada do jogador vence a do computador, retorna 'jogador'.
    3. Caso contrário, retorna 'computador'.

    Examples:
    >>> determinar_vencedor('pedra', 'tesoura', obter_regras())
    'jogador'
    >>> determinar_vencedor('papel', 'tesoura', obter_regras())
    'computador'
    >>> determinar_vencedor('papel', 'papel', obter_regras())
    'empate'

    Note:
    - Não há validação dos argumentos. Argumentos inválidos podem causar exceções.
    """
    # (passo 1) Verifica empate
    if jogada_jogador == jogada_computador:
        return 'empate'
    # (passo 2) Verifica se o jogador vence
    if regras[jogada_jogador] == jogada_computador:
        return 'jogador'
    # (passo 3) Caso contrário, computador vence
    return 'computador'

#---------------------------------------------------------------------------------------------------

# Quest-4 de 6: Atualizar o Placar
def atualizar_placar(placar: dict[str, int], vencedor_rodada: str) -> dict[str, int]:
    """
    Atualiza o placar do jogo conforme o vencedor_rodada.

    Args:
        placar (dict[str, int]): Dicionário com as chaves 'jogador', 'computador', 'empates'.
        vencedor_rodada (str): Vencedor da rodada ('jogador', 'computador' ou 'empate').

    Returns:
        dict[str, int]: O placar atualizado.

    Como funciona:
    - Incrementa o valor correspondente no placar de acordo com o vencedor_rodada.

    Pseudocódigo:
    1. Se vencedor_rodada for 'jogador', incrementa placar['jogador'].
    2. Se vencedor_rodada for 'computador', incrementa placar['computador'].
    3. Se vencedor_rodada for 'empate', incrementa placar['empates'].
    4. Retorna o placar atualizado.

    Examples:
    >>> atualizar_placar({'jogador': 0, 'computador': 0, 'empates': 0}, 'jogador')
    {'jogador': 1, 'computador': 0, 'empates': 0}

    >>> atualizar_placar({'jogador': 1, 'computador': 2, 'empates': 1}, 'empate')
    {'jogador': 1, 'computador': 2, 'empates': 2}
    """
    # (passo 1) Incrementa placar do jogador
    if vencedor_rodada == 'jogador':
        placar['jogador'] += 1
    # (passo 2) Incrementa placar do computador
    elif vencedor_rodada == 'computador':
        placar['computador'] += 1
    # (passo 3) Incrementa empates
    elif vencedor_rodada == 'empate':
        placar['empates'] += 1
    # (passo 4) Retorna placar atualizado
    return placar

#---------------------------------------------------------------------------------------------------

# Quest-5 de 6: Exibir Resultado da Rodada
def exibir_resultado_rodada(jogada_jogador: str, jogada_computador: str, vencedor_rodada: str) -> None:
    """
    Exibe o resultado da rodada de forma formatada para o usuário.

    Args:
        jogada_jogador (str): Jogada escolhida pelo usuário.
        jogada_computador (str): Jogada escolhida pelo computador.
        vencedor_rodada (str): Vencedor da rodada ('jogador', 'computador' ou 'empate').

    Como funciona:
    - Imprime as escolhas do jogador e do computador.
    - Exibe uma mensagem indicando quem venceu ou se houve empate.

    Pseudocódigo:
    1. Imprime as escolhas do jogador e do computador.
    2. Se vencedor_rodada for 'jogador', imprime mensagem de vitória.
    3. Se vencedor_rodada for 'empate', imprime mensagem de empate.
    4. Caso contrário, imprime mensagem de derrota.

    Examples:
    >>> exibir_resultado_rodada('pedra', 'tesoura', 'jogador')
    Você escolheu: PEDRA | Computador escolheu: TESOURA
    >> Você venceu! <<

    >>> exibir_resultado_rodada('papel', 'papel', 'empate')
    Você escolheu: PAPEL | Computador escolheu: PAPEL
    >> Empate! <<
    """
    # (passo 1) Imprime escolhas
    print(f"Você escolheu: {jogada_jogador.upper()} | Computador escolheu: {jogada_computador.upper()}")
    # (passo 2) Mensagem de vitória
    if vencedor_rodada == 'jogador':
        print(">> Você venceu! <<")
    # (passo 3) Mensagem de empate
    elif vencedor_rodada == 'empate':
        print(">> Empate! <<")
    # (passo 4) Mensagem de derrota
    else:  # resultado == 'computador'
        print(">> Você perdeu! <<")

#---------------------------------------------------------------------------------------------------

def ler_jogada() -> str:
    """
    Solicita ao usuário que digite sua jogada e retorna a entrada em minúsculas.

    Returns:
        str: Jogada digitada pelo usuário, convertida para minúsculas.

    Examples:
    >>> # Supondo que o usuário digite 'Pedra'
    'pedra'
    """
    return input("Escolha sua arma: Pedra, Papel ou Tesoura? ").lower()


def print_placar(placar_dct: dict[str, int]) -> None:
    """
    Exibe o placar atual do jogo.

    Args:
        placar_dct (dict[str, int]): Dicionário com os pontos do jogador, computador e empates.

    Examples:
    >>> print_placar({'jogador': 2, 'computador': 1, 'empates': 0})
    Placar: Jogador 2 | Computador 1 | Empates 0
    """
    print(f"Placar: Jogador {placar_dct['jogador']} | Computador {placar_dct['computador']} | Empates {placar_dct['empates']}")


def ler_jogar_novamente() -> bool:
    """
    Pergunta ao usuário se deseja jogar novamente e retorna True para 's', False caso contrário.

    Returns:
        bool: True se o usuário digitar 's', False para qualquer outra resposta.

    Examples:
    >>> # Supondo que o usuário digite 's'
    True
    >>> # Supondo que o usuário digite 'n'
    False
    """
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'

#---------------------------------------------------------------------------------------------------

# Quest-6 de 6: Função Principal
def jogar() -> None:
    """
    Executa o loop principal do jogo Pedra, Papel e Tesoura, integrando todas as funções.

    Como funciona:
    - Inicializa as regras e o placar.
    - Executa um loop onde o usuário joga contra o computador até decidir parar.
    - Em cada rodada, lê a jogada do usuário, gera a jogada do computador, determina o vencedor,
      atualiza e exibe o placar, e pergunta se deseja jogar novamente.

    Pseudocódigo:
    1. Inicializa regras e placar.
    2. Enquanto o usuário quiser jogar:
        2.1 Exibe cabeçalho do jogo.
        2.2 Lê jogada do usuário.
        2.3 Gera jogada do computador.
        2.4 Determina vencedor.
        2.5 Exibe resultado e atualiza placar.
        2.6 Pergunta se deseja jogar novamente.
    3. Exibe mensagem de agradecimento.

    Examples:
    >>> jogar()
    # Executa o jogo interativo no terminal.
    """
    # (passo 1) Inicializa regras e placar
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}

    # (passo 2) Loop principal do jogo
    while True:
        # (passo 2.1) Exibe cabeçalho
        print("\n--- Jogo Pedra, Papel, Tesoura ---")

        # (passo 2.2) Lê jogada do usuário
        jogada_jogador = ler_jogada()

        # (passo 2.3) Gera jogada do computador
        jogada_computador = obter_jogada_computador()

        # (passo 2.4) Determina vencedor
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)

        # (passo 2.5) Exibe resultado e atualiza placar
        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)

        # (passo 2.6) Pergunta se deseja jogar novamente
        continuar = ler_jogar_novamente()
        if not continuar:
            break
    # (passo 3) Mensagem de agradecimento
    print("Obrigado por jogar!")

#---------------------------------------------------------------------------------------------------

# Inicia o jogo
if __name__ == '__main__':
    jogar()
