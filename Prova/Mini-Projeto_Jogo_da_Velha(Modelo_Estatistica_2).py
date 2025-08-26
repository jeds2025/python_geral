import random

#---------------------------------------------------------------------------------------------------

def obter_regras() -> dict[str, str]:
    """ Retorna as regras do jogo. """
    result = {
        'pedra'   : 'tesoura',
        'tesoura' : 'papel',
        'papel'   : 'pedra'
    }
    return result

#---------------------------------------------------------------------------------------------------

def obter_jogada_computador() -> str:
    """ Retorna uma jogada aleatória para o computador. """
    jogadas_validas = ['pedra', 'papel', 'tesoura']
    jogada = random.choice(jogadas_validas)
    return jogada

#---------------------------------------------------------------------------------------------------

def determinar_vencedor(jogada_jogador: str, jogada_computador: str, regras: dict[str, str]) -> str:
    """ Retorna o vencedor da rodada. """
    if jogada_jogador == jogada_computador:
        return 'empate'
    if regras[jogada_jogador] == jogada_computador:
        return 'jogador'
    return 'computador'

#---------------------------------------------------------------------------------------------------

def atualizar_placar(placar: dict[str, int], vencedor_rodada: str) -> dict[str, int]:
    """ Atualiza o placar. """
    match vencedor_rodada:
        case 'jogador':
            placar['jogador'] += 1     # Incrementa placar de jogador
        case 'computador':
            placar['computador'] += 1  # Incrementa placar de computador
        case 'empate':
            placar['empate'] += 1     # Incrementa empates
    # Retorna o placar atualizado
    return placar

#---------------------------------------------------------------------------------------------------

def exibir_resultado_rodada(jogada_jogador: str, jogada_computador: str, vencedor_rodada: str) -> None:
    """ Imprime o resultado da rodada. """
    print(f"Você escolheu: {jogada_jogador.upper()} | Computador escolheu: {jogada_computador.upper()}")
    match vencedor_rodada:
        case 'jogador':
            print(">> Você venceu! <<")
        case 'empate':
            print(">> Empate! <<")
        case _:
            print(">> Você perdeu! <<")

#---------------------------------------------------------------------------------------------------

def ler_jogada() -> str:
    """ Lê a jogada do usuário. """
    return input("Escolha sua arma: Pedra, Papel ou Tesoura? ").lower()


def print_placar(placar_dct: dict[str, int]) -> None:
    """ Exibe o placar atual. """
    print(f"Placar: Jogador {placar_dct['jogador']} | Computador {placar_dct['computador']} | Empates {placar_dct['empate']}")


def ler_jogar_novamente() -> bool:
    """ Pergunta se o usuário deseja jogar novamente. """
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'

#---------------------------------------------------------------------------------------------------

def exibir_estatisticas(historico: list[tuple[str, str, str]]) -> None: # <<< Quest-5 <<<<<<<<<<<<
    # (passo 1) Imprimir o cabeçalho da seção de estatísticas.
    print("\n--- Suas Estatísticas de Vitória ---") # <<< Quest-5 <<<<<<<<<<<<
    # (passo 2) Definir uma lista com as jogadas possíveis.
    jogadas_possiveis = ['pedra', 'papel', 'tesoura'] # <<< Quest-5 <<<<<<<<<<<<

    # (passo 3) Para cada 'jogada' na lista de jogadas possíveis:
    for jogada in jogadas_possiveis: # <<< Quest-5 <<<<<<<<<<<<
        # (passo 4) Filtrar vitórias do jogador com a jogada atual usando list comprehension.
        vitorias = [r for r in historico if r[0] == jogada and r[2] == 'jogador'] # <<< Quest-5 <<<<<<<<<<<<
        # (passo 5) Calcular o número de vitórias.
        num_vitorias = len(vitorias) # <<< Quest-5 <<<<<<<<<<<<
        # (passo 6) Imprimir a contagem de vitórias para a 'jogada' atual.
        print(f"- Você venceu {num_vitorias} vezes com {jogada.upper()}.") # <<< Quest-5 <<<<<<<<<<<<

#---------------------------------------------------------------------------------------------------

def jogar() -> None:
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empate": 0}

    historico_rodadas = [] # <<< Quest-5 <<<<<<<<<<<<

    # (passo 2) Iniciar o loop principal do jogo.
    while True:
        print("\n--- Jogo Pedra, Papel, Tesoura ---")

        # (passo 3) Executar a lógica de uma rodada.
        jogada_jogador = ler_jogada()

        jogada_computador = obter_jogada_computador()

        # (passo 4) Determinar o vencedor da rodada.
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)

        # (passo 5) Adicionar os detalhes da rodada ao `historico_rodadas`.
        historico_rodadas.append((jogada_jogador, jogada_computador, vencedor)) # <<< Quest-5 <<<<<<<<<<<<

        # (passo 6) Exibir resultado e atualizar placar.
        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)

        # (passo 7) Perguntar para continuar.
        continuar = ler_jogar_novamente()
        if not continuar:
            break

    exibir_estatisticas(historico_rodadas) # <<< Quest-5 <<<<<<<<<<<<

    # (passo 9) Exibir mensagem de despedida.
    print("\nObrigado por jogar!") # <<< Quest-5 <<<<<<<<<<<<

#---------------------------------------------------------------------------------------------------

# Inicia o jogo
if __name__ == '__main__':
    jogar()
