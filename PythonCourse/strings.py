myStr="Hello World"
myStr2="Hello,World"

#Ayuda de cada tipo de dato con funciones
#print(dir(myStr)) 

print(myStr)

#concatenar
print(myStr + "World")
print(f"{myStr}World") # Concatenar pero de otra forma
print("{0}World".format(myStr)) # Concatenar pero poniendo donde las llaves en la posicione n este caso 0 la palabra myStr

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace("Hello", 'Bye').upper()) #Metodos encadenados // No importa si pongo "" o '' para palabras
print(myStr.count('H')) # Me devuelve la cantidad de 'H'
print(myStr.count(' '))

print(myStr.startswith('Hello'))
print(myStr.startswith('hello'))
print(myStr.endswith('World'))

print(myStr.split()) # Separa el texto en palabras porque estan separadas por ' ' y me lo pone con una LISTA
print(myStr.split(',')) # Separa el texto en palabras porque estan separadas por ',' o cualquier tipo de caracter
print(myStr.find('o')) #buscar la letra 'o' y me duvuelve la POSICION

print(len(myStr)) #Longitud de la cadena, pero empieza desde el 0

myStr.index('e') #buscar la letra 'o' y me duvuelve la POSICION

print(myStr.isnumeric()) # ¿Es numerico?
print(myStr.isalpha()) # ¿Es alfanumerico?

#posiciones de la cadena con []
print(myStr[4])
print(myStr[-2]) #Obtener el caracter invento / empezando desde el final donde empieza en '1'