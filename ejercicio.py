terminar = 0
while terminar == 0:
    print("Elige a donde te quieres meter:")
    print("1. Pilas:")
    print("2. Colas:")
    print("3. Terminar el programa:")
    opcion = input("Escribe el numero correspondiente ")
    if opcion == "1":
        Alumnos=[]
        Alumnos.append("Antonio")
        Alumnos.append("Karla")
        Alumnos.append("Santiago")
        print("Pila actual ", Alumnos)
        SalirP = 0
        while SalirP == 0:
            print("1. Insertar en la pila:")
            print("2. Borrar en la pila")
            print("3. Imprimir pila")
            print("4. Salir de aqui")
            Epilas = input("Escribe el numero segun que quieres hacer ")
            if Epilas == "1":
                insercion = input("Escribe el nombre del alumno que quieres agregar ")
                Alumnos.append(insercion)
                print("Alumno agregado")
            elif Epilas == "2":
                if Alumnos:
                    Alumnos.pop()
                    print("Ultimo alumno borrado")
                else:
                    print("La pila esta vacia")
            elif Epilas == "3":
                print("Pila actual ", Alumnos)
            elif Epilas == "4":
                print("Saliendo de pilas")
                SalirP = 1;    
            else:
                print("Elige una opcion valida")
    elif opcion == "2":
        from collections import deque
        Colores = deque(["Azul", "Amarillo", "Rojo"])
        print("Cola actual ", Colores)
        SalirC = 0
        while SalirC == 0:
            print("1. Insertar en la cola:")
            print("2. Borrar en la cola")
            print("3. Imprimir cola")
            print("4. Salir de aqui")
            Ecolas = input("Escribe el numero segun que quieres hacer ")
            if Ecolas == "1":
                insercion = input("Escribe el nombre del color que quieres agregar ")
                Colores.append(insercion)
                print("Color agregado")
            elif Ecolas == "2":
                if Colores:
                    Colores.popleft()
                    print("Primer color borrado")
                else:
                    print("La cola esta vacia")
            elif Ecolas == "3":
                print("Cola actual ", Colores)
            elif Ecolas == "4":
                print("Saliendo de colas")
                SalirC = 1
            else:
                print("Elige una opcion valida")
    elif opcion == "3":
        print("Terminando operaciones")
        terminar = 1
    else:
        print("Elige una opcion valida")