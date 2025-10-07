import random

numero =random.randint(1,10)

A=0
tentativa=0

while (A!=numero):
    
    A=int(input("insira um numero de 1 a 10\n"))
    tentativa+=1
print("o numero de tentativas foi",tentativa)