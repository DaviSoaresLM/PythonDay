"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
preço total."""

import math

# Metros quadrados da área a ser pintada
area_Pintada = float(input('Digite o tamanho em metros quadrados da área a ser pintada:'))

# Quantidade de tinta necessária - 1L para 3m²
litros_Necessarios = area_Pintada / 3

# Quantidade de latas necessárias - 18 L por Lata
quantidades_Latas = litros_Necessarios / 18

# Arredondar o número de latas para cima
quantidades_Latas = math.ceil(quantidades_Latas)

# Cálculo preço total das latas - 80 x número de latas
preco_Lata = 80.00
preco_Total = quantidades_Latas * preco_Lata

# Resultados
print(f"Você precisará de {quantidades_Latas} latas de tinta")
print(f"O preço total é: R$ {preco_Total:.2f}")



