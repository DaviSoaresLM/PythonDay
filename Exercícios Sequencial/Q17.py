'''OBSERVAÇÃO - FALTA CONCLUÍR'''


'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

import math

# Metros quadrados da área a ser pintada
area_Pintada = float(input('Digite o tamanho em metros quadrados da área a ser pintada:'))

# Quantidade de tinta necessária - 1L para 6m²
litros_Necessarios = area_Pintada / 6

# Quantidade de latas necessárias - 18 L por lata
quantidades_Latas = litros_Necessarios / 18

# Arrendondando a quantidade de latas pra cima
quantidades_Latas = math.ceil(quantidades_Latas)

# Quantidade de Litros por Galão - 1 Galão para 3.6L + Arredondamento para cima
quantidades_Galoes = litros_Necessarios / 3.6

# Quantidade de Galões Necessários arrendondando pra cima
quantidades_Galoes = math.ceil(quantidades_Latas)

# Determinando os preços da Lata e do Galão
preco_Lata = 80.00
preco_Galao = 25.00

# Determinando os preços ao comprar Latas, Galões e Misturas
preco_Total_Latas = quantidades_Latas * preco_Lata


# Determinando o valor de compra dos Galões
preco_Total_Galoes = quantidades_Galoes * preco_Galao

# Determinando o valor da mistura + Folga (10%)
preco_Mistura = (quantidades_Latas * preco_Lata) + (quantidades_Galoes * preco_Galao)
folga = preco_Mistura * ( 10 / 100)

# Decisão do cliente

escolha = (int(input("Digite '1' se quer comprar penas Latas, Digite '2' se quer comprar apenas Galões, Digite '3' se "
              "quer misturar Latas e Galões"))

if escolha == '1':
    print(f"O valor comprando apenas latas é: R$ {preco_Total_Latas}")
elif escolha == '2':
    print(f"O valor comprando apenas galões é: R$ {preco_Total_Galoes}")
elif escolha == '3'':
    print(f"O valor total ao comprar latas e galões é: R$ {preco_Mistura}")
else:
    print("Valor inválido,Digite '1' se quer comprar penas Latas, Digite '2' se quer comprar apenas Galões, Digite '3' se "
              "quer misturar Latas e Galões")
    escolha = None




