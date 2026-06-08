# TPI Programación - Gestión de Países

## Integrantes

* Francisco Romero
* Patrick Da Graça

## Descripción

Este proyecto consiste en una aplicación de consola desarrollada en Python para la gestión de información de países almacenada en un archivo CSV.

El sistema permite agregar nuevos países, actualizar información existente, realizar búsquedas, aplicar filtros, ordenar registros y obtener estadísticas sobre los datos almacenados.

La información se persiste en un archivo CSV ubicado dentro de la carpeta `datos`.

---

# Estructura del Proyecto

```text
TPI_PROGRAMACION/
│
├── archivos/
│   └── csv_manager.py
│
├── datos/
│   └── datos.csv
│
├── funciones/
│   ├── agregar_pais.py
│   ├── actualizar_pais.py
│   ├── busqueda_pais.py
│   ├── filtrar_pais.py
│   ├── ordenar_pais.py
│   └── ver_estadisticas.py
│
├── validaciones/
│   └── validaciones.py
│
└── main.py
```

---

# Requisitos

* Python 3.10 o superior.

No se utilizan librerías externas.

---

# Ejecución

Desde la carpeta raíz del proyecto ejecutar:

```bash
python main.py
```

---

# Funcionalidades

## 1. Agregar país

Permite registrar un nuevo país indicando:

* Nombre
* Población
* Superficie
* Continente

Validaciones:

* El nombre no puede contener números.
* La población debe ser un entero positivo.
* La superficie debe ser un entero positivo.
* El continente debe pertenecer a una lista predefinida.
* No se permiten países duplicados.

---

## 2. Actualizar país

Permite modificar:

* Población
* Superficie

de un país previamente registrado.

Antes de realizar la modificación se verifica que el país exista en el dataset.

---

## 3. Buscar país

Permite buscar países mediante coincidencia parcial o exacta sobre el nombre.

La búsqueda no distingue entre mayúsculas y minúsculas.

---

## 4. Filtrar países

Permite filtrar registros por:

### Continente

Muestra todos los países pertenecientes al continente seleccionado.

### Población

Permite definir un rango mínimo y máximo de población.

### Superficie

Permite definir un rango mínimo y máximo de superficie.

---

## 5. Ordenar países

Permite ordenar los registros por:

* Nombre
* Población
* Superficie

La superficie puede visualizarse tanto en orden ascendente como descendente.

---

## 6. Estadísticas

El sistema permite visualizar:

* País con mayor población.
* País con menor población.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.

---

# Persistencia de Datos

Los datos son almacenados en:

```text
datos/datos.csv
```

Al iniciar el programa los registros son cargados desde el archivo CSV y convertidos a una lista de diccionarios.

Cuando se agrega o actualiza información, el dataset es reescrito automáticamente para mantener la persistencia de los cambios.

---

# Validaciones Implementadas

* Control de opciones de menú.
* Control de rangos numéricos.
* Verificación de existencia de países.
* Validación de continentes.
* Validación de población.
* Validación de superficie.
* Validación de formato durante la carga del CSV.

Las líneas con formato inválido son ignoradas y notificadas al usuario mediante un mensaje de advertencia.

---

# Diseño Utilizado

El proyecto fue desarrollado utilizando una arquitectura modular.

Se implementó una separación de responsabilidades mediante módulos independientes:

* Gestión de archivos CSV.
* Validaciones.
* Funcionalidades principales.
* Menú principal.

La información se manipula internamente mediante listas de diccionarios, facilitando las operaciones de búsqueda, filtrado, ordenamiento y generación de estadísticas.