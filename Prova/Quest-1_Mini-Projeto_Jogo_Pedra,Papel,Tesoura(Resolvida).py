"""
PROF CARLOS. Sua resposta não precisa ser exatamente igual. O IMPORTANTE é, você sabe usar o CFG 
  para traduzir o seu programa. É comum, esquecermos de traduzir algumas mensagens do jogo.
  Logo, a correção não foi rigorosa.
"""

import random

# +++ BEGIN Quest-1 ++++++++++++++++++++ BEGIN Quest-1 ++++++++++++++++++++ BEGIN Quest-1 +++
# Justificativa: A questão exige a centralização de todas as configurações, regras e
# textos em uma única estrutura de dados (CFG) para tornar o jogo "data-driven".
# Isso desacopla a lógica do jogo dos dados que ele utiliza, facilitando a manutenção,
# tradução para outros idiomas e futuras expansões sem alterar o código principal.

CFG = {
    # Português - Brasil
    'pt-br': {
        'jogadas_validas': ['pedra', 'papel', 'tesoura'],
        'regras': {
            'pedra': 'tesoura',
            'papel': 'pedra',
            'tesoura': 'papel',
        },
        'mensagens': {
            'vitoria': '>> Você venceu! <<',
            'derrota': '>> Você perdeu! <<',
            'empate': '>> Empate! <<',
            'invalida': 'Jogada inválida! Por favor, escolha uma das opções válidas.',
            'jogar_novamente': 'Jogar novamente? (s/n): ',
            'titulo_jogo': '--- Jogo Pedra, Papel, Tesoura ---',
            'prompt_jogada': 'Escolha sua jogada ({options}): ',
            'placar_template': 'Placar: Jogador {jogador} | Computador {computador} | Empates {empates}',
            'agradecimento': 'Obrigado por jogar!',
        },
        'respostas_validas': {
            'sim': 's',
            'nao': 'n'
        }
    },
    # Inglês - Estados Unidos
    'en-us': {
        'jogadas_validas': ['rock', 'paper', 'scissors'],
        'regras': {
            'rock'    : 'scissors',
            'paper'   : 'rock',
            'scissors': 'paper',
        },
        'mensagens': {
            'vitoria': '>> You won! <<',
            'derrota': '>> You lost! <<',
            'empate': ">> It's a tie! <<",
            'invalida': 'Invalid move! Please choose one of the valid options.',
            'jogar_novamente': 'Play again? (y/n):',
            'titulo_jogo': '--- Rock, Paper, Scissors Game ---',
            'prompt_jogada': 'Choose your move ({options}): ',
            'placar_template': 'Score: Player {jogador} | Computer {computador} | Ties {empates}', 
            'agradecimento': 'Thanks for playing!',
        },
        'respostas_validas': {
            'sim': 'y',
            'nao': 'n'
        }
    },
    # Coreano
    'ko': {
        'jogadas_validas': ['바위', '보', '가위'],
        'regras': {
            '바위': '가위',   # Pedra quebra Tesoura
            '보': '바위',     # Papel embrulha Pedra
            '가위': '보',     # Tesoura corta Papel
        },
        'mensagens': {
            'vitoria': '>> 당신이 이겼습니다! <<', # Você ganhou!
            'derrota': '>> 당신이 졌습니다! <<',   # Você perdeu!
            'empate': '>> 무승부입니다! <<',       # Empate!
            'invalida': '잘못된 입력입니다! 유효한 옵션을 선택하세요.', # Entrada Inválida
            'jogar_novamente': '다시 플레이 하시겠습니까? (y/n)',  # Jogar novamente
            'titulo_jogo': '--- 가위바위보 게임 ---',
            'prompt_jogada': '움직임을 선택하세요 ({options}): ',
            'placar_template': '점수: 플레이어 {jogador} | 컴퓨터 {computador} | 무승부 {empates}',
            'agradecimento': '플레이해주셔서 감사합니다!', 
        },
        'respostas_validas': {
            'sim': 'y',  # É isso mesmo y ou n, yes / no. É como os coreanos usam
            'nao': 'n'
        }
    }
}

# Definição do idioma a ser utilizado no jogo
# Mude para 'en-us' ou 'ko' para testar outros idiomas
IDIOMA = 'pt-br'

# Variável global com as configurações específicas do idioma selecionado para simplificar acessos
CFG_IDIOMA = CFG[IDIOMA] # <<< Quest-1 <<<<<<<<<<<<
# +++ END Quest-1 ++++++++++++++++++++++ END Quest-1 ++++++++++++++++++++++ END Quest-1 +++++

#---------------------------------------------------------------------------------------------------

def obter_jogada_computador() -> str: # <<< Quest-1 <<<<<<<<<<<<
    """ Gera uma jogada aleatória para o computador com base nas configurações globais. """
    jogadas_validas = CFG_IDIOMA['jogadas_validas'] # <<< Quest-1 <<<<<<<<<<<<
    jogada = random.choice(jogadas_validas)
    return jogada

#---------------------------------------------------------------------------------------------------

def determinar_vencedor(jogada_jogador: str, jogada_computador: str) -> str: # <<< Quest-1 <<<<<<<<<<<<
    """ Determina o vencedor da rodada, consultando as regras na configuração global. """
    if jogada_jogador == jogada_computador:
        return 'empate'
    if CFG_IDIOMA['regras'][jogada_jogador] == jogada_computador: # <<< Quest-1 <<<<<<<<<<<<
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
            placar['empates'] += 1
    return placar

#---------------------------------------------------------------------------------------------------

def exibir_resultado_rodada(jogada_jogador: str, jogada_computador: str, vencedor_rodada: str) -> None: # <<< Quest-1 <<<<<<<<<<<<
    """ Exibe o resultado da rodada, usando textos da configuração global. """
    print(f"Você escolheu: {jogada_jogador.upper()} | Computador escolheu: {jogada_computador.upper()}")
    match vencedor_rodada:
        case 'jogador':
            print(CFG_IDIOMA['mensagens']['vitoria']) # <<< Quest-1 <<<<<<<<<<<<
        case 'empate':
            print(CFG_IDIOMA['mensagens']['empate']) # <<< Quest-1 <<<<<<<<<<<<
        case _:
            print(CFG_IDIOMA['mensagens']['derrota']) # <<< Quest-1 <<<<<<<<<<<<

#---------------------------------------------------------------------------------------------------

def ler_jogada() -> str:
    """ Solicita ao usuário que digite sua jogada e retorna a entrada em minúsculas. """
    opcoes_str = ", ".join(CFG_IDIOMA['jogadas_validas'])  # <<< Quest-1 <<<<<<<<<<<<
    prompt = CFG_IDIOMA['mensagens']['prompt_jogada'].format(options=opcoes_str)  # <<< Quest-1 <<<<<<<<<<<<
    return input(prompt).lower()  # <<< Quest-1 <<<<<<<<<<<<


def print_placar(placar_dct):
    """ Mostra o placar atual do jogo, usando o texto do idioma escolhido. """
    # Pega o texto do placar no idioma atual
    texto = CFG_IDIOMA['mensagens']['placar_template']  # <<< Quest-1 <<<<<<<<<<<<
    # Substitui as chaves pelos valores do placar
    placar_formatado = texto.format(  # <<< Quest-1 <<<<<<<<<<<<
        jogador=placar_dct['jogador'],
        computador=placar_dct['computador'],
        empates=placar_dct['empates']
    )
    print(placar_formatado)  # <<< Quest-1 <<<<<<<<<<<<


def ler_jogar_novamente() -> bool:
    """ Pergunta ao usuário se deseja jogar novamente e retorna True para 's', False caso contrário. """
    resposta = input(CFG_IDIOMA['mensagens']['jogar_novamente']).lower()  # <<< Quest-1 <<<<<<<<<<<<
    return resposta == CFG_IDIOMA['respostas_validas']['sim']  # <<< Quest-1 <<<<<<<<<<<<

#---------------------------------------------------------------------------------------------------

def jogar() -> None:
    """ Executa o loop principal do jogo, orientado pela configuração global. """
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}

    while True:
        print(f"\n{CFG_IDIOMA['mensagens']['titulo_jogo']}")  # <<< Quest-1 <<<<<<<<<<<<

        jogada_jogador = ler_jogada()

# +++ BEGIN Quest-1 ++++++++++++++++++++ BEGIN Quest-1 ++++++++++++++++++++ BEGIN Quest-1 +++
        # Justificativa: Um laço de validação foi adicionado para garantir que a entrada do
        # jogador seja uma das jogadas válidas definidas na configuração global. Isso torna o
        # programa mais robusto e utiliza a mensagem de erro especificada no `CFG_IDIOMA`.
        while jogada_jogador not in CFG_IDIOMA['jogadas_validas']: # <<< Quest-1 <<<<<<<<<<<<
            print(CFG_IDIOMA['mensagens']['invalida'])  # <<< Quest-1 <<<<<<<<<<<<
            jogada_jogador = ler_jogada()
# +++ END Quest-1 ++++++++++++++++++++++ END Quest-1 ++++++++++++++++++++++ END Quest-1 +++++

        jogada_computador = obter_jogada_computador() # <<< Quest-1 <<<<<<<<<<<<

        vencedor = determinar_vencedor(jogada_jogador, jogada_computador) # <<< Quest-1 <<<<<<<<<<<<

        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor) # <<< Quest-1 <<<<<<<<<<<<
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)

        continuar = ler_jogar_novamente()
        if not continuar:
            break
    
    print(CFG_IDIOMA['mensagens']['agradecimento'])  # <<< Quest-1 <<<<<<<<<<<<

#---------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    jogar()
