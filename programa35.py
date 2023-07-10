def Programa35():
    print("Programa 35. Lista de números del 1 al 10\n")
    
    for numero in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
        if numero > 5:
            print("El número", numero, "es mayor a 5")
        elif numero <= 0:
            print("El número", numero, "es menor o igual a cero")
        else:
            print("El número", numero, "es menor o igual que 5")
        if numero == 9:
            break

    print("\nFinal del programa")

Programa35()