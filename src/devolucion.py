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
   1 == "Feedback de los comentarios"
   2 == "Graficos de cambios de emociones"
   3 == "Promedio de las emociones" 
   print("===== MENÚ DE RESULTADOS =====")

   print("1 - Feedback personalizado")
   print("    Para obtener una devolución sobre cómo su comentario")
   print("    impactó en las emociones de sus compañeros según")
   print("    el contexto académico seleccionado.\n")

   print("2 - Visualización de emociones")
   print("    Para ver gráficos comparando las emociones antes")
   print("    y después del comentario realizado.\n")

   print("3 - Promedios emocionales")
   print("    Para ver los niveles promedio de estrés,")
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

   if not in partes:
      feedback = "El clima se mantuvo bastante estable despues del comentario"
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



########  
  print("2. Visualizar grafico","\n","Muestra los cambios emocionales generados a partir de los comentario (Esto va a incluir datos simulados)")
  print("3.Ver metricas", "\n", "muestra promedios grupales, cambios emocionales y feedback del comentario (Esto va a incluir datos simulados)",'\n')



elif accion == 2: 
    ver_grafico= grafico()
    return ver_grafico
    
elif accion == 3: 
    print("Promedios grupales: ", calcular_promedios_grupales(), "/n", 
          "Cambios de las emociones: ", comparar_promedios(), "/n", 
          "Feedback del comentario: ", feedback_comentario())



