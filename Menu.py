
from Funciones import agregarRetiro, eliminarRetiro, actualizarRetiro, mostrarUnRetiro, mostrarTodosLosRetiros

#creo esta coleccion para ya tener datos cargados
colRetiros =[
        {
            "legajo": "1",
            "apellido_nombre": "Perez, Juan",
            "dni": "12345678",
            "libro_retirado": "Libro1"
        },
        {
            "legajo": "2",
            "apellido_nombre": "Gomez, Ana",
            "dni": "23456789",
            "libro_retirado": "Libro2"
        },
        {
            "legajo": "3",
            "apellido_nombre": "Lopez, Maria",
            "dni": "87654824",
            "libro_retirado": "Libro3"
        },
        {
            "legajo": "4",
            "apellido_nombre": "Martinez, Luis",
            "dni": "121548674",
            "libro_retirado": "Libro4"
        },
        {
            "legajo": "5",
            "apellido_nombre": "Fernandez, Carlos",
            "dni": "544654587",
            "libro_retirado": "Libro5"
        },
    ]

#creo esta coleccion para ya tener datos cargados
librosDisponibles = ["libro1", "libro2", "libro3", "libro4", "libro5"
                    ,"libro6", "libro7", "libro8", "libro9", "libro10"]


def dar_bienvenida():
    mensaje = """
╔═════════════════════════════════════╗
║           Bienvenido/a al           ║
║ SISTEMA DE GESTION DE LA BIBLIOTECA ║
╚═════════════════════════════════════╝
    """
    print(mensaje)
    

def menu_pincipal():
    print("\n**************** Menu principal de la biblioteca ****************\n")
    print("1. Agregar persona a retiro de libros\n")
    print("2. Eliminar eliminar perosna de retiro de libros\n")
    print("3. Actualizar datos de retiro\n")
    print("4. Ver datos de un retiro\n")
    print("5. Ver todos los datos de retiro\n")
    print("6. Salir\n")
    opcion = input("\n Seleccione una opcion: ")
    return opcion


while True:
        dar_bienvenida()
        opcion = menu_pincipal()
        if (opcion.isdigit() and 1 <= int(opcion) <= 6):
            match opcion:
                case "1":
                    agregarRetiro(colRetiros, librosDisponibles)
                case "2":
                    legajo = input("\nIngrese el numero de legajo: ")
                    eliminarRetiro(colRetiros,legajo)
                case "3":
                    legajo = input("\nIngrese el numero de legajo: " )
                    actualizarRetiro(colRetiros, legajo)
                case "4":
                    legajo = input("\nIngrese el numero de legajo: ")
                    mostrarUnRetiro(colRetiros, legajo)
                case "5":
                    mostrarTodosLosRetiros(colRetiros)
                case "6":
                    print("\n Saliendo del programa...")
                    break
        else:
            print( "\n\n Por favor ingrese un valor dentro de las opciones...")












