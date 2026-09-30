nfilas= 3
ncolumnas= 3

matriz1 =[[0 for columna in range (ncolumnas)]for fila in range (nfilas)]
matriz2 =[[0 for columna in range (ncolumnas)]for fila in range (nfilas)]
suma= [[0 for columna in range (ncolumnas)]for fila in range (nfilas)]

numero = 1

for fila in range(nfilas):
    for columna in range(ncolumnas):
        matriz1[fila][columna] = numero
        numero += 1

numero = 1

for fila in range(nfilas):
    for columna in range(ncolumnas):
        matriz2[fila][columna] = numero
        numero += 2

for fila in range(nfilas):
    for columna in range(ncolumnas):
        suma[fila][columna] = matriz1[fila][columna] + matriz2[fila][columna]


for fila in range (nfilas):
    for columna in range (ncolumnas):
        print(matriz1[fila][columna], end= " ")
    print ()

for fila in range (nfilas):
    for columna in range (ncolumnas):
        print(matriz2[fila][columna], end= " ")
    print ()

for fila in range (nfilas):
    for columna in range (ncolumnas):
        print(suma[fila][columna], end= " ")
    print ()

print("Ejercicio 2")
# Crea una función que genere una matriz identidad de tamaño n × n

def matriz_id(n):
    matriz = [[0 for columna in range (n)]for fila in range (n)] 
    for fila in range(n):
        for columna in range(n):
            if fila == columna:
                matriz[fila][columna] = 1

    return matriz

n = int(input("a: "))
matriz_ide = matriz_id(n)

for fila in range (n):
    for columna in range (n):
        print(matriz_ide[fila][columna], end= " ")
    print ()

print("Ejercicio3")
# Dada una matriz de m × n, genera su transpuesta e imprímela.

ncolumnas1 = int(input("columnas: "))
nfilas1 = int(input("filas: "))

matriza =[[0 for columna in range (ncolumnas1)]for fila in range (nfilas1)]

for fila in range(nfilas1):
    for columna in range(ncolumnas1):
        matriza[fila][columna] = int(input("Número: "))

print("matriz no trans")
for fila in range (nfilas1):
    for columna in range (ncolumnas1):
        print(matriza[fila][columna], end= " ")
    print ()


print("matriz trans")
for fila in range (ncolumnas1):
    for columna in range (nfilas1):
        print(matriza[columna][fila], end= " ")
    print ()

print("Ejercicio4")
# Implementa un programa que multiplique dos matrices de las mismas dimensiones

ncolumna = int(input("columnas: "))
nfila = int(input("filas: "))

matrix1 =[[0 for columna in range (ncolumna)]for fila in range (nfila)]
matrix2 =[[0 for columna in range (ncolumna)]for fila in range (nfila)]
mult= [[0 for columna in range (ncolumna)]for fila in range (nfila)]

numero = 1

for fila in range(nfila):
    for columna in range(ncolumna):
        matrix1[fila][columna] = numero
        numero += 2

numero= 1

for fila in range(nfila):
    for columna in range(ncolumna):
        matrix2[fila][columna] = numero
        numero += 3

for fila in range(nfila):
    for columna in range(ncolumna):
        for c in range(ncolumna):
            mult[fila][columna] += matrix1[fila][c] * matrix2[c][columna]

print("m1")
for fila in range (nfila):
    for columna in range (ncolumna):
        print(matrix1[fila][columna], end= " ")
    print ()

print("m2")
for fila in range (nfila):
    for columna in range (ncolumna):
        print(matrix2[fila][columna], end= " ")
    print ()
print("resultado")
for fila in range (nfila):
    for columna in range (ncolumna):
        print(mult[fila][columna], end= " ")
    print()
    
print("Ejercicio5")
#Dada una matriz cuadrada, calcula la suma de su diagonal principal y su diagonal secundari

nc= int(input("lados: "))
matrizc =[[0 for columna in range (nc)]for fila in range (nc)]

numero=1 

for filai in range (nc):
    for columnaj in range (nc):
        matrizc[filai][columnaj] = numero
        numero += 2

for filai in range (nc):
    for columnaj in range (nc):
        print(matrizc[filai][columnaj], end= " ")
    print ()

sumar1= 0
sumar2=0

for filai in range(nc):
    for columnaj in range(nc):

        if filai == columnaj:
            sumar1 += matrizc[filai][columnaj]

        if filai + columnaj == nc - 1:
            sumar2 += matrizc[filai][columnaj]

print("suma pricipal: ", sumar1)
print("suma secundaria: ", sumar2)



