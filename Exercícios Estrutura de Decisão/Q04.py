#Faça um Programa que verifique se uma letra digitada é vogal ou consoante

#Recebendo a letra:
letra = str(input("Digite uma letra:").lower()) #Convertendo a letra para minúscula

#Verificando se a letra é vogal ou consoante
if letra.isalpha() and len(letra) == 1: #Verifica se a letra pertence ao alfabeto
    if letra in "aeiou":
        print("A letra é uma vogal.")
    else:
        print("A letra é uma consoante.")
else:
    print("Por favor, digite uma letra!")