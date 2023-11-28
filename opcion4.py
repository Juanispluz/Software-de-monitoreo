import pandas as pd

# Función para verificar el formato de fecha
def validar_formato_fecha(fecha):
    try:
        pd.to_datetime(fecha, format='%d/%m/%Y')
        return True
    except ValueError:
        return False

# Función para obtener estadísticas descriptivas para un día específico
def estadisticas_descriptivas_por_dia(df, fecha):
    # Validar el formato de fecha
    if not validar_formato_fecha(fecha):
        print("Formato de fecha incorrecto. Utilice el formato dd/mm/yyyy.")
        return

    # Convertir la fecha al formato 'YYYY-MM-DD' para la filtración
    fecha_formato_correcto = pd.to_datetime(fecha, format='%d/%m/%Y').strftime('%d/%m/%Y')

    # Filtrar datos para el día específico
    datos_dia = df[df['Fecha'] == fecha_formato_correcto]

    if datos_dia.empty:
        print(f"No hay datos disponibles para la fecha {fecha}")
        return

    while True:
        print("\nSeleccione una variable para obtener estadísticas descriptivas:")
        print("a. Temperatura")
        print("b. Humedad relativa")
        print("c. Radiación solar")
        print("d. Velocidad del viento")
        print("e. Regresar")

        opcion = input("Seleccione una opción: ")

        if opcion == "a":
            variable = 'T_Amb'
        elif opcion == "b":
            variable = 'HR_Amb'
        elif opcion == "c":
            variable = 'Rad'
        elif opcion == "d":
            variable = 'Vel'
        elif opcion == "e":
            break
        else:
            print(f'La opción "{opcion}" no es válida. Por favor, seleccione una opción de "a" hasta "e".')
            continue

        # Calcular estadísticas descriptivas
        promedio = datos_dia[variable].mean()
        desviacion_estandar = datos_dia[variable].std()
        valor_minimo = datos_dia[variable].min()
        valor_maximo = datos_dia[variable].max()

        # Mostrar resultados
        print(f"\nEstadísticas de {variable} para el día {fecha}:")
        print(f"Promedio: {promedio:.2f}")
        print(f"Desviación estándar: {desviacion_estandar:.2f}")
        print(f"Min: {valor_minimo:.2f}")
        print(f"Max: {valor_maximo:.2f}")
