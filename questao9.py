import os
os.system ("cls")

# dados
renda = float(input("Digite sua renda mensal: "))
emprestimo = float(input("Digite quanto de emprestimo você precisa: "))
prestacao = int(input("Quantas prestações pretende pagar: "))
# processamento dos dados
parcela = emprestimo / prestacao
valor_total_do_emprestimo = renda * 10
valor_da_prestacao = (renda * 0.3)

# resultado
if emprestimo >= valor_total_do_emprestimo and parcela >= valor_da_prestacao:
    print("\nO empréstimo pode ser concedido.")
else:
    print("\nO empréstimo não pode ser concedido.")
