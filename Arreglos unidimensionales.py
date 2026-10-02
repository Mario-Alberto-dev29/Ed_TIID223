"""
Captura 1:
numeros = [10, 20, 30, 40, 50]
print(numeros[2])
"""

"""
Captura 2:
numeros = [10, 20, 30, 40, 50]
numeros[2] = 100
print(numeros)
"""

"""
Captura 3:
numeros = [10, 20, 30, 40, 50]
numeros [2] = 100
numeros.append([60])
print(numeros)
"""

"""
Captura 4:
numeros = [10, 20, 30, 40, 50]
numeros [2] = 100
numeros.append([60, 70])
print(numeros[5][0])

"""

"""
Opcion 1:
numeros = [10, 20, 30, 40, 50]
numeros [2] = 100
numeros.append(60)
numeros.append(70)
print(numeros)

"""

"""
Opcion 2:
numeros = [10, 20, 30, 40, 50]
numeros [2] = 100
numeros.append([60, 70])
print(numeros[5][0])

"""

"""
Captura 5

Numeros = [10, 20, 30, 40]
Numeros.insert(2, 25)
print(Numeros)

"""

""""
Captura 6
numeros = [10, 20, 30, 40]
numeros = numeros + [50]
print(numeros)
"""

""""
numeros = [10, 20, 30, 40]
numeros = numeros + [50, 60, 70]
print(numeros)
"""

"""
Ejemplos:
numeros = [10, 20, 30]
numeros.extend([40, 50, 60])
print(numeros)

numeros = [10, 20, 30]
otros_numeros = [40, 50, 60]
numeros.extend(otros_numeros)
print(numeros)
"""

"""
Experimento:
numeros = [10, 20, 30]
numeros[len(numeros):] = [40]
print(numeros)
print(len(numeros))
"""

"""
Ejercicio 1:
calificaciones = [70, 85, 90, 65]
calificaciones.append(95)
calificaciones.insert(2, 80)
print(calificaciones)
"""

"""
colores = ["Azul", "Amarillo", "Rosa"] 
colores.extend(["Verde", "Morado", "Rojo"])
colores.append("negro")
print(colores[6])
"""

numeros = [10, 20, 30, 40] 
numeros.insert(2, 95)
numeros.append(50)
numeros.append(67)

i = 0

while (i < len(numeros)):
    print("El número en la posición " + str(i) + " es " + str(numeros[i]))
    i += 1

