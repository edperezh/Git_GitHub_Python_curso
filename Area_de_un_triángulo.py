import math

def area_triangulo(s1: float, s2: float, s3: float) -> float:
    """
    Calcula el área de un triángulo dados sus tres lados (s1, s2, s3),
    utilizando la fórmula de Herón. Retorna el área redondeada a
    una cifra decimal.
     """  
    s = (s1 + s2 + s3) / 2  # Semiperímetro
    area = ((s * (s - s1) * (s - s2) * (s - s3)))**1/2
    return round(area, 1)

# Solicita al usuario los valores de los lados del triángulo
s1 = float(input("Ingresa la longitud del primer lado: "))
s2 = float(input("Ingresa la longitud del segundo lado: "))
s3 = float(input("Ingresa la longitud del tercer lado: "))

# Calcula el área y la muestra en pantalla
resultado = area_triangulo(s1, s2, s3)
print(f"El área del triángulo es: {resultado}")

