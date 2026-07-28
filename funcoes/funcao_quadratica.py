def delta(a,b,c):

    return b**2 - 4*a*c

def funcao_quadratica(a,b,c):

    discriminante = delta(a,b,c)

    x1 = (-b + discriminante**(1/2))/(2*a)
    x2 = (-b - discriminante**(1/2))/(2*a)

    return x1,x2

print(funcao_quadratica(1,5,6))
print(funcao_quadratica(1,-5,6))
print(funcao_quadratica(1,6,9))
print(funcao_quadratica(1,-7,12))
