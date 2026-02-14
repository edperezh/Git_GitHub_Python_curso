def Centigrados_Convertir_Fahrenheit (Grado_Centigrados: float)->float:
    Conversion = (Grado_Centigrados * (9/5)) + 32
    return Conversion
F = float (input ("Digite los grados en Centigrados: "))
print ("Los grados en Fahrenheit son ", str (Centigrados_Convertir_Fahrenheit(F)))

def Convertir_Radianes_Grados (Radianes: float) -> float:
    Pi = 3.141592
    Grados = (360 * Radianes) / (2 * Pi)
    return Grados
R = float (input ("Digite la cantidad de radianes a convertir: "))
print ("Los grados son ", str (Convertir_Radianes_Grados(R)) )