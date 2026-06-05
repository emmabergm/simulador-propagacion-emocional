def menu_2(): 
   '''
   Le da opciones al usuario de que devolucion quiere ver: 
   - Feedback de como influyen los comentarios 
   - Grafico neutro y grafico post que compare el cambio 
   - promedio grupal de emcoion a partir de cada comentario 

   Returns: 
   ----------
   str: opcion elegida 
   '''
   pass 

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
    pass

def grafico_neutro(menu_2, archivo_e_n): 
    '''
    Genera el grafico de emociones neutras 

    Parameters
    ----------
    menu_2 : str
        Si la opcion elegida es feedback, que se desarrolle la funcion 
    archivo_e_n : csv
        Archivo de emociones neutras para comparar con el otro archivo

    Returns
    -------
    plt: grafico 

    '''
    pass 

def grafico_e_post(menu_2, archivo_e_post): 
    '''
    Genera el grafico de emociones despues del comentario  

    Parameters
    ----------
    menu_2 : str
        Si la opcion elegida es feedback, que se desarrolle la funcion 
    archivo_e_post : csv
        Archivo de emociones post para comparar con el otro archivo

    Returns
    -------
    plt: grafico 

    '''
    pass 


def promedio_grupal(menu_2, archivo_e_post): 
    '''
    Sacar el promedio grupal de las emociones y devolver una valoracion grupal 

    Parameters
    ----------
    menu_2 : str
        Si la opcion elegida es feedback, que se desarrolle la funcion 
    archivo_e_post : csv
        Archivo de emociones despues de los comentarios.

    Returns
    -------
    float: promedio 

    '''
    pass