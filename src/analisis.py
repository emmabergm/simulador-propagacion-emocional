
import pandas as pd 

def calcualar_promedios_grupales(df):
    """
  Calcula los promedios emocionales del grupo.

  Esta función recibe un DataFrame con las valoraciones emocionales de los
  estudiantes y calcula el promedio de estrés, motivación y tranquilidad.
  Luego devuelve esos promedios en un nuevo DataFrame.

  Parameters
  ----------
  df : DataFrame
      DataFrame con las columnas "estres", "motivacion" y "tranquilidad".

  Raises
  ------
  ValueError
      Si el DataFrame está vacío y no hay datos para calcular el promedio.

  Returns
  -------
  df_promedio : DataFrame
      DataFrame con una fila que contiene los promedios de estrés,
      motivación y tranquilidad.
  """
      
    try:
        if df.empty:
            raise ValueError("No hay datos para calcular el promedio")
        df_promedio = pd.DataFrame([df[["estres", "motivacion", "tranquilidad"]].mean()])
        return df_promedio
    except Exception as e:
        print(f"Error en calcualar_promedios_grupales: {e}")
        raise
        
    

def comparar_promedios(promedio_neutro, promedio_comentario): 
 """
    Compara los promedios emocionales neutros con los promedios posteriores
    a un comentario.

    Esta función calcula la diferencia entre los promedios posteriores al
    comentario y los promedios neutros. Permite observar si el estrés,
    la motivación y la tranquilidad aumentaron o disminuyeron después
    del comentario.

    Parameters
    ----------
    promedio_neutro : DataFrame
        DataFrame con los promedios emocionales iniciales o neutros.
        Debe contener las columnas "estres", "motivacion" y "tranquilidad".

    promedio_comentario : DataFrame
        DataFrame con los promedios emocionales posteriores al comentario.
        Debe contener las columnas "estres", "motivacion" y "tranquilidad".

    Returns
    -------
    cambio_estres : float
        Diferencia entre el promedio posterior y el promedio neutro de estrés.

    cambio_motivacion : float
        Diferencia entre el promedio posterior y el promedio neutro de motivación.

    cambio_tranquilidad : float
        Diferencia entre el promedio posterior y el promedio neutro de tranquilidad.
    """

    try:
        cambio_estres = promedio_comentario["estres"].iloc[0] - promedio_neutro["estres"].iloc[0]
        cambio_motivacion = promedio_comentario["motivacion"].iloc[0] - promedio_neutro["motivacion"].iloc[0]
        cambio_tranquilidad = promedio_comentario["tranquilidad"].iloc[0] - promedio_neutro["tranquilidad"].iloc[0]
        return cambio_estres, cambio_motivacion, cambio_tranquilidad
   except Exception as e:
        print(f"Error en comparar_promedios: {e}")
        raise

    

def feedback_comentario( situacion,comentario, cambio_estres, cambio_motivacion, cambio_tranquilidad ): 
    """
   Genera una devolución sobre el impacto emocional de un comentario.

   Esta función analiza los cambios emocionales producidos después de un
   comentario, teniendo en cuenta la situación académica en la que se encuentra
   el estudiante: "parciales" o "no_parciales".

   Según qué emoción haya aumentado más, la función devuelve un mensaje
   indicando si el comentario generó más estrés, más motivación o más
   tranquilidad en el grupo.

   Parameters
   ----------
   situacion : str
    Situación académica en la que se da el comentario. Puede ser
    "parciales" o "no_parciales".

comentario : str
    Comentario elegido por el usuario.

cambio_estres : float
    Cambio que tuvo la emoción estrés a partir del comentario.

cambio_motivacion : float
    Cambio que tuvo la emoción motivación a partir del comentario.

cambio_tranquilidad : float
    Cambio que tuvo la emoción tranquilidad a partir del comentario.
    
   Returns
   -------
   mensaje : str
       Mensaje con el análisis del impacto emocional del comentario.
   """
    try:
        if situacion == "parciales": 
            if (cambio_estres > cambio_motivacion) and (cambio_estres > cambio_tranquilidad): 
                mensaje = "En parciales no esta bueno hacer ese comentario porque genera mucho estres en el grupo"
            elif (cambio_motivacion > cambio_tranquilidad) and (cambio_motivacion > cambio_estres): 
                mensaje = "El comentario fue positivo ya que ayudo a motivar a mucha gente para sus proximos examenes!!"
            else: 
                mensaje = "Gracias por tu comentario, este ayudo a tranquilizar a tus companeros de clase"

        elif situacion == "no_parciales": 
            if (cambio_estres > cambio_motivacion) and (cambio_estres > cambio_tranquilidad): 
                mensaje = "Intenta evitar un comentario asi ya que estresa al grupo"
            elif (cambio_motivacion > cambio_tranquilidad) and (cambio_motivacion > cambio_estres): 
                mensaje = "Esta buenisimo este tipo de comentario durante la cursada ya que motiva a los alumnos a seguir enfocados"
            else: 
                mensaje = "Comentar algo asi siempre es bienvenido porque tranquiliza el estres!!"
        else:
            mensaje = f"Situacion no reconocida: '{situacion}'"

        return mensaje
    except Exception as e:
        print(f"Error en feedback_comentario: {e}")
        raise
        
    
