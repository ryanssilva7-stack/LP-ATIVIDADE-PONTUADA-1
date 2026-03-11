import os
os.system("cls")

# dados
print("Escolha o combustivel pelos códigos G (gasolina) ou A (álcool)")
combustivel = input("Combustível: ").upper()
litros = int(input("Litros:"))

# processamento
if combustivel == "G" and litros >= 25:
    valor = 0.03 * (litros * 6.59)

elif combustivel == "G" and litros <= 25:
    valor = 0.05 * (litros * 6.59)

elif combustivel == "A" and litros >= 25:
    valor = 0.04 * (litros * 3.79)

elif combustivel == "A" and litros <= 25:
    valor = 0.02 * (litros * 3.79)


arredondar = round(valor,2)

# saida
print (f"Valor: R${arredondar}")
