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
    
    a= df_comentario.iloc[indice]["a"]
    b= df_comentario.iloc[indice]["b"]
    c= df_comentario.iloc[indice]["c"]
    
    
    print("Ante esta situacion: ", situacion)
    try: 
        respuesta=input("Ante esta situacion, que comentario le harias a la clase?: (a,b,c) ingresar en minuscula")
    except ValueError: 
        print('Opcion invalida')
        respuesta=input("Ante esta situacion, que comentario le harias a la clase?: (a,b,c) ingresar en minuscula")
    
    return respuesta 
        
    
    
    
    
    
    
    
    
    
    
    
    
    
   
        
        
    
        
        
        
    
          
        
        
    
     

