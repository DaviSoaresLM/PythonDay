'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

# Receba o tamanho do arquivo em Megabytes
arquivo = float(input("Digite o tamanho do arquivo em Mb:"))

# Receba a velocidade de Internet em Megabytes por segundo

velocidade_Internet = float(input("Digite a velocidade da internet em Mbs: "))

# Cálculo do tempo de Download
tempo_Download = arquivo / (velocidade_Internet / 8)

print(f"O tempo aproximado de download é {tempo_Download:.1f} minutos")

