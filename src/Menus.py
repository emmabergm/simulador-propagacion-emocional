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
    
if nombre in dicc_cargados:   
    while True: 
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
    
    

def menu_parte_1(info_estudiante2, presentar_comentario,valoracion_comentario,grafico,calcular_promedios_grupales,comparar_promedios,feedback_comentario):
    '''
    Muestra un menu sobre las opciones que puede realizar con el programa. 

     Parameters
    ----------
    info_estudiante2 : function
        Función que solicita y devuelve las emociones iniciales de un
        nuevo estudiante.

    presentar_comentario : function
        Función que presenta una situación académica y permite seleccionar
        un comentario.

    valoracion_comentario : function
        Función que registra las emociones del estudiante luego de
        visualizar el comentario.

    grafico : function
        Función que genera y muestra gráficos con los cambios emocionales.

    calcular_promedios_grupales : function
        Función que calcula los promedios grupales de estrés,
        motivación y tranquilidad.

    comparar_promedios : function
        Función que compara los promedios emocionales antes y después
        de los comentarios.

    feedback_comentario : function
        Función que genera una devolución sobre el impacto emocional
        de los comentarios seleccionados.
    
    Raises
    ------
    ValueError
        Si el usuario ingresa una opción no válida en alguno de los
        menús interactivos.

    Returns
    -------
    None.
        
    
    '''
    
    
    while True:
        try: 
            continuar=input("Desea continuar con el programa? (si/no)").lower()
            
            
            if continuar=="no": 
                print("Gracias por participar")
                break
            
           elif continuar=="si":
               
               print("1. Agregar otro estudiante.","\n", "Permite cargar el estado emocional inicial, presentar una situacion y valorar el comentario",'\n')
               print("2. Visualizar grafico","\n","Muestra los cambios emocionales generados a partir de los comentario (Esto va a incluir datos simulados)")
               print("3.Ver metricas", "\n", "muestra promedios grupales, cambios emocionales y feedback del comentario (Esto va a incluir datos simulados)",'\n')
               
               accion = int(input("Que quiere realizar? : "))
                
                try: 
                    if accion == 1: 
                        while True: 
                            agregar_estudiante=input("Desea agregar la informacion de otro estudiante? (si/no) ")
                            if agregar_estudiante=="si": 
                                estres_neutro2,tranquilidad_neutro2,motivacion_neutro2= info_estudiante2()
                                comentario2 = presentar_comentario()
                                estres_e2,tranquilidad_e2,motivacion_e2=valoracion_comentario()
                                return comentario2 
                            if agregar_estudiante=="no": 
                                print("Se termino la carga de estudiantes")
                                break
                        
                   
                    elif accion == 2: 
                        ver_grafico= grafico()
                        return ver_grafico
                        
                    elif accion == 3: 
                        print("Promedios grupales: ", calcular_promedios_grupales(), "/n", 
                              "Cambios de las emociones: ", comparar_promedios(), "/n", 
                              "Feedback del comentario: ", feedback_comentario())
                except ValueError: 
                    print("La opcion es invalida")
                    accion=input("Que quiere realizar?: x: agregar otro estudiante, y:visualizar grafico, z:ver metricas")
            
        except ValueError: 
                    print("Debe ingresar si o no")
                    continuar=input("Desea continuar con el programa? (si/no)")
                    
                            
                    
               
                   
       
        

    
    
    
            
        
        
        
       
        
    
    

            
