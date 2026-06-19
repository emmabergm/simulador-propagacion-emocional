import pandas as pd
import os

from src.comentario import situacion, numero_random, asociacion, guardar_respuesta
from src.Menus import menu_situacion, menu_com2, menu_parte2, menu_parte_3
from src.Partes import parte_1, parte_2, parte_2_comentario2
from src.carga_datos import cargar_datos

from src.carga_datos import cargar_datos

df_neutro, df_comentario, df_motivacion, df_tranquilidad, df_estres, df_grupos, archivo_grupos = cargar_datos()

nombre_grupo = input("Ingrese el nombre de su grupo: ")

if nombre_grupo in df_grupos["nombre"].values:
    fila = df_grupos[df_grupos["nombre"] == nombre_grupo].iloc[0]
    print(f"El grupo '{nombre_grupo}' ya existe.")
    opcion = input("¿Que deseas hacer? (1) Continuar como usuario 2  (2) Empezar de cero: ")

    if opcion == "1":
        tipo_situacion   = fila["situacion"]
        tipo_situacion_2 = fila["situacion_2"]
        indice           = int(fila["indice"])
        parte_1_sit1     = fila["respuesta_1"]
        parte_1_sit2     = fila["respuesta_2"]
        guardar_respuesta(parte_1_sit1, indice, df_comentario, tipo_situacion)
        guardar_respuesta(parte_1_sit2, indice, df_comentario, tipo_situacion_2)
        df_asociado_1 = asociacion(parte_1_sit1, df_tranquilidad, df_motivacion, df_estres)
        df_asociado_2 = asociacion(parte_1_sit2, df_tranquilidad, df_motivacion, df_estres)

    else:
        df_grupos = df_grupos[df_grupos["nombre"] != nombre_grupo]
        df_grupos.to_csv(archivo_grupos, index=False)
        while True:  # ← adentro del else
            nombre_grupo = input("Ingrese el nombre del nuevo grupo: ")
            if nombre_grupo in df_grupos["nombre"].values:
                print("Ese nombre ya existe, ingrese uno diferente")
                continue
            break

if nombre_grupo not in df_grupos["nombre"].values:
    tipo_situacion = situacion()
    indice = numero_random(df_comentario)
    parte_1_sit1 = parte_1(tipo_situacion, indice, df_comentario)
    df_asociado_1 = asociacion(parte_1_sit1, df_tranquilidad, df_motivacion, df_estres)

    menu_situacion(tipo_situacion)
    while True:
        tipo_situacion_2 = situacion()
        if tipo_situacion_2 == tipo_situacion:
            print("Debe ingresar una situacion diferente a la anterior")
            continue
        break
    parte_1_sit2 = parte_1(tipo_situacion_2, indice, df_comentario)
    df_asociado_2 = asociacion(parte_1_sit2, df_tranquilidad, df_motivacion, df_estres)

    df_grupos.loc[len(df_grupos)] = [nombre_grupo, tipo_situacion, tipo_situacion_2, indice, parte_1_sit1, parte_1_sit2]
    df_grupos.to_csv(archivo_grupos, index=False)


menu_2 = menu_parte2()
if menu_2 == "si":
    comentario_1, estudiante_2, edad_2 = parte_2(df_neutro, df_comentario, parte_1_sit1, indice, tipo_situacion, df_asociado_1)
    menu_com = menu_com2()
    if menu_com == "continuar":
        comentario_2 = parte_2_comentario2(df_comentario, parte_1_sit2, indice, tipo_situacion_2, df_asociado_2, estudiante_2, edad_2)
        menu_parte_3(df_neutro, df_asociado_1, df_asociado_2, tipo_situacion, tipo_situacion_2, df_comentario, parte_1_sit1, parte_1_sit2, indice, comentario_1)

