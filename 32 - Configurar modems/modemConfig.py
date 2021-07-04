# Python program to demonstrate
# command line arguments
 
import sys
from modem import Modem 

if len(sys.argv) == 3:
	port = sys.argv[1]
	baud = sys.argv[2]
	modem = Modem(port=port,baud=baud)
	# 

else:
	print("Se ingresaron más argumentos de los Requeridos.\nEjemplo: \"NombreArchivo.py argumento01 argumento02\"")
