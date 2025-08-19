# Importa o módulo 'random' para gerar jogadas aleatórias do computador
import random

# Define as regras do jogo: cada jogada vence de outra
def obter_regras() -> dict[str, str]:
    return {
        'pedra'   : 'tesoura',  # Pedra vence tesoura
        'tesoura' : 'papel',    # Tesoura vence papel
        'papel'   : 'pedra'     # Papel vence pedra
    }

# Gera uma jogada aleatória para o computador
def obter_jogada_computador() -> str:
    jogadas_validas = ['pedra', 'papel', 'tesoura']
    return random.choice(jogadas_validas)

# Solicita a jogada de um jogador humano, exibindo seu nome
def ler_jogada_humana(nome: str) -> str:
    return input(f"{nome}, escolha sua arma: Pedra, Papel ou Tesoura? ").lower()

# Decide qual função usar para obter a jogada, dependendo do tipo de jogador
def obter_jogada(tipo: str, nome: str) -> str:
    if tipo == 'Humano':
        return ler_jogada_humana(nome)  # Jogador humano escolhe
    else:
        return obter_jogada_computador()  # Computador joga aleatoriamente

# Determina o vencedor da rodada com base nas regras
def determinar_vencedor(jogada1: str, jogada2: str, regras: dict[str, str]) -> str:
    if jogada1 == jogada2:
        return 'empate'  # Empate se as jogadas forem iguais
    if regras[jogada1] == jogada2:
        return 'jogador1'  # Jogador 1 vence
    return 'jogador2'  # Caso contrário, jogador 2 vence

# Atualiza o placar com base no resultado da rodada
def atualizar_placar(placar: dict[str, int], vencedor_rodada: str) -> dict[str, int]:
    if vencedor_rodada == 'jogador1':
        placar['jogador1'] += 1
    elif vencedor_rodada == 'jogador2':
        placar['jogador2'] += 1
    elif vencedor_rodada == 'empate':
        placar['empates'] += 1
    return placar

# Exibe o resultado da rodada com os nomes e jogadas dos jogadores
def exibir_resultado_rodada(jogada1: str, jogada2: str, nome1: str, nome2: str, vencedor: str) -> None:
    print(f"{nome1} escolheu: {jogada1.upper()} | {nome2} escolheu: {jogada2.upper()}")
    if vencedor == 'jogador1':
        print(f">> {nome1} venceu! <<")
    elif vencedor == 'jogador2':
        print(f">> {nome2} venceu! <<")
    else:
        print(">> Empate! <<")

# Exibe o placar atual com os nomes dos jogadores
def print_placar(placar: dict[str, int], nome1: str, nome2: str) -> None:
    print(f"Placar: {nome1} {placar['jogador1']} | {nome2} {placar['jogador2']} | Empates {placar['empates']}")

# Pergunta ao jogador se deseja jogar novamente
def ler_jogar_novamente() -> bool:
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'

# Configura os tipos de jogadores (Humano ou Computador) e define seus nomes
def configurar_jogadores() -> tuple[str, str, str, str]:
    print("=== Jogo Pedra, Papel e Tesoura ===")
    
    # Define tipo do jogador 1
    while True:
        tipo1 = input("Qual o tipo do Jogador-1: ").strip()
        if tipo1 in ['Humano', 'Computador']:
            break
        print("Tipo inválido. Use só 'Humano' ou 'Computador'.")
    
    # Define tipo do jogador 2
    while True:
        tipo2 = input("Qual o tipo do Jogador-2: ").strip()
        if tipo2 in ['Humano', 'Computador']:
            break
        print("Tipo inválido. Use só 'Humano' ou 'Computador'.")

    # Cria nomes personalizados com base no tipo
    nome1 = f"{tipo1}-1"
    nome2 = f"{tipo2}-2"
    return tipo1, tipo2, nome1, nome2

# Função principal que controla o fluxo do jogo
def jogar() -> None:
    regras_dct = obter_regras()  # Obtém as regras do jogo
    placar_dct = {"jogador1": 0, "jogador2": 0, "empates": 0}  # Inicializa o placar
    tipo1, tipo2, nome1, nome2 = configurar_jogadores()  # Configura os jogadores

    while True:
        print("\n--- Nova Rodada ---")
        
        # Obtém as jogadas dos dois jogadores
        jogada1 = obter_jogada(tipo1, nome1)
        jogada2 = obter_jogada(tipo2, nome2)

        # Determina o vencedor da rodada
        vencedor = determinar_vencedor(jogada1, jogada2, regras_dct)

        # Exibe o resultado e atualiza o placar
        exibir_resultado_rodada(jogada1, jogada2, nome1, nome2, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct, nome1, nome2)

        # Verifica se o jogador deseja continuar
        if not ler_jogar_novamente():
            break

    print("Obrigado por jogar!")  # Mensagem de encerramento

# Executa o jogo se o script for rodado diretamente
if __name__ == '__main__':
    jogar()
