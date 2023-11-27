import pandas as pd
from opcion1 import leer_configuracion, configurar_parametros, solicitar_contrasena, escribir_configuracion
from opcion2 import informacion_ambiental
from opcion3 import graficos
from opcion4 import estadisticas_descriptivas_por_dia
from opcion5 import  tiempo_ejecucion, start_time

if __name__ == "__main__":   
    while True:
        print("\nMenú Principal:")
        print("1. Configuración")
        print("2. Información Ambiental")
        print("3. Gráficos")
        print("4. Estadística Descriptiva")
        print("5. Tiempo de ejecución")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        data = pd.read_csv("utils\Datos_ambientales.txt")
        configuracion_actual = leer_configuracion()

        if opcion == "1":
            if solicitar_contrasena():         
                if configuracion_actual is None:
                    print("Configuración no encontrada. Se creará una nueva configuración predeterminada.")
                    configuracion_actual = {
                        'hora_minima': 0,
                        'hora_maxima': 23,
                        'limite_temperatura': 0.0,
                        'limite_humedad': 0.0,
                        'limite_radiacion': 0.0,
                        'limite_velocidad_viento': 0.0,
                    }
                    escribir_configuracion(configuracion_actual)

                configurar_parametros(configuracion_actual) 
            else:
                print("Contraseña incorrecta. Acceso denegado.")

        elif opcion == "2":
            if configuracion_actual:
                 informacion_ambiental(configuracion_actual)
            else:
                print("Error: Configuración no encontrada. Configure los parámetros primero.")

        elif opcion == "3":
              graficos()

        elif opcion == "4":
            fecha_ingresada = input("Ingrese la fecha en formato dd/mm/yyyy: ")
            estadisticas_descriptivas_por_dia(data, fecha_ingresada)
        
        elif opcion == "5":
            tiempo_ejecucion(start_time)

        elif opcion == "6":
            print("Saliendo del programa. Hasta luego.")
            break

        else:
            print(f'La opción "{opcion}" no es válida. Por favor, seleccione una opción del 1 al 6.')