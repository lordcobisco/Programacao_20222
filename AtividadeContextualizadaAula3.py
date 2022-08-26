#Exercício da aula 3

#variáveis
valueFaixaDetec = 250  
  #medido em nm
valuePixels = '40x40' 
  #resolução do microscópio em pixels
valueAngIncidencia = 30 
valueFaixaLuz = '5.05' 
  #Faixa de iluminação desejada
  #valor em graus
valueLimResol = 0.584 
  #medido em μm 
  #limite da resolução desejada
valueMaxIntensi = 1.05 break
valueMinIntensi = 2.05
valueProfFundo = 8.05
modelMicro = 'MaMin' 
  #Modelo de microscópio confocal
tipoCelula = 'Cerebral'


#Mensagem 1
print('Olá! Bem vindo ao MicroFoc.')
print('Este programa tem o objetivo de receber os dados do usuário para a configuração de um microscópio confocal.')

    #Primeira etapa
    #Inicialmente, o usuário deverá indicar todos os valores de cada variável.
    #Se houver alteração no valor padrão, o programa indicará ao final de cada pergunta.
valueFaixaDetec2 = input('Insira a faixa do detector, em nm:')
print('Houve alteração da faixa do detector?',int(valueFaixaDetec) != int(valueFaixaDetec2))

valuePixels2 = input('Insira a resolução do microscópio confocal, em pixels:')
print('Houve alteração da resolução?',str(valuePixels) != str(valuePixels2))

valueAngIncidencia2 = input('Insira o ângulo de incidência, em graus, do microscópio:')
print('Houve alteração do limite de resolução?',float(valueAngIncidencia) != float(valueAngIncidencia2))

valueFaixaLuz2 = input('Insira a faixa de iluminação desejada:')
print('Houve alteração nesta faixa de iluminação?',float(valueFaixaLuz) != float(valueFaixaLuz2))

valueLimResol2 = input('Insira o limite de resolução, em pixels:')
print('Houve alteração no limite de resolução?',float(valueLimResol) != float(valueLimResol2))

valueMaxIntensi2 = input('Insira o valor da intensidade no ponto mais alto do microscópio:')
print('Houve alteração do valor da intensidade no ponto mais alto?',int(valueMaxIntensi) != int(valueMaxIntensi2))

valueMinIntensi2 = input('Insira o valor da intensidade no ponto mais baixo do microscópio:')
print('Houve alteração do valor da intensidade no ponto mais baixo?',float(valueMinIntensi) != float(valueMinIntensi2))

valueProfFundo2 = input('Insira o valor do controle de profundidade de campo:')
print('Houve alteração na profundidade?',float(valueProfFundo) != float(valueProfFundo2))

modelMicro2 = input('Insira o modelo do microscópio utilizado:')
print('Houve alteração no modelo do microscópio?',str(modelMicro) != str(modelMicro2))

tipoCelula2 = input('Insira o tipo da célula que será estudada:')
print('Houve alteração no tipo da célula?',str(tipoCelula) != str(tipoCelula2))


    #Próxima etapa:
    #Retorno ao usuário sobre as informações por ele fornecidas:
print('As informações de configurações setadas pelo usuário estão apresentadas abaixo.')
print('A faixa do detector é:', valueFaixaDetec2)
print('A resolução escolhida do microscópio confocal é:', valueLimResol2)
print('O ângulo de incidência escolhido é:', valueAngIncidencia2)
print('A faixa de iluminação desejada é:', valueFaixaLuz2)
print('O o limite de resolução é:', valueLimResol2)
print('O valor da intensidade no ponto mais alto é:', valueMaxIntensi2)
print('O valor da intensidade no ponto mais baixo é:', valueMinIntensi2)
print('O valor do controle de profundidade de campo é:', valueProfFundo2)
print('O modelo do microscópio utilizado é:', modelMicro2)
print('O  tipo da célula que será estudada é:', tipoCelula2)


    #Próxima etapa: calibração horizontal
    #O usuário irá apertar a tecla correspondente à primeira letra do seu nome 10x e à última letra do seu nome 10x.

valuePrimeiraL = 'KKKKKKKKKK'
valueUltimaL = 'EEEEEEEEEE'

print('Vamos realizar a calibração horizontal.')
print('Você deve pressionar a primeira letra do seu nome 10 vezes e, depois, pressionar a última letra do seu nome 10 vezes.')

valuePrimeiraL2 = input('Pressione a primeira letra do seu nome 10 vezes (com o caps ativado) e confirme:')
print(str(valuePrimeiraL) == str(valuePrimeiraL2))
print(valuePrimeiraL2)

valueUltimaL2 = input('Pressione a última letra do seu nome 10 vezes (com o caps ativado) e confirme:')
print(str(valueUltimaL) == str(valueUltimaL2))
print(valueUltimaL2)
print('Próxima etapa.')


    #Próxima etapa: calibração vertical
    #O usuário irá apertar a tecla correspondente à segunda letra do seu nome 10x e à penúltima letra do seu nome 10x.

valueSegundaL = 'AAAAAAAAAA'
valuePenultL = 'NNNNNNNNNN'

print('Agora, vamos realizar a calibração vertical.')
print('Você deve pressionar a segunda letra do seu nome 10 vezes e, depois, pressionar a penúltima letra do seu nome 10 vezes.')


valueSegundaL2 = input('Pressione a segunda letra do seu nome 10 vezes (com o caps ativado) e confirme:')
print(str(valueSegundaL) == str(valueSegundaL2))
print(valueSegundaL2)

valuePenultL2 = input('Pressione a penúltima letra do seu nome 10 vezes (com o caps ativado) e confirme:')
print(str(valuePenultL) == str(valuePenultL2))
print(valuePenultL2)

    #Finalização
print('Calibração concluída com sucesso.')
print('Muito obrigada.')
break