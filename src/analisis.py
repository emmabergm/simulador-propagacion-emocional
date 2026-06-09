    
def cargar_datos_emociones(archivo_neutro, archivo_e_comentario1, archivo_e_comentario2):
    '''
    Abre los archivos con las emociones neutras y las emociones posteriores
    al comentario.

    Parameters
    ----------
    archivo_neutro : csv
        Archivo con las valoraciones de las emociones neutras
    archivo_e_coemntario1 : csv
        Archivo con las valoraciones de las emociones post coemntario 1
    archivo_e_coemntario2 : csv
        Archivo con las valoraciones de las emociones post coemntario 2
        
    Raises
    -------
    FileNotFound
        Si el archivo no existe o la ruta es incorrecta 
    Returns
    -------
    None.

    '''
    pass


def unir_datos_emocionales(df_neutro, df_post1, df_post2):
    '''
    Une la información emocional neutra y posterior de un mismo estudiante.

    Parameters
    ----------
    df_neutro : DataFrame
        Dataframe que contiene los datos neutros de las emociones  
    df_post1 : DataFrame
        Dataframe que contiene los datos leugo del comentario 1 de las emociones 
    df_post2: DataFrame
        Dataframe que contiene los datos leugo del comentario 2 de las emociones 
    

    Returns
    -------
    None.

    '''

    pass


def calcular_promedios_grupales(df):
    """
    Calcula los promedios emocionales del grupo y los agrega a un diccionario donde la clave es la emocion y el valor la valoracaion emocional 

    Parameters
    ----------
    df: DataFrame
        Se recibe el DataFrame del que se quiera sacar el promedio. 
        
    Raises
    ZeroDivision
        Si la cantidad de estudiantes que participa es igual a cero. 
    Returns
    -------
    diccionario_promedio: dicc
        Devuelve el promedio pedido 
    """
    pass

def comparar_promedios(diccionario_promedio_neutro, diccionario_promedio_post): 
   """
    Recibe como parametro el diccionario del promedio neutro y el diccionario del promedio post el comentario dependiendo de la situacion. 
    
    Va a comparar el promedio de las emociones neutras y luego el promedio de las emociones luego del comentario. 


    Parameters
    ----------
    diccionario_promedio_neutro : dicc
        Diccionario con los estados emocionales neutros
    diccionario_promedio_post : dicc
        Diccionario con los estados emocionales depues del comebario.

    Returns
    -------
    cambio: float
        Devuelve la diferencia entre los promedios; para ver el cambio de lso estados emocionales en el grupo. 

    """
   pass



#def identificar_emocion_mas_afectada(df_cambios):
    #"""
    #Identifica cuál fue la emoción que más cambió después del comentario.

    #Esta función analiza los cambios emocionales calculados y determina si el
    #comentario afectó principalmente el estrés, la calma, la motivación, la
    #ansiedad u otra emoción medida.
  
    #"""
    #pass
#Agregar para complejizar: PREGUNTAR


def feedback_emociones( situacion,comentario, cambio ): 
    """
    Ante el comentario, que va a depender de la situacion academica, el cambio va a ser disitno. 
    Esta fucnion analiza el cambio en cada caso. 

    Parameters
    ----------
    situacion: str
        Situacion en la que se da el comentario. 
    comentario : str
        COmentario elegido por el usuario
    cambio : float
        Cambio que tuvo cada emocion a partir del comentario. 

    Returns
    -------
    feedback: str
        Analisis del comentario

    """
