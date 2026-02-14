def calcular_BMI (x,y):
    BMI = ((x)/(y**2))*720
    return float (round ((BMI),2))

# intrucciones:

peso_lb = round ((float(input('introduce el peso en libras de la persona: '))),2)
altura_inch = round ((float(input('introduce la altura en pulgadas de la persona: '))),2)

print (calcular_BMI(peso_lb, altura_inch))

# Como el peso es en libra la tabla para verificar tu BMI es otra que con el peso en kilogramos

# comentario sobre el BMI de Rafael