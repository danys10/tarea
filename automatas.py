#marcoa ntonio lopez avelizapa
#rubicelia montiel juarez
#olga cordero grijalva
#daniel alberto velasco valerio
#cesar antonio garcia tolentino

edges={
		(1,'a'):2,
		(1,'b'):3,
		(2,'a'):2,
		(2,'b'):3,
		(3,'a'):4,
		(3,'b'):3
	}

final = [2,4];

def quintupla(string, current, edges, final):
	if string == "":
		return current in final
	else:
		letter = string[0]
		if (current, letter)in edges:
			destination = edges[(current, letter)]
			siguiente = string[1:]
			return quintupla(siguiente,destination,edges,final)
		else :
			return False

while True:
	print("")
	cadena = raw_input("ingrese el lenguaje a evaluar  -->  ")
	print("")			
	print(quintupla(cadena,1,edges,final))
	print("")
	var1 = input("si desea traducir ingrese 2 sino otro numero -->  ")
	
	if (var1 == 2):
		if (quintupla(cadena,1,edges,final) == True):
			print("")
			print("cadena aceptada =D")
			print("")
		else:
			print("")
			print("cadena no aceptada ='( ")
			print("")
	else:
		break
	var2 = input("si desea continuar ingrese 2, sino otro numero -->  ")	
	if var2 != 2: break

print("")
print("adios ")
