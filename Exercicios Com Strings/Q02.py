'''Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida
mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que
ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.'''

#Recebendoo o nome
nome = input("Digite seu nome:")

#Utilizando o upper para mostrar o nome em Maiúsculas independente se foi escrito "A" ou "a"
nome = nome.upper()

#Invertendo o nome
nome_Invertido = nome[::-1]

#Trazendo o resultado:
print(f"Seu nome ao contrário é '{nome_Invertido}'")