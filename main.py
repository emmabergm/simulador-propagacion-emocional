import pandas as pd

from src.comentarios import situacion
from src.comentarios import realizar_pregunta
from src.comentarios import asociacion
from src.alumnos import info_estudiante2 
from src.alumnos import valoracion_comentario
from src.analisis import  unir_datos_emocionales
from src.analisis import calcualar_promedios_grupales
from src.analisis import comparar_promedios
from src.analisis import feedback_comentario

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
primer_comentario = funcion(situacion_estudiante, planteo_situacion_1)

situacion_estudiante = situacion()
planteo_situacion_2 = realizar_pregunta(df_comentario)

respuesta_1 = realizar_pregunta(df_comentario) 


if menu_1 == "True": 
  estudiante_2 = input("Ingrese su nombre: ")
  
else: 
  print("Muchas gracias por su respuesta!") #NO ESTA BIEN 
edad_e_2 = int(input("Ingrese su edad: ")
menu_1 = "funcion de menu"
