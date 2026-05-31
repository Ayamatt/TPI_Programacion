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