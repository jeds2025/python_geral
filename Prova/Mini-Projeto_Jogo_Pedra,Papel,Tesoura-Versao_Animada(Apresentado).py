"""
================================================================================
Mini-Projeto: Jogo Pedra, Papel e Tesoura - VERSÃO ANIMADA
Autor.....: Prof. Carlos Augusto de S. Almeida
Data......: 26/07/2025
Contato...: carlos.almeida@academico.ifs.edu.br
Licença...: GNU General Public License (GPL)
Requisitos: Python 3.10+

Descrição: Versão visualmente aprimorada do jogo Pedra, Papel e Tesoura, desenvolvida
    como uma ferramenta de aprendizado. O código é extensivamente comentado e 
    documentado, focando em clareza, boas práticas de programação e na criação de uma 
    experiência de jogo interativa e envolvente no terminal. Inclui animações, cores, 
    modos de jogo e uma IA adaptativa.

Versão: 1.1 Refatorada e Robusta
================================================================================
"""

import collections
import os
import random
import time

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#region Módulos e Constantes Globais

# Classe para gerenciar as cores do terminal de forma organizada.
# O uso de uma classe agrupa constantes relacionadas, melhorando a legibilidade do código.
class Cores:
    """Agrupa códigos de escape ANSI para colorir o texto no terminal."""
    RESET = '\033[0m'
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'

# Dicionário central para toda a Arte ASCII usada no jogo.
# Armazenar artes como dados (em um dicionário) separa a lógica da apresentação.
ARTES_ASCII: dict[str, list[str]] = {
    'punho': [
        "    __________      ",
        "---'   ______)      ",
        "      (_____)       ",
        "      (_____)       ",
        "      (____)        ",
        "---.__(___)         ",
        "      Punho         "
    ],
    'pedra': [
        "    __________      ",
        "---'   ______)      ",
        "      (_____)       ",
        "      (_____)       ",
        "      (____)        ",
        "---.__(___)         ",
        "      Pedra         " 
    ],
    'papel': [
        "    __________      ",
        "---'    ______)____ ",
        "           _______) ",
        "          _______)  ",
        "         _______)   ",
        "---.__________)     ",
        "       Papel        "
    ],
    'tesoura': [
        "    _______         ",
        "---'   ____)____    ",
        "          ______)   ",
        "       __________)  ",
        "      (____)        ",
        "---.__(___)         ",
        "       Tesoura      "
    ],
    'tesoura_quebrada': [
        "    _______         ",
        "---'   ____)____    ",
        "          x_____)   ",
        "       x_________)  ",
        "      (x___)        ",
        "---.__(x__)         ",
        "  Tesoura Quebrada  " 
    ],
    'papel_cortado': [
        "    --.--        ",
        "---'  /  )____   ",
        "     /  ______)  ",
        "    /  _______)  ",
        "   /  _______)   ",
        "---.__________)  ",
        " Papel Cortado   " 
    ],
    'pedra_coberta': [
        "   -----------    ",
        "--|           |---",
        "  |   Pedra   |   ",
        "  |  Coberta  |   ",
        "  |           |   ",
        "  --------------- ",
        "                  "
    ],
    'trofeu': [
        "      ___________    ",
        "     '._==_==_=_.'   ",
        "     .-\\:      /-.  ",
        "    | (|:.     |) |  ",
        "     '-|:.     |-'   ",
        "       \\::.    /    ",
        "        '::. .'      ",
        "          ) (        ",
        "        _.' '._      ",
        "       `-------`     ",
        "        Troféu       ",
    ]
}

# Dicionário que define os resultados visuais das interações de vitória.
# Centraliza a lógica de "quem quebra o quê" para a animação de confronto.
REGRAS_IMPACTO = {
    ('pedra', 'tesoura'): {'arte_perdedor': 'tesoura_quebrada', 'msg': "* Pedra esmaga Tesoura! *"},
    ('tesoura', 'papel'): {'arte_perdedor': 'papel_cortado', 'msg': "* Tesoura corta Papel! *"},
    ('papel', 'pedra'): {'arte_perdedor': 'pedra_coberta', 'msg': "* Papel embrulha Pedra! *"}
}
#endregion
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#region Funções Utilitárias e de Interface
def limpar_tela() -> None:
    """
    Limpa a tela do terminal para criar animações e manter a interface organizada.

    Como funciona:
    - A função utiliza o módulo `os` para executar um comando do sistema operacional.
    - O comando 'cls' é para sistemas Windows, enquanto 'clear' é para sistemas baseados em Unix
      (Linux, macOS).
    - O operador ternário `('cls' if os.name == 'nt' else 'clear')` seleciona o comando correto
      com base no sistema operacional detectado por `os.name`.

    Pseudocódigo:
    1. Executa o comando de limpeza de tela apropriado para o sistema operacional.

    Examples:
        >>> limpar_tela()
        # O conteúdo anterior do terminal é removido.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

#===============================================================================

def exibir_banner_inicial() -> None:
    """
    Exibe um banner de boas-vindas estilizado no início do programa.

    Como funciona:
    - A função primeiro limpa a tela para garantir que o banner seja a única coisa visível.
    - Em seguida, imprime uma série de strings formatadas com cores e bordas para criar um
      título visualmente atraente.

    Pseudocódigo:
    1. Limpa a tela do terminal.
    2. Imprime o banner de boas-vindas formatado.

    Examples:
        >>> exibir_banner_inicial()
        # Exibe o banner formatado no terminal.
    """
    limpar_tela()
    print(Cores.CIANO + "==========================================================")
    print("|                                                        |")
    print("|   Bem-vindo ao PEDRA, PAPEL & TESOURA: Edição Épica!   |")
    print("|                                                        |")
    print("==========================================================" + Cores.RESET)
    print()

#===============================================================================

def obter_nome_jogador() -> str:
    """
    Solicita e retorna o nome do jogador, garantindo que não seja vazio.

    Returns:
        str: O nome do jogador, capitalizado e sem espaços em branco nas extremidades.

    Como funciona:
    - A função entra em um laço infinito (`while True`) que só é quebrado quando uma entrada
      válida é fornecida.
    - A cada iteração, solicita o nome ao usuário. O método `.strip()` remove espaços em branco
      extras do início e do fim.
    - Se o nome resultante não for uma string vazia, ele é capitalizado e retornado,
      encerrando o laço. Caso contrário, uma mensagem de erro é exibida.

    Pseudocódigo:
    1. Inicia um laço de repetição para solicitar a entrada.
    2. Lê e remove espaços em branco da entrada do usuário.
    3. Se a entrada for válida (não vazia), capitaliza e retorna o nome.
    4. Se a entrada for inválida, exibe uma mensagem de erro e repete o laço.

    Examples:
        # Supondo que o usuário digite "  carlos  "
        >>> obter_nome_jogador()
        'Carlos'
    """
    while True:
        nome = input("Primeiro, qual o seu nome? ").strip()
        if nome:
            return nome.capitalize()
        print(Cores.VERMELHO + "Por favor, digite um nome válido." + Cores.RESET)

#===============================================================================

def escolher_modo_jogo() -> dict[str, str | int | float]:
    """
    Permite ao jogador escolher o modo de jogo e retorna suas regras.

    Returns:
        dict[str, str | int | float]: Um dicionário contendo o tipo de modo e o número de
        vitórias necessárias para vencer a partida. Para o modo casual, o número de vitórias
        é infinito (`float('inf')`).

    Como funciona:
    - Exibe um menu com as opções de modo de jogo.
    - Entra em um laço `while True` para aguardar uma entrada válida (1, 2 ou 3).
    - Com base na escolha, cria e retorna um dicionário que define as regras da partida.

    Pseudocódigo:
    1. Exibe o menu de opções para o usuário.
    2. Inicia um laço de repetição para validar a entrada.
    3. Lê a escolha do usuário.
    4. Se a escolha for '1', '2' ou '3', retorna o dicionário de regras correspondente.
    5. Se a escolha for inválida, exibe uma mensagem de erro e continua o laço.

    Examples:
        # Supondo que o usuário digite "2"
        >>> escolher_modo_jogo()
        {'tipo': 'melhor_de_3', 'vitorias_necessarias': 2}
    """
    print("\nOlá! Qual modo de jogo você prefere?")
    print(f"{Cores.AMARELO}[1]{Cores.RESET} Casual (Jogue até cansar)")
    print(f"{Cores.AMARELO}[2]{Cores.RESET} Melhor de 3 (Vence quem ganhar 2 rodadas)")
    print(f"{Cores.AMARELO}[3]{Cores.RESET} Melhor de 5 (Vence quem ganhar 3 rodadas)")

    while True:
        escolha = input("Sua escolha: ").strip()
        if escolha == '1':
            return {'tipo': 'casual', 'vitorias_necessarias': float('inf')}
        if escolha == '2':
            return {'tipo': 'melhor_de_3', 'vitorias_necessarias': 2}
        if escolha == '3':
            return {'tipo': 'melhor_de_5', 'vitorias_necessarias': 3}
        print(Cores.VERMELHO + "Opção inválida. Digite 1, 2 ou 3." + Cores.RESET)
#endregion
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#region Funções de Lógica do Jogo
def ler_jogada_jogador() -> str:
    """
    Lê a jogada do usuário, permitindo abreviações e validando a entrada.

    Returns:
        str: A jogada validada ('pedra', 'papel' ou 'tesoura').

    Como funciona:
    - Um dicionário `jogadas_validas` mapeia entradas possíveis (incluindo abreviações como
      'pe' ou 't') para a jogada canônica ('pedra', 'tesoura', etc.).
    - Um laço `while True` garante que a função continue solicitando a entrada até que uma
      jogada válida seja fornecida.
    - A entrada do usuário é convertida para minúsculas e tem espaços removidos. Se a entrada
      for uma chave no dicionário, seu valor correspondente é retornado.

    Pseudocódigo:
    1. Define um dicionário para mapear entradas válidas e abreviações.
    2. Inicia um laço infinito para solicitar a jogada.
    3. Lê e formata a entrada do usuário.
    4. Se a entrada for uma chave válida no dicionário, retorna a jogada correspondente.
    5. Caso contrário, exibe uma mensagem de erro e continua o laço.

    Examples:
        # Supondo que o usuário digite "t"
        >>> ler_jogada_jogador()
        'tesoura'
    """
    jogadas_validas = {
        'pedra': 'pedra', 'pe': 'pedra',
        'papel': 'papel', 'pa': 'papel',
        'tesoura': 'tesoura', 't': 'tesoura'
    }
    while True:
        prompt = f"{Cores.CIANO}[?] Declare sua arma (Pedra, Papel ou Tesoura): {Cores.RESET}"
        entrada = input(prompt).lower().strip()
        if entrada in jogadas_validas:
            return jogadas_validas[entrada]
        print(Cores.VERMELHO + "Arma desconhecida! Escolha entre Pedra, Papel ou Tesoura." + Cores.RESET)

#===============================================================================

def obter_jogada_computador_adaptativa(historico_jogador: list[str]) -> str:
    """
    Gera a jogada do computador com uma estratégia adaptativa.

    A IA tenta contra-atacar a jogada mais frequente do jogador para aumentar o desafio, mas
    com um elemento de aleatoriedade para não ser totalmente previsível.

    Args:
        historico_jogador (list[str]): Uma lista das jogadas anteriores do jogador na sessão.

    Returns:
        str: A jogada escolhida pelo computador ('pedra', 'papel' ou 'tesoura').

    Como funciona:
    - Se o histórico de jogadas do jogador for pequeno (menos de 5 rodadas), a IA joga de forma
      completamente aleatória para coletar dados.
    - Com um histórico maior, a IA analisa as últimas 5 jogadas do jogador para identificar
      a mais frequente, utilizando `collections.Counter`.
    - Com uma probabilidade de 75%, a IA escolherá a jogada que vence a jogada mais comum do
      jogador.
    - Com uma probabilidade de 25%, a IA ignora a análise e joga aleatoriamente, para evitar
      ser muito previsível.

    Pseudocódigo:
    1. Define as jogadas possíveis e as regras de contra-ataque.
    2. Se o histórico do jogador for muito curto, retorna uma jogada aleatória.
    3. Analisa as últimas 5 jogadas do jogador para encontrar a mais comum.
    4. Gera um número aleatório para decidir entre contra-atacar ou jogar aleatoriamente.
    5. Se decidir contra-atacar, seleciona a jogada que vence a mais comum do jogador.
    6. Caso contrário, seleciona uma jogada aleatória.
    7. Retorna a jogada escolhida.

    Examples:
        # O resultado é probabilístico.
        >>> historico = ['pedra', 'pedra', 'tesoura', 'pedra', 'pedra']
        >>> obter_jogada_computador_adaptativa(historico)
        # A jogada mais provável (75% de chance) será 'papel'.
    """
    jogadas = ['pedra', 'papel', 'tesoura']
    regras_vitoria = {'pedra': 'papel', 'papel': 'tesoura', 'tesoura': 'pedra'}

    if len(historico_jogador) < 5:
        return random.choice(jogadas)

    jogada_mais_comum = collections.Counter(historico_jogador[-5:]).most_common(1)[0][0]

    if random.random() < 0.75:
        return regras_vitoria[jogada_mais_comum]
    else:
        return random.choice(jogadas)

#===============================================================================

def determinar_vencedor(jogada_jogador: str, jogada_computador: str) -> str:
    """
    Determina o vencedor da rodada com base nas jogadas.

    Args:
        jogada_jogador (str): A jogada do jogador ('pedra', 'papel' ou 'tesoura').
        jogada_computador (str): A jogada do computador.

    Returns:
        str: 'jogador' se o jogador vencer, 'computador' se o computador vencer, ou 'empate'.

    Como funciona:
    - Um dicionário `regras` define a lógica de vitória (ex: 'pedra' vence 'tesoura').
    - A função primeiro verifica se as jogadas são iguais, resultando em um empate.
    - Em seguida, utiliza o dicionário de regras para verificar se a jogada do jogador vence
      a do computador.
    - Se nenhuma das condições anteriores for atendida, conclui-se que o computador venceu.

    Pseudocódigo:
    1. Define um dicionário com as regras de vitória.
    2. Compara as jogadas para verificar se houve empate.
    3. Se não houver empate, verifica se o jogador venceu consultando o dicionário de regras.
    4. Se o jogador não venceu, o computador é o vencedor.
    5. Retorna a string que representa o resultado.

    Examples:
        >>> determinar_vencedor('pedra', 'tesoura')
        'jogador'
    """
    regras = {
        'pedra': 'tesoura',
        'tesoura': 'papel',
        'papel': 'pedra'
    }
    if jogada_jogador == jogada_computador:
        return 'empate'
    if regras[jogada_jogador] == jogada_computador:
        return 'jogador'
    return 'computador'

#===============================================================================

def atualizar_estado(
    estado: dict, vencedor: str, jogada_jogador: str
) -> None:
    """
    Atualiza o placar e as estatísticas da sessão com base no resultado da rodada.

    Esta função modifica o dicionário `estado` diretamente (mutação), em vez de retornar um
    novo. Isso é eficiente para gerenciar um estado de jogo complexo.

    Args:
        estado (dict): O dicionário principal que contém todo o estado do jogo.
        vencedor (str): O vencedor da rodada ('jogador', 'computador' ou 'empate').
        jogada_jogador (str): A jogada feita pelo jogador nesta rodada.

    Como funciona:
    - A jogada do jogador é adicionada ao histórico e sua contagem é incrementada nas
      estatísticas.
    - Com base na string `vencedor`, a função incrementa o placar da partida atual e as
      estatísticas gerais de vitória, derrota ou empate.

    Pseudocódigo:
    1. Adiciona a jogada atual do jogador ao histórico.
    2. Incrementa a contagem da jogada específica nas estatísticas.
    3. Se o vencedor for 'jogador', incrementa o placar e as vitórias.
    4. Se o vencedor for 'computador', incrementa o placar e as derrotas.
    5. Se for 'empate', incrementa apenas a contagem de empates.
    """
    estado['historico_jogador'].append(jogada_jogador)
    estado['estatisticas']['jogadas_jogador'][jogada_jogador] += 1

    if vencedor == 'jogador':
        estado['placar_partida']['jogador'] += 1
        estado['estatisticas']['vitorias'] += 1
    elif vencedor == 'computador':
        estado['placar_partida']['computador'] += 1
        estado['estatisticas']['derrotas'] += 1
    else:  # empate
        estado['estatisticas']['empates'] += 1
#endregion
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#region Funções de Animação e Exibição
def animacao_mao_treme() -> None:
    """
    Exibe uma animação de contagem regressiva com uma mão (punho) tremendo.

    Como funciona:
    - A função itera sobre os textos "Pedra...", "Papel...", "Tesoura...".
    - A cada iteração, limpa a tela, exibe o texto atual e a arte ASCII de um punho.
    - Uma pausa de 0.7 segundos (`time.sleep`) é usada para criar o ritmo da animação.

    Pseudocódigo:
    1. Itera sobre a lista de textos da contagem.
    2. Em cada iteração, limpa a tela.
    3. Exibe o texto da contagem e a arte do punho.
    4. Pausa a execução por um breve período.
    """
    for texto in ["Pedra...", "Papel...", "Tesoura..."]:
        limpar_tela()
        print(f"\n\n{Cores.AMARELO}{texto.center(60)}{Cores.RESET}\n")
        for linha in ARTES_ASCII['punho']:
            print(" " * 20 + linha)
        time.sleep(0.7)
        limpar_tela()

#===============================================================================

def exibir_confronto_animado(
    jogador: str, jog_jogador: str, jog_computador: str, vencedor: str
) -> None:
    """
    Exibe a animação de impacto da batalha com base no resultado da rodada.

    Args:
        jogador (str): O nome do jogador.
        jog_jogador (str): A jogada do jogador.
        jog_computador (str): A jogada do computador.
        vencedor (str): O resultado da rodada ('jogador', 'computador' ou 'empate').

    Como funciona:
    - A função utiliza um conjunto de funções auxiliares para organizar a exibição.
    - A função `_selecionar_artes_e_mensagens` é a principal. Ela determina o resultado e, se
      houver um vencedor, consulta o dicionário `REGRAS_IMPACTO` para obter a arte especial
      (ex: `tesoura_quebrada`) e a mensagem correspondente.
    - Em seguida, as outras funções auxiliares montam e exibem a cena final do confronto,
      mostrando as duas artes lado a lado e as mensagens de resultado.

    Pseudocódigo:
    1. Limpa a tela.
    2. Chama a função `_selecionar_artes_e_mensagens` para obter as artes, cores e mensagens corretas.
    3. Se houver vencedor, ela consulta o dicionário `REGRAS_IMPACTO`.
    4. Imprime o cabeçalho da cena de confronto.
    5. Itera sobre as linhas das artes, imprimindo-as lado a lado.
    6. Imprime o rodapé com os nomes das jogadas.
    7. Exibe a mensagem de impacto e a mensagem final do vencedor.

    Examples:
        >>> exibir_confronto_animado('Carlos', 'pedra', 'tesoura', 'jogador')
        # Exibe a arte da pedra ao lado da tesoura quebrada e uma mensagem de vitória.
    """
    def _selecionar_artes_e_mensagens():
        """Seleciona artes, cores e mensagens de impacto com base no resultado da rodada."""
        if vencedor == 'empate':
            arte_jog = ARTES_ASCII[jog_jogador]
            arte_comp = ARTES_ASCII[jog_computador]
            cor = Cores.AMARELO
            msg_venc = ">> EMPATE! <<"
            msg_impacto = f"{Cores.AMARELO}* Empate! *{Cores.RESET}"
            return arte_jog, arte_comp, msg_impacto, cor, msg_venc

        if vencedor == 'jogador':
            jogada_vencedora, jogada_perdedora = jog_jogador, jog_computador
            cor, msg_venc = Cores.VERDE, f">> {jogador.upper()} VENCEU A RODADA! <<"
        else: # vencedor == 'computador'
            jogada_vencedora, jogada_perdedora = jog_computador, jog_jogador
            cor, msg_venc = Cores.VERMELHO, ">> COMPUTADOR VENCEU A RODADA! <<"

        impacto = REGRAS_IMPACTO.get((jogada_vencedora, jogada_perdedora))
        msg_impacto = f"{Cores.VERMELHO}{impacto['msg']}{Cores.RESET}"
        
        arte_vencedora = ARTES_ASCII[jogada_vencedora]
        arte_perdedora = ARTES_ASCII[impacto['arte_perdedor']]

        arte_jog, arte_comp = (arte_vencedora, arte_perdedora) if vencedor == 'jogador' else (arte_perdedora, arte_vencedora)
        
        return arte_jog, arte_comp, msg_impacto, cor, msg_venc

    def _imprimir_cabecalho():
        print(f"\n{Cores.CIANO}{jogador.upper().center(28)}{Cores.RESET}{'COMPUTADOR'.center(35)}")
        print("-" * 64)

    def _imprimir_artes_lado_a_lado(arte_jog, arte_comp):
        for i in range(len(arte_jog)):
            print(f"{arte_jog[i]:<28}    {arte_comp[i]}")
        print("-" * 64)

    def _imprimir_nomes_jogadas():
        print(f"[{jog_jogador.upper():^26}]    [{jog_computador.upper():^26}]")

    def _imprimir_mensagens(msg_impacto, cor, msg_venc):
        print(f"\n{msg_impacto.center(70)}\n")
        print(f"{cor}{msg_venc.center(64)}{Cores.RESET}")

    limpar_tela()
    arte_jogador, arte_computador, mensagem_impacto, cor_msg, msg_vencedor = _selecionar_artes_e_mensagens()
    
    _imprimir_cabecalho()
    _imprimir_artes_lado_a_lado(arte_jogador, arte_computador)
    _imprimir_nomes_jogadas()
    _imprimir_mensagens(mensagem_impacto, cor_msg, msg_vencedor)

#===============================================================================

def exibir_placar_partida(estado: dict) -> None:
    """
    Exibe o placar atual da partida (para modos "Melhor de X").

    Args:
        estado (dict): O dicionário de estado do jogo, contendo o placar e o modo.
    """
    nome_jogador = estado['nome_jogador']
    placar = estado['placar_partida']
    modo = estado['modo_jogo']['tipo'].replace('_', ' ').title()

    print("\n" + "="*40)
    print(f"  PLACAR DA PARTIDA ({modo})")
    print(f"  {Cores.CIANO}{nome_jogador}: {placar['jogador']}{Cores.RESET} | "
          f"{Cores.VERMELHO}Computador: {placar['computador']}{Cores.RESET}")
    print("="*40 + "\n")

#===============================================================================

def exibir_estatisticas_finais(estado: dict) -> None:
    """
    Exibe um resumo completo e estilizado da sessão de jogo ao final.

    Args:
        estado (dict): O dicionário de estado final do jogo.

    Como funciona:
    - A função calcula estatísticas agregadas, como a taxa de vitória e a arma favorita do
      jogador.
    - Exibe uma mensagem de encerramento e uma arte de troféu se o jogador tiver mais vitórias
      que derrotas.
    - Apresenta um painel detalhado com todas as estatísticas da sessão.

    Pseudocódigo:
    1. Limpa a tela.
    2. Extrai as estatísticas do dicionário de estado.
    3. Exibe o banner de "FIM DE JOGO".
    4. Compara vitórias e derrotas para exibir uma mensagem personalizada e o troféu.
    5. Calcula a taxa de vitória e a arma mais usada, tratando o caso de nenhum jogo ter sido jogado.
    6. Exibe o painel final com todas as estatísticas formatadas.
    """
    limpar_tela()
    stats = estado['estatisticas']
    nome_jogador = estado['nome_jogador']

    print(Cores.MAGENTA + "=========================================")
    print("|                                       |")
    print("|           FIM DE JOGO!                |")
    print("|                                       |")
    print("=========================================" + Cores.RESET)

    if stats['vitorias'] > stats['derrotas']:
        print(f"\nParabéns, {nome_jogador}! Você foi o grande campeão da sessão!")
        for linha in ARTES_ASCII['trofeu']:
            print(Cores.AMARELO + linha.center(40) + Cores.RESET)
    elif stats['derrotas'] > stats['vitorias']:
        print(f"\nNão foi dessa vez, {nome_jogador}. O computador levou a melhor!")
    else:
        print(f"\nUma batalha equilibrada, {nome_jogador}! Terminaram empatados.")

    total_jogos = stats['vitorias'] + stats['derrotas'] + stats['empates']
    taxa_vitoria = (stats['vitorias'] / total_jogos * 100) if total_jogos > 0 else 0
    
    arma_favorita = "Nenhuma"
    if total_jogos > 0:
        arma_favorita = max(stats['jogadas_jogador'], key=stats['jogadas_jogador'].get)

    print("\n--- SUAS ESTATÍSTICAS DA SESSÃO ---")
    print(f"  {Cores.VERDE}Vitórias: {stats['vitorias']}{Cores.RESET}")
    print(f"  {Cores.VERMELHO}Derrotas: {stats['derrotas']}{Cores.RESET}")
    print(f"  {Cores.AMARELO}Empates:  {stats['empates']}{Cores.RESET}")
    print(f"  Taxa de Vitória: {taxa_vitoria:.1f}%")
    print(f"  Sua Arma Favorita: {arma_favorita.capitalize()}")
    print("-" * 35)
#endregion
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#region Funções Principais de Orquestração
def executar_partida(estado: dict) -> None:
    """
    Gerencia o fluxo de uma única partida, seja casual ou "Melhor de X".

    Esta função orquestra o laço principal de uma partida, desde a primeira rodada até que
    a condição de vitória seja atingida.

    Args:
        estado (dict): O dicionário principal do estado do jogo.

    Como funciona:
    - Zera o placar da partida no início.
    - Entra em um laço `while True` que representa as rodadas.
    - A cada rodada, chama as funções apropriadas para: ler a jogada, animar, obter a jogada
      do computador, determinar o vencedor, atualizar o estado e exibir o resultado.
    - Verifica se a condição de vitória do modo "Melhor de X" foi alcançada. Se sim, exibe o
      vencedor da partida e encerra o laço.
    - Aguarda o jogador pressionar Enter para iniciar a próxima rodada.

    Pseudocódigo:
    1. Reseta o placar da partida.
    2. Inicia um laço infinito para as rodadas.
    3. Limpa a tela e exibe o cabeçalho e o placar da rodada.
    4. Executa a sequência de uma rodada completa (ler jogada, animar, etc.).
    5. Atualiza o estado do jogo com o resultado.
    6. Exibe a animação de confronto.
    7. Pausa para o jogador absorver o resultado da rodada.
    8. Verifica se algum jogador atingiu o número de vitórias necessárias.
    9. Se a partida terminou, anuncia o vencedor e quebra o laço.
    """
    estado['placar_partida'] = { 'jogador': 0, 'computador': 0 }
    rodada = 1

    while True:
        limpar_tela()
        print(f"--- RODADA {rodada} ---")
        if estado['modo_jogo']['tipo'] != 'casual':
            exibir_placar_partida(estado)

        jogada_jogador = ler_jogada_jogador()
        animacao_mao_treme()
        jogada_computador = obter_jogada_computador_adaptativa(estado['historico_jogador'])
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador)

        atualizar_estado(estado, vencedor, jogada_jogador)

        exibir_confronto_animado(
            estado['nome_jogador'], jogada_jogador, jogada_computador, vencedor
        )

        placar_jog = estado['placar_partida']['jogador']
        placar_comp = estado['placar_partida']['computador']
        vitorias_nec = estado['modo_jogo']['vitorias_necessarias']

        input("\nPressione Enter para continuar...")

        if placar_jog >= vitorias_nec or placar_comp >= vitorias_nec:
            limpar_tela()
            exibir_placar_partida(estado)
            vencedor_partida = estado['nome_jogador'] if placar_jog > placar_comp else "Computador"
            print(f"{Cores.VERDE}*** {vencedor_partida.upper()} VENCEU A PARTIDA! ***{Cores.RESET}")
            break

        rodada += 1

#===============================================================================

def jogar() -> None:
    """
    Função principal que inicia e gerencia o ciclo de vida completo do jogo.

    Esta é a função de mais alto nível que orquestra toda a experiência do usuário, desde a
    tela de boas-vindas até a exibição das estatísticas finais.

    Como funciona:
    - Prepara o ambiente inicial (banner, nome do jogador).
    - Inicializa um dicionário de `estado_geral` que persistirá por toda a sessão,
      armazenando estatísticas acumuladas.
    - Entra em um laço `while True` que permite ao jogador jogar múltiplas partidas.
    - A cada iteração, o jogador escolhe um modo de jogo, e a função `executar_partida` é
      chamada.
    - Após cada partida, pergunta se o jogador deseja jogar novamente. O laço é quebrado se a
      resposta não for 's'.
    - Ao final, exibe as estatísticas completas da sessão e uma mensagem de despedida.

    Pseudocódigo:
    1. Exibe o banner inicial e obtém o nome do jogador.
    2. Cria o dicionário de estado global para a sessão.
    3. Inicia um laço infinito para permitir múltiplas partidas.
    4. Dentro do laço, permite ao jogador escolher o modo de jogo.
    5. Chama a função `executar_partida` para rodar uma partida completa.
    6. Pergunta ao jogador se deseja jogar novamente.
    7. Se a resposta for não, encerra o laço.
    8. Ao sair do laço, exibe as estatísticas finais da sessão.
    9. Imprime uma mensagem de despedida.
    """
    exibir_banner_inicial()
    nome_jogador = obter_nome_jogador()

    estado_geral = {
        'nome_jogador': nome_jogador,
        'historico_jogador': [],
        'estatisticas': {
            'vitorias': 0, 'derrotas': 0, 'empates': 0,
            'jogadas_jogador': {'pedra': 0, 'papel': 0, 'tesoura': 0}
        }
    }

    while True:
        limpar_tela()
        modo_jogo = escolher_modo_jogo()
        estado_geral['modo_jogo'] = modo_jogo

        executar_partida(estado_geral)

        resposta = input("\nDeseja jogar outra partida? (s/n): ").lower().strip()
        if resposta != 's':
            break

    exibir_estatisticas_finais(estado_geral)
    print("\nObrigado por jogar! Até a próxima!\n")
#endregion
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# A construção `if __name__ == '__main__':` é uma convenção em Python.
# Ela garante que o código dentro deste bloco só será executado quando o arquivo for
# rodado diretamente como um script, e não quando for importado como um módulo.
# O bloco try...except garante uma saída elegante caso o usuário pressione Ctrl+C.
if __name__ == '__main__':
    try:
        jogar()
    except KeyboardInterrupt:
        print("\n\nJogo interrompido pelo usuário. Até a próxima!")
