# 15- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto 
# de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:salário bruto.



valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas_mes = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário bruto
salario_bruto = valor_por_hora * horas_trabalhadas_mes

# Calcula os descontos de IR, INSS e sindicato
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05

# Calcula o salário líquido após os descontos
salario_liquido = salario_bruto - (desconto_ir + desconto_inss + desconto_sindicato)

# Imprime os resultados
print("Salário Bruto: R$", salario_bruto)
print("Desconto IR (11%): R$", desconto_ir)
print("Desconto INSS (8%): R$", desconto_inss)
print("Desconto Sindicato (5%): R$", desconto_sindicato)
print("Salário Líquido: R$", salario_liquido)