"""
Módulo responsável por controlar o jogador: posição e pontuação.
"""

def iniciar_jogador():
    """
    Define posição inicial e pontuação.
    """
    return {"posicao": [0, 0], "pontos": 0}

def mover(jogador, direcao, tamanho):
    """
    Move o jogador no labirinto com base na direção informada.
    """
    x, y = jogador["posicao"]

    match direcao:
        case "w":  # cima
            x = max(0, x - 1)
        case "s":  # baixo
            x = min(tamanho - 1, x + 1)
        case "a":  # esquerda
            y = max(0, y - 1)
        case "d":  # direita
            y = min(tamanho - 1, y + 1)
        case _:  # inválido
            print("Movimento inválido.")

    jogador["posicao"] = [x, y]
    return jogador

def pontuar(jogador, labirinto):
    """
    Atualiza a pontuação se o jogador encontrar um ponto livre.
    """
    x, y = jogador["posicao"]
    if labirinto[x][y] == ".":
        jogador["pontos"] += 1
        labirinto[x][y] = "@"
    return jogador
