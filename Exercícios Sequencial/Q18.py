'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

arquivo = float(input("Digite o tamanho do arquivo em Megabytes:"))

velocidade_Internet = float(input("Digite a velocidade da internet em Mbs: "))

tempo_Download = arquivo / (velocidade_Internet / 8)

print(f"O tempo aproximado de download é {tempo_Download:.1f} minutos")
