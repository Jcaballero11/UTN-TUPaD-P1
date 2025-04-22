def calcular_promedio(a,b,c):
    return (a + b + c) / 3

# Solicitar los tres números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Calcular el promedio usando la función
promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio de los tres números es: {promedio:.2f}")
