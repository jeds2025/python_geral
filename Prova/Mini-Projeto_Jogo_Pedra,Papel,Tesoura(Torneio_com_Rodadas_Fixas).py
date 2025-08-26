import random

def obter_regras() -> dict[str, str]:
    return {
        'pedra': 'tesoura',
        'tesoura': 'papel',
        'papel': 'pedra'
    }

def obter_jogada_computador() -> str:
    return random.choice(['pedra', 'papel', 'tesoura'])

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
    print(f"{jogada_jogador.upper()} vs {jogada_computador.upper()} => {vencedor_rodada.upper()}")

def ler_jogada() -> str:
    return input("Escolha sua arma: Pedra, Papel ou Tesoura? ").lower()

def print_placar(placar_dct: dict[str, int]) -> None:
    print(f"Placar: Jogador {placar_dct['jogador']} | Computador {placar_dct['computador']} | Empates {placar_dct['empate']}")

def jogar() -> None:
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empate": 0}
    rodadas = int(input("Quantas rodadas deseja jogar? "))
    for _ in range(rodadas):
        print("\n--- Rodada ---")
        jogada_jogador = ler_jogada()
        jogada_computador = obter_jogada_computador()
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)
        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)
    
        print("\n=== Resultado Final ===")
    if placar_dct['jogador'] > placar_dct['computador']:
        print(">> Você venceu o torneio! <<")
    elif placar_dct['jogador'] < placar_dct['computador']:
        print(">> O computador venceu o torneio! <<")
    else:
        print(">> O torneio terminou empatado! <<")
    print("Obrigado por jogar!")

if __name__ == '__main__':
    jogar()