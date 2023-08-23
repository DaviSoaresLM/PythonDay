#Faça um Programa que leia três números e mostre o maior e o menor deles
'''Utiliza min() - Determina o valor mínimo de um 1 ou mais valores; oposto do Max mas aceita os mesmos
argumentos'''

#Recebendo os valores:
n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))
n3 = int(input("Digite um número:"))

#Determinando maior número dos 3:
maior = max(n1,n2,n3)
#Determinando o menor número dos 3:
menor = min(n1,n2,n3)
#Resultado
print("O maior número é {} e o menor é {}".format(maior, menor))
