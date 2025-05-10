# Datos
profundidad = [100, 500, 1000, 2000, 2890, 2900, 4000, 5000, 5500, 6470]  # en km
rho = [3.38, 3.85, 4.58, 5.12, 5.56, 9.90, 11.32, 12.12, 12.92, 13.09]  # en 1000 kg/m^3
alpha = [8.05, 9.65, 11.46, 12.82, 13.72, 8.07, 9.51, 10.30, 11.14, 11.26]  # en km/s
beta = [4.45, 5.22, 6.38, 6.92, 7.27, 0, 0, 0, 3.58, 3.67]  # en km/s

# Funciones para calcular
def calcular_mu(rho, beta):
    return rho * (beta**2)

def calcular_K(rho, alpha, beta):
    return rho * (alpha**2 - (4/3)*(beta**2))

def calcular_nu(K, mu):
    return (3*K - 2*mu) / (2*(3*K + mu))

# Cálculo
print(f"{'Prof (km)':>8} {'mu (GPa)':>10} {'K (GPa)':>10} {'nu':>8}")
for i in range(len(profundidad)):
    rho_real = rho[i] * 1000  # Convertir a kg/m³
    alpha_real = alpha[i] * 1000  # Convertir a m/s
    beta_real = beta[i] * 1000  # Convertir a m/s

    if beta_real != 0:
        mu = calcular_mu(rho_real, beta_real) / 1e9  # en GPa
        K = calcular_K(rho_real, alpha_real, beta_real) / 1e9  # en GPa
        nu = calcular_nu(K, mu)
        print(f"{profundidad[i]:>8} {mu:10.2f} {K:10.2f} {nu:8.2f}")
    else:
        print(f"{profundidad[i]:>8} {'-':>10} {'-':>10} {'-':>8}")
