import os
os.system ("cls")

# dados
print("""
--------- produtos da loja ---------
                              Valor
Sabão                       R$  6,50
Detergente                  R$ 13,99
Lubrificante                R$ 19,99
Toalha de mesa              R$ 24,60
      """)


nome = input("Produto: ").lower()
unidade = int(input("Quantas unidades deseja: "))
desconto = int
# processamento dos dados
match nome:
    case "sabão":
        total = unidade * 6.50
    case "detergente":
        total = unidade * 13.99
    case "lubrificante":
        total = unidade * 19.99
    case "toalha de mesa":
        total = unidade * 24.60
    case _:
        print("\nproduto inválido.")

if unidade <= 5:
    desconto = total * 0.02
elif unidade > 5 and unidade <= 10:
    desconto = total * 0.03 
elif unidade > 10:
    desconto = total * 0.05

total_a_pagar = total - desconto
arredondar = round(total_a_pagar, 2)
arredondar2 = round(total, 2)
# resultado
print(f"\nValor orignal: R${arredondar2}")
print(f"Valor com desconto: R${arredondar}")