from parametros import cargar_parametros
from generador import generar_variables
from simulador import calcular_alcance, filtrar_angulos
from visualizacion import graficar_histogramas

def main():
    params = cargar_parametros()
    
    v0, g, angles_deg, angles_rad = generar_variables(params)
    ranges = calcular_alcance(v0, g, angles_rad)
    valid_angles = filtrar_angulos(ranges, angles_deg, params['d_min'], params['d_max'])

    if len(valid_angles) == 0:
        print("No se encontró ningún ángulo que cumpla con el rango especificado.")
    else:
        print(f"Ángulo mínimo válido: {min(valid_angles):.2f}°")
        print(f"Ángulo máximo válido: {max(valid_angles):.2f}°")
        print(f"Número de casos válidos: {len(valid_angles)}")

    graficar_histogramas(v0, g, ranges, angles_deg, valid_angles)

if __name__ == "__main__":
    main()