#Author: Carlos Eduardo Cordeiro dos Santos
#Date: 2026-07-28 

#Description (Portuguese): A seguir, criamos uma funcao que recebe dois numeros e retorna a soma de todos 
#os impares entre os mesmos (inclusive, quando for o caso de serem impares)

def somatorio_impares(num1, num2):

    soma = 0

    n = 0

    if(num2 < num1):

        aux = num1 #valor maior
        num1 = num2 #valor menor transfere-se ao num1
        num2 = aux #valor maior transfere-se ao num2
    
    num_inicial = num1


    while(num_inicial<=num2):

        if((num_inicial % 2)==1):

            soma = soma + num_inicial
        num_inicial = num_inicial + 1

    return soma

print(somatorio_impares(-2,-4))
print(somatorio_impares(2,6))
print(somatorio_impares(0,7))
print(somatorio_impares(1,1))
print(somatorio_impares(2,2))
