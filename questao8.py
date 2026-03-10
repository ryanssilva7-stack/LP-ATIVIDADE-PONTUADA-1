import os
os.system ("cls")

# dados
print("""
------------ CD'S DA LOJA ------------
   Cores                       Preços
                    
  Verde                       R$ 10,00
  Azul                        R$ 20,00
 Amarelo                      R$ 30,00
Vermelho                      R$ 40,00
      """)


cor = input("Cor do CD: ").lower()
# processamento dos dados
match cor:
    case "verde":
        print(f"O CD {cor} está por R$ 10,00")
    case "azul":
        print(f"O CD {cor} está por R$ 20,00")
    case "amarelo":
        print(f"O CD {cor} está por R$ 30,00")
    case "vermelho":
        print(f"O CD {cor} está por R$ 40,00")
    case _:
        print("\nCor de CD inválido.")

# resultado
