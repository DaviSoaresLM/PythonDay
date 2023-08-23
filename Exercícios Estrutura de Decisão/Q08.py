'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.'''

#Recebendo os valores dos produtos
produto1 = float(input("Digite o valor do primeiro produto:"))
produto2 = float(input("Digite o valor do segundo produto:"))
produto3 = float(input("Digite o valor do terceiro produto:"))

#Determinando o valor mínimo
produto_Barato = min(produto1,produto2,produto3)

#Verificar qual é o produto mais barato:
if produto_Barato == produto1 :
    produto_Escolhido = "Produto 1"
elif produto_Barato == produto2 :
    produto_Escolhido = "Produto 2"
else:
    produto_Escolhido = "Produto 3"

#Resultado
print("Compre o {} pois é o mais barato.".format(produto_Escolhido))
