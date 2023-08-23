'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou
N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

#Recebendo o valor te Turno:
turno = input("Em que turno você estuda? M - Matutino, V - Vespertino ou N - Noturno:")

#Utilizando upper para converter em maíúsculo independente se o usuário escrever "I" ou "i"
turno = turno.upper()

#Verificando o turno e imprimindo o resultado
if turno == 'M':
    print("Bom dia!")
elif turno == 'V':
    print("Boa tarde!")
elif turno == 'N':
    print("Boa noite!")
else:
    print("Valor inválido!")
