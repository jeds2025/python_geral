import random

# Funções originais
def obter_regras() -> dict[str, str]:
    result = {
        'pedra': 'tesoura',
        'tesoura': 'papel',
        'papel': 'pedra'
    }
    return result

def obter_jogada_computador() -> str:
    jogadas_validas = ['pedra', 'papel', 'tesoura']
    jogada = random.choice(jogadas_validas)
    return jogada

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

# Variações
def modo_1_classico():
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}
    while True:
        print("\n--- Modo 1: Clássico ---")
        jogada_jogador = ler_jogada()
        jogada_computador = obter_jogada_computador()
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)
        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)
        if not ler_jogar_novamente():
            break
    print("Obrigado por jogar!")

def modo_2_probabilistico():
    regras_dct = obter_regras()
    jogadas_validas = ['pedra', 'papel', 'tesoura']
    pesos = [0.5, 0.3, 0.2]
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}
    while True:
        print("\n--- Modo 2: Probabilístico ---")
        jogada_jogador = ler_jogada()
        jogada_computador = random.choices(jogadas_validas, weights=pesos, k=1)[0]
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)
        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)
        if not ler_jogar_novamente():
            break
    print("Obrigado por jogar!")

historico_jogadas = []
def modo_3_inteligente():
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}
    while True:
        print("\n--- Modo 3: Inteligente ---")
        jogada_jogador = ler_jogada()
        historico_jogadas.append(jogada_jogador)
        if len(historico_jogadas) > 1:
            ultima = historico_jogadas[-2]
            jogada_computador = next((j for j in regras_dct if regras_dct[j] == ultima), obter_jogada_computador())
        else:
            jogada_computador = obter_jogada_computador()
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)
        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)
        if not ler_jogar_novamente():
            break
    print("Obrigado por jogar!")

def modo_4_torneio():
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}
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

historico = []
def modo_5_historico():
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}
    while True:
        print("\n--- Modo 5: Histórico ---")
        jogada_jogador = ler_jogada()
        jogada_computador = obter_jogada_computador()
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)
        historico.append(f"{jogada_jogador} vs {jogada_computador} => {vencedor}")
        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)
        if not ler_jogar_novamente():
            break
    print("\n=== Histórico de Rodadas ===")
    for linha in historico:
        print(linha)
    print("Obrigado por jogar!")

def modo_6_didatico():
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}
    while True:
        print("\n--- Modo 6: Didático ---")
        jogada_jogador = ler_jogada()
        jogada_computador = obter_jogada_computador()
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)
        print(f"Você escolheu: {jogada_jogador.upper()} | Computador escolheu: {jogada_computador.upper()}")
        if vencedor == 'jogador':
            print(f">> Você venceu! Porque {jogada_jogador} vence {jogada_computador}. <<")
        elif vencedor == 'computador':
            print(f">> Você perdeu! Porque {jogada_computador} vence {jogada_jogador}. <<")
        else:
            print(">> Empate! Ambos escolheram a mesma arma. <<")
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)
        if not ler_jogar_novamente():
            break
    print("Obrigado por jogar!")

def modo_7_oculto():
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}
    while True:
        print("\n--- Modo 7: Oculto ---")
        jogada_jogador = ler_jogada()
        jogada_computador = obter_jogada_computador()
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)
        print(f"Você escolheu: {jogada_jogador.upper()} | Resultado: {vencedor.upper()} (jogada do computador oculta)")
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)
        if not ler_jogar_novamente():
            break
    print("Obrigado por jogar!")

def modo_8_reverso():
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}
    while True:
        print("\n--- Modo 8: Reverso ---")
        jogada_jogador = ler_jogada()
        jogada_computador = obter_jogada_computador()
        vencedor_original = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)
        if vencedor_original == 'jogador':
            vencedor = 'computador'
        elif vencedor_original == 'computador':
            vencedor = 'jogador'
        else:
            vencedor = 'empates'
        print(f"Você escolheu: {jogada_jogador.upper()} | Computador escolheu: {jogada_computador.upper()}")
        print(f">> Resultado invertido: {vencedor.upper()} <<")
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)
        if not ler_jogar_novamente():
            break
    print("Obrigado por jogar!")

def modo_9_silencioso():
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}
    while True:
        print("\n--- Modo 9: Silencioso ---")
        jogada_jogador = ler_jogada()
        jogada_computador = obter_jogada_computador()
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)
        if not ler_jogar_novamente():
            break
    print("Obrigado por jogar!")

def modo_10_estatistico():
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}
    total_rodadas = 0
    while True:
        print("\n--- Modo 10: Estatístico ---")
        jogada_jogador = ler_jogada()
        jogada_computador = obter_jogada_computador()
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)
        total_rodadas += 1
        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)
        print(f"Média de vitórias por rodada: Jogador {placar_dct['jogador']/total_rodadas:.2f} | Computador {placar_dct['computador']/total_rodadas:.2f}")
        if not ler_jogar_novamente():
            break
    print("Obrigado por jogar!")
    
def menu():
    modos = {
        "1": ("Clássico", modo_1_classico),
        "2": ("Probabilístico", modo_2_probabilistico),
        "3": ("Inteligente", modo_3_inteligente),
        "4": ("Torneio", modo_4_torneio),
        "5": ("Histórico", modo_5_historico),
        "6": ("Didático", modo_6_didatico),
        "7": ("Oculto", modo_7_oculto),
        "8": ("Reverso", modo_8_reverso),
        "9": ("Silencioso", modo_9_silencioso),
        "10": ("Estatístico", modo_10_estatistico),
    }

    while True:
        print("\n=== Menu de Variações ===")
        for k, (nome, _) in modos.items():
            print(f"{k}. {nome}")
        escolha = input("Escolha o modo (1-10) ou 'sair': ").strip()
        if escolha == 'sair':
            print("Até a próxima, Enaldo!")
            break
        elif escolha in modos:
            print(f"\n>> Iniciando modo: {modos[escolha][0]} <<")
            modos[escolha][1]()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()