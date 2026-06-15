


from src.comentario import realizar_pregunta
from src.comentario import guardar_respuesta
from src.alumnos import info_estudiante2
from src.alumnos import presentar_comentario
from src.alumnos import valoracion_comentario



 

def parte_1(situacion, indice, df_comentario): 
    
        respuesta = realizar_pregunta(df_comentario,indice)
        df_respuesta = guardar_respuesta(respuesta, indice, df_comentario, situacion )
    
        return respuesta  
    
        
        
def parte_2(df_neutro, df_comentario, respuesta, indice, situacion,df_asociado):
    
    estudiante_2, edad_2 =info_estudiante2(df_neutro,situacion)
    comentario=presentar_comentario(df_comentario, respuesta, indice, situacion)
    valoracion_post= valoracion_comentario(estudiante_2, edad_2,comentario,situacion, df_asociado)
    
    return comentario
    
    
    
    
    
    
    