from instrucciones.aritmetica import *
from instrucciones.trigonometrica import *
from clases_abstractas.lexema import *
from clases_abstractas.numero import *
from errores.generar_errores import *
import os

#Palabras
reserved = {
    'ROPERACIONES'      : 'operaciones',
    'ROPERACION'        : 'operacion',
    'RVALOR1'           : 'valor1',
    'RVALOR2'           : 'valor2',
    'RSUMA'             : 'suma',
    'RRESTA'            : 'resta',
    'RMULTIPLICACION'   : 'multiplicacion',
    'RDIVISION'         : 'division',
    'RPOTENCIA'         : 'potencia',
    'RDIVISION'         : 'division',
    'RPOTENCIA'         : 'potencia',
    'RRAIZ'             : 'raiz',
    'RINVERSO'          : 'inverso',
    'RSENO'             : 'seno',
    'RCOSENO'           : 'coseno',
    'RTANGENTE'         : 'tangente',
    'RMODULO'           : 'modulo',
    'COMA'              : ',',
    'PUNTO'             : '.',
    'DPUNTOS'           : ':',
    'CORI'              : '[',
    'CORD'              : ']',
    'LLAVEI'            : '{',
    'LLAVED'            : '}',
    'DTEXTO'            : 'texto',
    'DFONDO'            : 'fondo',
    'DFUENTE'           : 'fuente',
    'DFORMA'            : 'forma',
}
lexemas = list(reserved.values())

global n_linea
global n_columna
global instrucciones
global lista_lexemas
global lista_errores
global lista_datos_graphviz

n_linea = 1
n_columna = 0
lista_lexemas = []
instrucciones = []
lista_errores = []
lista_datos_graphviz = []


def instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ""
    puntero = 0
    while cadena:
        char = cadena[puntero]
        puntero += 1
        if char == '\"':
            lexema, cadena = armar_lexema(cadena[puntero:])
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna)
                lista_lexemas.append(l)
                n_columna += len(lexema)+1
                puntero = 0
        elif char.isdigit():
            token, cadena = armar_numero(cadena)
            if token and cadena:
                n = Numero(token, n_linea, n_columna)
                lista_lexemas.append(n)
                n_columna += len(str(token))
                puntero = 0
        elif char == '-':
            token, cadena = armar_numero(cadena)
            if token and cadena:
                n = Numero(token, n_linea, n_columna)
                lista_lexemas.append(n)
                n_columna += len(str(token))
                puntero = 0
        elif char == "[" or char == "]":
            c = Lexema(char, n_linea, n_columna)
            n_columna += 1
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
        elif char == "\t":
            cadena = cadena[4:]
            n_columna += 4
            puntero = 0
        elif char == "\n":
            cadena = cadena[1:]
            n_columna = 0
            n_linea += 1
            puntero = 0
        elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == ':' or char == '.' :
            cadena = cadena[1:]
            n_columna += 1
            puntero = 0
        else:
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
            lista_errores.append(Errores(char, n_linea, n_columna))
    return lista_lexemas

def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ""
    puntero = ""
    for char in cadena:
        puntero += char
        if char == '\"':
            return lexema, cadena[len(puntero):]
        else:
            lexema += char
    return None, None

def armar_numero(cadena):
    numero = ''
    puntero = ''
    is_decimal = False
    isNegative = False
    for char in cadena:
        puntero += char
        if char == "-":
            isNegative = True
        if char == ".":
            is_decimal = True
        if char == '"' or char == ' ' or char == '\n' or char == '\t' or char == ']' or char == ',':
            if is_decimal:
                return float(numero), cadena[len(puntero)-1:]
            if isNegative:
                return int(numero), cadena[len(puntero)-1:]
            else:
                return int(numero), cadena[len(puntero)-1:]
        else:
            numero += char
    return None, None

def operar():
    global lista_lexemas
    global instrucciones
    operacion = ''
    n1 = ''
    n2 = ''
    while lista_lexemas:
        lexema = lista_lexemas.pop(0)
        if lexema.operar(None) == 'operacion':
            operacion = lista_lexemas.pop(0)
        elif lexema.operar(None) == 'valor1':
            n1 = lista_lexemas.pop(0)
            if n1.operar(None) == '[':
                n1 = operar()
        elif lexema.operar(None) == 'valor2':
            n2 = lista_lexemas.pop(0)
            if n2.operar(None) == '[':
                n2 = operar()
        if operacion and n1 and n2:
            return operaciones_aritmeticas(n1, n2, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n2.getFila()}:{n2.getColumna()}')
        elif operacion and n1 and (operacion.operar(None) == 'seno' or operacion.operar(None) == 'coseno' or operacion.operar(None) == 'tangente'):
            return operaciones_trigonometricas(n1, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
    return None

def lexemas_grafico():
    global lista_lexemas
    for i in range(len(lista_lexemas)):
        lexema = lista_lexemas[i]
        if lexema.operar(None) == 'texto':
            lista_datos_graphviz.append(lista_lexemas[i+1].operar(None))
        if lexema.operar(None) == 'fondo':
            lista_datos_graphviz.append(lista_lexemas[i+1].operar(None))
        elif lexema.operar(None) == 'fuente':
            lista_datos_graphviz.append(lista_lexemas[i+1].operar(None))
        elif lexema.operar(None) == 'forma':
            lista_datos_graphviz.append(lista_lexemas[i+1].operar(None))

def realizar_operaciones():
    global instrucciones
    left = ""
    right = ""
    while True:
        operacion = operar()
        if operacion:
            instrucciones.append(operacion)
        else:
            break
        for instruccion in instrucciones:
            instruccion.operar(None)
    return instrucciones

def graficar():
    titulo = lista_datos_graphviz[0]
    dot = 'digraph grafo{\n'
    for i in range(len(instrucciones)):
        dot += separar(i, 0, '', instrucciones[i])
    dot += f'''
    labelloc = "t"
    label = "{titulo}"
    '''
    dot += '}'
    return dot

def generar_grafica(nombre_grafica):
    nombre = nombre_grafica+".dot"
    with open(nombre, 'w') as f:
        f.write(graficar())
    os.system(f'dot -Tpng {nombre} -o {nombre_grafica}.png')

def limpiar_lista():
    instrucciones.clear()
    lista_datos_graphviz.clear()

def limpiar_lista_errores():
    global n_linea
    lista_errores.clear()
    n_linea = 1

def separar(i, id, etiqueta, objeto):
    global lista_datos_graphviz
    colorFondo = lista_datos_graphviz[1]
    colorFuente = lista_datos_graphviz[2]
    forma = lista_datos_graphviz[3]
    #Colores
    rojo='red'
    amarillo='yellow'
    azul='blue'
    morado='purple'
    naranja='orange'
    verde='green'
    negro='black'
    blanco='white'
    #Fondo
    if colorFondo=="rojo":
        colorFondo=rojo
    elif colorFondo=="amarillo":
        colorFondo=amarillo
    elif colorFondo=="azul":
        colorFondo=azul
    elif colorFondo=="morado":
        colorFondo=morado
    elif colorFondo=="naranja" or colorFondo == "anaranjado":
        colorFondo=naranja
    elif colorFondo=="verde":
        colorFondo=verde
    elif colorFondo=="blanco":
        colorFondo = negro
    elif colorFondo=="negro":
        colorFondo=blanco
    else:
        colorFondo = "grey"
    #Fuente
    if colorFuente == "rojo":
        colorFuente = rojo
    elif colorFuente == "amarillo":
        colorFuente = amarillo
    elif colorFuente == "azul":
        colorFuente = azul
    elif colorFuente == "morado":
        colorFuente = morado
    elif colorFuente == "naranja" or colorFuente == "anaranjado":
        colorFuente = naranja
    elif colorFuente == "verde":
        colorFuente = verde
    elif colorFuente == "blanco":
        colorFuente = blanco
    elif colorFuente == "negro":
        colorFuente = negro
    else:
        colorFuente = "grey"
    #Formas
    if forma == "circulo" or forma == "circle":
        forma = "circle"
    elif forma == "cuadrado" or forma == "box":
        forma = "box"
    elif forma == "poligono" or forma == "polygon":
        forma = "polygon"
    elif forma == "elipse" or forma == "polygon":
        forma = "ellipse"
    elif forma == "triangulo" or forma == "triangle":
        forma = "triangle"
    elif forma == "ovalo" or forma == "oval":
        forma = "oval"
    elif forma == "rombo" or forma == "diamond":
        forma = "diamond"
    elif forma == "trapezoide" or forma == "trapezium":
        forma = "trapezium"
    else:
        forma = "circle"
    dot = ""
    if objeto:
        if type(objeto) == Numero:
            dot += f'nodo_{i}{id}{etiqueta}[label="{objeto.operar(None)}",fontcolor="{colorFuente}",fillcolor={colorFondo}, style=filled,shape={forma}];\n'
        if type(objeto) == operaciones_trigonometricas:
            print(objeto.columna)
            dot += f'nodo_{i}{id}{etiqueta}[label="{objeto.tipo.lexema}\\n{objeto.operar(None)}",fontcolor="{colorFuente}",fillcolor={colorFondo}, style=filled,shape={forma}];\n'
            dot += separar(i, id+1, etiqueta+"_angulo", objeto.left)
            dot += f'nodo_{i}{id}{etiqueta} -> nodo_{i}{id+1}{etiqueta}_angulo;\n'
        if type(objeto) ==  operaciones_aritmeticas:
            dot += f'nodo_{i}{id}{etiqueta}[label="{objeto.tipo.lexema}\\n{objeto.operar(None)}",fontcolor="{colorFuente}",fillcolor={colorFondo}, style=filled,shape={forma}];\n'
            dot += separar(i, id+1, etiqueta + "_left", objeto.left)
            dot += f'nodo_{i}{id}{etiqueta} -> nodo_{i}{id+1}{etiqueta}_left;\n'
            dot += separar(i, id+1, etiqueta+"_right", objeto.right)
            dot += f'nodo_{i}{id}{etiqueta} -> nodo_{i}{id+1}{etiqueta}_right;\n'
    return dot

def obtener_errores():
    global lista_errores
    formatoErrores = '{\n\t"errores":[\n'
    for i in range(len(lista_errores)):
        error = lista_errores[i]
        formatoErrores += error.operar(i+1)
        if i != len(lista_errores)-1:
            formatoErrores += ',\n'
        else:
            formatoErrores += '\n'
    formatoErrores += '\t]\n}'
    return formatoErrores

def crear_archivo_errores():
    nombre = "RESULTADOS_202201524"+".json"
    with open(nombre, 'w') as f:
        f.write(obtener_errores())