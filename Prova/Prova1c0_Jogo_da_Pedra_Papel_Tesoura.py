import random

def escolher_opcao():
    """Escolhe aleatoriamente entre pedra, papel ou tesoura para o computador."""
    return random.choice(['pedra', 'papel', 'tesoura'])

def verificar_vencedor(jogador, computador):
    """Verifica o resultado da partida entre jogador e computador."""
    if jogador == computador:
        return 'Empate'
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        return 'Jogador'
    else:
        return 'Computador'

def jogar():
    print("--- Jogo Pedra, Papel e Tesoura ---")
    print("Opções válidas: pedra, papel, tesoura")
    print("Digite 'sair' para encerrar o jogo.")
    
    placar = {"Jogador": 0, "Computador": 0, "Empates": 0}
    
    while True:
        escolha_jogador = input("\nDigite sua escolha: ").strip().lower()
        
        if escolha_jogador == 'sair':
            print("\n--- Resultado Final ---")
            print(f"Você venceu {placar['Jogador']} vezes.")
            print(f"O computador venceu {placar['Computador']} vezes.")
            print(f"Houve {placar['Empates']} empates.")
            print("Encerrando jogo. Obrigado por jogar!")
            break
        
        if escolha_jogador not in ['pedra', 'papel', 'tesoura']:
            print("Escolha inválida! Tente novamente.")
            continue
        
        escolha_computador = escolher_opcao()
        print(f"Computador escolheu: {escolha_computador}")
        
        resultado = verificar_vencedor(escolha_jogador, escolha_computador)
        
        if resultado == 'Empate':
            print("Empate!")
            placar['Empates'] += 1
        elif resultado == 'Jogador':
            print("Você venceu!")
            placar['Jogador'] += 1
        else:
            print("Computador venceu!")
            placar['Computador'] += 1

if __name__ == "__main__":
    jogar()
