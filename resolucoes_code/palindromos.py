#Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

# Solicitando a palavra do usuário
palavra = input("Digite uma palavra: ")

# Invertendo a string
palavra_invertida = palavra[::-1]

# Verificando se é palíndromo
if palavra == palavra_invertida:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")

