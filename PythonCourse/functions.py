# FUNCIONES
# print(), dir(), type()

def hello():
    print("Hello World")

def helloname(name="Persona"): #Parametro por defecto poniendo =....
    print("Hello "+name)


def perimetro(base, altura):
    perim=(base*2)+(altura*2)
    return perim    

# FUNCIONES LAMBDA - en una sola linea sin nombre

add=lambda n1, n2 : n1+n2

hello()
helloname("Alvaro")
print(perimetro(5,10))
print(add(10,5))



