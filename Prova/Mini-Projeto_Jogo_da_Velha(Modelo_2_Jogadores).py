import random

#---------------------------------------------------------------------------------------------------

def obter_regras() -> dict[str, str]:
    """ Retorna um dicionário que representa as regras do jogo Pedra, Papel e Tesoura. """
    result = {
        'pedra'   : 'tesoura',
        'tesoura' : 'papel',
        'papel'   : 'pedra'
    }
    return result

#---------------------------------------------------------------------------------------------------

def determinar_vencedor(jogada_a: str, jogada_b: str, regras: dict[str, str]) -> str: # <<< Quest-5 <<<<<<<<<<<<
   
    if jogada_a == jogada_b: # <<< Quest-5 <<<<<<<<<<<<
        return 'empate'
    if regras[jogada_a] == jogada_b: # <<< Quest-5 <<<<<<<<<<<<
        return 'jogador_a' # <<< Quest-5 <<<<<<<<<<<<
    return 'jogador_b' # <<< Quest-5 <<<<<<<<<<<<


def atualizar_placar(placar: dict[str, int], vencedor_rodada: str) -> dict[str, int]: # <<< Quest-5 <<<<<<<<<<<<
   
    match vencedor_rodada:
        case 'jogador_a':
            placar['jogador_a'] += 1 # <<< Quest-5 <<<<<<<<<<<<
        case 'jogador_b':
            placar['jogador_b'] += 1 # <<< Quest-5 <<<<<<<<<<<<
        case 'empate':
            placar['empate'] += 1
    return placar

def exibir_resultado_rodada(jogada_a: str, jogada_b: str, vencedor_rodada: str) -> None: # <<< Quest-5 <<<<<<<<<<<<

    print(f"Jogador-A escolheu: {jogada_a.upper()} | Jogador-B escolheu: {jogada_b.upper()}") # <<< Quest-5 <<<<<<<<<<<<
    match vencedor_rodada:
        case 'jogador_a': # <<< Quest-5 <<<<<<<<<<<<
            print(">> Jogador-A venceu! <<") # <<< Quest-5 <<<<<<<<<<<<
        case 'empate':
            print(">> Empate! <<")
        case _: #
            print(">> Jogador-B venceu! <<") # <<< Quest-5 <<<<<<<<<<<<


def ler_jogada(nome_jogador: str) -> str: # <<< Quest-5 <<<<<<<<<<<<

    prompt = f"Escolha sua arma, {nome_jogador}: Pedra, Papel ou Tesoura? " # <<< Quest-5 <<<<<<<<<<<<
    return input(prompt).lower() # <<< Quest-5 <<<<<<<<<<<<


def print_placar(placar_dct: dict[str, int]) -> None: # <<< Quest-5 <<<<<<<<<<<<

    print(f"Placar: Jogador-A {placar_dct['jogador_a']} | Jogador-B {placar_dct['jogador_b']} | Empates {placar_dct['empate']}") # <<< Quest-5 <<<<<<<<<<<<


def ler_jogar_novamente() -> bool:
    """ Pergunta ao usuário se deseja jogar novamente e retorna True para 's', False caso contrário. """
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'

#---------------------------------------------------------------------------------------------------


def jogar() -> None: # <<< Quest-5 <<<<<<<<<<<<

    regras_dct = obter_regras()
    placar_dct = {"jogador_a": 0, "jogador_b": 0, "empate": 0} # <<< Quest-5 <<<<<<<<<<<<

    while True:
        print("\n--- Jogo Pedra, Papel, Tesoura ---")

        jogada_jogador_a = ler_jogada("Jogador-A") # <<< Quest-5 <<<<<<<<<<<<
        jogada_jogador_b = ler_jogada("Jogador-B") # <<< Quest-5 <<<<<<<<<<<<

        vencedor = determinar_vencedor(jogada_jogador_a, jogada_jogador_b, regras_dct) # <<< Quest-5 <<<<<<<<<<<<

        exibir_resultado_rodada(jogada_jogador_a, jogada_jogador_b, vencedor) # <<< Quest-5 <<<<<<<<<<<<
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct) # <<< Quest-5 <<<<<<<<<<<<

        if not ler_jogar_novamente():
            break

    print("Obrigado por jogar!")

#---------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    jogar()
