from antlr4 import *
import sys
import argparse
import split
from antlr4 import FileStream, InputStream, CommonTokenStream
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from calculadoraLexer import calculadoraLexer
from calculadoraParser import calculadoraParser
from calculadoraVisitor import calculadoraVisitor
from math import sin, cos, tan, radians
from collections import Counter

class EvalVisitor(calculadoraVisitor):
    def __init__(self):
        self.memory = {}
        self.functions = {
            'euclides': (['a', 'b'], self.euclides)
        }
        
    # Funcion encargada de calcular la euclidiana
    def euclides(self, a, b):
        return euclides(a, b)

    # Funcion encargada de imprimir
    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        if isinstance(value, np.ndarray):
            formatted_matrix = np.array2string(value, separator=', ', formatter={'float_kind': lambda x: "%.2f" % x})
            print(formatted_matrix.replace('\n', ''))
        else:
            print(value)
        return value

    # Funcion encargada de reconocer parentesis
    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    # Funcion encargada de asignar varibales
    def visitAssign(self, ctx):
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id] = value
        return value

    # Funcion encargada de realizar potenciacion
    def visitPower(self, ctx):
        base = self.visit(ctx.expr(0))
        exponent = self.visit(ctx.expr(1))
        return base ** exponent

    # Funcion encargada de realzar la multiplicacion y division
    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if isinstance(left, np.ndarray) and isinstance(right, np.ndarray):
            if ctx.op.type == calculadoraParser.MUL:
                return np.matmul(left, right)
            else:
                sys.exit("División de matrices no soportada")
        elif isinstance(left, np.ndarray) or isinstance(right, np.ndarray):
            if ctx.op.type == calculadoraParser.MUL:
                return left * right
            else:
                return left / right
        else:
            if ctx.op.type == calculadoraParser.MUL:
                return left * right
            else:
                return left / right

    # Funcion encargada de realizar la suma y resta
    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if isinstance(left, np.ndarray) or isinstance(right, np.ndarray):
            return np.add(left, right) if ctx.op.type == calculadoraParser.ADD else np.subtract(left, right)
        if ctx.op.type == calculadoraParser.ADD:
            return left + right
        else:
            return left - right

    # Funcion encargada de calcular la raiz 
    def visitRoot(self, ctx):
        base = self.visit(ctx.expr(0))
        exponent = self.visit(ctx.expr(1))
        return base ** (1/exponent)

    # Funcion encargada de calcular el residuo
    def visitMod(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left % right

    # Funcion encargada de reconocer enteros
    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    # Funcion encargada de reconocer flotantes
    def visitFloat(self, ctx):
        return float(ctx.FLOAT().getText())

    # Funcion encargada de reconocer string
    def visitString(self, ctx):
        return ctx.STRING().getText()[1:-1]

    # Funcion encargada de reconocer ID
    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        else:
            raise Exception(f"Undefined variable '{name}'")

    # Funcion encargada de reconocer booleanos
    def visitBool(self, ctx):
        text = ctx.getText().lower()
        if text == 'true':
            return True
        elif text == 'false':
            return False
        else:
            sys.exit(f"Invalid boolean value: {text}")

    # Funcion encargada de reconocer operadores unarios
    def visitUnary(self, ctx):
        expr_value = self.visit(ctx.expr())
        if ctx.getChild(0).getText() == '-':
            return -expr_value
        elif ctx.getChild(0).getText() == '!':
            if isinstance(expr_value, bool):
                return not expr_value
            else:
                sys.exit("Operador '!' solo se puede aplicar a booleanos")

    # Funcion encargada de realizar la negacion booleana
    def visitNegacion(self, ctx):
        expr_value = self.visit(ctx.expr())
        if isinstance(expr_value, bool):
            return not expr_value
        else:
            sys.exit("Operador '!' solo se puede aplicar a booleanos")

    # Funcion encargada de calcular incremento
    def visitIncrement(self, ctx):
        return self.visit(ctx.expr()) + 1

    # Funcion encargada de calcular decremento
    def visitDecrement(self, ctx):
        return self.visit(ctx.expr()) - 1

    # Funcion encargada de realizar la funcion seno
    def visitSinFunction(self, ctx):
        expr_value = self.visit(ctx.expr())
        return sin(radians(expr_value))

    # Funcion encargada de realizar la funcion coseno
    def visitCosFunction(self, ctx):
        expr_value = self.visit(ctx.expr())
        return cos(radians(expr_value))

    # Funcion encargada de realizar la funcion tangente
    def visitTanFunction(self, ctx):
        expr_value = self.visit(ctx.expr())
        return tan(radians(expr_value))

    # Funcion encargada de reconocer matrices
    def visitMatrix(self, ctx):
        matrix_values = []
        for row_ctx in ctx.matrix_contents().row():
            row_values = [self.visit(expr) for expr in row_ctx.expr()]
            matrix_values.append(row_values)
        return np.array(matrix_values)

    # Funcion encargada de realizar la transpuesta
    def visitTransposeExpr(self, ctx):
        matrix = self.visit(ctx.expr())
        return matrix.T

    # Funcion encargada de realizar la inversa
    def visitInverseExpr(self, ctx):
        matrix = self.visit(ctx.expr())
        try:
            return np.linalg.inv(matrix)
        except np.linalg.LinAlgError:
            sys.exit("Error: La matriz no es invertible.")
            return None

    # Funcion encargada de reconocer bucles for
    def visitForStat(self, ctx):
        var_name = ctx.ID().getText()
        start_value = self.visit(ctx.expr(0))
        end_value = self.visit(ctx.expr(1))
        for i in range(start_value, end_value + 1):
            self.memory[var_name] = i
            for stat_ctx in ctx.stat():
                self.visit(stat_ctx)
        return None

    # Funcion encargada de reconocer operadores de comparacion
    def visitComparison(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == calculadoraParser.EQ:
            return left == right
        elif ctx.op.type == calculadoraParser.NEQ:
            return left != right
        elif ctx.op.type == calculadoraParser.LT:
            return left < right
        elif ctx.op.type == calculadoraParser.GT:
            return left > right
        elif ctx.op.type == calculadoraParser.LE:
            return left <= right
        elif ctx.op.type == calculadoraParser.GE:
            return left >= right
        else:
            sys.exit(f"Operador de comparación no soportado: {ctx.op.type}")

    # Funcion encargada de reconocer condicionales 
    def visitIfStat(self, ctx):
        condition = self.visit(ctx.expr())
        if condition:
            if hasattr(ctx, 'stat') and isinstance(ctx.stat(0), list):
                for stat_ctx in ctx.stat(0):
                    self.visit(stat_ctx)
            else:
                self.visit(ctx.stat(0))
        elif ctx.stat(1) is not None:
            if hasattr(ctx, 'stat') and isinstance(ctx.stat(1), list):
                for stat_ctx in ctx.stat(1):
                    self.visit(stat_ctx)
            else:
                self.visit(ctx.stat(1))
        return None

    # Funcion encargada de reconocer bucles while
    def visitWhileStat(self, ctx):
        while True:
            for stat_ctx in ctx.stat():
                self.visit(stat_ctx)
            if not self.visit(ctx.expr()):
                break
        return None

    # Funcion encargada de realizar impresiones
    def visitPrint(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return value

    # Funcion encargada de reconocer listas
    def visitList(self, ctx):
    	list_values = []
    	if ctx.list_contents() is not None:
        	list_values = self.visit(ctx.list_contents())
    	return list_values

    # Funcion encargada de revisar el contenido de la lista
    def visitList_contents(self, ctx):
    	return [self.visit(expr) for expr in ctx.expr()]

    # Funcion encargada de añadir elementos a la lista
    def visitListAppend(self, ctx):
        list_obj = self.visit(ctx.expr(0))
        value_to_append = self.visit(ctx.expr(1))
        if isinstance(list_obj, list):
            list_obj.append(value_to_append)
        else:
            sys.exit("La operación append solo se puede aplicar a listas.")
        return list_obj

    # Funcion encargada de eliminar elementos de la lista
    def visitListRemove(self, ctx):
        list_obj = self.visit(ctx.expr(0))
        value_to_remove = self.visit(ctx.expr(1))
        if isinstance(list_obj, list):
            list_obj.remove(value_to_remove)
        else:
            sys.exit("La operación remove solo se puede aplicar a listas.")
        return list_obj

    # Funcion encargada de calcular el tamaño de la lista
    def visitListLen(self, ctx):
        list_obj = self.visit(ctx.expr())
        if isinstance(list_obj, list):
            return len(list_obj)
        else:
            sys.exit("La operación len solo se puede aplicar a listas.")

    # Funcion encargada de visitar el indice de la lista
    def visitListIndex(self, ctx):
        list_obj = self.visit(ctx.expr(0))
        value_to_find = self.visit(ctx.expr(1))
        if isinstance(list_obj, list):
            try:
                return list_obj.index(value_to_find)
            except ValueError:
                sys.exit(f"El valor {value_to_find} no se encuentra en la lista.")
        else:
            sys.exit("La operación index solo se puede aplicar a listas.")

    # Funcion encargada de eliminar la lista
    def visitListPop(self, ctx):
        list_obj = self.visit(ctx.expr())
        if isinstance(list_obj, list):
            return list_obj.pop()
        else:
            sys.exit("La operación pop solo se puede aplicar a listas.")

    # Funcion encargada de reconocer tuplas
    def visitTupla(self, ctx):
    	tuple_values = []
    	if ctx.list_contents() is not None:
        	tuple_values = tuple(self.visit(expr) for expr in ctx.list_contents().expr())
    	return tuple_values


    # Funcion encargada de reconocer diccionarios
    def visitDicti(self, ctx):
        dict_values = {}
        if ctx.dict_contents() is not None:
            for entry_ctx in ctx.dict_contents().dict_entry():
                key = self.visit(entry_ctx.expr(0))
                value = self.visit(entry_ctx.expr(1))
                dict_values[key] = value
        return dict_values

    # Funcion encargada de acceder al diccionarios
    def visitDictAccess(self, ctx):
    	dict_name = ctx.ID().getText()
    	key = self.visit(ctx.expr())
    	if dict_name in self.memory and isinstance(self.memory[dict_name], dict):
        	return self.memory[dict_name].get(key)
    	else:
        	sys.exit(f"La clave '{key}' no existe en el diccionario '{dict_name}' o el objeto no es un diccionario.")

    # Funcion encargada de reconocer la entrada de un diccionarios
    def visitDict_entry(self, ctx):
        key = self.visit(ctx.expr(0))
        if ctx.list() is not None:
            value = self.visit(ctx.list())
        else:
            value = self.visit(ctx.expr(1))
        return key, value

    # Funcion encargada de reconocer el contenido de un diccionario
    def visitDict_contents(self, ctx):
    	dict_values = {}
    	for entry_ctx in ctx.dict_entry():
        	key, value = self.visit(entry_ctx)
        	dict_values[key] = value
    	return dict_values


    # Funcion encargada de asignar los valores de un diccionario
    def visitAssignDict(self, ctx):
    	dict_name = ctx.ID().getText()
    	dict_values = {}
    	if ctx.dict_contents() is not None:
        	for entry_ctx in ctx.dict_contents().dict_entry():
            		key, value = self.visit(entry_ctx)
            		dict_values[key] = value
    	self.memory[dict_name] = dict_values
    	return dict_values

    # Funcion encargada de reconocer la clave de un diccionario
    def visitGetDictKey(self, ctx):
      dict_obj = self.visit(ctx.expr(0))
      key_to_find = self.visit(ctx.expr(1))
      if isinstance(dict_obj, dict):
          try:
              return [k for k, v in dict_obj.items() if v == key_to_find]
          except ValueError:
              sys.exit(f"No se encontró ninguna clave asociada al valor {key_to_find}.")
      else:
          sys.exit("La operación get_key solo se puede aplicar a diccionarios.")

    # Funcion encargada de reconocer los valores de un diccionario
    def visitGetDictValue(self, ctx):
      dict_obj = self.visit(ctx.expr(0))
      key_to_find = self.visit(ctx.expr(1))
      if isinstance(dict_obj, dict):
          return dict_obj.get(key_to_find, f"No se encontró valor para la clave {key_to_find}.")
      else:
          sys.exit("La operación get_value solo se puede aplicar a diccionarios.")

    # Funcion encargada de añadir un elemento a un diccionario
    def visitAddDictEntry(self, ctx):
      dict_obj = self.visit(ctx.expr(0))
      new_key = self.visit(ctx.expr(1))
      new_value = self.visit(ctx.expr(2))
      if isinstance(dict_obj, dict):
          dict_obj[new_key] = new_value
          return dict_obj
      else:
          sys.exit("La operación add_entry solo se puede aplicar a diccionarios.")


    # Funcion encargada de eliminar un elemento a un diccionario
    def visitRemoveDictEntry(self, ctx):
      dict_obj = self.visit(ctx.expr(0))
      key_to_remove = self.visit(ctx.expr(1))
      if isinstance(dict_obj, dict):
          try:
              del dict_obj[key_to_remove]
              return dict_obj
          except KeyError:
              sys.exit(f"No se encontró ninguna entrada con la clave {key_to_remove}.")
      else:
          sys.exit("La operación remove_entry solo se puede aplicar a diccionarios.")


    # Funcion encargada de reconocer una funcion
    def visitFunctionDef(self, ctx):
        func_name = ctx.ID().getText()
        params = [param.getText() for param in ctx.params().ID()] if ctx.params() else []
        statements = ctx.stat()
        self.functions[func_name] = (params, statements)
        return None

    # Funcion encargada de realizar el llamado de una funcion
    def visitFunctionCall(self, ctx):
        func_name = ctx.ID().getText()
        args = [self.visit(arg) for arg in ctx.args().expr()] if ctx.args() else []
        if func_name in self.functions:
            params, statements = self.functions[func_name]
            if len(params) != len(args):
                raise Exception("Argument count mismatch")

            old_memory = self.memory.copy()

            for param, arg in zip(params, args):
                self.memory[param] = arg

            result = None
            for statement in statements:
                result = self.visit(statement)
                if isinstance(result, ReturnValue):
                    result = result.value
                    break

            self.memory = old_memory
            return result
        else:
            raise Exception(f"Undefined function '{func_name}'")


    # Funcion encargada de reconocer un dataframe
    def visitDataframe(self, ctx):
        dict_contents = self.visit(ctx.expr())
        return pd.DataFrame(dict_contents)

    # Funcion encargada de mostrar la cabeza de un dataframe
    def visitDataframeHead(self, ctx):
        dataframe_obj = self.visit(ctx.expr())
        return dataframe_obj.head()

    # Funcion encargada de calcular la media de un dataframe
    def visitDataframeMean(self, ctx):
        dataframe_obj = self.visit(ctx.expr())
        return dataframe_obj.mean()

    # Funcion encargada de mostrar la descripcion de un dataframe
    def visitDataframeDescribe(self, ctx):
        dataframe_obj = self.visit(ctx.expr())
        return dataframe_obj.describe()

    # Funcion encargada de convertir un dataframe en una serie
    def visitDataframeSeries(self, ctx):
        dataframe_obj = self.visit(ctx.expr(0))
        column_to_series = self.visit(ctx.expr(1))
        return dataframe_obj[column_to_series]

    # Funcion encargada de generar un grafico de lineas para las funciones de seno coseno y tangente
    def visitGraficaLineas(self, ctx):
        dataframe_obj = self.visit(ctx.expr())
        ax=dataframe_obj.plot(figsize=(10, 6))
        plt.plot(dataframe_obj["intervalo"], dataframe_obj["seno"], label='Seno', color='blue')
        plt.plot(dataframe_obj["intervalo"], dataframe_obj["coseno"], label='Coseno', color='green')
        plt.plot(dataframe_obj["intervalo"], dataframe_obj["tangente"], label='Tangente', color='red')
        ax.set_xlim(-6, 6)
        ax.set_ylim(-2, 2)
        plt.title('Grafica lineas')
        plt.xlabel('Índice')
        plt.ylabel('Valores')
        plt.grid(True)
        return plt.show()

    # Funcion encargada de generar un grafico de barras
    def visitGraficaBarras(self, ctx):
        dataframe_obj = self.visit(ctx.expr())
        dataframe_obj.plot(kind='bar')
        plt.title('Grafica barras')
        plt.xlabel('eje x')
        plt.ylabel('eje y')
        plt.grid(axis='y')
        return plt.show()


    # Funcion encargada de generar un grafico de puntos
    def visitGraficaPuntos(self, ctx):
        dataframe_obj = self.visit(ctx.expr())
        dataframe_obj.plot(kind='scatter', x='X', y='Y', figsize=(10, 6))
        plt.title('Gráfica de Puntos')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        return plt.show()

    # Funcion encargada de generar un histograma para la palabra que ams se repite en el quijote
    def visitGraficaHistograma(self, ctx):
        dataframe_obj = self.visit(ctx.expr())

        if 'Data' in dataframe_obj.columns:
            dataframe_obj['Data'].plot(kind='hist', bins=10, color='lightgreen', edgecolor='black')
            plt.title('Histograma')
            plt.xlabel('Frecuencia de palabras')
            plt.ylabel('Número de palabras')
            plt.grid(axis='y')
            plt.show()
        else:
            print("La columna 'Data' no se encuentra en el DataFrame.")


    # Funcion encargada de generar un grafico de caja
    def visitGraficaCaja(self, ctx):
        dataframe_obj = self.visit(ctx.expr())
        dataframe_obj.plot(kind='box')
        plt.title('Gráfica de Caja')
        plt.grid(True)
        return plt.show()

    # Funcion encargada de abrir un archivo
    def visitOpenFile(self, ctx):
        file_path = self.visit(ctx.expr(0))
        mode = self.visit(ctx.expr(1))
        return open(file_path, mode)

    # Funcion encargada de modificar un archivo
    def visitWriteFile(self, ctx):
    	file_id = ctx.ID().getText()
    	content = self.visit(ctx.expr())
    	with open(file_id, 'w') as file:
        	file.write(content)
    	return print("Archivo Actualizado")

    # Funcion encargada de modificar varias lienas de un archivo
    def visitWritelinesFile(self, ctx):
    	file_id = ctx.ID().getText()
    	print(file_id)
    	lines = self.visit(ctx.expr())
    	print(lines)
    	if isinstance(lines, list):
    		with open(file_id, 'w') as file:
    			file.writelines(lines)
    	else:
            	sys.exit("Argument to 'writelines' must be a list.")

    	return print("Archivo Actualizado")

    # Funcion encargada de leer un archivo
    def visitReadFile(self, ctx):
    	file_id = ctx.ID().getText()
    	with open(file_id, 'r') as file:
    		cont=file.read()
    	return cont

    # Funcion encargada de eliminar un archivo
    def visitDeleteFile(self, ctx):
    	file_name = ctx.ID().getText()
    	os.remove(file_name)
    	return print("Archivo Eliminado")

    # Funcion encargada de cerrar un archivo
    def visitCloseFile(self, ctx):
        file_id = ctx.ID().getText()
        with open(file_id, 'w') as file:
        	file.close()
        return print("Archivo Cerrado")

    # Funcion encargada de generar un csv en base a un dataframe
    def visitCrearCsv(self, ctx):
    	dataframe_obj = self.visit(ctx.expr())
    	file_name = ctx.STRING().getText()
    	file_name = file_name.strip('"')
    	dataframe_obj.to_csv(file_name, index=False)
    	return print("CSV generado")

    # Funcion encargada de leer un csv
    def visitLeerCsv(self, ctx):
    	file_name = ctx.STRING().getText()
    	file_name = file_name.strip('"')
    	dataframe_obj = pd.read_csv(file_name)
    	self.memory[ctx.ID().getText()] = dataframe_obj
    	return dataframe_obj

    # Funcion encargada de retornar
    def visitReturn(self, ctx):
        obj = self.visit(ctx.expr())
        return obj

    # Funcion encargada de calcular el factorial de un numero
    def visitFactorial(self, ctx):
        num = int(ctx.INT().getText())
        return math.factorial(num)

    # Funcion encargada de calcular la euclidiana
    def visitEuclidesFunction(self, ctx):
        a = int(self.visit(ctx.expr(0)))
        b = int(self.visit(ctx.expr(1)))
        while b != 0:
        	a, b = b, a % b
        return a


    # Funcion encargada de calcular la palabra que mas se repite de un archivo
    def visitRepetida(self, ctx):
        texto = self.visit(ctx.expr())
        print(texto)
        contador_palabras = Counter(texto.split())
        palabras_mas_comunes = contador_palabras.most_common(10)
        frecuencias = [frecuencia for palabra, frecuencia in palabras_mas_comunes]
        df_frecuencias = pd.DataFrame(frecuencias, columns=['Data'])

        return df_frecuencias






class ReturnValue:
    def __init__(self, value):
        self.value = value

def main():

    parser = argparse.ArgumentParser(description="Ejecutar calculadora")
    parser.add_argument('archivo', nargs='?', type=str, help="Archivo de entrada", default=None)


    args = parser.parse_args()

    if args.archivo:
        print(f"Leyendo desde el archivo: {args.archivo}")

        input_stream = FileStream(args.archivo)
    else:
        print("Leyendo desde la entrada de la consola (presiona Ctrl+D para finalizar):")

        try:
            input_lines = sys.stdin.read()
        except EOFError:
            input_lines = ""
        input_stream = InputStream(input_lines)

    lexer = calculadoraLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = calculadoraParser(token_stream)
    tree = parser.prog()

    eval_visitor = EvalVisitor()


    for child in tree.children:
        try:
            eval_visitor.visit(child)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

if __name__ == '__main__':
    main()
