"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    Res1 = 0
    with open('data.csv') as datos:
        datos = csv.reader(datos, delimiter='	')
        for fila in datos:
            Res1 += int(fila[1])
    return Res1

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    letras = []
    Res2 = []

    with open('data.csv') as datos:
        datos = csv.reader(datos, delimiter='	')
        for i in datos:
            letras.append(i[0])         
    for j in set(letras):
        Res2.append((j, letras.count(j)))
    Res2.sort()

    return Res2

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    letra=[]
    suma = []
    Res3=[]
    with open('data.csv') as datos:
        datos = csv.reader(datos, delimiter='	')
        for i in datos:
            if(not i[0] in letra):
                letra.append(i[0])
                suma.append(int(i[1]))
            else:
                suma[letra.index(i[0])]+=int(i[1])
    for J in letra:
        R3.append((J,conteo[letra.index(J)]))
    Res3.sort(reverse=False)
    return

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    
    Meses = []
    with open('data.csv') as datos:
        datos = csv.reader(datos, delimiter='	')
        for i in datos:
            Mes = i[2].split("-")[1]
            Meses.append(mes)
    Res4 = []
    for Mes in sorted(set(Meses)):
        Res4.append((Mes, Meses.count(Mes)))
    return Res4
  
def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    Letra = []
    Conteo = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for i in datos:
            if not i[0] in letras:
                Letra.append(i[0])
                Conteo.append([int(i[1])])
            else:
                Conteo[Letra.index(i[0])].append(int(i[1]))
    Res5 = []
    for l in sorted(set(Letra)):
        Res5.append((l, max(Conteo[Letra.index(l)]), min(Conteo[Letras.index(l)])))  
    return Res5
    
def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    cadenas = []
    valores = []
    with open('data.csv') as datos:
        datos = csv.reader(datos, delimiter='	')
        for i in datos:
            dic = i[4].split(',')

            for j in dic: 
                cadena = j.split(':')[0]
                valor = j.split(':')[1]

                if cadena not in cadenas:
                    cadenas.append(cadena)
                    valores.append([int(valor)])
                else:
                    valores[cadenas.index(cadena)].append(int(valor))
    R6 = []
    for cadena in sorted(cadenas):
        R6.append((cadena, min(valores[cadenas.index(cadena)]), max(valores[cadenas.index(cadena)])))

    return R6
    
def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    numeros = []
    letras = []
    with open('data.csv') as datos:
        datos = csv.reader(datos, delimiter='	')
        for fila in datos:
            if int(fila[1]) not in numeros:
                numeros.append(int(fila[1]))
                letras.append([fila[0]])
            else:
                letras[numeros.index(int(fila[1]))].append(fila[0])
    R7 = []
    for numero in sorted(numeros):
        R7.append((numero, letras[numeros.index(numero)]))
    return R7
   
def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    numeros = []
    letras = []
    with open('data.csv') as datos:
        datos = csv.reader(datos, delimiter='	')
        for fila in datos:
            if int(fila[1]) not in numeros:
                numeros.append(int(fila[1]))
                letras.append({fila[0]})
            else:
                letras[numeros.index(int(fila[1]))].add(fila[0])
    R8 = []
    for numero in sorted(numeros):
        R8.append((numero, list(sorted(letras[numeros.index(numero)]))))
    R8.sort()
    
    return R8
    
def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    dic = {}

    with open('data.csv') as datos:
        datos = csv.reader(datos, delimiter='	')
        for fila in datos:
            diccionario = fila[4].split(',')
            for i in diccionario: 
                cadena = i.split(':')[0]

                if cadena not in dic.keys():
                    dic[cadena] = 1
                else:
                    dic[cadena] += 1

    R9 = dict(sorted(dic.items()))
    
    return R9
    
def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
     R10 = []

    with open('data.csv') as datos:
        datos = csv.reader(datos, delimiter='	')
        for fila in datos:
            col4 = len(fila[3].split(','))
            col5 = len(fila[4].split(','))
            R10.append((fila[0], col4, col5))
        
    return R10

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    letras = {}

    with open('data.csv') as datos:
        datos = csv.reader(datos, delimiter='	')
        for fila in datos:
            for letra in fila[3].split(','):
                if not letra in letras.keys():
                    letras[letra] = int(fila[1])
                else:
                    letras[letra] += int(fila[1])

    R11 = dict(sorted(letras.items()))
    return R11

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    letras = {}
    with open('data.csv') as datos:
        datos = csv.reader(datos, delimiter='	')
        for fila in datos:
            letra = fila[0]
                
            for elemento in fila[4].split(','):
                numero = int(elemento.split(':')[1])

                if not letra in letras.keys():
                    letras[letra] = numero
                else:
                    letras[letra] += numero

    R12 = dict(sorted(letras.items()))
    return R12
