from clases_abstractas.abstract import Expresion

class operaciones_aritmeticas(Expresion):
    def __init__(self, left, right, tipo, fila, columna):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        valor_izquierdo = ''
        valor_derecho = ''

        if self.left != None:
            valor_izquierdo = self.left.operar(arbol)
        if self.right != None:
            valor_derecho = self.right.operar(arbol)

        if self.tipo.operar(arbol) == 'suma':
            resultado = valor_izquierdo+valor_derecho
            return resultado
        elif self.tipo.operar(arbol) == 'resta':
            resultado = valor_izquierdo - valor_derecho
            return resultado
        elif self.tipo.operar(arbol) == 'multiplicacion':
            resultado = valor_izquierdo * valor_derecho
            return resultado
        elif self.tipo.operar(arbol) == 'division':
            resultado = valor_izquierdo / valor_derecho
            return resultado
        elif self.tipo.operar(arbol) == 'modulo':
            resultado = valor_izquierdo % valor_derecho
            return resultado
        elif self.tipo.operar(arbol) == 'potencia':
            resultado = valor_izquierdo ** valor_derecho
            return resultado
        elif self.tipo.operar(arbol) == 'raiz':
            resultado = valor_izquierdo ** (1/valor_derecho)
            return resultado
        elif self.tipo.operar(arbol) == 'inverso':
            resultado = 1/valor_izquierdo
            return resultado
        else:
            return None

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()