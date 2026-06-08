from archivos.csv_manager import cargar_paises

def validar_nombre_pais():
    while True:
        nombre = input("Ingrese el nombre del país: ").strip()

        # Acá los lens de 4 y 56 hacen referencia a los países con nombres más cortos y largos posibles: (corto: perú, largo: El Reino Unido de Gran Bretaña e Irlanda del Norte)
        if len(nombre) < 4 or len(nombre) > 56:
            print("Error: nombre de país inválido (debe posees entre 4 y 56 carácteres).")

        elif any(caracter.isdigit() for caracter in nombre):
            print("Error: el nombre no puede contener números.")

        else:
            return nombre


def validar_poblacion():
    while True:
        try:
            poblacion = int(input("Ingrese la población: "))

            if poblacion <= 0:
                print("Error: la población debe ser mayor a cero.")

            else:
                return poblacion

        except ValueError:
            print("Error: ingrese un número entero.")


def validar_superficie():
    while True:
        try:
            superficie = int(input("Ingrese la superficie (km²): "))

            if superficie <= 0:
                print("Error: la superficie debe ser mayor a cero.")

            else:
                return superficie

        except ValueError:
            print("Error: ingrese un número entero.")


def validar_continente():
    continentes = [
        "América",
        "Europa",
        "Asia",
        "África",
        "Oceanía"
    ]

    while True:
        continente = input("Ingrese el continente: ").title()

        if continente in continentes:
            return continente

        print("Error: continente inválido (los continentes válidos son: América, Europa, Asia, África, Oceanía).")


def validar_nombre_existente():

    paises = cargar_paises()

    while True:
        nombre = input("Ingrese el nombre del país: ").strip()

        for pais in paises:
            if pais["nombre"].lower() == nombre.lower():
                return nombre

        print("Error: el país no existe.")

    
def validar_opcion_filtro():
    seleccion_usuario = input("\nIngresá una opción: ").strip()

    while not seleccion_usuario.isdigit() or seleccion_usuario == "" or int(seleccion_usuario) < 1 or int(seleccion_usuario) > 4:
        if seleccion_usuario == "":
            print('Error: No podés ingresar un dato vacío.')
            seleccion_usuario = input("\nIngresá una opción: ").strip()
        elif not seleccion_usuario.isdigit():
            print('Error: Por favor ingresá solo números positivos.')
            seleccion_usuario = input("\nIngresá una opción: ").strip()
        else:
            print('Error: Por favor ingresá una opción dentro del rango indicado.')
            seleccion_usuario = input("\nIngresá una opción: ").strip()
    
    seleccion_usuario = int(seleccion_usuario)
    
    return seleccion_usuario

def validar_rango_poblacion():

    while True:
        try: 
            rango_poblacion = int(input('Ingrese el rango solicitado: '))

            if rango_poblacion and rango_poblacion > 0:
                return rango_poblacion

            else:
                print("Error: la población no puede ser menor a 1.")
            
        except ValueError:
            print('Ingrese solo números enteros')

def validar_rango_superficie():

    while True:
        try:
            superficie_ingresada = int(input('Ingrese la superficie solicitada: '))

            if superficie_ingresada >= 1 and superficie_ingresada <= 17100000: #MAX sería la superficie de Rusia
                return superficie_ingresada

            else:
                print("Error: la superficie no puede ser menor a 1.")

        except ValueError:
            print("Error: Ingrese un rango de superficie mayor/igual a 1 km² y menor/igual a 17.100.000 km²")


#Funciones validar estadisticas
        
        
def validar_menu_estadisticas():
    while True:

        try:
            seleccion_usuario = int(input('Ingrese la opción: '))
            if seleccion_usuario >= 1 and seleccion_usuario <= 5:
                return seleccion_usuario
            else:
                print('Error: Seleccione un número entero entre 1 y 5\n')
            
        except ValueError:
            print('Error: Seleccione un número entero entre 1 y 5\n')