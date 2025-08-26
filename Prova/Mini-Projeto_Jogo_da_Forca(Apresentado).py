"""
=============================================================
Mini-Projeto: Jogo da Forca
Autor.....: Prof. Carlos Augusto de S. Almeida
Data......: 26/07/2025
Contato...: carlos.almeida@academico.ifs.edu.br
Licença...: GNU General Public License (GPL)
Requisitos: Python 3.12+

Descrição: Jogo da Forca em Python. O sistema escolhe uma palavra secreta e o 
    jogador deve adivinhar as letras, com número limitado de tentativas. O jogo 
    exibe o progresso, letras erradas e informa vitória ou derrota ao final.
Versão...: 1.0
=============================================================
"""

import random
from typing import Tuple

# ==============================================================================================
# DEFINIÇÃO DAS FUNÇÕES AUXILIARES (desenvolvidas nas questões anteriores)
# ==============================================================================================

def obter_palavra_secreta() -> str:
    """Seleciona e retorna aleatoriamente uma palavra de uma lista predefinida."""
    palavras = ["python", "programacao", "desenvolvimento", "algoritmo", "computador", "interface"]
    return random.choice(palavras).lower()

def exibir_palavra_mascarada(palavra_secreta: str, letras_corretas: set[str]) -> str:
    """Constrói a string que representa o progresso do jogador na palavra."""
    return " ".join([letra if letra in letras_corretas else "_" for letra in palavra_secreta])

def validar_letra(letra: str, letras_corretas: set[str], letras_erradas: set[str]) -> Tuple[bool, str]:
    """Valida a letra digitada pelo jogador."""
    letra = letra.lower()
    if len(letra) != 1 or not letra.isalpha():
        return (False, 'Entrada inválida. Por favor, digite uma única letra.')
    if letra in letras_corretas or letra in letras_erradas:
        return (False, 'Você já tentou essa letra.')
    return (True, 'Letra válida.')

def processar_jogada(letra: str, palavra_secreta: str, corretas: set[str], erradas: set[str], tentativas: int) -> int:
    """Processa uma letra válida, atualizando o estado do jogo."""
    if letra in palavra_secreta:
        corretas.add(letra)
        print("Correto!")
    else:
        erradas.add(letra)
        tentativas -= 1
        print("Errado!")
    return tentativas

def checar_fim_de_jogo(palavra_secreta: str, letras_corretas: set[str], tentativas: int) -> str:
    """Verifica e retorna o estado atual do jogo: vitória, derrota ou continuação."""
    if set(palavra_secreta).issubset(letras_corretas):
        return 'vitoria'
    if tentativas == 0:
        return 'derrota'
    return 'continua'

# ==============================================================================================
# FUNÇÃO PRINCIPAL DO JOGO
# ==============================================================================================

def jogar():
    """
    Orquestra a execução completa do Jogo da Forca.

    Esta função principal inicializa o jogo, gerencia o loop de rodadas, interage com o
    jogador, invoca as funções auxiliares para processar a lógica e determina o resultado
    final.

    Como funciona:
    O jogo começa com a seleção de uma palavra secreta e a inicialização das variáveis de
    estado (tentativas, conjuntos de letras). Um loop `while` infinito é iniciado, que só
    será quebrado por uma condição de vitória ou derrota. A cada iteração, o estado atual do
    jogo é exibido, uma letra é solicitada ao jogador, e essa letra é validada. Se válida, a
    jogada é processada. Ao final de cada rodada, o estado do jogo é verificado. Se o jogo
    terminou, uma mensagem final é exibida e o loop é interrompido.

    Pseudocódigo:
    1.  Iniciar o jogo: chamar `obter_palavra_secreta` para obter a palavra.
    2.  Inicializar as variáveis de estado: tentativas, e os conjuntos de letras corretas e
        erradas (vazios).
    3.  Iniciar um loop infinito (`while True`) para as rodadas do jogo.
    4.  Dentro do loop, exibir o cabeçalho e o estado atual do jogo:
        - Chamar `exibir_palavra_mascarada` e imprimir o resultado.
        - Imprimir as letras erradas e o número de tentativas restantes.
    5.  Solicitar ao jogador que digite uma letra.
    6.  Chamar `validar_letra` para verificar a entrada.
        - Se a letra for inválida, imprimir a mensagem de erro e usar `continue` para
          iniciar a próxima rodada.
    7.  Se a letra for válida, chamar `processar_jogada` para atualizar o estado do jogo.
    8.  Chamar `checar_fim_de_jogo` para verificar se o jogo terminou.
    9.  Se o estado for 'vitoria':
        - Imprimir a mensagem de vitória, revelando a palavra, e usar `break` para sair do loop.
    10. Se o estado for 'derrota':
        - Imprimir a mensagem de derrota, revelando a palavra, e usar `break`.
    11. Se o estado for 'continua', o loop prossegue para a próxima rodada.
    """
    # (passo 1) Seleciona a palavra secreta.
    palavra_secreta = obter_palavra_secreta()
    # (passo 2) Inicializa as variáveis de controle do jogo.
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 6

    # (passo 3) Loop principal do jogo.
    while True:
        # (passo 4) Exibe o estado atual do jogo.
        print("\n--- Jogo da Forca ---")
        display = exibir_palavra_mascarada(palavra_secreta, letras_corretas)
        print(f"Palavra: {display.upper()}")
        print(f"Letras erradas: {sorted(list(letras_erradas))}")
        print(f"Tentativas restantes: {tentativas}")

        # (passo 5) Pede a entrada do jogador.
        letra_digitada = input("Digite uma letra: ")

        # (passo 6) Valida a entrada.
        valida, mensagem = validar_letra(letra_digitada, letras_corretas, letras_erradas)
        if not valida:
            print(mensagem)
            continue
        
        letra_normalizada = letra_digitada.lower()

        # (passo 7) Processa a jogada.
        tentativas = processar_jogada(
            letra_normalizada, palavra_secreta, letras_corretas, letras_erradas, tentativas
        )
        
        # (passo 8) Verifica o fim do jogo.
        estado_jogo = checar_fim_de_jogo(palavra_secreta, letras_corretas, tentativas)

        if estado_jogo == 'vitoria':
            # (passo 9) Exibe a mensagem de vitória.
            print(f"\nParabéns, você venceu! A palavra era: '{palavra_secreta.upper()}'.")
            break
        elif estado_jogo == 'derrota':
            # (passo 10) Exibe a mensagem de derrota.
            print(f"\nVocê perdeu! A palavra era: '{palavra_secreta.upper()}'.")
            break
        # (passo 11) O jogo continua se o estado for 'continua'.

# Inicia o jogo quando o script é executado.
if __name__ == '__main__':
    jogar()
