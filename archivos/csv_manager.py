def cargar_paises():

    paises = []

    with open("datos/datos.csv","r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        for numero_linea, linea in enumerate(lineas[1:], start=2):
            try:
                datos = linea.strip().split(",")

                if len(datos) != 4:
                    raise ValueError

                pais = {
                    "nombre": datos[0],
                    "poblacion": int(datos[1]),
                    "superficie": int(datos[2]),
                    "continente": datos[3]
                }

                paises.append(pais)

            except ValueError:
                print(f"Advertencia: línea {numero_linea} ignorada por formato inválido.")

    return paises


def guardar_paises(paises):

    with open("datos/datos.csv", "w", encoding="utf-8") as archivo:
        archivo.write("nombre, poblacion, superficie, continente\n")

        for pais in paises:
            archivo.write(
                f"{pais['nombre']},"
                f"{pais['poblacion']},"
                f"{pais['superficie']},"
                f"{pais['continente']}\n"
            )