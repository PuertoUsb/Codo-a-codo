
def agregarRetiro(colRetiros, listaLibros):
    legajo = input("\n Ingrese el numero de legajo: ")
    apellidoNombre = input("\n Ingrese nombre y apellido: ")
    dni = input("\n Ingrese el D.N.I: \n")
    libroRetirado = input("Ingrese el nombre del libro a retirar: ")

    for unLibro in listaLibros:
       if (unLibro == libroRetirado):
           nuevoRetiro = {
            "legajo": legajo,
            "apellido_nombre": apellidoNombre, 
            "dni": dni,
            "libro_retirado": libroRetirado,
            }
           colRetiros.append(nuevoRetiro)
           print ("\n Retiro agregado exitosamente.")
           break
    else:
        print("\n El libro no se encuentra en la biblioteca.")


def eliminarRetiro(colRetiros,numLegajo):
    encontrado = False
    for unRetiro in colRetiros:
        if (unRetiro["legajo"] == numLegajo):
            colRetiros.remove(unRetiro)
            print(F"\n Retiro con legajo {numLegajo} legajo eliminado.")
            encontrado = True
            break
    if (not encontrado):
        print(F"\n No se encontró un retiro con el legajo {numLegajo}.")


def actualizarRetiro(colRetiros, numLegajo):
    encontrado = False
    for unRetiro in colRetiros:
        if (unRetiro["legajo"] == numLegajo):
            nuevoNombreApellido = input("\n Ingrese nuevo nombre y apellido: ")
            nuevoDni = input("\n Ingrese nuevo dni: \n")
            nuevoLibroRetirado = input("\n Ingrese el nombre del libro a retirar: ")
        
            unRetiro["apellido_nombre"] = nuevoNombreApellido
            unRetiro["dni"] = nuevoDni
            unRetiro["libro_retirado"] = nuevoLibroRetirado

            print(f"\n Retiro con legajo {numLegajo} actualizado correctamente.")
            encontrado = True
            break 
    if (not encontrado):
        print(F"\n No se encontró un retiro con el legajo {numLegajo}.")


def mostrarUnRetiro(colRetiros, numLegajo):
    encontrado = False
    for unRetiro in colRetiros:
        if (unRetiro["legajo"] == numLegajo):
            print(f"Legajo: {unRetiro['legajo']}")
            print(f"Nombre y apellido: {unRetiro['apellido_nombre']}")
            print(f"DNI: {unRetiro['dni']}")
            print(f"Libro retirado: {unRetiro['libro_retirado']}")
            encontrado = True
            break
    if (not encontrado):
        print(F"\n No se encontró un retiro con el legajo {numLegajo}.")

def mostrarTodosLosRetiros(colRetiros):
    if (len(colRetiros) == 0):
        print("\n No hay retiros registrados.")
    else:
        print("\n Retiros registrados: ")
        for unRetiro in colRetiros:
    
            print(f"\n Legajo: {unRetiro['legajo']} ")
            print(f"\n Nombre y apellido: {unRetiro['apellido_nombre']}")
            print(f"\n DNI: {unRetiro['dni']}")
            print(f"\n Libro retirado: {unRetiro['libro_retirado']}")
            print("\n ======================================")


