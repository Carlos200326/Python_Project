def somatorioPrimos(num1,num2):

    if(num1>num2):

        aux= num2
        num2=num1
        num1=aux
    
    soma = 0

    contagem_divisores=0
    divisor=1

    while(num1<=num2):
        
        while contagem_divisores<=num1:
            if(num1 % divisor)==0:

                contagem_divisores = contagem_divisores + 1
        


