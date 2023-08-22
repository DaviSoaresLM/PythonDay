# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada

numero = float(input("Digite um número:"))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print("O número digitado foi {}, seu dobro é {}, seu triplo é {}, sua raíz é {:.2f}".format(numero, dobro, triplo,raiz))
