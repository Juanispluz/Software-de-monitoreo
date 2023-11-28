import csv
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from opcion1 import leer_configuracion


def leer_datos_ambientales():
    datos_ambientales = []
    with open("utils\Datos_ambientales.txt", "r") as file:
        next(file)  # Saltar la primera línea que contiene los encabezados
        for line in file:
            datos = line.strip().split(',')
            datos_ambientales.append(datos)
    return datos_ambientales

def calcular_estadisticas_diarias(datos_ambientales, hora_minima, hora_maxima):
    estadisticas_diarias = {'temperatura': {'min': [], 'promedio': [], 'max': []},
                            'humedad': {'min': [], 'promedio': [], 'max': []},
                            'radiacion': {'min': [], 'promedio': [], 'max': []},
                            'viento': {'min': [], 'promedio': [], 'max': []}}

    for datos in datos_ambientales:
        hora = int(datos[0][:2])
        if hora_minima <= hora <= hora_maxima:
            fecha_hora = f"{datos[1]} {datos[0]}"
            fecha_hora_dt = datetime.strptime(fecha_hora, "%d/%m/%Y %H:%M:%S")

            estadisticas_diarias['temperatura']['min'].append(float(datos[2]))
            estadisticas_diarias['temperatura']['promedio'].append(float(datos[2]))
            estadisticas_diarias['temperatura']['max'].append(float(datos[2]))

            estadisticas_diarias['humedad']['min'].append(float(datos[3]))
            estadisticas_diarias['humedad']['promedio'].append(float(datos[3]))
            estadisticas_diarias['humedad']['max'].append(float(datos[3]))

            estadisticas_diarias['radiacion']['min'].append(float(datos[4]))
            estadisticas_diarias['radiacion']['promedio'].append(float(datos[4]))
            estadisticas_diarias['radiacion']['max'].append(float(datos[4]))

            estadisticas_diarias['viento']['min'].append(float(datos[5]))
            estadisticas_diarias['viento']['promedio'].append(float(datos[5]))
            estadisticas_diarias['viento']['max'].append(float(datos[5]))

    return estadisticas_diarias

def graficar_temperaturas(estadisticas_temperatura):
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))
    fig.suptitle("Gráfico de Temperaturas")

    axs[0].plot(estadisticas_temperatura['min'], label='Mínimo')
    axs[0].set_ylabel("Temperatura (°C)")
    axs[0].legend()

    axs[1].plot(estadisticas_temperatura['promedio'], label='Promedio')
    axs[1].set_ylabel("Temperatura (°C)")
    axs[1].legend()

    axs[2].plot(estadisticas_temperatura['max'], label='Máximo')
    axs[2].set_xlabel("Días")
    axs[2].set_ylabel("Temperatura (°C)")
    axs[2].legend()

    plt.show()

def graficar_humedades(estadisticas_humedad):
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))
    fig.suptitle("Gráfico de Humedades Relativas")

    axs[0].plot(estadisticas_humedad['min'], label='Mínimo')
    axs[0].set_ylabel("Humedad Relativa (%)")
    axs[0].legend()

    axs[1].plot(estadisticas_humedad['promedio'], label='Promedio')
    axs[1].set_ylabel("Humedad Relativa (%)")
    axs[1].legend()

    axs[2].plot(estadisticas_humedad['max'], label='Máximo')
    axs[2].set_xlabel("Días")
    axs[2].set_ylabel("Humedad Relativa (%)")
    axs[2].legend()

    plt.show()

def graficar_radiacion(estadisticas_radiacion):
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))
    fig.suptitle("Gráfico de Radiación Solar")

    axs[0].plot(estadisticas_radiacion['min'], label='Mínimo')
    axs[0].set_ylabel("Radiación Solar (W/m²)")
    axs[0].legend()

    axs[1].plot(estadisticas_radiacion['promedio'], label='Promedio')
    axs[1].set_ylabel("Radiación Solar (W/m²)")
    axs[1].legend()

    axs[2].plot(estadisticas_radiacion['max'], label='Máximo')
    axs[2].set_xlabel("Días")
    axs[2].set_ylabel("Radiación Solar (W/m²)")
    axs[2].legend()

    plt.show()

def graficar_viento(estadisticas_viento):
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))
    fig.suptitle("Gráfico de Velocidad del Viento")

    axs[0].plot(estadisticas_viento['min'], label='Mínimo')
    axs[0].set_ylabel("Velocidad del Viento (m/s)")
    axs[0].legend()

    axs[1].plot(estadisticas_viento['promedio'], label='Promedio')
    axs[1].set_ylabel("Velocidad del Viento (m/s)")
    axs[1].legend()

    axs[2].plot(estadisticas_viento['max'], label='Máximo')
    axs[2].set_xlabel("Días")
    axs[2].set_ylabel("Velocidad del Viento (m/s)")
    axs[2].legend()

    plt.show()

def graficar_todas_las_variables(estadisticas_diarias, rango_fechas):
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Gráficos de Todas las Variables")

    axs[0, 0].plot(estadisticas_diarias['temperatura']['min'], label='Temperatura Mínima')
    axs[0, 0].plot(estadisticas_diarias['temperatura']['promedio'], label='Temperatura Promedio')
    axs[0, 0].plot(estadisticas_diarias['temperatura']['max'], label='Temperatura Máxima')
    axs[0, 0].set_title("Temperatura")
    axs[0, 0].legend()

    axs[0, 1].plot(estadisticas_diarias['humedad']['min'], label='Humedad Mínima')
    axs[0, 1].plot(estadisticas_diarias['humedad']['promedio'], label='Humedad Promedio')
    axs[0, 1].plot(estadisticas_diarias['humedad']['max'], label='Humedad Máxima')
    axs[0, 1].set_title("Humedad Relativa")
    axs[0, 1].legend()

    axs[1, 0].plot(estadisticas_diarias['radiacion']['min'], label='Radiación Mínima')
    axs[1, 0].plot(estadisticas_diarias['radiacion']['promedio'], label='Radiación Promedio')
    axs[1, 0].plot(estadisticas_diarias['radiacion']['max'], label='Radiación Máxima')
    axs[1, 0].set_title("Radiación Solar")
    axs[1, 0].legend()

    axs[1, 1].plot(estadisticas_diarias['viento']['min'], label='Viento Mínimo')
    axs[1, 1].plot(estadisticas_diarias['viento']['promedio'], label='Viento Promedio')
    axs[1, 1].plot(estadisticas_diarias['viento']['max'], label='Viento Máximo')
    axs[1, 1].set_title("Velocidad del Viento")
    axs[1, 1].legend()

    plt.show()

def graficos():
    configuracion_actual = leer_configuracion()
    
    if configuracion_actual is None:
        print("No se encontró el archivo de configuración. Ejecute la opción de Configuración primero.")
        return

    datos_ambientales = leer_datos_ambientales()
    estadisticas_diarias = calcular_estadisticas_diarias(datos_ambientales, configuracion_actual['hora_minima'], configuracion_actual['hora_maxima'])

    while True:
        print("\nMenú Gráficos:")
        print("a. Gráfico independiente de temperaturas")
        print("b. Gráfico independiente de humedades relativas")
        print("c. Gráfico independiente de radiación solar")
        print("d. Gráfico independiente de velocidad del viento")
        print("e. En una misma figura (subplot) presentar todas las gráficas anteriores para un rango de fechas")
        print("f. Regresar")

        opcion = input("Seleccione una opción: ")

        if opcion == "a":
            graficar_temperaturas(estadisticas_diarias['temperatura'])
        elif opcion == "b":
            graficar_humedades(estadisticas_diarias['humedad'])
        elif opcion == "c":
            graficar_radiacion(estadisticas_diarias['radiacion'])
        elif opcion == "d":
            graficar_viento(estadisticas_diarias['viento'])
        elif opcion == "e":
            try:
                fecha_inicio = datetime.strptime(input("Ingrese la fecha de inicio (dd/mm/yyyy): "), "%d/%m/%Y")
                fecha_fin = datetime.strptime(input("Ingrese la fecha de fin (dd/mm/yyyy): "), "%d/%m/%Y")
                rango_fechas = [fecha_inicio.date() + timedelta(days=i) for i in range((fecha_fin - fecha_inicio).days + 1)]
                graficar_todas_las_variables(estadisticas_diarias, rango_fechas)
            except ValueError:
                print("Formato de fecha incorrecto. Utilice el formato dd/mm/yyyy.")
        elif opcion == "f":
            break
        else:
            print(f'La opción "{opcion}" no es válida. Por favor, seleccione una opción de "a" hasta "f".')