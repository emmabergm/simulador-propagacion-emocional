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



#Parte 1 (interaccion con estudiante 1) - comentarios
try: 
    nombre_grupo = input("Ingrese el nombre de su grupo: ")
    
    situacion = situacion()
    
<<<<<<< HEAD
    try:
       
=======
    menu_principal = menu_inicio(nombre_grupo, situacion)
    indice = numero_random()
    respuesta = realizar_pregunta(indice, df_comentario)
    guardar_rta = guardar_respuesta(respuesta, indice, df_comentario, situacion )
    df_respuesta = guardar_respuesta(respuesta_1, indice, df_comentario, situacion_1 )
    df_asociado_1 = asociado(respuesta_1, df_tranquilidad, df_motivacion, df_estres)
    comentario=realizar_pregunta(df_comentario)
    
    
>>>>>>> 34e6c16e5776684109931f1814d426634c75d814
        
        
    
        if menu_principal == "si": 
            parte_1_sit1 = parte_1(situacion, indice, df_comentario)
            df_asociado_1 = asociado(parte_1_sit1, df_tranquilidad, df_motivacion, df_estres)
            parte_1_sit_2 = parte_1(situacion, indice, df_comentario)
            df_asociado_2 = asociado(parte_1_sit2, df_tranquilidad, df_motivacion, df_estres)
    
    parte_2 = 

# Parte 1 (interaccion con estudiante 1)






# Parte 1.2 

situacion_2 = situacion()
respuesta_2 = realizar_pregunta(indice, df_comentario)
df_respuesta = guardar_respuesta(respuesta_2, indice, df_comentario, situacion_2 )
df_asociado_2 = asociado(respuesta_1, df_tranquilidad, df_motivacion, df_estres)

# Menu 1 

menu_1 = menu_parte_1()

# Parte 2 (interaccion con estudiante 2)



if menu_1 == "True": 
 
  
else: 
  print("Muchas gracias por su respuesta!") #NO ESTA BIEN 

edad_e_2 = int(input("Ingrese su edad: "))

edad_e_2 = int(input("Ingrese su edad: "))

menu_1 = "funcion de menu"

edad_e_2 = int(input("Ingrese su edad: "))

informacion_estudiante2 = info_estudiante2 (df_neutro, estudiante_2, edad_e_2 )
presentar_comentario(df_comentario, respuesta_1, indice, situacion_1) 
valoracion_1 = valoracion_comentario(estudiante_2, edad_e_2, respuesta, df_comentario,  df_asociado_1)

#Parte 2.1 
presentar_comentario(df_comentario, respuesta_2, indice, situacion_2)
valoracion_2 = valoracion_comentario(estudiante_2, edad_e_2, respuesta, df_comentario,  df_asociado)

# Parte 3 (analisis)
#unir idea

promedio=calcular_promedios_grupales()
cambio_estres, cambio_motivacion, cambio_tranquilidad= comparar_promedios(promedio)
feedback=feedback_comentario(situacion, comentario, cambio_estres, cambio_tranquilidad, cambio_motivacion)



