
# Lê e valida a altura.
while True:
    try:
        at = float(input("Insira a sua altura em metros (ex: 1.75)\n"))
        if at <= 0:
            print("Tem de ser maior que zero.")
        elif at > 3:
            print("Use metros (ex: 1.75).")
        elif at < 1.0:
            print("Altura inválida.")
        else:
            break
    except:
        print("Introduza a altura em metros (ex: 1.75).")

# Lê e valida o peso.
while True:
    try:
        kg = float(input("Insira o seu peso em kg (ex: 70)\n"))
        if kg <= 0:
            print("Tem de ser maior que zero.")
        elif kg > 300:
            print("Peso inválido.")
        elif kg < 25:
            print("Peso inválido.")
        else:
            break
    except:
        print("Introduza o peso em kg (ex: 70).")

# Calcula o IMC.
imc = kg / (at * at)
imc = round(imc, 2)

# Mostra a categoria do IMC.
if imc < 18.5:
    print("abaixo do peso")
if imc >= 18.5 and imc < 24.9:
    print("peso normal")
if imc >= 25 and imc < 29.9:
    print("excesso de peso")
if imc >= 30:
    print("obesidade")

# Mostra o IMC final.
print("o seu imc é de", imc)