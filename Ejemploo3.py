# Función para calcular el área de un rectángulo
def area_rectangulo(lado1, lado2):
    area_rect= lado1 * lado2
    return area_rect

# Función para calcular el área de un triángulo
def area_triangulo(base, altura):
    area_triang = 0.5 * base * altura
    return area_triang

# Función principal
if __name__ == "__main__":
    print("\n--AREA DEL RECTÁNGULO--")
    L1 = float(input("Ingrese la medida del lado 1 del rectángulo: "))
    L2 = float(input("Ingrese la medida del lado 2 del rectángulo: "))
    area1 = area_rectangulo(L1, L2)
    print(f"El área del rectángulo es: {area1}")

    print("\n--AREA DEL TRIÁNGULO--")
    base = float(input("Ingrese la medida de la base del triángulo: "))
    altura = float(input("Ingrese la medida de la altura del triángulo: "))
    area2 = area_triangulo(base, altura)
    print(f"El área del triángulo es: {area2}")

