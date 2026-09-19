#Declarando un arreglo
numeros=[10,20,30,40,50]
print(numeros[2])

#Reasigne el valor de la p. 3 a 15
numeros[3] = 15
print(numeros)

#Agregamos un valor al final del arreglo
numeros.append(50)
print(numeros)

#Eliminamos un valor del arreglo por posición
numeros.pop(1)
print(numeros)

#Eliminamos un valor del arreglo por número
numeros.remove(30)
print(numeros)

frutas=["Mango", "Manzana", "Uva", "Pera", "Macuya"]
frutas.remove("Uva")
print(frutas)

frutas.pop(3)
print(frutas)

frutas.append("Kiwi")
print(frutas)

frutas[2] ="Fresa"
print(frutas)

arreglo = []
n = int(input("Ingrese el tamaño del arreglo: "))
arreglo.append(int(input("Ingrese el valor 0 ")))
print(arreglo)

