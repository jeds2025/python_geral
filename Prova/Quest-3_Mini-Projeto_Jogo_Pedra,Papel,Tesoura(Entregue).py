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

def jogar() -> None:
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}
    historico = []

    print("\n=== Jogo Pedra, Papel e Tesoura ===")

    while True:
        print("\n--------------------------")
        jogada_jogador = ler_jogada()
        jogada_computador = obter_jogada_computador()
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)

        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)

        # A cada Jogada o resultado é registrado no histórico
        resultado_texto = {
            'jogador': 'Você venceu!',
            'computador': 'Você perdeu!',
            'empate': 'Empate!'
        }
        historico.append(f"{jogada_jogador.upper()} vs {jogada_computador.upper()}, >> {resultado_texto[vencedor]} <<")

        if not ler_jogar_novamente():
            break

    print("\n=== Histórico de Jogadas ===")
    for registro in historico:
        print(registro)

    print("\nObrigado por jogar!")

if __name__ == '__main__':
    jogar()

