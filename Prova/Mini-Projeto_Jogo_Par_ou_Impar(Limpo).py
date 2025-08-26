import random
import sys

def verificar_paridade(numero: int) -> str:
    return 'par' if numero % 2 == 0 else 'impar'

def obter_numero_computador(maximo: int) -> int:
    return random.randint(0, maximo)

def determinar_vencedor_rodada(soma: int, escolha_jogador: str) -> str:
    resultado_real = verificar_paridade(soma)
    return 'jogador' if resultado_real == escolha_jogador else 'computador'

def atualizar_placar(placar: dict[str, int], vencedor: str) -> dict[str, int]:
    placar[vencedor] += 1
    return placar

def exibir_resultado_rodada(num_jogador: int, num_computador: int, escolha_jogador: str, vencedor: str) -> None:
    soma = num_jogador + num_computador
    paridade_soma = verificar_paridade(soma)
    print()
    print(f"Você jogou {num_jogador} e escolheu {escolha_jogador.upper()}.")
    print(f"O computador jogou {num_computador}.")
    print(f"A soma é {soma} ({paridade_soma.upper()}).")
    if vencedor == 'jogador':
        print(">> Você venceu! <<")
    else:
        print(">> Você perdeu! <<")

def jogar():
    NUMERO_MAXIMO = 5
    placar = {"jogador": 0, "computador": 0}

    while True:
        print("\n--- Jogo Par ou Ímpar ---")

        escolha_paridade = ""
        while escolha_paridade not in ["par", "impar"]:
            escolha_paridade = input("Você escolhe PAR ou IMPAR? ").lower().strip()
            if escolha_paridade == "ímpar":
                escolha_paridade = "impar"

        num_jogador = -1
        while num_jogador == -1:
            entrada = input(f"Digite um número (0-{NUMERO_MAXIMO}): ").strip()
            if entrada.isdigit() and 0 <= int(entrada) <= NUMERO_MAXIMO:
                num_jogador = int(entrada)
            else:
                print(f"Entrada inválida. Digite um número entre 0 e {NUMERO_MAXIMO}.")

        num_computador = obter_numero_computador(NUMERO_MAXIMO)
        soma_total = num_jogador + num_computador
        vencedor = determinar_vencedor_rodada(soma_total, escolha_paridade)
        placar = atualizar_placar(placar, vencedor)
        exibir_resultado_rodada(num_jogador, num_computador, escolha_paridade, vencedor)
        print(f"PLACAR: Jogador {placar['jogador']} X {placar['computador']} Computador")

        continuar = ""
        while continuar not in ['s', 'n']:
            continuar = input("\nJogar novamente? (s/n): ").lower().strip()
        if continuar == 'n':
            print("Obrigado por jogar!")
            break

if __name__ == '__main__':
    try:
        jogar()
    except (KeyboardInterrupt, EOFError):
        print("\n\nJogo interrompido. Obrigado por jogar!")
        sys.exit(0)
