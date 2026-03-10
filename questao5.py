import os
os.system ("cls")

# dados
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um segundo número: "))
codigo = (input("Escolha um código de operação: "))
# processamento dos dados
match codigo:
    case "-":
        resultado = numero1-numero2
    case "+":
        resultado = numero1+numero2
    case "*":
        resultado = numero1*numero2
    case "/":
        resultado = numero1/numero2
    case _:
        print("\ncódigo de operação inválido.")

# resultado
print(f"\nO resultado é igual a {resultado}")