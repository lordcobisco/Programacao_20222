#ATIVIDADE DA AULA 6 usando commit

#Método de discriminação de estímulos auditivos para primatas através do condicionamento operante.

varAnimalHab = str(input('o animal esta habituado?'))
if(varAnimalHab == 'sim'):
  print('iniciar coleta')
if (varAnimalHab == 'nao'):
  print('habituar animal')

prox=str(input('o animal se aprixou 30 cm?'))
if(prox=='sim'):
  print('colocar 0,5 ml de recompensa')
if(prox=='nao'):
  print('nao recebe comida')
quantasVezesTocou = int(input('quantas vezes o animal tocou na barra'))
if(quantasVezesTocou>20):
  print('passar proxima etapa')
if(quantasVezesTocou<20):
  print('nao avanca experimento')
print('SOM1ACIONADO')
barra=str(input('o animal tocou a barra direita ou barra esquerda'))
if(barra=='direita'):
  print('libera 0,5ml de alimento')
if(barra=='esquerda'):
  print('nao libera comida')
print('SOM2ACIONADO')
barra=str(input('o animal tocou a barra direita ou barra esquerda'))
if(barra=='direita'):
  print('libera 0,5ml de alimento')
if(barra=='esquerda'):
  print('nao libera comida')

print('quantas vezes o animal tocou na barra?')

contador = 0
while contador <51:
  print(contador)
  contador=contador+1

print('TEMPO DO EXPERIMENTO 30MIN')
TempoExperimento=int(input('quantas vezes o animal tocou a barra em 30mi?'))
if(TempoExperimento<=50):
  print('coletar dados experimento')
else:
  print('seguir proxima fase')