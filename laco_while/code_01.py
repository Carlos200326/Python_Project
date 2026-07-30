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

print("========Versao 1 da funcao somatorio_impares=========")
print(somatorio_impares(2,2))
print(somatorio_impares(1,4))
print(somatorio_impares(3,3))
print(somatorio_impares(7,1))
print(somatorio_impares(-4,-2))
print(somatorio_impares(-6,-6))
print(somatorio_impares(-3,-3))
print(somatorio_impares(0,0))
print(somatorio_impares(-2,-4))


def somatorio_impares2(num1,num2):

    if(num1>num2):

        aux = num1
        num1 = num2
        num2 = aux
    
    if(num1%2 == 0):
        
        if(num1 + 1 <= num2):
            
            num1 = num1 + 1

        if(num1 == num2):

            return 0

    soma = 0
    
    while(num1<=num2):

        """interrupcao de laco de interacao while ocorre quando num1 eh maior do que num2 
          => condicao de parada"""  
        
        soma = soma + num1

        num1=num1 + 2

    return soma
print("========Versao 2 da funcao somatorio_impares=========")
print(somatorio_impares2(2,2))
print(somatorio_impares2(1,4))
print(somatorio_impares2(3,3))
print(somatorio_impares2(7,1))
print(somatorio_impares2(-4,-2))
print(somatorio_impares2(-6,-6))
print(somatorio_impares2(-3,-3))
print(somatorio_impares2(0,0))
print(somatorio_impares2(-2,-4))
