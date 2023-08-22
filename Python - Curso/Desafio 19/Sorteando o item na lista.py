'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
que ajude ele, lendo o nome deles e escrevendo o nome escolhido'''

from random import choice
aluno1 = str(input("Digite o nome do aluno:"))
aluno2 = str(input("Digite o nome do aluno:"))
aluno3 = str(input("Digite o nome do aluno:"))
aluno4 = str(input("Digite o nome do aluno:"))

#Lista com nome dos alunos
alunos = [aluno1,aluno2,aluno3,aluno4]

#Sorteando o aluno
escolhido = choice(alunos)

#Resultado
print("O aluno escolhido foi {}".format(escolhido))


