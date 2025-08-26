"""
=============================================================
Mini-Projeto: Jogo Adivinhe o Número
Autor.....: Prof. Carlos Augusto de S. Almeida
Data......: 26/07/2025
Contato...: carlos.almeida@academico.ifs.edu.br
Licença...: GNU General Public License (GPL)
Requisitos: Python 3.12+

Descrição: Jogo interativo em Python onde o computador escolhe um número secreto 
    e o jogador deve adivinhar em um número limitado de tentativas. O sistema 
    fornece dicas ("muito alto", "muito baixo") e informa vitória ou derrota ao final.
Versão...: 1.0
=============================================================
"""

import random

# ==============================================================================================
# DEFINIÇÃO DAS FUNÇÕES AUXILIARES (desenvolvidas nas questões anteriores)
# ==============================================================================================

def gerar_numero_secreto(minimo: int, maximo: int) -> int:
    """Gera um número inteiro aleatório dentro de um intervalo especificado."""
    return random.randint(minimo, maximo)

def validar_entrada(entrada_usuario: str) -> bool:
    """Verifica se uma string fornecida contém exclusivamente caracteres numéricos."""
    return entrada_usuario.strip().isdigit()

def analisar_palpite(palpite: int, numero_secreto: int) -> str:
    """Compara o palpite do jogador com o número secreto e retorna o resultado."""
    match resultado_analise:
        case "muito baixo":
            print("Ops, seu palpite foi muito baixo!")
        case "muito alto":
            print("Ops, seu palpite foi muito alto!")
        case "correto":
            print("Parabéns! Você acertou!")
        case _:
            raise ValueError("'resultado_analise' desconhecido!")

def atualizar_tentativas(tentativas_restantes: int) -> int:
    """Decrementa o número de tentativas restantes em uma unidade."""
    return tentativas_restantes - 1

# ==============================================================================================
# FUNÇÃO PRINCIPAL DO JOGO
# ==============================================================================================

def jogar():
    """
    Orquestra o jogo 'Adivinhe o Número' do início ao fim.

    Esta função gerencia o fluxo principal do jogo, incluindo a configuração inicial, o loop de
    jogadas, a interação com o usuário, a validação de entradas e a determinação do resultado
    final (vitória ou derrota).

    Como funciona:
    A função inicializa as variáveis do jogo, como o número secreto e o total de tentativas.
    Em seguida, entra em um loop `while` que continua enquanto o jogador tiver tentativas. A
    cada iteração, solicita um palpite, valida a entrada, analisa a jogada e fornece
    feedback. O loop pode ser interrompido por uma vitória (`break`) ou terminar naturalmente
    quando as tentativas se esgotam. Uma mensagem de vitória ou derrota é exibida no final.

    Pseudocódigo:
    1.  Definir as constantes do jogo: intervalo de números e número máximo de tentativas.
    2.  Imprimir uma mensagem de boas-vindas.
    3.  Gerar o número secreto chamando `gerar_numero_secreto`.
    4.  Inicializar uma variável de controle de vitória (ex: `acertou = False`).
    5.  Iniciar um loop `while` que continua enquanto houver tentativas (`tentativas > 0`).
    6.  Dentro do loop, exibir o número de tentativas restantes.
    7.  Solicitar o palpite do jogador e armazenar como string.
    8.  Validar a entrada usando `validar_entrada`. Se for inválida, exibir uma mensagem de
        erro e continuar para a próxima iteração do loop, sem gastar uma tentativa.
    9.  Converter a entrada validada para um número inteiro.
    10. Analisar o palpite com `analisar_palpite`.
    11. Verificar o resultado da análise:
        a. Se for 'correto', exibir mensagem de vitória, atualizar a variável de controle
           `acertou` para True e encerrar o loop com `break`.
        b. Se for 'muito alto' ou 'muito baixo', exibir o feedback correspondente.
    12. Se o palpite foi incorreto, decrementar o número de tentativas com `atualizar_tentativas`.
    13. Após o término do loop, verificar a variável `acertou`. Se for `False`, significa
        que o jogador perdeu. Exibir a mensagem de derrota, revelando o número secreto.

    Note:
        A função utiliza um bloco `if __name__ == '__main__':` para garantir que a execução do
        jogo só ocorra quando o script for executado diretamente.
    """
    # (passo 1) Define os parâmetros do jogo.
    MIN_NUMERO = 1
    MAX_NUMERO = 100
    TOTAL_TENTATIVAS = 7

    # (passo 2) Imprime o cabeçalho do jogo.
    print(f"--- Adivinhe o Número ({MIN_NUMERO}-{MAX_NUMERO}) ---")
    
    # (passo 3) Gera o número secreto para a partida.
    numero_secreto = gerar_numero_secreto(MIN_NUMERO, MAX_NUMERO)
    
    # Inicializa as variáveis de controle da partida.
    tentativas = TOTAL_TENTATIVAS
    # (passo 4) Flag para controlar se o jogador acertou o número.
    acertou = False

    # (passo 5) Loop principal do jogo.
    while tentativas > 0:
        # (passo 6) Exibe o estado atual do jogo.
        print(f"Você tem {tentativas} tentativas.")
        
        # (passo 7) Solicita a entrada do jogador.
        palpite_str = input("Qual o seu palpite? ")
        
        # (passo 8) Valida a entrada do jogador.
        if not validar_entrada(palpite_str):
            print("Entrada inválida. Por favor, digite um número.")
            print() # Adiciona uma linha em branco para melhor legibilidade
            continue # Pula para a próxima iteração sem gastar uma tentativa
            
        # (passo 9) Converte a entrada para inteiro.
        palpite_int = int(palpite_str)
        
        # (passo 10) Analisa o palpite.
        resultado = analisar_palpite(palpite_int, numero_secreto)
        
        # (passo 11) Fornece feedback com base na análise.
        if resultado == 'correto':
            # (passo 11a) O jogador acertou.
            print(f"Parabéns! Você acertou o número {numero_secreto}!")
            acertou = True
            break # Encerra o loop, pois o jogo acabou.
        else:
            # (passo 11b) O jogador errou. Fornece uma dica.
            # Nota: O formato "Muito alto!" é usado para corresponder ao exemplo da questão.
            dica = "Muito baixo!" if resultado == 'muito baixo' else "Muito alto!"
            print(dica)

        # (passo 12) Decrementa o número de tentativas se o palpite foi incorreto.
        tentativas = atualizar_tentativas(tentativas)
        print() # Adiciona uma linha em branco para espaçamento

    # (passo 13) Após o loop, verifica se o jogador não acertou.
    if not acertou:
        print("\nFim de jogo! Você não conseguiu adivinhar.")
        print(f"O número secreto era: {numero_secreto}")


# Inicia o jogo quando o script é executado diretamente.
if __name__ == '__main__':
    jogar()
