## Aplicación Numérica Con Análisis Léxico

## abstract.py

Se define una clase Expresion la cual es una clase abstracta que utiliza el módulo abc. Esta clase abstracta sirve como una plantilla base para definir otras clases que representan expresiones en algún tipo de árbol de expresiones o estructura similar, además proporciona una estructura básica para representar expresiones y requiere que las clases derivadas implementen ciertos métodos. Las clases derivadas de Expresion deben implementar “operar”, “getFila”, y “getColumna” de acuerdo con la lógica específica de la expresión que representan.

<image src="https://i.ibb.co/tKjHLJn/abstract.png">


## lexema.py

La clase Lexema es una subclase de la clase abstracta Expresion definida anteriormente. Esta clase Lexema representa una expresión que consiste en un lexema (texto) junto con su ubicación en un archivo o estructura similar. Esta implementación específica devuelve el lexema como resultado de la operación y proporciona métodos para obtener la fila y la columna del lexema.

<image src="https://i.ibb.co/CsynT6t/lexema.png">


## numero.py

La clase Numero es otra subclase de la clase abstracta Expresion. Al igual que la clase Lexema, esta clase Numero representa una expresión, pero en este caso, representa un número. Dicha clase representa una expresión numérica y devuelve su valor como resultado de la operación, también proporciona métodos para obtener la fila y la columna del número.

<image src="https://i.ibb.co/TkGTsqx/numero.png">


## generar_errores.py
La clase Errores es otra subclase de la clase abstracta Expresion. A diferencia de las clases Lexema y Numero, esta clase Errores representa errores léxicos o errores en el análisis léxico del lenguaje declarado en el archivo de entrada. En el init se declaran las variables de fila y columna que representan la ubicación del error léxico con respecto al lenguaje. 

El método de operar toma un argumento “no”, que es el error encontrado en el archivo de entrada. Luego, crea una representación en formato JSON del error léxico, incluyendo el número de error (no), el lexema que causó el error, el tipo de error, la columna y la fila en la que ocurrió el error.

<image src="https://i.ibb.co/4Sx6xD4/generar-errores.png">


## aritmetica.py
La clase operaciones_aritmeticas es una implementación concreta de la clase abstracta Expresion. Representa expresiones aritméticas que involucran operaciones como suma, resta, multiplicación, división, etc. La implementación del método operar ejecuta la operación aritmética correspondiente en función de la expresión tipo proporcionada y devuelve el resultado.

El constructor de la clase toma cinco parámetros: left, right, tipo, fila, y columna. Left y Right representan las expresiones izquierda y derecha de la operación aritmética, respectivamente. Tipo es una expresión que determina el tipo de operación aritmética que se debe realizar.

El método operar implementa el método abstracto operar de la clase base Expresion. Realiza la operación aritmética basada en el tipo de operación proporcionado por la expresión tipo. Primero, obtiene los valores numéricos de las expresiones izquierda y derecha llamando a self.left.operar(arbol) y self.right.operar(arbol), respectivamente. Luego, realiza la operación aritmética correspondiente en función del valor devuelto por self.tipo.operar(arbol). El resultado de la operación se almacena en la variable resultado y se devuelve como resultado de la función operar.

<image src="https://i.ibb.co/x21j9CV/aritmetica.png">


## trigonometrica.py

La clase operaciones_trigonometricas es una implementación concreta de la clase abstracta Expresion. Representa expresiones trigonométricas que involucran funciones trigonométricas como el seno, el coseno y la tangente. La implementación del método operar calcula el resultado de la operación trigonométrica correspondiente y lo devuelve.

El constructor de la clase operaciones_trigonometricas toma tres parámetros: left, tipo, fila, y columna. Left representa la expresión cuyo resultado se utilizará como argumento para la función trigonométrica. Tipo es una expresión que determina el tipo de operación trigonométrica que se debe realizar.

El método operar implementa el método abstracto operar de la clase base Expresion. Realiza la operación trigonométrica basada en el tipo de operación proporcionado por la expresión tipo. Primero, obtiene el valor numérico de la expresión left llamando a self.left.operar(arbol). El resultado se asume que representa un ángulo en grados. Luego, verifica el tipo de operación trigonométrica proporcionada por self.tipo.operar(arbol) y calcula el resultado correspondiente utilizando las funciones trigonométricas del módulo math. Los resultados se redondean a dos decimales antes de ser devueltos.

<image src="https://i.ibb.co/DtG2CtV/trigonometrica.png">


## main.py

La clase ventana_principal es una clase que define la interfaz gráfica de una aplicación de escritura y análisis de archivos JSON utilizando la biblioteca Tkinter en Python. 

- ***Constructor***

El constructor de la clase se llama cuando se crea un objeto de la clase. En este caso, se llama cuando se crea una instancia de ventana_principal.

1.	En el constructor se declaran las variables self.archivo_seleccionado y self.archivo_analizado que son variables de instancia que se utilizan para rastrear si se ha seleccionado un archivo y si se ha analizado un archivo JSON. Inicialmente, ambas se establecen en False.
2.	Se configura la ventana principal de la aplicación con un título, dimensiones, color de fondo y se hace que la ventana no sea redimensionable.
3.	Se crea un marco (opciones_frame) para los botones de opciones en la parte superior de la ventana.
4.	Se crea un botón llamado boton_archivo que se usa para mostrar un menú desplegable de opciones relacionadas con archivos, como abrir, guardar, guardar como y salir.
5.	Se crea un menú (opciones) que contiene las opciones relacionadas con archivos y se asocia con el botón boton_archivo.
6.	Se crean botones para realizar acciones como analizar, mostrar errores y generar un reporte.
7.	Se empaqueta el marco opciones_frame y el marco cuadrotexto_frame para que ocupen espacio en la ventana principal.

<image src="https://i.ibb.co/sFB7Ns7/constructor.png">


- ***Buscar_Archivo***

Esta función se llama cuando se hace clic en la opción "Abrir" del menú desplegable de archivo. Realiza lo siguiente:

1.	Muestra un cuadro de diálogo para seleccionar un archivo JSON.
2.	Lee el contenido del archivo seleccionado y lo muestra en el cuadro de texto (self.cuadroTexto).
3.	Actualiza la variable self.texto con el contenido del archivo.
4.	Establece la variable self.archivo_seleccionado en True para indicar que se ha seleccionado un archivo.

<image src="https://i.ibb.co/30Ghx2s/buscar-archivo.png">


- ***Guardar_Archivo***

Esta función se llama cuando se hace clic en la opción "Guardar" del menú desplegable de archivo. Realiza lo siguiente:

1.	Comprueba si se ha seleccionado un archivo (self.archivo_seleccionado es True).
2.	Obtiene el contenido del cuadro de texto (self.cuadroTexto).
3.	Escribe el contenido en el archivo original seleccionado (self.ruta_seleccionada).

<image src="https://i.ibb.co/8s78c1D/guardar-archivo.png">


- ***Guardar_Como***

Esta función se llama cuando se hace clic en la opción "Guardar Como" del menú desplegable de archivo. Realiza lo siguiente:

1.	Comprueba si se ha seleccionado un archivo (self.archivo_seleccionado es True).
2.	Obtiene el contenido del cuadro de texto (self.cuadroTexto).
3.	Abre un cuadro de diálogo para seleccionar la ubicación y el nombre del archivo en el que se guardará.
4.	Escribe el contenido en el archivo seleccionado.

<image src="https://i.ibb.co/y0CV2Xm/guardar-como.png">


- ***Salir***

Esta función se llama cuando se hace clic en la opción "Salir" del menú desplegable de archivo. Muestra un mensaje de despedida y cierra la aplicación.

<image src="https://i.ibb.co/tHDJq0F/salir.png">


- ***Analizar***

Esta función se llama cuando se hace clic en el botón "Analizar". Realiza lo siguiente:

1.	Comprueba si se ha seleccionado un archivo (self.archivo_seleccionado es True).
2.	Llama a la función instruccion con el contenido del archivo para analizar el archivo JSON.
3.	Llama a otras funciones para realizar operaciones específicas (realizar_operaciones).
4.	Muestra un mensaje de información si el análisis se realiza correctamente.

<image src="https://i.ibb.co/FDbXMRY/analizar.png">


- ***Reporte***

Esta función se llama cuando se hace clic en el botón "Reporte". Realiza lo siguiente:

1.	Comprueba si se ha realizado el análisis del archivo (self.archivo_analizado es True).
2.	Llama a la función generar_grafica para crear un reporte gráfico.
3.	Muestra un mensaje de información si el reporte se crea correctamente.

<image src="https://i.ibb.co/nmKFdgW/reporte.png">


- ***Errores***

Esta función se llama cuando se hace clic en el botón "Errores". Realiza lo siguiente:

1.	Comprueba si se ha realizado el análisis del archivo (self.archivo_analizado es True).
2.	Llama a la función crear_archivo_errores para crear un informe de errores.
3.	Muestra un mensaje de información si el informe de errores se crea correctamente.

<image src="https://i.ibb.co/qWMG44G/erorres.png">


## analizador.py

El archivo analizador contiene una serie de funciones que son utilizadas para el análisis léxico del documento de entrada. Al principio del archivo se tienen las siguientes instrucciones.

- Importaciones: La clase comienza importando varias clases y módulos necesarios. Entre ellos, se importan clases relacionadas con operaciones aritméticas y trigonométricas, así como clases relacionadas con el manejo de errores. Estas importaciones son necesarias para realizar operaciones y gestionar errores durante el análisis del código.

- Diccionario de palabras reservadas: Se define un diccionario llamado reserved que contiene palabras reservadas del lenguaje que estás analizando. Estas palabras reservadas se asignan a ciertos lexemas, lo que permite reconocer y clasificar diferentes elementos del código fuente.

- Variables globales: Se definen varias variables globales, como n_linea, n_columna, lista_lexemas, instrucciones, lista_errores, y lista_datos_graphviz. Estas variables se utilizan para realizar un seguimiento de la posición en el código fuente, almacenar lexemas, instrucciones y errores, y recopilar información para la generación de gráficos.

<image src="https://i.ibb.co/0th1bd0/analizador.png">


- ***armar_instrucciones***

Esta función realiza el análisis léxico del código fuente representado como una cadena. Itera sobre la cadena de entrada y reconoce lexemas, números y otros elementos, construyendo una lista de lexemas.

1.	Itera sobre la cadena de entrada caracter por caracter.
2.	Reconoce lexemas, números y caracteres especiales, como comillas, corchetes, tabulaciones y saltos de línea.
3.	Almacena los lexemas reconocidos en la lista lista_lexemas.

<image src="https://i.ibb.co/w0bQtRF/armar-instrucciones.png">


- ***armar_lexema***

Esta función se utiliza para extraer un lexema entre comillas dobles dentro de la cadena.

1.	Itera sobre la cadena de entrada.
2.	Cuando encuentra una comilla doble, devuelve el lexema dentro de las comillas y la cadena restante después del lexema.

<image src="https://i.ibb.co/VqY8xts/armar-lexema.png">


- ***armar_numero***

Esta función se utiliza para extraer números de la cadena, incluyendo números decimales y números negativos.

1.	Itera sobre la cadena de entrada.
2.	Cuando encuentra un carácter que no es parte de un número válido, devuelve el número extraído y la cadena restante después del número.

<image src="https://i.ibb.co/rmTyNQ4/armar-numero.png">


- ***operar_cadena***

Esta función realiza análisis sintáctico para construir un árbol de expresiones a partir de los lexemas almacenados en lista_lexemas.

1.	Itera sobre los lexemas en lista_lexemas.
2.	Reconoce operadores aritméticos y trigonométricos, así como valores numéricos.
3.	Construye y retorna árboles de expresiones que representan las operaciones reconocidas.

<image src="https://i.ibb.co/mty2H50/operar-cadena.png">


- ***lexemas_grafico***

Esta función se utiliza para obtener información relacionada con el formato de gráficos a partir de los lexemas.

1.	Itera sobre los lexemas en busca de información relacionada con el formato de gráficos, como texto, color de fondo, color de fuente y forma.
2.	Almacena esta información en la lista lista_datos_graphviz.

<image src="https://i.ibb.co/XX9wVLC/lexemas-grafico.png">


- ***realizar_operaciones***

Esta función realiza las operaciones aritméticas y trigonométricas previamente reconocidas y construidas en lista_lexemas.

1.	Itera sobre las instrucciones previamente construidas y realiza las operaciones correspondientes.
2.	Almacena los resultados de las operaciones en instrucciones.

<image src="https://i.ibb.co/xsgyVN5/realizar-operaciones.png">


- ***graficar***

Esta función genera un código en formato DOT (utilizado por Graphviz) para crear un gráfico basado en las instrucciones y los formatos de gráficos almacenados en instrucciones y lista_datos_graphviz.

1.	Itera sobre las instrucciones y los formatos de gráficos para generar el código DOT necesario para crear un gráfico.
2.	Incluye etiquetas, colores, formas y conexiones entre nodos.

<image src="https://i.ibb.co/HdJR07s/graficar.png">


- ***generar_grafica***

Esta función utiliza el código DOT generado por graficar() para crear un archivo PDF con el gráfico correspondiente.

1.	Genera un archivo DOT y lo utiliza con Graphviz para crear un archivo PDF con el gráfico.

<image src="https://i.ibb.co/2vJtvMK/generar-grafica.png">


- ***limpiar_lista***

Esta función limpia la lista instrucciones y lista_datos_graphviz, lo que permite realizar nuevas operaciones y gráficos sin conflictos con datos anteriores.

<image src="https://i.ibb.co/F4BJhKP/limpiar-lista.png">


- ***limpiar_lista_errores***

Esta función reinicia la lista de errores y restablece la variable n_linea a 1. Es útil para eliminar errores previos y comenzar un nuevo análisis.

<image src="https://i.ibb.co/t8GGWKF/limpiar-lista-errores.png">


- ***configuracion_nodo***

Esta función se utiliza para configurar nodos en el código DOT de Graphviz, definiendo su aspecto y conexiones.

1.	Configura los nodos con etiquetas, colores de fondo y fuente, formas y conexiones según el tipo de objeto proporcionado (Número o expresión aritmética/trigonométrica).
2.	La función se llama recursivamente para manejar subnodos en el árbol de expresiones.

<image src="https://i.ibb.co/DVJjrFN/configuraciones-nodo1.png">
<image src="https://i.ibb.co/4JXp0Pd/configuraciones-nodo2.png">


- ***obtener_errores***

Esta función recopila información sobre errores léxicos almacenados en lista_errores y la devuelve en formato JSON.

1.	Itera sobre los errores en lista_errores y los formatea como objetos JSON en una estructura que describe los errores y su ubicación en el código fuente.

<image src="https://i.ibb.co/mqk3LDx/obtener-errores.png">


- ***crear_archivo_errores***

Esta función crea un archivo JSON que contiene información sobre los errores léxicos encontrados en el código fuente

<image src="https://i.ibb.co/4FYFWvG/crear-archivo-errores.png">