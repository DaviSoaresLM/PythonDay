'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
1 - Para homens: (72.7*h) - 58
2 - Para mulheres: (62.1*h) - 44.7'''


altura = float(input("Digite sua altura:"))

genero = input("Digite seu gênero ( M se for masculino e F se for feminino):")

if genero == 'M' or 'm':
    peso_Ideal = (72.7 * altura) - 58

elif genero == 'F' or 'f':
    peso_Ideal = (62.1 * altura) - 44.7

else:
    print("Gênero não identificado, utilize 'M' para masculino ou 'F' para feminino")
    peso_Ideal = None
if peso_Ideal is not None:
    print(f"Dada a sua altura {altura:.2f}cm, o seu peso ideal é: {peso_Ideal:.2f}Kg")