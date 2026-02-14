def invertir_numero(numero: int) -> int:
    # Extrae el dígito de las unidades
    unidades = numero % 10  
    numero //= 10  # Elimina la última cifra del número
    
    # Extrae el dígito de las decenas
    decenas = numero % 10  
    numero //= 10  # Elimina la última cifra del número
    
    # Extrae el dígito de las centenas
    centenas = numero % 10  
    numero //= 10  # Elimina la última cifra del número
    
    # Extrae el dígito de los millares
    millares = numero % 10  

    # Construye el número invertido concatenando los dígitos en orden inverso
    inverso = str(unidades) + str(decenas) + str(centenas) + str(millares)

    # Convierte el resultado a un entero y lo retorna
    return int(inverso)

N = int ( input ("Digite el numero a invertir: "))
print ("El numero invertido es ", str (invertir_numero(N)))
