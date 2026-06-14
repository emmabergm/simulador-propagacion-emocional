import matplotlib.pyplot as plt

def grafico(df_neutro, df_asociado_1, df_asociado_2): 
    """
    Genera un grafico de barras que comapra los promedios de las emociones (estres, motivacion y tranquilidad) en estado neutro, luego del comentario 1 y luego del comentario 2.

    Parametros
    ----------
    df_neutro : pandas.DataFrame
        DataFrame que contiene las valoraciones emocionales iniciales
    df_asociado_1 : pandas.DataFrame
        DataFrame que contiene las valoraciones emocioanles despues del primer comentario
    df_asociado_2 : pandas.DataFrame
        DataFrame con las valoraciones emocionales despues del segundo comentario

    Returns
    -------
    None
        Muestra el grafico en pantalla
    """

    emociones = ["estres", "motivacion", "tranquilidad"]
    
    valores_neutros = []
    valores_comentario_1= []
    valores_comentario_2= []
    
    for emocion in emociones:
        valores_neutros=valores_neutros.append(df_neutro[emocion].mean())
        valores_comentario_1=valores_comentario_1.append(df_asociado_1[emocion].mean())
        valores_comentario_2=valores_comentario_2.append(df_asociado_2[emocion].mean())
        
    x = range(len(emociones))
    ancho = 0.2

    plt.figure()

    plt.bar(
        x,
        valores_neutros,
        width=ancho,
        label="Neutro"
    )

    plt.bar(
        [i + ancho for i in x],
        valores_comentario_1,
        width=ancho,
        label="Comentario 1"
    )

    plt.bar(
        [i + ancho*2 for i in x],
        valores_comentario_2,
        width=ancho,
        label="Comentario 2"
    )

    plt.xticks(
        [i + ancho for i in x],
        emociones
    )

    plt.ylabel("Nivel emocional promedio")

    plt.title("cambios emocionales")

    plt.legend()

    plt.ylim(0, 100)

    plt.show()
        

    
   
    '''
    Funcion que crea el grafico a partir de los datos

    Parameters
    ----------
    archivo_comentarios : csv
        Archivo que contiene los dos comentarios elegidos por el usuario 
    archivo_e_n : csv
        Archivo que contiene datos de las emociones neutras de los estudiantes 
    archivo_e_comentario1 : csv
        Archivo que contiene datos de las emcoiones despues que se haga el coemntario 1
    archivo_e_comentario2 : csv
        Archivo que contiene datos de las emcoiones despues que se haga el coemntario 2

    Returns
    -------
    Grafico 

    '''
   
    pass 
