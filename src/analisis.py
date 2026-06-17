
import pandas as pd 

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

    df_promedio = pd.DataFrame([df[["estres", "motivacion", "tranquilidad"]].mean()])

    return df_promedio
    
     


def comparar_promedios(promedio_neutro, promedio_comentario): 
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
   cambio_estres = promedio_comentario["estres"].iloc[0] - promedio_neutro["estres"].iloc[0]
   cambio_tranquilidad = promedio_comentario["tranquilidad"].iloc[0] - promedio_neutro["tranquilidad"].iloc[0]
   cambio_motivacion = promedio_comentario["motivacion"].iloc[0] - promedio_neutro["motivacion"].iloc[0]
   
   #print("El cambio en el estres fue: ", cambio_estres)
   #print("El cambio en la tranquilidad fue: ", cambio_tranquilidad)
   #print("El cambio en la motivacion fue: ", cambio_motivacion)
   
   return cambio_estres, cambio_tranquilidad, cambio_motivacion

       



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
    else:
        mensaje = f"Situacion no reconocida: '{situacion}'"
            
    return mensaje 
            
        
    
