'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média
alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

#Recebendo as notas
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))

#Calculando a média
media = (n1+n2)/2

#Imprimindo o resultado
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")
