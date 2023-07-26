# Atividade 16

area_pintada= float(input("Dgite o tamanho da area a ser pintada em metros: "))

cobertura_por_litro = 3

capacidade_lata = 18

preco_lata = 80.00

litros_necessarios = area_pintada / cobertura_por_litro

quantidade_latas = int((litros_necessarios + capacidade_lata - 1) // capacidade_lata)

preco_total = quantidade_latas * preco_lata

print("Quantidade de latas de tintas a serem compradas: ", quantidade_latas)
print("Preço total: R$", preco_total)