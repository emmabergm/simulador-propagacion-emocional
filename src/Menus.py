from src.analisis import calcualar_promedios_grupales
from src.analisis import comparar_promedios
from src.analisis import feedback_comentario 
from src.graficos import grafico
from src.Partes import parte_2

dicc_cargados = {}

def menu_inicio(nombre, situacion): 
    '''
    Agrega los nombres a una lista, para guardar los datos de los usuarios que ingresan 

    Parameters
    ----------
    nombre : str
        Nombre de un grupo experimental
    situacion : str
        Situacion en la que se encuentra el usuario (parcial/no parcial)

    Raises
    ------
    ValueError
        Se produce si la respuesta ingresada por el usuario no es "si" ni "no"
        
    Returns
    -------
    str
       La respuesta ingresada por el usuario, y "si" cuando se crea un nuevo registro

    '''
    
    

    if dicc_cargados=={}: 
        dicc_cargados[situacion]=nombre
        return "si"
        

    if situacion not in dicc_cargados:
        dicc_cargados[situacion] = nombre
        return "no"  

    
    elif dicc_cargados[situacion] == nombre:
        while True:
            eleccion = input("Desea continuar con la información ya cargada? (si/no): ").lower()
            return eleccion
            break
            
            if (eleccion != "si") or (eleccion != "no"): 
                raise ValueError ("Debe responder con si o con no")
    
            
#
   
def menu_parte2(): 
    """
    Consulta al usuario si desea seguir con la segunda parte del programa.

    Raises
    ------
    ValueError
        Se produce cuando la respuesta ingresada no es "si" ni "no"

    Returns
    -------
    str : eleccion 
        Devuelve "si" si el usuario desea continuar con la segunda parte.
        Devuelve "no" si el usuario decide finalizar con el programa
    """
     
    eleccion=input("Desea seguir con la parte 2? (si/no): ").lower()
    
    while True: 
            if eleccion=="si": 
                return eleccion
            
            elif eleccion=="no": 
                print("Muchas gracias por las respuesta!")
                break
            elif (eleccion != "si") or (eleccion != "no"): 
                   raise ValueError ("Debe responder con si o con no")
                   
            return eleccion     


def menu_parte_3(df_neutro, df_asociado_1, df_asociado_2, situacion, df_comentario, parte_1_sit1, parte_1_sit2, indice, comentario):
    '''
    Parameters
    ----------
    df_neutro : pandas.DataFrame
       DataFrame que contiene las valoraciones emocionales iniciales de los participantes
    df_asociado_1: pandas.DataFrame
       DataFrame que contiene las valoraciones emocionales luego del primer comentario
    df_asociado_2: pandas.DataFrame
       DataFrame que contiene las valoraciones emocionales luego del segundo comentario
    situacion : str
        Situacion seleccionada por el participante durante el programa
    df.comentario : pandas.DataFrame
        DataFrame que contiene los comentarios asociados a cada situacion
    parte_1_sit1 : pandas.DataFrame
        Datos correspondientes a la primera situacion elegida para agregar nuevos registros
    parte_1_sit2 : pandas.DataFrame
        Datos correspondientes a la segunda situacion elegida para agregar nuevos registros
    indice : int
        Indice de la situacion o comentario seleccionado
    Comentario : str
        Comentario evaluado por el participabnte
        
    Raises
    ------
    ValueError
        Si el usuario ingresa una opción no válida en alguno de los
        menús interactivos.

    Returns
    -------
    None.
    
    '''

    while True:
            continuar=input("Desea continuar con el programa? (si/no)").lower()
            
            if (continuar != "si") and (continuar != "no"):
                raise ValueError("Debe ingresar si/no")
                
            if continuar=="no": 
                print("Gracias por participar")
                break
            
            elif continuar=="si":
               
               print("1. Agregar otro estudiante.","\n", "Permite cargar el estado emocional inicial, presentar una situacion y valorar el comentario",'\n')
               print("2. Quiere ver las metricas del experimento (Estas van a incluir datos simulados)")
               
               accion = int(input("Que quiere realizar? : "))
               break

        
                
    promedio_neutro = calcualar_promedios_grupales(df_neutro)
    promedio_comentario1 = calcualar_promedios_grupales(df_asociado_1)
    promedio_comentario2 = calcualar_promedios_grupales(df_asociado_2)
                
    cambio_estres1, cambio_motivacion1, cambio_tranquilidad1 = comparar_promedios(promedio_neutro, promedio_comentario1) 
    cambio_estres2, cambio_motivacion2, cambio_tranquilidad2 = comparar_promedios(promedio_neutro, promedio_comentario2)
                
    feedback1 = feedback_comentario(situacion, comentario, cambio_estres1, cambio_motivacion1, cambio_tranquilidad1)
    feedback2 = feedback_comentario(situacion, comentario, cambio_estres2, cambio_motivacion2, cambio_tranquilidad2)
    
    if accion == 1:
        agrego_estudiante = parte_2(df_neutro, df_comentario, parte_1_sit1, indice, situacion, df_asociado_1) #COMO LE PASAMOS LA SITUACION?????
        agrego_estudiante_s2 = parte_2(df_neutro, df_comentario, parte_1_sit2, indice, situacion, df_asociado_2)
                    

    elif accion == 2:
        print("1. Promedios grupales. ",  "/n", 
              "2. Cambios de las emociones. ","/n", 
              "3. Feedback del comentario. ", "/n",
              "4. Grafico que compara las emociones neutras y despues de cada comentario. ")
               
    while True: 
        eleccion = int(input("Que metrica desea ver? (elija una opcion, luego puede ingresar otra):  "))
            
        if eleccion == 1: 
                         
            print("El promedio de las emociones al inciar, es decir las neutras es: ", promedio_neutro, "\n"
                  "El promedio por emocion luego del primer comentario es el siguiente: ", promedio_comentario1, "\n",
                  "Por ultimo el promedio por emocion luego del segundo comentario es el siguiente: ", promedio_comentario2)
            break
                        
        elif eleccion == 2:   
                         
            print("Los cambios emcoionales entre la valoracion neutra y luego del primer comentario son los siguientes: " ,"\n",
                  "Cambio estres: " , cambio_estres1,"\n",
                  "Cambio motivacion" , cambio_motivacion1, "\n", 
                  "Cambio tranquilidad" , cambio_tranquilidad1, "\n",
                  "Los cambios emcoionales entre la valoracion neutra y luego del segundo comentario son los siguientes:" , "\n",  
                  "Cambio estres: " , cambio_estres2,"\n", 
                  "Cambio motivacion" , cambio_motivacion2, "\n",
                  "Cambio tranquilidad" , cambio_tranquilidad2)
            break
                     
        elif eleccion == 3: 
            print("El feedback leugo del comentario 1 es: " , feedback1,"\n", 
                  "El feedback luego del comentario 2 es: " , feedback2)
            break 
                    
        elif eleccion == 4: 
            ver_grafico = grafico(df_neutro, df_asociado_1, df_asociado_2) #CHEQUEAR SI HAY QUE RENEAR PARA QUE SE VEA
            return ver_grafico
            break
                    
        else:
            raise ValueError("La opción es inválida")


                    
                            

    
            
        
            
        
        
    
                    
               
                   
       
        

    
    
    
            
        
        
        
       
        
    
    

            
