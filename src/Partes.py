


from src.comentario import realizar_pregunta
from src.comentario import guardar_respuesta
from src.alumnos import info_estudiante2
from src.alumnos import presentar_comentario
from src.alumnos import valoracion_comentario



 

def parte_1(situacion, indice, df_comentario): 
    """
    Ejecuta la primer parte del programa. Presenta una pregunta al usuario, guarda su respuesta y la devuelve

     Parameters
     ----------
     situacion: str
         Contexto académico ingresado por el usuario. Puede ser "parciales"
         o "no parciales".

     indice: int
         Número entero aleatorio que representa una posición dentro del
         DataFrame.
    
     df_comentario: DataFrame
         DataFrame que contiene los comentarios

     Returns
     -------
     str
         Respuesta elegida por el usuario
         """
    
    respuesta = realizar_pregunta(df_comentario,indice)
    df_respuesta = guardar_respuesta(respuesta, indice, df_comentario, situacion )
    return respuesta  
    
        
        
def parte_2(df_neutro, df_comentario, respuesta, indice, situacion,df_asociado):
    """
    Ejecuta la segunda parte del programa. Toma los datos del segundo estudiante, se le presenta el comentario y registra su valoracion emocioanl ante tal comentario.
    
    Parameters
    ----------
    df_neutro: DataFrame
         DataFrame que contiene las valoraciones emocionales neutras

    df_comentario: DataFrame
         DataFrame que contiene los comentarios

    respuesta: str
         Respuesta elegida por el primer estudiante

    indice: int
         Número entero aleatorio que representa una posición dentro del
         DataFrame.
        
    situacion: str
         Contexto académico ingresado por el usuario. Puede ser "parciales"
         o "no parciales".

    df_asociado: DataFrame
         DataFrame donde se guardan las valoraciones emocionales luego del comentario

    Returns
    -------
    str
         Comentario presentado y nombre del estudiante
    int
         Edad del estudiante
    """
    estudiante_2, edad_2 =info_estudiante2(df_neutro,situacion)
    comentario=presentar_comentario(df_comentario, respuesta, situacion)
    valoracion_post= valoracion_comentario(estudiante_2, edad_2,comentario,situacion, df_asociado, indice, df_comentario)
    
    return comentario, estudiante_2, edad_2
    
def parte_2_comentario2(df_comentario, respuesta, indice, situacion, df_asociado, estudiante_2, edad_2):
   """
   Presenta un segundo comentario al usuario y registra su valoracion emovional despues de este.

   Parameters
   ----------
   df_comentario: DataFrame
       DataFrame que contiene los comentarios

   respuesta: str
       Respuesta elegida por el primer estudiante

   indice: int
       Número entero aleatorio que representa una posición dentro del
      DataFrame.

   situacion: str
       Contexto académico ingresado por el usuario. Puede ser "parciales"
       o "no parciales".
     
   df_asociado: DataFrame
       DataFrame donde se guardan las valoraciones emocionales luego del comentario

   estudiante_2: str
       Nombre del segundo estudiante
   edad_2: int
       Edad del segundo estudiante

   Returns
   -------
   str
       Comentario presentado al estudiante
   """
 
   comentario = presentar_comentario(df_comentario, respuesta, situacion)
   valoracion_post = valoracion_comentario(estudiante_2, edad_2, comentario, situacion, df_asociado, indice, df_comentario)
   return comentario


    
    
    
