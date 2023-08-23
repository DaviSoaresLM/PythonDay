'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para
desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o
reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

#Recebendo o valor do salário:
salario_Atual = float(input("Digite o valor do seu salário: R$"))

#Determinando os valores dos reajustes
aumento_20 = 0.20
aumento_15 = 0.15
aumento_10 = 0.10
aumento_5 = 0.05

#Determinando o reajuste com base no salário atual:
if salario_Atual <= 280.00:
    percentual_Aumento = aumento_20
elif salario_Atual <=700.00:
    percentual_Aumento = aumento_15
elif salario_Atual <= 1500.00:
    percentual_Aumento = aumento_10
else:
    percentual_Aumento = aumento_5

#Calculando os valores
valor_Aumento = salario_Atual * percentual_Aumento
novo_Salario = salario_Atual + valor_Aumento

#Imprimindo resultados
print(f"Salário antes do reajuste: R${salario_Atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_Aumento * 100 :.2f}%")
print(f"O valor do aumento é: R${valor_Aumento:.2f}")
print(f"O novo salário é: R${novo_Salario:.2f}")
