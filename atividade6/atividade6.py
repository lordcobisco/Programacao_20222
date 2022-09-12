# -*- coding: utf-8 -*-
"""
***Seja o seguinte procedimento cirúrgico:***


1. Procedimento de anestesia: Pode-se utilizar uma diversidade de fármacos para anestesia os animais, dentre eles Ketamina e xilazina utilizados em conjunto, halotano (gasoso). Verificar a dosagem correta de acordo com o peso dos animais.
2. Depois do anestésico ter feito efeito, deve-se posicionar o animal no estereotáxico. As barras que suportam o peso do animal devem ser posicionadas no ouvido externo do animal. Normalmente o animal dá uma pequena piscada, devido ao estímulo da musculatura responsável por este movimento. Em seguida verificar a angulação da cabeça do animal, a qual deve estar sem diferenças de angulação entre o bregma e o lambda, para ter uma superfície de cirurgia plana.
3. Limpeza do campo de trabalho: Este procedimento requer o cumprimento de algumas etapas: Retirada da pelagem que recobre a parte superior da calota craniana, Retirada dos tecidos moles (epiderme, derme e tecido conjuntivo) até alcançar a parte óssea da caixa craniana. Por último e não menos importante deve-se limpar a calota craniana de qualquer resto de “pele” que esteja sobrando utilizando H2O2 10 volumes.
4. Com o animal em posição e com o campo cirúrgico devidamente limpo, utiliza-se uma pequena camada de poliacrilato em todo o perímetro externo para evitar sangramentos.
5. Após este procedimento deve-se escolher um ponto para a fixação de parafusos, de preferência na parte posterior da calota craniana, pois a camada óssea é mais espessa e suporta uma maior profundidade do parafuso. 

Obs: Cuidar para não aprofundar muito o parafuso. Com parafusos maiores deve-se dar até 3 voltas no parafuso.
>> Posicionar a agulha (devidamente preparada para o tamanho da cânula e que servirá de suporte para a fixação das cânulas) sobre o bregma (ver figura acima). Fazer os cálculos de posicionamento AnteroPosterior (AP), LateroLateral (LL) e DorsoVentral (DV). Os valores utilizados para os cálculos são os valores encontrados nas réguas a partir do posicionamento da agulha.

>> E. G.: Hipocampo (CA1): Valores hipotéticos para fins de cálculo.

>> AP: 6,42 cm 

>> LL: 3,23 cm

>> DV: 4,2 cm

>> Isso significa que estes foram os valores encontrados em cada régua do estereotáxico e se subtrai ou soma a estes, os valores de cada estrutura ou núcleo. CA1: AP - 0,42 cm LL +/- 0,30 cm DV - 0,20 cm.

>> AP: 6,42 cm – 0,42 = 6,00

>> LL: 3,33 cm + 0,30 = 3,63 / - 0,30 = 3,03  (BILATERAL)

>> DV: 4,20 cm – 0,20 = 4,00

6. Após estes cálculos feitos é hora de localizar os pontos de inserção das cânulas-guia. Assim que estes pontos forem localizados é necessário fazer furos para a introdução das cânulas-guia. A localização destes pontos deve ser definida pelos valores encontrados nos cálculos AnteroPosterior (6,00) e LateroLateral (3,63 e 3,03). Deve-se escolher qual dos hemisférios vai ser colocada a primeira cânula, daí os dois valores para as medidas LL.
7. Depois de posicionar a agulha, fazer um furo com a broca até alcançar as meninges. A não perfuração das meninges é o procedimento ideal, e para conseguir isso apoie a mão que segura a broca contra o assoalho ou ao estereotáxico e perfure o crânio a +- 450 de angulação.
8. Após ter atingido este objetivo, introduza a cânula-guia previamente confeccionada até o valor DorsoVentral (4,00) que foi calculado anteriormente.
9. Logo após drenar qualquer sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado no crânio. Para isso utilize pequenos rolos de papel absorvente.
10. Faça uma mistura do acrílico polimerizante com o solvente até ficar com textura espessa porém maleável (o ideal é que a mistura seja capaz de cobrir a parte desejada sem escorrer por todo o crânio). Com essa mistura faça um capacete abrangendo o crânio, a cânula-guia e o parafuso. Deixe secar até ficar suficientemente rígido. O tempo de secagem varia de acordo com a temperatura e umidade da sala. 
11. O próximo passo é a fixação da outra cânula-guia. Deve-se levantar levemente o braço do estereotáxico cuidando para que a cânula-guia previamente fixada não se movimente. Logo após, posicionar a agulha sobre o outro ponto de inserção da cânula-guia. Introduzir a cânula-guia até o valor DV (4,00) calculado previamente.
12. Seguir novamente a descrição do item 9 e após fixar a cânula conforme item 10. De preferência espalhar o cimento sobre a maior área do crânio, sempre deixando um espaço entre o capacete e o início da área tecidual. Este cuidado previne de um futuro descolamento do capacete devido a entrada de sangue u outro líquido entre o capacete e o crânio.
11. Levantar bem devagar seguindo as instruções do item contida no item 11. Acomodar o animal em uma caixa aquecida por uma lâmpada e sem outros animais acordados. Assim que o animal despertar colocá-lo de volta a sua caixa-moradia.

***Desenvolva um programa em Python que automatize o procedimento cirúrgico apresentado, assumindo que:***

*   As entradas (seja informações de máquina, posicionamentos a serem medidos etc.) serão traduzidas em inputs no programa.
*   O detalhamento das etapas é informado na tela para o usuário a cada passo do procedimento.
*   O programa deve conter estruturas de tomada de decisão (if-elif-else).
*   O programa deve conter estruturas de repetição (while-for).
*   O programa deve conter pelo menos 1 variável de cada tipo (lista, tupla e dicionário)

Procedimento de anestesia
"""

while(True):
  
  procedimentoAnestesia = input('Qual o tipo de fármaco utilizado? ')
  pesoAnimal = input('Qual o peso do animal? ')
  dosagem = float(input('Qual a dosagem do anestesico de acordo com o peso do animal? '))
  informacoes = input('Todas as informações estão corretas? (s/n) ')  
    
  if informacoes == 's':
      print('Aguarde o fármaco fazer efeito, e siga para próxima etapa.')
      break
  else:
      continue

"""Posicionamento"""

while(True):
  
  print('As perguntas devem ser respondidas com "s" para sim ou "n" para não.')

  farmacoEfeito = input('O farmáco fez efeito? ')
  if farmacoEfeito == 's':
    print('Posicione o animal no estereotáxico.')
  else:
    print('Aguardar o farmáco fazer efeito, se necessário refaça a dosagem do anestesico.')
    continue
  
  posicionamento = input('O animal está posicionado corretamente no estereotáxico? ')
  if posicionamento == 's':
    print('Não há diferenças de angulação entre o bregma e o lambda. Seguir para a próxima etapa.')
    break
  else:
    print('Verificar a angulação da cabeça do animal. ')
    continue

"""Limpeza do campo de trabalho"""

print('As perguntas devem ser respondidas com "s" para sim ou "n" para não.')
lista = []
while(True):
  
  retirarPelagem = input('Foi realizada a retirada da pelagem que recobre a parte superior da calota craniana? ')
  retirarTecidosMoles = input('Foi realizada a retirada dos tecidos moles até alcançar a parte óssea da caixa craniana? ')
  if retirarPelagem == 's' and retirarTecidosMoles == 's':
    print('Limpar a calota craniana com H2O2.')
    for i in range(10):
      lista.append('Volume '+ str(i+1))
    print(lista)
    print('Limpeza devidamente realizada seguir para a próxima etapa.')
    break
  else:
    print('Refazer procedimentos.')
    continue

"""Camada de poliacrilato """

while(True):
  
  limpeza = input('O campo cirúrgico está devidamente limpo? ')
  
  if posicionamento == 's' and limpeza == 's':
     print('Colocar camada de poliacrilato em todo perémetro externo para evitar sangramentos.')
     print('Seguir para próxima etapa.')
     break
  else:
     print('Refazer procedimentos.')
     continue

"""Ponto para a fixação de parafusos"""

print('Adicione as informações para realização do cálculo do ponto de fixação dos parafusos.')

referenciaAP = float(input('Adicione a coorenada de referência AnteroPosterior (AP): '))
referenciaLL = float(input('Adicione a coorenada de referência LateroLateral (LL): '))
referenciaDV = float(input('Adicione a coorenada de referência DorsoVentral (DV): '))

pontosReferencia = (referenciaAP, referenciaLL, referenciaDV)

coordenadaAP = float(input('Adicione a distância AnteroPosterior (AP): '))
coordenadaLL = float(input('Adicione a distância de referência LateroLateral (LL): '))
coordenadaDV = float(input('Adicione a distância de referência DorsoVentral (DV): '))

coordenada = (coordenadaAP, coordenadaLL, coordenadaDV)

Novo_AP = pontosReferencia[0] + coordenada[0]
Novo_LL1 = pontosReferencia[1] + coordenada[1]
Novo_LL2 = pontosReferencia[1] - coordenada[1]
Novo_DV = pontosReferencia[2] + coordenada[2]

pontosFixacao = {'AP': Novo_AP, 'LL1': Novo_LL1, 'LL2': Novo_LL2, 'DV': Novo_DV}
print('Os pontos para fixação dos parafusos são: ', pontosFixacao)
print('Seguir para próxima etapa.')

"""Localizar os pontos de inserção das cânulas-guia"""

while(True):

  a = float(input('Insira a posição do AP: '))
  if a == pontosFixacao['AP']:
    print('Agulha posicionada corretamente.')
  else:
    print('Insira o valor correto.')
    continue

  canula = input('Em qual dos hemisférios vai ser colocada a primeira cânula? ')
  if canula == 'direito':
    b1 = float(input('Insira a posição do LL direito: '))
    if b1 == pontosFixacao['LL1']:
      print('Agulha posicionada corretamente.')  
    else:
      print('Insira o valor correto.')
    b2 = float(input('Insira a posição do LL esquerdo: '))
    if b2 == pontosFixacao['LL2']:
      print('Agulha posicionada corretamente.') 
    else:
      print('Insira o valor correto.')
      continue 

  if canula == 'esquerdo':
    b2 = float(input('Insira a posição do LL esquerdo: '))
    if b2 == pontosFixacao['LL2']:
      print('Agulha posicionada corretamente.') 
    else:
      print('Insira o valor correto.') 
    b1 = float(input('Insira a posição do LL direito: '))
    if b1 == pontosFixacao['LL1']:
      print('Agulha posicionada corretamente.')  
    else:
      print('Insira o valor correto.')
      continue

  print('Seguir para próxima etapa.')

"""Furo com a broca até alcançar as meninges."""

while(True):
  perfuracao = int(input('Insira o ângulo para perfuração: '))
  if perfuracao == 45:
    print('Realizar furo com a broca até alcançar as meninges.')
    break
  else:
    print('Insira o Ângulo correto.')
    continue

"""Introduza a cânula-guia"""

while(True):
  c = float(input('Insira a posição do DV: '))
  if c == pontosFixacao['DV']:
    print('Introduza a cânula-guia previamente confeccionada.') 
    break
  else:
    print('Insira o valor correto.')
    continue

"""Drenar sangue ou líquido cefalorraquidiano"""

liquido = input('Há sangue ou líquido cefalorraquidiano saindo pelo orifício criado no crânio? ')
if liquido == 's':
  print('Utilizar pequenos rolos de papel absorvente para drenar.')
else:
  print('Seguir para próxima etapa.')

"""Capacete """

print('Faça uma mistura do acrílico polimerizante com o solvente até ficar com textura espessa porém maleável.')
capacete = input('A mistura é suficiente para cobrir o crânio, a cânula-guia e o parafuso? ')

if capacete == 's':
  while(True):
    seco = input('O material do capacete está seco? ')
    if seco == 's':
       print('Seguir para o próximo passo.')
       break
    else:
      print('Esperar o material secar.')
      continue

"""Fixação da outra cânula-guia"""