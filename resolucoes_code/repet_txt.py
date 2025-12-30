# Agora vamos solicitar uma string e um número inteiro como entrada.
# Depois teremos que retornar a string repetida o número de vezes informado

# Solicitando os dados do usuário
texto = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

# Repetindo a string
resultado = (texto + " " )* numero

# Exibindo o resultado
print(resultado)
