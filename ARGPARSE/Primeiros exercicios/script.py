#import sys

#args = sys.argv
#print('Nome do script:', args [0])
#print('Outros argumentos:', args [1:])

import argparse

parser = argparse.ArgumentParser(description="Programa que cumprimenta")

parser.add_argument("nome", help="Seu nome")  # argumento obrigatório
args = parser.parse_args()

print(f"Olá, {args.nome}!")
