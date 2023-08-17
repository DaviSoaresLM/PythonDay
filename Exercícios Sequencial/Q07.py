'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para
o usuário'''

quadrado = float(input("Digite o valor do Lado do quadrado:"))

area = quadrado ** 2

dobroArea = 2 * area

print(f"O valor citado foi {quadrado}, sua área é: {area:.2f} e o dobro da"
      f"área é: {dobroArea:.2f}")