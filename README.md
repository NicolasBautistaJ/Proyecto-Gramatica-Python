# Proyecto-Gramatica-Python


## Integrantes= Sara Romero y Nicolas Bautista

Ejecucion

El programa puede ser ejecutado tanto por consola como leyendo las instrucciones desde un archivo de texto

Para ejecutarlo por consola es necesario ejecutar estos comandos:

Para cargar la gramatica:

antlr4 -Dlanguage=Python3 -visitor calculadora.g4

Para ejecutar el programa:

python3 main.py


Por otro lado para ejecutar desde un archivo de texto se utilizan estos comandos:

Para cargar la gramatica:

antlr4 -Dlanguage=Python3 -visitor calculadora.g4

Para ejecutar el programa con el nombre del archivo desde el que se leeran las instrucciones:

python3 main.py NOMBRE DEL ARCHIVO

En este caso existen dos archivo el primero prueba las uncionalidades de la gramatica el cual es ejemplo.txt y el otro es el que tiene la solucion a la sustenacion el cual se llama sustentacion.txt

### Nota= Para ejecutar los programas es necesario tener instaladas en el entorno de desarrollo todos los elementos que se importaron en el archivo main
