from decimal import InvalidOperation
from tkinter import N

#Habituação

habituação=0
habituação=int(input('a habituação foi feita? 0(não) 1 (sim:'))

if habituação==0:
    print ('o animal não foi habituado')
elif habituação==1:
    print ('habituação realizada')
    habituação=1
alse:
print('incorreto')

aproximxação= 0
if habituação==1:
    aproximxação=30
    sagui= float(input('qual a distaância em cm?'))# colocar a distância 

    if sagui>0 and sagui <=aproximxação:
        print('0,5ml liberado')
        aproximxação=1
    elif sagui==0
        print('nada liberado')
    else:
        print('incorreto')

toque= 0
if aproximxação==1:
    toque =int(input(' o sagui tocou na barra 20x? 0 (n) 1(s):'))
    if toque== 0
    print('o animal não passou para a próxima etapa')
elif toque==1:
    print('o animal passou para a próxima etapa')
    toque=1
else:
    print('invalido')

som= 0
if toque==1:
    print('parabén, você esta no fim')
    print('você tem quatro opções')
    print('1-Phi')
    print('2 treinado')
    print ('3 esquerda')
    print('4 direita')
    som = int(input('qual som tocou:'))
    barra= int(input('qual bairra foi tocada:'))
    
if som ==1 and barra == 3
    print =('parabén você foi recompensado!')
    som =1
elif som ==2 and barra==4:
    print('parabéns, você foi recompensado')
else:
    print=('repetir teste')

# finalizando o experimento 

if som==1:
    tempoMinuto=int(input('o experimento foi realizado 50x em 30min?:s/n'))
    if tempoMinuto==0
    print('experimento não finalizado')
elif tempoMinuto== 1:
    print('experimento finalizado')
else:
    print('invalido')













