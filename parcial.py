import re
import json
import os

def clear_console() -> None:
    """
    Esta función borra la pantalla de la consola en Python esperando la entrada del usuario y luego
    llamando al comando 'cls' para borrar la pantalla.
    """
    _ = input('Presiona cualquier tecla para continuar.')
    os.system('cls')


def leer_archivo (nombre_archivo : str) -> list:
    """
    Función que lee un json, carga el archivo y lo transforma a una lista de diccionarios

    Args:
        Recibe el nombre del archivo como string

    Returns:
        Retorna la lista, que contiene una lista de diccionarios
    """
    lista= []
    with open (nombre_archivo, "r", encoding ='utf-8') as archivo:  #UTF-8 para que permita caracteres especiales
        dict = json.load (archivo)
        lista = dict["jugadores"]
    return lista

def imprimir_dato(dato : str) -> None:
    """
       Recibe el dato para imprimirlo mediante print

    Args:
        dato (str): dato especificado
    """
    print(dato)

def imprimir_menu():
    """
    Función que imprime el menú, todo el texto es guardado en la variable menú.

    No devuelve nada
    """
    menu = (
    "1. Mostrar la lista de todos los jugadores del Dream Team.\n"
    "2. Seleccionar un jugador por su índice y mostrar sus estadísticas"
    "completas\n"
    "3. Guardar las estadísticas de ese jugador en un archivo CSV.\n" 
    "4. Buscar un jugador por su nombre y mostrar sus logros.\n"
    "5. Calcular y mostrar el promedio de puntos por partido de todo el equipo ordenado por nombre de manera ascendente.\n"
    "6. Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.\n"
    "7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.\n"
    "8- Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.\n"
    "9- Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.\n"
    "10- Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.\n"
    "11- Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.\n"
    "12- Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.\n"
    "13- Calcular y mostrar el jugador con la mayor cantidad de robos totales.\n"
    "14- Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.\n"
    "15- Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.\n"
    "16- Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.\n"
    "17- Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos\n"
    "18- Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.\n"
    "19- Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas\n"
    "20- Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.\n"
    "23- Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.\n"
    "24- Determinar la cantidad de jugadores que hay por cada posición.\n"
    "25- Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente.\n"
    "26- Determinar qué jugador tiene las mejores estadísticas en cada valor.\n"
    "27- Determinar qué jugador tiene las mejores estadísticas de todos.\n"

    
    )

    imprimir_dato(menu)

def opciones_menu_principal():
    """
    No recibe nada
    Se encarga de imprimir el menu de opciones y pedirle al usuario una opcion de entre todas
    validando la opcion  mediante RegEx y la retorna, si da error retorna -1.
    """
    imprimir_menu()
    opcion = input("Elija una opcion: ")
    print("")
    if re.match(r"[1-9]|1[1-9]|20|23|24|25|26|27", opcion): #*
        return opcion
    else:
        return -1
#1--------------------------------------------------------------------------1
#1 - 2
def mostrar_lista_jugadores(lista_jugadores:list, formato:bool)-> None:
    """
        En cada bucle del for accede  a cada diccionario individual 
        de los jugadores mediante el índice, toma el valor de las claves 
        nombre y  posición de dicho índice, para luego imprimirlo por pantalla
        con el formato indicado necesario (punto 1 y 2)

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

def es_entero(string)-> bool:
    """_summary_
        Funcion que verifica si el string es entero o no mediante RegEX
        Verifica si la expresión es verdadera o falsa, utilizando re.search
        la expresión quiere decir.. "empieza con un número entero en un rango de 
        0 al 9, una o más ocurrencias, y termina con un número entero".
    Args:
        string (str): se envia un string por parámetro

    Returns:
        bool: la función devuelve un booleano, 
        true- si el string encaja con la expresión regular
        false- si en cambio el string no cumple con la expresión regular ingresada
        (ser entero)

    """
    if re.search(r"^[0-9]+$", string):  #*
        return True
    else:
        return False
    
def es_flotante(string:str)->bool:
    """Función que verifica si el string es un número flotante válido mediante RegEx.
        le doy la opción al usuario de que ponga , o ., pero después lo formateo en la 
        función donde llamo a esta función.
    
    Args:
        string (str): string a verificar.
    
    Returns:
        bool: True si la cadena es un número flotante válido, False en caso contrario.
    """
    if re.match(r"(^[0-9]+)(\.|\,)([0-9]+$)", string):
        return True
    else:
        return False
    
def es_texto(string):
    """
       Función que verifica si el string es un texto, devuelve, admite
       mayúsculas y minúculas, una o más ocurrencias.

    Args:
        string (str): stringa verificar

    Returns:
        bool: True si la cadena es string válido, False en caso contrario.
    """
    if re.match(r"(^[a-zA-Z ]+$)", string):
        return True
    else:
        return False
    
def es_miembro_salon(logros:str)-> bool:
    """
        Función que revisa si la cadena ingresada contiene exactamente la expresión
        "Miembro del Salon de la Fama del Baloncesto".
    Args:
        logros (str): texto a evaluar

    Returns:
        bool: retorna true si encuentra el patrón y false si no lo hace.
    """
    patron = r'\bMiembro del Salon de la Fama del Baloncesto\b'
    if re.search(patron, logros):
        return True
    else:
        return False
    
def hay_coincidencia_inexacta(nombre_ingresado:str, lista_jugadores:list)->list:
    """
       Función que verifica si hay ocurrencias con el nombre de algún jugador 
       de la lista

    Args:
        nombre_ingresado (str): nombre ingresado, validado previamente
        lista_jugadores (list): lista de los jugadores, con sus claves

    Returns:
        list: Retorna una lista, que incluye los valores de nombres, seguidos de sus logros, 
        en pares de a 2 Ej[Nombre,logros,nombre,logros...].
    """
    patron = r'.*{0}.*'.format(nombre_ingresado.lower())
    jugadores_coincidentes = []
    for jugador in lista_jugadores:
        nombre_jugador = jugador["nombre"].lower()
        if re.search(patron, nombre_jugador):
            jugadores_coincidentes.append(jugador["nombre"])
            jugadores_coincidentes.append(jugador["logros"])
    return jugadores_coincidentes
    
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
            if ingreso_indice_entero >= len(lista_jugadores): 
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

#----------------------------------------------------------------------------  
def selecciona_jugador_por_indice(lista_jugadores: list)-> int:
    """_summary_
        Función que  selecciona un jugador mediante el índice ingresado,
        usa las funcionaes verificar_input y iterar_estadisticas
    Args:
        lista_jugadores (list): Recibe la lista de diccionarios de jugadores.

    Returns:
        int: Retorna el número del índice seleccionado, para usar luego.
    """
    indice_validado=verificar_input(lista_jugadores)

    mensaje=iterar_estadisticas(lista_jugadores, indice_validado)
    print(mensaje)  

    return indice_validado

#----------------------------------------------------------------------------
#3
def generar_csv_estadisticas_jugador(nombre_archivo: str, lista_jugadores: list, indice_seleccionado: int)-> None:
    """
       Función que genera un csv del jugador seleccionado en el punto 2, 
       primero itera  cada clave, en el índice seleccionado de la lista, luego
       verifica si la clave es "estadistica", esto no sucede hasta que llega a esa
       clave, escribe en el csv los valores de las claves "nombre" y "posición",
       cuando llega al punto mencionado, escribe los nombre de las claves dentro de estadísticas
       en la siguiente estructura repetitiva, hacemos el mismo proceso pero accediendo a las claves
       mediante los elementos que iteramos.

    Args:
        nombre_archivo (str): nombre del archivo, el título está definido por el nombre del jugador
        lista_jugadores (list): lista de cada jugador con sus respectivos diccionarios
        indice_seleccionado (int): indice seleccionado en el ejercicio2
    
    Returns:
        La función no retorna nada
    """
    with open(nombre_archivo, "w") as archivo:
        lista_de_claves = []
        lista_de_valores = []
        for clave in lista_jugadores[indice_seleccionado]:
            if clave != "estadisticas":
                mensaje = "{0}".format(clave)
                lista_de_claves.append(mensaje)
            else:
                for clave_estadisticas in lista_jugadores[indice_seleccionado]["estadisticas"]:
                    mensaje_estadisticas = "{0}".format(clave_estadisticas)
                    lista_de_claves.append(mensaje_estadisticas)
        separador = ","
        separado_con_coma_claves= separador.join(lista_de_claves[:-1])
        claves=separado_con_coma_claves


        for clave in lista_jugadores[indice_seleccionado]:
            if clave != "estadisticas":
                valor = str(lista_jugadores[indice_seleccionado][clave])
                lista_de_valores.append(valor)
            else:
                for clave_estadisticas in lista_jugadores[indice_seleccionado]["estadisticas"]:
                    valor_estadisticas = str(lista_jugadores[indice_seleccionado]["estadisticas"][clave_estadisticas])
                    lista_de_valores.append(valor_estadisticas)
        separador = ","
        separado_con_coma_valores = separador.join(lista_de_valores[:-1])
        valores=separado_con_coma_valores

        archivo.write("{0}\n{1}".format(claves,valores))

                
            
def quick_sort(lista_original:list, flag_orden:bool) -> list:
    """
        Función que ordena generando sublistas, separándola de izquierda y derecha
        según si es mayor o menor al pivot, el pivot va cambiando dependiendo la lista
        que llega en la recursividad, los elementos y el tamaño de las listas también
        hasta que queda una lista igual a 1 (también contempla el caso en el que llegue)
        una lista vacía, finalmente ordena según la especificación pasada por booleano.
    Args:
        lista_original (list): listas generadas en las funciones, en los casos de ordenar.
        flag_orden (bool): valor que detalla si el orden es ascendente o descendente

    Returns:
        list: retorna la lista izquierda o la derecha, dependiendo del orden seleccionado
    """
    lista_de = []  # Lista para almacenar los elementos mayores al pivote
    lista_iz = []  # Lista para almacenar los elementos menores o iguales al pivote

    if len(lista_original) <= 1:
        return lista_original  # Si la lista tiene 0 o 1 elemento, ya está ordenada
    else:
  
        pivot = lista_original[0]  # Selecciona el primer elemento como pivote


        for elemento in lista_original[1:]:
            if elemento > pivot:

                lista_de.append(elemento)  # Agrega elementos mayores al pivote a lista_de

            else:
                lista_iz.append(elemento)  # Agrega elementos menores o iguales al pivote a lista_iz

    if flag_orden:  
        lista_iz = quick_sort(lista_iz, True)  # Ordena recursivamente la lista izquierda

        lista_iz.append(pivot)  # Agrega el pivote a lista_iz
        
        lista_de = quick_sort(lista_de, True)  # Ordena recursivamente la lista derecha [3 4]

        lista_iz.extend(lista_de)  # Combina las listas ordenadas de la izquierda y derecha

        return lista_iz  # Devuelve la lista ordenada de manera ascendente
    else:
        lista_iz = quick_sort(lista_iz, False)  # Ordena recursivamente la lista izquierda

        lista_de.append(pivot)  # Agrega el pivote a lista_de
        lista_de = quick_sort(lista_de, False)  # Ordena recursivamente la lista derecha

        
        lista_de.extend(lista_iz)  # Combina las listas ordenadas de la derecha e izquierda
        return lista_de  # Devuelve la lista ordenada de manera descendente
#-----------------------------------------------------------------------------------------
def calcular_mostrar_promedio_menos_ultimo (lista_jugadores :list, dato : str) -> None:
    """
        Función que calcula el promedio de el dream team exceptuando el último
    Args:
        lista_jugadores (list): lista de jugadores para acceder a sus datos
        dato (str): dato especifico para acceder al valor 
    
    Returns: La función no devuelve nada
    """
    lista_valores_nombre_promedio_puntos = []
    for indice in range(len(lista_jugadores)):
        nombre_promedio_puntos = lista_jugadores[indice]["nombre"]
        valor_promedio_puntos = lista_jugadores[indice]["estadisticas"][dato]
        datos_promedio_puntos = "{0} | {1}".format(valor_promedio_puntos, nombre_promedio_puntos)
        lista_valores_nombre_promedio_puntos.append(datos_promedio_puntos)
    lista_valores_nombre_promedio_puntos_quick = quick_sort(lista_valores_nombre_promedio_puntos, False)
    menor_promedio = lista_valores_nombre_promedio_puntos_quick[0]
    separador_menor_promedio = "|"
    menor_promedio_split = menor_promedio.split(separador_menor_promedio)
    menor_promedio_split_numero_string = menor_promedio_split[0]
    menor_promedio_split_numero_flotante = float(menor_promedio_split_numero_string)
    
    acumulador_promedio_puntos = 0
    for indice in range(len(lista_jugadores)):
        if lista_jugadores[indice]["estadisticas"][dato] == menor_promedio_split_numero_flotante:
            reducir_rango = len(lista_jugadores) -1

        else: 
            acumulador_promedio_puntos  +=  lista_jugadores[indice]["estadisticas"][dato]
    promedio = acumulador_promedio_puntos/reducir_rango
    print("{0}".format(promedio))


        

        
    # lista_jugadores_menos_ultimo= lista_jugadores[:-1]
    # acumulador_promedio_puntos_por_partido_menos_ultimo = 0
    # for indice in range(len(lista_jugadores_menos_ultimo)):
    #     acumulador_promedio_puntos_por_partido_menos_ultimo+=lista_jugadores[indice]["estadisticas"][dato]
    #     promedio_acumulador_promedio_puntos = acumulador_promedio_puntos_por_partido_menos_ultimo / len(lista_jugadores_menos_ultimo)

    # print("El promedio de puntos por partido del Dream Team menos el últmo es:{0}".format(promedio_acumulador_promedio_puntos))

#---------------------------------------------------------------------------
def calcular_y_mostrar_dato(lista_jugadores:list,dato:str) -> None:
    """
        Función para calcular y mostrar el dato, según el dato especificado

    Args:
        lista_jugadores (list): la lista de jugadores para acceder al dato
        dato (str): el dato para acceder al valor

    Returns:
        La función no devuelve nada
    """
    if dato == "logros":
        lista_jugadores_con_logros_maximo = []
        for indice in range(len(lista_jugadores)):
             if indice == 0 or len(lista_jugadores[indice][dato]) > maximo_logros:
                maximo_logros = len(lista_jugadores[indice][dato])
        
        for indice in range(len(lista_jugadores)):
            if len(lista_jugadores[indice][dato]) == maximo_logros:
                lista_jugadores_con_logros_maximo.append(lista_jugadores[indice]["nombre"])
        formato_cadena_maximos(lista_jugadores_con_logros_maximo,dato,maximo_logros)

            
    elif dato == 'promedio_puntos_por_partido':
        lista_jugadores_ordenados = []
        acumulador_promedio_puntos_por_partido = 0
        for indice in range(len(lista_jugadores)):
                nombre_promedio_puntos_por_partido=lista_jugadores[indice]["nombre"]
                valor_promedio_puntos_por_partido=lista_jugadores[indice]["estadisticas"][dato]
                acumulador_promedio_puntos_por_partido+=lista_jugadores[indice]["estadisticas"][dato]
                datos_juntos= "{0} : {1}".format(nombre_promedio_puntos_por_partido,valor_promedio_puntos_por_partido)
                lista_jugadores_ordenados.append(datos_juntos)
        promedio_acumulador_promedio_puntos = acumulador_promedio_puntos_por_partido / len(lista_jugadores)
        lista_jugadores_ordenados_quick = quick_sort(lista_jugadores_ordenados, True)
        separador_lista_jugadores_ordenados_quick = "\n"
        lista_jugadores_ordenados_quick_join = separador_lista_jugadores_ordenados_quick.join(lista_jugadores_ordenados_quick)
        print("El promedio de puntos por partido del Dream Team es:{0}\nOrden ascendente por orden alfabético del promedio puntos por partido:\n{1}".format(promedio_acumulador_promedio_puntos,
                                                                                                                                                            lista_jugadores_ordenados_quick_join))

    else:
        lista_jugadores_maximos= []
        for indice in range(len(lista_jugadores)):
            if indice == 0 or lista_jugadores[indice]["estadisticas"][dato] > maximo:
                maximo = lista_jugadores[indice]["estadisticas"][dato]


        for indice in range(len(lista_jugadores)):
            if lista_jugadores[indice]["estadisticas"][dato] == maximo:
                lista_jugadores_maximos.append(lista_jugadores[indice]["nombre"])
        formato_cadena_maximos(lista_jugadores_maximos,dato,maximo)

def formato_cadena_maximos(lista:list,dato:str,maximo:int) -> None:
    """
        Función para darle un formato a las cadenas dependiendo el tamaño de la lista.
    Args:
        lista (list): lista a darle formato.
        dato (str): dato especificado para poner en el print.
        maximo (int): maximo especificado para poner en el print.
    
    Returns:
        No devuelve nada.
    """
    if len(lista) == 1:
        cadena_maximos = lista[0]
    elif len(lista) == 2:
        texto = " y "
        cadena_maximos=texto.join(lista)
    else:
        texto = ","
        palabras_con_coma= texto.join(lista[0:-1])
        cadena_maximos = "{0} y {1}".format(palabras_con_coma,lista[-1])

    print("El jugador con el máximo de '{0}' es {1} con un total de {2}.\n".format(dato.replace("_", " "),cadena_maximos,maximo))
    
def buscar_jugador_dato(lista_jugadores:list, tipo_valor:str, dato:str) -> str:
    """
        Función que busca los datos de un jugador según el valor ingresado por input
        se verifica en cada if si el valor es válido, imprime por pantalla la mayoría
        salvo que se trate del dato logros, en ese caso, retorna un string para usar en el menú
    Args:
        lista_jugadores (list): lista de jugadores para acceder al dato
        tipo_valor (str): tipo de valor a verificar y que quiero que el usuario ingrese
        dato (str): dato para acceder a la clave en el diccionario estadisticas o, en su defencto, la clave
        del diccionario del jugador, en específico, sus logros

    Returns:
        str: devuelve un string que contiene los logros y el nombre del jugador
    """
    respuesta_valida = False
    if tipo_valor == "valor_flotante":
        while (respuesta_valida == False):
            ingresar_flotante_str= input("Ingrese un número: ")
            print("")

            if es_flotante(ingresar_flotante_str):
                valor_sanitizado=ingresar_flotante_str.replace(",", ".")
                ingresar_flotante_float= float(valor_sanitizado)
                respuesta_valida = True

            elif es_entero(ingresar_flotante_str):
                ingresar_flotante_float= float(ingresar_flotante_str)
                respuesta_valida = True

            else:
                print("Número inválido")
        
        if dato == "porcentaje_tiros_de_campo":
                lista_jugadores_ordenados_porcentaje_puntos_campo = []
                for indice in range(len(lista_jugadores)):
                    posicion_promedio_porcentaje_puntos_campo=lista_jugadores[indice]["posicion"]
                    nombre_promedio_porcentaje_puntos_campo=lista_jugadores[indice]["nombre"]
                    valor_promedio_porcentaje_puntos_campo=lista_jugadores[indice]["estadisticas"][dato]
                    datos_juntos_porcentaje_puntos_campo= "{0}|{1} : {2}".format(posicion_promedio_porcentaje_puntos_campo,nombre_promedio_porcentaje_puntos_campo, valor_promedio_porcentaje_puntos_campo)  
                    lista_jugadores_ordenados_porcentaje_puntos_campo.append(datos_juntos_porcentaje_puntos_campo)
                lista_jugadores_ordenados_porcentaje_puntos__campo_quick= quick_sort(lista_jugadores_ordenados_porcentaje_puntos_campo, True)
                separador_lista_jugadores_ordenados__porcentajes_puntos_campo_quick = "\n"
                lista_jugadores_ordenados_porcentajes_puntos_campo_quick_join = separador_lista_jugadores_ordenados__porcentajes_puntos_campo_quick.join(lista_jugadores_ordenados_porcentaje_puntos__campo_quick)
                print(lista_jugadores_ordenados_porcentajes_puntos_campo_quick_join)

        else:
            encontrar_jugadores_superiores(lista_jugadores, dato, ingresar_flotante_float)

    elif tipo_valor == "nombre":
         while (respuesta_valida == False):
            ingresar_nombre= input("Ingrese un nombre: ")

            if es_texto(ingresar_nombre):
                
                lista_logros_jugador= hay_coincidencia_inexacta(ingresar_nombre,lista_jugadores)
                if len(lista_logros_jugador) > 0:
                    texto_logros_nombre_acumulado = ""
                    for indice in range(len(lista_logros_jugador)):
                        if indice % 2 !=0:
                            
                            separador_logros = " | "
                            logros = "||{0}|| Logros: \n{1}.\n".format(lista_logros_jugador[indice-1],separador_logros.join(lista_logros_jugador[indice]))
                            
                            texto_logros_nombre_acumulado += logros
                    return texto_logros_nombre_acumulado
  
                else:
                    print("El texto ingresado no coincide con ningún jugador")
                
            
            else: 
                print("Nombre inválido")


def encontrar_jugadores_superiores(lista_jugadores:list, dato:str, maximo:str):
    """
        Función que agrega los jugadores que superen el máximo definido previamente
        luego, formatea un mensaje según el tamaño de la lista de jugadores que superen
        ese valor
    Args:
        lista_jugadores (list): la lista de jugadores
        dato (str): el dato, para guardar el nombre de quienes tengan un dato que supere el máximo
        maximo (str): el máximo, definido previamente fuera de la función
    """
    jugadores_superiores = []
    ningun_superior = False
    for jugador in lista_jugadores:
        if jugador["estadisticas"][dato] > maximo:
            jugadores_superiores.append(jugador["nombre"])

    if len(jugadores_superiores) == 1:
        cadena_maximos = jugadores_superiores[0]
    elif len(jugadores_superiores) == 2:
        cadena_maximos = " y ".join(jugadores_superiores)
    elif len(jugadores_superiores) > 2:
        palabras_con_coma = ", ".join(jugadores_superiores[:-1])
        cadena_maximos = "{0} y {1}".format(palabras_con_coma, jugadores_superiores[-1])
    else:
        ningun_superior = True

    if ningun_superior == False:
        print("Los jugadores que han superado el valor {0} de {1} son: {2}.\n".format(maximo, dato.replace("_", " "),cadena_maximos))
    else:
        print("No hay ningún jugador que supere este valor.\n")

def ordenar_dato(lista_jugadores:list,dato:str)-> list:
    """
       Función que ordena cada lista enviada

    Args:
        lista_jugadores (list): la lista de jugadores
        dato (str): el dato a ordenar

    Returns:
        list: la lista ordenada de cada dato
    """
    lista_dato = []
    for indice in range(len(lista_jugadores)):
        lista_dato.append(lista_jugadores[indice]["estadisticas"][dato])
    lista_dato_quick = quick_sort(lista_dato,False)
    return lista_dato_quick

def mostrar_posicion_segun_estadistica(lista_jugadores:list,tipo:str)-> str:
    """
        Función que muestra el ranking de cada dato de la lista de jugadores
    Args:
        lista_jugadores (list): la lista de jugadores
        tipo(str):   dependiendo del ejercicio

    Return: devuelve el ranking o el total de rankings acumuladors de cada jugador
    """
    dato_ordenado_puntos=ordenar_dato(lista_jugadores,"puntos_totales")
    dato_ordenado_rebotes=ordenar_dato(lista_jugadores,"rebotes_totales")
    dato_ordenado_asistencias=ordenar_dato(lista_jugadores,"asistencias_totales")
    dato_ordenado_robos=ordenar_dato(lista_jugadores,"robos_totales")
    acumulador_de_rankings = ""
    acumulador_de_datos= ""
    flag_encabezado = True
    
    for jugador in lista_jugadores:

        nombre_mostrar_pos = jugador["nombre"]
        if jugador["estadisticas"]["puntos_totales"] in dato_ordenado_puntos:
            indice_puntos = dato_ordenado_puntos.index(jugador["estadisticas"]["puntos_totales"]) + 1
            indice_puntos_texto = str(indice_puntos)
        if jugador["estadisticas"]["rebotes_totales"] in dato_ordenado_rebotes:
            indice_rebotes = dato_ordenado_rebotes.index(jugador["estadisticas"]["rebotes_totales"]) + 1
            indice_rebotes_texto = str(indice_rebotes)
        if jugador["estadisticas"]["asistencias_totales"] in dato_ordenado_asistencias:
            indice_asistencias = dato_ordenado_asistencias.index(jugador["estadisticas"]["asistencias_totales"]) + 1
            indice_asistencias_texto= str(indice_asistencias)
        if jugador["estadisticas"]["robos_totales"] in dato_ordenado_robos:
            indice_robos_totales= dato_ordenado_robos.index(jugador["estadisticas"]["robos_totales"]) + 1
            indice_robos_totales_texto = str(indice_robos_totales)
        suma_rankings_cada_jugador = indice_puntos+indice_rebotes+indice_asistencias+indice_robos_totales
        suma_rankings_cada_jugador_texto = str(suma_rankings_cada_jugador)
        acumulador_de_rankings+= "{0} {1}\n".format(suma_rankings_cada_jugador_texto, jugador["nombre"])
        todos_los_datos="{0}|{1}|{2}|{3}|{4}\n".format(nombre_mostrar_pos.ljust(20), indice_puntos_texto.ljust(6), indice_rebotes_texto.ljust(8), indice_asistencias_texto.ljust(11), indice_robos_totales_texto.ljust(5))
        acumulador_de_datos+= todos_los_datos  

    if tipo == "mostrar_ranking":
        print("{0}|{1}|{2}|{3}|{4}".format("Nombre".ljust(20),"Puntos".ljust(6), "Rebotes".ljust(8), "Asistencias".ljust(11), "Robos".ljust(5)))

        return acumulador_de_datos
    else:
        return acumulador_de_rankings
def contar_posicion(lista_jugadores:list):
    """
        Función que cuenta la cantidad de jugadores en cad posición
    Args:
        lista_jugadores (list): _description_
    """
    contador_escolta= 0
    contador_base= 0
    contador_ala_pivot = 0
    contador_alero = 0
    contador_pivot = 0
    for indice in range(len(lista_jugadores)):
        if lista_jugadores[indice]["posicion"] == "Escolta":
            contador_escolta += 1
        if lista_jugadores[indice]["posicion"] == "Base":
                contador_base += 1
        if lista_jugadores[indice]["posicion"] == "Ala-Pivot":
                contador_ala_pivot += 1
        if lista_jugadores[indice]["posicion"] == "Alero":
                contador_alero += 1
        if lista_jugadores[indice]["posicion"] == "Pivot":
                contador_pivot += 1
    print("Cantidad de jugadores en cada posición: ")
    print("Escolta: {0}".format(contador_escolta))
    print("Base: {0}".format(contador_base))
    print("Ala-Pivot: {0}".format(contador_ala_pivot))
    print("Alero: {0}".format(contador_alero))
    print("Pivot: {0}".format(contador_pivot))

def veces_all_star_ordenado(lista_jugadores):
    for indice in range(len(lista_jugadores)):
        print(lista_jugadores[indice]["logros"])
        patron= re.search(r'[1-9]+ veces All-Star')

        if patron in lista_jugadores[indice]["logros"]:
            print("{0}".format(lista_jugadores[indice]['nombre']))

# Determinar qué jugador tiene las mejores estadísticas en cada valor. La salida por pantalla debe tener un formato similar a este:
# Mayor cantidad de temporadas: Karl Malone (19)
# Mayor cantidad de puntos totales: Karl Malon (36928)
def maximo_cada_dato(lista_jugadores, dato):
        lista_jugadores_maximos= []
        for indice in range(len(lista_jugadores)):
            if indice == 0 or lista_jugadores[indice]["estadisticas"][dato] > maximo_individual:
                maximo_individual = lista_jugadores[indice]["estadisticas"][dato]


        for indice in range(len(lista_jugadores)):
            if lista_jugadores[indice]["estadisticas"][dato] == maximo_individual:
                lista_jugadores_maximos.append(lista_jugadores[indice]["nombre"])
        formato_maximos(lista_jugadores_maximos,dato,maximo_individual)

def formato_maximos(lista:list,dato:str,maximo:int) -> None:
    """
        Función para darle un formato a las cadenas dependiendo el tamaño de la lista.
    Args:
        lista (list): lista a darle formato.
        dato (str): dato especificado para poner en el print.
        maximo (int): maximo especificado para poner en el print.
    
    Returns:
        No devuelve nada.
    """
    if len(lista) == 1:
        cadena_maximos = lista[0]
    elif len(lista) == 2:
        texto = " y "
        cadena_maximos=texto.join(lista)
    else:
        texto = ","
        palabras_con_coma= texto.join(lista[0:-1])
        cadena_maximos = "{0} y {1}".format(palabras_con_coma,lista[-1])

    print("Mayor cantidad de {0}: {1} ({2})\n".format(dato.replace("_", " "),cadena_maximos,maximo))

def veces_all_star_ordenado(lista_jugadores: list):
    jugadores_con_all = []  # Acumulador para almacenar los jugadores con el logro "X veces All-Star"
    for indice in range(len(lista_jugadores)):
        jugadores_con_all += hay_logro_all_stars(lista_jugadores, indice)  # Agregar los jugadores encontrados al acumulador
    return jugadores_con_all

def hay_logro_all_stars(lista_jugadores, indice):
    jugadores_con_all = []
    for logro in lista_jugadores[indice]["logros"]:
        logro_tiene = "{0},{1}".format(lista_jugadores[indice]["nombre"], logro)
        if re.search(r"[0-9]+ veces All-Star", logro_tiene):
            logro_tiene_split = logro_tiene.split(",")
            invertir_logro_nombre = "{0},{1}".format(logro_tiene_split[1], logro_tiene_split[0])
            jugadores_con_all.append(invertir_logro_nombre)
    return jugadores_con_all



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
                nombre_logros=buscar_jugador_dato(lista_jugadores, "nombre", "logros")
                print(nombre_logros)
            elif opcion == "5":
                calcular_y_mostrar_dato(lista_jugadores, "promedio_puntos_por_partido")
            elif opcion == "6":
                miembro_salon=buscar_jugador_dato(lista_jugadores, "nombre", "logros")
                miembro_salon_sanitizar=miembro_salon.replace("Miembro del Salon de la Fama del Baloncesto Universitario", "dato-erroreo").split("||")
                miembro_salon_sanitizar_menos_primero= miembro_salon_sanitizar[1:]
                
                for indice in range(len(miembro_salon_sanitizar_menos_primero)):
                    if indice % 2 != 0:
                        if es_miembro_salon(miembro_salon_sanitizar_menos_primero[indice]):
                            es_miembro = "{0} pertenece al salón de la fama del baloncesto.\n".format(miembro_salon_sanitizar_menos_primero[indice-1])
                            print(es_miembro)
                        else: 
                            print("El jugador ingresado no pertenece al salón de la fama del baloncesto.")
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
                buscar_jugador_dato(lista_jugadores, "valor_flotante", "promedio_puntos_por_partido")
            elif opcion == "11":
                buscar_jugador_dato(lista_jugadores, "valor_flotante", "promedio_rebotes_por_partido")
            elif opcion == "12":
                buscar_jugador_dato(lista_jugadores, "valor_flotante", "promedio_asistencias_por_partido")
            elif opcion == "13":
                calcular_y_mostrar_dato(lista_jugadores, "robos_totales")
            elif opcion == "14":
                calcular_y_mostrar_dato(lista_jugadores, "bloqueos_totales")
            elif opcion == "15":
                buscar_jugador_dato(lista_jugadores, "valor_flotante", "porcentaje_tiros_libres")
            elif opcion == "16":
                calcular_mostrar_promedio_menos_ultimo(lista_jugadores, "promedio_puntos_por_partido")
            elif opcion == "17":
                calcular_y_mostrar_dato(lista_jugadores, "logros")

            elif opcion == "18":
                buscar_jugador_dato(lista_jugadores, "valor_flotante", "porcentaje_tiros_triples")
            elif opcion == "19":
                calcular_y_mostrar_dato(lista_jugadores, "temporadas")
            elif opcion == "20":
                buscar_jugador_dato(lista_jugadores, "valor_flotante", "porcentaje_tiros_de_campo")
            elif opcion == "23":
                ranking=mostrar_posicion_segun_estadistica(lista_jugadores,"mostrar_ranking")
                print(ranking)
            elif opcion == "24":
                contar_posicion(lista_jugadores)
            elif opcion == "25":
                pass
                # veces_all_star_lista=veces_all_star_ordenado(lista_jugadores)
                # veces_all_star_lista_ordenada= quick_sort(veces_all_star_lista,True)
                # print(veces_all_star_lista_ordenada)
            elif opcion == "26":
                maximo_cada_dato(lista_jugadores,"temporadas" )
                maximo_cada_dato(lista_jugadores,"puntos_totales" )
                maximo_cada_dato(lista_jugadores,"promedio_puntos_por_partido")
                maximo_cada_dato(lista_jugadores,"rebotes_totales")
                maximo_cada_dato(lista_jugadores,"promedio_rebotes_por_partido")
                maximo_cada_dato(lista_jugadores,"asistencias_totales")
                maximo_cada_dato(lista_jugadores,"promedio_asistencias_por_partido")
                maximo_cada_dato(lista_jugadores,"robos_totales")
                maximo_cada_dato(lista_jugadores,"bloqueos_totales")
                maximo_cada_dato(lista_jugadores,"porcentaje_tiros_de_campo")
                maximo_cada_dato(lista_jugadores,"porcentaje_tiros_libres")
                maximo_cada_dato(lista_jugadores,"porcentaje_tiros_triples")

            elif opcion == "27":
                cada_jugador_total_ranking=mostrar_posicion_segun_estadistica(lista_jugadores,"mostrar_maximo")
                separador_ranking = "\n"
                cada_jugador_total_ranking_split= cada_jugador_total_ranking.split(separador_ranking)
                cada_jugador_total_ranking_split_quick= quick_sort(cada_jugador_total_ranking_split,True)
                cada_jugador_total_ranking_split_quick_menos_primero= cada_jugador_total_ranking_split_quick[1:]
                cada_jugador_total_ranking_split_quick_menos_primero_mejor_jugador=cada_jugador_total_ranking_split_quick_menos_primero[1]
                cada_jugador_total_ranking_split_quick_menos_primero_mejor_jugador_split=cada_jugador_total_ranking_split_quick_menos_primero_mejor_jugador.split(" ")

                print("El mejor jugador es {0} {1}".format(cada_jugador_total_ranking_split_quick_menos_primero_mejor_jugador_split[1], cada_jugador_total_ranking_split_quick_menos_primero_mejor_jugador_split[2]))
            else:
                print("Opcion inválida")
            clear_console()


lista_jugadores = leer_archivo("dt.json")

menu_de_opciones(lista_jugadores)
