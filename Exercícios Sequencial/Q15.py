'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$'''

#Ganho/h e Horas Trabalhadas
ganho_Horas = float(input("Quanto você ganha por hora?"))
horas_Trabalhadas = float(input("Quantas horas você trabalhou no mês?"))

#Salário Bruto
salario_Bruto = ganho_Horas * horas_Trabalhadas

#Imposto de Renda = -11%
imposto_Renda = salario_Bruto * (11 / 100)

#Valor pago ao Inss = 8%
inss = salario_Bruto * (8 / 100)

#Valor pago ao Sindicato = 5%
sindicato = salario_Bruto * (5 / 100)

#Valor Descontos
desconto = imposto_Renda + inss + sindicato

#Salário Líquido
salario_Liquido = salario_Bruto - desconto

print(f"+ Salário bruto: R$ {salario_Bruto:.2f}")
print(f"- IR: R$ {imposto_Renda:.2f}")
print(f"- INSS: R$ {inss:.2f}")
print(f"- Sindicato: R$ {sindicato:.2f}")
print(f"= Salário Líquido: R$ {salario_Liquido:.2f}")



