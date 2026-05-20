# simulador-propagacion-emocional
Trabajo aplicado de programación: simulador de propagación emocional en Python.

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
