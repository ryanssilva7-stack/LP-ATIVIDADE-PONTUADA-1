import os
os.system ("cls")

# dados
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um segundo número: "))

# processamento dos dados
if numero1 == numero2:
    resultado = numero1 + numero2
else:
    resultado = numero1 * numero2

# resultado
print(f"\nO resultado dos valores é igual a {resultado}")