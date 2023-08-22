'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,  M - Masculino, Sexo Inválido.'''

#Recebendo a Letra

letra = str(input('Digite "M" se você é do sexo Masculino, digite "F" se você é do sexo feminino:'))

#Testando se é M,F ou Inválido

if letra == 'M' or "m":
    print("{} - Masculino".format(letra))
elif letra == 'F' or 'f':
    print("{} - Feminino".format(letra))
else:
    print("Sexo inválido, tente novamente com M para masculino e F para feminino")



