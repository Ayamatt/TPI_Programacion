#trabajar con listas de diccionarios
from validaciones.validaciones import validar_menu_estadisticas
from archivos.csv_manager import cargar_paises

# Permite ver estadísticas de los países del dataset (País con mayor y menor porblación, promedio total de población y superficie y cantidad de países por continente)

def ver_estadisticas():

    paises = cargar_paises()

    print('Seleccione la estadística a visualizar:\n')
    print('1) País con mayor población\n2) País con menor población\n3) Promedio de población\n4) Promedio de superficie\n5) Cantidad de países por continente\n')

    seleccion_usuario = validar_menu_estadisticas()

    #Opción 1
    if seleccion_usuario == 1:

        pais_encontrado = ''.title()
        mayor_poblacion = 0

        for pais in paises:

            if mayor_poblacion < pais['poblacion']:
                    mayor_poblacion = pais['poblacion']
                    pais_encontrado = pais['nombre'] + str(f': {mayor_poblacion} habitantes')

        print(f"{pais_encontrado}\n")
        return
        
    #Opción 2
    elif seleccion_usuario == 2: 

        pais_encontrado = ''.title()
        menor_poblacion = float('inf')

        for pais in paises:

            if pais['poblacion'] < menor_poblacion:
                menor_poblacion = pais['poblacion']
                pais_encontrado = pais['nombre'] + str(f': {menor_poblacion} habitantes')

        print(f"{pais_encontrado}\n")
        return

    #Opción 3
    elif seleccion_usuario == 3: 

        sumatoria_poblacion = 0
        cantidad_paises = 0

        for pais in paises:
            sumatoria_poblacion += pais['poblacion']
            cantidad_paises += 1
        print(f'El promedio de la población de los países listados es de {sumatoria_poblacion / cantidad_paises:.0f} personas.\n')
        return 
            
    #Opcion 4
    elif seleccion_usuario == 4:

        sumatoria_superficie = 0
        cantidad_paises = 0

        for pais in paises:
            sumatoria_superficie += pais['superficie']
            cantidad_paises += 1
        print(f'El promedio de superficie de los países listados es de {sumatoria_superficie / cantidad_paises:.0f} km2.\n')
        return 
        
    #Opcion 5
    else:
        america = 0
        asia = 0
        africa = 0
        oceania = 0
        europa = 0

        for pais in paises:

            if pais['continente'] == 'América':
                america += 1
            elif pais['continente'] == 'Asia':
                asia += 1
            elif pais['continente'] == 'Oceanía':
                oceania += 1
            elif pais['continente'] == 'África':
                africa += 1
            elif pais['continente'] == 'Europa':
                europa += 1

        print(f'\nPaíses por continente\n\nAmérica: {america} países\nAsia: {asia} países\nOceanía: {oceania} países\nÁfrica: {africa} países\nEuropa: {europa} países\n')
        return