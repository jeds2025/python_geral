import random

#---------------------------------------------------------------------------------------------------

def obter_regras() -> dict[str, str]:
    """ Retorna um dicionário que representa as regras do jogo Pedra, Papel e Tesoura. """
    result = {
        'pedra'   : 'tesoura',
        'tesoura' : 'papel',
        'papel'   : 'pedra'
    }
    return result

#---------------------------------------------------------------------------------------------------

def obter_jogada_computador() -> str:
    """ Gera e retorna uma jogada aleatória válida para o computador. """
    jogadas_validas = ['pedra', 'papel', 'tesoura']
    jogada = random.choice(jogadas_validas)
    return jogada

#---------------------------------------------------------------------------------------------------

def determinar_vencedor( jogada_p1: str, jogada_p2: str, regras: dict[str, str] ) -> str:
    """ Determina o vencedor da rodada com base nas jogadas dos jogadores 1 e 2. """
    # (passo 1) Verifica empate
    if jogada_p1 == jogada_p2: # <<< Quest-5 <<<<<<<<<<<<
        return 'empate'
    # (passo 2, 3) Verifica se o Jogador 1 vence
    if regras[jogada_p1] == jogada_p2: # <<< Quest-5 <<<<<<<<<<<<
        return 'p1' # <<< Quest-5 <<<<<<<<<<<<
    # (passo 4) Caso contrário, Jogador 2 vence
    return 'p2' # <<< Quest-5 <<<<<<<<<<<<

#---------------------------------------------------------------------------------------------------

def atualizar_placar(placar: dict[str, int], vencedor_rodada: str) -> dict[str, int]:
    """ Atualiza o placar do jogo de forma genérica para 'p1' e 'p2'. """
    match vencedor_rodada:
        case 'p1':         # (passo 2) Incrementa placar do Jogador 1
            placar['p1'] += 1 # <<< Quest-5 <<<<<<<<<<<<
        case 'p2':         # (passo 3) Incrementa placar do Jogador 2
            placar['p2'] += 1 # <<< Quest-5 <<<<<<<<<<<<
        case 'empate':     # (passo 4) Incrementa empates
            placar['empates'] += 1
    # (passo 5) Retorna placar atualizado
    return placar

#---------------------------------------------------------------------------------------------------

def exibir_resultado_rodada(jogada_p1: str, jogada_p2: str, vencedor: str, nome_p1: str, nome_p2: str) -> None:
    """
    Exibe o resultado da rodada de forma dinâmica, usando os nomes dos jogadores.

    Pseudocódigo:
    1. Imprimir as escolhas de `nome_p1` e `nome_p2`.
    2. Com base no `vencedor`:
    3. Se for 'p1', imprimir a mensagem de vitória para `nome_p1`.
    4. Se for 'p2', imprimir a mensagem de vitória para `nome_p2`.
    5. Se for 'empate', imprimir a mensagem de empate.
    """
    # (passo 1) Imprime escolhas
    print(f"{nome_p1} escolheu: {jogada_p1.upper()} | {nome_p2} escolheu: {jogada_p2.upper()}") # <<< Quest-5 <<<<<<<<<<<<
    # (passo 2, 3, 4, 5) Mensagem de vitória ou empate
    match vencedor: # <<< Quest-5 <<<<<<<<<<<<
        case 'p1':  # (passo 3) Mensagem de vitória para P1
            print(f">> {nome_p1} venceu! <<") # <<< Quest-5 <<<<<<<<<<<<
        case 'p2':  # (passo 4) Mensagem de vitória para P2
            print(f">> {nome_p2} venceu! <<") # <<< Quest-5 <<<<<<<<<<<<
        case 'empate':   # (passo 5) Mensagem de empate
            print(">> Empate! <<") # <<< Quest-5 <<<<<<<<<<<<

#---------------------------------------------------------------------------------------------------

# +++ BEGIN Quest-5 ++++++++++++++++++++ BEGIN Quest-5 ++++++++++++++++++++ BEGIN Quest-5 +++
def ler_tipo_jogador(numero_jogador: int) -> str:
    """ Solicita o tipo do jogador (Humano ou Computador). """
    tipo = input(f"Defina o tipo do Jogador-{numero_jogador}: ").lower()
    return tipo

# Justificativa: Função que centraliza a lógica de obtenção da jogada. Ela atua como um
# dispatcher, chamando a função de input para 'Humano' ou a de geração aleatória para 'Computador'.
def obter_jogada(tipo_jogador: str, nome_jogador: str) -> str:
    """ Obtém a jogada de um jogador com base em seu tipo. """
    if tipo_jogador == 'humano':
        # Reutiliza a lógica de ler jogada, mas com um prompt dinâmico
        return input(f"{nome_jogador}, escolha sua arma: Pedra, Papel ou Tesoura? ").lower()
    else:  # Computador
        return obter_jogada_computador()
# +++ END Quest-5 ++++++++++++++++++++++ END Quest-5 ++++++++++++++++++++++ END Quest-5 +++++

def print_placar(placar_dct: dict[str, int], nome_p1: str, nome_p2: str) -> None: # <<< Quest-5 <<<<<<<<<<<<
    """
    Exibe o placar atual do jogo com os nomes dinâmicos dos jogadores.

    Args:
        placar_dct (dict[str, int]): O placar com chaves 'p1', 'p2', e 'empates'.
        nome_p1 (str): O nome de exibição do Jogador 1.
        nome_p2 (str): O nome de exibição do Jogador 2.
    """
    print(
        f"Placar: {nome_p1} {placar_dct['p1']} | " # <<< Quest-5 <<<<<<<<<<<<
        f"{nome_p2} {placar_dct['p2']} | Empates {placar_dct['empates']}" # <<< Quest-5 <<<<<<<<<<<<
    )

def ler_jogar_novamente() -> bool:
    """ Pergunta ao usuário se deseja jogar novamente e retorna True para 's', False caso contrário. """
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'

#---------------------------------------------------------------------------------------------------

def jogar() -> None:
    """ Executa o loop principal do jogo, agora com suporte a diferentes tipos de jogadores. """
    # (passo 1) Inicializa regras
    regras_dct = obter_regras()

# +++ BEGIN Quest-5 ++++++++++++++++++++ BEGIN Quest-5 ++++++++++++++++++++ BEGIN Quest-5 +++
    # Justificativa: Adicionado um bloco de configuração inicial que define os tipos de
    # jogadores (Humano/Computador) e seus nomes de exibição para toda a sessão de jogo.
    print("=== Jogo Pedra, Papel e Tesoura ===") # <<< Quest-5 <<<<<<<<<<<<
    # (passo 2.1) Define os tipos de jogadores
    tipo_p1 = ler_tipo_jogador(1) # <<< Quest-5 <<<<<<<<<<<<
    tipo_p2 = ler_tipo_jogador(2) # <<< Quest-5 <<<<<<<<<<<<

    # (passo 2.2) Define os nomes de exibição dos jogadores
    if tipo_p1 == tipo_p2: # <<< Quest-5 <<<<<<<<<<<<
        nome_p1, nome_p2 = f"{tipo_p1}-1", f"{tipo_p2}-2" # <<< Quest-5 <<<<<<<<<<<<
    else: # <<< Quest-5 <<<<<<<<<<<<
        nome_p1, nome_p2 = tipo_p1, tipo_p2 # <<< Quest-5 <<<<<<<<<<<<
# +++ END Quest-5 ++++++++++++++++++++++ END Quest-5 ++++++++++++++++++++++ END Quest-5 +++++

    # (passo 3) Inicializa placar genérico
    placar_dct = {"p1": 0, "p2": 0, "empates": 0} # <<< Quest-5 <<<<<<<<<<<<

    # (passo 4) Loop principal do jogo
    while True:
        print("\n--- Jogo Pedra, Papel, Tesoura ---") # <<< Quest-5 <<<<<<<<<<<<

# +++ BEGIN Quest-5 ++++++++++++++++++++ BEGIN Quest-5 ++++++++++++++++++++ BEGIN Quest-5 +++
        # Justificativa: A obtenção de jogadas foi generalizada para chamar a função
        # 'obter_jogada', que lida com a lógica de pedir input para humanos ou gerar
        # uma jogada aleatória para computadores.
        # (passo 4.1) Obtém a jogada de cada jogador com base no seu tipo
        jogada_p1 = obter_jogada(tipo_p1, nome_p1) # <<< Quest-5 <<<<<<<<<<<<
        jogada_p2 = obter_jogada(tipo_p2, nome_p2) # <<< Quest-5 <<<<<<<<<<<<
# +++ END Quest-5 ++++++++++++++++++++++ END Quest-5 ++++++++++++++++++++++ END Quest-5 +++++

        # (passo 4.2) Determina vencedor
        vencedor = determinar_vencedor(jogada_p1, jogada_p2, regras_dct) # <<< Quest-5 <<<<<<<<<<<<

        # (passo 4.3) Exibe resultado e atualiza placar
        exibir_resultado_rodada(jogada_p1, jogada_p2, vencedor, nome_p1, nome_p2) # <<< Quest-5 <<<<<<<<<<<<
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct, nome_p1, nome_p2) # <<< Quest-5 <<<<<<<<<<<<

        # (passo 4.4) Pergunta se deseja jogar novamente
        continuar = ler_jogar_novamente()
        if not continuar:
            break
    # (passo 5) Mensagem de agradecimento
    print("Obrigado por jogar!")

#---------------------------------------------------------------------------------------------------

# Inicia o jogo
if __name__ == '__main__':
    jogar()
