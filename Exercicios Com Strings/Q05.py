#Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida

#Pode usar o For ou While para tornar mais simples, fica a seu critério

#Recebendo o nome:
nome = input("Digite seu nome:")

#Convertendo para uma Vertical e Invertida
for i in range(len(nome), 0, -1):
    print(nome[:i])