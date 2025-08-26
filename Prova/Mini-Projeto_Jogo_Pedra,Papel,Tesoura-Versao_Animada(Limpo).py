import collections
import os
import random
import time

class Cores:
    """Agrupa códigos de escape ANSI para colorir o texto no terminal."""
    RESET = '\033[0m'
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'

ARTES_ASCII: dict[str, list[str]] = {
    'punho': [
        "    __________      ",
        "---'   ______)      ",
        "      (_____)       ",
        "      (_____)       ",
        "      (____)        ",
        "---.__(___)         ",
        "      Punho         "
    ],
    'pedra': [
        "    __________      ",
        "---'   ______)      ",
        "      (_____)       ",
        "      (_____)       ",
        "      (____)        ",
        "---.__(___)         ",
        "      Pedra         " 
    ],
    'papel': [
        "    __________      ",
        "---'    ______)____ ",
        "           _______) ",
        "          _______)  ",
        "         _______)   ",
        "---.__________)     ",
        "       Papel        "
    ],
    'tesoura': [
        "    _______         ",
        "---'   ____)____    ",
        "          ______)   ",
        "       __________)  ",
        "      (____)        ",
        "---.__(___)         ",
        "       Tesoura      "
    ],
    'tesoura_quebrada': [
        "    _______         ",
        "---'   ____)____    ",
        "          x_____)   ",
        "       x_________)  ",
        "      (x___)        ",
        "---.__(x__)         ",
        "  Tesoura Quebrada  " 
    ],
    'papel_cortado': [
        "    --.--        ",
        "---'  /  )____   ",
        "     /  ______)  ",
        "    /  _______)  ",
        "   /  _______)   ",
        "---.__________)  ",
        " Papel Cortado   " 
    ],
    'pedra_coberta': [
        "   -----------    ",
        "--|           |---",
        "  |   Pedra   |   ",
        "  |  Coberta  |   ",
        "  |           |   ",
        "  --------------- ",
        "                  "
    ],
    'trofeu': [
        "      ___________    ",
        "     '._==_==_=_.'   ",
        "     .-\\:      /-.  ",
        "    | (|:.     |) |  ",
        "     '-|:.     |-'   ",
        "       \\::.    /    ",
        "        '::. .'      ",
        "          ) (        ",
        "        _.' '._      ",
        "       `-------`     ",
        "        Troféu       ",
    ]
}

REGRAS_IMPACTO = {
    ('pedra', 'tesoura'): {'arte_perdedor': 'tesoura_quebrada', 'msg': "* Pedra esmaga Tesoura! *"},
    ('tesoura', 'papel'): {'arte_perdedor': 'papel_cortado', 'msg': "* Tesoura corta Papel! *"},
    ('papel', 'pedra'): {'arte_perdedor': 'pedra_coberta', 'msg': "* Papel embrulha Pedra! *"}
}

def limpar_tela() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_banner_inicial() -> None:
    limpar_tela()
    print(Cores.CIANO + "==========================================================")
    print("|                                                        |")
    print("|   Bem-vindo ao PEDRA, PAPEL & TESOURA: Edição Épica!   |")
    print("|                                                        |")
    print("==========================================================" + Cores.RESET)
    print()

def obter_nome_jogador() -> str:
    while True:
        nome = input("Primeiro, qual o seu nome? ").strip()
        if nome:
            return nome.capitalize()
        print(Cores.VERMELHO + "Por favor, digite um nome válido." + Cores.RESET)

def escolher_modo_jogo() -> dict[str, str | int | float]:
    print("\nOlá! Qual modo de jogo você prefere?")
    print(f"{Cores.AMARELO}[1]{Cores.RESET} Casual (Jogue até cansar)")
    print(f"{Cores.AMARELO}[2]{Cores.RESET} Melhor de 3 (Vence quem ganhar 2 rodadas)")
    print(f"{Cores.AMARELO}[3]{Cores.RESET} Melhor de 5 (Vence quem ganhar 3 rodadas)")

    while True:
        escolha = input("Sua escolha: ").strip()
        if escolha == '1':
            return {'tipo': 'casual', 'vitorias_necessarias': float('inf')}
        if escolha == '2':
            return {'tipo': 'melhor_de_3', 'vitorias_necessarias': 2}
        if escolha == '3':
            return {'tipo': 'melhor_de_5', 'vitorias_necessarias': 3}
        print(Cores.VERMELHO + "Opção inválida. Digite 1, 2 ou 3." + Cores.RESET)

def ler_jogada_jogador() -> str:
    jogadas_validas = {
        'pedra': 'pedra', 'pe': 'pedra',
        'papel': 'papel', 'pa': 'papel',
        'tesoura': 'tesoura', 't': 'tesoura'
    }
    while True:
        prompt = f"{Cores.CIANO}[?] Declare sua arma (Pedra, Papel ou Tesoura): {Cores.RESET}"
        entrada = input(prompt).lower().strip()
        if entrada in jogadas_validas:
            return jogadas_validas[entrada]
        print(Cores.VERMELHO + "Arma desconhecida! Escolha entre Pedra, Papel ou Tesoura." + Cores.RESET)

def obter_jogada_computador_adaptativa(historico_jogador: list[str]) -> str:
    jogadas = ['pedra', 'papel', 'tesoura']
    regras_vitoria = {'pedra': 'papel', 'papel': 'tesoura', 'tesoura': 'pedra'}

    if len(historico_jogador) < 5:
        return random.choice(jogadas)

    jogada_mais_comum = collections.Counter(historico_jogador[-5:]).most_common(1)[0][0]

    if random.random() < 0.75:
        return regras_vitoria[jogada_mais_comum]
    else:
        return random.choice(jogadas)

def determinar_vencedor(jogada_jogador: str, jogada_computador: str) -> str:
    regras = {
        'pedra': 'tesoura',
        'tesoura': 'papel',
        'papel': 'pedra'
    }
    if jogada_jogador == jogada_computador:
        return 'empate'
    if regras[jogada_jogador] == jogada_computador:
        return 'jogador'
    return 'computador'

def atualizar_estado(
    estado: dict, vencedor: str, jogada_jogador: str
) -> None:
    estado['historico_jogador'].append(jogada_jogador)
    estado['estatisticas']['jogadas_jogador'][jogada_jogador] += 1

    if vencedor == 'jogador':
        estado['placar_partida']['jogador'] += 1
        estado['estatisticas']['vitorias'] += 1
    elif vencedor == 'computador':
        estado['placar_partida']['computador'] += 1
        estado['estatisticas']['derrotas'] += 1
    else:  # empate
        estado['estatisticas']['empates'] += 1

def animacao_mao_treme() -> None:
    for texto in ["Pedra...", "Papel...", "Tesoura..."]:
        limpar_tela()
        print(f"\n\n{Cores.AMARELO}{texto.center(60)}{Cores.RESET}\n")
        for linha in ARTES_ASCII['punho']:
            print(" " * 20 + linha)
        time.sleep(0.7)
        limpar_tela()

def exibir_confronto_animado(
    jogador: str, jog_jogador: str, jog_computador: str, vencedor: str
) -> None:

    def _selecionar_artes_e_mensagens():
        """Seleciona artes, cores e mensagens de impacto com base no resultado da rodada."""
        if vencedor == 'empate':
            arte_jog = ARTES_ASCII[jog_jogador]
            arte_comp = ARTES_ASCII[jog_computador]
            cor = Cores.AMARELO
            msg_venc = ">> EMPATE! <<"
            msg_impacto = f"{Cores.AMARELO}* Empate! *{Cores.RESET}"
            return arte_jog, arte_comp, msg_impacto, cor, msg_venc

        if vencedor == 'jogador':
            jogada_vencedora, jogada_perdedora = jog_jogador, jog_computador
            cor, msg_venc = Cores.VERDE, f">> {jogador.upper()} VENCEU A RODADA! <<"
        else: # vencedor == 'computador'
            jogada_vencedora, jogada_perdedora = jog_computador, jog_jogador
            cor, msg_venc = Cores.VERMELHO, ">> COMPUTADOR VENCEU A RODADA! <<"

        impacto = REGRAS_IMPACTO.get((jogada_vencedora, jogada_perdedora))
        msg_impacto = f"{Cores.VERMELHO}{impacto['msg']}{Cores.RESET}"
        
        arte_vencedora = ARTES_ASCII[jogada_vencedora]
        arte_perdedora = ARTES_ASCII[impacto['arte_perdedor']]

        arte_jog, arte_comp = (arte_vencedora, arte_perdedora) if vencedor == 'jogador' else (arte_perdedora, arte_vencedora)
        
        return arte_jog, arte_comp, msg_impacto, cor, msg_venc

    def _imprimir_cabecalho():
        print(f"\n{Cores.CIANO}{jogador.upper().center(28)}{Cores.RESET}{'COMPUTADOR'.center(35)}")
        print("-" * 64)

    def _imprimir_artes_lado_a_lado(arte_jog, arte_comp):
        for i in range(len(arte_jog)):
            print(f"{arte_jog[i]:<28}    {arte_comp[i]}")
        print("-" * 64)

    def _imprimir_nomes_jogadas():
        print(f"[{jog_jogador.upper():^26}]    [{jog_computador.upper():^26}]")

    def _imprimir_mensagens(msg_impacto, cor, msg_venc):
        print(f"\n{msg_impacto.center(70)}\n")
        print(f"{cor}{msg_venc.center(64)}{Cores.RESET}")

    limpar_tela()
    arte_jogador, arte_computador, mensagem_impacto, cor_msg, msg_vencedor = _selecionar_artes_e_mensagens()
    
    _imprimir_cabecalho()
    _imprimir_artes_lado_a_lado(arte_jogador, arte_computador)
    _imprimir_nomes_jogadas()
    _imprimir_mensagens(mensagem_impacto, cor_msg, msg_vencedor)

def exibir_placar_partida(estado: dict) -> None:
    nome_jogador = estado['nome_jogador']
    placar = estado['placar_partida']
    modo = estado['modo_jogo']['tipo'].replace('_', ' ').title()

    print("\n" + "="*40)
    print(f"  PLACAR DA PARTIDA ({modo})")
    print(f"  {Cores.CIANO}{nome_jogador}: {placar['jogador']}{Cores.RESET} | "
          f"{Cores.VERMELHO}Computador: {placar['computador']}{Cores.RESET}")
    print("="*40 + "\n")

def exibir_estatisticas_finais(estado: dict) -> None:
    limpar_tela()
    stats = estado['estatisticas']
    nome_jogador = estado['nome_jogador']

    print(Cores.MAGENTA + "=========================================")
    print("|                                       |")
    print("|           FIM DE JOGO!                |")
    print("|                                       |")
    print("=========================================" + Cores.RESET)

    if stats['vitorias'] > stats['derrotas']:
        print(f"\nParabéns, {nome_jogador}! Você foi o grande campeão da sessão!")
        for linha in ARTES_ASCII['trofeu']:
            print(Cores.AMARELO + linha.center(40) + Cores.RESET)
    elif stats['derrotas'] > stats['vitorias']:
        print(f"\nNão foi dessa vez, {nome_jogador}. O computador levou a melhor!")
    else:
        print(f"\nUma batalha equilibrada, {nome_jogador}! Terminaram empatados.")

    total_jogos = stats['vitorias'] + stats['derrotas'] + stats['empates']
    taxa_vitoria = (stats['vitorias'] / total_jogos * 100) if total_jogos > 0 else 0
    
    arma_favorita = "Nenhuma"
    if total_jogos > 0:
        arma_favorita = max(stats['jogadas_jogador'], key=stats['jogadas_jogador'].get)

    print("\n--- SUAS ESTATÍSTICAS DA SESSÃO ---")
    print(f"  {Cores.VERDE}Vitórias: {stats['vitorias']}{Cores.RESET}")
    print(f"  {Cores.VERMELHO}Derrotas: {stats['derrotas']}{Cores.RESET}")
    print(f"  {Cores.AMARELO}Empates:  {stats['empates']}{Cores.RESET}")
    print(f"  Taxa de Vitória: {taxa_vitoria:.1f}%")
    print(f"  Sua Arma Favorita: {arma_favorita.capitalize()}")
    print("-" * 35)

def executar_partida(estado: dict) -> None:
    estado['placar_partida'] = { 'jogador': 0, 'computador': 0 }
    rodada = 1

    while True:
        limpar_tela()
        print(f"--- RODADA {rodada} ---")
        if estado['modo_jogo']['tipo'] != 'casual':
            exibir_placar_partida(estado)

        jogada_jogador = ler_jogada_jogador()
        animacao_mao_treme()
        jogada_computador = obter_jogada_computador_adaptativa(estado['historico_jogador'])
        vencedor = determinar_vencedor(jogada_jogador, jogada_computador)

        atualizar_estado(estado, vencedor, jogada_jogador)

        exibir_confronto_animado(
            estado['nome_jogador'], jogada_jogador, jogada_computador, vencedor
        )

        placar_jog = estado['placar_partida']['jogador']
        placar_comp = estado['placar_partida']['computador']
        vitorias_nec = estado['modo_jogo']['vitorias_necessarias']

        input("\nPressione Enter para continuar...")

        if placar_jog >= vitorias_nec or placar_comp >= vitorias_nec:
            limpar_tela()
            exibir_placar_partida(estado)
            vencedor_partida = estado['nome_jogador'] if placar_jog > placar_comp else "Computador"
            print(f"{Cores.VERDE}*** {vencedor_partida.upper()} VENCEU A PARTIDA! ***{Cores.RESET}")
            break

        rodada += 1

def jogar() -> None:
    exibir_banner_inicial()
    nome_jogador = obter_nome_jogador()

    estado_geral = {
        'nome_jogador': nome_jogador,
        'historico_jogador': [],
        'estatisticas': {
            'vitorias': 0, 'derrotas': 0, 'empates': 0,
            'jogadas_jogador': {'pedra': 0, 'papel': 0, 'tesoura': 0}
        }
    }

    while True:
        limpar_tela()
        modo_jogo = escolher_modo_jogo()
        estado_geral['modo_jogo'] = modo_jogo

        executar_partida(estado_geral)

        resposta = input("\nDeseja jogar outra partida? (s/n): ").lower().strip()
        if resposta != 's':
            break

    exibir_estatisticas_finais(estado_geral)
    print("\nObrigado por jogar! Até a próxima!\n")

if __name__ == '__main__':
    try:
        jogar()
    except KeyboardInterrupt:
        print("\n\nJogo interrompido pelo usuário. Até a próxima!")
