# 11-Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.


num1 = int(input("Digite o primero numero inteiro: "))
num2 = int (input("Digite o segundo numero inteiro: "))
num3 = float(input("Digite um numero real: "))

Dobro =(2 * num1) * (num2 / 2)

soma = (3 * num1) + num3

elev_cubo = num3 ** 3

print("o Dobro do primeiro com metade do segundo é: ", Dobro)
print(" A soma do triplo do primeiro com o terceiro é: ", soma)
print("O terceiro elevado ao cubo é: ", elev_cubo)