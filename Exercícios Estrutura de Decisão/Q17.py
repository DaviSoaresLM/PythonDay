'''Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou
não bissexto.'''

#Recebendo o ano:
ano = int(input("Digite um ano: "))

#Verificando se o ano é bissexto com base nas regras do calendário gregoriano:
if (ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")
    