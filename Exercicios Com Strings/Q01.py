'''Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu
comprimento.Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no
conteúdo.'''

#Recebendo as strings
string1 = str(input("Digite uma frase:"))
string2 = str(input("Digite uma frase:"))

#Determinando o tamanho das strings
quantidade_String1 = len(string1)
quantidade_String2 = len(string2)

#verifica se possuem o mesmo comprimento
comprimento_Igual = quantidade_String1 == quantidade_String2

#Verifica se são iguais no conteúdo
conteudo_Igual = string1 == string2

#Imprimindo o conteúdo:
print('Tamanho de "{}" é: "{}"'.format(string1, quantidade_String1))
print('Tamanho de "{}" é: "{}"'.format(string2, quantidade_String2))

#Testando se possuam o mesmo comprimento
if comprimento_Igual:
    print("As duas strings são de tamanhos iguais")
else:
    print("As duas strings são de tamanhos diferentes")

#Testando se possuem o mesmo conteúdo
if conteudo_Igual:
    print("As duas strings possuem conteúdo igual.")
else:
    print("As duas strings possuem conteúdo diferente.")