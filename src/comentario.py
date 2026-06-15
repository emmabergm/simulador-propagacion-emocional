import random 

def situacion(): 
    '''
    Funcion que pregunta en que contexto se encuentra (parciales/no parciales) 

    Returns
    -------
    situacion

    '''
    
    
    while True: 
        situacion = input("En que situacion academica se encuentra? (parcailes/ no parciales): ")
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
     
   
    
    situacion= df_comentario.iloc[indice]["id_situacion"]
    situacion_texto = df_comentario.iloc[indice]["situacion"]
    

    opciones = df_comentario[df_comentario["id_situacion"] == situacion]

    
        
    
   
    a = opciones[opciones["opcion"] == "a"]["comentario"].values[0]
    b = opciones[opciones["opcion"] == "b"]["comentario"].values[0]
    c = opciones[opciones["opcion"] == "c"]["comentario"].values[0]
    
    
    print("Si te encontras en el siguiente contexto: ", situacion_texto)

    try: 
        respuesta = input(f"Que comentario le harias a tu grupo de estudio?\na) {a}\nb) {b}\nc) {c}\n(ingresar en minuscula): ")
    except ValueError: 
        print('Opcion invalida')
        respuesta = input(f"Que comentario le harias a tu grupo de estudio?\na) {a}\nb) {b}\nc) {c}\n(ingresar en minuscula): ")
    
    return respuesta 

def guardar_respuesta (respuesta, indice, df, situacion_texto):
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
    

    id_sit = df.iloc[indice]["id_situacion"]
    df.loc[(df["id_situacion"] == id_sit) & (df["opcion"] == respuesta), situacion_texto] = "True"
    df_respuesta = df
   
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
    
    
    
    
    
    
    
    
    
    
    
    
   
        
        
    
        
        
        
    
          
        
        
    
     

