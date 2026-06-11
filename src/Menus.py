# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:02:31 2026

@author: olivi
"""

def menu_inicio(nombre): 
    '''
    Agrega los nombres a una lista, para guardar los datos de los usuarios que ingresan 

    Parameters
    ----------
    nombre : str
        Nombre de un grupo experimental


    Returns
    -------
    None.

    '''
    
    nombres = []
    
    
    while True: 
        if nombre in nombres: 
            eleccion = input("Desea continuar con la informacion ya cargada?: ")
            eleccion = eleccion.lower()
            return eleccion 
            break 
       
        if (eleccion != "si") or (eleccion != "no"): 
            raise ValueError ("Debe responder con si o con no")
           
        else: 
            nombres.append(nombre)
            return "si"
            break
    
def menu_situacion(situacion):   
    '''
    

    Parameters
    ----------

   situacion: str
       Situacion en la que se encuentra, parciales o no parciales 

    Raises
    ------
    ValueError
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    situaciones = []
    
    while True: 
        situaciones.append(situacion)
        
        if (situacion != "parciales") and (situacion != "no parciales"):
            raise ValueError("La situacion ingresada no existe")
            
        
        elif situacion in situaciones: 
            raise ValueError("La situacion ya fue ingresada")
            
        else: 
            break
        
        if situacion == "no parciales": 
            situacion = "no_parciales"
        

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
    
    

            
