from clases_abstractas.abstract import Expresion
import math
from math import *

class operaciones_trigonometricas(Expresion):

    def __init__(self, left, tipo, fila, columna):
        self.left = left
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        valor_izquierdo = ''
        if self.left != None:
            valor_izquierdo = self.left.operar(arbol)
        if self.tipo.operar(arbol) == 'seno':
            resultado = math.sin(math.radians(valor_izquierdo))
            resultado = round(resultado, 2)
            return resultado
        elif self.tipo.operar(arbol) == 'coseno':
            resultado = math.cos(math.radians(valor_izquierdo))
            resultado = round(resultado, 2)
            return resultado
        elif self.tipo.operar(arbol) == 'tangente':
            resultado = math.tan(math.radians(valor_izquierdo))
            resultado = round(resultado, 2)
            return resultado
        elif self.tipo.operar(arbol) == 'inverso':
            resultado = 1/valor_izquierdo
            resultado = round(resultado, 3)
            return resultado
        else:
            return None

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
