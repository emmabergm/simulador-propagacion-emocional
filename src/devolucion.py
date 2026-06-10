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
   1 = Feedback
   2 = Graficos
   3 = Promedio de emociones 
   print("1 - Feedback")
   print("2 - Graficos")
   print("3 - Promedio de emociones")
      
   while True: 
      try: 
         opcion = input("Ingrese la opcion deseada: ")
      
         if opcion != ("1", "2", "3"):
            raise ValueError ("La opcion ingresada no es valida")
 
      except ValueError:
         print("La opcion ingresada no es valida. Intente nuevamente.")
         
   return opcion 

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


