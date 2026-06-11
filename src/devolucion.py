def menu_2(): 
   '''
   Le da opciones al usuario de que devolucion quiere ver: 
   - Feedback de como influyen los comentarios 
   - Grafico neutro y grafico post que compare el cambio 
   - promedio grupal de emocion a partir de cada comentario 
   
   Raises
   ValueError: si la opcion que elige ver no es valida.

   Returns: 
   ----------
   str: opcion elegida 
   '''
   1 == "Feedback"
   2 == "Graficos"
   3 == "Promedio de emociones" 
   print("===== MENÚ DE RESULTADOS =====")

   print("1 - Feedback personalizado")
   print("    Obtenga una devolución sobre cómo su comentario")
   print("    impactó en las emociones de sus compañeros según")
   print("    el contexto académico seleccionado.\n")

   print("2 - Visualización de emociones")
   print("    Observe gráficos comparando las emociones antes")
   print("    y después del comentario realizado.\n")

   print("3 - Promedios emocionales")
   print("    Consulte los niveles promedio de estrés,")
   print("    motivación y tranquilidad del grupo.\n")

   
   
   while True:
    try:
        opcion = input("Ingrese la opción deseada: ")

        if opcion != 1 or opcion != 2 or opcion != 3:
            raise ValueError("La opción ingresada no es válida")

        return opcion

    except ValueError:
        print("La opción ingresada no es válida. Intente nuevamente.")
    
         

def feedback_emociones(menu_2, archivo_e_n, archivo_e_post): 
    '''
    Funcion que devuelve un feedback a partir de lo que sucedio con las emociones 

    Parameters
    ----------
    menu_2 : str
        Si la opcion elegida es feedback, que se desarrolle la funcion 
    archivo_e_n : csv 
        Archivo de emociones neutras para comparar con el otro archivo
    archivo_e_post : csv
        Archivo de emociones despues de los comentarios. 

    Returns
    -------
    str: feedback 

    '''
    1 = Feedback 
    if menu_2 == 1
   

