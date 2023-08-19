# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

numero = int(input("Digite um número inteiro:"))
antecessor = numero - 1
sucessor  = numero + 1

print('O numero escolhido foi {}, seu antencessor é {} e seu sucessor é {}'.format(numero, antecessor, sucessor))
