#Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical

#Recebendo o nome
nome = input("Digite seu nome:")

#Utilizando a função 'str.replace() para substituir os caracteres por eles mesmos e quebrar linha
nome_Vertical = nome.replace("","\n")[1:-1]

#Imprimindo o f
print(nome_Vertical)
