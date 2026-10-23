
excelente = 0
bom = 0
ruim = 0

for i in range(1, 51):
    print(f"\nEntrevistado {i}")

    idade = input("Qual é sua idade? ")
    nome = input("Qual é seu nome? ")

    opiniao = input(
        "Digite 1 para Excelente, 2 para Bom e 3 para Ruim: "
    )

    if opiniao == "1":
        print("Você avaliou o produto como: Excelente")
        excelente += 1

    elif opiniao == "2":
        print("Você avaliou o produto como: Bom")
        bom += 1

    elif opiniao == "3":
        print("Você avaliou o produto como: Ruim")
        ruim += 1

    else:
        print("Opinião inválida!")

print("\n--- RESULTADO FINAL ---")
print("Excelente:", excelente)
print("Bom:", bom)
print("Ruim:", ruim)
