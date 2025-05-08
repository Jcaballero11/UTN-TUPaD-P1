#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    return f"Hola {nombre}"

def principal():
    nombre= input("Ingresa tu nombre: ")
    print(saludar_usuario(nombre))

principal()

#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.
def imprimir_hola_mundo():
    return "Hola Mundo"

def principal():
    print(imprimir_hola_mundo())

principal()

#3.Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido):
    print(f"Soy {nombre}{apellido}")

# Programa principal
# Solicitar los datos al usuario
nombre_usuario = input("Ingrese su nombre: " )
apellido_usuario = input("Ingrese su apellido: ")

# Llamar a la función con los valores ingresados
informacion_personal(nombre_usuario, apellido_usuario)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.
PI = 3.14

def cal_area_cir(radio):
    return PI * radio ** 2

def cal_per_cir(radio):
    return 2 * PI * radio

#solicitar el radio al usuario
radio_usuario = float(input("Ingrese el radio del circulo: "))

#calcular el area y perimetro
area = cal_area_cir(radio_usuario)
perimetro = cal_per_cir(radio_usuario)

print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.
# Función que convierte segundos a horas
def seg_a_horas(segundos):
    return segundos / 3600

# Solicitar la cantidad de segundos al usuario
seg_ingresados = float(input("Ingrese la cantidad de segundos: "))

# Calcular las horas usando la función
horas = seg_a_horas(seg_ingresados)

print(f"{seg_ingresados} segundos equivalen a {horas:.2f} horas")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_mult(numero):
    print(f"Tabla de multiplicar del {numero}")
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero_usuario = int(input("Ingrese el numero que desea saber: "))

tabla_mult(numero_usuario)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b

    if b!= 0:
        division = a / b
    else:
        division = "No se puede dividir por 0"
    return (suma, resta, multiplicacion, division)

# Solicitar los números al usuario
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))

# Llamar a la función
resultados = operaciones_basicas(a,b)

print(f"\nResultados de las operaciones con {a} y {b}:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
#ción para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Solicitar datos al usuario
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

# Calcular el IMC
imc = calcular_imc(peso, altura)

print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Pedir al usuario la temperatura en Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Calcular la temperatura en Fahrenheit
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.
def calcular_promedio(a,b,c):
    return (a + b + c) / 3

# Solicitar los tres números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Calcular el promedio usando la función
promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio de los tres números es: {promedio:.2f}")