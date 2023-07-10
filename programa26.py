print("Programa 26. Clasificación de Triángulos\n")

def Programa26():
    verticeA = float(input("Ingrese la longitud del primer vértice: "))
    verticeB = float(input("Ingrese la longitud del segundo vértice: "))
    verticeC = float(input("Ingrese la longitud del tercer vértice: "))

    if verticeA == verticeB == verticeC:
        print("El triángulo es equilátero")
    elif verticeA == verticeB or verticeA == verticeC or verticeB == verticeC:
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")

    print("\nFinal del Programa")

Programa26()


