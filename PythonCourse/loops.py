################## FOR ###################

# LISTAS

foods=['apples', 'bread', 'cheese']

#print(foods[0])
#print(foods[1])
#print(foods[2])


#for foods in foods: # Recorrer cada uno de los elementos de foods
#    print(foods)

for foods in foods: # Recorrer lista con condiciones
    if foods=='apples':
        print('You have to buy this')
    else:
        print(foods, end=" ")    


# Para romper el bucle poner break 
# # Para continuar en el bucle y que pase a la siguiente iteracion poner continue        

# NUMEROS

for number in range(1, 8):
    print(number)

# STRINGS

for letter in "Hello":
    print(letter)


################## WHILE ###################

count = 1
while count <= 6:
    print(count)
    count=count+1
