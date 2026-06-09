# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:02:31 2026

@author: olivi
"""

def menu_parte_1(): 
    '''
    Pregunta si desea salir o seguir con la Parte 2, si desea salir 
    se imprime un mensaje agradeciendo la participacion y se corta el programa

    Returns
    -------
    None.

    '''

    
    pregunta = input("Desea seguir con la segunda parte? ")
    if pregunta == "si": 
        return True 
    else: 
        print("Muchas gracias por su mensaje!")
        print("Ingrese "seguir" para continuar con la parte 2")    
        return False 
            
            
