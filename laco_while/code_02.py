def somatorio_pares(num1,num2):

    if(num1>num2):

        aux = num1
        num1 = num2
        num2 = aux

    if(num1%2):

        num1 = num1 + 1
    
    soma = 0

    while num1<=num2:

        soma = soma + num1
        num1 =  num1 + 2
    
    return soma

print(somatorio_pares(1,3))
print(somatorio_pares(2,2))
print(somatorio_pares(3,3))
print(somatorio_pares(9,1))
print(somatorio_pares(1,9))
print(somatorio_pares(8,2))
print(somatorio_pares(2,8))
print(somatorio_pares(-1,-3))
print(somatorio_pares(-3,-1))
print(somatorio_pares(-2,-2))
print(somatorio_pares(-4,-2))
print(somatorio_pares(-2,-4))
print(somatorio_pares(0,8))
        

