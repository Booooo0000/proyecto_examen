print("Programa 19. Calcula la compra de 5 artículos \n")

def Programa19():
    valor1 = float(input("Precio del artículo 1: "))
    valor2 = float(input("Precio del artículo 2: "))
    valor3 = float(input("Precio del artículo 3: "))
    valor4 = float(input("Precio del artículo 4: "))
    valor5 = float(input("Precio del artículo 5: "))

    total1 = valor1 + valor2 + valor3 + valor4 + valor5
    total2 = total1 * 1.07
    promedio = total1 / 5

    RD1 = round(total1, 2)
    RD2 = round(total2, 2)
    RD3 = round(promedio, 2)

    print("El total 1 es:", RD1)
    print("El total 2 es:", RD2)
    print("El promedio es:", RD3)

    print("\nFinal del Programa")

Programa19()
