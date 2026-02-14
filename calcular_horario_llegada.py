def calcular_horario_llegada(hora_salida, minuto_salida, segundo_salida, duracion_horas, duracion_minutos, duracion_segundos):
    # Convertir todo a segundos
    total_segundos_salida = hora_salida * 3600 + minuto_salida * 60 + segundo_salida
    total_segundos_duracion = duracion_horas * 3600 + duracion_minutos * 60 + duracion_segundos

    # Sumar la duración al tiempo de salida
    total_segundos_llegada = total_segundos_salida + total_segundos_duracion

    # Calcular las horas, minutos y segundos de la hora de llegada
    horas_llegada = total_segundos_llegada // 3600
    minutos_llegada = (total_segundos_llegada % 3600) // 60
    segundos_llegada = total_segundos_llegada % 60

    # Crear la cadena de la hora de llegada en el formato deseado
    hora_llegada_str = f"{horas_llegada:02}:{minutos_llegada:02}:{segundos_llegada:02}"
    
    return hora_llegada_str

# Ejemplo de uso
hora_salida = int(input('ingrese hora de salida de 0 a 23:')) 
minuto_salida = int(input('ingrese minuto de salida de 0 a 60:')) 
segundo_salida = int(input('ingrese segundo de salida de 0 a 60:')) 
duracion_horas = int(input('ingrese horas de duracion de 0 a 24:')) 
duracion_minutos = int(input('ingrese minutos de duracion de 0 a 60:')) 
duracion_segundos = int(input('ingrese segundos de duracion de 0 a 60:')) 

hora_llegada = calcular_horario_llegada(hora_salida, minuto_salida, segundo_salida, duracion_horas, duracion_minutos, duracion_segundos)
print(hora_llegada)  