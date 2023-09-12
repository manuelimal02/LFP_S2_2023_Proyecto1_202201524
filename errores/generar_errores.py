from clases_abstractas.abstract import Expresion

class Errores(Expresion):
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)
    def operar(self, no):
        no_ = f'\t\t"no.":{no}'+','+'\n'
        desc = '\t\t"descripcion":{\n'
        lex = f'\t\t\t"lexema": "{self.lexema}"'+','+'\n'
        tipo = '\t\t\t"tipo": "error lexico"'+','+'\n'
        columna = f'\t\t\t"columna": {self.columna}'+','+'\n'
        fila = f'\t\t\t"fila": {self.fila}\n'
        fin = "\t\t}\n"
        return '\t{\n' + no_ + desc + lex + tipo + columna + fila + fin + '\t}'
    def getColumna(self):
        return super().getColumna()
    def getFila(self):
        return super().getFila()
