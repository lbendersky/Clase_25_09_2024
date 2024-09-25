numeros = (1, 2, 3, 4, 5) #los parentesis son opcionales
colores = "Rojo", #hay tuplas de un solo valor 
mixta = 10, "Azul", True, colores #pueden ser mixtas, incluyendo otras tuplas

#Operaciones

print(numeros)

numeros = numeros * 3 #replica una tupla

print(numeros)

numeros += 6, #concatena una tupla con otra solamente, provoca un TypeError si no

print(numeros)

print(3 in numeros) #Verifica si 3 se encuentra en la tupla devuelve un valor booleano
print(10 not in numeros) #verifica si 10 no esta en la tupla devuelve un valor booleano
