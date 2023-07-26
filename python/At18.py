# Atividade 18
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para dowload MB: "))

velocidade_internet_mbps = float(input("Digite a velocidade do link de internet em mbps: "))

tamanho_arquivo_mbps = tamanho_arquivo_mb * 8

tempo_dowload_min = tamanho_arquivo_mbps / velocidade_internet_mbps / 60 

print("O tempo aproximado de dowload do arquivo é de: ", tempo_dowload_min, "minutos")