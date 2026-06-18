import random 

def situacion(): 
   '''
   Solicita al usuario el contexto académico en el que se encuentra.

    Esta función pregunta si el estudiante se encuentra en una situación de
     "parciales" o "no parciales". La respuesta se convierte a minúscula para
     evitar errores por el uso de mayúsculas.

     Returns
     -------
     situacion : str
     Contexto académico ingresado por el usuario. Puede ser "parciales"
     o "no parciales".

     Raises
     ------
     ValueError
     Si el usuario ingresa una situación distinta de "parciales" o
    "no parciales".
    
   '''
   while True:
           situacion = input("En que situacion academica se encuentra? (parciales/ no parciales): ").lower()

           if (situacion != "parciales") and (situacion != "no parciales"):
               print("La situacion ingresada no existe")
               continue

           if situacion == "no parciales":
               situacion = "no_parciales"
           return situacion
      
        


def numero_random(df_comentario): 
   '''
    Genera un índice aleatorio para seleccionar una situación del DataFrame.

    Esta función utiliza la cantidad de filas del DataFrame de comentarios
    para generar un número aleatorio. Ese número se usa como índice para elegir
    una situación académica al azar.

    Parameters
    ----------
    df_comentario : DataFrame
        DataFrame que contiene las situaciones académicas y los comentarios
        posibles.

    Returns
    -------
    indice : int
        Número entero aleatorio que representa una posición dentro del
        DataFrame.
    '''
   try:
        indice = random.randint(0, len(df_comentario)-1)
        return indice
   except Exception as e:
        print(f"Error en numero_random: {e}")
        raise
    


    
    
def realizar_pregunta(df_comentario, indice): 
    '''
    Presenta una situación académica y solicita al usuario elegir un comentario.

    Esta función toma una situación del DataFrame usando un índice aleatorio.
    Luego muestra el contexto al usuario junto con tres posibles comentarios:
    opción "a", opción "b" y opción "c". Finalmente, solicita al usuario que
    ingrese la letra del comentario que haría a su grupo de estudio.

    Parameters
    ----------
    df_comentario : DataFrame
        DataFrame que contiene las situaciones académicas y las opciones de
        comentarios disponibles.

    indice : int
        Índice utilizado para seleccionar una situación dentro del DataFrame.

    Returns
    -------
    respuesta : str
        Letra elegida por el usuario. Puede ser "a", "b" o "c".
    '''
   
    
    situacion= df_comentario.iloc[indice]["id_situacion"]
    situacion_texto = df_comentario.iloc[indice]["situacion"]
    

    opciones = df_comentario[df_comentario["id_situacion"] == situacion]

    
        
    
   
    a = opciones[opciones["opcion"] == "a"]["comentario"].values[0]
    b = opciones[opciones["opcion"] == "b"]["comentario"].values[0]
    c = opciones[opciones["opcion"] == "c"]["comentario"].values[0]
    
    
    print("Si te encontras en el siguiente contexto: ", situacion_texto)
    while True:
        respuesta = input(f"Que comentario le harias a tu grupo de estudio?\na) {a}\nb) {b}\nc) {c}\n ingrese su respuesta: ").lower()
        if (respuesta != "a") and (respuesta != "b") and (respuesta != "c"):
            print("Opcion invalida, elija a, b o c")
            continue
        break

    return respuesta

def guardar_respuesta (respuesta, indice, df, situacion_texto):
    '''
   Guarda en el DataFrame la respuesta elegida por el usuario.

   Esta función identifica la situación correspondiente al índice recibido y
   marca como "True" la opción de comentario elegida por el usuario dentro de
   la columna que representa la situación académica.

   Parameters
   ----------
   respuesta : str
       Letra elegida por el usuario. Puede ser "a", "b" o "c".

   indice : int
       Índice de la situación seleccionada dentro del DataFrame.

   df : DataFrame
       DataFrame que contiene las situaciones, las opciones de comentarios y
       las columnas correspondientes al contexto académico.

   situacion_texto : str
       Nombre de la columna donde se guardará la respuesta según el contexto
       académico. Por ejemplo, "parciales" o "no parciales".

   Returns
   -------
   df_respuesta : DataFrame
       DataFrame actualizado con la respuesta elegida marcada como "True".
   '''

    try:
        id_sit = df.iloc[indice]["id_situacion"]
        df.loc[(df["id_situacion"] == id_sit) & (df["opcion"] == respuesta), situacion_texto] = "True"
        df_respuesta = df
        return df_respuesta
    except Exception as e:
        print(f"Error en guardar_respuesta: {e}")
        raise
        
    
def asociacion(respuesta, df_tranquilidad, df_motivacion, df_estres): 
    '''
    Asocia la respuesta elegida con un DataFrame emocional.

    Esta función relaciona la opción de comentario elegida por el usuario con
    una emoción principal. Según la respuesta seleccionada, devuelve el
    DataFrame correspondiente a tranquilidad, motivación o estrés.

    Parameters
    ----------
    respuesta : str
        Letra elegida por el usuario. Puede ser "a", "b" o "c".

    df_tranquilidad : DataFrame
        DataFrame con los datos asociados a comentarios que generan mayor
        tranquilidad.

    df_motivacion : DataFrame
        DataFrame con los datos asociados a comentarios que generan mayor
        motivación.

    df_estres : DataFrame
        DataFrame con los datos asociados a comentarios que generan mayor
        estrés.

    Returns
    -------
    df_asociado : DataFrame
        DataFrame emocional asociado a la respuesta elegida.
    '''
    try:
        if respuesta == "a": 
            df_asociado = df_tranquilidad
        elif respuesta == "b": 
            df_asociado = df_motivacion 
        else: 
            df_asociado = df_estres
        return df_asociado
    except Exception as e:
        print(f"Error en asociacion: {e}")
        raise
        

    
    
    
    
    
    
    
    
    
    
    
   
        
        
    
        
        
        
    
          
        
        
    
     

