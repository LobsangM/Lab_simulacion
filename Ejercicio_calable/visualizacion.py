import matplotlib.pyplot as plt

def graficar_histogramas(v0, g, ranges, angles_deg, valid_angles):
    fig, axs = plt.subplots(2, 3, figsize=(18, 8))

    axs[0, 0].hist(v0, bins=100, color='skyblue', edgecolor='black')
    axs[0, 0].set_title("Distribución de la velocidad inicial $v_0$")
    axs[0, 0].set_xlabel("Velocidad (m/s)")
    axs[0, 0].set_ylabel("Frecuencia")
    axs[0, 0].grid(True)

    axs[0, 1].hist(g, bins=100, color='lightcoral', edgecolor='black')
    axs[0, 1].set_title("Distribución de la gravedad $g$")
    axs[0, 1].set_xlabel("Gravedad (m/s²)")
    axs[0, 1].set_ylabel("Frecuencia")
    axs[0, 1].grid(True)

    axs[0, 2].hist(ranges, bins=100, color='goldenrod', edgecolor='black')
    axs[0, 2].set_title("Distribución del alcance $R$")
    axs[0, 2].set_xlabel("Alcance (m)")
    axs[0, 2].set_ylabel("Frecuencia")
    axs[0, 2].grid(True)

    axs[1, 0].hist(angles_deg, bins=100, color='lightgray', edgecolor='black')
    axs[1, 0].set_title("Distribución de todos los ángulos generados")
    axs[1, 0].set_xlabel("Ángulo (°)")
    axs[1, 0].set_ylabel("Frecuencia")
    axs[1, 0].grid(True)

    axs[1, 1].hist(valid_angles, bins=100, color='lightgreen', edgecolor='black')
    axs[1, 1].set_title("Ángulos que cumplen con el rango objetivo")
    axs[1, 1].set_xlabel("Ángulo (°)")
    axs[1, 1].set_ylabel("Frecuencia")
    axs[1, 1].grid(True)

    axs[1, 2].axis('off')

    plt.tight_layout()
    plt.show()