from instrucciones.aritmetica import operaciones_aritmeticas
from instrucciones.trigonometrica import operaciones_trigonometricas
from clases_abstractas.lexema import Lexema
from clases_abstractas.numero import Numero
from errores.generar_errores import Errores
import os

reserved = {
    'OPERACIONES'      : 'operaciones',
    'OPERACION'        : 'operacion',
    'VALOR1'           : 'valor1',
    'VALOR2'           : 'valor2',
    'SUMA'             : 'suma',
    'RESTA'            : 'resta',
    'MULTIPLICACION'   : 'multiplicacion',
    'DIVISION'         : 'division',
    'POTENCIA'         : 'potencia',
    'DIVISION'         : 'division',
    'POTENCIA'         : 'potencia',
    'RAIZ'             : 'raiz',
    'INVERSO'          : 'inverso',
    'SENO'             : 'seno',
    'COSENO'           : 'coseno',
    'TANGENTE'         : 'tangente',
    'MODULO'           : 'modulo',
    'COMA'             : ',',
    'PUNTO'            : '.',
    'DPUNTOS'          : ':',
    'CORI'             : '[',
    'CORD'             : ']',
    'LLAVEI'           : '{',
    'LLAVED'           : '}',
    'TEXTO'            : 'texto',
    'FONDO'            : 'fondo',
    'FUENTE'           : 'fuente',
    'FORMA'            : 'forma',
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

def armar_instrucciones(cadena):
    limpiar_lista_errores()
    limpiar_lista()
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = 0
    #Se analiza el contenido del cuadro de texto. 
    while cadena:
        char = cadena[puntero]
        puntero += 1
        #Al encontrar " se empieza a armar el lexema.
        if char == '"':       
            lexema, cadena = armar_lexema(cadena[puntero:])
            if lexema and cadena:
                n_columna += 1
                #Se arma el lexema como clase
                l = Lexema(lexema.lower(), n_linea, n_columna)
                #Se agrega los lexemas a la lista_lexema
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
        #Al encontrar numero se empieza a armar el numero.
        elif char.isdigit():
            token, cadena = armar_numero(cadena)
            if token and cadena:
                n_columna += 1
                # Se arma el numero como clase
                n = Numero(token, n_linea, n_columna)
                #Se agrega los numeros a la lista_lexema
                lista_lexemas.append(n)
                n_columna += len(str(token)) + 1
                puntero = 0
        elif char == '[' or char == ']':
            # Se arma el numero como clase
            c = Lexema(char, n_linea, n_columna)
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
        elif char =="\t":
            n_columna += 4
            cadena = cadena[4:]
            puntero = 0
        elif char == "\n":
            cadena = cadena[1:]
            puntero = 0
            n_linea += 1
            n_columna = 1
        elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == '.' or char == ':':
            n_columna += 1
            cadena = cadena[1:]
            puntero = 0
        else:
            #Se agrega el lexema a la lista_errores
            lista_errores.append(Errores(char, n_linea, n_columna))
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
    return lista_lexemas

def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = ''
    for char in cadena:
        puntero += char
        if char == '\"':
            #Si encuentra una ", se termina de leer el token
            return lexema, cadena[len(puntero):]    
        else:
            #Se crea el Token
            lexema += char   
    return None, None

def armar_numero(cadena):
    numero = ''
    puntero = ''
    is_decimal =  False
    for char in cadena:
        puntero += char
        if char == '.':
            is_decimal = True
        if char == '"' or char == ' ' or char == '\n' or char == '\t':
            if is_decimal:
                return float(numero), cadena[len(puntero)-1:]
            else:
                return int(numero), cadena[len(puntero)-1:]
        else:
            if char != ',':
                #Si no es una "," se agrega al numero
                numero += char
    return None, None

def operar_cadenas():
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
                n1 = operar_cadenas()
        elif lexema.operar(None) ==  'valor2':
            n2 = lista_lexemas.pop(0)
            if n2.operar(None) == '[':
                n2 = operar_cadenas()
        if operacion and n1 and n2:
            return operaciones_aritmeticas(n1, n2, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n2.getFila()}:{n2.getColumna()}')
        elif operacion and n1 and (operacion.operar(None) == 'seno' or operacion.operar(None) == 'coseno' or operacion.operar(None) == 'tangente' or operacion.operar(None) == 'inverso'):
            return operaciones_trigonometricas(n1, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
    return None

def lexema_grafico():
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
    lexema_grafico()
    global instrucciones
    while True:
        operacion = operar_cadenas()
        if operacion:
            instrucciones.append(operacion)
        else:
            break
        for instruccion in instrucciones:
            instruccion.operar(None)
    return instrucciones

def limpiar_lista():
    instrucciones.clear()
    lista_datos_graphviz.clear()

def limpiar_lista_errores():
    global n_linea
    lista_errores.clear()
    n_linea = 1

def configuracion_nodo(i, id, etiqueta, objeto):
    global lista_datos_graphviz
    color_fondo_nodo = lista_datos_graphviz[1]
    color_fuente_nodo= lista_datos_graphviz[2]
    forma_nodo = lista_datos_graphviz[3]
    #Fondo
    if color_fondo_nodo=="rojo" or color_fondo_nodo=="red":
        color_fondo_nodo="red"
    elif color_fondo_nodo=="amarillo" or color_fondo_nodo=="yellow":
        color_fondo_nodo="yellow"
    elif color_fondo_nodo=="azul" or color_fondo_nodo=="blue":
        color_fondo_nodo="blue"
    elif color_fondo_nodo=="morado" or  color_fondo_nodo=="purple":
        color_fondo_nodo="purple"
    elif color_fondo_nodo=="naranja" or color_fondo_nodo=="anaranjado" or color_fondo_nodo=="orange":
        color_fondo_nodo="orange"
    elif color_fondo_nodo=="verde" or color_fondo_nodo=="green":
        color_fondo_nodo="green"
    elif color_fondo_nodo=="blanco" or color_fondo_nodo=="white":
        color_fondo_nodo="white"
    elif color_fondo_nodo=="negro" or  color_fondo_nodo=="black":
        color_fondo_nodo="black"
    else:
        color_fondo_nodo = "white"
    #Fuente
    if color_fuente_nodo== "rojo" or color_fuente_nodo=="red":
        color_fuente_nodo="red"
    elif color_fuente_nodo== "amarillo" or color_fuente_nodo=="yellow":
        color_fuente_nodo= "yellow"
    elif color_fuente_nodo== "azul" or color_fuente_nodo=="blue":
        color_fuente_nodo= "blue"
    elif color_fuente_nodo== "morado" or color_fuente_nodo=="purple":
        color_fuente_nodo= "purple"
    elif color_fuente_nodo== "naranja" or color_fuente_nodo== "anaranjado" or color_fuente_nodo=="orange":
        color_fuente_nodo= "orange"
    elif color_fuente_nodo== "verde" or color_fuente_nodo=="green":
        color_fuente_nodo= "green"
    elif color_fuente_nodo== "blanco" or color_fuente_nodo=="white":
        color_fuente_nodo= "white"
    elif color_fuente_nodo== "negro" or color_fuente_nodo=="black":
        color_fuente_nodo= "black"
    else:
        color_fuente_nodo= "black"
    #Formas
    if forma_nodo== "circulo" or forma_nodo== "circle":
        forma_nodo= "circle"
    elif forma_nodo == "cuadrado" or forma_nodo == "box":
        forma_nodo = "box"
    elif forma_nodo == "poligono" or forma_nodo == "polygon":
        forma_nodo = "polygon"
    elif forma_nodo == "elipse" or forma_nodo == "ellipse":
        forma_nodo = "ellipse"
    elif forma_nodo == "triangulo" or forma_nodo == "triangle":
        forma_nodo = "triangle"
    elif forma_nodo == "ovalo" or forma_nodo == "oval":
        forma_nodo = "oval"
    elif forma_nodo == "rombo" or forma_nodo == "diamond":
        forma_nodo = "diamond"
    elif forma_nodo == "trapezoide" or forma_nodo == "trapezium":
        forma_nodo = "trapezium"
    else:
        forma_nodo = "circle"
    text_dot = ""
    if objeto:
        if type(objeto) == Numero:
            text_dot = text_dot + f'nodo_{i}{id}{etiqueta}[label="{objeto.operar(None)}",fontcolor="{color_fuente_nodo}",fillcolor={color_fondo_nodo}, style=filled,shape={forma_nodo}];\n'
        if type(objeto) == operaciones_trigonometricas:
            text_dot = text_dot + f'nodo_{i}{id}{etiqueta}[label="{objeto.tipo.lexema}\\n{objeto.operar(None)}",fontcolor="{color_fuente_nodo}",fillcolor={color_fondo_nodo}, style=filled,shape={forma_nodo}];\n'
            text_dot = text_dot + configuracion_nodo(i, id+1, etiqueta+"_angulo", objeto.left)
            text_dot = text_dot + f'nodo_{i}{id}{etiqueta} -> nodo_{i}{id+1}{etiqueta}_angulo;\n'
        if type(objeto) ==  operaciones_aritmeticas:
            text_dot = text_dot + f'nodo_{i}{id}{etiqueta}[label="{objeto.tipo.lexema}\\n{objeto.operar(None)}",fontcolor="{color_fuente_nodo}",fillcolor={color_fondo_nodo}, style=filled,shape={forma_nodo}];\n'
            text_dot = text_dot + configuracion_nodo(i, id+1, etiqueta + "_left", objeto.left)
            text_dot = text_dot +f'nodo_{i}{id}{etiqueta} -> nodo_{i}{id+1}{etiqueta}_left;\n'
            text_dot = text_dot +configuracion_nodo(i, id+1, etiqueta+"_right", objeto.right)
            text_dot = text_dot + f'nodo_{i}{id}{etiqueta} -> nodo_{i}{id+1}{etiqueta}_right;\n'
    return text_dot

def graficar():
    titulo = lista_datos_graphviz[0]
    text_dot = 'digraph grafo{\n'
    for i in range(len(instrucciones)):
        text_dot = text_dot + configuracion_nodo(i, 0, '', instrucciones[i])
    text_dot = text_dot +  f'''
    labelloc = "t"
    label = "{titulo}"
    '''
    text_dot = text_dot +  '}'
    return text_dot

def generar_grafica():
    nombre = "REPORTE_202201524"+".dot"
    with open(nombre, 'w') as f:
        f.write(graficar())
    os.system(f'dot -Tpdf {nombre} -o {"REPORTE_202201524"}.pdf')

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