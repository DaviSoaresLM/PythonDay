''''Faça ym programa que leia um ângulo qualquer e mostre na tela o valor da seno, cosseno,
e tangente desse ângulo.'''

import math
num = float(input("Digite um valor para o ângulo:"))

#Convertendo para seno, cosseno e tangente, grau para radiano
ang_Radiano = math.radians(num)
seno = math.sin(num)
cosseno = math.cos(num)
tangente = math.tan(num)

#Resultado

print(f"O ângulo citado é {num}°")
print(f"Seu seno é:{seno:.4f}")
print(f"Seu cosseno é {cosseno:.4f}")
print(f"Sua tangente é {tangente:.4f}°")
