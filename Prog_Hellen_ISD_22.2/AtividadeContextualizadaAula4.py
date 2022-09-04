'''
a) Requisito 1: Habituação
1-Se o animal está habituado, registrar em uma variável
'''

habituacao=input('Houve Habituação?(s/n)')

'''
b) Requisito 2: Regime de aproximações sucessivas

1-Iniciar a variável com 30cm
'''
aproximacao=30

# 2-Se a variável de aproximação diminuiu (animal aproximou), liberar 0,5ml de rec
alteracao=float(input('Qual o valor da distancia entre o animal e a barra?(valor) '))
if alteracao<aproximacao:
  print('liberar 0,5ml de rec')

# 3-Se animal tocou na barra 20x, retornar que o experimento passou para a próxima etapa
contagem=int(input('Quantas vezes o animal tocou na barra?(numero) '))
if contagem>=20:
  print('O experimento passou para a próxima etapa')

# 4-Se o som1 foi emitido e o animal tocou na barra esquerda, c
toquesom1=input('O animal tocou na barra esquerda?(s/n) ')
if toquesom1 == 's':
  print('Liberar 0,5ml de rec')

# 5-Caso contrário não liberar nada
else:
  print('Não liberar nada')

# 6-Se o som2 foi emitido e o animal tocou na barra direita, liberar 0,5ml de rec
toquesom2=input('O animal tocou na barra direita?(s/n) ')
if toquesom2 == 's':
  print('Liberar 0,5ml de rec')

# 7-Caso contrário não liberar nada
else:
  print('Não liberar nada')

# 8-Se o experimento foi realizado 50x em 30min, apresentar que o experimento seguirá para a próxima fase.
total=input('O experimento foi realizado 50x em 30min?(s/n) ')
if total=='s':
  print('O experimento seguirá para a próxima fase')
