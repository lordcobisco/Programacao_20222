#variaveis 
from cgi import print_directory


faixaDetector=40
fluorForo= 'dapi'
laser=453
lentes= 6 
ganho=568
resolução='1024x1024'
bitProfundidade= 14
xIluminaçao='sim'#luz ligada 1
yiluminação='sim'#luz ligada 2

breakpoint()
#começar
print('Esse programa tem como objetivo receber dados para ajustar a configuração microscopica')

#fornecendo os dados 
faixaDetector2=(input('digite a faixa do detector:'))
print('houve mudança na variável', faixaDetector!=faixaDetector2)

fluorForo2=input('digite o fluoróforo que vai ser usado:')
print('houve mudança nessa variável?', fluorForo!=fluorForo2)

laser2=int(int('digite qual o laser que vai ser usado'))
print ('houve mudança na variável?', laser!=laser2)

lentes2= int(input('digite as lentes a serem usadas:'))
print('houve mudança na variável?', lentes!=lentes2)

ganho2=int(input('digite qual foi o ganho:'))
print('houve mudança na variável?', ganho!=ganho2)

resolução2=int(input('digite a resolução usada:'))
print('houve mudandça na variável:', resolução!=resolução2)

bitProfundidade2=int(input('digite qual o foi a profundidade:'))
print ('houve mudança na variável?', bitProfundidade!= bitProfundidade2)

xIluminaçao2= input('digite a iluminação a ser usada: ')
print=(' houve mudança na iluminação ?', xIluminaçao!=xIluminaçao2)

yiluminação2= input(' digite a yiluminação a ser usada:')
print=('houve mudança na yiluminação?', yiluminação!= yiluminação2)

# F-informações
print('As informações de configurações setadas pelo usuário são:')

print(' A faixaDetector É:',faixaDetector2)
print('O fluoróforo é :', fluorForo2 )
print('O laser é:', laser2)
print('As lentes são: ', lentes2)
print('O ganho foi:', ganho2)
print( 'A resolução foi:', resolução2)
print(' O bitprofundidade:', bitProfundidade2)
print('A Xiluminação foi:', xIluminaçao2)
print(' A  yiluminação foi:', yiluminação2)

#G- calibração do equipamento no sentido horizontal
letra1= input('digite a primera letra do seu nome')
letra2= input('digite a ultima letra do seu nome')
print(letra1*10)
print(letra2*10)

#calibração do equipamento no sentido vertical

seg_letra= input('digite a segunda letra do seu nome')
pen_letra=input('digite a penultima letra do se noome')
print(seg_letra*10)
print(pen_letra*10)

print( 'calibração finalizar')