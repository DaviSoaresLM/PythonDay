'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira'''
#Ex: Digite um número: 6.127
#O número 6.127 tem parte inteira 6.


num = float(input('Digite um número real:'))

#Parte inteira
num_Int = int(num)

print('A parte inteira do número "{}" é "{}"'.format(num,num_Int))


