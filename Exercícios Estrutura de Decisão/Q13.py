'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.'''

dia_int = int(input("Digite um número do dia da semana:"))
dia_sem = ""

if dia_int == 1:
    dia_sem = "Domingo"
elif dia_int == 2:
    dia_sem = "Segunda"
elif dia_int == 3:
    dia_sem = "Terça"
elif dia_int == 4:
    dia_sem = "Quarta"
elif dia_int == 5:
    dia_sem = "Quinta"
elif dia_int == 6:
    dia_sem = "Sexta"
elif dia_int == 7:
    dia_sem = "Sábado"
if dia_int == "":
    print("Valor inválido")
else:
    print(f"O dia da semana correspondendo ao número {dia_int} é {dia_sem}")




