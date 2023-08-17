'''Faça um Programa que peça a temperatura em graus Fahrenheit,  transforme e mostre a
temperatura em graus Celsius'''

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit:"))

Celsius = 5 * ((fahrenheit-32) / 9)

print(f"(A temperatura {fahrenheit:.2f}°F equivale a {Celsius:.1f}°C")
