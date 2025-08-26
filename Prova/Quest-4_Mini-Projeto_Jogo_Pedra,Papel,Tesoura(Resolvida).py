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

def determinar_vencedor(
    jogada_jogador: str, jogada_computador: str, regras: dict[str, str], cheat_mode_ativo: bool # <<< Quest-4 <<<<<<<<<<<<
) -> str:
    """ Determina o vencedor, considerando a regra da 'granada' se o modo de trapaça estiver ativo. """
# +++ BEGIN Quest-4 ++++++++++++++++++++ BEGIN Quest-4 ++++++++++++++++++++ BEGIN Quest-4 +++
    # Justificativa: Adiciona a lógica condicional para a 'granada'. A vitória só ocorre
    # se a jogada for 'granada' E o modo de trapaça estiver ativo, cumprindo os requisitos
    # de que a arma só funciona após a ativação do código.

    # (passo 1) Verificar a condição de vitória por trapaça.
    if jogada_jogador == 'granada' and cheat_mode_ativo: 
        return 'jogador' 
# +++ END Quest-4 ++++++++++++++++++++++ END Quest-4 ++++++++++++++++++++++ END Quest-4 +++++

    # (passo 2) Verifica empate
    if jogada_jogador == jogada_computador:
        return 'empate'
    # (passo 3) Verifica se o jogador vence com as regras padrão
    if regras[jogada_jogador] == jogada_computador:
        return 'jogador'
    # (passo 4) Caso contrário, computador vence
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
            placar['empates'] += 1
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
    print(f"Placar: Jogador {placar_dct['jogador']} | Computador {placar_dct['computador']} | Empates {placar_dct['empates']}")


def ler_jogar_novamente() -> bool:
    """ Pergunta ao usuário se deseja jogar novamente e retorna True para 's', False caso contrário. """
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'

#---------------------------------------------------------------------------------------------------

def jogar() -> None:
    """ Executa o loop principal do jogo, integrando o sistema de código de trapaça. """
    # (passo 1) Inicializa regras, placar e modo de trapaça
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}
    cheat_mode_ativo = False  # <<< Quest-4 <<<<<<<<<<<<

    # (passo 2) Loop principal do jogo
    while True:
        # (passo 3) Exibe cabeçalho
        print("\n--- Jogo Pedra, Papel, Tesoura ---")

        # (passo 4) Lê jogada do usuário
        jogada_jogador = ler_jogada()

# +++ BEGIN Quest-4 ++++++++++++++++++++ BEGIN Quest-4 ++++++++++++++++++++ BEGIN Quest-4 +++
        # Justificativa: Este bloco verifica se a entrada do jogador é o código de trapaça.
        # Se for, ele ativa o modo de trapaça e imediatamente solicita a jogada real,
        # cumprindo a exigência de que a ativação e a jogada ocorram na mesma rodada.

        # (passo 5) Verifica se a entrada é o código de trapaça.
        if jogada_jogador == 'codigo-de-trapaca': 
            # (passo 5a) Ativa o modo de trapaça.
            cheat_mode_ativo = True 
            # (passo 5b) Exibe a mensagem de ativação.
            print("Cheat code ativado – arma 'granada' liberada!")
            # (passo 5c) Pede a jogada de arma novamente.
            jogada_jogador = ler_jogada()
# +++ END Quest-4 ++++++++++++++++++++++ END Quest-4 ++++++++++++++++++++++ END Quest-4 +++++

        # (passo 6) Gera jogada do computador
        jogada_computador = obter_jogada_computador()

        # (passo 7) Determina vencedor, passando o estado do modo de trapaça.
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct, cheat_mode_ativo) # <<< Quest-4 <<<<<<<<<<<<

        # (passo 8) Exibe resultado e atualiza placar
        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)

        # (passo 9) Pergunta se deseja jogar novamente
        continuar = ler_jogar_novamente()
        if not continuar:
            break
    # (passo 10) Mensagem de agradecimento
    print("Obrigado por jogar!")

#---------------------------------------------------------------------------------------------------

# Inicia o jogo
if __name__ == '__main__':
    jogar()
