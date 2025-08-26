import random

def obter_regras() -> dict[str, str]:
    # (passo 1) Cria o dicionário de regras
    result = {
        'pedra': 'tesoura',
        'tesoura': 'papel',
        'papel': 'pedra'
    }
    # (passo 2) Retorna o dicionário
    return result

def obter_jogada_computador() -> str:
    # (passo 1) Define as jogadas válidas
    jogadas_validas = ['pedra', 'papel', 'tesoura']
    # (passo 2) Seleciona aleatoriamente
    jogada = random.choice(jogadas_validas)
    # (passo 3) Retorna a jogada
    return jogada

def determinar_vencedor(jogada_jogador: str, jogada_computador: str, regras: dict[str, str]) -> str:
    # (passo 1) Verifica empate
    if jogada_jogador == jogada_computador:
        return 'empate'
    # (passo 2) Verifica se o jogador vence
    if regras[jogada_jogador] == jogada_computador:
        return 'jogador'
    # (passo 3) Caso contrário, computador vence
    return 'computador'

def atualizar_placar(placar: dict[str, int], vencedor_rodada: str) -> dict[str, int]:
    # (passo 1) Incrementa placar do jogador
    if vencedor_rodada == 'jogador':
        placar['jogador'] += 1
    # (passo 2) Incrementa placar do computador
    elif vencedor_rodada == 'computador':
        placar['computador'] += 1
    # (passo 3) Incrementa empates
    elif vencedor_rodada == 'empate':
        placar['empates'] += 1
    # (passo 4) Retorna placar atualizado
    return placar

def exibir_resultado_rodada(jogada_jogador: str, jogada_computador: str, vencedor_rodada: str) -> None:
    # (passo 1) Imprime escolhas
    print(f"Você escolheu: {jogada_jogador.upper()} | Computador escolheu: {jogada_computador.upper()}")
    # (passo 2) Mensagem de vitória
    if vencedor_rodada == 'jogador':
        print(">> Você venceu! <<")
    # (passo 3) Mensagem de empate
    elif vencedor_rodada == 'empate':
        print(">> Empate! <<")
    # (passo 4) Mensagem de derrota
    else:  # resultado == 'computador'
        print(">> Você perdeu! <<")

def ler_jogada() -> str:
    # (passo 1) Simula reconhecimento de voz
    print("* Simulando reconhecimento de voz... *")
    jogada = input("Fale (ou digite) sua arma: Pedra, Papel ou Tesoura? ").lower()
    # (passo 2) Retorna jogada
    return jogada

def print_placar(placar_dct: dict[str, int]) -> None:
    print(f"Placar: Jogador {placar_dct['jogador']} | Computador {placar_dct['computador']} | Empates {placar_dct['empates']}")

def ler_jogar_novamente() -> bool:
    resposta = input("Jogar novamente? (s/n): ").lower()
    return resposta == 's'

def jogar() -> None:
    # (passo 1) Inicializa regras e placar
    regras_dct = obter_regras()
    placar_dct = {"jogador": 0, "computador": 0, "empates": 0}
    # (passo 2) Loop principal do jogo
    while True:
        # (passo 2.1) Exibe cabeçalho
        print("\n--- Jogo Pedra, Papel, Tesoura (Simulação de Voz) ---")
        # (passo 2.2) Lê jogada do usuário
        jogada_jogador = ler_jogada()
        # (passo 2.3) Gera jogada do computador
        jogada_computador = obter_jogada_computador()
        # (passo 2.4) Determina vencedor
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador, regras_dct)
        # (passo 2.5) Exibe resultado e atualiza placar
        exibir_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        placar_dct = atualizar_placar(placar_dct, vencedor)
        print_placar(placar_dct)
        # (passo 2.6) Pergunta se deseja jogar novamente
        continuar = ler_jogar_novamente()
        if not continuar:
            break
    # (passo 3) Mensagem de agradecimento
    print("Obrigado por jogar!")

if __name__ == '__main__':
    jogar()