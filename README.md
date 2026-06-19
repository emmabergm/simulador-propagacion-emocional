# Simulador de Propagación Emocional

Trabajo aplicado de programación: simulador de propagación emocional en Python.

## Integrantes

Olivia Kemmerer, Camila Iglesias, Emma Bergmann, Athina Lambert y Uma Rodriguez Videla.

## Objetivo

El objetivo del trabajo es evaluar cómo un comentario de un estudiante puede impactar en las emociones de otro estudiante dentro de un grupo, teniendo en cuenta el contexto académico en el que ocurre la interacción: parciales o no parciales.

## Partes del programa que realizó cada participante

- Olivia, Camila y Athina: código y archivos.
- Emma y Uma: diagramas de flujo, docstrings y README.
## Instrucciones para ejecutar el programa

1. Clonar o descargar el repositorio.
2. Verificar que los archivos Excel estén dentro de la carpeta `archivos/`.
3. Instalar las librerías necesarias:

```bash
pip install -r requirements.txt
```

4. Ejecutar el archivo principal:

```bash
python main.py
```

El proyecto necesita la participación de dos usuarios. Si lo ejecuta una sola persona, debe asumir ambos roles.

## Librerías utilizadas

- pandas
- matplotlib
- openpyxl
- random

## Estructura del repositorio

```text
simulador-propagacion-emocional/
│
├── archivos/
│   ├── archivo_comentario.xlsx
│   ├── archivo_e_n.xlsx
│   └── archivo_e_post.xlsx
│
├── src/
│   ├── comentarios.py
│   ├── alumnos.py
│   ├── Menus.py
│   ├── Partes.py
│   ├── graficos.py
│   └── analisis.py
│
├── diagramas/
├── main.py
├── requirements.txt
└── README.md
```
## Explicación breve de las funciones principales:

- `situacion()`: pregunta si el estudiante se encuentra en contexto de parciales o no parciales.
- `numero_random()`: selecciona aleatoriamente una situación del archivo de comentarios.
- `realizar_pregunta()`: muestra una situación académica y tres comentarios posibles.
- `guardar_respuesta()`: guarda la respuesta elegida por el estudiante en el DataFrame.
- `asociacion()`: asocia la respuesta elegida con un DataFrame emocional.
- `info_estudiante2()`: registra las emociones iniciales del segundo estudiante.
- `valoracion_comentario()`: registra las emociones posteriores al comentario.
- `calcular_promedios_grupales()`: calcula promedios de estrés, motivación y tranquilidad.
- `comparar_promedios()`: compara las emociones neutras con las posteriores.
- `feedback_comentario()`: genera una devolución sobre el impacto emocional del comentario.
- `grafico()`: genera gráficos comparativos de las emociones.

## Resultados, salidas, metricas, graficos o funcionalidades generadas: 

- Registro de emociones iniciales del Estudiante 2.
- Registro de emociones posteriores a cada comentario.
- Promedios grupales de estrés, motivación y tranquilidad.
- Comparación entre emociones neutras y emociones posteriores.
- Feedback sobre el impacto emocional de los comentarios.
- Gráficos que comparan los cambios emocionales.

## Diagramas de diseño:
El proyecto incluye diagramas de flujo de las funciones principales. Estos diagramas representan la lógica general del programa, las decisiones, los procesos y los posibles errores.

Los diagramas se encuentran en la carpeta `diagramas/`.

## Uso de Pandas

El proyecto utiliza Pandas para leer y modificar archivos Excel con información sobre comentarios, emociones neutras y emociones posteriores.

Los archivos utilizados se encuentran en la carpeta `archivos/`:

- `archivo_comentario.xlsx`
- `archivo_e_n.xlsx`
- `archivo_e_post.xlsx`

Con Pandas se cargan estos archivos como DataFrames, se guardan respuestas, se calculan promedios y se comparan cambios emocionales.

## Declaración de uso de IA:

Durante el desarrollo del proyecto se utilizó inteligencia artificial como herramienta de apoyo para:
- Revisar errores de código
- Ayudarnos con funcionalidades de cada librería.
- Ayudarnos a generar linea de codigo del histograma

El código final fue revisado, adaptado y probado por las integrantes del grupo.

## Notas o explicaciones adicionales para correr correctamente el programa: 
- El programa debe ejecutarse desde la carpeta principal del repositorio.
- Los archivos Excel deben estar dentro de la carpeta archivos/.
- El proyecto necesita dos usuarios: Estudiante 1 y Estudiante 2.
  - Si una sola persona ejecuta el programa, debe responder simulando ambos roles.
- Las respuestas deben ingresarse respetando las opciones indicadas por consola.
- Las valoraciones emocionales deben ingresarse dentro del rango solicitado por el programa.
