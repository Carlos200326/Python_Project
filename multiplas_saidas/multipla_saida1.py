def calculo_operacoes(num1,num2):

    """
        Funcao que recebe dois numeros e retorna o resultado das operacoes
        de soma, subtracao, multiplicacao e divisao entre os dois numeros

    """

    soma = num1 + num2 
    sub = num1 - num2
    mult = num1 * num2
    div = num1 / num2
    div_inteiro= num1//num2
    resto = num1 % num2

    return soma, sub, mult, div, div_inteiro, resto

def notasAlunos(p1, p2, pf):

    """
        Funcao recebe notas da p1, p2, pf e retorna a media parcial (obtida com as notas da p1 e p2)
        e a media final (obtida com as notas da media parcial e da prova final)

    """
    mp = (p1 + p2)/2
    mf = (mp + pf)/2

    return mp, mf

def ordemNumerica(num):

    """
        Funcao recebe um numero e retorna o numero de centenas, dezenas e unidades presente
        nesse numero.

    """

    centena = num//100
    dezena = (num - centena*100)//10
    unidade = (num - centena*100 - dezena*10)

    return centena, dezena, unidade


print(calculo_operacoes(5,2))
print(calculo_operacoes(1,2))
print(calculo_operacoes(1,7))
print(calculo_operacoes(2,6))

print("--------")

print(notasAlunos(8.5,9,8))
print(notasAlunos(6,7,9.5))
print(notasAlunos(5,5.9,9))
print(notasAlunos(6.8,6.9,9.9))

print("---------")

print(ordemNumerica(253))
print(ordemNumerica(135))
print(ordemNumerica(831))
print(ordemNumerica(807))
print(ordemNumerica(992))
