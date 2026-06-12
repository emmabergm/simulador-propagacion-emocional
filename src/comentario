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
        situacion = situacion.lower()
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


    
    
def realizar_pregunta(df_comentario): 
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
    #llamar archivo 
    
    indice= random.randint(0, len(df_comentario)-1)
    
    situacion= df_comentario.iloc[indice]["comentario profesora"]
    
<<<<<<< HEAD
    opciones = df_comentario[df_comentario["id_situacion"] == id_situacion]
<<<<<<< HEAD

=======
    
>>>>>>> 3114e40e2fb59d34368718ad23255f5f07000013
    for i in range(len(opciones)): 
        print(
            opciones.iloc[i]["opcion"],
            opciones.iloc[i]["comentario"])
        
    print("Ante esta situacion: ", id_situacion)
   
=======
    a= df_comentario.iloc[indice]["a"]
    b= df_comentario.iloc[indice]["b"]
    c= df_comentario.iloc[indice]["c"]
    
    
    print("Si te encontras en el siguiente contexto: ", situacion)
>>>>>>> d3a5af79fdbeb750269292902e5c1731406fe1e3
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
    
    
    
    
    
    
    
    
    
    
    
    
   
        
        
    
        
        
        
    
          
        
        
    
     

