import getpass

def leer_configuracion():
    try:
        with open("configs/configuracion.txt", "r") as config_file:
            config_data = config_file.readline().strip().split(",")
            return {
                'hora_minima': int(config_data[0]),
                'hora_maxima': int(config_data[1]),
                'limite_temperatura': float(config_data[2]),
                'limite_humedad': float(config_data[3]),
                'limite_radiacion': float(config_data[4]),
                'limite_velocidad_viento': float(config_data[5]),
            }
    except FileNotFoundError:
        return None

def escribir_configuracion(config):
    with open("configs/configuracion.txt", "w") as config_file:
        config_file.write(f"{config['hora_minima']},{config['hora_maxima']},"
                          f"{config['limite_temperatura']},{config['limite_humedad']},"
                          f"{config['limite_radiacion']},{config['limite_velocidad_viento']}")

def solicitar_contrasena():
    password = getpass.getpass("Ingrese la contraseña: ")
    # Verificar la contraseña (puedes cambiar la contraseña según tus necesidades)
    return password == "root"

def mostrar_valor_actual(opcion, configuracion):
    opciones = {
        'a': 'hora_minima',
        'b': 'hora_maxima',
        'c': 'limite_temperatura',
        'd': 'limite_humedad',
        'e': 'limite_radiacion',
        'f': 'limite_velocidad_viento',
    }
    print(f"\nValor actual de {opciones[opcion]}: {configuracion[opciones[opcion]]}")

def configurar_parametros(configuracion):
    while True:
        print("\nMenú de Configuración:")
        print("a. Hora mínima")
        print("b. Hora máxima")
        print("c. Límite temperatura")
        print("d. Límite humedad relativa")
        print("e. Límite radiación solar")
        print("f. Límite velocidad del viento")
        print("g. Regresar")

        opcion = input("Seleccione una opción: ").lower()

        if opcion in "abcdef":
            mostrar_valor_actual(opcion, configuracion)

        if opcion == "a":
            configurar_hora_minima(configuracion)
        elif opcion == "b":
            configurar_hora_maxima(configuracion)
        elif opcion == "c":
            configurar_limite_temperatura(configuracion)
        elif opcion == "d":
            configurar_limite_humedad(configuracion)
        elif opcion == "e":
            configurar_limite_radiacion(configuracion)
        elif opcion == "f":
            configurar_limite_velocidad_viento(configuracion)
        elif opcion == "g":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def configurar_hora_minima(configuracion):
    nueva_hora_minima = int(input("Ingrese la nueva hora mínima (0-23): "))
    configuracion['hora_minima'] = nueva_hora_minima
    escribir_configuracion(configuracion)

def configurar_hora_maxima(configuracion):
    nueva_hora_maxima = int(input("Ingrese la nueva hora máxima (0-23, mayor que la hora mínima): "))
    configuracion['hora_maxima'] = nueva_hora_maxima
    escribir_configuracion(configuracion)

def configurar_limite_temperatura(configuracion):
    nuevo_limite_temperatura = float(input("Ingrese el nuevo límite de temperatura: "))
    configuracion['limite_temperatura'] = nuevo_limite_temperatura
    escribir_configuracion(configuracion)

def configurar_limite_humedad(configuracion):
    nuevo_limite_humedad = float(input("Ingrese el nuevo límite de humedad relativa: "))
    configuracion['limite_humedad'] = nuevo_limite_humedad
    escribir_configuracion(configuracion)

def configurar_limite_radiacion(configuracion):
    nuevo_limite_radiacion = float(input("Ingrese el nuevo límite de radiación solar: "))
    configuracion['limite_radiacion'] = nuevo_limite_radiacion
    escribir_configuracion(configuracion)

def configurar_limite_velocidad_viento(configuracion):
    nuevo_limite_velocidad_viento = float(input("Ingrese el nuevo límite de velocidad del viento: "))
    configuracion['limite_velocidad_viento'] = nuevo_limite_velocidad_viento
    escribir_configuracion(configuracion)