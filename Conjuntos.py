conjunto_mixto = {1, "Valor", "Objeto"}
print(conjunto_mixto) 

#Metodos

conjunto_mixto.add(300)
print(conjunto_mixto)

conjunto_mixto.remove(1)
print(conjunto_mixto)

conjunto_mixto.discard(1)
print(conjunto_mixto)

conjunto_mixto.discard("Valor")
print(conjunto_mixto)

conjunto_mixto.clear()
print(conjunto_mixto)

print()

conjunto = {1, 2, 3, 4, 10} #sin repetidos
conjunto2 = {5, 4, 2, 6}

conjunto_ej = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}

if conjunto.issubset(conjunto_ej):
    print("Esta en el conjunto")

print()

#Funciones y operadores

print(f"Longitud: {len(conjunto)}")
print(f"Maximo: {max(conjunto)}")
print(f"Minimo: {min(conjunto)}")
print(f"Sumatoria: {sum(conjunto)}")
print(f"Esta tres en el conjunto?: {3 in conjunto}")
print(f"No esta 19 en el conjunto?: {19 not in conjunto}")

#Operaciones entre conjuntos

print()

interseccion = conjunto&conjunto2
print(interseccion) #Solo 2 y 4 pertenecen a ambos conjuntos

union = conjunto|conjunto2
print(union) #Todos los elementos de ambos conjuntos sin repetir

resta = conjunto-conjunto2
print(resta) #2 y 4 desaparecen del conjunto llamado "conjunto"

diferencia_simetrica = conjunto^conjunto2
print(diferencia_simetrica) #Se muestran todos los valores no compartidos, siendo estos 2 y 4

print()

#Conversion de datos

conjunto_a_lista = list(conjunto)
print(conjunto_a_lista)

lista_a_tupla = tuple(conjunto_a_lista)
print(lista_a_tupla)

tupla_a_conjunto = set(lista_a_tupla)
print(tupla_a_conjunto)