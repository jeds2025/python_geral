import random

def obter_regras() -> dict[str, str]:
    return {
        'pedra'   : 'tesoura',
        'tesoura' : 'papel',
        'papel'   : 'pedra'
    }

def obter_jogada_computador() -> str:
    jogadas_validas = ['pedra', 'papel', 'tesoura']
    return random.choice(jogadas_validas)

def determinar_vencedor(jogada_jogador: str, jogada_computador: str, regras: dict[str, str]) -> str:
    if jogada_jogador == jogada_computador:
        return 'empate'
    if jogada_jogador == 'granada':
        return 'jogador'
    if regras[jogada_jogador] == jogada_computador:
        return 'jogador'
    return 'computador'

def atualizar_placar(placar: dict[str, int], vencedor_rodada: str) -> dict[str, int]:
    if vencedor_rodada == 'jogador':
        placar['jogador'] += 1
    elif vencedor_rodada == 'computador':
        placar['computador'] += 1
    elif vencedor_rodada == 'empate':
        placar['empates'] += 1
    return placar

def exibir_resultado_rodada(jogada_jogador: str, jogada_computador: str, vencedor_rodada: str) -> None:
    print(f"Você escolheu: {jogada_jogador.upper()} | Computador escolheu: {jogada_computador.upper()}")
    if vencedor_rodada == 'jogador':
        print(">> Você venceu! <<")
    elif vencedor_rodada == 'empate':
        print(">> Empate! <<")
    else:  
        print(">> Você perdeu! <<")

# Verifica a jogada do jogador, com trapaca para liberar a 'granada'
def ler_jogada(granada_liberada: bool) -> str:
    while True:
        jogada = input("Escolha sua arma: Pedra, Papel ou Tesoura? ").lower()
        if jogada == 'codigo-de-trapaca':
            print("Trapaca ativada – A arma 'granada' foi liberada!")
            return 'codigo-de-trapaca'
        if jogada in ['pedra', 'papel', 'tesoura']:
            return jogada
        if jogada == 'granada':
            if granada_liberada:
                return jogada
            else:
                print("A Arma 'granada' não disponível. O Código de trapaça não foi ativado.")
        else:
            print("Jogada inválida. Tente novamente.")

def print_placar(placar_dct: dict[str, int]) -> None:
    print(f"Placar: Jogador {placar_dct['jogador']} | Computador {placar_dct['computador']} | Empates {placar_dct['empates']}")

def ler_jogar_novamente() -> bool:
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'

def jogar() -> None:
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}
    granada_liberada = False

    while True:
        print("\n--- Jogo Pedra, Papel, Tesoura ---")

        jogada_jogador = ler_jogada(granada_liberada)
        # Se o jogador escolheu 'codigo-de-trapaca', a granada é ativada com 'True'
        if jogada_jogador == 'codigo-de-trapaca':
            granada_liberada = True
            jogada_jogador = ler_jogada(granada_liberada)

        jogada_computador = obter_jogada_computador()

        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)

        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)

        if not ler_jogar_novamente():
            break
    print("Obrigado por jogar!")

if __name__ == '__main__':
    jogar()

