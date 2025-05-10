import numpy as np

def generar_variables(params):
    N = params['N']
    v0 = np.random.normal(params['v0_mean'], params['v0_mean'] * params['v0_std_percent'], N)
    g = np.random.normal(params['g_mean'], params['g_std'], N)
    angles_deg = np.random.uniform(params['angle_min_deg'], params['angle_max_deg'], N)
    angles_rad = np.radians(angles_deg)
    return v0, g, angles_deg, angles_rad