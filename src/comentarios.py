# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:01:36 2026

@author: olivi
"""
def situacion(estudiante_1): 
    '''
    Funcion que pregunta en que contexto se encuentra (parciales/no parciales) 
    
    Parameters
    ----------
    estudiante_1 : str
        nombre del estudiante que responde la pregunta 

    Returns
    -------
    situacion

    '''
    while True: 
        situacion = input("En que situacion academica se encuentra? (parcailes/ no parciales)")
    
        if (situacion != "parciales") and (situacion != "no parciales"):
            raise ValueError("La situacion ingresada no existe")
        else: 
            break 
    
    return situacion 
        

def realizar_pregunta(archivo): 
    '''
    Presentarle la sitaucion al usuario (que el programa presente una situacion random) y preguntar que comentario haria 

    Parameters
    -----------

    archivo: csv 
        archivo con situaciones y posibles respuestas 

    Returns
    --------
    str: respuesta (a,b,c)
    '''
    pass 

def guardar_respuesta(situacion, archivo):
    '''
    Guardar la eleccion de comentario del estudiante en cada situacion

    Parameters
    ----------
    funcion_pregunta: str
        La situacion y respuesta que ingreso el estudiante 
    
    archivo: cvs
        Archivo en donde se encuntran las opciones de comentarios y se guarda la elegida
        

    Returns
    -------
    archivo

    '''
    pass 
