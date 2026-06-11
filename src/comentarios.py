import random 

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

def numero_random(df_comentario): 
    '''
    Genera un numero random. Este numero representa una situacion academica distinta. 

    Parameters
    ----------
    df_comentario : xlsx
        Archivo donde estan guardados las situaciones que plantea la profesora y las opciones de comentario que se puedan hacer.

    Returns
    -------
    int: el numero random que representa la situacion. 

    '''
    id_situacion= random.randint(0, len(df_comentario)-1)
    
    return id_situacion 

def realizar_pregunta(df_comentario, id_situacion ): 
    '''
    Ante la situacion generada por el prgrama, la idea es que el usuario sea presentado con tres alternativas de comentario que le puede hacer a su grupo de clase. 
    Su respuesta va a estar condicionada por el conetexto academico en el que esta. 

    Parameters
    ----------
    df_comentario : xlsx
        Archivo en el que se presentan las distintas situaciones que presenta una profesora y los comentarios posibles que puede hacer el estudiante.
    id_situacion : int
        Es un numero que representa una situacion (academica) planteada por la profesora.
        
    Raises
    ------
    ValueError si la opcion no es valida, es decir, si no ingresa a,b o c. 

    Returns
    -------
    respuesta : str
        Letra que representa un comentario elegido por el estudiante.

    '''
    
    opciones = df_comentario[df_comentario["id_situacion"] == id_situacion]
    
    for i in range(len(opciones)): 
        print(
            opciones.iloc[i]["opcion"],
            opciones.iloc[i]["comentario"])
        
    print("Ante esta situacion: ", id_situacion)
   
    try: 
        respuesta=input("Que comentario le harias a tu clase? (a,b,c) porfavor ingresar en minusculas: ")
    except ValueError: 
        print('Opcion invalida')
        respuesta=input("Que comentario le harias a tu clase? (a,b,c) porfavor ingresar en minusculas: ")
    
    return respuesta 
        
    
    
    
    
    
    
    
    
    
    
    
    
    
   
        
        
    
        
        
        
    
          
        
        
    
     

