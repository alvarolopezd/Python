# Datos que no van a cambiar,
#Se usan por ejemplo para diccionarios, para elementos que no van a cambiar nunca

#Se pueden crear con () o con un contrudctor tuple(())
myTuple=(1,2,3, 'Enero', 'Febrero', 'Marzo') #En el caso tupla de 1 solo elemento es necesairo poner la coma tuple(1,)
print(myTuple)
print(type(myTuple))

newTuple=tuple((3,2,1))
print(newTuple)

#print(dir(myTuple))

#Acceder a elementos de la tupla
print(myTuple[2])

#Eliminar la tupla
#del myTuple