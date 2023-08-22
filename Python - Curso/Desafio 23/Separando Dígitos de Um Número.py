'''Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''
#Ex: Digite um número: 18834;  unidade: 4; dezena: 3; cententa: 8; milhar:1

#Recebendo o número:
numero = int(input("Digite um número entre 0 e 9999:"))

#Classificando em Unidade, Dezena, Centena e Milhar:
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

#Mostrando valores:
print("Analisando o número {}".format(numero))
print("Unidade:{}".format(u))
print("Dezena:{}".format(d))
print("Centena:{}".format(c))
print("Milhar: {}".format(m))




