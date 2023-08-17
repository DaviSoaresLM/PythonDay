'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no
mês. Calcule e mostre o total do seu salário no referido mês.'''

ganho_Hora = float(input("Digite o valor que ganha por hora: "))

hora_Trabalho = float(input("Digite o total de horas trabalhadas no mês:"))

salario_Total = ganho_Hora * hora_Trabalho

print(f"Seu ganho por hora é: R$ {ganho_Hora}/h, você trabalhou um total de: {hora_Trabalho} " 
      f"horas esse mês e o salário total no mês é: R$ {salario_Total:.2f}")

