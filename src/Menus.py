# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:02:31 2026

@author: olivi
"""

def menu_inicio(nombre, situacion): 
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
    
    dicc_cargados = {}
    
    
    
    while True: 
        if nombre in dicc_cargados: 
            eleccion = input("Desea continuar con la informacion ya cargada?: ")
            eleccion = eleccion.lower()
            return eleccion 
            break 
       
        if (eleccion != "si") or (eleccion != "no"): 
            raise ValueError ("Debe responder con si o con no")
           
        else: 
            dicc_cargados[situacion] = nombre 
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
            
        return situacion 
    


                    
                            
                    
               
                   
       
        

    
    
    
            
        
        
        
       
        
    
    

            
