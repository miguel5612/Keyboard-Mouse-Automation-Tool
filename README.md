# Mockup Tool

Herramienta que permite simular una API y emular acciones del teclado y el ratón. Ideal para pruebas automatizadas y simulaciones de interacciones del usuario.

## Tabla de Contenidos

1. [Instalación](#instalación)
2. [Uso](#uso)
   - [API Mockup](#api-mockup)
   - [Emulación de Teclado y Ratón](#emulación-de-teclado-y-ratón)
3. [Ejemplos](#ejemplos)
4. [Limitaciones](#limitaciones)
5. [Licencia](#licencia)

## Instalación

1. Asegúrese de tener instalado Python.
2. Clone o descargue este repositorio.
3. Instale las dependencias necesarias:

```bash
pip install Flask pyautogui
```

## Uso

### API Mockup

- Configure los parámetros de la API simulada, incluido el método de solicitud, el nombre del parámetro, el valor esperado, el tipo de respuesta y el contenido de la respuesta.
- Haga clic en "Iniciar API" para iniciar la API en el puerto 5000.

### Emulación de Teclado y Ratón

- Ingrese o cargue desde un archivo los comandos que desea ejecutar. Estos comandos pueden incluir acciones como abrir aplicaciones, escribir texto y presionar teclas específicas.
- Haga clic en "Execute Commands" para iniciar la emulación.

## Ejemplos

### API Mockup

Suponga que desea simular una API que responde con un JSON cuando se hace una solicitud GET con un parámetro `id` de valor `1234`. Para ello:

1. Seleccione "GET" en el "Método de Solicitud".
2. Ingrese "id" en "Nombre del Parámetro".
3. Ingrese "1234" en "Valor".
4. Seleccione "JSON" en "Tipo de Respuesta".
5. En "Contenido de Respuesta", ingrese `{ "nombre": "Juan", "edad": 30 }`.
6. Haga clic en "Iniciar API".

Cuando haga una solicitud GET a `http://localhost:5000/api?id=1234`, la respuesta será el JSON `{ "nombre": "Juan", "edad": 30 }`.

### Emulación de Teclado y Ratón

Suponga que desea abrir el Bloc de notas y escribir "Hola Mundo". Para ello:

1. En el área de texto, ingrese:
open notepad
wait 1
type Hola Mundo

2. Haga clic en "Execute Commands".

El programa abrirá el Bloc de notas y escribirá "Hola Mundo" en él.


## Limitaciones

Actualmente, la API simulada solo se ejecuta en el puerto 5000.
La emulación puede no funcionar correctamente si se interrumpe manualmente durante su ejecución.

## Licencia
Este software es de código abierto y se distribuye bajo la licencia MIT.

