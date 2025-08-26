# Importa o módulo 'random' para gerar jogadas aleatórias
import random

# Função que define as regras do jogo: cada jogada vence de outra
def obter_regras() -> dict[str, str]:
    return {
        'pedra'   : 'tesoura',  # Pedra vence tesoura
        'tesoura' : 'papel',    # Tesoura vence papel
        'papel'   : 'pedra'     # Papel vence pedra
    }

# Função que determina a jogada do computador com base na dificuldade escolhida
def obter_jogada_computador(jogada_jogador: str, dificuldade: str, regras: dict[str, str]) -> str:
    jogadas_validas = ['pedra', 'papel', 'tesoura']

    if dificuldade == 'normal':
        # Escolhe aleatoriamente uma jogada
        return random.choice(jogadas_validas)
    elif dificuldade == 'facil':
        # Escolhe a jogada que perde para a jogada do jogador (jogador sempre vence)
        return regras[jogada_jogador]
    elif dificuldade == 'dificil':
        # Escolhe a jogada que vence a jogada do jogador (computador sempre vence)
        for jogada in jogadas_validas:
            if regras[jogada] == jogada_jogador:
                return jogada

    # Se a dificuldade for inválida, joga aleatoriamente
    return random.choice(jogadas_validas)

# Função que determina o vencedor da rodada
def determinar_vencedor(jogada_jogador: str, jogada_computador: str, regras: dict[str, str]) -> str:
    if jogada_jogador == jogada_computador:
        return 'empate'  # Empate se as jogadas forem iguais
    if regras[jogada_jogador] == jogada_computador:
        return 'jogador'  # Jogador vence
    return 'computador'  # Computador vence

# Função que atualiza o placar com base no resultado da rodada
def atualizar_placar(placar: dict[str, int], vencedor_rodada: str) -> dict[str, int]:
    if vencedor_rodada == 'jogador':
        placar['jogador'] += 1
    elif vencedor_rodada == 'computador':
        placar['computador'] += 1
    elif vencedor_rodada == 'empate':
        placar['empates'] += 1
    return placar

# Função que exibe o resultado da rodada
def exibir_resultado_rodada(jogada_jogador: str, jogada_computador: str, vencedor_rodada: str) -> None:
    print(f"Você escolheu: {jogada_jogador.upper()} | Computador escolheu: {jogada_computador.upper()}")
    if vencedor_rodada == 'jogador':
        print(">> Você venceu! <<")
    elif vencedor_rodada == 'empate':
        print(">> Empate! <<")
    else:  
        print(">> Você perdeu! <<")

# Função que solicita a jogada do jogador e valida a entrada
def ler_jogada() -> str:
    jogadas_validas = ['pedra', 'papel', 'tesoura']
    while True:
        jogada = input("Escolha sua arma: Pedra, Papel ou Tesoura? ").lower()
        if jogada in jogadas_validas:
            return jogada
        print("Jogada inválida. Tente novamente.")

# Função que exibe o placar atual
def print_placar(placar_dct: dict[str, int]) -> None:
    print(f"Placar: Jogador {placar_dct['jogador']} | Computador {placar_dct['computador']} | Empates {placar_dct['empates']}")

# Função que pergunta se o jogador deseja jogar novamente
def ler_jogar_novamente() -> bool:
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'

# Função que solicita e valida a dificuldade escolhida pelo jogador
def ler_dificuldade() -> str:
    while True:
        dificuldade = input("Escolha o nível de dificuldade (facil / normal / dificil): ").lower()
        if dificuldade in ['facil', 'normal', 'dificil']:
            return dificuldade
        print("Entrada inválida. Tente novamente.")

# Função principal que controla o fluxo do jogo
def jogar() -> None:
    regras_dct = obter_regras()  # Obtém as regras do jogo
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}  # Inicializa o placar

    print("\n=== Jogo Pedra, Papel e Tesoura ===")
    dificuldade = ler_dificuldade()  # Lê a dificuldade escolhida

    while True:
        print("\n--- Nova Rodada ---")

        jogada_jogador = ler_jogada()  # Lê a jogada do jogador
        jogada_computador = obter_jogada_computador(jogada_jogador, dificuldade, regras_dct)  # Gera jogada do computador

        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)  # Determina o vencedor

        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)  # Exibe o resultado
        placar_dct = atualizar_placar(placar_dct, vencedor)  # Atualiza o placar
        print_placar(placar_dct)  # Exibe o placar

        if not ler_jogar_novamente():  # Pergunta se deseja continuar
            break

    print("Obrigado por jogar!")  # Mensagem final

# Executa o jogo se o script for rodado diretamente
if __name__ == '__main__':
    jogar()
