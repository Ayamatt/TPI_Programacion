def buscar_pais(pais_buscado , paises): #devuelve una lista con el diccionario del país encontrado

    pais_encontrado = []
    
    #Paises lista de dict
    for pais in paises:
        if pais_buscado.lower() == pais['nombre']: #coincidencia exacta
            pais_encontrado.append(pais) 
            return pais_encontrado
        elif pais_buscado.lower() in pais['nombre']: #coincidencia parcial
            pais_encontrado.append(pais)
            return pais_encontrado
        else:
            return 'No se encontró el país ingresado'

def datos_limpios(pais_encontrado): #recibe la lista de diccionarios de la búsqueda por país y nos devuelve los datos limpios
    
    datos = ''

    for pais in pais_encontrado:
        for clave , valor in pais.items():
            datos += (f"{clave.capitalize()}: {str(valor).capitalize()}\n")
    return datos



            


