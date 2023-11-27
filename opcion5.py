import datetime

# Definir una función llamada tiempo_ejecucion que toma el tiempo de inicio como argumento
def tiempo_ejecucion(start_time):
    end_time = datetime.datetime.now()  # Obtiene la fecha y hora actuales como tiempo de finalización
    elapsed_time = end_time - start_time  # Calcula la diferencia de tiempo entre el inicio y el final

    # Dividir el tiempo transcurrido en horas, minutos y segundos
    hours, remainder = divmod(elapsed_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Formatear el tiempo para que tenga el formato HH:MM:SS
    elapsed_time_formatted = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)

    # Imprimir el tiempo transcurrido
    print(f"\nTiempo transcurrido: {elapsed_time_formatted}")

# Obtener el tiempo de inicio actual
start_time = datetime.datetime.now()

## Llamar a la función tiempo_ejecucion con el tiempo de inicio como argumento
# tiempo_ejecucion(start_time)