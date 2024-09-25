colores = "Rojo", "Azul", "Amarillo"
mixta = 10, "Valor", True, colores

print(mixta[2:4])
print(mixta[0])
print(mixta[3][1])

print()

for variable in mixta:
    print(variable, end=" ")

print("\n\n")

color1, color2, color3 = colores
print(color1, color2, color3)

pintura = (color3, color2, color1)
print(pintura)

numeros = 1, 20, 1, 3, 10

#funciones y metodos
print(f"Longitud: {len(numeros)}")
print(f"Maximo: {max(numeros)}")
print(f"Minimo: {min(numeros)}")
print(f"Sumatoria: {sum(numeros)}")
print(f"Donde se ubica el 3: {numeros.index(3)}")
print(f"Cuantos 1 hay: {numeros.count(1)}")

