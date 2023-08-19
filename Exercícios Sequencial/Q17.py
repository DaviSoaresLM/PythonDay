'''OBSERVAÇÃO - FALTA CONCLUÍR'''


'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

import math

litros_Lata = 18
preco_Lata = 80
litros_Galoes = 3.6
preco_Galoes = 25

m2 = float(input("Por favor, insira o tamanho da área em metros quadrados"))
litros_Necessarios = m2 / 6

# 1 - Comprar apenas latas de 18L
qtd_Latas = math.ceil(litros_Necessarios / litros_Lata)
custo_Latas = qtd_Latas * preco_Lata
print("Somente latas de 18: ")
print(f"O cliente precisa comprar {qtd_Latas} latas, que custarão R${custo_Latas}.")

#2 - Comprar apenas galões de 3.6 litros
qtd_Galoes