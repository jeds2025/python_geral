import random

#---------------------------------------------------------------------------------------------------

def obter_regras() -> dict[str, str]:
    """ Retorna um dicionário que representa as regras do jogo Pedra, Papel e Tesoura. """
    # (passo 1) Cria o dicionário de regras
    result = {
        'pedra'   : 'tesoura',
        'tesoura' : 'papel',
        'papel'   : 'pedra'
    }
    # (passo 2) Retorna o dicionário
    return result

#---------------------------------------------------------------------------------------------------

def obter_jogada_computador() -> str:
    """ Gera e retorna uma jogada aleatória válida para o computador. """
    # (passo 1) Define as jogadas válidas
    jogadas_validas = ['pedra', 'papel', 'tesoura']
    # (passo 2) Seleciona aleatoriamente
    jogada = random.choice(jogadas_validas)
    # (passo 3) Retorna a jogada
    return jogada

#---------------------------------------------------------------------------------------------------

def determinar_vencedor(jogada_jogador: str, jogada_computador: str, regras: dict[str, str]) -> str:
    """ Determina o vencedor da rodada com base nas jogadas do jogador e do computador. """
    # (passo 1) Verifica empate
    if jogada_jogador == jogada_computador:
        return 'empate'
    # (passo 2) Verifica se o jogador vence
    if regras[jogada_jogador] == jogada_computador:
        return 'jogador'
    # (passo 3) Caso contrário, computador vence
    return 'computador'

#---------------------------------------------------------------------------------------------------

def atualizar_placar(placar: dict[str, int], vencedor_rodada: str) -> dict[str, int]:
    """ Atualiza o placar do jogo conforme o vencedor_rodada. """
    match vencedor_rodada:
        case 'jogador':    # (passo 1) Incrementa placar do jogador
            placar['jogador'] += 1
        case 'computador': # (passo 2) Incrementa placar do computador
            placar['computador'] += 1
        case 'empate':     # (passo 3) Incrementa empates
            placar['empates'] += 1
    # (passo 4) Retorna placar atualizado
    return placar

#---------------------------------------------------------------------------------------------------

def obter_resultado_rodada(vencedor_rodada: str) -> str:
    match vencedor_rodada:
        case 'jogador':  # (passo 2) Mensagem de vitória
            print(">> Você venceu! <<")
        case 'empate':   # (passo 3) Mensagem de empate
            print(">> Empate! <<")
        case _:          # (passo 4) Mensagem de derrota
            print(">> Você perdeu! <<")

# Quest-5 de 6: Exibir Resultado da Rodada
def print_resultado_rodada(jogada_jogador: str, jogada_computador: str, vencedor_rodada: str) -> str:
    """ Exibe o resultado da rodada de forma formatada para o usuário. """
    # (passo 1) Imprime escolhas
    print(f"Você escolheu: {jogada_jogador.upper()} | Computador escolheu: {jogada_computador.upper()}")
    # (passo 2, 3, 4) Mensagem de vitória, empate ou derrota
    return obter_resultado_rodada(vencedor_rodada)

#---------------------------------------------------------------------------------------------------

# +++ BEGIN Quest-3 ++++++++++++++++++++ BEGIN Quest-3 ++++++++++++++++++++ BEGIN Quest-3 +++
def print_historico_jogadas(historico: list[dict[str, str]]) -> None: # <<< Quest-3 <<<<<<<<<<<<
    """ Exibe o histórico de todas as rodadas jogadas em uma sessão. """
    # (passo 1) Imprimir o cabeçalho "Histórico de Jogadas".
    print("\n=== Histórico de Jogadas ===")

    # (passo 2) Para cada rodada na lista de histórico:
    for rodada in historico:
        # (passo 2.1) Com base no valor de 'vencedor', definir a mensagem.
        resultado_msg = obter_resultado_rodada( rodada['vencedor'] )
        # (passo 2.2) Imprimir a linha formatada.
        print( f"{rodada['jogador'].upper()} vs {rodada['computador'].upper()}, {resultado_msg}" ) 
# +++ END Quest-3 ++++++++++++++++++++++ END Quest-3 ++++++++++++++++++++++ END Quest-3 +++++

#---------------------------------------------------------------------------------------------------

def ler_jogada() -> str:
    """ Solicita ao usuário que digite sua jogada e retorna a entrada em minúsculas. """
    return input("Escolha sua arma: Pedra, Papel ou Tesoura? ").lower()


def print_placar(placar_dct: dict[str, int]) -> None:
    """ Exibe o placar atual do jogo. """
    print(f"Placar: Jogador {placar_dct['jogador']} | Computador {placar_dct['computador']} | Empates {placar_dct['empates']}")


def ler_jogar_novamente() -> bool:
    """ Pergunta ao usuário se deseja jogar novamente e retorna True para 's', False caso contrário. """
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'

#---------------------------------------------------------------------------------------------------

def jogar() -> None:
    """ Executa o loop principal do jogo, registrando e exibindo um histórico das rodadas. """
    # (passo 1) Inicializa regras e placar
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}

# +++ BEGIN Quest-3 ++++++++++++++++++++ BEGIN Quest-3 ++++++++++++++++++++ BEGIN Quest-3 +++
    # (passo 2) Inicializar uma lista vazia para armazenar o histórico das rodadas.
    historico_rodadas = [] 
# +++ END Quest-3 ++++++++++++++++++++++ END Quest-3 ++++++++++++++++++++++ END Quest-3 +++++

    # (passo 3) Loop principal do jogo
    while True:
        # (passo 3.1) Exibe cabeçalho
        print("\n--- Jogo Pedra, Papel, Tesoura ---")

        # (passo 3.2) Lê jogada do usuário
        jogada_jogador = ler_jogada()

        # (passo 3.3) Gera jogada do computador
        jogada_computador = obter_jogada_computador()

        # (passo 3.4) Determina vencedor
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)

        # (passo 3.5) Exibe resultado e atualiza placar
        print_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)

# +++ BEGIN Quest-3 ++++++++++++++++++++ BEGIN Quest-3 ++++++++++++++++++++ BEGIN Quest-3 +++
        # (passo 3.6) Armazenar os dados da rodada na lista de histórico.
        dados_rodada = { 'jogador': jogada_jogador, 'computador': jogada_computador, 'vencedor': vencedor }
        historico_rodadas.append(dados_rodada)
# +++ END Quest-3 ++++++++++++++++++++++ END Quest-3 ++++++++++++++++++++++ END Quest-3 +++++

        # (passo 3.7) Pergunta se deseja jogar novamente
        continuar = ler_jogar_novamente()
        print("--------------------------") # <<< Quest-3 <<<<<<<<<<<<
        # (passo 3.9) Se a resposta for não, interromper o loop.
        if not continuar:
            break

# +++ BEGIN Quest-3 ++++++++++++++++++++ BEGIN Quest-3 ++++++++++++++++++++ BEGIN Quest-3 +++
    # (passo 4) Chamar a função `print_historico_jogadas`.
    print_historico_jogadas(historico_rodadas) # <<< Quest-3 <<<<<<<<<<<<
# +++ END Quest-3 ++++++++++++++++++++++ END Quest-3 ++++++++++++++++++++++ END Quest-3 +++++

    # (passo 5) Mensagem de agradecimento
    print("\nObrigado por jogar!") # <<< Quest-3 <<<<<<<<<<<<

#---------------------------------------------------------------------------------------------------

# Inicia o jogo
if __name__ == '__main__':
    jogar()
