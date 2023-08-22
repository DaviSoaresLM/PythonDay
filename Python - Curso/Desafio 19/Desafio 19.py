'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
que ajude ele, lendo o nome deles e escrevendo o nome escolhido'''

import random
aluno1 = input("Digite o nome do aluno:")
aluno2 = input("Digite o nome do aluno:")
aluno3 = input("Digite o nome do aluno:")
aluno4 = input("Digite o nome do aluno:")

#Lista com nome dos alunos
alunos = [aluno1,aluno2,aluno3,aluno4]

#Sorteando o aluno
aluno_Escolhido =  random.choice(alunos)

#Resultado
print(f"O aluno escolhido para apagar o quadro é: '{aluno_Escolhido}'")

