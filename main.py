from funciones.agregar_pais import agregar_pais
from funciones.actualizar_pais import actualizar_pais
from funciones.busqueda_pais import buscar_pais
from funciones.filtrar_pais import filtrar_pais
from funciones.ordenar_pais import ordenar_pais
from funciones.ver_estadisticas import ver_estadisticas

while True:
    print("===== Menú Principal =====\n")
    print("1) Agregar país")
    print("2) Actualizar datos de población y superficie")
    print("3) Buscar país por nombre")
    print("4) Filtrar país")
    print("5) Ordenar país")
    print("6) Mostrar estadísticas")
    print("7) Salir")
    print("=========================\n")

    try:
        opcion = int(input("Ingrese la opción deseada: "))

        if opcion < 1 or opcion > 7:
            print("Error: opción ingresada fuera de rango.\n")

        elif opcion == 1:
            agregar_pais()

        elif opcion == 2:
            actualizar_pais()

        elif opcion == 3:
            buscar_pais()

        elif opcion == 4:
            filtrar_pais()

        elif opcion == 5:
            ordenar_pais()

        elif opcion == 6:
            ver_estadisticas()

        else:
            print("¡Gracias por utilizar el sistema! Terminando...")
            break

    except ValueError as e:
        print(f"Error: Por favor ingrese una opción válida.\n")

    except Exception as e:
        print(f"Error: {e}\n")
