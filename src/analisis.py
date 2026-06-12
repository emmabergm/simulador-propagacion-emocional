
def unir_ideas (df_neutro, df_post1, df_post2):
    '''
    Se une la informacion de cada estudiante segun la emocion. 

    Parameters
    ----------
    situacion : str
        Contexto academico, parciales no parciales.
    respuesta : str
        Letra que representa el comentario.

    Returns
    -------
    df_comparacion : xlsx
        Las emociones, respectivamnete, de cada estudiante.

    '''
    df_comparacion = pd.merge(
        df_neutro,
        df_post1,
        on="nombre")

    df_comparacion = df_comparacion.drop(
        columns=["edad", "situacion"]
    )

    return df_comparacion
    


def calcualar_promedios_grupales(df):
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
    
    
    if df.empty:
        raise ValueError ("No hay datos para calcular el promedio")
        
    dicc_promedio = {}
    
    promedio_estres = df.groupby["estres"].mean()
    promedio_motivacion = df.groupby["motivacion"].mean()
    promedio_tranquilidad = df.groupby["tranquilidad"].mean()
    
    
    dicc_promedio["estres"] = promedio_estres 
    dicc_promedio["motivacion"] = promedio_motivacion 
    dicc_promedio["tranquilidad"] = promedio_tranquilidad
    
     
            
    
    return dicc_promedio 

def comparar_promedios(diccionario_promedio_neutro, diccionario_promedio_post): 
   """
    Recibe como parametro el diccionario del promedio neutro y el diccionario del promedio post el comentario dependiendo de la situacion. 
    
    Va a comparar el promedio de las emociones neutras y luego el promedio de las emociones luego del comentario. 


    Parameters
    ----------
    diccionario_promedio_neutro : dicc
        Diccionario con los estados emocionales neutros
    diccionario_promedio_post : dicc
        Diccionario con los estados emocionales depues del comentario.

    Returns
    -------
    cambio: float
        Devuelve la diferencia entre los promedios; para ver el cambio de lso estados emocionales en el grupo. 

    """

   cambio_estres= diccionario_promedio_post["estres"] - diccionario_promedio_neutro["estres"] 
   cambio_tranquilidad= diccionario_promedio_post["tranquilidad"] - diccionario_promedio_neutro["tranquilidad"]
   cambio_motivacion= diccionario_promedio_post["motivacion"] - diccionario_promedio_neutro["motivacion"]
   
   #print("El cambio en el estres fue: ", cambio_estres)
   #print("El cambio en la tranquilidad fue: ", cambio_tranquilidad)
   #print("El cambio en la motivacion fue: ", cambio_motivacion)
   
   return cambio_estres, cambio_tranquilidad, cambio_motivacion

       
   

   



#def identificar_emocion_mas_afectada(df_cambios):
    #"""
    #Identifica cuál fue la emoción que más cambió después del comentario.

    #Esta función analiza los cambios emocionales calculados y determina si el
    #comentario afectó principalmente el estrés, la calma, la motivación, la
    #ansiedad u otra emoción medida.
  
    #"""
    #pass
#Agregar para complejizar: PREGUNTAR


def feedback_comentario( situacion,comentario, cambio_estres, cambio_tranquilidad, cambio_motivacion ): 
    """
    Ante el comentario, que va a depender de la situacion academica, el cambio va a ser disitno. 
    Esta funcion analiza el cambio en cada caso. 

    Parameters
    ----------
    situacion: str
        Situacion en la que se da el comentario. 
    comentario : str
        Comentario elegido por el usuario
    cambio_estres : float
        Cambio que tuvo la emocion estres a partir del comentario.
    cambio_tranquilidad : float
        Cambio que tuvo la emocion tranquilidad a partir del comentario. 
    cambio_motivacion : float
        Cambio que tuvo la emocion motivacion a partir del comentario. 

    Returns
    -------
    feedback: str
        Analisis del comentario

    """
    
    if situacion == "parciales": 
        if (cambio_estres > cambio_motivacion) and ( cambio_estres > cambio_tranquilidad): 
            mensaje= "En parciales no esta bueno hacer ese comentario porque genera mucho estres en el grupo"
        elif (cambio_motivacion > cambio_tranquilidad) and (cambio_motivacion > cambio_estres): 
            mensaje= "El comentario fue positivo ya que ayudo a motivar a mucha gente para sus proximos examenes!!"
        else: 
            mensaje= "Gracias por tu comentario, este ayudo a tranquilizar a tus companeros de clase"
            
    elif situacion == "no parciales": 
        if (cambio_estres > cambio_motivacion) and ( cambio_estres > cambio_tranquilidad): 
            mensaje= "Intenta eviatr un comentario asi ya que estresa al grupo"
        elif (cambio_motivacion > cambio_tranquilidad) and (cambio_motivacion > cambio_estres): 
            mensaje= "Esta buenisimo este tipo de comentario durante la cursada ya que motiva a los alumnos a seguir enfocados"
        else: 
            mensaje= "Comentar algo asi siempre es bienvenido porque tranquiliza el estres!!"
            
    return mensaje 
            
        
    
