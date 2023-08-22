'''Faça um programa que leia a largura da parede e a altura de uma parede em metros, calcule a
sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta,
pinta em media 2m²'''

#Recebendo Valores
largura_Parede = float(input("Digite o valor da largura da parede: "))
altura_Parede = float(input("Digite o valor da altura da parede: "))

#Calculando a área
area = largura_Parede * altura_Parede

#Calculando a quantidade de tinta -> 1l = 2m²
litro_Tinta = area / 2

#Mostrando Resultados
print(f"Dada a altura da parede {altura_Parede}m²")
print(f"Dada a largura da parede {largura_Parede}m²")
print(f"O valor da sua área é {area}m2")
print(f"será necessário o total de {litro_Tinta}l de tinta")