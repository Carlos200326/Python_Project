def calculaSoma(num1, num2):

    """
        Retorna a soma de dois numeros

    """
    
    return num1 + num2

def calcula_divisao(num1, num2):

    """
        Retorna a divisao entre dois numeros

    """

    return num1/num2

def complexo_soma(num1, num2):

    """
    Retorna a soma de dois numeros complexos

    """

    return num1 + num2

soma = calculaSoma(10,20)
divisao = calcula_divisao(9.5,2)
soma_complexa = complexo_soma(1+5j, 2+8j)

print(type(soma))
print(soma)

print(type(divisao))
print(divisao)

print(type(soma_complexa))
print(soma_complexa)
