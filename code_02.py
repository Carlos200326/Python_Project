"""#Crie uma funcao que receba um numero e uma lista, insira o mesmo numero na lista, considere que a lista recebida esteja
em ordem crescente e sua missao eh manter ordenada da mesma maneira."""

def ListaOrdenada(numero, lista):

    lista_ordenada = []

    pos = 0

    n_elementos = len(lista)

    if(type(numero)!= int and type(numero)!= float):

        """
        
        Retorna-se o valor -1 que indica o recebimento de um valor invalido.
        
        """
        return -1

    while pos < n_elementos:

        elemento = lista[pos]

        """

        Seleciona-se o elemento referente a cada posicao da lista e salvamos na variavel
        elemento para realizamos a comparacao com numero, a fim de se decidir o momento em que se deve
        inserir o numero, neste caso, se dá de dois modo, quando o numero em menor do que um elemento referente a
        uma determinada posicao, entao eh inserido antes deste em uma nova lista; ja o outro modo ocorre quando
        chega-se ao final da lista, onde se contata que nenhum valor desta eh superior ao numero, portante, 
        este devera ser adicionado ao final.
        
        """

        if(type(elemento)!= int and type(elemento)!= float):

            print(f"O elemento {elemento} nao eh um valor valido para comparacao.")
            pos = pos + 1
            continue

        if(numero < elemento):

            lista_ordenada = lista_ordenada + [numero] + lista[pos:]
            break

        else:

            lista_ordenada = lista_ordenada + [elemento]

        pos = pos + 1

    if(pos >= n_elementos):

        lista_ordenada = lista_ordenada + [numero]

    return lista_ordenada

print(ListaOrdenada(10,[]))
print(ListaOrdenada(8,[10,[10],10.5,20]))
print(ListaOrdenada(1.5,[1,3,7,22.5]))
print(ListaOrdenada(2.4,[0.7,1.1,2.9,5,6,8,9]))
print(ListaOrdenada(8,[bool,1,2,3]))
print(ListaOrdenada(9,[2,7,[2.5]]))