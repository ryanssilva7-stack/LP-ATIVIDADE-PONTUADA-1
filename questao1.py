import os
os.system ("cls")

# entrada
numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite um segundo valor: "))
numero3 = int(input("Digite um terceiro valor: "))

# prcoesso
soma = numero1 + numero2

# saida
if soma < numero3:
    print(f"{numero1} + {numero2} é menor que {numero3}")
else:
    print(f"{numero1} + {numero2} é maior que {numero3}")
