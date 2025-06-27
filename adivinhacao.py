#juan miguel n24 1°E
import random

import os 

erro=0
sorteando=random.randrage(0,100)
jogador=int(input("digite seu número!   "))
while(sorTeado!=jogador):
    os.system('cls')
    if(sorteado>jogador):
        PRINT("ERRO, o número é maior")
    elif(sorteado<jogador):
        print("ERRO, o número é menor")
    erros+=1
    jogador=int(input("digite seu número:  "))
print("número" = str(jogador) + " , você acertou em: "+ str(erros+1) + "tentativa")
