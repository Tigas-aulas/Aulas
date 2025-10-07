at=float(input("insira a sua altura\n"))
kg=int(input("insira o seu peso\n"))

imc=kg/(at*at)

if(imc<18.5):
    print("abaixo do peso")
if(imc<=18.5 and imc<24.9):
    print("peso normal")
if(imc>=25 and imc<29.9):
    print("excesso de peso")
if(imc>30):
    print("obesidade")

print(imc)