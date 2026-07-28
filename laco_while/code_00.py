def potencia(x,y):


    n = 0
    resposta = 1

    while(n < y):

        resposta = resposta * x
        n = n + 1

    return resposta

print(potencia(2,4))
print(potencia(2,2))
print(potencia(1,2))
print(potencia(1,0))
print(potencia(0,0)) #Caso em que forcamos 0 elevado a 0 a ser um
print(potencia(3,3))
