import pandas as pd

from src.comentarios import situacion
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

archivo_comentario = "C:/Users\camil\OneDrive\Documents\GitHub\simulador-propagacion-emocional\archivos\archivo_comentario (1).xlsx"

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
    
       

    menu_principal = menu_inicio(nombre_grupo, situacion)
   
  
    
    

        
# Parte 1 (interaccion con estudiante 1)
        
    
    if menu_principal == "si":  
        indice = numero_random()
        parte_1_sit1 = parte_1(situacion, indice, df_comentario)
        df_asociado_1 = asociado(parte_1_sit1, df_tranquilidad, df_motivacion, df_estres)
        parte_1_sit_2 = parte_1(situacion, indice, df_comentario)
        df_asociado_2 = asociado(parte_1_sit2, df_tranquilidad, df_motivacion, df_estres)
    
#Parte 2   

    menu_2 = menu_parte_2() 
    if menu_2 == "si": 
        parte_2_com1 = parte_2(df_neutro, df_comentario, parte_1_sit1, indice, situacion, df_asociado_1) #COMO LE PASAMOS LA SITUACION?????
        parte_2_com2 = parte_2(df_neutro, df_comentario, parte_1_sit2, indice, situacion, df_asociado_2)
        
    
# Parte 3

    menu_3 = menu_parte_3(df_neutro, df_asociado_1, df_asociado_2, situacion, df_comentario, parte_1_sit1, parte_1_sit2, indice)

except ValueError as e:
    ("Error: ")

    









