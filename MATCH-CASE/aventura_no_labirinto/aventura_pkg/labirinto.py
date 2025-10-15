"""
Módulo responsável pela criação e impressão do labirinto.
"""

import random

def criar_labirinto(tamanho=5):
    """
    Cria um labirinto simples com paredes (#) e caminhos (.)
    """
    labirinto = []
    for _ in range(tamanho):
        linha = [random.choice([".", ".", ".", "#"]) for _ in range(tamanho)]
        labirinto.append(linha)

    # Garante início e fim livres
    labirinto[0][0] = "S"  # Start
    labirinto[-1][-1] = "E"  # Exit
    return labirinto

def imprimir_labirinto(labirinto):
    """
    Imprime o labirinto no terminal.
    """
    for linha in labirinto:
        print(" ".join(linha))
