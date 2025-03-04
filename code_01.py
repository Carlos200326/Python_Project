def CalcularMedia(notas):

    indice = 0
    lista_media = []

    n_notas = len(notas)

    if(n_notas == 0):

        return -1

    if(n_notas % 2 != 0):

        return -2

    while indice < n_notas:

        soma = notas[indice] + notas[indice + 1]
        media = soma / 2.0

        lista_media = lista_media + [media]

        indice = indice + 2

    return lista_media

print(CalcularMedia([]))
print(CalcularMedia([6.7]))
print(CalcularMedia([8,9]))
print(CalcularMedia([8,9,6,7]))
print(CalcularMedia([6,7,9,8,7.5,9.6]))
print(CalcularMedia([5.5,7.8,9.6,8.5, 9.4,7.8]))
