print("Programa 28. Evalúa calificaciones\n")

def Programa28():
    nota = int(input("Ingrese la nota:"))

    if nota >= 90 and nota <= 100:
        print("La letra correspondiente es A")
    
    elif nota >= 80 and nota <= 89:
        print("La letra correspondiente es B")

    elif nota >= 70 and nota <= 79:
        print("La letra correspondiente es C")
    
    elif nota >= 60 and nota <= 69:
        print("La letra correspondiente es D")
    
    else:
        print("La nota correspondiente es F")

    print("\nFinal del programa")

Programa28()
