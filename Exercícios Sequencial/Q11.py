'''Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
1 - O produto do dobro do primeiro com metade do segundo .
2 - a soma do triplo do primeiro com o terceiro.
3 - o terceiro elevado ao cubo.'''

n_Inteiro1 = int(input("Digite o primeiro número inteiro:"))

n_Inteiro2 = int(input("Digite o segundo número inteiro:"))

n_Real  = float(input("Digite um número real:"))

resultado01 = (n_Inteiro1 * 2) + (n_Inteiro2 / 2)
resultado02 = (n_Inteiro1 * 3) + n_Real
resultado03 = n_Real ** 3

print("1 - O produto do dobro do primeiro número com metade do segundo número"
      " é:", resultado01)
print("2 - A soma do triplo do primeiro número com o terceiro número é:", resultado02)
print("3 - O terceiro número elevado ao cubo é: {:.2f}".format(resultado03))