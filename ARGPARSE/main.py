import argparse
from personalizador import painel, estilo

modulos = {
    "painel": painel,
    "estilo": estilo
}

funcoes = {
    "painel": ["painel_simples", "painel_alerta"],
    "estilo": ["negrito", "verde"]
}

def main():
    parser = argparse.ArgumentParser(description="Programa com rich")
    parser.add_argument("texto", help="Texto ou caminho de arquivo")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Se for arquivo")
    parser.add_argument("-m", "--modulo", required=True, choices=modulos.keys())
    parser.add_argument("-f", "--funcao", required=True)

    args = parser.parse_args()

    if args.funcao not in funcoes[args.modulo]:
        print("Funções válidas:", funcoes[args.modulo])
        return

    modulo = modulos[args.modulo]
    funcao = getattr(modulo, args.funcao)
    funcao(args.texto, args.arquivo)

if __name__ == "__main__":
    main()
