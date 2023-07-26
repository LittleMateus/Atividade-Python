# Atividade 17
area_pintada = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

cobertura_por_litro = 6

capacidade_lata = 18

capacidade_galao = 3.6

preco_lata = 80.00

preco_galao = 25.00

litros_necessarios = area_pintada / cobertura_por_litro
litros_com_folga = litros_necessarios * 1.10

quantidade_latas = int((litros_com_folga + capacidade_lata - 1) // capacidade_lata)

quantidade_galoes = int((litros_com_folga + capacidade_galao - 1) // capacidade_galao)

preco_total_latas = quantidade_latas * preco_lata

preco_total_galoes = quantidade_galoes * preco_galao

sobra_litros = litros_com_folga - quantidade_latas * capacidade_lata
quantidade_galoes_mistura = int((sobra_litros + capacidade_galao - 1) // capacidade_galao)

preco_total_mistura = quantidade_latas * preco_lata + quantidade_galoes_mistura * preco_galao

print("Situação 1: Comprar apenas latas de 18 litros")
print("Quantidade de latas a serem compradas:", quantidade_latas)
print("Preço total: R$", preco_total_latas)

print("\nSituação 2: Comprar apenas galões de 3,6 litros")
print("Quantidade de galões a serem comprados:", quantidade_galoes)
print("Preço total: R$", preco_total_galoes)

print("\nSituação 3: Comprar mistura de latas e galões (minimizando o desperdício)")
print("Quantidade de latas a serem compradas:", quantidade_latas)
print("Quantidade de galões a serem comprados:", quantidade_galoes_mistura)
print("Preço total: R$", preco_total_mistura)