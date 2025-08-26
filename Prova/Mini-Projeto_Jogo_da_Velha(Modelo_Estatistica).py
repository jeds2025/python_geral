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

def determinar_vencedor(jogada_jogador: str, jogada_computador: str, regras: dict[str, str]) -> str:
    """ Determina o vencedor da rodada com base nas jogadas do jogador e do computador. """
    if jogada_jogador == jogada_computador:
        return 'empate'
    # Verifica se a jogada é válida antes de acessar as regras
    if jogada_jogador in regras and regras[jogada_jogador] == jogada_computador:
        return 'jogador'
    return 'computador'

#---------------------------------------------------------------------------------------------------

def atualizar_placar(placar: dict[str, int], vencedor_rodada: str) -> dict[str, int]:
    """ Atualiza o placar do jogo conforme o vencedor_rodada. """
    match vencedor_rodada:
        case 'jogador':
            placar['jogador'] += 1
        case 'computador':
            placar['computador'] += 1
        case 'empate':
            placar['empate'] += 1
    return placar

#---------------------------------------------------------------------------------------------------

def exibir_resultado_rodada(jogada_jogador: str, jogada_computador: str, vencedor_rodada: str) -> None:
    """ Exibe o resultado da rodada de forma formatada para o usuário. """
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
    """ Solicita ao usuário que digite sua jogada e retorna a entrada em minúsculas. """
    return input("Escolha sua arma: Pedra, Papel ou Tesoura? ").lower()


def print_placar(placar_dct: dict[str, int]) -> None:
    """ Exibe o placar atual do jogo. """
    print(f"Placar: Jogador {placar_dct['jogador']} | Computador {placar_dct['computador']} | Empates {placar_dct['empate']}")


def ler_jogar_novamente() -> bool:
    """ Pergunta ao usuário se deseja jogar novamente e retorna True para 's', False caso contrário. """
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'



def exibir_analise_estatistica(historico_partida: list[tuple[str, str, str]]) -> None:
    # (passo 1) Lida com o caso de nenhuma rodada ter sido jogada.
    total_rodadas = len(historico_partida)
    if total_rodadas == 0:
        print("\nNenhuma rodada foi jogada para gerar estatísticas.")
        return

    # (passo 2) Imprime o cabeçalho.
    print("\n=== Estatísticas da Partida ===")

    # (passo 3) Calcula a jogada mais usada.
    jogadas_validas = ['pedra', 'papel', 'tesoura']
    jogadas_usuario = [r[0] for r in historico_partida if r[0] in jogadas_validas]
    if jogadas_usuario:
        contagem = {j: jogadas_usuario.count(j) for j in jogadas_validas}
        jogada_mais_usada = max(contagem, key=contagem.get)
        percentual = (contagem[jogada_mais_usada] / len(jogadas_usuario)) * 100
        print(f"Sua jogada mais usada: {jogada_mais_usada.upper()} ({percentual:.1f}% das jogadas)")

        # (passo 4) Calcula a taxa de vitória com essa jogada.
        vitorias_com_jogada = len([r for r in historico_partida if r[0] == jogada_mais_usada and r[2] == 'jogador'])
        taxa_vitoria = (vitorias_com_jogada / contagem[jogada_mais_usada]) * 100
        print(f"Taxa de vitória com {jogada_mais_usada.upper()}: {taxa_vitoria:.1f}%")

    # (passo 5) Calcula a maior sequência de vitórias.
    maior_sequencia, sequencia_atual = 0, 0
    for _, _, vencedor in historico_partida:
        if vencedor == 'jogador':
            sequencia_atual += 1
        else:
            maior_sequencia = max(maior_sequencia, sequencia_atual)
            sequencia_atual = 0
    maior_sequencia = max(maior_sequencia, sequencia_atual)
    print(f"Maior sequência de vitórias: {maior_sequencia} rodadas")


#---------------------------------------------------------------------------------------------------

def jogar() -> None:
    
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empate": 0}
    historico_partida: list[tuple[str, str, str]] = [] # <<< Quest-5 <<<<<<<<<<<<

    while True:
        print("\n--- Jogo Pedra, Papel, Tesoura ---")
        jogada_jogador = ler_jogada()
        jogada_computador = obter_jogada_computador()
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)

        historico_partida.append((jogada_jogador, jogada_computador, vencedor)) # <<< Quest-5 <<<<<<<<<<<<

        # Evita exibir resultado para jogadas inválidas, mantendo-as no histórico
        if jogada_jogador not in regras_dct:
             print("Jogada inválida! Por favor, tente novamente.")
        else:
            exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
            placar_dct = atualizar_placar(placar_dct, vencedor)
            print_placar(placar_dct)

        continuar = ler_jogar_novamente()
        if not continuar:
            break

    exibir_analise_estatistica(historico_partida) # <<< Quest-5 <<<<<<<<<<<<
    
    print("\nObrigado por jogar!")

#---------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    jogar()
