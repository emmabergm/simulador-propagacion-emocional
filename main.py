import pandas as pd

from src.comentarios import situacion
from src.comentarios import realizar_pregunta
from src.comentarios import guardar_respuesta
from src.comentarios import numero_random 
from src.comentarios import asociacion
from src.alumnos import info_estudiante2 
from src.alumnos import presentar_comentario
from src.alumnos import valoracion_comentario
from src.analisis import  unir_datos_emocionales
from src.analisis import calcualar_promedios_grupales
from src.analisis import comparar_promedios
from src.analisis import feedback_comentario
from src.Menu_parte_1 import menu_parte_1
from src.devolucion import menu_2
from src.devolucion import feedback_emociones

#from src.validacion_datos import 
#from src.graficos import 
#from src.devolucion import 

# Abrir archivos: 
archivo_neutro= "C:/Users/camil/OneDrive/Desktop/Simulador emocional/simulador-propagacion-emocional/archivos/archivo_e_n.xlsx"

archivo_e_comentario1= "C:/Users/camil/OneDrive/Desktop/Simulador emocional/simulador-propagacion-emocional/archivos/archivo_e_post.xlsx"

archivo_comentario = "C:/Users/olivi/OneDrive/Documentos/GitHub/simulador-propagacion-emocional/archivos/archivo_comentario.xlsx"

try: 
     
    df_neutro= pd.read_excel(archivo_neutro)
 
    df_comentario = pd.read_excel(archivo_comentario)
 
    df_motivacion= pd.read_excel(archivo_e_comentario1, sheet_name="Comentario_motivacional")
    df_tranquilidad=pd.read_excel(archivo_e_comentario1, sheet_name="Comentario_tranquilidad")
    df_estres=pd.read_excel(archivo_e_comentario1, sheet_name= "Comentario_estres")
 
except FileNotFoundError: 
    print("El archivo no se encontro")


#Parte 1: 

estudiante_1 = input("Ingrese su nombre: ")

situacion_estudiante = situacion()
planteo_situacion_1 = realizar_pregunta(df_comentario)

situacion_estudiante = situacion()
planteo_situacion_2 = realizar_pregunta(df_comentario)

respuesta_1 = realizar_pregunta(df_comentario) 

# Parte 1 (interaccion con estudiante 1)

estudiante_1 = input("Ingrese su nombre: ")

situacion_1 = situacion()
indice = numero_random()
respuesta_1 = realizar_pregunta(indice, df_comentario)
df_respuesta = guardar_respuesta(respuesta_1, indice, df_comentario, situacion_1 )
df_asociado_1 = asociacion(respuesta_1, df_tranquilidad, df_motivacion, df_estres)

# Parte 1.2 

situacion_2 = situacion()
respuesta_2 = realizar_pregunta(indice, df_comentario)
df_respuesta = guardar_respuesta(respuesta_2, indice, df_comentario, situacion_2 )
df_asociado_2 = asociacion(respuesta_1, df_tranquilidad, df_motivacion, df_estres)

# Menu 1 

menu_1 = menu_parte_1()

# Parte 2 (interaccion con estudiante 2)



if menu_1 == "True": 
  estudiante_2 = input("Ingrese su nombre: ")

else: 
  print("Muchas gracias por su respuesta!") #NO ESTA BIEN 
edad_e_2 = int(input("Ingrese su edad: "))
menu_1 = "funcion de menu"
edad_e_2 = int(input("Ingrese su edad: "))

informacion_estudiante2 = info_estudiante2 (df_neutro, estudiante_2, edad_e_2 )
print(presentar_comentario = presentar_comentario(df_comentario, respuesta_1, indice, situacion_1)) 
valoracion_1 = valoracion_comentario(estudiante_2, edad_e_2, respuesta_1, df_comentario,  df_asociado_1)

#Parte 2.1 
presentar_comentario(df_comentario, respuesta_2, indice, situacion_2)
valoracion_2 = valoracion_comentario(estudiante_2, edad_e_2, respuesta_2, df_comentario,  df_asociado_2)

# Parte 3 (analisis)

union_df = unir_datos_emocionales(df_neutro, df_asociado_1, df_asociado_2)

promedio_neutro = calcualar_promedios_grupales(df_neutro)
promedio_asociado_1 = calcualar_promedios_grupales(df_asociado_1)
promedio_asociado_2 = calcualar_promedios_grupales(df_asociado_2)


cambio_estres_1, cambio_tranquilidad_1, cambio_motivacion_1 = comparar_promedios(promedio_neutro, promedio_asociado_1)
cambio_estres_2, cambio_tranquilidad_2, cambio_motivacion_2 = comparar_promedios(promedio_neutro, promedio_asociado_2)

feedback_1 = feedback_comentario( situacion_1, presentar_comentario, cambio_estres_1, cambio_tranquilidad_1, cambio_motivacion_1 )
feedback_2 =  feedback_comentario( situacion_2, presentar_comentario, cambio_estres_2, cambio_tranquilidad_2, cambio_motivacion_2 )

# Parte 4 (devolucion) 

# Menu 2 

menu_parte_2 = menu_2()

devolucion = feedback_emociones(menu_parte_2, df_neutro, df_asociado_1)
devolucion = feedback_emociones(menu_parte_2, df_neutro, df_asociado_2)

#Validacion de dato 



