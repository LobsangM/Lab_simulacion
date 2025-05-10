import numpy as np

def calcular_alcance(v0, g, angles_rad):
    return (v0 ** 2) * np.sin(2 * angles_rad) / g

def filtrar_angulos(ranges, angles_deg, d_min, d_max):
    flrt = (ranges >= d_min) & (ranges <= d_max)
    return angles_deg[flrt]