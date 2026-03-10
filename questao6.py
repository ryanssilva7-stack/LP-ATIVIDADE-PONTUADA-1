import os
os.system ("cls")

# dados
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

# processamento dos dados
media = (nota1+nota2) / 2

# resultado
if media >= 6:
    print("\nAprovado, parabéns!")
elif media >= 4:
    print("\nEm recuperação.")
elif media < 4:
    print("\nReprovado.")

print(f"\n{media}")