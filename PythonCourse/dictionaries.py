#Diccionarios con key:items

#Se podrian hacer listas de listas [[],[]] pero es mas sensilo con diccionarios
Producto = {
    "Nombre":"Libro",
    "Cantidad":3 ,
    "Precio":7.5
}

Persona = {
    "Nombre":"Alvaro",
    "Apellido":"Lopez"
}

print(Producto)
print(Persona)

#print(dir(Producto))
print(Persona.items())

#Limpiar diccionario
Persona.clear()

#lista de productos formado por diferentes diccionarios
Productos = [
    {"Nombre":"Libro", "Precio":7.5},
    {"Nombre":"Comida", "Precio":8}
]

print(Productos)