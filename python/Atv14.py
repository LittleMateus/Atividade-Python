# Atividade 14 (Nao botei o enuciado pq é mt grande é a do pescador)

peso_regulamento = 50 

peso_peixes = float(input("Qual é o peso total dos peixes seu joão? em kg"))

if peso_peixes > peso_regulamento:
    excesso = peso_peixes - peso_regulamento
    valor_multa = excesso * 4.00

    print("Seu joão o peso de peixes excedeu o lmite do regulamento.")
    print(f"Excesso de peso: {excesso: 2.f} kg")
    print(f"Valor da multa: R$ {valor_multa:.2f}")
else:
    print("peso de peixes dentro do limite do regulamento. Sem multas🙌")
    