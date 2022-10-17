from random import randint


import random
veltracajas=[]
numtracaja=int(input("Insira o número de tracajás do grupo, entre 1 até 50: "))
if (numtracaja<1 or numtracaja>50):
    print("Valor inválido, escolha apenas números entre 1 até 50.")
else:
    for i in range(1,numtracaja+1):
        veltracajas.append(random.randint(1,25))
    for l in veltracajas:
        print(l)
    veltracajas.sort(reverse=True)
    if (veltracajas[0]<10):
        print("\n1.")
    if (veltracajas[0]>=10 and veltracajas[0]<15):
        print("\n2.")
    if(veltracajas[0]>=15):
        print("\n3.")