# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode
# comprar. Considere US$1.00 = R$4.,97

dinheiro = float(input('Digite a quantia do seu dinheiro:'))
dolar = 4.97
conversao = dinheiro / dolar

print('Você tem R${}, o valor convertido em dólar é US${:.2f}'.format(dinheiro, conversao))
