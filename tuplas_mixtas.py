colores = "Rojo", "Azul", "Amarillo"
mixta = 10, "Valor", True, colores #Una tupla puede contener otras tuplas

print(f"Rebanadas: {mixta[2:4]}") #Se pueden usar rebanadas
print(f"Primer valor de la tupla: {mixta[0]}")
print(f"Acceder a valores de la tupla colores: {mixta[3][1]}")

print()

for variable in mixta: #Se puede iterar con un ciclo
    print(variable, end=" ")

print("\n\n")

color1, color2, color3 = colores #Desempaquetado
print(color1, color2, color3)

pintura = (color3, color2, color1) #Empaquetado
print(pintura)

numeros = 1, 20, 1, 3, 10

#funciones y metodos
print(f"Longitud: {len(numeros)}")
print(f"Maximo: {max(numeros)}")
print(f"Minimo: {min(numeros)}")
print(f"Sumatoria: {sum(numeros)}")
print(f"Donde se ubica el 3: {numeros.index(3)}")
print(f"Cuantos 1 hay: {numeros.count(1)}")

