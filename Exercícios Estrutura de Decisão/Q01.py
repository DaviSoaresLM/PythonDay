#Faça um programa que peça dois números e imprima o maior deles

#Recebendo os números:
n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))

#Verificando qual o maior número:
if n1 > n2 :
    print(f"O maior número é: {n1}")
elif n1 == n2:
    print("Ambos são iguais")
else:
    print(f"O maior número é: {n2}")
