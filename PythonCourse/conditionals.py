edad=input("Introduce la edad: ")

if int(edad)<=30:
    print("La edad es menor o igual a 30")
else:
    print("La edad es mayor que 30")

if int(edad)<30 and int(edad)>15:
    print("Estas en la juventud")

#Se pueden usar and, or, not


color=input("Introduce un color")
if color=="azul":
    print("El colo es el azul")
elif color=="verde":
    print("El color es el verde")
else:
    print("Se desconoce el color introducido")    


