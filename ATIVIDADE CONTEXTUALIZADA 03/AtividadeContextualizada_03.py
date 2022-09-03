#Atividade contextualizada 03 

#Variáveis
inicio = 'Este programa configura o microscópio confocal para aquisição de imagens.'
print(inicio)

mensagem = 'Houve alguma mudança na variável?'

tipo_celular = 'epitelial'
resolucao = '1080p'
zoom = '100x'
filtro = 'pink'
tamanho_imagem = '10x20cm'
ganho = '570'
salvar_como = 'JPEG'
comprimento_onda = '305 nm'
volts = '220' 
ano = '2010'

escolha_tipo_celula = input('Digite qual o tipo de célula:')
mensagem = input('Houve alteração na variável inserida? Digite s ou n:')
print((mensagem=='s' and escolha_tipo_celula!=tipo_celular) or (mensagem=='n' and escolha_tipo_celula==tipo_celular ))

escolha_resolucao = input('Digite qual o tipo de resolução:')
mensagem = input('Houve alteração na variável inserida? Digite s ou n:')
print((mensagem=='s' and escolha_resolucao!=resolucao) or (mensagem=='n' and escolha_resolucao==resolucao ))

escolha_zoom = input('Digite qual a quantidade de zoom:')
mensagem = input('Houve alteração na variável inserida? Digite s ou n:')
print((mensagem=='s' and escolha_zoom!=zoom) or (mensagem=='n' and escolha_zoom==zoom ))

escolha_filtro = input('Digite qual o tipo de filtro:')
mensagem = input('Houve alteração na variável inserida? Digite s ou n:')
print((mensagem=='s' and escolha_filtro!=filtro) or (mensagem=='n' and escolha_filtro==filtro ))

escolha_tamanho_imagem = input('Digite qual o tamanho da imagem:')
mensagem = input('Houve alteração na variável inserida? Digite s ou n:')
print((mensagem=='s' and escolha_tamanho_imagem!=tamanho_imagem) or (mensagem=='n' and escolha_tamanho_imagem==tamanho_imagem ))

escolha_ganho = input('Digite o ganho:')
mensagem = input('Houve alteração na variável inserida? Digite s ou n:')
print((mensagem=='s' and escolha_ganho!=ganho) or (mensagem=='n' and escolha_ganho==ganho ))

escolha_salvar_como = input('Digite como salvar:')
mensagem = input('Houve alteração na variável inserida? Digite s ou n:')
print((mensagem=='s' and escolha_salvar_como!=salvar_como) or (mensagem=='n' and escolha_salvar_como==salvar_como ))

escolha_comprimento_onda = input('Digite qual o comprimento de onda:')
mensagem = input('Houve alteração na variável inserida? Digite s ou n:')
print((mensagem=='s' and escolha_comprimento_onda!=comprimento_onda) or (mensagem=='n' and escolha_comprimento_onda==comprimento_onda ))

escolha_volts = input('Digite quantos volts:')
mensagem = input('Houve alteração na variável inserida? Digite s ou n:')
print((mensagem=='s' and escolha_volts!=volts) or (mensagem=='n' and escolha_volts==volts ))

escolha_ano = input('Digite qual o ano:')
mensagem = input('Houve alteração na variável inserida? Digite s ou n:')
print((mensagem=='s' and escolha_ano!=ano) or (mensagem=='n' and escolha_ano==ano ))

infos = 'Configurações definidas pelo usuário:'

print(infos)
print(escolha_tipo_celula)
print(escolha_resolucao)
print(escolha_zoom)
print(escolha_filtro)
print(escolha_tamanho_imagem)
print(escolha_ganho)
print(escolha_salvar_como)
print(escolha_comprimento_onda)
print(escolha_volts)
print(escolha_ano)

calibrar = 'Início da calibração, siga as instruções:'
print(calibrar)
 
calibracao_telaH = 'Calibração de tela sentido horizontal'
print(calibracao_telaH)
 
calibracaoI = input('Digite a letra inicial de seu nome:')
nome_okI = 'Inicial digitada com sucesso:'
print (nome_okI, end=''), print(calibracaoI)
 
calibracaoI_x = input('Digite 10x a letra inicial de seu nome:')
mensagemI = input('A letra inicial de seu nome foi digitada 10x? Digite s ou n:')
 
sucesso= 'Etapa da calibração feita com sucesso:'
print(sucesso, end=''), print(calibracaoI_x == calibracaoI*10)
 
calibracaoF = input('Digite a última letra de seu nome:')
nome_okF = 'Última letra digitada com sucesso:'
print (nome_okF, end=''), print(calibracaoF)
 
calibracaoF_x = input('Digite 10x a última letra de seu nome:')
mensagemF = input('A última letra de seu nome foi digitada 10x? Digite s ou n:')
 
sucesso= 'Etapa da calibração feita com sucesso:'
print(sucesso, end=''), print(calibracaoF_x == calibracaoF*10)
 
fim_horizontal = 'Final calibração de tela sentido horizontal, caso alguma resposta foi False, repetir processo.'
print(fim_horizontal)
 
calibracao_telaV = 'Calibração de tela sentido vertical'
print(calibracao_telaV)
 
calibracaoY = input('Digite a segunda letra de seu nome:')
nome_okY = 'Segunda letra digitada com sucesso:'
print (nome_okY, end=''), print(calibracaoY)
 
calibracaoY_x = input('Digite 10x a segunda letra de seu nome:')
mensagemY = input('A segunda letra de seu nome foi digitada 10x? Digite s ou n:')
 
sucesso= 'Etapa da calibração feita com sucesso:'
print(sucesso, end=''), print(calibracaoY_x == calibracaoY*10)
 
calibracaoFF = input('Digite a penúltima letra de seu nome:')
nome_okFF = 'Penúltima letra digitada com sucesso:'
print (nome_okFF, end=''), print(calibracaoFF)
 
calibracaoFF_x = input('Digite 10x a penúltima letra de seu nome:')
mensagemFF = input('A penúltima letra de seu nome foi digitada 10x? Digite s ou n:')
 
sucesso= 'Etapa da calibração feita com sucesso:'
print(sucesso, end=''), print(calibracaoFF_x == calibracaoFF*10)
 
acabou = 'Final calibração: Caso alguma resposta foi False, repetir o processo.'
print(acabou)









