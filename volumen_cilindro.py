def volumen_cilindro(radio_base: float, altura: float) -> float:
    area_base = 3.1416 * radio_base * radio_base
    return area_base * altura

r = float (input ("Digite el radio: "))
a = float (input("Digite la altura: "))
print ("El volumen es ", str (volumen_cilindro(r, a)) )



