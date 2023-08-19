# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = float(input('Digite um valor em metros:'))
centimetros = valor * 100
milimetros = valor * 1000

print('O valor {}m equivale a {}cm e {}mm'.format(valor, centimetros, milimetros))
