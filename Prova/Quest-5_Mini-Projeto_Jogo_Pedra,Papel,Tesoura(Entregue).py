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

def ler_jogada_humana(nome: str) -> str:
    return input(f"{nome}, escolha sua arma: Pedra, Papel ou Tesoura? ").lower()

# Faz a decisão da jogada como Humano ou Computador
def obter_jogada(tipo: str, nome: str) -> str:
    if tipo == 'Humano':
        return ler_jogada_humana(nome)
    else:
        return obter_jogada_computador()

def determinar_vencedor(jogada1: str, jogada2: str, regras: dict[str, str]) -> str:
    if jogada1 == jogada2:
        return 'empate'
    if regras[jogada1] == jogada2:
        return 'jogador1'
    return 'jogador2'

def atualizar_placar(placar: dict[str, int], vencedor_rodada: str) -> dict[str, int]:
    if vencedor_rodada == 'jogador1':
        placar['jogador1'] += 1
    elif vencedor_rodada == 'jogador2':
        placar['jogador2'] += 1
    elif vencedor_rodada == 'empate':
        placar['empates'] += 1
    return placar

def exibir_resultado_rodada(jogada1: str, jogada2: str, nome1: str, nome2: str, vencedor: str) -> None:
    print(f"{nome1} escolheu: {jogada1.upper()} | {nome2} escolheu: {jogada2.upper()}")
    if vencedor == 'jogador1':
        print(f">> {nome1} venceu! <<")
    elif vencedor == 'jogador2':
        print(f">> {nome2} venceu! <<")
    else:
        print(">> Empate! <<")

def print_placar(placar: dict[str, int], nome1: str, nome2: str) -> None:
    print(f"Placar: {nome1} {placar['jogador1']} | {nome2} {placar['jogador2']} | Empates {placar['empates']}")

def ler_jogar_novamente() -> bool:
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'

 # Tipos de jogadores
def configurar_jogadores() -> tuple[str, str, str, str]:
    print("=== Jogo Pedra, Papel e Tesoura ===")
    while True:
        tipo1 = input("Qual o tipo do Jogador-1: ").strip()
        if tipo1 in ['Humano', 'Computador']:
            break
        print("Tipo inválido. Use só 'Humano' ou 'Computador'.")
    while True:
        tipo2 = input("Qual o tipo do Jogador-2: ").strip()
        if tipo2 in ['Humano', 'Computador']:
            break
        print("Tipo inválido. Use só 'Humano' ou 'Computador'.")

    nome1 = f"{tipo1}-1"
    nome2 = f"{tipo2}-2"
    return tipo1, tipo2, nome1, nome2

def jogar() -> None:
    regras_dct = obter_regras()
    placar_dct = {"jogador1": 0, "jogador2": 0, "empates": 0}
    tipo1, tipo2, nome1, nome2 = configurar_jogadores()

    while True:
        print("\n--- Nova Rodada ---")
        jogada1 = obter_jogada(tipo1, nome1)
        jogada2 = obter_jogada(tipo2, nome2)

        vencedor = determinar_vencedor(jogada1, jogada2, regras_dct)

        exibir_resultado_rodada(jogada1, jogada2, nome1, nome2, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct, nome1, nome2)

        if not ler_jogar_novamente():
            break
    print("Obrigado por jogar!")

if __name__ == '__main__':
    jogar()
