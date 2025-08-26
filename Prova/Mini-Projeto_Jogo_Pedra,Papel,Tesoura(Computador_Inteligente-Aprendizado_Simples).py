import random

historico_jogadas = []

def obter_regras() -> dict[str, str]:
    return {
        'pedra': 'tesoura',
        'tesoura': 'papel',
        'papel': 'pedra'
    }

def obter_jogada_computador() -> str:
    jogadas_validas = ['pedra', 'papel', 'tesoura']
    if not historico_jogadas:
        return random.choice(jogadas_validas)
    ultima_jogada = historico_jogadas[-1]
    for jogada in jogadas_validas:
        if obter_regras()[jogada] == ultima_jogada:
            return jogada
    return random.choice(jogadas_validas)

def determinar_vencedor(jogada_jogador: str, jogada_computador: str, regras: dict[str, str]) -> str:
    if jogada_jogador == jogada_computador:
        return 'empate'
    if regras[jogada_jogador] == jogada_computador:
        return 'jogador'
    return 'computador'

def atualizar_placar(placar: dict[str, int], vencedor_rodada: str) -> dict[str, int]:
    placar[vencedor_rodada] += 1
    return placar

def exibir_resultado_rodada(jogada_jogador: str, jogada_computador: str, vencedor_rodada: str) -> None:
    print(f"Você escolheu: {jogada_jogador.upper()} | Computador escolheu: {jogada_computador.upper()}")
    print(f">> Resultado: {vencedor_rodada.upper()} <<")

def ler_jogada() -> str:
    jogada = input("Escolha sua arma: Pedra, Papel ou Tesoura? ").lower()
    historico_jogadas.append(jogada)
    return jogada

def print_placar(placar_dct: dict[str, int]) -> None:
    print(f"Placar: Jogador {placar_dct['jogador']} | Computador {placar_dct['computador']} | Empates {placar_dct['empate']}")

def ler_jogar_novamente() -> bool:
    return input("Jogar novamente? (s/n): ").lower() == 's'

def jogar() -> None:
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empate": 0}
    while True:
        print("\n--- Jogo Inteligente ---")
        jogada_jogador = ler_jogada()
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