import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class MonteCarloPi:
    def __init__(self, num_puntos):
        self.num_puntos = num_puntos
    
    def calcular_pi(self):
        x = np.random.uniform(-1, 1, self.num_puntos)
        y = np.random.uniform(-1, 1, self.num_puntos)
        dentro_circulo = np.sum(x**2 + y**2 <= 1)
        return 4 * dentro_circulo / self.num_puntos

if __name__ == "__main__":
    num_experimentos = 500
    num_puntos = 100000
    valores_pi = np.array([MonteCarloPi(num_puntos).calcular_pi() for _ in range(num_experimentos)])
    
    media = np.mean(valores_pi)
    varianza = np.var(valores_pi)
    desviacion_std = np.std(valores_pi)
    
    print(f"Media: {media}")
    print(f"Varianza: {varianza}")
    print(f"Desviación estándar: {desviacion_std}")

    
    plt.figure(figsize=(8,6))
    sns.histplot(valores_pi, bins=20, kde=True, color='blue', alpha=0.7)
    plt.axvline(x=media, color='r', linestyle='--', label=f"Media: {media:.5f}")
    plt.axvline(x=3.1416, color='g', linestyle='--', label="Valor de pi")
    plt.xlabel("Estimación de pi")
    plt.ylabel("Frecuencia")
    plt.title("Distribución de valores de pi")
    plt.legend()
    plt.show()


