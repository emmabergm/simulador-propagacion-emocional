# simulador-propagacion-emocional
Trabajo aplicado de programación: simulador de propagación emocional en Python.

Integrantes: Olivia Kemmerer, Camila Iglesias, Emma Bergmann, Athina Lambert, Uma Rodriguez Videla

Objetivo:  El objetivo del trabajo es evaluar cómo los comentarios se modifican dependiendo de la situación en la que estamos (parciales o no, en este caso) y cómo eso termina repercutiendo en las emociones del resto de las personas en un grupo.

Partes del programa que realiza cada participante: 
Olivia, Camila y Athina: se encargaron del código y de los archivos 
Emma y Uma: se encargaron de los diagramas de flujo y el docstring

Instrucciones para ejecutar el programa: 
- Corroborar tener descargados los archivos encontrados en la carpeta de archivos
- El proyecto necesita de dos usuarios, en caso de ser una sola la que lo corra, asumir el papel de dos.

 Librerías utilizadas: 
 - pandas
 - random
 - matplotlib

Estructura del repositorio: 
1. carpeta con archivos:
  - archivo con emociones neutras
  - archivo con emociones asociadas al comentario (ambos contienen datos simulados)
  - archivo de comentarios y contextos posibles
2. src:
  - comentarios
  - alumnos
  - Menus
  - Partes
  - grafico
  - analisis
3. diagramas
4. main
5. requirements.txt
6. README

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

Resultados, salidas, metricas, graficos o funcionalidades generadas: 

- Registro de emociones iniciales del Estudiante 2.
- Registro de emociones posteriores a cada comentario.
- Promedios grupales de estrés, motivación y tranquilidad.
- Comparación entre emociones neutras y emociones posteriores.
- Feedback sobre el impacto emocional de los comentarios.
- Gráficos que comparan los cambios emocionales.

Diagramas de diseño: El proyecto incluye diagramas de flujo de las funciones principales. Estos diagramas representan la lógica general del programa, las decisiones, los procesos y los posibles errores.

Los diagramas se encuentran en la carpeta `diagramas/`.

Declaración de uso de IA: Durante el desarrollo del proyecto se utilizó inteligencia artificial como herramienta de apoyo para:

- organizar la estructura del proyecto;
- revisar errores de código;
- mejorar docstrings;
- ordenar el README;
- explicar funciones y corregir problemas de lógica.

El código final fue revisado, adaptado y probado por las integrantes del grupo.

Notas o explicaciones adicionales para correr correctamente el programa: 

## Uso de Pandas

El proyecto utiliza Pandas para leer y modificar archivos Excel con información sobre comentarios, emociones neutras y emociones posteriores.

Los archivos utilizados se encuentran en la carpeta `archivos/`:

- `archivo_comentario.xlsx`
- `archivo_e_n.xlsx`
- `archivo_e_post.xlsx`

Con Pandas se cargan estos archivos como DataFrames, se guardan respuestas, se calculan promedios y se comparan cambios emocionales.
