# Organización del Trabajo - TPI Programación

## Estado actual del proyecto

Actualmente se encuentra implementada la estructura base del proyecto:

* Menú principal en consola.
* Organización modular por carpetas.
* Lectura y escritura del archivo CSV.
* Funcionalidad para agregar países.
* Funcionalidad para actualizar población y superficie.
* Validaciones básicas de entradas.
* Módulo centralizado para manejo de archivos CSV.

### Estructura actual

```text
TPI_PROGRAMACION/
│
├── datos/
│   └── datos.csv
│
├── archivos/
│   └── csv_manager.py
│
├── funciones/
│   ├── agregar_pais.py
│   ├── actualizar_pais.py
    ├── busqueda_pais.py
    ├── filtrar_pais.py 
    ├── ver_estadisticas.py 
│
├── validaciones/
│   └── validaciones.py
│
└── main.py
```

---

## Tareas sugeridas

### Opción 3 - Buscar país por nombre

Crear el archivo:

```text
funciones/busqueda_pais.py
```

Implementar:

```python
def buscar_pais():
```

Requerimientos:

* Utilizar `cargar_paises()`.
* Permitir coincidencia exacta o parcial.
* Ignorar mayúsculas/minúsculas.
* Mostrar los datos completos del país encontrado.
* Informar cuando no existan coincidencias.

Ejemplo:

```text
Ingrese nombre: arg

Resultado:
Argentina
Población: 45376763
Superficie: 2780400
Continente: América
```

---

### Opción 4 - Filtrar países

Crear:

```text
funciones/filtrar_pais.py
```

Implementar:

```python
def filtrar_pais() listo
```

Con submenú:

```text
1) Filtrar por continente
2) Filtrar por población
3) Filtrar por superficie
4) Volver
```

#### Filtrar por continente

Ejemplo:

```text
Ingrese continente: América
```

Mostrar todos los países pertenecientes a ese continente.

#### Filtrar por población

Solicitar:

```text
Población mínima
Población máxima
```

Mostrar los países dentro del rango.

#### Filtrar por superficie

Solicitar:

```text
Superficie mínima
Superficie máxima
```

Mostrar los países dentro del rango.

---

### Validaciones necesarias

Agregar en:

```text
validaciones/validaciones.py listo
```

Funciones para validar:

```python
validar_opcion_filtro() listo
validar_rango_poblacion() listo
validar_rango_superficie() listo
```

---

## Recomendaciones

* Todas las funciones deben trabajar utilizando:

```python
paises = cargar_paises()
```

* No acceder directamente al CSV desde las funciones de búsqueda o filtros.
* Utilizar listas de diccionarios para recorrer los datos.
* Mantener una función por responsabilidad.
* Seguir la misma estructura utilizada en agregar y actualizar país.

---

## Pendiente para etapas posteriores

### Opción 5

Ordenamientos:

* Nombre
* Población
* Superficie
* Ascendente y descendente

### Opción 6

Estadísticas:

* País con mayor población.
* País con menor población.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.

```
```
