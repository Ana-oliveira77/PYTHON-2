def somatorio(n):
    return 1 if n == 1 else n + somatorio(n - 1)

n = int(input("Digite N: "))
print("A soma de", n, "até 1 é:", somatorio(n))
