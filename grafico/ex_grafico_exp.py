import matplotlib.pyplot as plt
import numpy as np

def funcao_exp(t):

    return 30*np.exp(-(1/3)*t)

t = np.linspace(0, 15, 200)

vo = funcao_exp(t)

#plotagem de grafico

plt.plot(t, vo, label=r'$f(x)=30e^{- \frac{1}{3}t}$', color='blue', linewidth=2)


plt.title("Tensão no Capacitor vs Tempo - Resposta Natural")
plt.xlabel("tempo")
plt.ylabel("vo(t)")

plt.legend()
plt.grid("True")

#Exibir gráfico
plt.show()
