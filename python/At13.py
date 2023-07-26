# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite sua altura em metros: "))

peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 *altura) - 44.7

print("Peso ideal para homens: ", peso_ideal_homem, "kg")
print("peso ideal para mulheres: ", peso_ideal_mulher, "kg")
    

    
    
    