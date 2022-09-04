'''
a) Crie as variáveis necessárias para que o programa funcione corretamente.
b) Inicialize as variáveis com valores padrão adequados.
'''
celula = 'neurais'
resolucao = '1000x'
modelo = 'eletronico de varredura'
voltagem = '220'
digital = 's'
medida = 'nm'
lente = 'objetiva'
fonte_luz = 'P2000'
cor = 'preto'
faixa_luz = '150'

# c) Crie uma pequena mensagem de apresentação do programa para realizar uma
# interface com o usuário. Ex.: “Esse programa tem como objetivo receber dados para ...”
print('Esse programa tem como objetivo receber dados para configurar o microscópio')

'''
d) Solicite algumas informações necessárias para a configuração de um microscópio
 dessa natureza. Buscar pelo menos 10 itens para essas informações de entrada.
 Ex.: resolução da imagem desejada, tipo de célula a ser escaneada, faixa de iluminação necessária.

e) Para cada informação digitada, apresente na tela a seguinte mensagem:
 “Houve alteração na variável inserida?”. Após a mensagem, apresentar verdadeiro ou falso
 com base no que foi digitado pelo usuário e o que estava armazenado na variável. Obs.: Não deve ser utilizado if aqui
 '''
qualcelula = input('Quais células serão analisadas?')
alteracao = input('Houve alteração na variável inserida?(s/n)')
print((alteracao == 's' and qualcelula!=celula) or (alteracao == 'n' and qualcelula==celula))

qualresolucao = input('Qual a resolução da imagem?')
alteracao=input('Houve alteração na variável inserida?(s/n)')
print((alteracao == 's' and qualresolucao!=resolucao) or (alteracao == 'n' and qualresolucao==resolucao))

qualmodelo = input('Qual modelo do microscopio? ')
alteracao=input('Houve alteração na variável inserida?(s/n)')
print((alteracao == 's' and qualmodelo!=modelo) or (alteracao == 'n' and qualmodelo==modelo))

qualvoltagem = input('Qual a voltagem do microscopio? (s)')
alteracao=input('Houve alteração na variável inserida?(s/n)')
print((alteracao=='s' and qualvoltagem!=voltagem) or (alteracao=='n' and qualvoltagem==voltagem))

qualdigital = input('O microscopio é digital?')
alteracao=input('Houve alteração na variável inserida?(s/n)')
print((alteracao=='s' and qualdigital!=digital) or (alteracao=='n' and qualdigital==digital))

qualmedida = input('Qual a medida do microscopio')
alteracao=input('Houve alteração na variável inserida?(s/n)')
print((alteracao=='s' and qualmedida!=medida) or (alteracao=='n' and qualmedida==medida))

quallente = input('Qual a lente do microscopio?')
alteracao=input('Houve alteração na variável inserida?(s/n)')
print((alteracao=='s' and quallente!=lente) or (alteracao=='n' and quallente==lente))

qualfonte_luz = input('Qual a fonte de luz do microscopio')
alteracao=input('Houve alteração na variável inserida?(s/n)')
print((alteracao=='s' and qualfonte_luz!=fonte_luz) or (alteracao=='n' and qualfonte_luz==fonte_luz))

qualcor = input('Qual a cor do microscopio?')
alteracao=input('Houve alteração na variável inserida?(s/n)')
print((alteracao=='s' and qualcor!=cor) or (alteracao=='n' and qualcor==cor))

qualfaixa_luz = input('Qual a faixa de luz do microscopio?')
alteracao=input('Houve alteração na variável inserida?(s/n)')
print((alteracao=='s' and qualfaixa_luz!=faixa_luz) or (alteracao=='n' and qualfaixa_luz==faixa_luz))

'''
f) Retorne ao usuário de forma organizada as informações que foram digitadas.
Ex.: “As informações de configurações setadas pelo usuário são: ...”
'''
print('As informações de configurações setadas pelo usuário são:')
print("celula = ", qualcelula)
print("resolucao = ", qualresolucao)
print("modelo = ", qualmodelo)
print("voltagem = ", qualvoltagem)
print("digital = ", qualdigital)
print("medida = ", qualmedida)
print("lente = ", quallente)
print("fonte_luz = ", qualfonte_luz)
print("cor = ", qualcor)
print("faixa_luz = ", qualfaixa_luz)

'''
g) Após setada as configurações iniciais o usuário deve utilizar dois caracteres
para a calibração do equipamento no sentido horizontal. Para isso, ele deve apertar
a tecla correspondente à primeira letra do seu nome 10x e à última letra do seu nome 10x.

h) Imediatamente após apertar a tecla o programa deve apresentar na tela que
a informação foi corretamente digitada e mostrar o caractere pressionado.
'''
primeiraletra = input('Aperte 10x a tecla correspondente à primeira letra do seu nome: ')
ultimaletra = input('Aperte 10x a tecla correspondente à ultima letra do seu nome: ')
retorno = print('A informação foi digitada corretamente!', primeiraletra, ultimaletra)

'''
i) Na sequência o usuário deve utilizar dois caracteres para a calibração do equipamento
no sentido vertical. Para isso, ele deve apertar a tecla correspondente à segunda
letra do seu nome 10x e à penúltima letra do seu nome 10x.

j) Imediatamente após apertar a tecla o programa deve apresentar na tela que
a informação foi corretamente digitada e mostrar o caractere pressionado.
'''
segundaletra = input('Aperte 10x a tecla correspondente à segunda letra do seu nome: ')
penultimaletra = input('Aperte 10x a tecla correspondente à penultima letra do seu nome: ')
retorno = print('A informação foi digitada corretamente!', segundaletra, penultimaletra)
# k) Finalmente, o programa deverá apresentar na tela que houve o término da calibração do sistema.
print('Término da calibração do sistema')