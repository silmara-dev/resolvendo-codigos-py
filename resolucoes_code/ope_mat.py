# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

#Declaração do tipo de variável e solicitação da entrada de dados
dado1 = int(input("Digite o primeiro número: "))
dado2 = int(input("Digite o primeiro número: "))

#Operações
soma = dado1 + dado2
subi = dado1 - dado2
mult = dado1 * dado2

# Verificando divisão por zero
if dado2 != 0:
    div = dado1 / dado2
else:
    divisao = "Não é possível dividir por zero"

#Resultados 
print("O numeros ", dado1, " e ", dado2, " somados é igual a: ",soma)
print("O numeros ", dado1, " e ", dado2, " subtraidos é igual a: ",subi)
print("O numeros ", dado1, " e ", dado2, " multiplicados é igual a: ",mult)
print("O numeros ", dado1, " e ", dado2, " divididos é igual a: ",div)
