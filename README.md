# Keyboard & Mouse Automation Tool

Herramienta que permite simular una API y emular acciones avanzadas del teclado y el ratón. Ideal para automatizar comportamientos en tu PC y simulaciones de interacciones del usuario.

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

### Emulación de Teclado y Ratón

- Ingrese o cargue desde un archivo los comandos que desea ejecutar. Estos comandos pueden incluir acciones como abrir aplicaciones, escribir texto y presionar teclas específicas.
- Haga clic en "Execute Commands" para iniciar la emulación.

### Características Adicionales

- Repetición de Comandos: Puede incluir un número al comienzo de un comando para que este se repita x veces en la ejecución. Ejemplo: 2 type data resultará en datadata.
- Rutas con Espacios: Para comandos como open, puede incluir rutas con espacios encerrándolas en comillas dobles.
- Click Avanzado: El comando click ahora permite enviar parámetros como left, right o el nombre del botón (aunque puede no funcionar perfectamente con el nombre del botón).

### API Mockup

- Configure los parámetros de la API simulada, incluido el método de solicitud, el nombre del parámetro, el valor esperado, el tipo de respuesta y el contenido de la respuesta.
- Haga clic en "Iniciar API" para iniciar la API en el puerto 5000.

## Ejemplos

### Emulación de Teclado y Ratón

Suponga que desea abrir el Bloc de notas y escribir "Hola Mundo". Para ello:

1. En el área de texto, ingrese:

```
open notepad
wait 1
type Hola Mundo
```

2. Haga clic en "Execute Commands".

El programa abrirá el Bloc de notas y escribirá "Hola Mundo" en él.

### Evitar el Apagado de Pantalla

Para evitar que el computador entre en modo de suspensión o apague la pantalla mientras estás ocupado en otras tareas, puedes hacer que el programa emule el movimiento del ratón en intervalos aleatorios entre 0 y 30 segundos. De esta manera, el sistema operativo creerá que estás interactuando activamente con el computador.

1. En el área de texto, ingrese:

```
loop:
wait random(0,30)
move mouse random(-10,10) random(-10,10)
goto loop
css
```

2. Haga clic en "Execute Commands".

El programa emulará el movimiento del ratón en posiciones aleatorias dentro de un rango de -10 a 10 píxeles en ambos ejes (x, y) cada 0 a 30 segundos. Esto evitará que el sistema operativo active cualquier salvapantallas o entre en modo de suspensión.


### API Mockup

Suponga que desea simular una API que responde con un JSON cuando se hace una solicitud GET con un parámetro `id` de valor `1234`. Para ello:

1. Seleccione "GET" en el "Método de Solicitud".
2. Ingrese "id" en "Nombre del Parámetro".
3. Ingrese "1234" en "Valor".
4. Seleccione "JSON" en "Tipo de Respuesta".
5. En "Contenido de Respuesta", ingrese `{ "nombre": "Juan", "edad": 30 }`.
6. Haga clic en "Iniciar API".

Cuando haga una solicitud GET a `http://localhost:5000/api?id=1234`, la respuesta será el JSON `{ "nombre": "Juan", "edad": 30 }`.

## Limitaciones

Actualmente, la API simulada solo se ejecuta en el puerto 5000.
La emulación puede no funcionar correctamente si se interrumpe manualmente durante su ejecución.

## Licencia
Este software es de código abierto y se distribuye bajo la licencia MIT.

