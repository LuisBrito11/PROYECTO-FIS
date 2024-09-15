import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress

# Función para cargar los datos
def cargar_datos(archivo_csv):
    # Leer datos del archivo CSV
    datos = pd.read_csv(archivo_csv)
    # Extraer columnas de fuerza y aceleración
    fuerza = datos['fuerza'].values
    aceleracion = datos['aceleracion'].values
    return fuerza, aceleracion

# Función para ajustar los datos a una recta (y = mx + b)
def ajuste_lineal(fuerza, aceleracion):
    # Ajuste lineal
    pendiente, intercepto, r_value, p_value, std_err = linregress(aceleracion, fuerza)
    return pendiente, intercepto, std_err

# Función para graficar los datos y el ajuste
def graficar_datos(fuerza, aceleracion, pendiente, intercepto):
    plt.figure(figsize=(8, 6))
    # Gráfica de los datos experimentales
    plt.scatter(aceleracion, fuerza, label='Datos experimentales', color='blue')
    # Gráfica de la línea de ajuste
    plt.plot(aceleracion, pendiente * aceleracion + intercepto, label=f'Ajuste lineal: F = {pendiente:.2f} * a + {intercepto:.2f}', color='red')
    # Etiquetas y título
    plt.xlabel('Aceleración (m/s^2)')
    plt.ylabel('Fuerza (N)')
    plt.title('Fuerza Aplicada vs. Aceleración')
    plt.legend()
    plt.grid(True)
    plt.show()

# Función principal para el análisis de datos
def analizar_datos(archivo_csv):
    # Cargar datos experimentales
    fuerza, aceleracion = cargar_datos(archivo_csv)
    # Realizar ajuste lineal
    pendiente, intercepto, std_err = ajuste_lineal(fuerza, aceleracion)
    # Calcular la masa (pendiente)
    masa = pendiente
    # Calcular la incertidumbre de la masa
    incertidumbre_masa = std_err
    # Mostrar resultados
    print(f'Masa calculada (pendiente): {masa:.2f} kg')
    print(f'Incertidumbre de la masa: ±{incertidumbre_masa:.2f} kg')
    # Graficar datos y ajuste
    graficar_datos(fuerza, aceleracion, pendiente, intercepto)

# Ruta al archivo CSV con los datos experimentales
archivo_csv = 'datos_experimento.csv'

# Ejecutar el análisis de datos
analizar_datos(archivo_csv)
