# Importa o módulo 'random' para gerar jogadas aleatórias do computador
import random

# Função que define as regras do jogo: cada jogada vence de outra
def obter_regras() -> dict[str, str]:
    return {
        'pedra'   : 'tesoura',  # Pedra vence tesoura
        'tesoura' : 'papel',    # Tesoura vence papel
        'papel'   : 'pedra'     # Papel vence pedra
    }

# Função que gera uma jogada aleatória para o computador
def obter_jogada_computador() -> str:
    jogadas_validas = ['pedra', 'papel', 'tesoura']
    return random.choice(jogadas_validas)

# Função que determina o vencedor da rodada com base nas regras
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

# Função que exibe o placar atual formatado
def print_placar(placar_dct: dict[str, int]) -> None:
    print(f"Placar: Jogador {placar_dct['jogador']} | Computador {placar_dct['computador']} | Empates {placar_dct['empates']}")

# Função que pergunta ao jogador se deseja jogar novamente
def ler_jogar_novamente() -> bool:
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'

# Função principal que controla o fluxo do jogo
def jogar() -> None:
    regras_dct = obter_regras()  # Obtém as regras do jogo
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}  # Inicializa o placar
    historico = []  # Lista para armazenar o histórico de jogadas

    print("\n=== Jogo Pedra, Papel e Tesoura ===")

    while True:
        print("\n--------------------------")
        jogada_jogador = ler_jogada()  # Lê a jogada do jogador
        jogada_computador = obter_jogada_computador()  # Gera jogada do computador
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)  # Determina o vencedor

        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)  # Exibe o resultado
        placar_dct = atualizar_placar(placar_dct, vencedor)  # Atualiza o placar
        print_placar(placar_dct)  # Mostra o placar

        # Registra o resultado da rodada no histórico
        resultado_texto = {
            'jogador': 'Você venceu!',
            'computador': 'Você perdeu!',
            'empate': 'Empate!'
        }
        historico.append(f"{jogada_jogador.upper()} vs {jogada_computador.upper()}, >> {resultado_texto[vencedor]} <<")

        if not ler_jogar_novamente():  # Verifica se o jogador quer continuar
            break

    # Exibe o histórico completo de jogadas ao final do jogo
    print("\n=== Histórico de Jogadas ===")
    for registro in historico:
        print(registro)

    print("\nObrigado por jogar!")  # Mensagem de encerramento

# Executa o jogo se o script for rodado diretamente
if __name__ == '__main__':
    jogar()
