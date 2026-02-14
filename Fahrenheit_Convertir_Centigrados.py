def Fahrenheit_Convertir_Centigrados (Grado_Fahrenheit: float)->float:
    Conversion = (Grado_Fahrenheit - 32) * (5/9)
    return Conversion
F = float (input ("Digite los grados en Fahrenheit: "))
print ("Los grados en centigrados son ", str (Fahrenheit_Convertir_Centigrados(F)))

