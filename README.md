# simulador-propagacion-emocional
Trabajo aplicado de programación: simulador de propagación emocional en Python.

Integrantes: Olivia Kemmerer, Camila Iglesias, Emma Bergmann, Athina Lambert, Uma Rodriguez Videla

Objetivo:  El objetivo del trabajo es evaluar como los comentarios se modifican dependiendo de la situacion en la que estamos (parciales o no, en este caso) y como eso termina repercutiendo en las emociones del resto de las personas en un grupo.

Partes del programa que realizo cada participante: 
Olivia, Camila y Athina: se encargaron del codigo y de los archivos 
Emma y Uma: se encargaron de los diagramas de flujo y el docstring

Instrucciones para ejecutar el programa: 
- Corroborar tener descargados los archivos encontrados en la carpeta de archivos
- El proyecto necesita de dos usuarios, en caso de ser una sola la que lo corra, asumir el papel de dos.

 Librerias utilizadas: 
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
5. requierments
6. README

Explicacion breve de las funciones principales: 

Resultados, salidas, metricas, graficos o funcionalidades generadas: 

Diagramas de diseño: 

Declaracion de uso de IA: 

Notas o explicaciones adicionales para correr correctamente el programa: 

## Implementación futura de Pandas para lectura del dataset

En una próxima etapa del proyecto, implementaríamos la librería Pandas para leer un dataset en formato CSV con la información inicial de los personajes de la simulación.

Actualmente, el sistema trabaja con personajes generados dentro del programa o definidos manualmente. Con Pandas, podríamos cargar esos personajes desde un archivo externo, por ejemplo:

`data/dataset_emociones.csv`

Este dataset podría incluir columnas como:

- nombre
- estres
- calma
- motivacion
- resiliencia

Un ejemplo de estructura del dataset sería:

| nombre | estres | calma | motivacion | resiliencia |
|---|---:|---:|---:|---:|
| Persona 1 | 70 | 30 | 50 | 0.4 |
| Persona 2 | 45 | 55 | 65 | 0.7 |
| Persona 3 | 80 | 20 | 40 | 0.3 |

Para leer el archivo usaríamos la función `read_csv()` de Pandas:

```python
import pandas as pd

df = pd.read_csv("data/dataset_emociones.csv")
