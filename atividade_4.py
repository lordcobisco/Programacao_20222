habit_animal=(input("O animal está habituado ao ambiente? s/n"))
distancia=30
contagem_de_toques = 0
cent_aproximados=int(input("O animal se aproximou da barra quantos centímetros? "))
distancia_2= cent_aproximados-distancia 
#ii
if (distancia_2<30):
    print("Liberar 0.5 de rec")
#iii
barra=input("A barra foi tocada pelo animal? s/n") #01 tentativa
if (barra=='s'):
     print("Liberar 0.5 de rec")
     contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #02 tentativa
if (barra=='s'):
     print("Liberar 0.5 de rec")
     contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #03 tentativa
if (barra=='s'):
     print("Liberar 0.5 de rec")
     contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #04 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
    print(contagem_de_toques)
barra=input("A barra foi tocada pelo animal? s/n") #05 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #06 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #07 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #08 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #09 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #10 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #11 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #12 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #13 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #14 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #15 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #16 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #17 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #18 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #19 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
barra=input("A barra foi tocada pelo animal? s/n") #20 tentativa
if (barra=='s'):
    print("Liberar 0.5 de rec")
    contagem_de_toques +=1
else:
    print("repetir até que ela seja tocada")
    contagem_de_toques +=1
print(contagem_de_toques)
if (contagem_de_toques==20):
        print("Parabéns! Avançe para a próxima etapa do experimento")
else:
    exit()
print("Etapa de discriminação auditiva")
som=int(input("Que som você irá tocar? 1/2:"))
barra=int(input("Qual barra o animal apertou? 1/2"))
if (som==1 and barra=='s'):
    print("Liberar 0.5ml de recompensa")
elif(som==2 and barra==2):
    print("Liberar 0.5ml de recompensa")
else:
    print("Não liberar recompensa")
tempo=int(input("Informe a duração do experimento:"))
quantidade=int(input("Informe a quantidade de vezes em que a barra foi apertada:"))
if(tempo>30 and quantidade==50):
    print("Parabéns! Você passou para a proxima fase!!")
else: 
    print("Não passou para a proxima fase! Tente novamente!")