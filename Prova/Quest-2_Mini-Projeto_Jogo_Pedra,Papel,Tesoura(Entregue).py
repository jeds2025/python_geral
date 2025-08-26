import random

def obter_regras() -> dict[str, str]:
    return {
        'pedra'   : 'tesoura',
        'tesoura' : 'papel',
        'papel'   : 'pedra'
    }

# O Computador escolhe a jogada com base na dificuldade escolhida
def obter_jogada_computador(jogada_jogador: str, dificuldade: str, regras: dict[str, str]) -> str:
    jogadas_validas = ['pedra', 'papel', 'tesoura']

    if dificuldade == 'normal':
        return random.choice(jogadas_validas)
    elif dificuldade == 'facil':
# O Computador escolhe sempre a jogada que perde para a jogada do jogador
        return regras[jogada_jogador]
    elif dificuldade == 'dificil':
# O Computador escolhe sempre a jogada que vence a jogada do jogador
        for jogada in jogadas_validas:
            if regras[jogada] == jogada_jogador:
                return jogada

# Se não for escolhida a dificuldade será sempre normal
    return random.choice(jogadas_validas)

def determinar_vencedor(jogada_jogador: str, jogada_computador: str, regras: dict[str, str]) -> str:
    if jogada_jogador == jogada_computador:
        return 'empate'
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

def ler_jogada() -> str:
    return input("Escolha sua arma: Pedra, Papel ou Tesoura? ").lower()

def print_placar(placar_dct: dict[str, int]) -> None:
    print(f"Placar: Jogador {placar_dct['jogador']} | Computador {placar_dct['computador']} | Empates {placar_dct['empates']}")

def ler_jogar_novamente() -> bool:
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'

# Vai ler a dificuldade escolhida para o Computador
def ler_dificuldade() -> str:
    while True:
        dificuldade = input("Escolha o nível de dificuldade (facil / normal / dificil): ").lower()
        if dificuldade in ['facil', 'normal', 'dificil']:
            return dificuldade
        print("Entrada inválida. Tente novamente.")

def jogar() -> None:
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}

    print("\n=== Jogo Pedra, Papel e Tesoura ===")
    dificuldade = ler_dificuldade()

    while True:
        print("\n--- Nova Rodada ---")

        jogada_jogador = ler_jogada()
        jogada_computador = obter_jogada_computador(jogada_jogador, dificuldade, regras_dct)

        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)

        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)

        if not ler_jogar_novamente():
            break
    print("Obrigado por jogar!")

if __name__ == '__main__':
    jogar()
