'''O mesmo professor do desafio anterior quer sortear a ordem da apresentação de trabalhos dos
alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada'''

import random
aluno1 = input("Digite o nome do aluno:")
aluno2 = input("Digite o nome do aluno:")
aluno3 = input("Digite o nome do aluno:")
aluno4 = input("Digite o nome do aluno:")

#Lista com nome dos alunos
alunos = [aluno1,aluno2,aluno3,aluno4]

#Embaralhando e sorteando
random.shuffle(alunos)

print("A ordem da apresentação dos trabalhos é: ")
print("1." + alunos[0])
print("2." + alunos[1])
print("3." + alunos[2])
print("4." + alunos[3])




