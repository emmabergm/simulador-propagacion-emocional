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
    

def menu_parte_1(info_estudiante2, presentar_comentario,valoracion_comentario,grafico,calcular_promedios_grupales,comparar_promedios,feedback_comentario): 
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
        try: 
            continuar=input("Desea continuar con el programa? (si/no)")
            
            
            if continuar=="no": 
                print("Gracias por participar")
                break
            
            elif continuar=="si":
                
                print("1. Agregar otro estudiante.","\n", "Permite cargar el estado emocional inicial, presentar una situacion y valorar el comentario",'\n')
                print("2. Visualizar grafico","\n","Muestra los cambios emocionales generados a partir de los comentario")
                print("3.Ver metricas", "\n", "muestra promedios grupales, cambios emocionales y feedback del comentario",'\n')
                
                accion=input("Que quiere realizar? : ")
                
                try: 
                    if accion =="1": 
                        while True: 
                            agregar_estudiante=input("Desea agregar la informacion de otro estudiante? (si/no) ")
                            if agregar_estudiante=="si": 
                                estres_neutro2,tranquilidad_neutro2,motivacion_neutro2= info_estudiante2()
                                comentario2=presentar_comentario()
                                estres_e2,tranquilidad_e2,motivacion_e2=valoracion_comentario()
                            if agregar_estudiante=="no": 
                                print("Se termino la carga de estudiantes")
                                break
                        
                   
                    elif accion=="2": 
                        ver_grafico= grafico()
                        
                    elif accion=="3": 
                        print("Promedios grupales: ", calcular_promedios_grupales(), "/n", 
                              "Cambios de las emociones: ", comparar_promedios(), "/n", 
                              "Feedback del comentario: ", feedback_comentario())
                except ValueError as e: 
                    print("La opcion es invalida")
                    accion=input("Que quiere realizar?: x: agregar otro estudiante, y:visualizar grafico, z:ver metricas")
            
        except ValueError as e: 
                    print("Debe ingresar si o no")
                    continuar=input("Desea continuar con el programa? (si/no)")
                    
                            
                    
               
                   
       
        

    
    
    
            
        
        
        
       
        
    
    

            
