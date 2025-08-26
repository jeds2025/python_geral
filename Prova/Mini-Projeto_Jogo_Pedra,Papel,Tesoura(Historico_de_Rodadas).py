<<<<<<< Updated upstream
import random

historico = []

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
    print(f"Você escolheu: {jogada_jogador.upper()} | Computador escolheu: {jogada_computador.upper()}")
    if vencedor_rodada == 'jogador':
        print(">> Você venceu! <<")
    elif vencedor_rodada == 'empate':
        print(">> Empate! <<")
    else:
        print(">> Você perdeu! <<")
    historico.append(f"{jogada_jogador} vs {jogada_computador} => {vencedor_rodada}")

def ler_jogada() -> str:
    return input("Escolha sua arma: Pedra, Papel ou Tesoura? ").lower()

def print_placar(placar_dct: dict[str, int]) -> None:
    print(f"Placar: Jogador {placar_dct['jogador']} | Computador {placar_dct['computador']} | Empates {placar_dct['empate']}")

def ler_jogar_novamente() -> bool:
    return input("Jogar novamente? (s/n): ").lower() == 's'

def jogar() -> None:
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empate": 0}
    while True:
        print("\n--- Jogo com Histórico ---")
        jogada_jogador = ler_jogada()
        jogada_computador = obter_jogada_computador()
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)
        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)
        if not ler_jogar_novamente():
            break
    print("\n=== Histórico de Rodadas ===")
    for linha in historico:
        print(linha)
    print("Obrigado por jogar!")

if __name__ == '__main__':
=======
import random

historico = []

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
    print(f"Você escolheu: {jogada_jogador.upper()} | Computador escolheu: {jogada_computador.upper()}")
    if vencedor_rodada == 'jogador':
        print(">> Você venceu! <<")
    elif vencedor_rodada == 'empate':
        print(">> Empate! <<")
    else:
        print(">> Você perdeu! <<")
    historico.append(f"{jogada_jogador} vs {jogada_computador} => {vencedor_rodada}")

def ler_jogada() -> str:
    return input("Escolha sua arma: Pedra, Papel ou Tesoura? ").lower()

def print_placar(placar_dct: dict[str, int]) -> None:
    print(f"Placar: Jogador {placar_dct['jogador']} | Computador {placar_dct['computador']} | Empates {placar_dct['empate']}")

def ler_jogar_novamente() -> bool:
    return input("Jogar novamente? (s/n): ").lower() == 's'

def jogar() -> None:
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empate": 0}
    while True:
        print("\n--- Jogo com Histórico ---")
        jogada_jogador = ler_jogada()
        jogada_computador = obter_jogada_computador()
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)
        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)
        if not ler_jogar_novamente():
            break
    print("\n=== Histórico de Rodadas ===")
    for linha in historico:
        print(linha)
    print("Obrigado por jogar!")

if __name__ == '__main__':
>>>>>>> Stashed changes
    jogar()