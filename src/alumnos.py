


def info_estudiante2 ():
    '''
    Le pregunta al estudiante por su informacion actual neutra 

    Parameters
    ----------
    estudiante_2 : str
        Nombre del estudiante dos que va a valorar sus emociones a partir de los comentarios 

    Returns
    -------
    valoracion neutra para cada emocion

    '''
    while True: 
        estres = int(input("Ingrese su estado de estres actual: "))
        motivacion = int(input("Ingrese su estado de motivacion actual: "))
        tranquilidad = int(input("Ingrese su estado de tranquilidad actual: "))
        
        if (0 > tranquilidad > 100) or (0 > estres > 100) or (0 > motivacion > 100): 
            raise ValueError("Los valores deben encontrarse dentro del rango (1 - 100) ")
        else: 
            break 
        
    return estres, motivacion, tranquilidad 

def guardar_archivo_neutro(estudiante_2, edad_e_2, funcion_info): 
    '''
    Agregar la informacion del estudiante_2 al archivo de emociones neutras 

    Parameters
    ----------
     estudiante_2 : str
        Nombre del estudiante dos que va a valorar sus emociones a partir de los comentarios 
     edad_e_2: int
         Edad del estudiante 2 
     funcion_info : int 
        La funcion va a retornar la edad en int y la valoracion por emocion en int tambien 

    Returns
    -------
    None.

    '''
    pass 

def valoracion_comentario(estudiante_2, edad_e_2, archivo_comentario, archivo_emociones): 
    '''
    Presentarle al estudiante_2 el comentario elegido por el estudiante_1 y preguntarle su valoracion
    (Van a presentarse 2 comentarios) (Validar datos)
    Parameters
    ----------
     estudiante_2 : str
        Nombre del estudiante dos que va a valorar sus emociones a partir de los comentarios 
     edad_e_2: int
         Edad del estudiante 2 
    archivo_comentario : cvs
        archivo que tiene guardado el comentario que eligio el estudiante_1
    archivo_emociones: cvs
        archivo en el que se va a guardar la valoracion que haga el estudiante_2 del coemntario 

    Returns
    -------
    None.

    '''
    pass
