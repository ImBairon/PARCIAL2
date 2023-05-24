def calcular_cuadrados(n):
    suma = 0
    for i in range(1, n+1):
        suma += (2*i - 1)
        cuadrado = suma
        print("Número =", i)
        print("Cuadrado =", cuadrado)
        print("Método =", '+'.join(str(2*j - 1) for j in range(1, i+1)))
        print()

n = int(input("Ingrese el valor de n: "))
calcular_cuadrados(n)
