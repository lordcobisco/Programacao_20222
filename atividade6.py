from operator import truediv


anestesiaFarmacos= ['xilazina', 'Ketamina']
dosagem= ('xilazina- 2 mg/kg', 'ketamina-1 a 4,5mh-kg ')
via= ('xilazina- intraperitoneal', 'Ketamina-intraperitoneal') 

# I-procedimentos de anestesia

pesoAnimal= input("qual o peso em g do animal a ser usado")
print(pesoAnimal)

print("tipo de anestesico:", anestesico)
anestUsado= input("colocar nome do anestesico")

print("melhor dosagem:",dosagem )
dosUsada= float(input("colocar o valor da dose usada"))

print("vias recomendadas:", via)
viaUsada= input("colocar via usada")

print("o anestesico usado foi:", anestUsado)
print("a dose usada foi:"dosUsada)
print(" a via usada foi:"viaUsada)


#II-posicionamento do animal no estereotáxico

print("As barras que suportam o peso do animal devem ser posicionadas no ouvido externo do animal")
print ("verificar a angulação da cabeça do animal 3x,")

posição= 0
for posição in range (3):
    posicionamento= int( input("o animal está na posição correta? sim (1)- não (0):"))

if posicionamento==1:
    print("o animal está na posiçãocorreta")
elif posicionamento==1:
    print ("o animal está na posição e angulação correta ")
else:

   print (erro)

   #III- Limpeza do campo de trabalho

   etapas= ("Retirada da pelagem ", "Retirada dos tecidos moles","limpar a calota craniana")
   for i in etapas:
    if etapas=="limpar a calota craniana":
        print("tilizando H2O2 10 volumes")

    #IV 
campo_limpo=False
animal_sujo= True
while campo_limpo== False:
    print('limpe o campo')
    limpeza = input("o campo foi limpo? s/n")
    if limpeza == 's':
        campo_limpo = True
print("limpeza concluida")

#v fixação dos parafusos 





    

