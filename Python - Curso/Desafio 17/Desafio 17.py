'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo. Calcule e mostre o comprimento da hipotenusa'''

import math

cat_Oposto = float(input("Digite o valor do cateto oposto: "))
cat_Adjacente = float(input("Digite o comprimento  do cateto adjacente: "))

#Calculando hipotenusa
hipotenusa = math.sqrt(cat_Oposto**2 + cat_Adjacente**2)

#Resultado
print("O comprimento da hipotenusa é:", hipotenusa)



