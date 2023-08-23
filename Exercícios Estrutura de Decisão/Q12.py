'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas
no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
abaixo.  No exemplo o valor da hora é 5 e a quantidade de hora é 220.
            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00'''

#Recebendo o valor da Hora e da quantidade de horas trabalhadas:
valor_hora = float(input("Digite o valor da sua hora: R$"))
hora_Trabalhada = float(input("Digite a quantidade de horas trabalhadas: "))

#Determinando o valor do salário bruto:
salario_Bruto = valor_hora * hora_Trabalhada

#Determinando os valores de desconto do IR


if salario_Bruto <= 900.00:
    desconto_Ir = 0
elif salario_Bruto <= 1500.00:
    desconto_Ir = salario_Bruto * 0.05
elif salario_Bruto <= 2500.00:
    desconto_Ir = salario_Bruto * 0.10
else:
    desconto_Ir = salario_Bruto * 0.20

#Desconto Sindicato
desc_Sindicato = 0.03 * salario_Bruto

#Desconto INSS
desc_Inss = 0.10 * salario_Bruto
#FGTS
fgts = 0.11 * salario_Bruto

#Soma de todos os descontos =
soma_Descontos = desconto_Ir + desc_Sindicato + desc_Inss

#Determinando o valor do salário líquido
salario_Liquido = salario_Bruto - soma_Descontos
#Imprindo o resultado
print(f"Salário bruto: R${salario_Bruto:.2f}")
print(f"(-) IR: R${desconto_Ir:.2f}")
print(f"(-) INSS: R${desc_Inss:.2f}")
print(f"FGTS: R${fgts:.2f}")
print(f"Total de descontos: R${soma_Descontos:.2f}")
print(f"Salário líquido: R${salario_Liquido:.2f}")


