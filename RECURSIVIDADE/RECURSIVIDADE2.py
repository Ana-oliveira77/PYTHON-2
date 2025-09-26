
a= int(input("Digite o primeiro número: "))
b= int(input("Digite o segundo número: "))



def imprime_intervalo(a, b):


    if a > b:
        print("Valores invalidos")
        return

    if a == b:
        print(a, end ='')

    else: 
        imprime_intervalo (a+1, b)
        print(a, end ='')



imprime_intervalo (a , b)
