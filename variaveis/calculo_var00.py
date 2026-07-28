def calcVolEsfera(raio):
    ''' Funcao que recebe o valor do raio de uma esfera e retorna o seu volume. '''

    pi = 3.1415
    
    return 4/3 * pi * raio**3

def CalcDistanciaMRUA(t0,tf,v0,vf):
    ''' Funcao que recebe o valor de instante inicial, instante final, velocidade
    inicial e velocidade final de um movimento retilineo acelerado e retorna a distancia
    total percorrida
    '''

    t = tf-t0
    deltaV = vf - v0

    a = deltaV/t

    return v0 + a*t**2/2


print(calcVolEsfera(1))
print(calcVolEsfera(2))

print(CalcDistanciaMRUA(2,10,10,50))
print(CalcDistanciaMRUA(0,9,1,9.5))
print(CalcDistanciaMRUA(4,9,4,25))
