def fatorial(num):

    #Calculo do fatorial do numero

    if(num<0):

        return -1

    fator = 1
    resultado = 1

    while fator<=num:

        resultado = resultado * fator
        fator = fator + 1

    return resultado #Resultado de fatorial apos o termino do ciclo while

print(fatorial(0))
print(fatorial(1))
print(fatorial(2))
print(fatorial(3))
print(fatorial(4))
print(fatorial(5))
print(fatorial(6))

