def verificar_primo(n, divisor=None):
    if n < 2:
        return False

    if divisor is None:
        divisor = 2

    if divisor * divisor > n:
        return True

    if n % divisor == 0:
        return False

    return verificar_primo(n, divisor + 1)

try:
    numero = int(input("Digite um número para verificar se é primo: "))
    
    if verificar_primo(numero):
        print(f"{numero} é um número primo!")
    else:
        print(f"{numero} não é um número primo.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
