#Faça um Programa que leia três números e mostre o maior deles
'''Utilizando o max() - serve para determinar um ou mais valores máximos. Aceita uma sequência de valores
como argumento, como uma lista, tupla, ou até mesmo uma sequência separada por vírgulas.'''

#Recebendo os números:
n1 = float(input("Digite um valor:"))
n2 = float(input("Digite um valor:"))
n3 = float(input("Digite um valor:"))

#Determinando maior número dos 3 - Utilizando max.
maior = max(n1,n2,n3)

#Resultado
print("O maior número é {}".format(maior))