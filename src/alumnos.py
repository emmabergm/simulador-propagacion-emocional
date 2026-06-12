


def info_estudiante2 (df_neutro):
    '''
    Le pregunta al estudiante por su informacion actual neutra 

    Parameters
    ----------
    df_neutro: DataFrame 
        Dataframe con la informacion predeterminada de estudiantes en estado neutro 
     estudiante_2 : str
        Nombre del estudiante dos que va a valorar sus emociones a partir de los comentarios 
      edad_e_2: int
          Edad del estudiante 2 
          
    Raises 
    -------
    ValueError
        si los valores estan fuera del rango 
    
    Returns
    -------
    None

    '''
    estudiante_2 = input("Ingrese su nombre: ")
    edad_e_2 = int(input("Ingrese su edad: "))
    
    if edad_e_2 < 0: 
        raise ValueError("La edad no puede ser negativa")

    while True: 
        estres = int(input("Ingrese su estado de estres actual: "))
        motivacion = int(input("Ingrese su estado de motivacion actual: "))
        tranquilidad = int(input("Ingrese su estado de tranquilidad actual: "))
        
        if (0 > tranquilidad > 100) or (0 > estres > 100) or (0 > motivacion > 100): 
            raise ValueError("Los valores deben encontrarse dentro del rango (1 - 100) ")
        else: 
            break 
        
    df_neutro.loc[len(df_neutro)] = estudiante_2, edad_e_2, estres, motivacion, tranquilidad
    
    return estudiante_2, edad_e_2 

def presentar_comentario(df_comentario, respuesta, indice, situacion ): 
    '''
    La funcion se encarga de encontrar en el DataFrame y presentarle el comentario al usuario 2 que va a valorar su estado emocional a partir de eso 

    Parameters
    ----------
    df_comentario : DataFrame
        DESCRIPTION.
    respuesta : str
        respuesta del usuario, es decir a,b,c
    indice : int
        numero random elegido por la computadora
    situacion : str
        situacion 1 en la que se encuentra el usuario 1
        
    Returns
    -------
    str: comentario elegido por el usuario 1 

    '''
    comentario = df_comentario.loc[(df_comentario["id_pregunta"] == 1) &(df_comentario[situacion] == True),"comentario"].iloc[0]
    print(comentario)
    
    return comentario

def valoracion_comentario(estudiante_2, edad_e_2, respuesta, df_comentario, df_asociado): 
    '''
    Presentarle al estudiante_2 el comentario elegido por el estudiante_1 y preguntarle su valoracion
    (Van a presentarse 2 comentarios) (Validar datos)
    Parameters
    ----------
     estudiante_2 : str
        Nombre del estudiante dos que va a valorar sus emociones a partir de los comentarios 
     edad_e_2: int
         Edad del estudiante 2 
    archivo_comentario : cvs
        archivo que tiene guardado el comentario que eligio el estudiante_1
    archivo_emociones: cvs
        archivo en el que se va a guardar la valoracion que haga el estudiante_2 del coemntario 

    Returns
    -------
    None.

    '''
    while True: 
        valoracion_estres = input("Cual seria tu valoracion emoicional el siguiente comentario:", 
                       df_comentario["respuesta"],
                       "Ingresa tu valoracion de estres: ") 
        valoracion_motivacion = input("Ingresa tu valoracion de la emocion motivacion: ")
        valoracion_tranquilidad = input("Ingresa tu valoracion de la emocion tranquilidad: ")
        df_asociado.loc[len(df_asociado)] = estudiante_2, edad_e_2,valoracion_estres, valoracion_motivacion, valoracion_tranquilidad
    
        if (0 > valoracion_estres > 100) or (0 > valoracion_motivacion > 100) or (0 > valoracion_tranquilidad > 100): 
            raise ValueError("Los valores deben encontrarse dentro del rango (1 - 100) ")
        else: 
            break 
    #ACA va a haber que llamar a la funcion 2 veces, cada vez para un comentario distinto#
    
    
                       
                       
    
