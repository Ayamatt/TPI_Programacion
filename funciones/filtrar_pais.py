from validaciones.validaciones import (
    validar_opcion_filtro,
    validar_continente,
    validar_rango_poblacion,
    validar_rango_superficie
)

from archivos.csv_manager import cargar_paises

def filtrar_pais():

    paises = cargar_paises()

    print('Filtrar país por:\n')
    print('1) Continente\n2) Población\n3) Superficie\n4) Volver')

    seleccion_usuario = validar_opcion_filtro()

    #Opción 1
    if seleccion_usuario == 1:

        coincidencias_continente  = '\n'

        seleccion_continente = validar_continente()
        print()
        for pais in paises:
            if seleccion_continente == pais['continente'].title():
                for clave, valor in pais.items():
                    coincidencias_continente += f'{clave.title()}: {str(valor).title()}\n'
                    
        print("=== Información de los países ===")
        print(coincidencias_continente)
        return
    
    #Opción 2
    elif seleccion_usuario == 2:

        paises_dentro_del_rango = '\n'

        print('Rango mínimo de población')
        rango_minimo = validar_rango_poblacion()
        print('Rango máximo de población')
        rango_maximo = validar_rango_poblacion()

        for pais in paises:
            if rango_minimo <= pais['poblacion'] <= rango_maximo:
                for clave , valor in pais.items():
                    paises_dentro_del_rango += f'{clave.title()}: {str(valor).title()}\n'

        print("=== Información de los países ===")
        print(paises_dentro_del_rango)
        return
    
    #Opción 3
    elif seleccion_usuario == 3:
        
        paises_dentro_del_rango = '\n'

        print('Ingresá el rango mínimo de superficie')
        rango_minimo = validar_rango_superficie()
        print('Ingresá el rango máximo de superficie')
        rango_maximo = validar_rango_superficie()

        for pais in paises:
            if rango_minimo <= pais['superficie'] <= rango_maximo:
                for clave , valor in pais.items():
                    paises_dentro_del_rango += f'{clave.title()}: {str(valor).title()}\n'

        print("=== Información de los países ===")
        print(paises_dentro_del_rango)
        return
    
    else:
        return 'Volviendo al menú...'
    