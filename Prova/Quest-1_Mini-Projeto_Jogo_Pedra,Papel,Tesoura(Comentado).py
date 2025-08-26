<<<<<<< HEAD
# Importa o módulo 'random' para gerar jogadas aleatórias do computador
import random

# Dicionário de configuração internacionalizado com suporte a múltiplos idiomas
CFG = {
    # Configuração para Português do Brasil
    'pt-br': {
        'jogadas_validas': ['pedra', 'papel', 'tesoura'],  # Jogadas permitidas
        'regras': {  # Regras de vitória
            'pedra': 'tesoura',
            'papel': 'pedra',
            'tesoura': 'papel',
        },
        'mensagens': {  # Mensagens exibidas ao jogador
            'titulo': '--- Jogo Pedra, Papel, Tesoura ---',
            'solicitar_jogada': 'Escolha sua arma: Pedra, Papel ou Tesoura? ',
            'vitoria': '>> Você venceu! <<',
            'derrota': '>> Você perdeu! <<',
            'empate': '>> Empate! <<',
            'invalida': 'Jogada inválida! Por favor, escolha entre: Pedra, Papel ou Tesoura.',
            'placar': 'Placar: Jogador {} | Computador {} | Empates {}',
            'jogar_novamente': 'Jogar novamente? (s/n): ',
            'agradecimento': 'Obrigado por jogar!'
        }
    },
    # Configuração para Inglês
    'en-us': {
        'jogadas_validas': ['rock', 'paper', 'scissors'],
        'regras': {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper',
        },
        'mensagens': {
            'titulo': '--- Rock, Paper, Scissors Game ---',
            'solicitar_jogada': 'Choose your weapon: Rock, Paper, or Scissors? ',
            'vitoria': '>> You won! <<',
            'derrota': '>> You lost! <<',
            'empate': '>> Draw! <<',
            'invalida': 'Invalid move! Please choose between: Rock, Paper, or Scissors.',
            'placar': 'Score: Player {} | Computer {} | Draws {}',
            'jogar_novamente': 'Play again? (y/n): ',
            'agradecimento': 'Thanks for playing!'
        }
    },
    # Configuração para Coreano
    'ko': {
        'jogadas_validas': ['바위', '보', '가위'],
        'regras': {
            '바위': '가위',
            '보': '바위',
            '가위': '보',
        },
        'mensagens': {
            'titulo': '--- 가위 바위 보 게임 ---',
            'solicitar_jogada': '무기를 선택하세요: 바위, 보, 가위? ',
            'vitoria': '>> 당신이 이겼습니다! <<',
            'derrota': '>> 당신이 졌습니다! <<',
            'empate': '>> 무승부! <<',
            'invalida': '잘못된 선택입니다! 바위, 보, 가위 중에서 선택하세요.',
            'placar': '점수: 플레이어 {} | 컴퓨터 {} | 무승부 {}',
            'jogar_novamente': '다시 하시겠습니까? (s/n): ',
            'agradecimento': '게임해 주셔서 감사합니다!'
        }
    }
}

# Solicita ao jogador que escolha o idioma
print("Selecione o idioma: 'pt-br', 'en-us', 'ko'")
IDIOMA = input("Informe o idioma no qual você deseja Jogar: ").strip().lower()  # Normaliza a entrada

# Verifica se o idioma escolhido está disponível; se não, define 'pt-br' como padrão
if IDIOMA not in CFG:
    print("Idioma não suportado. Usando 'pt-br' como padrão.")
    IDIOMA = 'pt-br'

# Função que retorna as regras de vitória conforme o idioma
def obter_regras() -> dict[str, str]:
    return CFG[IDIOMA]['regras']

# Função que escolhe aleatoriamente uma jogada válida para o computador
def obter_jogada_computador() -> str:
    return random.choice(CFG[IDIOMA]['jogadas_validas'])

# Função que determina o vencedor da rodada com base nas regras
def determinar_vencedor(jogada_jogador: str, jogada_computador: str, regras: dict[str, str]) -> str:
    if jogada_jogador == jogada_computador:
        return 'empates'  # Corrigido para bater com a chave do placar
    return 'jogador' if regras[jogada_jogador] == jogada_computador else 'computador'

# Função que atualiza o placar com base no resultado da rodada
def atualizar_placar(placar: dict[str, int], vencedor: str) -> dict[str, int]:
    placar[vencedor] += 1  # Incrementa o contador correspondente
    return placar

# Função que exibe o resultado da rodada com mensagens personalizadas
def exibir_resultado_rodada(jogada_jogador: str, jogada_computador: str, vencedor: str) -> None:
    print(f"{CFG[IDIOMA]['mensagens']['titulo']}")  # Exibe o título do jogo
    print(f"Você escolheu: {jogada_jogador} | Computador: {jogada_computador}")  # Mostra as jogadas
    print(CFG[IDIOMA]['mensagens'][{'jogador': 'vitoria', 'computador': 'derrota', 'empates': 'empate'}[vencedor]])  # Mensagem do resultado

# Função que solicita a jogada do jogador e valida a entrada
def ler_jogada() -> str:
    while True:
        jogada = input(CFG[IDIOMA]['mensagens']['solicitar_jogada']).strip().lower()  # Lê e normaliza
        if jogada in CFG[IDIOMA]['jogadas_validas']:  # Verifica validade
            return jogada
        print(CFG[IDIOMA]['mensagens']['invalida'])  # Mensagem de erro

# Função que exibe o placar atual formatado conforme o idioma
def exibir_placar(placar: dict[str, int]) -> None:
    print(CFG[IDIOMA]['mensagens']['placar'].format(
        placar['jogador'], placar['computador'], placar['empates']
    ))

# Função que pergunta ao jogador se deseja jogar novamente
def perguntar_novamente() -> bool:
    return input(CFG[IDIOMA]['mensagens']['jogar_novamente']).lower() in {'s', 'y', 'sim', 'yes'}

# Função principal que controla o fluxo do jogo
def jogar() -> None:
    placar = {'jogador': 0, 'computador': 0, 'empates': 0}  # Inicializa o placar
    regras = obter_regras()  # Obtém as regras do idioma

    while True:
        jogada_jogador = ler_jogada()  # Jogada do jogador
        jogada_computador = obter_jogada_computador()  # Jogada do computador
        resultado = determinar_vencedor(jogada_jogador, jogada_computador, regras)  # Resultado da rodada

        placar = atualizar_placar(placar, resultado)  # Atualiza placar
        exibir_resultado_rodada(jogada_jogador, jogada_computador, resultado)  # Exibe resultado
        exibir_placar(placar)  # Mostra placar

        if not perguntar_novamente():  # Verifica se continua
            print(CFG[IDIOMA]['mensagens']['agradecimento'])  # Mensagem final
            break  # Encerra o jogo

# Executa o jogo se o script for rodado diretamente
if __name__ == '__main__':
    jogar()  # Inicia o jogo
=======
# Importa o módulo 'random' para gerar jogadas aleatórias do computador
import random

# Dicionário de configuração internacionalizado com suporte a múltiplos idiomas
CFG = {
    # Configuração para Português do Brasil
    'pt-br': {
        'jogadas_validas': ['pedra', 'papel', 'tesoura'],  # Jogadas permitidas
        'regras': {  # Regras de vitória
            'pedra': 'tesoura',
            'papel': 'pedra',
            'tesoura': 'papel',
        },
        'mensagens': {  # Mensagens exibidas ao jogador
            'titulo': '--- Jogo Pedra, Papel, Tesoura ---',
            'solicitar_jogada': 'Escolha sua arma: Pedra, Papel ou Tesoura? ',
            'vitoria': '>> Você venceu! <<',
            'derrota': '>> Você perdeu! <<',
            'empate': '>> Empate! <<',
            'invalida': 'Jogada inválida! Por favor, escolha entre: Pedra, Papel ou Tesoura.',
            'placar': 'Placar: Jogador {} | Computador {} | Empates {}',
            'jogar_novamente': 'Jogar novamente? (s/n): ',
            'agradecimento': 'Obrigado por jogar!'
        }
    },
    # Configuração para Inglês
    'en-us': {
        'jogadas_validas': ['rock', 'paper', 'scissors'],
        'regras': {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper',
        },
        'mensagens': {
            'titulo': '--- Rock, Paper, Scissors Game ---',
            'solicitar_jogada': 'Choose your weapon: Rock, Paper, or Scissors? ',
            'vitoria': '>> You won! <<',
            'derrota': '>> You lost! <<',
            'empate': '>> Draw! <<',
            'invalida': 'Invalid move! Please choose between: Rock, Paper, or Scissors.',
            'placar': 'Score: Player {} | Computer {} | Draws {}',
            'jogar_novamente': 'Play again? (y/n): ',
            'agradecimento': 'Thanks for playing!'
        }
    },
    # Configuração para Coreano
    'ko': {
        'jogadas_validas': ['바위', '보', '가위'],
        'regras': {
            '바위': '가위',
            '보': '바위',
            '가위': '보',
        },
        'mensagens': {
            'titulo': '--- 가위 바위 보 게임 ---',
            'solicitar_jogada': '무기를 선택하세요: 바위, 보, 가위? ',
            'vitoria': '>> 당신이 이겼습니다! <<',
            'derrota': '>> 당신이 졌습니다! <<',
            'empate': '>> 무승부! <<',
            'invalida': '잘못된 선택입니다! 바위, 보, 가위 중에서 선택하세요.',
            'placar': '점수: 플레이어 {} | 컴퓨터 {} | 무승부 {}',
            'jogar_novamente': '다시 하시겠습니까? (s/n): ',
            'agradecimento': '게임해 주셔서 감사합니다!'
        }
    }
}

# Solicita ao jogador que escolha o idioma
print("Selecione o idioma: 'pt-br', 'en-us', 'ko'")
IDIOMA = input("Informe o idioma no qual você deseja Jogar: ").strip().lower()  # Normaliza a entrada

# Verifica se o idioma escolhido está disponível; se não, define 'pt-br' como padrão
if IDIOMA not in CFG:
    print("Idioma não suportado. Usando 'pt-br' como padrão.")
    IDIOMA = 'pt-br'

# Função que retorna as regras de vitória conforme o idioma
def obter_regras() -> dict[str, str]:
    return CFG[IDIOMA]['regras']

# Função que escolhe aleatoriamente uma jogada válida para o computador
def obter_jogada_computador() -> str:
    return random.choice(CFG[IDIOMA]['jogadas_validas'])

# Função que determina o vencedor da rodada com base nas regras
def determinar_vencedor(jogada_jogador: str, jogada_computador: str, regras: dict[str, str]) -> str:
    if jogada_jogador == jogada_computador:
        return 'empates'  # Corrigido para bater com a chave do placar
    return 'jogador' if regras[jogada_jogador] == jogada_computador else 'computador'

# Função que atualiza o placar com base no resultado da rodada
def atualizar_placar(placar: dict[str, int], vencedor: str) -> dict[str, int]:
    placar[vencedor] += 1  # Incrementa o contador correspondente
    return placar

# Função que exibe o resultado da rodada com mensagens personalizadas
def exibir_resultado_rodada(jogada_jogador: str, jogada_computador: str, vencedor: str) -> None:
    print(f"{CFG[IDIOMA]['mensagens']['titulo']}")  # Exibe o título do jogo
    print(f"Você escolheu: {jogada_jogador} | Computador: {jogada_computador}")  # Mostra as jogadas
    print(CFG[IDIOMA]['mensagens'][{'jogador': 'vitoria', 'computador': 'derrota', 'empates': 'empate'}[vencedor]])  # Mensagem do resultado

# Função que solicita a jogada do jogador e valida a entrada
def ler_jogada() -> str:
    while True:
        jogada = input(CFG[IDIOMA]['mensagens']['solicitar_jogada']).strip().lower()  # Lê e normaliza
        if jogada in CFG[IDIOMA]['jogadas_validas']:  # Verifica validade
            return jogada
        print(CFG[IDIOMA]['mensagens']['invalida'])  # Mensagem de erro

# Função que exibe o placar atual formatado conforme o idioma
def exibir_placar(placar: dict[str, int]) -> None:
    print(CFG[IDIOMA]['mensagens']['placar'].format(
        placar['jogador'], placar['computador'], placar['empates']
    ))

# Função que pergunta ao jogador se deseja jogar novamente
def perguntar_novamente() -> bool:
    return input(CFG[IDIOMA]['mensagens']['jogar_novamente']).lower() in {'s', 'y', 'sim', 'yes'}

# Função principal que controla o fluxo do jogo
def jogar() -> None:
    placar = {'jogador': 0, 'computador': 0, 'empates': 0}  # Inicializa o placar
    regras = obter_regras()  # Obtém as regras do idioma

    while True:
        jogada_jogador = ler_jogada()  # Jogada do jogador
        jogada_computador = obter_jogada_computador()  # Jogada do computador
        resultado = determinar_vencedor(jogada_jogador, jogada_computador, regras)  # Resultado da rodada

        placar = atualizar_placar(placar, resultado)  # Atualiza placar
        exibir_resultado_rodada(jogada_jogador, jogada_computador, resultado)  # Exibe resultado
        exibir_placar(placar)  # Mostra placar

        if not perguntar_novamente():  # Verifica se continua
            print(CFG[IDIOMA]['mensagens']['agradecimento'])  # Mensagem final
            break  # Encerra o jogo

# Executa o jogo se o script for rodado diretamente
if __name__ == '__main__':
    jogar()  # Inicia o jogo
>>>>>>> f4e720c179cb9d63c4b9f288ed2e438a0e75cf64
