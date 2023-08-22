'''Crie um programa que leia o nome completo de uma pessoa e mostre:
1. O nome com todas as letras Maiúsculas e Minúsculas;
2. Quantas letras ao todo (sem considerar espaços);
3. Quantas letras tem o primeiro nome.'''

#Recebendo o Nome:
nome = str(input("Digite um nome completo: "))

#Letras Maíúsculas e Minúsculas
print("Nome Maiúsculo:", nome.upper())
print("Nome Minúsculo:", nome.lower())

#Quantas letras ao todo (sem considerar espaços)
quantidade_Letras = len(nome.replace(" ", ""))
print(("Quantidade total de letras é:", quantidade_Letras))

#Quantas letras tem o primeiro nome
primeiro_Nome = len(nome.split()[0])
print("A quantidade de letras no primeiro nome é:",primeiro_Nome)
