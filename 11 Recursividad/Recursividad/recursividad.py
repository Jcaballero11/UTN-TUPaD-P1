#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario un número entero positivo
num = int(input("Introduce un número entero positivo: "))

# Calcular e imprimir el factorial de todos los números del 1 al num
for i in range(1, num + 1):
    print(f"Factorial de {i} es {factorial(i)}")

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar al usuario la posición hasta la cual mostrar la serie
n = int(input("Introduce la posición hasta la cual mostrar la serie de Fibonacci: "))

# Mostrar la serie de Fibonacci hasta la posición n
print("Serie de Fibonacci:")
for i in range(n + 1):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛
#𝑚 = 𝑛 ∗ 𝑛
#(𝑚−1)
#. Prueba esta función en un 
#algoritmo general.
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Solicitar datos al usuario
base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente (entero no negativo): "))

resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es igual a {resultado}")

#4) Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto.
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Solicitar un número entero positivo al usuario
numero = int(input("Introduce un número entero positivo: "))

# Validar que el número sea positivo
if numero < 0:
    print("Por favor, introduce un número entero positivo.")
elif numero == 0:
    print("La representación binaria de 0 es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"La representación binaria de {numero} es: {binario}")

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
#lo es.
# Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().
def es_palindromo(palabra):
    #si la palabra tiene 0 o 1 letra, es un palíndromo
    if len(palabra) <= 1:
        return True
    # Si los extremos no coinciden, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Introduce una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(texto):
    print(f"'{texto}' es un palíndromo.")
else:
    print(f"'{texto}' no es un palíndromo.")

