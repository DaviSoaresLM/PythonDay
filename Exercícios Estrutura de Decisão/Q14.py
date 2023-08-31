'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
  O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

#Recebendo as notas
nota1 = float(input("Digite o valor da primeira nota:"))
nota2 = float(input("Digite o valor da segunda nota:"))

#Calculo da média:
media = (nota1 + nota2) / 2

#Estabelecendo os valores com if:
if media <= 4.0:
    conceito = "E"
    print(f"Sua média é: {media}\n"
          f"Conceito: {conceito}\n"
          f"Reprovado!")
elif media <= 6.0:
    conceito = "D"
    print(f"Sua média é: {media}\n"
          f"Conceito: {conceito}\n"
          f"Reprovado!")
elif media <= 7.5:
    conceito = "C"
    print(f"Sua média é: {media}\n"
          f"Conceito: {conceito}\n"
          f"Aprovado!")
elif media <= 9.0:
    conceito = "B"
    print(f"Sua média é: {media}\n"
          f"Conceito: {conceito}\n"
          f"Aprovado!")
elif media <= 10.0:
    conceito = "A"
    print(f"Sua média é: {media}"
          f"Conceito: {conceito}\n"
          f"Aprovado!")


