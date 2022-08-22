#AtividadeContextualizadaAula4
#Programa para habituação do animal

print('Olá! Bem vindo ao teste experimental da aula 4.')

habituação = str(input('O animal está habituado?'))
if (habituação=='sim'):
  print('Parabéns, vamos iniciar o teste.')
else:
  print('Treine o animal, ele precisa estar habituado. Não é bom passar para as próximas perguntas sem essa habituação.')

dist = str(input('O animal está com distância de 30 cm da barra?'))
if (dist=='sim'):
  print('Ele precisa se aproximar da barra.')
  print('Mas, vamos prosseguir.')
  #Aqui, em um programa real, eu não prosseguiria. Porém, como ainda não podemos usar outros comandos (como while) nesta atividade, prossegui para não ficar extenso. Em um programa, eu pediria para repetir a pergunta até que o animal estivesse mais próximo.
if (dist=='nao'):
  dist2 = int(input('Qual é a distância entre o animal e a barra?'))
  if dist2<30:
      print('Libere 0,5ml de suco.')
  else:
      print('Não libere suco.')

tbarra = str(input('O animal tocou alguma vez na barra?'))
if (tbarra=='sim'):
  tbarra2 = int(input('Quantas vezes o animal tocou na barra?'))
  if tbarra2>=20:
    print('Parabéns! O experimento passou para a próxima fase.')
  if tbarra2<20:
    print('O animal precisa tocar 20x na barra para que o experimento passe de fase.')
if (tbarra=='nao'):
    print('O animal precisa tocar na barra para prosseguir o experimento.')
    print('Tente novamente.')

som1 = str(input('Som 1 ativado. O animal tocou na barra esquerda?'))
if (som1=='sim'):
  print('Libere 0,5ml de suco.')
else:
  print('Não libere suco.')

som2 = str(input('Som 2 ativado. O animal tocou na barra direita?'))
if (som2=='sim'):
  print('Libere 0,5ml de suco.')
else:
  print('Não libere suco.')

pergfinal = int(input('Quantas vezes o animal tocou na barra durante 30min de experimento?'))
if pergfinal>50:
    print('Parabéns! O experimento passou para a próxima fase.')
if pergfinal<50:
    print('O animal precisa tocar 50x na barra, em 30min, para que o experimento passe de fase.')
