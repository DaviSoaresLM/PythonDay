#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

#Recebendo o valor:
num = float(input("Digite um valor:"))

#Testando se é positivo, negativo ou 0:
if num > 0:
    print("O número {} é positivo".format(num))
elif num < 0:
    print("O número {} é negativo".format(num))
else:
    print("O número é 0.")
