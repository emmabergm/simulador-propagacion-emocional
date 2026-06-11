# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:02:31 2026

@author: olivi
"""

def menu_parte_1(): 
    '''
    Pregunta si desea salir o seguir con la Parte 2, si desea salir 
    se imprime un mensaje agradeciendo la participacion y se corta el programa
    
    Raises 
    -------
    ValueError
        Si la palabra no es seguir 

    Returns
    -------
    bool: devuelve True si desea seguir 

    '''

    while True:

        opcion = input(
            "Escriba 'seguir' para continuar con la parte 2: ").lower()

        if opcion == "seguir":
            return True
            break
        
        else:
            raise ValueError("Debe ingresar 'seguir' para poder continuar con la parte 2")
    
    

            
