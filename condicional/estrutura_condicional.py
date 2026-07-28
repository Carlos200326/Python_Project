def funcao_exemplo(var1, var2):


    '''
    Crio uma estrutura condicional com a palavra chave if, em seguida, eu escrevo outras condicionais
    alternativas e fecho com a instrucao else quando for o caso em que estas condicoes nao sao sastifeitas,
    eu executo um codigo padrao pertencente a este else

    '''

    '''
    A logica abaixo consiste em comparar o valor entre duas variaveis que sao definidas pela passagem de 
    argumentos da chamada da funcao.

    '''

    if(var1>var2):

        valor_retorno = 1

    elif(var1==var2):

        valor_retorno = 2
    else:

        valor_retorno = 3

    return valor_retorno


'''
Espaco de chamada de funcoes

'''

print(funcao_exemplo(2.5,7))
print(funcao_exemplo(4.3,8))
print(funcao_exemplo(5,0.9))
print(funcao_exemplo(2.4,2.3))
print(funcao_exemplo(5.5,5.5))
print(funcao_exemplo(10,10))
