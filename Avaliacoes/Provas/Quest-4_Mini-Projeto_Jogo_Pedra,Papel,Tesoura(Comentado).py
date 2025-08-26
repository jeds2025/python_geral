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

# Determina o vencedor da rodada com base nas regras e na jogada do jogador
def determinar_vencedor(jogada_jogador: str, jogada_computador: str, regras: dict[str, str]) -> str:
    if jogada_jogador == jogada_computador:
        return 'empate'  # Empate se as jogadas forem iguais
    if jogada_jogador == 'granada':
        return 'jogador'  # Granada sempre vence
    if regras[jogada_jogador] == jogada_computador:
        return 'jogador'  # Jogador vence pela regra tradicional
    return 'computador'  # Caso contrário, computador vence

# Atualiza o placar com base no resultado da rodada
def atualizar_placar(placar: dict[str, int], vencedor_rodada: str) -> dict[str, int]:
    if vencedor_rodada == 'jogador':
        placar['jogador'] += 1
    elif vencedor_rodada == 'computador':
        placar['computador'] += 1
    elif vencedor_rodada == 'empate':
        placar['empates'] += 1
    return placar

# Exibe o resultado da rodada com as jogadas e o vencedor
def exibir_resultado_rodada(jogada_jogador: str, jogada_computador: str, vencedor_rodada: str) -> None:
    print(f"Você escolheu: {jogada_jogador.upper()} | Computador escolheu: {jogada_computador.upper()}")
    if vencedor_rodada == 'jogador':
        print(">> Você venceu! <<")
    elif vencedor_rodada == 'empate':
        print(">> Empate! <<")
    else:  
        print(">> Você perdeu! <<")

# Solicita a jogada do jogador e valida a entrada, incluindo o código de trapaça
def ler_jogada(granada_liberada: bool) -> str:
    while True:
        jogada = input("Escolha sua arma: Pedra, Papel ou Tesoura? ").lower()
        
        # Ativa a trapaça se o jogador digitar o código secreto
        if jogada == 'codigo-de-trapaca':
            print("Trapaca ativada – A arma 'granada' foi liberada!")
            return 'codigo-de-trapaca'
        
        # Jogadas tradicionais válidas
        if jogada in ['pedra', 'papel', 'tesoura']:
            return jogada
        
        # Jogada especial 'granada' só é permitida se a trapaça estiver ativada
        if jogada == 'granada':
            if granada_liberada:
                return jogada
            else:
                print("A Arma 'granada' não disponível. O Código de trapaça não foi ativado.")
        else:
            print("Jogada inválida. Tente novamente.")

# Exibe o placar atual formatado
def print_placar(placar_dct: dict[str, int]) -> None:
    print(f"Placar: Jogador {placar_dct['jogador']} | Computador {placar_dct['computador']} | Empates {placar_dct['empates']}")

# Pergunta ao jogador se deseja jogar novamente
def ler_jogar_novamente() -> bool:
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'

# Função principal que controla o fluxo do jogo
def jogar() -> None:
    regras_dct = obter_regras()  # Obtém as regras do jogo
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}  # Inicializa o placar
    granada_liberada = False  # Estado da trapaça (desativada por padrão)

    while True:
        print("\n--- Jogo Pedra, Papel, Tesoura ---")

        jogada_jogador = ler_jogada(granada_liberada)

        # Se o jogador ativou a trapaça, libera a granada e solicita nova jogada
        if jogada_jogador == 'codigo-de-trapaca':
            granada_liberada = True
            jogada_jogador = ler_jogada(granada_liberada)

        jogada_computador = obter_jogada_computador()  # Gera jogada do computador
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)  # Determina o vencedor

        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)  # Exibe o resultado
        placar_dct = atualizar_placar(placar_dct, vencedor)  # Atualiza o placar
        print_placar(placar_dct)  # Mostra o placar

        if not ler_jogar_novamente():  # Pergunta se deseja continuar
            break

    print("Obrigado por jogar!")  # Mensagem de encerramento

# Executa o jogo se o script for rodado diretamente
if __name__ == '__main__':
    jogar()

