def info_estudiante2 (df_neutro,situacion):
    '''
    Le solicita la informacion personal y el estado emocional inicial de un estudiante, valida los datos ingresados y los almacena en el DataFrame de emociones neutras
    
    Parameters
    ----------
    df_neutro: DataFrame 
        Dataframe con la informacion predeterminada de estudiantes en estado neutro  
          
    Raises 
    -------
    ValueError
        Si la edad ingresada es negativa o si alguna de las valoraciones emocionales se encuentra fuera del rango permitido
    
    Returns
    -------
    estudiante_2 : str
        Nombre del estudiante dos que va a valorar sus emociones a partir de los comentarios 
    edad_e_2: int
        Edad del estudiante 2 
    '''
    estudiante_2 = input("Ingrese su nombre: ")

    while True:
        try:
            edad_e_2 = int(input("Ingrese su edad: "))
        
        except ValueError:
            print("Debe ingresar un numero")
            continue
        if edad_e_2 < 0:
            print("La edad no puede ser negativa")
            continue
        break

    while True:
        try:
            estres = int(input("Ingrese su estado de estres actual (rango valido: 1-100): "))
        except ValueError:
            print("Debe ingresar un numero")
            continue
        if not (1 <= estres <= 100):
            print("Los valores deben encontrarse dentro del rango (1 - 100)")
            continue
        break

    while True:
        try:
            motivacion = int(input("Ingrese su estado de motivacion actual (rango valido: 1-100): "))
        except ValueError:
            print("Debe ingresar un numero")
            continue
        if not (1 <= motivacion <= 100):
            print("Los valores deben encontrarse dentro del rango (1 - 100)")
            continue
        break

    while True:
        try:
            tranquilidad = int(input("Ingrese su estado de tranquilidad actual (rango valido: 1-100): "))
        except ValueError:
            print("Debe ingresar un numero")
            continue
        if not (1 <= tranquilidad <= 100):
            print("Los valores deben encontrarse dentro del rango (1 - 100)")
            continue
        break

    df_neutro.loc[len(df_neutro)] = estudiante_2, edad_e_2, situacion, estres, motivacion, tranquilidad
    return estudiante_2, edad_e_2
  
  

def presentar_comentario(df_comentario, respuesta, situacion ): 
    '''
    La funcion se encarga de encontrar en el DataFrame el comentario y presentarselo al usuario 2 que va a valorar su estado emocional a partir de eso
    Parameters
    ----------
    df_comentario : pandas.DataFrame
        DataFrame que contiene los comentarios de las distintas situaciones
    respuesta : str
        Respuesta seleccionada por el usuario en la primera parte de la actividad
    indice : int
        Numero random elegido por el programa correspondiente a la opcion a elegir de las respuestas
    situacion : str
        Situacion para la cual se desea obtener el comentario asociado
        
    Returns
    -------
    str: 
        Comentario del DataFrame elegido por el usuario 1.

    '''
    
    try:
        comentario = df_comentario.loc[(df_comentario["opcion"] == respuesta) & (df_comentario[situacion] == "True"), "comentario"].iloc[0]
        return comentario
    except Exception as e:
        print(f"Error en presentar_comentario: {e}")
        raise

def valoracion_comentario(estudiante_2, edad_e_2, comentario, situacion, df_asociado, indice, df_comentario): 
    '''
    Presentarle al estudiante_2 el comentario elegido por el estudiante_1 y preguntarle su valoracion
    (Van a presentarse 2 comentarios) (Validar datos)
    Parameters
    ----------
     estudiante_2 : str
        Nombre del estudiante 2 que va a valorar sus emociones a partir de los comentarios 
     edad_e_2 : int
         Edad del estudiante 2 
    df_comentario : pandas.DataFrame
        DataFrame que tiene guardado el comentario que eligio el estudiante 1
    df_asociado : pandas.DataFrame
        DataFrame en el que se va a guardar la valoracion que haga el estudiante 2 luego del comentario

    Raises
    -----
    ValueError
        Si alguna de las valoraciones emocionales ingresadas se encuentra fuera del rango
        
    Returns
    -------
    None.

    '''
  
        
    if situacion == "parciales":
        print("\nContexto: ")
        print("El siguiente comentario fue hecho por un estudiante en un periodo de PARCIALES.")
        print("Imaginá que vos también estás en esa situación: con examenes proximos, presion academica y poco tiempo libre.")
        print(f"Situacion específica: {df_comentario.iloc[indice]['situacion']}")
        print(f"Comentario: {comentario}")
       
    else:
        print("\nContexto: ")
        print("El siguiente comentario fue hecho por un estudiante en un periodo SIN PARCIALES.")
        print("Imaginá que vos también estás en esa situación: sin examenes proximos, con más tiempo libre y menos presion academica.")
        print(f"Situacion específica: {df_comentario.iloc[indice]['situacion']}")
        print(f"Comentario: {comentario}")
        

    while True:
        try:
            valoracion_estres = int(input("Ingresa tu valoracion de estres: "))
        except ValueError:
            print("Debe ingresar un numero")
            continue
        if not (1 <= valoracion_estres <= 100):
            print("Los valores deben encontrarse dentro del rango (1 - 100)")
            continue
        break

    while True:
        try:
            valoracion_motivacion = int(input("Ingresa tu valoracion de la emocion motivacion: "))
        except ValueError:
            print("Debe ingresar un numero")
            continue
        if not (1 <= valoracion_motivacion <= 100):
            print("Los valores deben encontrarse dentro del rango (1 - 100)")
            continue
        break

    while True:
        try:
            valoracion_tranquilidad = int(input("Ingresa tu valoracion de la emocion tranquilidad: "))
        except ValueError:
            print("Debe ingresar un numero")
            continue
        if not (1 <= valoracion_tranquilidad <= 100):
            print("Los valores deben encontrarse dentro del rango (1 - 100)")
            continue
        break

    df_asociado.loc[len(df_asociado)] = estudiante_2, edad_e_2, situacion, valoracion_estres, valoracion_motivacion, valoracion_tranquilidad
   
  
    
   

    
    
                       
                       
    
