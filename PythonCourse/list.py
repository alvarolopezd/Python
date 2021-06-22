#Si creo una nueva lista se puede hacer con [] o con list((tupla)) si es una lista nueva
myList=["hola", 10, True, [1, 2]]#Se puede guardar una lista dentro de otra lista
print(myList)

myList=list(("hola", 10, True, [1, 2]))#Se puede guardar una lista dentro de otra lista
print(myList)

#Asignar los valores de una lista a otra variable lista con comnado list(())
newList=list(myList) 
print(newList)
newList=list((1,2,3,4)) 
print(newList)

#escribir rangos de listas
newList=list((range(1,10)))
print(newList)


print(dir(myList))

print(len(myList))


print(myList[1]) #Obtener la posicion de una lista, la lista empieza desde 0
print('hola'in myList)
print(5 in myList)

#Modificar partes de la lista
myList[1]='Hello'
print(myList)

#Agregar elementos a la lista
myList.append('violeta')
print(myList)

#Agregar varios elementos (con append no se puede poruqe se agrega una dupla o da error. No se quiere dupla)
myList.extend(('violet','yellow'))
print(myList)

myList.extend(['grey','red'])
print(myList)

# Insertar elementos donde yo quiera
myList.insert(len(myList),'blue') #ponerlo al final o poner -1 o en la posicion que quiera
print(myList)

#Eliminar ultimo elementos de la lista
myList.pop()
print(myList)

#Eliminar un elemento que yo inserte
myList.remove('yellow')
print(myList)

myList.pop(2)
print(myList)

#limpiar la lista
#myList.clear()
#print(myList)

#myList.sort(reverse=True)

print(myList)

print(myList.index('violet'))
