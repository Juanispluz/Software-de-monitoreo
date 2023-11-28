import csv
from datetime import datetime

def informacion_ambiental(config):
    while True:
        print("\nInformación Ambiental:")
        print("a. Número de días y mes con mayor temperatura excedida")
        print("b. Número de días y mes con mayor humedad excedida")
        print("c. Número de días y mes con mayor radiación excedida")
        print("d. Número de días y mes con mayor velocidad del viento excedida")
        print("e. Regresar al Menú Principal")

        opcion= input("Seleccione una opción (a-e): ")

        if opcion== "a":
            info = calcular_ocurrencias_mes(config, 'limite_temperatura', 2)
            mostrar_info("temperatura", info)
        elif opcion== "b":
            info = calcular_ocurrencias_mes(config, 'limite_humedad', 3)
            mostrar_info("humedad", info)
        elif opcion== "c":
            info = calcular_ocurrencias_mes(config, 'limite_radiacion', 4)
            mostrar_info("radiación solar", info)
        elif opcion== "d":
            info = calcular_ocurrencias_mes(config, 'limite_velocidad_viento', 5)
            mostrar_info("velocidad del viento", info)
        elif opcion== "e":
            break
        else:
            print(f'La opción "{opcion}" no es válida. Por favor, seleccione una opción de "a" hasta "e".')

def calcular_ocurrencias_mes(config, limite, columna):
    try:
        with open("utils\Datos_ambientales.txt", newline='') as data_file:
            reader = csv.reader(data_file)
            next(reader)  # Saltar la primera fila que contiene los encabezados

            ocurrencias = {}
            for row in reader:
                fecha_str = row[1]
                fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
                mes = fecha.month

                hora_actual = int(row[0][:2])
                if config['hora_minima'] <= hora_actual <= config['hora_maxima']:
                    if float(row[columna]) > config[limite]:
                        if mes not in ocurrencias:
                            ocurrencias[mes] = set()
                        ocurrencias[mes].add(fecha.day)

            # Convertir el conjunto de días a la cantidad de días únicos
            for mes, dias in ocurrencias.items():
                ocurrencias[mes] = len(dias)

            return ocurrencias
    except FileNotFoundError:
        return None


def mostrar_info(parametro, info):
    if info is not None:
        if not info:
            print(f"No hay días donde la {parametro} exceda el límite.")
        else:
            mes_max = max(info, key=info.get)
            print(f"Número de días y mes con mayor {parametro} excedida:")
            print(f"Días: {info[mes_max]}, Mes: {mes_max}")
    else:
        print("No se encontró el archivo de datos ambientales.")