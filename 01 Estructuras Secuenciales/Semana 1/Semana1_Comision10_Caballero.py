#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  
print("Hola Mundo");

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
#realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ");
print(f"Hola {nombre}!");

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
division = num1 / num2;
print(f"La suma de {num1} y {num2} es: {suma}");
print(f"La resta de {num1} y {num2} es: {resta}");
print(f"La multiplicacion de {num1} y {num2} es: {multiplicacion}");
print(f"La division de {num1} y {num2} es: {division}");

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
#modo: imc= peso en kg / (altura en m)2
altura = float(input("Ingrese su altura: "));
peso = float(input("Ingrese su peso: "));
masa_corporal = peso / (altura ** 2);
print(f"Su índice de masa corporal es: {masa_corporal}");

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#fahrenheit = (celsius * 9/5) + 32
celsius = float(input("Ingrese la temperatura en grados Celsius: "));
fahrenheit = (celsius * 9/5) + 32;
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}");

#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números.
num1 = float(input("Ingrese el primer numero: "));
num2 = float(input("Ingrese el segundo numero: "));
num3 = float(input("Ingrese el tercer numero: "));
promedio = (num1 + num2 + num3) / 3;
print(f"El promedio de los tres números es: {promedio}");
