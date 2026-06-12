


         

def feedback_emociones(cambio_estres, cambio_tranquilidad, cambio_motivacion): 

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
    cambios = []
    
    if cambio_estres > 1:
       cambios.append ("El estres del grupo aumento,")
    elif cambio_estres < -1:
       cambios.append ("El estres del grupo bajo, lo cual es positivo,")

    if cambio_motivacion > 1:
       cambios.append ("la motivacion mejoro,")
    elif cambio_motivacion < -1:
       cambios.append ("la motivacion cayo,")

    if cambio_tranquilidad > 1:
       cambios.append ("el grupo se encuentra mas tranquilo.")
    elif cambio_tranquilidad < -1:
       cambios.append ("la tranquilidad disminuyo.")

    if cambios==[]:
       feedback = ("El clima se mantuvo bastante estable despues del comentario")
    else: 
       feedback = (f"Despues del comentario, {cambios}")

    return feedback
    print (feedback)

 #si queremos que diga cual emocion cambio mas
     
    if cambio_estres>=0:
        cambio_estres_positivo = cambio_estres
    else:
        cambio_estres_positivo = cambio_estres * -1

    if cambio_motivacion>=0:
        cambio_motivacion_positivo = cambio_motivacion
    else:
        cambio_motivacion_positivo = cambio_motivacion * -1

    if cambio_tranquilidad>=0:
        cambio_tranquilidad_positivo = cambio_tranquilidad
    else:
        cambio_tranquilidad_positivo = cambio_tranquilidad * -1


    if cambio_estres_positivo >= cambio_motivacion_positivo and cambio_estres_positivo >= cambio_tranquilidad_positivo:
         emocion_predominante = "Cuidado con lo que decis! Ahora el estado emocional que predomina en el grupo es el estres!"
    elif cambio_motivacion_positivo >= cambio_estres_positivo and cambio_motivacion_positivo >= cambio_tranquilidad_positivo:
         emocion_predominante = "Buenisimo el comentario! La motivacion esta predominando en el estado emocional del grupo"
    else:
         emocion_predominante = "Tu mensaje genero tranquilidad en el grupo!"


    print (feedback)
    print (emocion_predominante)
 
 
  



    


