import random 

def situacion(): 
    '''
    Funcion que pregunta en que contexto se encuentra (parciales/no parciales) 

    Returns
    -------
    situacion

    '''
    situaciones = []
    
    while True: 
        situacion = input("En que situacion academica se encuentra? (parcailes/ no parciales)")
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

def guardar_respuesta (respuesta, indice, df, situacion):
    '''
    Funcion que guarda la respuesta en el Dataframe 

    Parameters
    ----------
    respuesta : str
        a,b,c 
    indice : int
        Numero random generado por la computadora
    df : DataFrame
        Dataframe que contiene la inofrmacion de los comentarios, es decir la situacion y las posibles respuestas
    situacion : str
        situacion en la que se encuentra el estudiante 1, parciales o no parciales 

    Returns
    -------
    None.

    '''
    
    df.loc[(df["id_pregunta"] == indice) & (df["opcion"] == respuesta), situacion] = True
    
    
def asociacion(respuesta, df_tranquilidad, df_motivacion, df_estres): 
    '''
    

    Parameters
    ----------
    respuesta : str
        a, b, c, dependiendo lo que elige el usuario 1
    df_tranquilidad : DataFrame 
        Tabla con cambios emocionales predeterminados a partir de el comentario asociado a la emocion
    df_motivacion : DataFrame 
        Tabla con cambios emocionales predeterminados a partir de el comentario asociado a la emocion
    df_estres : DataFrame
        Tabla con cambios emocionales predeterminados a partir de el comentario asociado a la emocion

    Returns
    -------
    DataFrame asociado a la respuesta 

    '''
    
    if respuesta == "a": 
        df_asociado = df_tranquilidad
    
    elif respuesta == "b": 
        df_asociado = df_motivacion 
    
    else: 
        df_asociado = df_estres
        
    return df_asociado 
    
    
    
    
    
    
    
    
    
    
    
    
   
        
        
    
        
        
        
    
          
        
        
    
     

