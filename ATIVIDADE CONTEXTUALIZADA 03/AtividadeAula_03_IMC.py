#Atividade IMC

peso = float (input("inserir peso do paciente (em kg):"))
altura = float (input('inserir altura do paciente (em metro):'))
imc=(peso)/(altura**2)
print('IMC: ', imc)

if imc <17:
    print ('muito abaixo do peso')
elif imc >= 17 and imc <= 18.5:
    print ('abaixo do peso normal')
elif imc > 18.5 and imc <= 25:
    print ('peso dentro do normal')
elif imc > 25 and imc <= 30:
    print ('peso acima do normal')
elif imc > 30:
    print ('muito acima do peso')