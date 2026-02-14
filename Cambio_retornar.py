"""Considere el software que se ejecuta en una máquina expendedora. Una de las tareas que debe realizar
es determinar cuánto cambio debe entregarle al cliente luego de que paga. Escriba una función que recibe
la cantidad de dinero (en pesos) a dar como cambio al cliente y retorne un mensaje con la cantidad de
monedas de cada denominación que deben ser entregadas, teniendo en cuenta que el cambio se debe otorgar
con la menor cantidad de monedas posible.

La máquina cuenta con monedas de 500, 200, 100 y 50 pesos, y el cambio total se entregará con monedas
de estas denominaciones. El mensaje retornado DEBE seguir el siguiente formato: “A,B,C,D” (sin espacios
intermedios) donde A, B, C y D son la cantidad de monedas de 500, 200, 100 y 50, respectivamente."""

def calcular_cambio (x):
    cambio = x//500
    return cambio
# intrucciones:
dinero_recibido = int(input ('DINERO RECIBIDO POR LA MAQUINA ES: '))
m_500 = dinero_recibido // 500
m500 = dinero_recibido-(m_500*500)
m_200 = m500 // 200
m200 = m500-(m_200*200) 
m_100 = m200 // 100
m100 = m200-(m_100*100)
m_50 = m100 // 50
print ('monedas de 500 en total:',calcular_cambio(dinero_recibido),',', 'monedas de 200:',m_200,',', 'monedas de 100:',m_100,',',
       'monedas de 50:',',',m_50 )
