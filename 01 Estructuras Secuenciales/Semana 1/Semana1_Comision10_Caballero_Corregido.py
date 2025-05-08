#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  
print("Hola Mundo");

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
#realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ");
print(f"Hola {nombre}!");
# Otra alternativa sin usar printf sería
print("Hola " + nombre + "!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla. 
nombre = input("Ingrese su nombre: ");
apellido = input("Ingrese su apellido: ");
edad = input("Ingrese su edad: ");
lugar = input("Ingrese su lugar de residencia: ");
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}");

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro.
radio = float(input("Ingrese el radio del círculo: "));
area = 3.14159 * (radio ** 2);
perimetro = 2 * 3.14159 * radio;
print(f"El área del círculo es {area} y su perímetro es {perimetro}")

#Al principio del programa necesitamos importar la librería math ya que la necesitaremos para utilizar el número pi
import math
#radio = float(input("Ingrese el radio del círculo: "));
#area_circulo = math.pi * (radio_circulo)**2
#perimetro_circulo = 2 * math.pi * radio_circulo
#sprint(f"El área del círculo es de {area_circulo} y el perímetro es de {perimetro_circulo}.")

# El resultado anterior tiene demasiados decimales, podemos usar la
# función round para redondear a 2 decimales Al principio del programa
# necesitamos importar la librería math ya que la necesitaremos para
# utilizar el número pi
import math
# Empezamos pidiendo al usuario que ingrese el radio del circulo y almacenando su respuesta en la variable "radio_circulo"
# Como usaremos el radio para cálculos matemáticos necesitamos que el valor ingresado sea un tipo de dato float, por lo que hacemos la conversión al declarar la variable
radio_circulo = float(input("Por favor, ingrese el radio del círculo: "))
# Realizamos el cálculo del área del círculo
area_circulo = round(math.pi * (radio_circulo)**2, 2)
# Realizamos el cálculo del perímetro del círculo
perimetro_circulo = round(2 * math.pi * radio_circulo, 2)
# Imprimimos ambos resultados por pantalla
print(f"El área del círculo es de {area_circulo} y el perímetro es de {perimetro_circulo}.")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale.
segundos = int(input("Ingrese los segundos: "));
horas = segundos / 3600;
print(f"Los segundos equivalen a {horas} horas");

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número.
numero = int(input("Ingrese un número: "));
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}");

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("Ingrese el primer numero: "));
num2 = int(input("Ingrese el segundo numero: "));
suma = num1 + num2;
resta = num1 - num2;
multiplicacion = num1 * num2;
division = round(num1 / num2,2);
print(f"La suma de {num1} y {num2} es: {suma}");
print(f"La resta de {num1} y {num2} es: {resta}");
print(f"La multiplicacion de {num1} y {num2} es: {multiplicacion}");
print(f"La division de {num1} y {num2} es: {division}");

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
#modo: imc= peso en kg / (altura en m)2
altura = float(input("Ingrese su altura: "));
peso = float(input("Ingrese su peso: "));
masa_corporal = round(peso / altura ** 2,2)
print(f"Su índice de masa corporal es: {masa_corporal}");

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#fahrenheit = (celsius * 9/5) + 32
celsius = float(input("Ingrese la temperatura en grados Celsius: "));
fahrenheit = round((9/5)*celsius+32,2);
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}");
#print(f"{temperatura_celsius} °C equivalen a {temperatura_fahrenheit} °F.")

#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números.
num1 = float(input("Ingrese el primer numero: "));
num2 = float(input("Ingrese el segundo numero: "));
num3 = float(input("Ingrese el tercer numero: "));
promedio = round((num1 + num2 + num3) / 3,2);
print(f"El promedio de los tres números es: {promedio}");
