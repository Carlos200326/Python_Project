def estado_nota(p1,p2):
    
    media = (p1+p2)/2

    if(media >= 7):

        return 1

    elif(3.0<=media<7):

        return 2

    """ Se nenhum dos casos anteriores forem atendidos, ele retorna 3 """

    return 3

def situacaoAluno(p1,p2):

    """
        A funcao recebe as notas de p1 e p2, calcula a media e retorna a situacao do aluno

    """

    media = (p1+p2)/2

    if(media>=7.0):

        situacao = 1

    elif(3.0<=media<7.0):

        situacao = 2

    else:

        situacao = 3

    return situacao

print("\033[32mPrimeira funcao: \033[0m")
print(estado_nota(10,9))
print(estado_nota(5,8))
print(estado_nota(2,1))
print(estado_nota(9,7))
print(estado_nota(8,5))
print(estado_nota(2,3))

print("-------------")

print("\033[34mSegunda funcao: \033[0m")

print(situacaoAluno(10,9))
print(situacaoAluno(5,8))
print(situacaoAluno(2,1))
print(situacaoAluno(9,7))
print(situacaoAluno(8,5))
print(situacaoAluno(2,3))

