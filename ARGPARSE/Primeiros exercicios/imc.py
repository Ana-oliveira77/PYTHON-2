import argparse

# Minha criação de teste do parser para compreender melhor na prática

parser = argparse.ArgumentParser(description= "Calculadora de IMC")

parser.add_argument ("peso", type=float, help= "Seu peso em kg" )
parser.add_argument ("altura", type=float, help= "Sua altura em metros")


args = parser.parse_args()

imc= args.peso / (args.altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
        print("Classificação: Abaixo do peso")
elif imc < 25:
        print("Classificação: Peso normal")
elif imc < 30:
        print("Classificação: Sobrepeso")
else:
        print("Classificação: Obesidade")