#Atividade 1 AULA 4 IMC

def imc(altura, peso):
	
	return peso / altura**2


peso = float(input('Digite seu Peso (Kg): '))
altura = float(input('Digite sua Altura (m): '))


indice = imc(altura, peso)


print('Seu IMC é: {:.2f}'.format(indice))

print('Muito abaixo do peso', indice < 17)
print('Abaixo do peso', 17 <= indice < 18.5)
print('Peso Normal', 18.5 <= indice < 25)
print('Acima do peso', 25 <= indice < 30)
print('Muito Acima do Peso', indice > 30)
print()