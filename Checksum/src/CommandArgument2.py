# Python program to demonstrate
# command line arguments
 
import sys
 
# total arguments
if len(sys.argv) == 2:
	var = sys.argv[1]
	print(var)
else:
	print("Se ingresaron más argumentos de los Requeridos.\nEjemplo: \"NombreArchivo.py argumento01\"")
