"""
Ponto de entrada do jogo. Controla a execução principal e CLI.
"""

import argparse
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import iniciar_jogador, mover, pontuar
from aventura_pkg.utils import menu_principal, imprime_instrucoes, animacao_vitoria

def main():
    parser = argparse.ArgumentParser(description="Jogo Aventura no Labirinto")
    parser.add_argument("--name", required=True, help="Nome do jogador")
    parser.add_argument("--color", default="cyan", help="Cor do texto principal")
    parser.add_argument("--dificuldade", choices=["facil", "medio", "dificil"], default="facil")
    parser.add_argument("--disable-sound", action="store_true", help="Desativa sons")
    parser.add_argument("--help-info", action="store_true", help="Mostra instruções")

    args = parser.parse_args()

    if args.help_info:
        imprime_instrucoes()
        return

    nome = args.name
    print(f"\nBem-vindo(a), {nome}! Prepare-se para o desafio!\n")

    while True:
        opcao = menu_principal()

        if opcao == "1":
            lab = criar_labirinto(5)
            jogador = iniciar_jogador()
            imprimir_labirinto(lab)

            while True:
                move = input("Movimento (W/A/S/D ou Q p/ sair): ").lower()
                if move == "q":
                    print("Saindo do jogo...")
                    break

                jogador = mover(jogador, move, len(lab))
                jogador = pontuar(jogador, lab)
                imprimir_labirinto(lab)

                x, y = jogador["posicao"]
                if lab[x][y] == "E":
                    animacao_vitoria()
                    print(f"Pontuação final: {jogador['pontos']}")
                    break

        elif opcao == "2":
            imprime_instrucoes()

        elif opcao == "3":
            print("Até logo!")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
