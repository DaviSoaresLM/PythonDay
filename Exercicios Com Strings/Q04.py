#Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

#Uma maneria simples é utilizando For ou While -  Fica a seu critério

#Recebendo o valor nome
nome = input("Digite um nome:")

#Convertendo o nome em Vertical e Escada
for i in range(len(nome)):
    print(nome[:i+1])