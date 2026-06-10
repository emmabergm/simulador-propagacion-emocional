# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:32:57 2026

@author: olivi
"""

def guardar_archivo_neutro(df_neutro, estudiante_2, edad_e_2, estres, motivacion, tranquilidad): 
    '''
    Agregar la informacion del estudiante_2 al archivo de emociones neutras 

    Parameters
    ----------
     df_neutro: DataFrame 
         Dataframe con la informacion predeterminada de estudiantes en estado neutro 
     estudiante_2 : str
        Nombre del estudiante dos que va a valorar sus emociones a partir de los comentarios 
     edad_e_2: int
         Edad del estudiante 2 
     estres : int 
       valoracion de estres del estudiante 2
     motivacion: int
         valoracion de motivacion del estudiante 2
    tranquilidad: int
        valoracion de tranquilidad del estudiante 2
    Returns
    -------
    None.

    '''
    df_neutro.loc[len(df_neutro)] = estudiante_2, edad_e_2, estres, motivacion, tranquilidad