'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 7Imprima os dados do programa com as mensagens adequadas.'''

#Recebendo valor - Quilo
peso = float(input("Digite o peso do peixe em Quilos:"))

#Limite de peso
limite = 50.0

#Excesso de peso
if peso > limite:
    excesso = peso - limite
    multa_Por_Quilo = 4.00
    multa = excesso * multa_Por_Quilo

else:
    excesso = 0
    multa = 0

#Resultados

if excesso > 0:
    print(f"O peso do peixe é de: {peso:.2f}Kg")
    print(f"O excesso é de: {excesso:.2f}Kg")
    print(f"O valor da multa é de: R$ {multa:.2f}")
else:
    print(f"O peso do peixe é de {peso:.2f}Kg e está dentro dos limites")


