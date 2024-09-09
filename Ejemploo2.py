def calcular(num1, num2, num3):
    resultado = num1 * num2 + num3
    return resultado

if __name__ == "__main__":
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    n3 = float(input("Ingrese el tercer número: "))
    resultado = calcular(n1, n2, n3)
    print(f"El resultado de {n1} * {n2} + {n3} es: {resultado}")


