import os
os.system("cls")

# dados
fruta = input("Escolha uma fruta: ").lower()
kg = int(input("Indique quantos KG deseja: "))

# processo

if fruta == "morango" and kg <= 5:
    preco = 2.50
else:
    preco = 2.20
    
if fruta == "maçã" and kg <= 5:
    preco = 1.80
else:
    preco = 1.50

if preco > 15 or kg <= 10:
    print("\nDesconto de 10%")
    valor = (preco + kg) * 0.1
else:
    valor = preco + kg

arrendondar = round (valor, 2)

# saida
print(f"Valor á pagar: R${valor}")
