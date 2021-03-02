# Python program to demonstrate
# command line arguments
 
import sys
 

if len(sys.argv) == 2:
	
	Data = sys.argv[1]
	print("Dato de ingreso: ", Data)
	#print(len(Data))
	Acumulador = ord(Data[0])
	for element in range(0, len(Data)): 
		if element + 1 < len(Data):
			#print("element: ",element)
			aux1 = Data[element + 1]
			Acumulador ^= ord(aux1)
	
	#print("Resultado", Acumulador)
	#print(hex(Acumulador))
	temp = hex(Acumulador)
	
	#print(Data + temp[2:len(temp)])
	if len(temp[2:len(temp)]) == 1:
		print("$" + Data + "*" + "0" + temp[2:len(temp)])
	else:
		print("$" + Data + "*" + temp[2:len(temp)])
	
else:
	print("Se ingresaron más argumentos de los Requeridos.\nEjemplo: \"NombreArchivo.py argumento01\"")
