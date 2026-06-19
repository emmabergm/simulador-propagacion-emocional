import matplotlib.pyplot as plt

def grafico(df_neutro, df_asociado_1, df_asociado_2): 
    """
    Genera un grafico de barras que compara los promedios de las emociones (estres, motivacion y tranquilidad) en estado neutro, luego del comentario 1 y luego del comentario 2.

    Parametros
    ----------
    df_neutro : pandas.DataFrame
        DataFrame que contiene las valoraciones emocionales iniciales
    df_asociado_1 : pandas.DataFrame
        DataFrame que contiene las valoraciones emocionales despues del primer comentario
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
        valores_neutros.append(df_neutro[emocion].mean())
        valores_comentario_1.append(df_asociado_1[emocion].mean())
        valores_comentario_2.append(df_asociado_2[emocion].mean())
        
    x = range(len(emociones))
    ancho = 0.2

    plt.figure()

    plt.bar(
        x,
        valores_neutros,
        width=ancho,
        label="Neutro",
        color="turquoise"
    )

    plt.bar(
        [i + ancho for i in x],
        valores_comentario_1,
        width=ancho,
        label="Comentario 1",
        color="gold"
    )

    plt.bar(
        [i + ancho*2 for i in x],
        valores_comentario_2,
        width=ancho,
        label="Comentario 2",
        color="blueviolet"
        
    )

    plt.xticks(
        [i + ancho for i in x],
        emociones
    )

    plt.ylabel("Nivel emocional promedio")

    plt.title("Cambios emocionales")

    plt.legend()

    plt.ylim(0, 100)

    plt.show()
    



def graficar_comparacion_emociones(df_comentario1, df_comentario2, emocion):
    """
    Genera y muestra tres histogramas, uno de cada emocion especifica, comparando los cambios en los valores luego de cada comentario.

    Parameters
    ----------
    df_comentario1: DataFrame
        DataFrame que contiene las valoraciones emocionales luego del primer comentario
    df_comentario2: DataFrame
        DataFrame que contiene las valoraciones emocionales luego del segundo comentario
    emocion: str
        Nombre de la emocion a analizar, sea "tranquilidad", "estres" o "motivacion"

    Raises
    ------
    Exception
        Si ocurre un error al obtener los datos o al generar el grafico

    Returns
    -------
    None.
        La funcion solamente muestra en pantalla un histograma comparativo de cada emocion. 
    """
    try:
        bins = 5
        valores_1 = df_comentario1[emocion]
        valores_2 = df_comentario2[emocion]

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(valores_1, bins=bins, range=(0, 100), alpha=0.6, label="Comentario 1", color="red", edgecolor="black")
        ax.hist(valores_2, bins=bins, range=(0, 100), alpha=0.6, label="Comentario 2", color="green", edgecolor="black")
        ax.set_xlabel(emocion.capitalize())
        ax.set_ylabel("Cantidad de personas")
        ax.set_title(f"Distribución de {emocion}: comentario 1 vs comentario 2")
        ax.legend()
        ax.grid(axis="y", linestyle="--", alpha=0.4)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error en graficar_comparacion_emociones: {e}")
        raise
