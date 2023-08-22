'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo. Calcule e mostre o comprimento da hipotenusa'''

import math
#Recebendo valores
cat_Oposto = float(input("Digite o valor do cateto oposto: "))
cat_Adjacente = float(input("Digite o comprimento  do cateto adjacente: "))

#Calculando hipotenusa
hipotenusa = math.hypot(cat_Oposto, cat_Adjacente)

#Resultado
print(f"O comprimento da hipotenusa é:{hipotenusa:.2f}")


