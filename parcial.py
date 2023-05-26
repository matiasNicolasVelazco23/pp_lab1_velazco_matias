import re
import json

def leer_archivo (nombre_archivo : str) -> list:
    """
    Función que lee un json, carga el archivo y lo transforma a una lista de diccionarios

    Args:
        Recibe el nombre del archivo como string

    Returns:
        Retorna la lista, que contiene una lista de diccionarios
    """
    lista= []
    with open (nombre_archivo, "r") as archivo: 
        dict = json.load (archivo)
        lista = dict["jugadores"]
    return lista

def imprimir_dato(dato : str) -> None:
    """
       Recibe el dato para imprimirlo mediante print

    Args:
        dato (_type_): _description_
    """
    print(dato)

def imprimir_menu():

    menu = (
    "1. Mostrar la lista de todos los jugadores del Dream Team.\n"
    "2. Seleccionar un jugador por su índice y mostrar sus estadísticas"
    "completas\n"
    "3. Guardar las estadísticas de ese jugador en un archivo CSV.\n" 
    "4. Buscar un jugador por su nombre y mostrar sus logros\n"
    "5. Calcular y mostrar el promedio de puntos por partido de todo el equipo"
     " del Dream Team, ordenado por nombre de manera ascendente. \n"
    "7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.\n"
    "8- Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.\n"
    "9- Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.\n"
    "13- Calcular y mostrar el jugador con la mayor cantidad de robos totales.\n"
    "14- Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.\n"
    "19-Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas\n"
    
    )

    imprimir_dato(menu)

def opciones_menu_principal():
    """
    No recibe nada
    Se encarga de imprimir el menu de opciones y pedirle al usuario una opcion de entre todas
    validando la opcion y la retorna si da error retorna -1
    """
    imprimir_menu()
    opcion = input("Elija una opcion: ")
    print("")
    if re.search(r"[1-9]|1[1-9]|20|", opcion):
        return opcion
    else:
        return -1
#1--------------------------------------------------------------------------1
def mostrar_lista_jugadores(lista_jugadores:list, formato:bool)-> None:
    """
        En cada bucle del for accede  a cada diccionario individual 
        de los jugadores mediante el índice, toma el valor de las claves 
        nombre y  posición de dicho índice, para luego imprimirlo por pantalla
        con el formato indicado, agregué un espacio después del último índice.

    Args:
        lista_jugadores (list): el parámetro que recibe representa una lista 
        de diccionarios en cada diccionario de la lista hay estadisticas y 
        datos de cada jugador.
        formato (bool): el parámetro que recibe es un valor booleano, true o 
        false, si es true, agrega el índice a la izquierda, sino, agrega un str
        vacío.

    Returns:
        la función no retorna nada.
    """

    for indice in range(len(lista_jugadores)):
        if formato:
            decoracion = "{0}- ".format(indice)
            posicion_si_no = ""
        else:
            decoracion = ""
            posicion_si_no = " - {0}".format(lista_jugadores[indice]["posicion"])
        mensaje= ("{0}{1}{2}".format(decoracion, lista_jugadores[indice]["nombre"],
                                     posicion_si_no))
        print(mensaje)
    print("")

def es_entero(string)-> bool:
    """_summary_
        Funcion que verifica si el string es entero o no mediante RegEX
        Verifica si la expresión es verdadera o falsa, mediante re.search
        la expresión quiere decir, empieza con un número entero en un rango de 
        0 al 9, una o más ocurrencias, y termina con un número entero.
    Args:
        string (str): se envia un string por parámetro

    Returns:
        bool: la función devuelve un booleano, 
        true- si el string encaja con la expresión regular
        false- si en cambio el string no cumple con la expresión regular ingresada
        (ser entero)

    """
    if re.search(r"^[0-9]+$", string): 
        return True
    else:
        return False
    
def verificar_input(lista_jugadores:list) -> int:
    """
        Función que verifica si el indíce ingresado por el usuario es un número
        válido, las condiciones son que sea un número entero y además, que no
        supere el tamaño de la lista de diccionarios.

    Args:
        lista_jugadores (list): recibe el parámetro de la lista generada desde
        el json.

    Returns:
        int: Devuelve el índice ya validado.
    """
    print("Índices disponibles: ")
    mostrar_lista_jugadores(lista_jugadores, True)
    respuesta_valida = False
    while(respuesta_valida == False):
        ingreso_indice_texto= input("Ingrese índice a buscar: ")
        print("")

        if es_entero(ingreso_indice_texto):
            ingreso_indice_entero= int(ingreso_indice_texto)
            if ingreso_indice_entero >= len(lista_jugadores): # Acá tengo un problema, cuando pongo 12 me salta error
                print("Asegurate de no ingresar un índice que supere el tamaño de la lista, el tamaño es: {0} índices, del 0 al 11.\n"
                                                                     .format(len(lista_jugadores))
                     )
            else:
                respuesta_valida = True
        else:
            print("Asegurate de ingresar un número entero.\n")

    return ingreso_indice_entero

def iterar_estadisticas(lista_jugadores: list, indice_validado: int) -> str:
    """
    Función que itera sobre las estadísticas del jugador seleccionado por índice y construye un mensaje con los datos.

    Args:
        lista_jugadores (list): La lista de diccionarios de jugadores.
        indice_validado (int): El índice validado del jugador seleccionado.

    Returns:
        str: El mensaje con los datos del jugador en formato de string.
    """
    mensaje = ""
    for clave, valor in lista_jugadores[indice_validado]["estadisticas"].items():
        datos = "{0}: {1}\n".format(clave.capitalize().replace("_", " "), valor)
        mensaje += datos
    return mensaje
    
def selecciona_jugador_por_indice(lista_jugadores: list)-> dict:
    """_summary_
        Función que  selecciona un jugador mediante el índice ingresado,
        usa las funcionaes verificar_input y iterar_estadisticas
    Args:
        lista_jugadores (list): Recibe la lista de diccionarios de jugadores.

    Returns:
        Retorna el diccionario deL jugador seleccionado por índice
        y verificado previamente
    """
    indice_validado=verificar_input(lista_jugadores)

    mensaje=iterar_estadisticas(lista_jugadores, indice_validado)
    print(mensaje)  

    return indice_validado

#----------------------------------------------------------------------------
#3)
#----------------------------------------------------------------------------
def generar_csv_estadisticas_jugador(nombre_archivo: str, lista_jugadores: list, indice_seleccionado: int)-> None:
    """
       Función que genera un csv del jugador seleccionado en el punto 2, 
       primero itera  cada clave, en el índice seleccionado de la lista, luego
       verifica si la clave es "estadistica", esto no sucede hasta que llega a esa
       clave, escribe en el csv los valores de las claves "nombre" y "posición",
       hasta que llega a la clave estadísticas, allí, escribo en el csv utilizando
       el retorno de la función iterar estadisticas, finalmente, cuando termina
       de ejecutarse esa función realizo un break para que no siga escribiendo las claves restantes
       (el ejercico no lo pide)

    Args:
        nombre_archivo (str): nombre del archivo, el título está definido por el nombre del jugador
        lista_jugadores (list): lista de cada jugador con sus respectivos diccionarios
        indice_seleccionado (int): indice seleccionado en el ejercicio2
    
    Returns:
        La función no retorna nada
    """
    with open(nombre_archivo, "w") as archivo: 
            for clave, valor in lista_jugadores[indice_seleccionado].items():
                if clave == "estadisticas":
                    archivo.write(iterar_estadisticas(lista_jugadores, indice_seleccionado))
                    break
                mensaje = "{0}: {1}\n".format(clave.capitalize(),valor)
                archivo.write(mensaje)
    

#----------------------------------------------------------------------------
# 4)Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, 
# como campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón
# de la Fama del Baloncesto, etc, 
#---------------------------------------------------------------------------
# 5)Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team,
#  ordenado por nombre de manera ascendente. 

def calcular_y_mostrar_dato(lista_jugadores:list,dato:str):
    lista_jugadores_maximos= []
    for indice in range(len(lista_jugadores)):
        if indice == 0 or lista_jugadores[indice]["estadisticas"][dato] > maximo:
            maximo = lista_jugadores[indice]["estadisticas"][dato]
    
    for indice in range(len(lista_jugadores)):
        if lista_jugadores[indice]["estadisticas"][dato] == maximo:
            lista_jugadores_maximos.append(lista_jugadores[indice]["nombre"])

    if len(lista_jugadores_maximos) == 1:
        cadena_maximos = lista_jugadores_maximos[0]
    elif len(lista_jugadores_maximos) == 2:
        texto = " y "
        cadena_maximos=texto.join(lista_jugadores_maximos)
    else:
        texto = ","
        palabras_con_coma= texto.join(lista_jugadores_maximos[0:-1])
        cadena_maximos = "{0} y {1}".format(palabras_con_coma,lista_jugadores_maximos[-1])
    continue



            

    print("El jugador con el máximo de '{0}' es {1} con un total de {2}\n".format(dato.replace("_", " "),cadena_maximos,maximo))

def menu_de_opciones(lista_jugadores:list):
    flag_se_selecciono = False
    while True:
            opcion = opciones_menu_principal()
            if opcion == "1":
                mostrar_lista_jugadores(lista_jugadores, False) 
            elif opcion == "2":
                indice_seleccionado=selecciona_jugador_por_indice(lista_jugadores)
                flag_se_selecciono = True
            elif opcion == "3":
                if flag_se_selecciono == True:
                    nombre_archivo = "jugador_estadisticas_completas_{0}.csv".format(lista_jugadores[indice_seleccionado]["nombre"].replace(" ","_"))
                    generar_csv_estadisticas_jugador(nombre_archivo, lista_jugadores, indice_seleccionado)
                else:
                    print("Aún no seleccionaste un índice, vuelve a intentarlo.\n")
            elif opcion == "4":
                    busca_y_mostrar(lista_jugadores)
            elif opcion == "5":
                calcular_y_mostrar_dato(lista_jugadores, "promedio_puntos_por_partido")
                pass
            elif opcion == "6":
                pass
            elif opcion == "7":
                calcular_y_mostrar_dato(lista_jugadores, "rebotes_totales")
                pass
            elif opcion == "8":
                calcular_y_mostrar_dato(lista_jugadores, "porcentaje_tiros_de_campo")
                pass
            elif opcion == "9":
                calcular_y_mostrar_dato(lista_jugadores, "asistencias_totales")
                pass
            elif opcion == "10":
                pass
            elif opcion == "11":
                pass
            elif opcion == "12":
                pass
            elif opcion == "13":
                calcular_y_mostrar_dato(lista_jugadores, "robos_totales")
                pass
            elif opcion == "14":
                calcular_y_mostrar_dato(lista_jugadores, "bloqueos_totales")
                pass
            elif opcion == "15":
                pass
            elif opcion == "16":
                calcular_y_mostrar_dato(lista_jugadores, "promedio_puntos")
                pass
            elif opcion == "17":
                calcular_y_mostrar_dato(lista_jugadores, "logros")
                pass
            elif opcion == "18":
                pass
            elif opcion == "19":
                calcular_y_mostrar_dato(lista_jugadores, "temporadas")
                pass
            elif opcion == "20":
                pass
            
            else:
                print("Opcion inválida")


lista_jugadores = leer_archivo("dt.json")

menu_de_opciones(lista_jugadores)
