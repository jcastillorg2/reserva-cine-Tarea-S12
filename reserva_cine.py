# Programa para reservar un asiento en una sala de cine
# La sala tiene 3 filas y 4 columnas.
# 0 = asiento libre
# 1 = asiento reservado

# Crear una matriz de 3 filas por 4 columnas,
# con todos los asientos inicialmente libres.
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Solicita al usuario la fila del asiento que desea reservar.
fila = int(input("Ingrese la fila (0 a 2): "))

# Solicita al usuario la columna del asiento que desea reservar.
columna = int(input("Ingrese la columna (0 a 3): "))

# Marca el asiento seleccionado como reservado.
asientos[fila][columna] = 1

# Muestra el estado completo de la sala.
print("\nEstado de la sala:")

# Recorre las filas de la matriz.
for i in range(3):

    # Recorre las columnas de cada fila.
    for j in range(4):
        print(asientos[i][j], end=" ")

    # Muestra la información en pantalla.
    print()
