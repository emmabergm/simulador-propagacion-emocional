import pandas as pd
import os


def cargar_datos():
    '''
    Carga todos los archivos de datos necesarios para el programa
    (estados emocionales neutros, comentarios asociados y grupos) y
    aplica las transformaciones iniciales correspondientes.

    Returns
    -------
    df_neutro : DataFrame
        Valoraciones emocionales iniciales.
    df_comentario : DataFrame
        Comentarios asociados a cada situación.
    df_motivacion : DataFrame
        Valoraciones emocionales luego del comentario motivacional.
    df_tranquilidad : DataFrame
        Valoraciones emocionales luego del comentario de tranquilidad.
    df_estres : DataFrame
        Valoraciones emocionales luego del comentario de estres.
    df_grupos : DataFrame
        Grupos ya registrados, leídos desde el csv si existe, o vacío si no.
    archivo_grupos : str
        Ruta del archivo csv de grupos (necesaria para guardar cambios luego).
    '''
    archivo_neutro = "archivos/archivo_e_n.xlsx"
    archivo_e_comentario1 = "archivos/archivo_e_post.xlsx"
    archivo_comentario = "archivos/archivo_comentario (1).xlsx"
    archivo_grupos = "grupos.csv"
    columnas = ["nombre", "situacion", "situacion_2", "indice", "respuesta_1", "respuesta_2"]

    try:
        df_neutro = pd.read_excel(archivo_neutro)
        df_neutro.columns = df_neutro.columns.str.strip()
        df_neutro[["estres", "motivacion", "tranquilidad"]] = df_neutro[["estres", "motivacion", "tranquilidad"]] * 100

        df_comentario = pd.read_excel(archivo_comentario)
        df_comentario.columns = df_comentario.columns.str.strip()
        df_comentario["parciales"] = df_comentario["parciales"].astype(str)
        df_comentario["no_parciales"] = df_comentario["no_parciales"].astype(str)

        df_motivacion = pd.read_excel(archivo_e_comentario1, sheet_name="Comentario_motivacional")
        df_motivacion.columns = df_motivacion.columns.str.strip()
        df_motivacion[["estres", "motivacion", "tranquilidad"]] = df_motivacion[["estres", "motivacion", "tranquilidad"]] * 100

        df_tranquilidad = pd.read_excel(archivo_e_comentario1, sheet_name="Comentario_tranquilidad")
        df_tranquilidad.columns = df_tranquilidad.columns.str.strip()
        df_tranquilidad[["estres", "motivacion", "tranquilidad"]] = df_tranquilidad[["estres", "motivacion", "tranquilidad"]] * 100

        df_estres = pd.read_excel(archivo_e_comentario1, sheet_name="Comentario_estres")
        df_estres.columns = df_estres.columns.str.strip()
        df_estres[["estres", "motivacion", "tranquilidad"]] = df_estres[["estres", "motivacion", "tranquilidad"]] * 100

        if os.path.exists(archivo_grupos):
            df_grupos = pd.read_csv(archivo_grupos)
        else:
            df_grupos = pd.DataFrame(columns=columnas)

        return df_neutro, df_comentario, df_motivacion, df_tranquilidad, df_estres, df_grupos, archivo_grupos

    except FileNotFoundError:
        print("El archivo no se encontro")
        raise