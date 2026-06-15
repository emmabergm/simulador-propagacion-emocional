import random 

def situacion(): 
    '''
    Funcion que pregunta en que contexto se encuentra (parciales/no parciales) 

    Returns
    -------
    situacion

    '''
    
    
    while True: 
        situacion = input("En que situacion academica se encuentra? (parcailes/ no parciales)")
        situacion = situacion.lower()
        
        
        if (situacion != "parciales") and (situacion != "no parciales"):
            raise ValueError("La situacion ingresada no existe")
        
        
            
        else: 
            break
        
        if situacion == "no parciales": 
            situacion = "no_parciales"
    
    return situacion 

def numero_random(df_comentario): 
    indice= random.randint(0, len(df_comentario)-1)
    return indice 
    


    
    
def realizar_pregunta(df_comentario, indice): 
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
     
    
   
    
    situacion= df_comentario.iloc[indice]["comentario profesora"]
    

    opciones = df_comentario[df_comentario["situacion"] == situacion]

    for i in range(len(opciones)): 
        print(
            opciones.iloc[i]["opcion"],
            opciones.iloc[i]["comentario"])
        
    print("Ante esta situacion: ", situacion)
   

    a= df_comentario.iloc[indice]["a"]
    b= df_comentario.iloc[indice]["b"]
    c= df_comentario.iloc[indice]["c"]
    
    
    print("Si te encontras en el siguiente contexto: ", situacion)

    try: 
        respuesta=input("Que comentario le harias a tu grupo de estudio?: ", a, b, c, "ingresar en minuscula")
    except ValueError: 
        print('Opcion invalida')
        respuesta = input("Que comentario le harias a tu grupo de estudio?:" , a, b, c, "ingresar en minuscula")
    
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
    DataFrame: Dataframe con la informacion actualizada, la respuesta elegida aparece como True

    '''
    
    df_respuesta = df.loc[(df["id_pregunta"] == indice) & (df["opcion"] == respuesta), situacion] = True
    
    return df_respuesta
    
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
    
    
    
    
    
    
    
    
    
    
    
    
   
        
        
    
        
        
        
    
          
        
        
    
     

