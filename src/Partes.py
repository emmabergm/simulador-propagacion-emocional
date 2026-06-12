# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 12:18:42 2026

@author: olivi
"""

from src.comentario import realizar_pregunta
from src.comentario import guardar_respuesta
 

def parte_1(situacion, indice, df_comentario): 
    
        respuesta = realizar_pregunta(indice, df_comentario)
        df_respuesta = guardar_respuesta(respuesta, indice, df_comentario, situacion )
    
        return respuesta  
    
        
        
def parte_2()
    
    