#Faça um Programa que leia três números e mostre-os em ordem decrescente
'''OBS:  função sorted() retorna uma nova lista ordenada e não altera a lista original; utilizar o
'reverse=true' para tornar a lista em ordem decrescente'''

#Recebendo os valores:
n1 = float(input("Digite um número:"))
n2 = float(input("Digite um número:"))
n3 = float(input("Digite um número:"))

#Adicionando os números em uma lista
numeros = [n1,n2,n3]

#Ordenando a lista em ordem decrescente
ordem_Decrescente = sorted(numeros, reverse=True)

#Resultado
print(f"A ordem decrescente dos números é: {ordem_Decrescente}")
