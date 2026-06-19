from src.analisis import calcualar_promedios_grupales
from src.analisis import comparar_promedios
from src.analisis import feedback_comentario 
from src.graficos import grafico
from src.Partes import parte_2
from src.Partes import parte_2_comentario2
from src.graficos import graficar_comparacion_emociones


def menu_grupos(df_grupos, nombre_grupo):
    """
    Busca un grupo por nombre y devuelve la situación asociada.

    Parametros
    ----------
    df_grupos: pandas.DataFrame
        DataFrame que contiene los nombres de los grupos y las situaciones asociadas.
    nombre_grupo : str
        Nombre del grupo seleccionado por el usuario.

    Returns
    -------
    str
        Situación correspondiente al grupo seleccionado ("parciales" o "no parciales")
    """
    if nombre_grupo in df_grupos["nombre"].values: 
        fila = df_grupos[df_grupos["nombre"] == nombre_grupo].iloc[0]
        return fila["situacion"]
            

def menu_situacion(tipo_situacion): 
    """
    Solicita al usuario una confirmacion para continuar con la segunda situacion del programa.

    Parameters
    -----------
    tipo_situacion: str
        Situacion seleccionada previamente por el usuario.

    Returns
    -------
    str
        La confirmacion ingresada por el usuario para continuar con el programa
    """
    print("\nAhora vamos a explorar como reaccionaria tu grupo ante la misma situacion pero en un contexto diferente.")
    print("Si antes elegiste 'parciales', ahora pensá en 'no parciales', y viceversa.\n")
    
    while True:
            confirmacion = input("\nEscriba 'continuar' para seguir: ").strip().lower()
            if confirmacion != "continuar":
                print("Debe escribir 'continuar' para seguir.")
                continue
            return confirmacion

def menu_parte2(): 
    """
    Consulta al usuario si desea seguir con la segunda parte del programa.

    Returns
    -------
    str 
        Devuelve "si" si el usuario desea continuar con la segunda parte.
        Devuelve "no" si el usuario decide finalizar con el programa
    """
    print("\nEn la siguiente parte del programa, debe ser realizada por otro usuario. La idea es que juegue el rol desde la persona que recibe esos comentarios y los valore con sus emociones.")
    while True: 
        eleccion = input("\nDesea seguir con la parte 2? (si/no): ").strip().lower()
        if eleccion == "si": 
            return eleccion
        elif eleccion == "no": 
            print("\nMuchas gracias por las respuestas!")
            return eleccion
        else:
            print("Debe responder con si o con no.")

def menu_com2(): 
    """
    Le solicita al usuario una confirmacion para continuar con la evaluacion del segundo comentario.

    Returns
    -------
    str
        La confirmacion ingresada por el usuario para continuar con el programa
    """
    
    print("\nAhora vamos a evaluar como te impacta un comentario diferente ante la misma situacion.")
    while True: 
        seguir = input("\nIngrese continuar para evaluar el siguiente comentario: ").strip().lower()
        if seguir != "continuar":
            print("Debe escribir 'continuar' para seguir.")
        else: 
            return seguir

def menu_parte_3(df_neutro, df_asociado_1, df_asociado_2, tipo_situacion,tipo_situacion_2, df_comentario, parte_1_sit1, parte_1_sit2, indice, comentario):
    '''
    Parameters
    ----------
    df_neutro: DataFrame
        DataFrame que contiene las valoraciones emocionales iniciales de los participantes
    df_asociado_1: DataFrame
        DataFrame que contiene las valoraciones emocionales luego del primer comentario
    df_asociado_2: DataFrame
        DataFrame que contiene las valoraciones emocionales luego del segundo comentario
    tipo_situacion: str
        Situacion academica del usuario ("parciales" o "no parciales")
    tipo_situacion2: str
        Segunda situacion academica del usuario ("parciales" o "no parciales"), utilizada para comparar los resultados obtenidos anteriormente en la otra situacion
    df_comentario: DataFrame
        DataFrame que contiene los comentarios asociados a cada situacion
    parte_1_sit1: DataFrame
        Datos correspondientes a la primera situacion elegida para agregar nuevos registros
    parte_1_sit2: DataFrame
        Datos correspondientes a la segunda situacion elegida para agregar nuevos registros
    indice : int
        Numero random elegido por el programa correspondiente a la opcion a elegir de las respuestas
    comentario : str
        Comentario evaluado por el participante

    Returns
    -------
    None.
    
    '''
    while True:
        print("1. Agregar otro estudiante.\n"
              "Permite cargar el estado emocional inicial, presentar una situacion y valorar el comentario\n"
              "2. Quiere ver las metricas del experimento (Estas van a incluir datos simulados).\n"
              "3. Terminar el programa\n")
        
        accion = input("\nQue quiere realizar? : ")
    

        if accion == "1":
            comentario_1, estudiante_2, edad_2 = parte_2(df_neutro, df_comentario, parte_1_sit1, indice, tipo_situacion, df_asociado_1)
            comentario_2 = parte_2_comentario2(df_comentario, parte_1_sit2, indice, tipo_situacion_2, df_asociado_2, estudiante_2, edad_2)
        elif accion == "2":
            menu_metricas(df_neutro, df_asociado_1, df_asociado_2, tipo_situacion, tipo_situacion_2, comentario)
        elif accion == "3":
            print("Muchas gracias por participar! ")
            return None
        else:
            print("Opcion invalida")
      
def menu_metricas(df_neutro, df_asociado_1, df_asociado_2, tipo_situacion, tipo_situacion_2, comentario):                     
    """
    Visualiza las distintas metricas obtenidas durante el programa, como los promedios grupales, cambios emocionales, feedback de los comentarios y graficos comparativos.

    Parameters
    ----------
    df_neutro: DataFrame
        DataFrame que contiene las valoraciones emocionales iniciales de los participantes
    df_asociado_1: DataFrame
        DataFrame que contiene las valoraciones emocionales luego del primer comentario
    df_asociado_2: DataFrame
        DataFrame que contiene las valoraciones emocionales luego del segundo comentario
    tipo_situacion: str
        Situacion academica del usuario ("parciales" o "no parciales")
    tipo_situacion2: str
        Segunda situacion academica del usuario ("parciales" o "no parciales"), utilizada para comparar los resultados obtenidos anteriormente en la otra situacion
    comentario : str
        Comentario evaluado por el participante

    Returns
    -------
    None
        Solamente muestra las metricas seleccionadas por los usuarios.
    """
    promedio_neutro = calcualar_promedios_grupales(df_neutro)
    promedio_comentario1 = calcualar_promedios_grupales(df_asociado_1)
    promedio_comentario2 = calcualar_promedios_grupales(df_asociado_2)

    cambio_estres1, cambio_motivacion1, cambio_tranquilidad1 = comparar_promedios(promedio_neutro, promedio_comentario1) 
    cambio_estres2, cambio_motivacion2, cambio_tranquilidad2 = comparar_promedios(promedio_neutro, promedio_comentario2)

    feedback1 = feedback_comentario(tipo_situacion, comentario, cambio_estres1, cambio_motivacion1, cambio_tranquilidad1)
    feedback2 = feedback_comentario(tipo_situacion_2, comentario, cambio_estres2, cambio_motivacion2, cambio_tranquilidad2)

    while True: 
        print("1. Promedios grupales.\n", 
              "2. Cambios de las emociones.\n", 
              "3. Feedback del comentario.\n",
              "4. Grafico que compara las emociones neutras y despues de cada comentario.\n "
              "5. Histogramas de cada emocion para evaluar el imapcto de cada comentario.\n",
              "6. Volver al menu principal")
        
        eleccion = input("\nQue metrica desea ver? (elija una opcion, luego puede ingresar otra):  ")
        

        if eleccion == "1": 
            print("\nEl promedio de las emociones al inciar, es decir las neutras es: ") 
            print(promedio_neutro)
            print("\nEl promedio por emocion luego del primer comentario es el siguiente: ")
            print(promedio_comentario1)
            print("\nPor ultimo el promedio por emocion luego del segundo comentario es el siguiente: ")
            print(promedio_comentario2)
        elif eleccion == "2":   
            print("\nLos cambios emcoionales entre la valoracion neutra y luego del primer comentario son los siguientes: ", "\n",
                  "Cambio estres: ", cambio_estres1, "\n",
                  "Cambio motivacion", cambio_motivacion1, "\n", 
                  "Cambio tranquilidad", cambio_tranquilidad1, "\n",
                  "Los cambios emcoionales entre la valoracion neutra y luego del segundo comentario son los siguientes:", "\n",  
                  "Cambio estres: ", cambio_estres2, "\n", 
                  "Cambio motivacion", cambio_motivacion2, "\n",
                  "Cambio tranquilidad", cambio_tranquilidad2)
            
        elif eleccion == "3": 
            print("\nEl feedback leugo del comentario 1 es: ", feedback1, "\n", 
                  "El feedback luego del comentario 2 es: ", feedback2)
        elif eleccion == "4": 
            grafico(df_neutro, df_asociado_1, df_asociado_2)
            
        elif eleccion == "5":
            while True:
                print("\n1. Estres\n",
                      "2. Motivacion\n",
                      "3. Tranquilidad")
                emocion_elegida = input("\nQue emocion desea ver?: ").strip()

                if emocion_elegida == "1":
                    graficar_comparacion_emociones(df_asociado_1, df_asociado_2, "estres")
                    break
                elif emocion_elegida == "2":
                    graficar_comparacion_emociones(df_asociado_1, df_asociado_2, "motivacion")
                    break
                elif emocion_elegida == "3":
                    graficar_comparacion_emociones(df_asociado_1, df_asociado_2, "tranquilidad")
                    break
                else:
                    print("Opcion invalida. Debe elegir 1, 2 o 3.")
            
        elif eleccion == "6": 
            break
        
         
        else:
            print("La opción es inválida")
                        
                        
