'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.'''

#Recebendo o preço
preco = float(input("Digite o preço do produto: R$"))

#Valor desconto
desconto = preco * (5 / 100)

#Determinando preço com desconto
preco_Final = preco - desconto

#Resultado
print(f"\nDado o preço R${preco} + desconto de 5%, o valor final é R${preco_Final}")


