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
# +++ BEGIN Quest-2 ++++++++++++++++++++ BEGIN Quest-2 ++++++++++++++++++++ BEGIN Quest-2 +++
# Justificativa: A função original foi completamente reescrita para implementar a lógica dos
# níveis de dificuldade. Em vez de apenas escolher aleatoriamente, agora ela recebe o
# nível e a jogada do oponente para decidir sua própria jogada de forma estratégica.
def obter_jogada_computador(nivel: str, jogada_oponente: str, regras: dict) -> str: # <<< Quest-2 <<<<<<<<<<<<
    """ Gera a jogada do computador com base no nível de dificuldade e na jogada do oponente. """

    # (passo 1) Verificar o nível de dificuldade.
    match nivel:

        case 'facil':
            # (passo 2) Computador joga para perder: escolhe o que o oponente vence.
            arma_perdedora_para = {
                'pedra'  : 'papel',    # papel vence pedra
                'papel'  : 'tesoura',  # tesoura vence papel
                'tesoura': 'pedra'     # pedra vence tesoura
            }
            # ou simplesmente
            # arma_perdodora_para = regras
            return arma_perdedora_para[jogada_oponente]     
        
        case 'dificil': 
            # (passo 3) Computador joga para ganhar: escolhe a arma que faz oponente perder.
            arma_vencedora_para = {
                'pedra'  : 'papel',    # papel vence pedra
                'papel'  : 'tesoura',  # tesoura vence papel
                'tesoura': 'pedra'     # pedra vence tesoura
            }
            # ou simplesmente
            # arma_vencedora_para = {v: k for k, v in arma_perdedora_para.items()}
            return arma_vencedora_para[jogada_oponente]
            
        case 'normal': 
            # (passo 4) Comportamento padrão: seleciona aleatoriamente.
            armas = ['pedra', 'papel', 'tesoura'] 
            return random.choice(armas)

    raise ValueError(f"Nível de dificuldade inválido '{nivel}'.")
# +++ END Quest-2 ++++++++++++++++++++++ END Quest-2 ++++++++++++++++++++++ END Quest-2 +++++
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
    return input("Escolha sua arma: Pedra, Papel ou Tesoura? > ").lower()


def print_placar(placar_dct: dict[str, int]) -> None:
    """ Exibe o placar atual do jogo. """
    print(
        f"Placar: Jogador {placar_dct['jogador']} | "
        f"Computador {placar_dct['computador']} | Empates {placar_dct['empates']}"
    )


def ler_jogar_novamente() -> bool:
    """ Pergunta ao usuário se deseja jogar novamente e retorna True para 's', False caso contrário. """
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'

#---------------------------------------------------------------------------------------------------
# +++ BEGIN Quest-2 ++++++++++++++++++++ BEGIN Quest-2 ++++++++++++++++++++ BEGIN Quest-2 +++
def ler_nivel_dificuldade() -> str:
    """ Solicita e valida o nível de dificuldade escolhido pelo usuário. """
    return input("Escolha o nível de dificuldade (facil / normal / dificil): ").lower()
# +++ END Quest-2 ++++++++++++++++++++++ END Quest-2 ++++++++++++++++++++++ END Quest-2 +++++
#---------------------------------------------------------------------------------------------------

def jogar() -> None:
    """ Executa o loop principal do jogo, integrando a seleção de dificuldade. """
    # (passo 1) Inicializa regras e placar
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}

    # (passo 2) Exibe o cabeçalho principal do jogo.
    print("=== Jogo Pedra, Papel e Tesoura ===") 
# +++ BEGIN Quest-2 ++++++++++++++++++++ BEGIN Quest-2 ++++++++++++++++++++ BEGIN Quest-2 +++
    # Justificativa: Adicionado para cumprir o requisito de perguntar o nível de
    # dificuldade uma única vez, antes do início do loop de rodadas do jogo.
    # (passo 3) Chamar `ler_nivel_dificuldade` para obter e armazenar o nível escolhido.
    nivel_dificuldade = ler_nivel_dificuldade() 
# +++ END Quest-2 ++++++++++++++++++++++ END Quest-2 ++++++++++++++++++++++ END Quest-2 +++++

    # (passo 4) Loop principal do jogo
    while True:
        # (passo 5) Lê jogada do usuário
        jogada_jogador = ler_jogada()

# +++ BEGIN Quest-2 ++++++++++++++++++++ BEGIN Quest-2 ++++++++++++++++++++ BEGIN Quest-2 +++
        # Justificativa: A chamada para obter a jogada do computador foi modificada para
        # passar os parâmetros necessários (nível de dificuldade e jogada do oponente) para
        # a nova lógica estratégica da função `obter_jogada_computador`.
        # (passo 6) Gera jogada do computador, passando nível e jogada do usuário.
        jogada_computador = obter_jogada_computador( nivel_dificuldade, jogada_jogador, regras_dct )
# +++ END Quest-2 ++++++++++++++++++++++ END Quest-2 ++++++++++++++++++++++ END Quest-2 +++++

        # (passo 7) Determina vencedor
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)

        # (passo 8) Exibe resultado e atualiza placar
        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)

        # (passo 9) Pergunta se deseja jogar novamente
        continuar = ler_jogar_novamente()
        if not continuar:
            break
        print("--------------------------------------") # Adicionado para separar as rodadas # <<< Quest-2 <<<<<<<<<<<<

    # (passo 10) Mensagem de agradecimento
    print("Obrigado por jogar!")

#---------------------------------------------------------------------------------------------------

# Inicia o jogo
if __name__ == '__main__':
    jogar()
