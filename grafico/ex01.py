#Exemplo criacao de grafico de barras
import matplotlib.pyplot as plt

componentes = ["RAM", "CPU", "GPU", "Cooler"]
consumo = [5, 65, 120, 15]

plt.barh(componentes, consumo, label="Computador 1", color="orange")

plt.title("Consumo vs Componentes")

plt.xlabel("Consumo [W]")
plt.ylabel("Componentes")

plt.legend()
plt.grid(True)
plt.show()




