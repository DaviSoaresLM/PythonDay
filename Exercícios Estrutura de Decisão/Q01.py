#Faça um programa que peça dois números e imprima o maior deles

#Recebendo os números:
n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))

#Verificando qual o maior número:
if n1 > n2 :
    print("O maior número é: {}".format(n1))
else:
    print("O maior número é: {}".format(n2))